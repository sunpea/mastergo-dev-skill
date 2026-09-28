---
name: mastergo-dev
description: MasterGo 开发者平台文档助手。当用户要写 MasterGo 插件、查 mg.* 插件 API 签名与参数、查 TypeScript 类型定义、写 DevMode DSL / 组件模板、调 MasterGo OpenAPI、或问「这个 API 怎么用 / 报这个错什么意思」时使用。提供的是文档知识，不是对设计稿的操作。
agent_created: true
---

# MasterGo 开发助手

`references/` 下是 [developers.mastergo.com](https://developers.mastergo.com/) 全站文档的本地镜像（109 页，0.72 MB，2026-09-03 同步）。写插件代码前先查这里，不要凭记忆编 API。

## 边界：本 skill 与 mastergo-local-api 的区别

两者触发词高度重叠，按下面规则分流：

| 用户要的是 | 走哪个 |
|---|---|
| 当前选中的图层、这份设计稿、导出前端代码、截图、导出变量 | `mastergo-local-api`（本机 127.0.0.1:30678，操作**运行中的设计稿**） |
| API 签名、参数含义、类型定义、怎么写、报错什么意思 | 本 skill（查**文档**） |

一句话：**操作设计稿用 local-api，写代码查文档用本 skill。**
两者可配合——先用 local-api 拿到图层结构，再按本 skill 的文档写处理代码。

## 检索方式：两级，别全量读

`references/` 有 100+ 个文件，全读会撑爆上下文。固定按两步走：

1. **先读 `references/API-INDEX.md`** —— 每行一个页面标题 + 路径 + 二级标题。用它定位文件。
2. **再 Read 那一个文件**，或按需 Grep：
   ```
   grep -rn "createFrame" ~/.workbuddy/skills/mastergo-dev/references/apis/
   ```

不要跳过第 1 步直接遍历目录。

## 目录结构

| 目录 | 内容 | 页数 |
|---|---|---|
| `apis/` | 插件 API：`mg.*` 全局对象、各节点类型（FrameNode/TextNode/ComponentNode…）、clientStorage、ui、viewport、websocket、variables | 30 |
| `types/` | TypeScript 类型：Paint、Effect、Font、Rect、Transform、Blend… | 34 |
| `devmode/` | DevMode：DSL 类型、组件模板（component / prop / slot / icon）、接入指南 | 18 |
| `guide/` | 入门：intro（插件运行机制）、setup（从零搭一个插件）、tutorials | 3 |
| `plugin-typings/` | 类型文件的安装与使用 | 2 |
| `rest-api/` | MasterGo OpenAPI（**内测态**，接口可能变动，用前提醒用户确认） | 1 |
| `updates/` | 更新日志，按日期命名。API 行为对不上文档时，来这里查变更 | 21 |

板块目录下的 `_index.md` 是该板块的索引页。

## 同步

文档会更新。用户问到没见过的新 API、或怀疑文档过时了，就跑一次：

```bash
python3 ~/.workbuddy/skills/mastergo-dev/scripts/sync.py          # 增量（按 ETag）
python3 ~/.workbuddy/skills/mastergo-dev/scripts/sync.py --full   # 全量重抓
python3 ~/.workbuddy/skills/mastergo-dev/scripts/sync.py --dry    # 只看哪些页变了
```

增量机制：站点每个页面都内嵌了 `__VP_HASH_MAP__`（全站源文件的构建哈希）。脚本抓一次首页就能知道哪几页变了，只重抓变化的页——无变更时几秒跑完，不用逐页问。页面清单则从首页重新解析 `app.js` 拿（hash map 的 key 是小写下划线文件名，还原不成真实 URL 的驼峰，不能当清单用），站点改版也能自愈。

## 几个坑

- **站点无版本选择器**，API 变更会直接覆盖线上文档。如果用户的代码突然报错，先查 `updates/`，再看 `sync-state.json` 里该页的上次同步时间。
- **`rest-api/` 是内测接口**，文档里标了「私有化」「Beta」「已废弃」标签，用前务必提醒用户核实。
- 文档里 `Readonly: true` 的属性不要写。节点类型会被设计师在设计工具里转换（Frame ↔ Group），插件若长期运行不要假设节点类型恒定。
