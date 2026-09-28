# NodeStyle

## NodeStyle

```
interface NodeStyle {
  id: `style-${NodeId}`
  type: NodeStyleType
  disable?: boolean
}
```

基础元素样式。 disable: 是否禁用，默认false。

## NodeStyleType

```
type NodeStyleType =
| 'VIEW'
| 'SVG'
| 'IMAGE'
| 'TEXT'
| 'INPUT'
| 'BUTTON'
| 'SCROLLVIEW'
```

节点转成的组件类型。

##

```
interface CssNodeStyle extends NodeStyle {
  name: string
  value: StyleSet
  layoutStyles: StyleSet
  attributes: Record<string, AttributeItem>
  inlineStyles?: StyleSet
  dynamicInlineStyles?: {
    [key in keyof StyleSet]: string
  }
  textStyles?: TextSegStyle[]
  classList?: ClassId[]
  tag?: 'IMG' | 'DIV' | 'TEXT' | 'BUTTON' | 'INPUT' | 'SLOT' | 'SVG' | 'OPTION'
  subSelectors?: Array<ClassStyle>
}
```

- `name`: `css类名`。
- `value`: 不包含 **布局样式** `css`的样式`map`，`key`为`kebab`形式，详见[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)。
- `layoutStyles`: 布局样式。属性包括

```
|'position'
|'flex-grow'
|'align-self'
|'flex-shrink'
|'top'
|'left'
|'bottom'
|'right'
|'width'
|'height'
|'transform'
|'transform-origin'
|'margin-left'
|'margin-top'
|'max-height'
|'max-width'
|'min-width'
|'min-height'
```
- `attributes`: `html`标签上的属性映射表，例如`disable`, `value`或一些框架的特殊语法，例如`Vue`的`v-for`, `@click`动态属性, `React`的一些绑定事件`onClick`这些。
- `inlineStyles`: 行内样式的`css`map，具体见[InlineStyle](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement/style)。
- `dynamicInlineStyles`: 动态绑定样式，类似于`Vue`的`:style`, `React`的`style=`。
- `textStyles`: 当文字有多段样式的时候,会被解析成多个文字标签,详见[TextSegStyle](/types/textSegStyle.html)。
- `tag`: 节点会被转换成的`dom`标签类型。
- `subSelectors`: 子选择器。

```
type TextSegStyle = {
  start: number
  end: number
  textStyleId: string
  textStyle: StyleSet
}
```

文字分段样式，区间左闭右开。 start: 文字的起始下标。 end: 文字的终止下标。

## ClassStyle

```
interface ClassStyle {
  id: ClassId
  name: string
  scoped: boolean
  value: StyleSet
  pseudo?: 'HOVER' | 'ACTIVE' | 'FOCUS' | 'DISABLED'
  type: 'group' | 'class' | 'pseudo' | 'id' | 'attribute' | 'combinators'
}
```

结构化css选择器样式,主要存在于全局样式或者节点样式的子选择器中。

- `id`: 样式id。
- `name`: 选择器名称。
- `scoped`: `css`是否仅作用在当前文件，防止`css`污染，默认为`true`。
- `value`: `css`样式的`map`,`key`为`kebab`形式，详见[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)。
- `pseudo`: 伪类类型，详见[pseudo](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-elements)。
- `type`: 选择器类型，详见[Selectors](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors)。

## AttributeItem

```
interface AttributeItem {
  type: Attribute
  name: string
  value: string
  valueType: 'STRING' | 'NUMBER' | 'BOOLEAN' | 'FUNCTION' | 'OBJECT' | 'ARRAY' | 'SLOT'
  valueSource?: 'PROPS' | 'METHODS' | 'DATA'
  defaultValue?: string | number | boolean
  expression?: string
  arguments?: string[]
}
type Attribute = 'STATIC' | 'DYNAMIC' | 'METHOD' | 'UNBIND'
```

dom标签上的属性。

- `type`: 属性类型。`STATIC`: 静态属性。
- `DYNAMIC`: 动态属性。
- `METHOD`: 方法属性。
- `UNBIND`: 定义但没有使用的属性类型, 会在[MGDSLFile](/devmode/types/mgdslfile.html)中定义，但不会使用。

- `name`: 属性名。
- `value`: 属性值或者对应的方法名称。
- `valueType`: 属性类型。`SLOT`: 插槽形式，在`Vue`中对应是`slot`,在React中对应是传给组件的`element`的`props`属性。

- `valueSource`: 属性来源，可以在该节点归属的[MGDSLFile](/devmode/types/mgdslfile.html)的对应数据中找到。 `PROP`: 在[MGDSLFile](/devmode/types/mgdslfile.html)的`props`中。 `METHOD`: 在[MGDSLFile](/devmode/types/mgdslfile.html)的`methods`中。 `DATA`: 在[MGDSLFile](/devmode/types/mgdslfile.html)的`data`中。
- `defaultValue`: 默认值。
- `expression`: 如果该属性是`METHOD`, 则`expression`是方法的内容。
- `arguments`: 如果该属性是`METHOD`, 则`arguments`是方法的传参。

NodeLayout