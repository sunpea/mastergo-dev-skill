#!/usr/bin/env python3
"""同步 developers.mastergo.com 全站文档到本地知识库 references/。

用法:
    python3 sync.py          增量同步（按 ETag，只重抓变化的）
    python3 sync.py --full   忽略 ETag，全量重抓
    python3 sync.py --dry    只探测有哪些页面变了，不落盘

注意: 站点 WAF 会拦截无 User-Agent 的请求，返回 HTTP 200 + 0 字节。
      必须带 UA，否则你会看到一堆空文件而不报错。
"""

import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

BASE = "https://developers.mastergo.com"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "references")
STATE_PATH = os.path.join(ROOT, "scripts", "sync-state.json")

FULL = "--full" in sys.argv
DRY = "--dry" in sys.argv


# ---------- 抓取 ----------

def fetch(path, etag=None):
    """返回 (body, etag, status)。304 时 body 为 None。"""
    url = BASE + path
    headers = {"User-Agent": UA, "Accept-Encoding": "identity"}
    if etag and not FULL:
        headers["If-None-Match"] = etag
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.read().decode("utf-8", "replace"), r.headers.get("ETag"), 200
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return None, etag, 304
        raise
    except Exception as e:
        print(f"  ! 抓取失败 {path}: {e}")
        return None, None, 0


def discover_pages():
    """从首页自愈发现 app.js，再抽取全站 sidebar 链接。

    不用递归爬：孤儿页会漏。VitePress 把全站 sidebar 打进了 app.js。
    app.js 文件名带 hash 会变，所以每次都从首页重新解析。
    """
    home, _, _ = fetch("/")
    if not home:
        sys.exit("首页抓取失败")
    m = re.search(r"/assets/app\.[0-9a-zA-Z]+\.js", home)
    if not m:
        sys.exit("未能在首页找到 app.js，站点结构可能已变更")
    appjs, _, _ = fetch(m.group(0))
    if not appjs:
        sys.exit("app.js 抓取失败")
    links = sorted(set(re.findall(r'"link":"(/[^"]+)"', appjs)))
    if not links:
        sys.exit("未能从 app.js 抽取到页面链接")
    return links


def url_to_key(link):
    """/apis/frameNode -> apis_framenode.md，用于查 __VP_HASH_MAP__。

    hash map 的 key 是源文件名（小写下划线），无法还原成真实 URL 的驼峰，
    所以清单仍走 app.js，hash map 只用来做变更检测。
    """
    p = link.strip("/")
    if not p:
        return "index.md"
    if link.endswith("/"):
        return p.replace("/", "_") + "_index.md"
    return p.replace("/", "_").lower() + ".md"


def fetch_hash_map():
    """抓首页拿全站源文件哈希。一次请求即可判断哪些页变了，不用逐页问。"""
    home, _, _ = fetch("/")
    if not home:
        return {}
    m = re.search(r'__VP_HASH_MAP__\s*=\s*JSON\.parse\("(.*?)"\)', home, re.S)
    if not m:
        return {}
    try:
        return json.loads(m.group(1).encode().decode("unicode_escape"))
    except Exception:
        return {}


# ---------- HTML -> Markdown ----------

def clean_inline(s):
    s = re.sub(r'<a[^>]*header-anchor[^>]*>.*?</a>', "", s, flags=re.S)
    s = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", s, flags=re.S)
    s = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", s, flags=re.S)
    s = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", s, flags=re.S)
    s = re.sub(r"<a[^>]*href=\"([^\"]*)\"[^>]*>(.*?)</a>", r"[\2](\1)", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def to_markdown(raw):
    """抽取 vp-doc 正文并转成 Markdown。代码块/表格用占位符保护，避免被标签清理破坏。"""
    m = (re.search(r'<div[^>]*class="[^"]*vp-doc[^"]*"[^>]*>(.*?)<footer', raw, re.S)
         or re.search(r"<main[^>]*>(.*?)</main>", raw, re.S))
    if not m:
        return ""
    body = m.group(1)
    body = re.sub(r"<(script|style|nav)\b.*?</\1>", "", body, flags=re.S)

    stash = []

    def stash_code(mo):
        lm = re.search(r'class="[^"]*language-([a-zA-Z0-9+#-]+)', mo.group(0))
        code = html.unescape(re.sub(r"<[^>]+>", "", mo.group(1)))
        stash.append("```" + (lm.group(1) if lm else "") + "\n" + code.strip() + "\n```")
        return f"\n\n@@S{len(stash)-1}@@\n\n"

    def stash_table(mo):
        rows, out = re.findall(r"<tr[^>]*>(.*?)</tr>", mo.group(0), re.S), []
        for i, r in enumerate(rows):
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)
            if not cells:
                continue
            cells = [clean_inline(c).replace("|", "\\|").replace("\n", " ") for c in cells]
            out.append("| " + " | ".join(cells) + " |")
            if i == 0:
                out.append("|" + "---|" * len(cells))
        stash.append("\n".join(out))
        return f"\n\n@@S{len(stash)-1}@@\n\n"

    body = re.sub(r"<pre[^>]*>(.*?)</pre>", stash_code, body, flags=re.S)
    body = re.sub(r"<table[^>]*>.*?</table>", stash_table, body, flags=re.S)

    # VitePress 提示框
    body = re.sub(r'<div[^>]*class="[^"]*custom-block[^"]*"[^>]*>', "\n\n> ", body)
    body = re.sub(r'<p[^>]*class="[^"]*custom-block-title[^"]*"[^>]*>(.*?)</p>',
                  lambda x: "> **" + clean_inline(x.group(1)) + "**\n> ", body, flags=re.S)

    body = re.sub(r"<(h[1-6])[^>]*>(.*?)</\1>",
                  lambda x: "\n\n" + "#" * int(x.group(1)[1]) + " "
                  + clean_inline(x.group(2)) + "\n", body, flags=re.S)
    body = re.sub(r"<li[^>]*>(.*?)</li>", lambda x: "\n- " + clean_inline(x.group(1)), body, flags=re.S)
    body = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>",
                  lambda x: "\n\n> " + clean_inline(x.group(1)) + "\n", body, flags=re.S)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</(p|div|tr|ul|ol|table|section|dt|dd)>", "\n", body)

    txt = html.unescape(re.sub(r"<[^>]+>", "", body))
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    for i, s in enumerate(stash):
        txt = txt.replace(f"@@S{i}@@", s)
    return txt


