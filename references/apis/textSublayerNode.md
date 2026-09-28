# TextSublayerNode
文本子图层节点是文本节点的精简版本：它们具有大多数文本属性（除了对齐方式和尺寸调整方式，这些属性在这些节点的文本子图层上不可编辑）以及填充。它们不可调整大小或重新定位。
您可以像设置任何其他文本节点一样设置文本内容（例如，connector.text.characters=“一些文本”）。与Mastergo中的所有其他文本操作一样，您需要确保字体加载完成。

## Base Traits

### `id`

- Readonly: `true`
- Type: `string`
TextSublayerNode 节点的 ID。

## Text Traits

### `hasMissingFont`

- Readonly: `true`
- Type: `boolean`
返回一个布尔值，代表文本节点所使用的字体中，是否存在未加载的（或丢失的）字体。

### `textAlignHorizontal`

- Readonly: `true`
- Type: `'CENTER'`
相对于文本框的水平对齐方式。文本子图层的对齐方式固定为CENTER。

### `textAlignVertical`

- Readonly: `true`
- Type: `'CENTER'`
相对于文本框的垂直对齐方式。文本子图层的对齐方式固定为CENTER。

### `textAutoResize`

- Readonly: `true`
- Type: `'WIDTH_AND_HEIGHT'`
定义文本框的尺寸调整以及如何适配文本框内文字的行为。文本子图层的尺寸调整方式固定为WIDTH_AND_HEIGHT。

- `'WIDTH_AND_HEIGHT'`: 单行模式，即文本框不会包裹其内容，文本框的宽高自动调整以适配其内容。

### `paragraphSpacing`

- Type: `number`
段落的垂直间距。设置该属性需要确保字体加载完成。

### `hyperlinks`
Type: hyperlinks: HyperlinkWithRange[], HyperlinkWithRange
获取文本节点的超链接数组。

## Text content

### `characters`

- Type: `string`
文本节点的原始字符。设置该属性需要确保字体加载完成。

> > **TIP**
> 并非所有我们认为是字符的字符在 JavaScript 中都以单个字符存储。JavaScript 字符串采用 UTF-16 编码。某些字符（如👍)使用两个字符存储。在浏览器控制台中尝试一下：👍.length 实际是 2。这两个字符称为代理对。更有意思的是：有些字符由多个表情符号组成。例如，“👨‍👧”，我们应该在浏览器中将其视为单个字符，但其长度为 5。“👨‍👧”.substring（0， 2） 是 “👨”，“👨‍👧”.substring（3， 5） 是 “👧”。
由于部分组合字符（如部分emoji表情、有序列表和无序列表的标识符等），是由两个或多个Unicode组成，直接使用characters.length则无法获取正确的长度。在设置和获取分段填充样式或列表样式时，建议使用 Array.from(textNode.characters).length 获取正确的文字长度和位置。

### `insertCharacters`

- Type: `insertCharacters(start: number, characters: string): void`
在原文本的 start 位置处插入字符，文本中第一个字符的索引为 0。插入字符的样式将与该位置的前一个字符的样式保持一致。如果在第 0 个位置插入字符，由于该位置的前面没有其他字符，所以插入字符的样式将于该位置的后一个字符的样式一致。设置该属性需要确保字体加载完成。

### `deleteCharacters`

- Type: `deleteCharacters(start: number, end: number): void`
删除文本中出于位置 [start, end) 处的字符，文本中第一个字符的索引为 0。设置该属性需要确保字体加载完成。

## TextStyles

### `textStyles`

- Readonly: `true`
- Type: [`ReadonlyArray`](/types/textSegStyle.html)
文字图层节点的特点之一是：它可以在不同的范围内采用不同的字体、字号、填充、样式等等。文本节点会对其进行分段表示，可获得文本节点的所有分段的样式属性。
以如下文字图层节点为例：
文本节点的 textStyles 属性将会是包含三个元素的数组，数组元素的类型为 TextSegStyle：

### `listStyles`

- Readonly: `true`
- Type: [`ReadonlyArray`](/types/textSegStyle.html)
文字图层的 listStyles 属性表示文字的每一个段落是否设置了列表样式，其中 level 表示列表样式的缩进，当 level为 2 时，表示有2个缩进，为 0 时则表示没有缩进。

## Text range functions

### `setRangeFontSize`

- Type: `setRangeFontSize(start: number, end: number, fontSize: number): void`
设置文本节点中 [start, end) 范围内的字符的 fontSize。调用该方法需要确保字体加载完成。

### `setRangeFontName`

- Type: `setRangeFontName(start: number, end: number, {family: string, style: number}): void`
设置文本节点中 [start, end) 范围内的字符的 fontName。（注：fontName 即 family 与 style）。例子：

```
async function setFontName() {
  // 加载字体列表
  const fonts = await mg.listAvailableFontsAsync()
  // 选择一个字体
  const font = fonts[0]
  // 设置某个文本节点的 FontName
  textNode.setRangeFontName(0, 3, {font.fontName.family, font.fontName.style})
}
```

### `setRangeLetterSpacing`

- Type: `setRangeLetterSpacing(start: number, end: number, value: LetterSpacing): void`, [LetterSpacing](/types/textSegStyle.html)
设置文本节点中 [start, end) 范围内的字间距。调用该方法需要确保字体加载完成。

### `setRangeLineHeight`

- Type: `setRangeLineHeight(start: number, end: number, value: LineHeight): void`, [LineHeight](/types/textSegStyle.html)
设置文本节点中 [start, end) 范围内的字符的行高。调用该方法需要确保字体加载完成。

### `setRangeTextDecoration`

- Type: `setRangeTextDecoration(start: number, end: number, paints: 'NONE' | 'UNDERLINE' | 'STRIKETHROUGH'): void`
设置文本节点中[start, end)范围内的字符的装饰。调用该方法需要确保字体加载完成。

### `setRangeHyperlink`

- Type: `setRangeHyperlink(start: number, end: number, hyperlink?: Hyperlink)`, [Hyperlink](/types/hyperlink.html)
为文本节点中 [start, end) 范围内的字符设置超链接。当参数 hyperlink 的值为 null 时代表移除超链接。

### `setRangeTextCase`
Type: setRangeTextCase:(start: number, end: number, textCase: TextCase): void
为文本节点中 [start, end) 范围内的字符设置文字大小写TextCase, 调用该方法需要确保字体加载完成。

### `setRangeFills`

- Type: `setRangeFills(start: number, end: number, paints: Paint[]): void`
设置文本节点中 [start, end) 范围内的字符的填充。

### `setRangeListStyle`

- Type: `setRangeListStyle(start: number, end: number, value: ListType): void`
为文本节点中 [start, end) 范围内的字符设置列表样式。当参数 value 的值为 none 时，取消设置列表样式。

### `setRangeFillStyleId`
Type: setRangeFillStyleId(start: number, end: number, fillStyleId: string): void
为文本节点中 [start, end) 范围内的字符设置填充样式。

### `setRangeTextStyleId`
Type: setRangeTextStyleId:(start: number, end: number, styleId: string): void
为文本节点中 [start, end) 范围内的字符设置文字样式, 调用该方法需要确保字体加载完成。

### `fills`

- Type: [`ReadonlyArray`](/types/paint.html)
图层的填充。

### `fillStyleId`

- Type: `string`
当前节点所链接的填充样式的 id。即当前节点的 fills 属性所链接的 PaintStyle 对象的 id。

TextNode