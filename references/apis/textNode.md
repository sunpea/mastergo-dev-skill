# TextNode

## Loading fonts
操作文本节点需要格外注意字体的加载，修改某些文本节点的属性或调用某些文本节点的方法时，要求必须确保相应的字体被正确地加载。通常您需要调用并等待 mg.loadFontAsync 函数执行成功后再对节点进行操作：

```
async function someActions() {
  // 等到字体加载成功
  await mg.loadFontAsync(fontName)
  // 然后再操作文本节点
  // ...
}
```

对于包含多个字体的文本图层，则需要等待所有字体加载完成：

```
async function someActions() {
  // 等待全部字体加载成功
  for (let { textStyle } of node.textStyles) {
    await mg.loadFontAsync(textStyle.fontName)
  }
  // 然后再操作节点
  // ...
}
```

## Missing fonts
Documentation coming soon...

## Text node properties

### `hasMissingFont`

- Readonly: `true`
- Type: `boolean`
返回一个布尔值，代表文本节点所使用的字体中，是否存在未加载的（或丢失的）字体。

### `textAlignHorizontal`

- Type: `'LEFT' | 'CENTER' | 'RIGHT' | 'JUSTIFIED'`
相对于文本框的水平对齐方式。设置该属性需要确保字体加载完成。

### `textAlignVertical`

- Type: `'TOP' | 'CENTER' | 'BOTTOM'`
相对于文本框的垂直对齐方式。设置该属性需要确保字体加载完成。

### `textAutoResize`

- Type: `'NONE' | 'WIDTH_AND_HEIGHT' | 'HEIGHT' | 'TRUNCATE' | 'TRUNCATE_AND_AUTO_WIDTH' | 'TRUNCATE_AND_AUTO_HEIGHT'`
定义文本框的尺寸调整以及如何适配文本框内文字的行为。设置该属性需要确保字体加载完成。

- `'NONE'`: 固定宽高，即文本框的尺寸是固定的（宽和高），无关其内容。
- `'HEIGHT'`: 自动高度，即文本框的宽度是固定的，且会包裹文本内容，其高度随着内容得变化进行适配。
- `'WIDTH_AND_HEIGHT'`: 单行模式，即文本框不会包裹其内容，文本框的宽高自动调整以适配其内容。
- `'TRUNCATE'`: 省略文本 + 固定宽高，即文本内容根据文本框大小自动换行，且超出文本框的内容将被裁切省略。
- `'TRUNCATE_AND_AUTO_WIDTH'`: 省略文本 + 单行模式，即结尾省略且文本框宽度自动调整以适配内容。
- `'TRUNCATE_AND_AUTO_HEIGHT'`: 省略文本 + 自动高度，即结尾省略且文本框高度随内容自动调整。

### `paragraphSpacing`

- Type: `number`
段落的垂直间距。设置该属性需要确保字体加载完成。

### `hyperlinks`
Type: hyperlinks: HyperlinkWithRange[], HyperlinkWithRange
获取文本节点的超链接数组。

### `superlinks`
Type: superlinks: { superlink: {layerId: string, link: string, linkFlag: string, pageId: string}, start: number, end: number }[]

