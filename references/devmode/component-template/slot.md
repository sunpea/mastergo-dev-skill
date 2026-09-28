# Slot
插槽数据。

## ComponentSlot

```
type ComponentSlot = {
  name: string
  relateNodeNames: (SlotMatchType | SlotMatchType[])[]
  ignoreClass?: boolean
} & ({type?: ''} | {
  type: 'TEXT'
} | {
  type: 'CUSTOM'
  getValue: GetValueType<'SLOT'>
})
```

- `name`: 插槽的名称。
- `relateNodeNames`: 关联的节点名称。
- `ignoreClass`: 默认`false`,是否忽略样式。
- `type`:`TEXT`: 纯文本
- `CUSTOM`: 自定义类型。 `getValue`: 返回[MGDSL](/devmode/types/mgdsldata.html)数据，id可为空。

## GetValueType
当一个属性值需要根据数据解析得来时，可以使用getValue来根据代码生成该值。

```
type GetValueType<T extends keyof ComponentPropType> = (nodeId: MGDSL.LayerId, nodeMap: Record<NodeId, MGDSL.MGNode>, componentId?: string) => {
  value: ComponentPropType[T] | undefined,
  nodeMap: Record<string, MGDSL.MGLayerNode>
}
```

Icon
Component prop