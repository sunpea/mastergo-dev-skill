# mastergo-dev skill

面向 Codex / WorkBuddy 的 MasterGo 开发者文档 skill。它用于查询 MasterGo 插件 API、TypeScript 类型、DevMode DSL、组件模板和 OpenAPI 文档，不用于直接操作设计稿。

## 内容

- `SKILL.md`：skill 的触发范围、使用方法和注意事项
- `references/API-INDEX.md`：本地文档总索引
- `references/`：MasterGo 开发者文档镜像
- `scripts/sync.py`：文档增量同步脚本
- `scripts/sync-state.json`：同步状态

## 安装

将仓库克隆到 Codex skill 目录：

```bash
git clone https://github.com/sunpea/mastergo-dev-skill.git ~/.codex/skills/mastergo-dev
```

也可以克隆到其他位置，再从 `~/.codex/skills/mastergo-dev` 建立软链接。

## 更新文档

```bash
python3 scripts/sync.py --dry
python3 scripts/sync.py
```

需要重新抓取全部页面时：

```bash
python3 scripts/sync.py --full
```

同步后请检查变更，再提交 `references/`、`references/API-INDEX.md` 和 `scripts/sync-state.json`。

## 使用约定

先读 `references/API-INDEX.md` 定位页面，再只打开当前问题相关的文档。在线文档可能随 MasterGo 宿主更新而变化，API 行为仍应在真实宿主中验证。

## 来源说明

`references/` 是从 [MasterGo 开发者平台](https://developers.mastergo.com/) 生成的本地文档镜像，原始文档及相关商标权利归其权利人所有。本仓库暂不附加开源许可证。
