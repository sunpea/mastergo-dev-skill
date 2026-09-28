# MGNode

## MGNode

```
type MGNode = MGLayerNode | MGOperationNode
```

## MGLayerNode

```
interface MGLayerNode {
  type: 'LAYER'
  id: LayerId
  children: NodeId[]
  name: string
  /**
   * 图层在代码中的组件名
   */
  componentName: string
  /**
   * 图层实际类型名称 RECTANGLE TEXT FRAME...
   */
  layerType: NodeType
  // 是否是蒙版
  isMask: boolean
  // 是否隐藏
  isVisible: boolean
  layout: NodeLayout
  style: CssNodeStyle | IOSNodeStyle | AndroidNodeStyle
  /**
   * 是否是根元素
   */
  isRoot: boolean
  parent?: NodeId
  /**
   * 关联的文件
   */
  relatedFile: FileId
  /**
   * 是否拆分成新文件,默认false
   */
  isNewFile?: boolean
}
```

通用节点图层，为画布实际存在节点。

- `type`: `Layer`, 图层类型。
- `id`: 图层id，具体为画布中的节点`id`。
- `name`: 图层名称，**组件集子组件的名称跟随组件集名称**。
- `children`: 子图层`id`数组, 具体数据可以根据`id`在`nodeMap`中查询。
- `componentName`: 转换后组件名称。
- `layerType`: 图层类型，详见
- `isMask`: 是否是蒙板。
- `isVisible`: 是否隐藏。
- `layout`: 布局信息，详见[Layout](/devmode/types/nodelayout.html)
- `style`: 样式信息, 详见[NodeStyle](/devmode/types/nodestyle.html)
- `isRoot`: 是否是根节点。
- `parent`: 父节点id。
- `relatedFile`: 关联文件id。
- `isNewFile`: 是否单独分出一个新文件，为`true`时则会以该节点为组件创建一个新的[MGDSLFile](/devmode/types/mgdslfile.html)。

## MGComponentNode

```
interface MGComponentNode extends MGLayerNode {
  layerType: 'COMPONENT'
  alias: string
  /**
   * 是组件集子组件的话则存在
   */
  componentSetId?: string
}
```

组件节点，详见ComponentNode。

- `alias`: 组件别名。
- `componentSetId`: 组件集`id`, 仅为组件集子组件时有值。

## MGInstanceNode

```
interface MGInstanceNode extends MGLayerNode {
  layerType: 'INSTANCE'
  /**
   * 实例的主组件Layer, 这里不开通用模型就不解析
   */
  mainComponent?: LayerId
}
```

实例节点，详见InstanceNode

- `mainComponent`: 实例主组件`id`。

## MGCustomNode

```
interface MGCustomNode extends MGLayerNode {
  layerType: 'CUSTOM'
  tagName?: string
  props?: ComponentProp[]
  imports: ImportItem[]
}
```

dsl自定义节点。

- `tagName`: 标签名或组件类名。
- `props`: 组件属性，详见[ComponentProp](/devmode/component-template/component-prop.html)。
- `imports`: 文件头部引入的内容, 详见[ImportItem](/devmode/types/mgdslfile.html#importitem)。

## MGTextNode

```
interface MGTextNode extends MGLayerNode {
  characters: string
}
```

文字节点，详见TextNode。

- `characters`: 文字内容。

## NodeType

```
type NodeType =
  | 'GROUP'
  | 'FRAME'
  | 'RECTANGLE'
  | 'TEXT'
  | 'LINE'
  | 'ELLIPSE'
  | 'POLYGON'
  | 'STAR'
  | 'PEN'
  | 'COMPONENT'
  | 'COMPONENTSET'
  | 'INSTANCE'
  | 'BOOLEANOPERATION'
  | 'SLICE'
  | 'CONNECTOR'
  | 'SECTION'
  | 'CUSTOM'
```

图层详情详见NodeType。

- `CUSTOM`: 自定义节点类型。

## MGOperationNode

```
type MGOperationNode = IfStatement | Iteration | Raw | TernaryExpression
```

## IfStatement

```
interface IfStatement {
  id: OperationId
  type: 'OPERATION'
  operationType: 'If_STATEMENT'
  // 表达式
  condition: string
  consequent: {
    type: 'MGNode' | 'EXPRESSION'
    body: MGNode | string
  }
  alternate: {
    type: 'MGNode' | 'EXPRESSION'
    body: MGNode | string
  }
}
```

条件运算。

- `condition`: 条件表达式，会被包裹进`if`判断语句内。
- `consequent`: `true`分支。
- `alternate`: `false`分支。 `type`: 内容类型。
- `body`: 分支内的内容，可以是`MGNode`或者`plain text`

## Iteration

```
interface Iteration {
  id: OperationId
  type: 'OPERATION'
  operationType: 'ITERATOR'
  // 迭代器的变量名
  variable: string
  body: MGNode
  // 作为key的变量名，属于迭代变量中元素上的字段
  key?: string
}
```

迭代。

- `variable`: 参与迭代的变量。
- `body`: 迭代器中的内容, 类型为`MGNode`。
- `key`: 类似于`vue`和`react`中的`key`，用来标识唯一性。

## TernaryExpression

```
interface TernaryExpression {
  id: OperationId
  type: 'OPERATION'
  operationType: 'TERNARY_EXPRESSION'
  condition: string
  trueExpression: {
    type: 'MGNode' | 'EXPRESSION'
    body: MGNode | string
  }
  falseExpression: {
    type: 'MGNode' | 'EXPRESSION'
    body: MGNode | string
  }
}
```

三目运算。

- `condition`: 条件表达式，会被包裹进`if`判断语句内。
- `trueExpression`: `true`分支。
- `falseExpression`: `false`分支。

## Raw

```
interface Raw {
  id: OperationId
  type: 'OPERATION'
  operationType: 'RAW'
  body: string
}
```

原始字符串,原始字符串会直接被加入进最后生成的代码中，参与代码生成，原则上可以是任何可以运行的plain text。

MGDSL
MGDSLFile