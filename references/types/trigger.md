# Trigger
Trigger类型表示触发行为，delay表示触发的延时，单位为毫秒，在type不为AFTER_DELAY是，dalay为0。

```
interface Trigger {
  readonly type: TriggerType;
  readonly delay: number;
}
```

- `type`：触发行为的类型。
- `delay`：延时。

## TriggerType

```
type TriggerType = 'ON_CLICK' | 'ON_DRAG' | 'ON_HOVER' | 'ON_PRESS' | 'MOUSE_ENTER' | 'MOUSE_LEAVE' | 'MOUSE_DOWN' | 'MOUSE_UP' | 'AFTER_DELAY'
```

- `ON_CLICK`：点击。
- `ON_HOVER`：悬停。
- `ON_PRESS`：按下。
- `ON_DRAG`：拖拽。
- `MOUSE_DOWN`：按下鼠标。
- `MOUSE_UP`：抬起鼠标。
- `MOUSE_ENTER`：光标移入。
- `MOUSE_LEAVE`：光标移出。
- `AFTER_DELAY`：延时。

Transition
UIViewport