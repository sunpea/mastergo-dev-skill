# mg.viewport
mg.viewport 对象可以用来读取或设置当前页面的用户可视区（即画布的可见区域）的信息。

- Type:

```
interface ViewportAPI {
  center: Vector
  zoom: number
  readonly bound: Rect
  rulerVisible: boolean
  layoutGridVisible: boolean
  layout: Layout
}
```

## `center`

- Type: `center: Vector`

```
interface Vector {
  readonly x: number
  readonly y: number
}
```

读取或设置可视区的中心点。例如：

```
// read
mg.viewport.center
// write
mg.viewport.center = { x: 100, y: 100 }
```

需要注意的是，你只能通过完全地设置 center 属性来实现对可视区的操作，而无法通过单独设置 center 对象的某个属性来完成对可视区的操作。例如，下面的代码是无效的：

```
mg.viewport.center.x = 100 // 无效
```

## `zoom`

- Type: `zoom: number`
读取或设置画布的缩放比例，值为 1 代表缩放比例为 100%，值为 0.5 代表缩放比例为 50%。例如：

```
// read
mg.viewport.zoom
// write
mg.viewport.zoom = 2 // 放大 2 倍
```

## `bound`

- Readonly: `true`
- Type: `bound: Rect`

```
interface Rect {
  readonly x: number
  readonly y: number
  readonly width: number
  readonly height: number
}
```

bound 相当于可视区的边界信息。其中 bound.x 和 bound.y 描述了可视区左上角的画布坐标。bound.width 和 bound.height 为可视区的宽高。

## `rulerVisible`

- Type: `boolean`
显示标尺。

## `layoutGridVisible`

- Type: `boolean`
显示布局网络。

## `positionOnDom`

- Readonly: `true`
- Type: `Rect`
画布在当前窗口的位置大小。

```
interface Rect {
  readonly x: number
  readonly y: number
  readonly width: number
  readonly height: number
}
```

## `layout`

- Readonly: `true`
- Type: `Layout`
窗口的页面布局，获取页面宽度、左侧列表宽度、画布宽度、右侧属性面板宽度。

```
interface Layout {
  readonly canvas: number
  readonly leftbar: number
  readonly rightbar: number
  readonly window: number
}
```

> > **TIP**
> 已废弃，请改用positionOnDom.

## `scrollAndZoomIntoView`

- Type: `(nodes: ReadonlyArray): void`
自动设置 viewport 的坐标，以使得 nodes 在屏幕上可见。

mastergo.ui
mastergo.clientStorage