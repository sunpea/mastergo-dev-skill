# Easing
Easing对象用于描述过渡效果。

```
interface Easing{
  readonly type: EasingType;
  readonly easingFunctionCubicBezier: {
    x1: number;
    x2: number;
    y1: number;
    y2: number;
  };
}
```

- `type`：过渡的类型，具体可查看类型 [EasingType](/types/easing.html#easingtype)。
- `easingFunctionCubicBezier`：自定义贝塞尔。

## EasingType

```
type EasingType = 'LINEAR' | 'EASE_IN' | 'EASE_OUT' | 'EASE_IN_AND_OUT' | 'EASE_IN_BACK' | 'EASE_OUT_BACK' | 'EASE_IN_AND_OUT_BACK' | 'CUSTOM_CUBIC_BEZIER'
```

- `LINEAR`：线性渐变。
- `EASE_IN`：缓入。
- `EASE_OUT`：缓出。
- `EASE_IN_AND_OUT`：缓入缓出。
- `EASE_IN_BACK`：后撤缓入。
- `EASE_OUT_BACK`：停滞缓出。
- `EASE_IN_AND_OUT_BACK`：弹性渐变。
- `CUSTOM_CUBIC_BEZIER`：自定义。

DropEvent
Effect