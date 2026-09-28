# ComponentTemplate

```
type ComponentTemplate = {
  documentId: string
  name: string
  importType: 'GLOBAL' | 'IMPORT'
  importPath: {
    name: string
    importName: string
    path: string
    type: 'script' | 'style'
  }[]
  framework: 'VUE2' | 'VUE3' | 'REACT'
  components: ComponentItem[]
  icons?: Icons
}
```

- `documentId`: 文件`id`。
- `name`: 模板名称，全局唯一。
- `importType`: 组件导入类型。 `GLOBAL`: 全局引入。
- `IMPORT`: `esm`引入。

- `importPath`: 导入模板文件路径配置。
- `importType`: 模板文件引入方式。 `GLOBAL`: 全局方式引入。
- `IMPORT`: `esModule`方式引入。

- `framework`: 模板框架，支持`'VUE2' | 'VUE3' | 'REACT'`。
- `components`: 包含的组件列表，详见[Component](/devmode/component-template/component.html)。
- `icons`: 图标库，详见[Icon](/devmode/component-template/icon.html)。

开发指南
Component