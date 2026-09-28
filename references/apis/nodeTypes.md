# Node Types
在 教程-节点类型 中曾介绍过，MasterGo 文件是由节点树构成的。每个节点都与特定的图层对应，用来描述图层信息。不同类型的节点对象拥有不同的属性集合，用于描述不同类型的图层。下面给出 MasterGo 中的所有图层节点的类型：

- [DocumentNode](./documentNode.html)
- [PageNode](./pageNode.html)
- [BooleanOperationNode](./booleanOperationNode.html)
- [ComponentNode](./componentNode.html)
- [ComponentSetNode](./componentSetNode.html)
- [ConnectorNode](./connectorNode.html)
- [EllipseNode](./ellipseNode.html)
- [FrameNode](./frameNode.html)
- [GroupNode](./groupNode.html)
- [InstanceNode](./instanceNode.html)
- [LineNode](./lineNode.html)
- [PenNode](./penNode.html)
- [PolygonNode](./polygonNode.html)
- [RectangleNode](./rectangleNode.html)
- [SliceNode](./sliceNode.html)
- [StarNode](./starNode.html)
- [SectionNode](./sectionNode.html)
- [IntelligentContainerNode](./intelligentContainerNode.html)
- [TextNode](./textNode.html)
- [TextSublayerNode](./textSublayerNode.html)
在 @mastergo/plugin-typings 的类型文件中，每个类型的节点都对应了一个 interface。另外，你可能已经注意到了，我们在前文中使用了 BaseNode 以及 SceneNode 这两个类型进行接口类型的描述。下面是 BaseNode 类型和 SceneNode 类型的定义：

```
type BaseNode = DocumentNode | PageNode | SceneNode

type SceneNode =
  | GroupNode
  | FrameNode
  | PenNode
  | StarNode
  | LineNode
  | EllipseNode
  | PolygonNode
  | RectangleNode
  | TextNode
  | ComponentNode
  | ComponentSetNode
  | InstanceNode
  | BooleanOperationNode
  | SliceNode
  | ConnectorNode
  | SectionNode
  | IntelligentContainerNode
```

大多数情况下，插件都在操作 SceneNode。可以把 SceneNode 理解为包含在页面中的图层节点类型。

mastergo.codegen
BooleanOperationNode