# mg
下面给出的属性和方法可以通过全局对象 mg 来访问。

## 属性

### `apiVersion`

- Readonly: `true`
- Type: `string`
运行插件的 MasterGo API 版本号，即定义在 manifest.json 中的 api 字段的值。

### `document`

- Readonly: `true`
- Type: `DocumentNode`
MasterGo 文档的根节点，可以通过它来访问其他页面节点，或查找子代节点。例如，可以通过 document.currentPage 来访问当前页面节点。

### `documentId`

- Readonly: `true`
- Type: `number`
当前文档的 ID。

### `command`

- Readonly: `true`
- Type: `string`
当前运行的command值， 当以子菜单为入口运行插件时，其值为子菜单的command。默认为空串。

### `mixed`

- Readonly: `true`
- Type: `string | symbol`
混合标记。如矩形图层的cornerRadius属性，若设置了单个角的圆角，则cornerRadius的值为mg.mixed。

> > **TIP**
> 注意：不建议使用字面量代替mg.mixed进行开发，特别是当其类型为symbol时。

### `ui`

- Readonly: `true`
- Type:

```
interface UIAPI {
  show(): void;
  hide(): void;
  close(): void;

  postMessage(pluginMessage: any, options?: UIPostMessageOptions): void;
  onmessage:
    | ((pluginMessage: any, props: OnMessageProperties) => void)
    | undefined;
}
```

该属性是一个对象，包含了用来操作用户界面并与用户界面进行信息交流的接口。详情请查看 mg.ui。

### `themeColor`

- Readonly: `true`
- Type: `'dark' | 'light'`
Master Go 系统的主题色, 值为 dark 或 light

### `viewport`

- Readonly: `true`
- Type:

```
interface ViewportAPI {
  center: Vector;
  zoom: number;
  readonly bounds: Rect;
}
```

该属性是一个对象，可以用来读取或设置当前页面的用户可视区（即画布的可见区域）。详情请查看 mg.viewport。

### `clientStorage`

- Readonly: `true`
- Type: ClientStorageAPI

```
interface ClientStorageAPI {
  getAsync(key: string): Promise<any | undefined>
  setAsync(key: string, value: any): Promise<void>
  keysAsync(): Promise<string[]>
  deleteAsync(key: string): Promise<void>
}
```

该属性是一个对象，包含了用来在用户机器上完成数据本地持久化存储的方法。详情请查看 mg.clientStorage。

### `currentUser`

- Readonly: `true`
- Type: [User](/types/user.html) | null
该属性是一个对象，包含了当前用户的相关信息，需要在manifest.json中设置permissions。

### `codegen`

- Readonly: `true`
- Type: [CodegenAPI](/apis/codegen.html) | null
该属性是一个对象，包含了研发模式代码生成相关的模块。详情请查看 mg.codegen。

### `variables`

- Readonly: `true`
- Type: VariablesAPI
该属性是一个对象，包含了变量管理相关的模块，用于管理设计变量（Design Variables）的集合、模式、分组、创建、绑定等。详情请查看 mg.variables。

## 方法

### `showUI`

- Type:

```
showUI(HTMLString: string, options?: ShowUIOptions): void
type ShowUIOptions = {
  width?: number
  height?: number
  visible?: boolean
  x?: number | string
  y?: number | string
  withoutHeader?: boolean
  headerVisible?: boolean // 私有化特有
  style?: Record<string, string> // 私有化特有
}
```

用来展示插件的用户界面，调用该方法会创建一个模态框。该模态框中会包含 <iframe> 标签，并加载HTMLString中指定的html字符串。
第一个参数可传入__html__加载ui代码，或者传入其他html代码。__html__ 为全局变量，类型为string，该值由 manifest.json 中指定的 ui 字段所引用的文件内容。
可通过options设置ui窗口的属性，类型为ShowUIOptions。

