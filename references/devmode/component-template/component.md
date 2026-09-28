# Component

```
type ComponentItem = ComponentOrigin & { id: string; matchName?: string; }

type ComponentOrigin = {
  name: string
  props: ComponentProp[]
  source: ComponentSource
  slots?: ComponentSlot[]
  ignoreRect?: boolean
}
```

- `name`: 组件名称。
- `props`: 组件的被透传的属性, 详见[ComponentProp](/devmode/component-template/component-prop.html)。
- `source`: 组件的来源，以虚拟路径形式表达。
- `slots`: 组件的插槽,类似于`Vue`的具名插槽[Slot](https://cn.vuejs.org/guide/components/slots.html)和`React`组件中的传递`jsx`来当做[chilren](https://react.dev/learn/passing-props-to-a-component)，详见[Slot](/devmode/component-template/slot.html)。
- `ignoreRect`: 忽略布局信息,默认`false`。

##

```
type ComponentSource = {
  path: string
  export: 'DEFAULT' | string
}
```

- `path`: 组件的虚拟路径,如：'@/components/xxx.vue'。
- `export``DEFAULT`: `export default {} 为 DEFAULT`。
- `string`: `export const xxx = {} 为 xxx`。

Component Template
Icon