> > **TIP**
> 已废弃，请改用hyperlinks.
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
- Type: [`ReadonlyArray`][TextListStyle](/types/textListStyle.html#TextListStyle)
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

### `setRangeFills`

- Type: `setRangeFills(start: number, end: number, paints: Paint[]): void`
设置文本节点中 [start, end) 范围内的字符的填充。

### `setRangeFillStyleId`
Type: setRangeFillStyleId(start: number, end: number, fillStyleId: string): void
为文本节点中 [start, end) 范围内的字符设置填充样式。

### `setRangeTextStyleId`
Type: setRangeTextStyleId:(start: number, end: number, styleId: string): void
为文本节点中 [start, end) 范围内的字符设置文字样式, 调用该方法需要确保字体加载完成。

### `setRangeTextCase`
Type: setRangeTextCase:(start: number, end: number, textCase: TextCase): void
为文本节点中 [start, end) 范围内的字符设置文字大小写TextCase, 调用该方法需要确保字体加载完成。

### `setRangeSuperLink`

- Type: `setRangeSuperLink(start: number, end: number, link: string | null): void`

> > **TIP**
> 已废弃,请改用setRangeHyperlink.
为文本节点中 [start, end) 范围内的字符设置超链接。当参数 link 的值为 null 时代表移除超链接。

### `setRangeListStyle`

- Type: `setRangeListStyle(start: number, end: number, value: ListType): void`[ListType](/types/textListStyle.html#TextListStyle)
为文本节点中 [start, end) 范围内的字符设置列表样式。当参数 value 的值为 none 时，取消设置列表样式。

## Base node properties

### `type`

- Readonly: `true`
- Type: `'TEXT'`
节点类型，对于 TextNode 节点来说，其值为字符串 'TextNode'。

### `clone`

- Type: `clone(): TextNode`
复制该文本节点。默认情况下，复制的新节点的父级节点为 mg.document.currentPage。

### `id`

- Readonly: `true`
- Type: `string`
TextNode 节点的 ID。

### `remove`

- Type: `remove():void`
将当前节点从parent节点中移除。

### `removed`

- Readonly: `true`
- Type: `boolean`
如果节点被移除了，则值为 true。如果插件保持运行状态，并且插件代码对某个节点存在引用，那么您应该始终检查节点的 removed 属性，在对节点进行操作之前先确保它没有被移除。

### `parent`

- Readonly: `true`
- Type: `(BaseNode & ChildrenMixin) | void`
获取当前节点的父节点。

### `name`

- Type: `string`
读取或设置节点的名字，即图层面板中所展示的图层名称。对于文字图层，其节点名字将随着文本内容自动更新。

### `getPluginData`

- Type: `getPluginData(key: string): string`
获取节点上存储自定义信息，对您的插件来说是私有的。如果要获取字符串以外的值类型，请先通过 JSON.parse 将其解码。

### `setPluginData`

- Type: `setPluginData(key: string, value: string): void`
允许您在任何节点上存储自定义信息，对您的插件来说是私有的。如果要存储字符串以外的值类型，请先通过 JSON.stringify 将其编码。

### `getPluginDataKeys`

- Type: `getPluginDataKeys(): string[]`
获取当前插件存储信息的所有键名。

### `removePluginData`

- Type: `removePluginData(key: string): void`
移除当前插件存储的自定义信息。

### `clearPluginData`

- Type: `clearPluginData(): void`
清除当前插件所有存储的自定义信息。

### `getSharedPluginData`

- Type: `getSharedPluginData(namespace: string, key: string): string`
获取存储在特定命名空间上的共享数据。

### `setSharedPluginData`

- Type: `setSharedPluginData(namespace: string, key: string, value: string): void`
这使您可以在任何节点上存储自定义信息。您可以稍后通过使用相同的命名空间和键调用 getSharedPluginData 来检索它。要查找存储在特定命名空间中的节点上的所有数据，请使用 getSharedPluginDataKeys。
您使用此 API 编写的任何数据都可以被任何插件读取。目的是允许插件相互操作。如果您不希望其他插件能够读取您的数据，请改用setPluginData。
您还必须提供命名空间参数以避免与其他插件的键冲突。此参数是强制性的，以防止多个插件使用通用键名（如数据）并相互覆盖。我们建议传递一个标识您的插件的值。可以将此命名空间提供给其他插件的作者，以便他们可以从您的插件中读取数据。

> > **WARNING**
> namespace用于标识您的插件并避免与其他插件发生键冲突的唯一字符串。命名空间必须至少包含 3 个字母数字字符。

### `getSharedPluginDataKeys`

- Type: `getSharedPluginDataKeys(namespace: string): string[]`
查找存储在特定命名空间中的节点上的所有数据的键名。

### `removeSharedPluginData`

- Type: `removeSharedPluginData(namespace: string, key: string): void`
移除存储在特定命名空间中的自定义信息。

### `clearSharedPluginData`

- Type: `clearSharedPluginData(namespace: string): void`
清除存储在特定命名空间上的所有数据。

> > **WARNING**
> 请谨慎调用此api，这样会导致其他人正在使用的共享的数据丢失。

## Scene node properties

### `isVisible`

- Type: `boolean`
节点是否可见。无论节点是否可见，都不影响插件对节点的访问。节点的 .isVisible 属性独立于它的父代节点。这意味着：即使该节点的 .isVisible === true，它也未必可见（父代节点中，任何一个节点不可见，那么该节点都不可见）。所以判断节点是否真的可见的正确方法是：确保该节点以及它的所有父代节点都满足条件 .isVisible === true。

### `isLocked`

- Type: `boolean`
节点是否被锁定。锁定的节点会组织用户在画布上对其进行特定的交互，例如拖动、选中图层。但无论图层节点是否被选中，都不影响插件代码对图层节点属性的读写操作。与判断节点是否可见的方式类似，判断节点是否真的被锁定正确方法是：只要该节点或任何一个它的父代节点满足条件 .isVisible === true，则认为该节点被锁定。

### `attachedConnectors`

- Readonly: `true`
- Type: [ConnectorNode[]](/apis/connectorNode.html)
吸附到节点的连接线节点数组。

### `componentPropertyReferences`

- Type: `componentPropertyReferences: { isVisible?: string, characters?: string, mainComponent?: string } | null`
此节点上附加的所有组件属性。仅当节点是组件子图层且未嵌套在实例节点中时，该节点才能具有组件属性引用。否则为空。键值对中的值是组件或组件集上的组件属性定义返回的组件属性id。

## Blend-related properties

### `opacity`

- Type: `number`
读取或设置图层的透明度，其值必须在 [0, 1] 区间。

### `blendMode`

- Type: [`BlendMode`](/types/blend.html)
图层的混合模式。

### `isMask`

- Type: `boolean`
图层是否是蒙版。

### `isMaskOutline`

- Type: `boolean`
图层是否是轮廓蒙版，值为false时为透明蒙层。只有当isMask为true时设置才能生效。

### `isMaskVisible`

- Type: `boolean`
图层是否显示蒙版。只有当isMask为true时设置才能生效，只有为轮廓蒙层的时候，才会在画布中显示蒙层。

### `effects`

- Type: `ReadonlyArray`, [Effect](/types/effect.html)
返回一个特效数组，具体数据结构可以查看 Effect。

### `effectStyleId`

- Type: `string`
当前节点所链接的特效样式的 id。即当前节点的 effects 属性所链接的 EffectStyle 对象的 id。

## Geometry-related properties

### `fills`

- Type: [`ReadonlyArray`](/types/paint.html)
图层的填充。

### `strokes`

- Type: [`ReadonlyArray`](/types/paint.html)
图层的描边。

### `strokeStyle`

- Type: `'SOLID' | 'DASH' | 'CUSTOM'`

### `strokeWeight`

- Type: `number`
描边的粗细，以像素为单位。必须是非负数，可以是小数。

### `strokeAlign`

- Type: `'CENTER' | 'INSIDE' | 'OUTSIDE'`
描边相对于图层边界的对齐方式。

- `'CENTER'`: 居中。
- `'INSIDE'`: 内部。
- `'OUTSIDE'`: 外部。

### `strokeCap`

- Type: `'NONE' | 'ROUND' | 'SQUARE' | 'LINE_ARROW' | 'TRIANGLE_ARROW' | 'ROUND_ARROW' | 'RING' | 'DIAMOND' | 'LINE'`
端点的装饰。

- `'NONE'`: 正常。
- `'ROUND'`: 圆角。
- `'SQUARE'`: 方型。
- `'LINE_ARROW'`: 普通箭头。
- `'TRIANGLE_ARROW'`: 三角箭头。
- `'ROUND_ARROW'` 圆箭头。
- `'RING'` 圆环。
- `'DIAMOND'` 方块。
- `'LINE'`直线。

### `strokeJoin`

- Type: `'MITER' | 'BEVEL' | 'ROUND'`
边角的装饰。

- `'MITER'`: 直角。
- `'BEVEL'`: 斜切。
- `'ROUND'`: 圆角。

### `strokeDashes`

- Type: `ReadonlyArray`
包含数字的数组。数组偶数下标元素代表虚线的长度，奇数下标元素代表虚线的间距。

### `dashCap`

- Type: `'NONE' | 'ROUND' | 'SQUARE'`
虚线端点装饰。

### `fillStyleId`

- Type: `string`
当前节点所链接的填充样式的 id。即当前节点的 fills 属性所链接的 PaintStyle 对象的 id。

### `strokeStyleId`

- Type: `string`
当前节点所链接的描边样式的 id。即当前节点的 strokes 属性所链接的 PaintStyle 对象的 id。

### `outlineStroke`

- Type: `() => TextNode | null`
该方法执行的动作与右键菜单中的“轮廓化”功能相同。如果该节点存在描边则该方法创建并返回描边的 TextNode 节点，否则返回 null。

> > **TIP**
> 注意：

- 在调用`outlineStroke`轮廓化后，layer的描边会被清除，也就是`strokes`会变成空数组。

## Layout-related properties

### `absoluteTransform`

- Type: [`Transform`](/types/transform.html)
图层节点相对于包含它的页面的位置，以变换矩阵的方式呈现。

### `relativeTransform`

- Type: [`Transform`](/types/transform.html)
图层节点相对于它的父级节点的位置，作为变换矩阵呈现。

### `absoluteBoundingBox`

- Readonly: `true`
- Type: [`Rect`](/types/rect.html)
图层节点相对于包含它的页面的位置，以Rect对象的方式呈现。

### `absoluteRenderBounds`

- Readonly: `true`
- Type: [`Rect | null`](/types/rect.html)
图层节点在画布中的实际渲染效果的定位和宽高，其值会受到该图层的旋转、填充、阴影、描边等效果影响，返回的坐标值为相对于画布的坐标，以Rect对象的方式呈现，当该图层不存在时，返回值为null。

### `x`

- Type: `number`
图层节点的位置，等价于 relativeTransform[0][2]。

### `y`

- Type: `number`
图层节点的位置，等价于 relativeTransform[1][2]。

### `bound`

- Type: [`Rect`](/types/rect.html)
图层节点的rect。

### `rotation`

- Type: `number`
图层节点的旋转角度。值域为 [-180, 180]。其值等价于：

```
Math.atan2(-relativeTransform[1][0], relativeTransform[0][0])
```

### `width`

- Type: `number`
图层节点的宽度。

### `height`

- Type: `number`
图层节点的高度。

### `maxWidth`

- Type: `number`
图层节点的最大宽度，该图层必须设置为自动布局或者是一个自动布局图层的直接子节点。

### `minWidth`

- Type: `number`
图层节点的最小宽度，该图层必须设置为自动布局或者是一个自动布局图层的直接子节点。

### `maxHeight`

- Type: `number`
图层节点的最大高度，该图层必须设置为自动布局或者是一个自动布局图层的直接子节点。

### `minHeight`

- Type: `number`
图层节点的最小高度，该图层必须设置为自动布局或者是一个自动布局图层的直接子节点。

### `flip`

- Type: `flip(direction: 'HORIZONTAL' | 'VERTICAL'): void`
翻转图层。

- `HORIZONTAL`: 水平翻转。
- `VERTICAL`: 垂直翻转。

### `resize`

- Type: `resize(width: number, height: number): void`
调整图层大小。同时设置图层的宽度和高度。

### `rescale`

- Type: `rescale(scale: number, scaleOption?: ScaleOption): void`

```
type ScaleCenter = 'TOPLEFT' | 'TOP' | 'TOPRIGHT' | 'LEFT' | 'CENTER' | 'RIGHT' | 'BOTTOMLEFT' | 'BOTTOM' | 'BOTTOMRIGHT'

interface ScaleOption {
  scaleCenter?: ScaleCenter
}
```

rescale方法用于等比缩放图层，且等比影响子图层的大小（width、height 或 fontSize）和相对定位，使其占百分比相等。
传入scale控制缩放系数，缩放后的宽高最小为0.01。设置scaleOption可设置缩放的行为，如设置scaleCenter控制缩放中心，默认为左上角TOPLEFT。

### `flexGrow`

- Type: `0 | 1`
该属性仅适用于采用自动布局的容器的直接子节点。代表该图层节点是否撑满容器的主轴，行为与 CSS 的 flex-grow 属性一致。

- `0`: 固定宽度。
- `1`: 充满容器。

### `alignSelf`

- Type: `"STRETCH" | "INHERIT"`
该属性仅适用于采用自动布局的容器的直接子节点。代表该图层节点是否撑满容器的交叉轴，行为与 CSS 的 align-self 属性一致。

- `"STRETCH"`: 撑满交叉轴。
- `"INHERIT"`: 固定高度。

### `layoutPositioning`

- Type: `"AUTO" | "ABSOLUTE"`
该属性仅适用于采用自动布局的容器的直接子节点。代表该图层节点的大小和位置是否通过自动布局设置或手动调整。

> > **TIP**
> 实例中的直接子节点始终为AUTO.

### `constraints`

- Type: [`Constraints`](/types/constraints.html)
图层约束。

> > **TIP**
> 该属性仅适用于采用非自动布局的容器的子节点。

### `constrainProportions`

- Type: `boolean`
锁定节点宽高比例。当为true时,修改节点的width或height会等比例修改height和width。

## Export-related properties

### `exportSettings`

- Type: [`ReadonlyArray`](/types/exportSettings.html)
节点的导出设置。

### `export`

- Type: `export(settings?: ExportSettings): Uint8Array | string`, [ExportSettings](/types/exportSettings.html)
将节点导出为对应的编码图片。如果是 SVG 格式，则返回字符串；否则返回 Uint8Array。

```
function exportImage() {
  const svgString = node.export({ format: 'SVG' })
  const uint8arr = node.export({ format: 'PNG' })
}
```

### `exportAsync`

- Type: `exportAsync(settings?: ExportSettings): Promise`, [ExportSettings](/types/exportSettings.html)
将节点异步导出为对应的编码图片。如果导出图层包含图片，该方法会加载原图，如果原图加载失败，会降级为预览图片。如果是 SVG 格式，则返回字符串；否则返回 Uint8Array。

```
async function exportImage() {
  const svgString = await node.exportAsync({ format: 'SVG' })
  const uint8arr = await node.exportAsync({ format: 'PNG' })
}
```

### `exportPng` 私有化

- Type: `exportPng(setting?: { filterIds?: string[], scale?: number }): string`
将节点导出为 PNG 图片，返回 base64 编码的 data URL 字符串（data:image/png;base64,...）。

- `filterIds`：要排除的子图层 ID 数组，排除的子图层不会被导出。默认为空数组。
- `scale`：缩放比例，默认为 `1`。

## Reaction prototyping-related properties

### `reactions`

- Type: [`Array`](/types/reaction.html)
获取或设置该节点设置的原型属性，若该图层没有任何以此为起点的原型交互，则返回空数组。每次设置原型属性都会将原有原型覆盖，若想清空该图层的所有原型，赋值空数组即可；若需要添加某原型交互，在原有原型数组上，添加完整的原型设置即可。

StarNode
TextSublayerNode