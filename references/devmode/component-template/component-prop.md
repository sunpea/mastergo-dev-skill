# Component Prop

```
type ComponentPropString = ComponentPropItem<'STRING'> & {
  nodePath?: SlotMatchType[],
}
type ComponentPropNumber = ComponentPropItem<'NUMBER'>
type ComponentPropBoolean = ComponentPropItem<'BOOLEAN'>
type ComponentPropFunction = ComponentPropItem<'FUNCTION'>
type ComponentPropObject = ComponentPropItem<'OBJECT'>
type ComponentPropArray = ComponentPropItem<'ARRAY'>
type ComponentPropInstance = ComponentPropItem<'SLOT'> & {
  nodePath?: SlotMatchType[],
  ignoreClass?: boolean,
}
type ComponentProp = ComponentPropString | ComponentPropNumber | ComponentPropBoolean | ComponentPropFunction | ComponentPropObject | ComponentPropArray | ComponentPropInstance
```

- `nodePath`: `React`的`INSTANCE`视为`Vue`的`SLOT`效果，故这里提供`nodePath`属性，继续遍历图层并以此图层为属性内容。
- `ignoreClass`: 忽略样式表，默认`false`。

## ComponentPropItem

```
type ComponentPropItem<T extends keyof ComponentPropType> = {
  type: T
  defaultValue?: ComponentPropType[T]
  getValue?: GetValueType<T>
  name: string
  aliasName?: string
  originalName?: string
  aliasMap?: Record<string, ComponentPropType[T] | undefined>
  dsmAlias?: Record<string, string>
  lowerCase?: boolean
  visible?: {
    aliasName: string
    aliasMap?: Record<string, boolean>
  },
}
```

组件属性元素。

- `type`: 类型。
- `defaultValue`: 默认值，也可作为初始值使用。
- `getValue`: 不适合在配置模板中使用，请尽量少的使用该函数。
- `aliasName`: 属性别名。
- `originalName`: 原始名称,区别于经过处理的`name`。
- `name`: 属性名，根据`aliasName`和`originalName`经过处理后的名称，用于最终的展示。
- `aliasMap`: 属性枚举值对应关系。一般和`aliasName`配合使用，根据画布图层的属性值，映射到代码中的属性值。
- `dsmAlias`: `DSM`属性枚举值对应关系。
- `lowerCase`: 组件库解析时，是否将大写属性值转换为小写。
- `visible`: 是否应用该属性。 `aliasName`: 画布图层属性名，当前当前仅支持属性名的判断。
- `aliasMap`: 画布图层属性值的映射。

Slot