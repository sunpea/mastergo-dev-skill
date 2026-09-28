# NodeLayout

## NodeLayout

```
interface NodeLayout {
  matrix?: Matrix
  width?: Dimension
  height?: Dimension
  renderWidth?: Dimension
  renderHeight?: Dimension
  autoLayout?: AutoLayout
  overflow?: 'HIDDEN' | 'VISIBLE'
  relatedLayout?: AbsoluteLayout | RelatedAutoLayout
}
```

## AutoLayout

```
type AutoLayout = {
  direction: 'COLUMN' | 'ROW',
  layoutWrap: 'NO_WRAP' | 'WRAP'
  itemSpacing: Dimension | 'AUTO'
  crossAxisSpacing: Dimension | 'AUTO' | null
  paddingTop: Dimension
  paddingRight: Dimension
  paddingBottom: Dimension
  paddingLeft: Dimension
  mainAxisAlignItems: AlignTypes
  crossAxisAlignItems: Exclude<AlignTypes, 'SPACE_BETWEEN'>
  crossAxisAlignContent: 'AUTO' | 'SPACE_BETWEEN'
  strokesIncludedInLayout: boolean
  itemReverseZIndex: boolean
}
```

元素的自动布局信息，详见Frame-related properties

## AbsoluteLayout

```
type AbsoluteLayout = {
  type: 'ABSOLUTE'
  bound: {
    left?: Dimension
    right?: Dimension
    top?: Dimension
    bottom?: Dimension
  },
  renderBound: {
    left?: Dimension
    right?: Dimension
    top?: Dimension
    bottom?: Dimension
  }
}
```

相对父元素的绝对定位。

- `bound`: 元素的盒模型，不包括外阴影和外描边。
- `renderBound`: 元素的盒模型，包含外阴影和外描边，实际渲染的`bound`。

## RelatedAutoLayout

```
type RelatedAutoLayout = {
  type: 'AUTO'
  alignSelf: 'STRETCH' | 'INHERIT' | 'AUTO'
  flexGrow: number
}
```

子元素自动布局, 详见alignSelf。

## Dimension

```
type Dimension = {
  type: 'PIXEL' | 'PERCENT' | 'CALC'
  value: number | string
}
```

尺寸单位

- `type``PIXEL`: 像素。
- `PERCENT`: 百分比。
- `CALC`: 计算值，类似于`css`的`calc`函数。

DSLSetting
NodeStyle