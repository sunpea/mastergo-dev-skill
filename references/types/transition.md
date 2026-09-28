# Transition
动画效果。

```
interface Transition {
  readonly type: TransitionType;
  readonly duration: number;
  readonly direction: TransitionDirection;
  readonly easing: Easing;
}
```

- type：动画类型，具体可查看类型 [TransitionType](/types/transition.html#transitiontype)。
- duration：动画持续时间。
- direction： 动画执行方向，具体可查看类型 [TransitionDirection](/types/transition.html#transitiondirection)。
- easing：动画过渡效果，具体可查看类型 [Easing](/types/easing.html)。

## TransitionType
动画类型。

```
type TransitionType = 'TANS_NONE' | 'INSTANT' | 'DISSOLVE' | 'SMART_ANIMATE' | 'MOVE_IN' | 'MOVE_OUT' | 'PUSH' | 'SLIDE_IN' | 'SLIDE_OUT' | 'DISPLACE'
```

- `INSTANT`：即时。
- `DISSOLVE`：溶解。
- `SLIDE_IN`：滑入。
- `SLIDE_OUT`：滑出。
- `MOVE_IN`：移入。
- `MOVE_OUT`：移出。
- `PUSH`：推入。
- `SMART_ANIMATE`：智能动画。
- `DISPLACE`：位移。

## TransitionDirection

```
type TransitionDirection = 'LEFT' | 'RIGHT' | 'TOP' | 'BOTTOM'
```

- `LEFT`：向左。
- `RIGHT`：向右。
- `TOP`：向上。
- `BOTTOM`：向下。

Transform
Trigger