def out_path(link):
    """URL 路径 -> references/ 下的 md 路径。"""
    p = link.strip("/")
    if not p:
        return os.path.join(REF, "index.md")
    if link.endswith("/"):
        return os.path.join(REF, p, "_index.md")
    return os.path.join(REF, p + ".md")


# ---------- 索引 ----------

def build_index(files):
    """两级路由表：先读这个定位文件，再 Read 具体文件。"""
    groups = {}
    for link, path in files:
        rel = os.path.relpath(path, REF)
        sec = rel.split(os.sep)[0] if os.sep in rel else "(首页)"
        try:
            md = open(path, encoding="utf-8").read()
        except OSError:
            continue
        title = next((l.lstrip("# ").strip() for l in md.splitlines() if l.startswith("# ")), link)
        heads = [l.lstrip("#").strip() for l in md.splitlines()
                 if re.match(r"^#{2,3} ", l)][:8]
        groups.setdefault(sec, []).append((title, rel, heads))

    lines = [
        "# MasterGo 开发文档索引",
        "",
        "用法：先在本文件定位到目标文件，再 Read 那个文件。不要全量读 references/。",
        "",
        f"共 {len(files)} 页。",
        "",
    ]
    for sec in sorted(groups):
        lines.append(f"## {sec}/")
        for title, rel, heads in sorted(groups[sec], key=lambda x: x[1]):
            lines.append(f"- **{title}** — `{rel}`")
            if heads:
                lines.append("  - " + " · ".join(h for h in heads if h))
        lines.append("")
    return "\n".join(lines) + "\n"


# ---------- 主流程 ----------

def main():
    os.makedirs(REF, exist_ok=True)
    state = {}
    if os.path.exists(STATE_PATH) and not FULL:
        try:
            state = json.load(open(STATE_PATH, encoding="utf-8"))
        except Exception:
            state = {}

    print("发现页面清单...")
    links = discover_pages()
    hashes = fetch_hash_map()
    print(f"  共 {len(links)} 页 · hash map {len(hashes)} 条 · 模式 "
          f"{'全量' if FULL else '增量'}")

    changed, skipped, failed, files = [], [], [], []
    for i, link in enumerate(links, 1):
        path = out_path(link)
        prev = state.get(link, {})
        cur_hash = hashes.get(url_to_key(link))

        # 优先用源文件 hash 判断（一次请求即可定全站变更）；hash map 不可用时退回 ETag
        if not FULL and cur_hash and prev.get("hash") == cur_hash and os.path.exists(path):
            skipped.append(link)
            files.append((link, path))
            print(f"  [{i}/{len(links)}] = {link}")
            continue

        body, etag, st = fetch(link, prev.get("etag"))
        if st == 304 and os.path.exists(path):
            skipped.append(link)
            files.append((link, path))
            print(f"  [{i}/{len(links)}] = {link}")
            continue
        if not body:
            failed.append(link)
            continue
        md = to_markdown(body)
        if not md:
            print(f"  ! 未能提取正文: {link}")
            failed.append(link)
            continue
        if len(md) < 20:
            print(f"  ? 正文极短，请人工确认: {link} ({len(md)} 字符)")
        if not DRY:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(md)
        state[link] = {"hash": cur_hash, "etag": etag,
                       "bytes": len(md), "synced": time.strftime("%Y-%m-%d")}
        changed.append((link, len(md)))
        files.append((link, path))
        print(f"  [{i}/{len(links)}] + {link}  {len(md)//1024}KB")

    if not DRY:
        with open(STATE_PATH, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=1)
        idx = build_index(files)
        with open(os.path.join(REF, "API-INDEX.md"), "w", encoding="utf-8") as f:
            f.write(idx)
        total = sum(os.path.getsize(p) for _, p in files if os.path.exists(p))
        print(f"\n索引: references/API-INDEX.md  ({len(idx)//1024}KB)")
        print(f"知识库合计: {total/1024/1024:.2f} MB")

    print(f"\n更新 {len(changed)} · 未变 {len(skipped)} · 失败 {len(failed)}")
    if failed:
        print("失败页:")
        for l in failed:
            print("  -", l)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
