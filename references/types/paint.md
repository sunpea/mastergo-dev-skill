# Paint
描边和填充。

```
type Paint = SolidPaint | GradientPaint | ImagePaint | ReferencePaint
```

- `SolidPaint` ：纯色描边和填充，具体可查看类型 [SolidPaint](/types/paint.html#solidpaint)。
- `GradientPaint` ：渐变描边和填充，具体可查看类型 [GradientPaint](/types/paint.html#gradientpaint)。
- `ImagePaint` ：图片描边和填充，具体可查看类型 [ImagePaint](/types/paint.html#imagepaint)。
- `ReferencePaint` ：引用型描边和填充，具体可查看类型 [ReferencePaint](/types/paint.html#referencepaint)。

## SolidPaint
纯色描边和填充。

```
interface SolidPaint {
  readonly type: 'SOLID'
  readonly color: RGBA

  readonly isVisible?: boolean
  readonly alpha?: number
  readonly blendMode?: BlendMode
}
```

- `type` ：描边和填充的类型，值为`SOLID`。
- `color` ：描边和填充的颜色，具体可查看类型 [RGBA](/types/rgb.html#rgba)。
- `isVisible` ：是否可见。
- `alpha` ：透明度，纯色模式下其值始终为1, 请设置color中的alpha。
- `blendMode` ：混合模式，具体可查看类型 [BlendMode](/types/blend.html)。

## GradientPaint
渐变描边和填充。

```
interface GradientPaint {
  readonly type:
    | 'GRADIENT_LINEAR' //  线性渐变
    | 'GRADIENT_RADIAL' // 径向渐变
    | 'GRADIENT_ANGULAR' // 旋转渐变
    | 'GRADIENT_DIAMOND' // 菱形渐变
  readonly transform: Transform
  readonly gradientStops: ReadonlyArray<ColorStop>
  readonly gradientHandlePositions: ReadonlyArray<{x: number, y: number}>
  readonly isVisible?: boolean
  readonly alpha?: number
  readonly blendMode?: BlendMode
}
```

- `type` ：描边和填充的类型： `GRADIENT_LINEAR` ：线性渐变。
- `GRADIENT_RADIAL` ：径向渐变。
- `GRADIENT_ANGULAR` ：旋转渐变。
- `GRADIENT_DIAMOND` ：菱形渐变。

- `transform` ：渐变尺寸形变，具体可查看类型 [Transform](/types/transform.html)。
- `gradientStops` ：渐变轴控制点位置，具体可查看类型 [ColorStop](/types/paint.html#colorstop)。
- `gradientHandlePositions` ： 渐变轴起止点相对位置。
- `isVisible` ：是否可见。
- `alpha` ：透明度，仅为渐变类型时有效。
- `blendMode` ：混合模式，具体可查看类型 [BlendMode](/types/blend.html)。

## ImagePaint
图片描边和填充。

```
interface ImagePaint {
  readonly type: 'IMAGE'
  readonly scaleMode: 'FILL' | 'TILE' | 'STRETCH' | 'FIT' | 'CROP'
  readonly rotation?: number
  readonly ratio?: number
  readonly imageRef: string

  readonly isVisible?: boolean
  readonly alpha?: number
  readonly blendMode?: BlendMode
  readonly filters?: ImageFilters
}
```

- `type` ：描边和填充的类型，值为 `IMAGE`。
- `scaleMode` ：图片在图层中的定位与缩放： `FILL` ：充满。
- `TILE` ：平铺。
- `STRETCH` ：拉伸。
- `FIT` ：适应。
- `CROP` ：裁剪。

- `rotation` ：旋转。
- `ratio` ：图片缩放比例。
- `imageRef` ：图片地址，imageRef只能是画布内已经存在的图片资源或者通过`mg.createImage`创建的图片。
- `isVisible` ：是否可见。
- `alpha` ：透明度。
- `blendMode` ：混合模式，具体可查看类型 [BlendMode](/types/blend.html)。
- `filters` ：图片滤镜，具体可查看类型 [ImageFilters](/types/paint.html#imageFilters)。

## ReferencePaint
引用型描边和填充。当样式的某个 mode 引用了另一个填充/描边样式（style 引用 style）时，该 paint 项为引用类型，不携带具体填充值，仅保留被引用样式的信息。

```
interface ReferencePaint {
  readonly type: 'REFERENCE';
  /** 被引用的样式 id */
  readonly reference: string;
  /** 解析后的源样式 id（可能与 reference 相同） */
  readonly referenceSource?: string;
  /** 所属模式 id */
  readonly modeId?: string;
}
```

- `type` ：固定为 `REFERENCE`。
- `reference` ：被引用的填充/描边样式 id，可据此用 `mg.importStyleByKeyAsync` 或 `mg.getStyleById` 进一步解析。
- `referenceSource` ：解析后的源样式 id（经过引用链解析后的末端样式），可能与 `reference` 相同。
- `modeId` ：该引用项所属的模式 id。

## ColorStop
渐变轴起止点相对位置。

```
interface ColorStop {
  readonly position: number
  readonly color: RGBA
}
```

- `position` ：渐变轴起点相对位置，值域为 `[0, 1]`。
- `color` ：渐变轴颜色，具体可查看类型 [RGBA](/types/rgb.html#rgba)。

## ImageFilters
图片滤镜。

```
interface ImageFilters {
  contrast?: number;
  exposure?: number;
  highlights?: number;
  saturation?: number;
  shadows?: number;
  temperature?: number;
  tint?: number
  hue?: number
}
```

- `contrast`：对比度。
- `exposure` ：曝光。
- `highlights` ：高光。
- `saturation` ：饱和度。
- `shadows` ：阴影。
- `temperature` ：色温。
- `tint` ：色调。
- `hue` ：色相。 以上属性值域皆为 `[-1, 1]`。

OverflowDirection
PenNetwork