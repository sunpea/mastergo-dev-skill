# MGDSLData

## MGDSLData

```
interface MGDSLData {
  readonly version: string
  framework: Framework
  readonly nodeMap: Record<NodeId, MGNode>
  readonly localStyleMap: StyleMap
  readonly fileMap: Record<FileId, MGDSLFile>
  root: MGLayerNode
  entry: FileId
  settings: DSLSettings
  importPath: ImportPath
  importType: 'GLOBAL' | 'IMPORT'
}
```

- `version`: dsl版本号。
- `framework`: dsl的框架类型，默认`VUE3`。
- `nodeMap`: 所有 [MGNode](/devmode/types/mgnode.html) 的映射表。
- `localStyleMap`: 自定义样式的映射表。
- `fileMap`: 虚拟文件[MGDSLFile](/devmode/types/mgdslfile.html)映射表。
- `root`: 入口节点。
- `entry`: 入口[MGDSLFile](/devmode/types/mgdslfile.html)的`id`。
- `settings`: `DSL`[配置项](/devmode/types/dslsettings.html)。
- `importPath`: 导入[模板文件](/devmode/component-template/component-template.html)路径配置。
- `importType`: [模板文件](/devmode/component-template/component-template.html)引入方式。 `GLOBAL`: 全局方式引入。
- `IMPORT`: `esModule`方式引入。

## JSDSLData

```
interface JSDSLData extends MGDSLData{
  /**
   * 全局样式表
   */
  globalStyleMap: {
    [classId: string]: ClassStyle
  }
}
interface ReactDSLData extends JSDSLData {
  readonly framework: 'REACT'
}
interface Vue3DSLData extends JSDSLData {
  readonly framework: 'VUE3'
}
interface Vue2DSLData extends JSDSLData {
  readonly framework: 'VUE2'
}
```

## AndroidDSLData

```
interface AndroidDSLData extends MGDSLData {
  readonly framework: 'ANDROID'
}
```

## IOSDSLData

```
interface IOSDSLData extends MGDSLData {
  readonly framework: 'IOS'
}
```

## Framework

```
type Framework = 'REACT' | 'VUE2' | 'VUE3' | 'ANDROID' | 'IOS'
```

## NodeId

```
type NodeId = LayerId | OperationId
type LayerId = string
type OperationId = string
```

## StyleMap

```
type StyleMap = {
  [styleId: string]: TokenItem | AndroidStyleItem
}
```

- `TokenItem`: 详见[Token](/devmode/types/token.html)
- `AndroidStyleItem`: `any`

## FileId

```
type FileId = string
```

- `FileId`: 文件id。

## ImportPath

```
type ImportPath = {
  name: string
  path: string
  type: 'script' | 'style'
}[]
```

- `script`: 脚本。
- `style` 样式。

简介
MGNode