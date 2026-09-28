# Action

```
interface Action {
  readonly type: ActionType;
  readonly destinationId: string;
  readonly navigation: Navigation;
  readonly transition: Transition;
  readonly url: string;
  readonly scrollToXOffset?: number;
  readonly scrollToYOffset?: number;
}
```

- `type` ：原型交互动作类型。
- `navigation` ：原型交互动作，具体可查看类型[Navigation](/types/action.html#navigation)。
- `destinationId` ：原型交互目标图层的id。
- `transition` ：原型交互的动画属性，具体可查看类型[Transition](/types/transition.html)。
- `url` ：原型交互动作是打开链接时，设置的url。
- `scrollToXOffset` ：原型交互动作是容器内滚动时，设置的横向缩进。
- `scrollToYOffset` ：原型交互动作是容器内滚动时，设置的纵向缩进。

## ActionType

```
type ActionType = 'BACK' | 'NODE'| 'URL'| 'CLOSE'| 'NONE';
```

- `BACK`： 返回上一级。
- `NODE`： 浮层行为相关，根据不同navigation取值，交互动作不同。 `NAVIGATE`：前往某个目标容器。
- `OVERLAY`：打开浮层。
- `SWAP_OVERLAY`：替换浮层。
- `SCROLL_TO`：容器内滚动，设置成该动作时，可设置对应的缩进值。

- `URL`： 打开链接。
- `CLOSE`： 关闭浮层。
- `NONE`： 无任何动作。

## Navigation
原型交互动作

```
type  Navigation =  'NAVIGATE' | 'OVERLAY' | 'SWAP_OVERLAY' | 'SCROLL_TO';
```

- `NAVIGATE`：前往某个目标容器。
- `OVERLAY`：打开浮层。
- `SWAP_OVERLAY`：替换浮层。
- `SCROLL_TO`：容器内滚动，设置成该动作时，可设置对应的缩进值。

TypeScript Types
ArcData