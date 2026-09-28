# IntelligentContainerNode
IntelligentContainerNode 即智能容器节点，用于承载 GLSL shader 动画效果。智能容器节点继承自容器节点（FrameNode），拥有容器节点的所有属性和能力，并额外支持 shader 代码的读写和播放控制。
智能容器节点特有的属性如下：

| 属性名 | 类型 | 读/写 | 说明 |
|---|---|---|---|
| `shaderCode` | `string` | 读/写 | GLSL 着色器代码，用于控制智能容器的渲染效果。 |
| `isPlaying` | `boolean` | 读/写 | 动画的播放状态，`true` 为播放，`false` 为暂停。 |

## GLSL 代码格式要求说明
智能容器对 GLSL 代码有以下格式要求：

- 仅需片段着色器
只需提供片段着色器（Fragment Shader）代码，不需要顶点着色器，也不从顶点着色器传入坐标。

- 必须声明的 uniform 参数
代码中必须声明以下两个 uniform 变量，名称固定不可更改：

```
uniform float u_time; // 时间戳，单位：毫秒
uniform sampler2D u_texture; // 画布纹理
```

- UV 坐标的获取方式
计算 UV 坐标时，必须通过 textureSize 获取纹理尺寸，不可硬编码分辨率：

```
vec2 uv = gl_FragCoord.xy / vec2(textureSize(u_texture, 0));
```

- 自定义参数须声明为 const
除上述两个 uniform 外，其他可调参数一律声明为 const，并附上默认值。每个参数上方需添加注释，说明其功能和取值范围，格式如下：

```
// 单个波纹生命周期（秒）：[1，20]
const float WAVE_LIFETIME = 8.0;
```

这个注释格式是设置面板自动解析参数的依据——面板会读取注释中的范围信息，将其映射为可拖拽调整的滑块。
完整实例

```
precision highp float;
uniform float u_time;
uniform sampler2D u_texture;
out vec4 fragColor;

// 极光强度: [0.2, 3.0]
const float AURORA_INTENSITY = 1.4;
// 流动速度: [0.0, 3.0]
const float FLOW_SPEED = 0.35;
// 条带数量: [1.0, 6.0]
const float BAND_COUNT = 3.0;
// 条带宽度: [0.02, 0.4]
const float BAND_WIDTH = 0.14;
// 主色 (青): vec3
const vec3 COLOR_CYAN = vec3(0.10, 0.95, 0.75);
// 次色 (紫): vec3
const vec3 COLOR_PURPLE = vec3(0.55, 0.25, 0.95);
// 辅色 (粉): vec3
const vec3 COLOR_PINK = vec3(0.95, 0.40, 0.75);
// 夜空底色: vec3
const vec3 NIGHT_COLOR = vec3(0.02, 0.03, 0.08);

float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float noise(vec2 p) {
    vec2 i = floor(p); vec2 f = fract(p);
    vec2 u = f * f * (3.0 - 2.0 * f);
    return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x),
               mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);
}
float fbm(vec2 p) {
    float v = 0.0;
    float a = 0.5;
    for (int i = 0; i < 5; i++) {
        v += a * noise(p);
        p *= 2.0;
        a *= 0.5;
    }
    return v;
}

void main() {
    vec2 resolution = vec2(textureSize(u_texture, 0).xy);
    vec2 uv = gl_FragCoord.xy / resolution;
    float t = u_time * 0.001 * FLOW_SPEED;

    float wave = fbm(vec2(uv.x * 3.0 + t, uv.y * 1.5 - t * 0.5));
    float curtain = 0.0;
    for (float i = 0.0; i < BAND_COUNT; i += 1.0) {
        float cy = 0.55 + 0.22 * sin(t * 0.7 + i * 1.7);
        float d = abs(uv.y - cy + (wave - 0.5) * 0.45);
        curtain += smoothstep(BAND_WIDTH, 0.0, d);
    }
    curtain = curtain / BAND_COUNT * AURORA_INTENSITY;

    vec3 col = mix(COLOR_PURPLE, COLOR_CYAN, uv.y);
    col = mix(col, COLOR_PINK, wave);
    col = NIGHT_COLOR + col * curtain;

    vec4 tex = texture(u_texture, uv);
    fragColor = vec4(col, tex.a);
}
```

## Base node properties

### `type`