- `'width'` ：`ui`窗口宽度，类型为`number`，默认为400。
- `'height'` ：`ui`窗口高度，类型为`number`，默认为600。该高度包括标题区域。
- `'visible'` ：控制窗口是否可视，类型为`boolean`，默认为true。
- `'x'` ：`ui`窗口横向定位，可传入具体的像素量(`number`)或百分比(`string`)。默认定位为画布右上角。
- `'y'` ：`ui`窗口纵向定位，可传入具体的像素量(`number`)或百分比(`string`)。默认定位为画布右上角。
- `withoutHeader` ：如果 `withoutHeader` 参数为 `true`，则 UI 界面的高度将不包含插件头部的高度。默认值为 `false`。
- `headerVisible` 私有化：如果 `headerVisible` 参数为 `false`，则 UI 界面的头部将不可见。默认值为 `true`。
- `style` 私有化：自定义 UI 界面的样式，类型为 `Record`。默认值为空对象。

### `closePlugin`

- Type: `closePlugin(): void`
用来关闭由 showUI 创建的模态框，一旦关闭插件，所有的定时器或请求动画帧都将被清除或取消。

### `on`

- Type:

```
on(type: PluginEventType, callback: CallableFunction): void
type PluginEventType = 'selectionchange' | 'layoutchange' | 'close' | 'currentpagechange' | 'themechange' | 'drop' | 'run'
interface DropEvent {
  x: number // 相对于画布左上角的页面定位x坐标
  y: number // 相对于画布左上角的页面定位y坐标
  absoluteX: number // 画布内x坐标
  absoluteY: number // 画布内y坐标
  dropMetadata?: any // 来源于插件ui传输的原始数据，不会做任何处理。
}
```

on 方法允许注册特定事件的处理函数，当事件发生时会执行该回调函数：

