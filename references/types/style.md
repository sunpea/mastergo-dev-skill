# Style
自定义样式。

```
type Style = PaintStyle | EffectStyle | TextStyle | GridStyle | StrokeWidthStyle | PaddingStyle | SpacingStyle | CornerRadiusStyle
```

- `PaintStyle` ：填充及描边样式，具体可查看类型[PaintStyle](/types/style.html#paintstyle)。
- `EffectStyle` ：特效样式，具体可查看类型[EffectStyle](/types/style.html#effectstyle)。
- `TextStyle` ：文字样式，具体可查看类型[TextStyle](/types/style.html#textstyle)。
- `GridStyle` ：网格样式，具体可查看类型[GridStyle](/types/style.html#gridstyle)。
- `StrokeWidthStyle` ：描边宽度样式，具体可查看类型[StrokeWidthStyle](/types/style.html#strokewidthstyle)。
- `PaddingStyle` ：内边距样式，具体可查看类型[PaddingStyle](/types/style.html#paddingstyle)。
- `SpacingStyle` ：间距样式，具体可查看类型[SpacingStyle](/types/style.html#spacingstyle)。
- `CornerRadiusStyle` ：圆角样式，具体可查看类型[CornerRadiusStyle](/types/style.html#cornerradiusstyle)。

## StyleType
样式类型。

```
type StyleType = 'PAINT' | 'TEXT' | 'EFFECT' | 'GRID' | 'STROKE_WIDTH' | 'PADDING' | 'SPACING' | 'CORNER_RADIUS'
```

- `PAINT` ：填充。
- `TEXT` ：文字。
- `EFFECT` ：特效。
- `GRID` ：网格。
- `STROKE_WIDTH` ：描边宽度。
- `PADDING` ：内边距。
- `SPACING` ：间距。
- `CORNER_RADIUS` ：圆角。

## PaintStyle
填充及描边样式。

```
interface PaintStyle extends BaseStyle {
  type: 'PAINT'
  paints: ReadonlyArray<Paint>
}
```

- `type` ：类型，取值为填充 `PAINT`。
- `paints` ：填充，具体可查看类型 [PAINT](/types/paint.html)。

## EffectStyle
特效样式。

```
interface EffectStyle extends BaseStyle {
  type: 'EFFECT'
  effects: ReadonlyArray<Effect>
}
```

- `type` ：类型，取值为特效 `EFFECT`。
- `effects` ：特效，具体可查看类型[Effect](/types/effect.html)。

## TextStyle
文字样式。

```
interface TextStyle extends BaseStyle {
  type: 'TEXT'
  fontSize: number
  fontStyle: string
  fontName: FontName
  decoration: TextDecoration
  letterSpacing: LetterSpacing
  letterSpacingUnit: 'PERCENT' | 'PIXELS'
  lineHeight: LineHeight
  textCase: TextCase
}
```

- `type` ：类型，取值为文字 `TEXT`。
- `fontSize` ：文字尺寸。
- `fontStyle` ：文字样式。
- `fontName` ：字体。
- `decoration` ：文字装饰线，具体可查看类型 [TextDecoration](/types/textSegStyle.html#textdecoration)。
- `letterSpacing` ：字间距，具体可查看类型 [LetterSpacing](/types/textSegStyle.html#letterspacing)。
- `letterSpacingUnit` ：字间距单位，取值为百分比 `PERCENT`，或像素 `PIXELS`。
- `lineHeight` ：行高，具体可查看类型 [LineHeight](/types/textSegStyle.html#lineheight)。
- `textCase` ：字母大小写，具体可查看类型 [TextCase](/types/textSegStyle.html#textcase)。

## GridStyle
网格样式。

```
interface GridStyle extends BaseStyle {
  type: 'GRID'
  layoutGrids: ReadonlyArray<LayoutGrid>
}
```

- `type` ：类型，取值为网格 `GRID`。
- `layoutGrids` ：网格布局样式，具体可查看类型 [LayoutGrid](/types/layoutGrid.html)。

## StrokeWidthStyle
描边宽度样式。

```
interface StrokeWidthStyle extends BaseStyle {
  type: 'STROKE_WIDTH'
  value: StrokeWidthValue
}

interface StrokeWidthValue {
  top: number
  right: number
  bottom: number
  left: number
}
```

- `type` ：类型，取值为描边宽度 `STROKE_WIDTH`。
- `value` ：描边宽度值，包含四个方向的描边宽度（上、右、下、左）。

## PaddingStyle
内边距样式。

```
interface PaddingStyle extends BaseStyle {
  type: 'PADDING'
  value: PaddingValue
}

interface PaddingValue {
  top: number
  right: number
  bottom: number
  left: number
}
```

- `type` ：类型，取值为内边距 `PADDING`。
- `value` ：内边距值，包含四个方向的内边距（上、右、下、左）。

## SpacingStyle
间距样式。

```
interface SpacingStyle extends BaseStyle {
  type: 'SPACING'
  value: number
}
```

- `type` ：类型，取值为间距 `SPACING`。
- `value` ：间距值。

## CornerRadiusStyle
圆角样式。

```
interface CornerRadiusStyle extends BaseStyle {
  type: 'CORNER_RADIUS'
  value: CornerRadiusValue
}

interface CornerRadiusValue {
  topLeft: number
  topRight: number
  bottomRight: number
  bottomLeft: number
}
```

- `type` ：类型，取值为圆角 `CORNER_RADIUS`。
- `value` ：圆角值，包含四个角的圆角（左上、右上、右下、左下）。

## BaseStyle
基础样式。

```
interface BaseStyle extends PublishableMixin {
  readonly id: string
  readonly type: StyleType
  readonly collectionId: string
  readonly collectionName: string
  name: string
  remove(): void
}
```

- `type` ：类型，具体可查看类型 [StyleType](/types/style.html#styletype)。
- `collectionId` ：样式所属集合的 id。
- `collectionName` ：样式所属集合的名称。
- `remove()` ：删除样式。

> > **TIP**
> 您无法删除团队库样式，remove方法在调用时会出错。

## PublishableMixin
发布状态。

```
interface PublishableMixin {
  description: string
  readonly isExternal: boolean
  readonly ukey: string
  readonly publishStatus: PublishStatus
}
```

- `description` ：描述。
- `isExternal` ：是否是远端数据。
- `ukey` ：唯一的key值。
- `publishStatus` ：描述可发布到团队库的元素（即样式和组件）的状态，具体可查看类型 [PublishStatus](/types/teamLibrary.html#publishstatus)。

SceneNode
TeamLibrary