- Readonly: `true`
- Type: `'INTELLIGENT_CONTAINER'`
节点类型，对于 IntelligentContainerNode 节点来说，其值为字符串 'INTELLIGENT_CONTAINER'。

### `clone`

- Type: `clone(): IntelligentContainerNode`
复制该智能容器节点。默认情况下，复制的新节点的父级节点为 mg.document.currentPage。

### `id`

- Readonly: `true`
- Type: `string`
IntelligentContainerNode 节点的 ID。

### `remove`

- Type: `remove():void`
将当前节点从parent节点中移除。

### `removed`

- Type: `boolean`
如果节点被移除了，则值为 true。如果插件保持运行状态，并且插件代码对某个节点存在引用，那么您应该始终检查节点的 removed 属性，在对节点进行操作之前先确保它没有被移除。

### `parent`

- Readonly: `true`
- Type: `(BaseNode & ChildrenMixin) | void`
获取当前节点的父节点。

### `name`

- Type: `string`
读取或设置智能容器的名字，即图层面板中所展示的图层名称。

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
节点是否被锁定。锁定的节点会阻止用户在画布上对其进行特定的交互，例如拖动、选中图层。但无论图层节点是否被选中，都不影响插件代码对图层节点属性的读写操作。与判断节点是否可见的方式类似，判断节点是否真的被锁定正确方法是：只要该节点或任何一个它的父代节点满足条件 .isVisible === true，则认为该节点被锁定。

### `attachedConnectors`

- Readonly: `true`
- Type: [ConnectorNode[]](/apis/connectorNode.html)
吸附到节点的连接线节点数组。

### `componentPropertyReferences`