- `'selectionchange'` 事件：当 `currentPage.selection` 变化时触发。回调参数为 `string[]`。
- `'currentpagechange'` 事件：当切换页面时触发，或插件修改 `mg.document.currentPage` 属性时触发。 回调参数为 `string` 。
- `'layoutchange'` 事件：当页面尺寸发生改变时触发，包括浏览器窗口尺寸、画布尺寸、左右侧面板尺寸。
- `'close'` 事件：当调用 `closePlugin` 函数时，或用户通过插件 UI 的关闭按钮关闭插件时触发。无回调参数 。
- `'themechange'`事件，当画布主题切换时触发。 回调参数为 `'dark' | 'light'`。
- `'drop'`事件，当页面外文件等元素拖拽进入画布触发，或由插件[ui侧触发drop事件](/guide/tutorials.html#ui侧触发drop事件)。回调参数为`DropEvent`。
- `'run'`事件，当插件运行时触发，会晚于主线程的代码执行，回调参数为所选中[子菜单](/guide/setup.html#manifest-json)的command值，与 [mg.command](/apis/mastergo.html#command) 相同，默认为空串。回调参数为`{command: string}`。

### `once`

- Type:

```
once(type: PluginEventType, callback: CallableFunction): void
type PluginEventType = 'selectionchange' | 'layoutchange' | 'close' | 'currentpagechange' | 'themechange' | 'drop' | 'run'
```

once 方法允许注册特定事件的处理函数，当事件发生时会执行该回调函数。与 on 函数的区别在于，通过 once 函数注册的事件处理函数只会执行一次。

### `off`

- Type:

```
off(type?: PluginEventType, callback?: CallableFunction): void
type PluginEventType = 'selectionchange' | 'layoutchange' | 'close' | 'currentpagechange' | 'themechange' | 'drop' | 'run'
```

移除事件处理函数。

- 如果没有为 `off` 函数传递参数，将会移除所有事件的事件处理函数。
- 如果只为 `off` 函数提供了事件名称，那么将移除该事件下的所有事件处理函数。
- 如果既为 `off` 函数指定了事件名称，也为其指定了事件处理函数，则只有该指定的事件处理函数会被移除。

### `showGrid`

- Type: `showGrid(show: boolean): void`
画布的布局网格是否显示。

### `saveVersionHistoryAsync`

- Type: `saveVersionHistoryAsync(desc: string, title?: string): Promise`
添加历史版本。 参数 desc 为对版本的描述。 参数 title 为版本的标题，可选。

### `notify`

- Type: `notify(message: string, options?: NotifyOptions): NotificationHandler`
在画布中展示一条通知消息。默认情况下，该通知会从页面的上方弹出。可以通过传递第二个参数并指定通知的类型和弹出位置等，详细请看mg.notify。

### `hexToRGBA`

- Type: `hexToRGBA(hex: string) : RGBA`
hex转rgba。

### `RGBAToHex`

- Type: `RGBAToHex(rgba: RGBA): string`
rbga转hex。

### `getTitleByFontFamilyAndStyle`

- Type: `getTitleByFontFamilyAndStyle(fontFamily: string, fontStyle: string): FontAlias` [FontAlias](/types/font.html)
获取字体别名及样式别名。

### `commitUndo`

- Type: `() => void`
默认情况下，插件的操作不会提交到撤销（undo）历史记录中。可以通过 mg.commitUndo() 函数手动地将当前的插件操作提交到撤销（undo）历史记录中。
举个例子，假设我们的插件执行了两个操作，即创建了两个矩形：

```
mg.createRectangle(); // 创建第一个矩形
mg.createRectangle(); // 创建第二个矩形
mg.triggerUndo();
```

这时，当我们执行撤销动作时，会撤销全部两个矩形。如果我们在两个矩形创建动作之间调用 mg.commitUndo() 函数：

```
mg.createRectangle(); // 创建第一个矩形
mg.commitUndo(); // 添加撤销历史
mg.createRectangle(); // 创建第二个矩形
mg.triggerUndo();
```

这时，如果我们执行撤销动作，将只会撤销掉第二个矩形的创建。

### `triggerUndo`

- Type: `() => void`
触发撤销动作，将会恢复到最后一次 commitUndo() 的状态。

### `exportPng` 私有化

- Type:

```
exportPng(params: ExportPngOptions): string
interface ExportPngOptions {
  ids?: string[]
  filterIds?: string[]
  scale?: number
}
```

将指定图层导出为 PNG 图片，返回 base64 编码的 data URL 字符串（data:image/png;base64,...）。

- `ids`：要导出的图层 ID 数组。不传或空数组时，有选中图层则导出选中图层，否则导出整页。
- `filterIds`：要排除的子图层 ID 数组，排除的子图层不会被导出。默认为空数组。
- `scale`：缩放比例，默认为 `1`。

### `exportSvgByLayerIds` 私有化

- Type: `exportSvgByLayerIds(layerIds: string[]): string`
根据给定的图层 ID 数组导出 SVG 字符串。如果 layerIds 为空数组，则返回空字符串。

## 节点操作

### `getNodeById`

- Type: `getNodeById(id: string): SceneNode | null`
根据给定的 id 查找相应的节点。如果没有找到对应的节点，则返回 null。

### `getNodeByPosition`

- Type: `getNodeByPosition(position: {x: number, y: number}): SceneNode | null`
与鼠标点击画布类似，根据给定的画布中的世界坐标，查找相应的节点。如果没有找到对应的节点，则返回 null。
若同一坐标下有多个图层为重叠关系，则返回最上层未被覆盖的图层节点。若同一坐标下有多个图层，并且为包含关系，则返回子图层节点。

```
const rect1 = mg.createRectangle();
const rect2 = mg.createRectangle();
const gotNode1 = mg.getNodeByPosition({x: rect1.x, y: rect1.y});
console.log(gotNode1.id === rect2.id) // true rect2在上层。

const child = mg.createRectangle();
const frame = mg.createFrame([child]);
const gotNode2 = mg.getNodeByPosition({x: frame.x, y: frame.y});
console.log(gotNode2.id === child.id) // true child为子图层。
```

### `getRootNodeById`

- Type: `getRootNodeById(id: string): SceneNode | null`
根据给定的 id 查找该节点所在图层树的根父节点。如果该节点本身就是根节点（没有父级），则返回 null。
根父节点是指图层层级结构中最顶层的节点，例如一个嵌套在 Frame 中的矩形，其根父节点就是该 Frame。

```
const child = mg.createRectangle();
const frame = mg.createFrame([child]);
const rootNode = mg.getRootNodeById(child.id);
console.log(rootNode.id === frame.id); // true
```

### `getRootParentLayerId`

- Type: `getRootParentLayerId(id: string): string | null`
根据给定的 id 查找该节点所在图层树的根父节点 ID。如果该节点本身就是根节点（没有父级），则返回 null。
与 getRootNodeById 类似，但返回的是根父节点的 ID 字符串，而非节点对象。

```
const child = mg.createRectangle();
const frame = mg.createFrame([child]);
const rootId = mg.getRootParentLayerId(child.id);
console.log(rootId === frame.id); // true
```

### `getTopContainerInfoListByPageID`

- Type: `getTopContainerInfoListByPageID(pageID: string): TopContainerInfo[] | null`
根据页面 ID 获取页面根容器的信息列表。返回值中的 id 字段是页面根节点的 ID；页面不存在或暂时没有可用数据时返回 null。

```
const rootContainers = mg.getTopContainerInfoListByPageID(mg.document.currentPage.id);
const rootNodeIds = rootContainers?.map(({ id }) => id) ?? [];
```

### `createRectangle`

- Type: `createRectangle(): RectangleNode`， [RectangleNode](/apis/rectangleNode.html)
创建一个新的矩形图层，其行为等价于使用快捷键 R，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createLine`

- Type: `createLine(): LineNode`，[LineNode](/apis/lineNode.html)
创建一个新的线段图层。其行为等价于使用快捷键 L，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createEllipse`

- Type: `createEllipse(): EllipseNode`，[EllipseNode](/apis/ellipseNode.html)
创建一个新的椭圆图层。其行为等价于使用快捷键 O，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createPolygon`

- Type: `createPolygon(): PolygonNode`，[PolygonNode](/apis/polygonNode.html)
创建一个新的多边形图层。

### `createStar`

- Type: `createStar(): StarNode`，[StarNode](/apis/starNode.html)
创建一个新的星型图层。

### `createPen`

- Type: `createPen(): PenNode`，[PenNode](/apis/penNode.html)
创建一个新的钢笔图层。其行为等价于使用快捷键 P，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createText`

- Type: `createText(): TextNode`，[TextNode](/apis/textNode.html)
创建一个新的文本图层。其行为等价于使用快捷键 T，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createFrame`

- Type: `createFrame(children?: SceneNode[]): FrameNode`，[FrameNode](/apis/frameNode.html)
创建一个新的容器图层。未传入参数时，其行为等价于使用快捷键 F，接着点击画布。传入参数时，传入的节点将被创建为容器的子节点。其行为等价于使用Mac快捷键 Command + Option + G 或Windows快捷键 Ctrl + Alt + G。 但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createSection`

- Type: `createSection(): SectionNode`，[SectionNode](/apis/sectionNode.html)
创建一个新的区域图层。其行为等价于使用快捷键 Q，接着点击画布。 但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createComponent`

- Type: `createComponent(children?: SceneNode[]): ComponentNode`，[ComponentNode](/apis/componentNode.html)
创建一个新的组件图层，当传入参数时，传入的节点将被创建为组件的子节点。

### `createPage`

- Type: `createPage(): PageNode`，[PageNode](/apis/pageNode.html)
创建一个新的页面。

### `createSlice`

- Type: `createSlice(): SliceNode`，[SliceNode](/apis/sliceNode.html)
创建一个新的切图图层。其行为等价于使用快捷键 S，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createConnector`

- Type: `createConnector(): ConnectorNode`，[ConnectorNode](/apis/connectorNode.html)
创建一个新的连接线图层。其行为等价于使用快捷键 X，接着点击画布。但与使用快捷键创建的图层不同，使用接口创建的图层不会处于选中状态。

### `createIntelligentContainer`

- Type: `createIntelligentContainer(): IntelligentContainerNode`，[IntelligentContainerNode](/apis/intelligentContainerNode.html)
创建一个新的智能容器图层。智能容器支持 GLSL shader 动画效果，可通过 shaderCode 属性设置 shader 代码，通过 isPlaying 属性控制播放状态。

### `createNodeFromSvgAsync`

- Type: `createNodeFromSvgAsync(svg: string): Promise`，[FrameNode](/apis/frameNode.html)
从 SVG 字符串创建新的节点。等价于 MasterGo 的导入 SVG 功能。

### `combineAsVariants`

- Type: `combineAsVariants(nodes: Array): ComponentSetNode`
将一组ComponentNode节点组合成ComponentSetNode节点。

### `group`

- Type: `group(children: SceneNode[]): GroupNode`，[GroupNode](/apis/groupNode.html)
group 函数用来根据其参数中指定的节点创建一个组。

### `union`

- Type: `union(children: SceneNode[]): BooleanOperationNode`，[BooleanOperationNode](/apis/booleanOperationNode.html)
union 函数用来根据其参数指定的节点创建一个新的布尔组（联集）图层。

### `subtract`

- Type: `subtract(children: SceneNode[]): BooleanOperationNode`，[BooleanOperationNode](/apis/booleanOperationNode.html)
subtract 函数用来根据其参数指定的节点创建一个新的布尔组（减去顶层）图层。

### `intersect`

- Type: `intersect(children: SceneNode[]): BooleanOperationNode`，[BooleanOperationNode](/apis/booleanOperationNode.html)
intersect 函数用来根据其参数指定的节点创建一个新的布尔组（交集）图层。

### `exclude`

- Type: `exclude(children: SceneNode[]): BooleanOperationNode`，[BooleanOperationNode](/apis/booleanOperationNode.html)
exclude 函数用来根据其参数指定的节点创建一个新的布尔组（差集）图层。

### `flatten`

- Type: `flatten(nodes: SceneNode[]): PenNode`，[PenNode](/apis/penNode.html)
flatten 函数用来拼合指定图层，并创建拼合后新的钢笔图层，原图层节点将被移除，即removed为true。

## 样式

### `getStyleById`

- Type: `(id: string) => Style | null`, [Style](/types/style.html)
根据给定的 id 查找对应的样式。如果没找到，则返回 null。

### `getStyleCodeById`

- Type: `(id: string, options?: StyleCodeOptions) => CodeString | null`
根据给定的 id 查找对应的研发模式样式code。如果没找到，则返回 null。

### `getWebStyleCodeById`

- Type: `(id: string, options?: WebStyleCodeOptions) => CodeString | null`
根据给定的 id 查找对应的研发模式样式code。如果没找到，则返回 null。

### `getAndroidStyleCodeById`

- Type: `(id: string, options?: AndroidStyleCodeOptions) => CodeString | null`
根据给定的 id 查找对应的 Android 研发模式 code 。如果没找到，则返回 null。

### `getIOSStyleCodeById`

- Type: `(id: string, options?: IOSStyleCodeOptions) => CodeString | null`
根据给定的 id 查找对应的 iOS 研发模式 code 。如果没找到，则返回 null。

### `createFillStyle`

- Type: `(config: { id: string, name: string, description?: string }) => PaintStyle`, [PaintStyle](/types/style.html#paintstyle)
通过传入一个带有填充的nodeId来创建一个新的 Fill 样式。此类型的样式可能包含图片，且可用于背景、描边、填充等多个场景。因此我们叫它 Paint。

> > **TIP**
> 注意：当TextNode的文字具有不同的填充时，createFillStyle只会为第一段填充创建style。

### `createStrokeStyle`

- Type: `(config: { id: string, name: string, description?: string }) => PaintStyle`, [PaintStyle](/types/style.html#paintstyle)
通过传入一个带有描边样式的nodeId和自定义名称来创建一个新的 Stroke 样式。此类型的样式可能包含图片，且可用于背景、描边、填充等多个场景。因此我们叫它 Paint。

### `createEffectStyle`

- Type: `(config: { id: string, name: string, description?: string }) => EffectStyle`, [EffectStyle](/types/style.html#effectstyle)
通过传入一个带有的特效的nodeId和自定义名称来创建一个新的特效样式。

### `createTextStyle`

- Type: `(config: { id: string, name: string, description?: string }) => TextStyle`, [TextStyle](/types/style.html#textstyle)
通过传入一个带有的文字样式的nodeId和自定义名称创建一个新的文字样式。

### `createGridStyle`

- Type: `(config: { id: string, name: string, description?: string }) => GridStyle`, [GridStyle](/types/style.html#gridstyle)
通过传入一个带有的布局网格的nodeId和自定义名称创建一个新的布局网格样式。

### `getLocalPaintStyles`

- Type: `getLocalPaintStyles(): PaintStyle[]`, [PaintStyle](/types/style.html#paintstyle)
返回本地paint样式列表。

### `getLocalEffectStyles`

- Type: `getLocalEffectStyles(): EffectStyle[]`, [EffectStyle](/types/style.html#effectstyle)
返回本地effect样式列表。

### `getLocalTextStyles`

- Type: `getLocalTextStyles(): TextStyle[]`, [TextStyle](/types/style.html#textstyle)
返回本地text样式列表。

### `getLocalGridStyles`

- Type: `getLocalGridStyles(): GridStyle[]`, [GridStyle](/types/style.html#gridstyle)
返回本地grid样式列表。

### `getLocalStrokeWidthStyles`

- Type: `getLocalStrokeWidthStyles(): StrokeWidthStyle[]`, [StrokeWidthStyle](/types/style.html#strokewidthstyle)
返回本地描边宽度样式列表。

### `getLocalPaddingStyles`

- Type: `getLocalPaddingStyles(): PaddingStyle[]`, [PaddingStyle](/types/style.html#paddingstyle)
返回本地内边距样式列表。

### `getLocalSpacingStyles`

- Type: `getLocalSpacingStyles(): SpacingStyle[]`, [SpacingStyle](/types/style.html#spacingstyle)
返回本地间距样式列表。

### `getLocalCornerRadiusStyles`

- Type: `getLocalCornerRadiusStyles(): CornerRadiusStyle[]`, [CornerRadiusStyle](/types/style.html#cornerradiusstyle)
返回本地圆角样式列表。
所有 getLocal*Styles 返回的样式对象都包含 collectionId 和 collectionName，分别表示样式所属集合的 id 和名称。

### `createStrokeWidthStyle`

- Type: `(config: { id: string, name: string, description?: string }) => StrokeWidthStyle`, [StrokeWidthStyle](/types/style.html#strokewidthstyle)
通过传入一个带有描边宽度的nodeId和自定义名称创建一个新的描边宽度样式。

### `createStrokeFillStyle`

- Type: `(config: { id: string, name: string, description?: string }) => PaintStyle`, [PaintStyle](/types/style.html#paintstyle)
通过传入一个带有描边填充的nodeId和自定义名称创建一个新的描边填充样式。

### `createPaddingStyle`

- Type: `(config: { id: string, name: string, description?: string }) => PaddingStyle`, [PaddingStyle](/types/style.html#paddingstyle)
通过传入一个带有内边距的nodeId和自定义名称创建一个新的内边距样式。注意：仅对自动布局中的图层有效。

### `createCornerRadiusStyle`

- Type: `(config: { id: string, name: string, description?: string }) => CornerRadiusStyle`, [CornerRadiusStyle](/types/style.html#cornerradiusstyle)
通过传入一个带有圆角的nodeId和自定义名称创建一个新的圆角样式。

### `createSpacingStyle`

- Type: `(config: { id: string, name: string, description?: string }) => SpacingStyle`, [SpacingStyle](/types/style.html#spacingstyle)
通过传入一个带有层间距的nodeId和自定义名称创建一个新的间距样式。注意：仅对自动布局中的图层有效。

### `createStyle`

- Type: `(type: StyleType, name: string, description?: string, collectionId?: string) => Style | null`
聚合创建样式方法。根据传入的样式类型和名称创建样式，无需依赖已有图层。支持的类型：'PAINT'、'TEXT'、'EFFECT'、'GRID'、'STROKE_WIDTH'、'PADDING'、'SPACING'、'CORNER_RADIUS'。

```
const style = mg.createStyle('PAINT', '我的填充样式');
const strokeStyle = mg.createStyle('STROKE_WIDTH', '描边宽度');
```

### `createStyleByLayer`

- Type: `(layerId: string, type: StyleType, name: string, description?: string, collectionId?: string) => Style | null`
通过图层创建样式。传入图层 ID 和样式类型，从图层当前属性中提取值并创建样式。

```
const node = mg.document.currentPage.selection[0];
const style = mg.createStyleByLayer(node.id, 'CORNER_RADIUS', '圆角样式');
```

### `createStyleCopy`

- Type: `(sourceStyleId: string, name?: string, description?: string) => Style | null`
复制已有样式创建一个新样式。不传 name 和 description 时沿用源样式的值。

```
const copy = mg.createStyleCopy('sourceStyleId', '副本名称');
```

## 团队库
这些 API 允许您从已订阅的团队库中获取组件或样式。这需要您有一个ukey，您可以在插件运行时从 component.ukey 或 style.ukey 获取它，然后将其使用到您的插件中。

### `getTeamLibraryAsync`

- Type: `getTeamLibraryAsync(): Promise`, [TeamLibrary](/types/teamLibrary.html)
当前已订阅的团队库组件和样式信息, 从中可以获取组件和样式的ukey。
返回的 TeamLibrary 中：

- 每个 `TeamLibraryComponent` 携带 `properties`（组件属性/变体属性）和 `textNodeNames`（后代 TEXT 图层名称数组）。老团队库可能缺省这两个字段，使用前请判断。
- 每个 `TeamLibraryStyle` 携带 `values`，即该样式在各模式下的值列表，元素结构为 `{ modeId, modeName, value }`。`value` 的形态随样式分类变化（paints/effects 为对象数组，colors 为 Paint[]，numbers/spacings 等为 number[]，strings 为 string，bools 为 boolean）。变量引用项或解析异常时，对应 mode 项仍保留但 `value` 为 `undefined`。老团队库可能缺省 `values` 字段。详见 [TeamLibraryStyle](/types/teamLibrary.html#teamlibrarystyle)。

### `getPublishedTeamLibraryAsync`

- Type: `getPublishedTeamLibraryAsync(): Promise`, [PublishedTeamLibrary](/types/teamLibrary.html#publishedteamlibrary)
获取当前文件发布的团队库内容。返回当前文件发布的组件、组件集、样式、变量和变量集合；当前文件未发布团队库，或当前用户没有查询权限时返回 null。
返回数据中的 style 字段与 TeamLibrary 相同，变量值通过 values 按 mode 返回；collections 为当前发布的变量集合及其模式信息。

```
const library = await mg.getPublishedTeamLibraryAsync()
if (library) {
  console.log(library.componentList)
  console.log(library.style.colors)
  console.log(library.collections)
}
```

### `importComponentByKeyAsync`

- Type: `importComponentByKeyAsync(ukey: string): Promise`, [ComponentNode](/apis/componentNode.html)
从已订阅的团队库中导入组件进入画布中。

```
async function importComponentFromLibrary(ukey: string) {
  try {
    const componentNode = await mg.importComponentByKeyAsync(ukey)
    const instance = componentNode.createInstance()
    // 其他操作
  } catch (error) {
    // 当传入的ukey无法关联到团队库组件时会抛错
    console.error('failed to import component', error)
  }
}
```

> > **WARNING**
> 导入进画布的团队库组件总是不可见的，它的数据存于远端，除了创建实例去使用它，您无法修改它的其他属性或调用其他方法。

### `importComponentSetByKeyAsync`

- Type: `importComponentSetByKeyAsync(ukey: string): Promise`, [ComponentSetNode](/apis/componentSetNode.html)
从已订阅的团队库中导入组件集进入画布中。

```
async function importComponentSetFromLibrary(ukey: string) {
  try {
    const componentSetNode = await mg.importComponentSetByKeyAsync(ukey)
    const childComponent = componentSetNode.children[0]
    const instance = childComponent.createInstance()
    // 其他操作
  } catch (error) {
    // 当传入的ukey无法关联到团队库组件集时会抛错
    console.error('failed to import componentSet', error)
  }
}
```

> > **WARNING**
> 导入进画布的团队库组件集总是不可见的，它的数据存于远端，除了通过不同状态的子组件创建实例去使用它，您无法修改它的其他属性或调用方法。

### `importStyleByKeyAsync`

- Type: `importStyleByKeyAsync(ukey: string): Promise`, [BaseStyle](/types/style.html##BaseStyle)
从已订阅的团队库中导入样式进入画布中。

```
async function importStyleByFromLibrary(ukey: string) {
  try {
    const style = await mg.importStyleByKeyAsync(ukey)
    const layer = mg.document.currentPage.selection[0] as RectangleNode
    if (style.type === 'PAINT') {
      layer.fillStyleId = style.id
    }
  } catch (error) {
    // 当传入的ukey无法关联到团队库样式时会抛错
    console.error('failed to import style', error)
  }
}
```

### `getComponentListVal`

- Type: `getComponentListVal(): ComponentItemVal[]`, [ComponentItemVal](/types/componentPropertiesRelated.html#componentitemval)
获取当前文件中的所有组件列表信息。此方法返回一个包含所有组件(不包括组件集)详细信息的数组，包括组件的 id、ukey、name、尺寸、所属页面等元数据信息。

> > **TIP**
> 注意：getComponentListVal 只会返回本地文件中的组件信息，不包括组件集(ComponentSet)。

```
const componentList = mg.getComponentListVal()
console.log(componentList)
// 输出示例：
// [
//   {
//     "id": "5:7",
//     "name": "按钮",
//     "componentSignature": "21474836485",
//     "ukey": "12345036836269+5:7",
//     "cover": "",
//     "description": "一个按钮组件",
//     "documentationLinks": [],
//     "height": 100,
//     "width": 200,
//     "isExternal": false,
//     "isHidden": false,
//     "pageId": "M",
//     "pageName": "页面 1",
//     "version": 1,
//     "componentNameAlias": ""
//   }
// ]
```

> > **WARNING**
> 团队库样式是存在于远端的，您无法修改它的属性或调用其方法。

### `teamLibrary`

- Type: [TeamLibrary](/types/teamLibrary.html)

> > **TIP**
> 已废弃，请改用getTeamLibraryAsync.
当前已订阅的团队库组件和样式信息, 从中可以获取组件和样式的ukey。

## 其它

### `listAvailableFontsAsync`

- Type: `() => Promise`, [Font](/types/font.html)
返回当前可用字体列表。该列表与字体选择器中列出的字体列表相同。

### `loadFontAsync`

- Type: `(fontName: FontName) => Promise`, [FontName](/types/font.html#fontname)
当插件修改会影响文字节点渲染的属性时，如 .fonstSize、.fontName 等，需要先确保字体可用。为此，在修改这些属性之前，需要先调用此函数加载对应的字体。
可以使用 listAvailableFontsAsync 的结果作为 loadFontAsync 的参数：

```
async function loadFont() {
  const fonts = await mg.listAvailableFontsAsync();
  // 加载指定的字体
  await mg.loadFontAsync(fonts[0].fontName);
}
```

### `createImage`

- Type: `createImage(imageData: Uint8Array): Promise`, [Image](/types/image.html)
根据给定的图片数据（Uint8Array 格式）创建一个图片对象，该图片对象可以用于图层的填充, 支持类型: png | jpeg | gif | webp。下面是一个为图层设置图片填充的例子：

```
async function fillTheSelection() {
  // 获取当前选中的图层
  const node = mg.document.currentPage.selection[0];
  // 创建一个图片对象
  const imageHandle = await mg.createImage(
    new Uint8Array([
      137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 0, 5,
      0, 0, 0, 5, 8, 6, 0, 0, 0, 141, 111, 38, 229, 0, 0, 0, 28, 73, 68, 65, 84,
      8, 215, 99, 248, 255, 255, 63, 195, 127, 6, 32, 5, 195, 32, 18, 132, 208,
      49, 241, 130, 88, 205, 4, 0, 14, 245, 53, 203, 209, 142, 14, 31, 0, 0, 0,
      0, 73, 69, 78, 68, 174, 66, 96, 130,
    ])
  );

  // 设置图片填充
  node.fills = [
    {
      type: "IMAGE",
      scaleMode: "FILL",
      imageRef: imageHandle.href, // 将 href 作为图片填充的 imageRef
    },
  ];
}
```

### `getImageByHref`

- Type: `(href: string) => Image`
根据图片的 href 获取图片 Image 对象，通常用于从图片填充中读取图片数据，并做进一步处理：

```
async function convertImage() {
  // 获取当前选中的图层
  const node = mg.document.currentPage.selection[0];
  // 遍历该图层的所有填充
  node.fills.forEach(async (fill) => {
    // 过滤出图片填充
    if (fill.type === "IMAGE") {
      // 调用 mg.getImageByHref 根据图片 href 获取图片对象
      const imageHandle = mg.getImageByHref(fill.imageRef);
      // 配合图片对象的 getBytesAsync 方法，即可取得图片的数据
      const bytes = await imageHandle.getBytesAsync();

      console.log(bytes); // Uint8Array

      // 接下来可以根据图片数据做进一步处理......
    }
  });
}
```

### `getHoverLayer`

- Type: `() => SceneNode | PageNode`, [SceneNode](/types/sceneNode.html)，[PageNode](/apis/pageNode.html)
返回当前鼠标正在hover的图层对象, 如果没有hover的图层，默认返回当前页面对象。

### documentCookie 私有化

- Type: `string`
添加获取当前文件的cookie。

API Reference
mastergo.variables