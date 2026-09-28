# Reaction
用于描述原型交互的相关信息

```
interface Reaction {
  readonly trigger: Trigger;
  readonly action?: Action;
}
```

- `trigger`：触发行为，具体可查看类型 [Trigger](/types/trigger.html)。
- `action`：原型交互动作，具体可查看类型 [Action](/types/action.html)。

PenPaths
Rect