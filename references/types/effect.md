# Effect
特效：阴影与模糊。

```
type Effect = ShadowEffect | BlurEffect | LiquidGlassEffect | MotionBlurEffect | ReferenceEffect;
```

## ShadowEffect
阴影。

```
interface ShadowEffect {
  readonly type: 'DROP_SHADOW' | 'INNER_SHADOW'
  readonly color: RGBA
  readonly offset: Vector
  readonly spread: number
  readonly radius: number
  readonly isVisible: boolean
  readonly blendMode: BlendMode
}
```

- `type` ：阴影类型，取值为 `DROP_SHADOW` 外阴影，或 `INNER_SHADOW` 内阴影。
- `color` ：阴影颜色。
- `offset` ：阴影的位置。
- `spread` ：扩张度。
- `radius` ：弧度。
- `isVisible` ：是否可见。
- `blendMode` ：混合模式，具体可查看类型 [`BlendMode`](/types/blend.html)。

## BlurEffect
模糊。

```
interface BlurEffect {
  readonly type: 'LAYER_BLUR' | 'BACKGROUND_BLUR'
  readonly radius: number
  readonly isVisible: boolean
  readonly blendMode: BlendMode
  readonly gradient: PluginGradientEffect
}

interface PluginGradientEffect {
  readonly mode: 'EVEN' | 'PROGRESSIVE';
  readonly gradientStops?: ReadonlyArray<PluginGradientStopItem>;
  readonly gradientHandlePositions?: [Point, Point];
  readonly transform?: Transform;
}

interface PluginGradientStopItem {
  readonly position: number;
  readonly value: number;
}

interface Point {
  readonly x: number;
  readonly y: number;
}
```

- `type` ：模糊类型，取值为 `LAYER_BLUR` 高斯模糊，或 `BACKGROUND_BLUR` 背景模糊。
- `radius` ：圆角。
- `isVisible` ：是否可见。
- `blendMode` ：混合模式，具体可查看类型 [`BlendMode`](/types/blend.html)
- `gradient` ：渐变模糊。
- `mode` ：渐变模式，取值为 `EVEN` 均匀模糊，或 `PROGRESSIVE` 渐进模糊。
- `gradientStops` ：渐变点和对应的值。
- `gradientHandlePositions` ：渐变位置。
- `transform` ：变换，具体可查看类型 [Transform](/types/transform.html)。

## LiquidGlassEffect
液态玻璃。

```
interface LiquidGlassEffect {
  readonly type: 'LIQUID_GLASS';
  readonly depth: number;
  readonly dispersion: number;
  readonly refraction: number;
  readonly lightIntensity: number;
  readonly lightAngle: number;
  readonly isVisible: boolean;
  readonly radius: number;
  readonly blendMode: BlendMode;
}
```

- `type` ：类型，取值为 `LIQUID_GLASS` 液态玻璃。
- `depth` ：深度。
- `dispersion` ：色散。
- `refraction` ：折射。
- `lightIntensity` ：强度 光强。
- `lightAngle` ：角度 光角度。
- `isVisible` ：是否可见。
- `blendMode` ：混合模式，具体可查看类型 [`BlendMode`](/types/blend.html)

## MotionBlurEffect
动感模糊。

```
interface MotionBlurEffect {
  readonly isVisible: boolean;
  readonly radius: number;
  readonly angle: number;
  readonly blendMode: BlendMode;
}
```

- `isVisible` ：是否可见。
- `radius` ：模糊半径。
- `angle` ：角度。
- `blendMode` ：混合模式，具体可查看类型 [`BlendMode`](/types/blend.html)

## ReferenceEffect
引用型特效。当样式的某个 mode 引用了另一个特效样式（style 引用 style）时，该 effect 项为引用类型，不携带具体特效值，仅保留被引用样式的信息。

```
interface ReferenceEffect {
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
- `reference` ：被引用的特效样式 id，可据此用 `mg.importStyleByKeyAsync` 或 `mg.getStyleById` 进一步解析。
- `referenceSource` ：解析后的源样式 id（经过引用链解析后的末端样式），可能与 `reference` 相同。
- `modeId` ：该引用项所属的模式 id。

Easing
ExportSettings