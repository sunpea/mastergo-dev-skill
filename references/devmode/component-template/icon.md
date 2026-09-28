# Icon

## Icon

```
type Icons = {
  reg: RegExpString
  getValue: (node: MGDSL.MGLayerNode) => MGDSL.MGCustomNode
}
```

- `reg`: 组件名正则。
- `getValue`: 根据[MGLayerNode](/devmode/types/mgnode.html#mglayernode)转换成[MGCustomNode](/devmode/types/mgnode.html#mgcustomnode)。

Component
Slot