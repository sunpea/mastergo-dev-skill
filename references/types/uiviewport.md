# UIViewport

```
interface UIViewport {
  x: number
  y: number
  height: number
  width: number
  headerHeight: number
  visible: boolean
  headerVisible?: boolean // 私有化特有
}
```

UIViewport属性用于描述当前插件ui视窗的相关属性，包括相对于画布页面的定位、宽高、显隐等。可用于获取ui视窗信息、定位校验、插件ui内外的坐标系换算等场景。

- `x` ：视窗横向定位，坐标原点为画布页面视窗左上角，单位为像素：
- `y` ：视窗纵向定位，坐标原点为画布页面视窗左上角，单位为像素：
- `height` ：插件ui视窗的高度，和[mg.ui.resize](/apis/ui.html#resize)和[ShowUIOptions['height']](/apis/mastergo.html#showui)中传入的宽度相同，单位为像素。
- `width` ：插件ui视窗的宽度，和[mg.ui.resize](/apis/ui.html#resize)和[ShowUIOptions['width']](/apis/mastergo.html#showui)中传入的宽度相同，单位为像素。
- `headerHeight` ：插件ui视窗标题栏高度。
- `visible` ：当前插件ui视窗是否可视。
- `headerVisible` 私有化：当前插件ui视窗标题栏是否可视。如果插件未设置[ShowUIOptions['headerVisible']](/apis/mastergo.html#showui)，则默认值为`true`。
具体尺寸可参考图例：

Trigger
User