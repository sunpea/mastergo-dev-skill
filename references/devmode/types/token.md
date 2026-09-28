# Token
Token是由画布内自定义样式转化而来的一种以变量的形式存在的标识。

##

## TokenCommonItem

```
type TokenItem = TokenCommonItem | TokenTextItem
type TokenCommonItem = {
  id: string
  type:
  | 'color'
  | 'padding'
  | 'border-radius'
  | 'border-width'
  | 'gap'
  name: TokenName
  value: TokenValue
  isMultiple?: boolean
}
type TokenName = string
type TokenValue = StyleSet[keyof StyleSet]
```

通用token。

- `id`: `token`id， 对应的是画布的[自定义样式](/types/style.html)的`id`。
- `type`: 自定义样式类型。 `color`: 颜色样式。
- `padding`: 边距样式。
- `border-radius`: 圆角样式。
- `border-width`: 描边粗细样式。
- `gap`: 间距样式。

- `name`: `token`名称，优先取`alias`，没有则使用原本样式名。
- `value`: `token`的具体值。
- `isMultiple`: 是否是多段样式, 暂不支持多段样式的应用。

##

```
type TokenTextItem = {
  id: string
  type: 'text'
  name: TokenName
  textItems: Record<TokenTextSubItemType, TokenTextSubItem>
}
```

文字token。由于文字样式的内容映射到代码中上是多个文字属性，所以文字会以多种子token形式存在。

- `id`: 文字样式的`id`。
- `type`: 类型为`text`。
- `name`: `token`名称，优先取`alias`，没有则使用原本样式名。
- `textItems`: 文字样式子样式映射。

## TokenTextSubItem

```
type TokenTextSubItemType =
| 'fontfamily'
| 'fontstyle'
| 'fontsize'
| 'lineheight'
| 'decoration'
| 'letterspacing'

type TokenTextSubItem = {
  type: TokenTextSubItemType
  name: TokenName
  value: TokenValue
}
```

文字的分类token。

- `type`: `fontfamily`: 字族。
- `fontstyle`: 字形。
- `fontsize`: 字号。
- `lineheight`: 行高。
- `decoration`: 装饰符。
- `letterspacing`: 字间距。

- `name`: `token`名称，以其类型为前缀。
- `value`: `token`值。

##

```
type StyleMap = {
  [styleId: string]: TokenItem
}
```

MGDSLFile
DSLSetting