- Type: `{ [nodeProperty in 'visible' | 'characters' | 'mainComponent']: string } | null`, [ComponentPropertyReferences](/types/componentPropertiesRelated.html#componentpropertyreferences)
此节点上附加的所有组件属性。仅当节点是组件子图层且未嵌套在实例节点中时，该节点才能具有组件属性引用。否则为空。键值对中的值是组件或组件集上的组件属性定义返回的组件属性id。

## Children-related properties

### `children`

- Readonly: `true`
- Type: `ReadonlyArray`
当前 IntelligentContainerNode 节点的直接子节点。

### `appendChild`

- Type: `appendChild(child: SceneNode): void`
将给定的节点 child 添加为当前 IntelligentContainerNode 节点的直接子节点。

### `insertChild`

- Type: `insertChild(index: number, child: SceneNode): void`
在指定的位置 index 处插入子节点 child。假设一个组有三个子节点 A、B、C，现在调用 insertChild 方法将插入图层节点 D：

- `insertChild(0, D)`，子节点顺序为：**`D`**、A、B、C。
- `insertChild(1, D)`，子节点顺序为：A、**`D`**、B、C。
- `insertChild(2, D)`，子节点顺序为：A、B、**`D`**、C。
- `insertChild(3, D)`，子节点顺序为：A、B、C、**`D`**。

### `findAll`

- Type: `findAll(callback?: (node: SceneNode) => boolean): ReadonlyArray`
从当前 IntelligentContainerNode 节点开始查找整个子树，对每个节点调用 callback 函数，并返回所有对于 callback 函数的返回值为 true 的节点。

### `findOne`

- Type: `findOne(callback: (node: SceneNode) => boolean): SceneNode | null`
从当前 IntelligentContainerNode 节点开始查找整个节点树，对每个节点调用 callback 函数，并返回第一个对于 callback 函数的返回值为 true 的节点。

### `findChildren`

- Type: `findChildren(callback?: (node: SceneNode) => boolean): ReadonlyArray`
与 findAll 类似，不同之处在于，findChildren 仅会在当前 IntelligentContainerNode 节点的直接子节点（不包括子节点的子节点）中进行查找。

### `findChild`

- Type: `findChild(callback: (node: SceneNode) => boolean): SceneNode | null`
与 findOne 类似，不同之处在于，findChild 仅会在当前 IntelligentContainerNode 节点的直接子节点（不包括子节点的子节点）中进行查找。

### `findAllWithCriteria`

- Type: `findAllWithCriteria(criteria: { types: T }): Array`
查找当前节点的所有子节点，返回所有类型符合的节点。

## IntelligentContainer-related properties

### `shaderCode`

- Type: `string`
智能容器的 GLSL shader 代码。可以读取或设置该属性来控制智能容器的渲染效果。

```
const ic = mg.createIntelligentContainer()
ic.shaderCode = 'void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }'
```

### `isPlaying`

- Type: `boolean`
智能容器的播放状态。true 表示正在播放动画，false 表示暂停。

```
const ic = mg.getNodeById('xxx')
console.log(ic.isPlaying) // true or false
ic.isPlaying = false // 暂停播放
ic.isPlaying = true // 继续播放
```

## Frame-related properties

### `clipsContent`

- Type: `boolean`
容器是否对超出的内容进行裁剪，即超出容器的图层是否可见。

### `layoutGrids`

- Type: [`ReadonlyArray`](/types/layoutGrid.html)
布局网格。

> > **TIP**
> 布局网格只有在非自动布局时设置才会生效。

### `gridStyleId`

- Type: string
布局网格样式Id。

### `flexMode`

- Type: `'NONE' | 'HORIZONTAL' | 'VERTICAL'`
表示该容器是否采用自动布局：

- `'NONE'`: 没有采用自动布局。
- `'HORIZONTAL'`: 自动布局，水平方向。
- `'VERTICAL'`: 自动布局，垂直方向。

### `flexWrap`

- Type: `'NO_WRAP' | 'WRAP'`
此属性只能在 flexMode === "HORIZONTAL" 的图层上设置。此属性必须设置为'WRAP'，才能使 crossAxisSpacing 和 crossAxisAlignContent 属性生效。

### `itemSpacing`

- Type: `number`
仅适用于采用自动布局的容器图层。代表该容器的子节点间的间距。

### `crossAxisSpacing`

- Type: `number` | `null`
仅适用于 flexWrap 设置为 WRAP 的自动布局图层。表达换行的行之间的距离。

### `mainAxisAlignItems`

- Type: `'FLEX_START' | 'FLEX_END' | 'CENTER' | 'SPACING_BETWEEN'`
仅适用于采用自动布局的容器图层。用于决定自动布局容器的子节点在主轴上的对齐方式。

### `crossAxisAlignItems`

- Type: `'FLEX_START' | 'FLEX_END' | 'CENTER'`
仅适用于采用自动布局的容器图层。用于决定自动布局容器的子节点在交叉轴上的对齐方式。

### `mainAxisSizingMode`

- Type: `'FIXED' | 'AUTO'`
仅适用于采用自动布局的容器图层。代表当前容器主轴方向上的长度。

### `crossAxisSizingMode`

- Type: `'FIXED' | 'AUTO'`
仅适用于采用自动布局的容器图层。代表当前容器交叉轴方向上的长度。

### `crossAxisAlignContent`

- Type: `'AUTO' | 'SPACE_BETWEEN'`
仅适用于自动布局模式为"WRAP"的自动布局图层。确定不同的行在自动布局图层内的分布方式。

### `itemReverseZIndex`

- Type: `boolean`
仅适用于采用自动布局的容器图层。用于决定此容器中图层的画布堆叠顺序。

### `strokesIncludedInLayout`

- Type: `boolean`
仅适用于采用自动布局的容器图层。用于决定描边是否包含在布局计算中。

### `paddingTop`

- Type: `number`
仅适用于采用自动布局的容器图层。容器的上内边距。

### `paddingRight`

- Type: `number`
仅适用于采用自动布局的容器图层。容器的右内边距。

### `paddingBottom`

- Type: `number`
仅适用于采用自动布局的容器图层。容器的下内边距。

### `paddingLeft`

- Type: `number`
仅适用于采用自动布局的容器图层。容器的左内边距。

### `resizeToFit`

- Type: `resizeToFit(): void`
适应内容大小。

## Geometry-related properties

### `fills`

- Type: [`ReadonlyArray`](/types/paint.html)
图层的填充。

### `strokes`

- Type: [`ReadonlyArray`](/types/paint.html)
图层的描边。

### `strokeStyle`

- Type: `'SOLID' | 'DASH' | 'CUSTOM'`
描边类型。

### `strokeWeight`

- Type: `number`
描边的粗细，以像素为单位。必须是非负数，可以是小数。

### `strokeTopWeight`

- Type: `number`
顶侧单边描边的粗细。

### `strokeLeftWeight`

- Type: `number`
左侧单边描边的粗细。

### `strokeBottomWeight`

- Type: `number`
底侧单边描边的粗细。

### `strokeRightWeight`

- Type: `number`
右侧单边描边的粗细。

### `strokeAlign`

- Type: `'CENTER' | 'INSIDE' | 'OUTSIDE'`
描边相对于图层边界的对齐方式。

### `strokeCap`

- Type: `'NONE' | 'ROUND' | 'SQUARE' | 'LINE_ARROW' | 'TRIANGLE_ARROW' | 'ROUND_ARROW' | 'RING' | 'DIAMOND' | 'LINE'`
端点的装饰。

### `strokeJoin`

- Type: `'MITER' | 'BEVEL' | 'ROUND'`
边角的装饰。

### `strokeDashes`

- Type: `ReadonlyArray`
包含数字的数组。数组偶数下标元素代表虚线的长度，奇数下标元素代表虚线的间距。

### `dashCap`

- Type: `'NONE' | 'ROUND' | 'SQUARE'`
虚线端点装饰。

### `fillStyleId`

- Type: `string`
当前节点所链接的填充样式的 id。

### `strokeStyleId`

- Type: `string`
当前节点所链接的描边样式的 id。

### `outlineStroke`

- Type: `() => FrameNode | null`
该方法执行的动作与右键菜单中的"轮廓化"功能相同。如果该节点存在描边则该方法创建并返回描边的 FrameNode 节点，否则返回 null。

## Corner-related properties

### `cornerSmooth`

- Type: `number`
控制角的平滑程度，值域为 [0, 1]。

### `cornerRadius`

- Type: `number | PluginAPI['mixed']`
圆角。

### `topLeftRadius`

- Type: `number`
左上角的角度。

### `topRightRadius`

- Type: `number`
右上角的角度。

### `bottomLeftRadius`

- Type: `number`
左下角的角度。

### `bottomRightRadius`

- Type: `number`
右下角的角度。

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
图层是否是轮廓蒙版。

### `isMaskVisible`

- Type: `boolean`
图层是否显示蒙版。

### `effects`

- Type: `ReadonlyArray`, [Effect](/types/effect.html)
返回一个特效数组。

### `effectStyleId`

- Type: `string`
当前节点所链接的特效样式的 id。

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
图层节点在画布中的实际渲染效果的定位和宽高。

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
图层节点的旋转角度。值域为 [-180, 180]。

### `width`

- Type: `number`
图层节点的宽度。

### `height`

- Type: `number`
图层节点的高度。

### `maxWidth`

- Type: `number`
图层节点的最大宽度。

### `minWidth`

- Type: `number`
图层节点的最小宽度。

### `maxHeight`

- Type: `number`
图层节点的最大高度。

### `minHeight`

- Type: `number`
图层节点的最小高度。

### `flip`

- Type: `flip(direction: 'HORIZONTAL' | 'VERTICAL'): void`
翻转图层。

### `resize`

- Type: `resize(width: number, height: number): void`
调整图层大小。同时设置图层的宽度和高度。

### `rescale`

- Type: `rescale(scale: number, scaleOption?: ScaleOption): void`
等比缩放图层。

### `flexGrow`

- Type: `0 | 1`
该属性仅适用于采用自动布局的容器的直接子节点。

### `alignSelf`

- Type: `"STRETCH" | "INHERIT"`
该属性仅适用于采用自动布局的容器的直接子节点。

### `layoutPositioning`

- Type: `"AUTO" | "ABSOLUTE"`
该属性仅适用于采用自动布局的容器的直接子节点。

### `constraints`

- Type: [`Constraints`](/types/constraints.html)
图层约束。

### `constrainProportions`

- Type: `boolean`
锁定节点宽高比例。

## Export-related properties

### `exportSettings`

- Type: [`ReadonlyArray`](/types/exportSettings.html)
节点的导出设置。

### `export`

- Type: `export(settings?: ExportSettings): Uint8Array | string`, [ExportSettings](/types/exportSettings.html)
将节点导出为对应的编码图片。

### `exportAsync`

- Type: `exportAsync(settings?: ExportSettings): Promise`, [ExportSettings](/types/exportSettings.html)
将节点异步导出为对应的编码图片。

## Reaction prototyping-related properties

### `reactions`

- Type: [`Array`](/types/reaction.html)
获取或设置该节点设置的原型属性。

### `overflowDirection`

- Type: [`readonly OverflowDirection`](/types/overflowDirection.html)
获取该节点溢出行为。

GroupNode
InstanceNode