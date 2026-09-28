# Constraints
约束

```
interface Constraints {
    readonly horizontal: ConstraintType
    readonly vertical: ConstraintType
  }
```

- `horizontal` ：水平方向的约束。
- `vertical` ：垂直方向的约束。

## ConstraintType
约束类型

```
type ConstraintType = 'START' | 'END' | 'STARTANDEND' | 'CENTER' | 'SCALE'
```

- `START` ：当方向为水平方向时，`START`表示靠左固定，即保持对象距离容器左侧的距离不变；当方向为垂直方向时，`START`表示顶端固定，即保持图像距离容器顶部的距离不变。
- `END` ：当方向为水平方向时，`END`表示靠左固定，即保持对象距离容器右侧的距离不变；当方向为垂直方向时，`END`表示底部固定，即保持图像距离容器底部的距离不变。
- `STARTANDEND` ：当方向为水平方向时，`STARTANDEND`表示左右固定，即保持对象距离容器左右两侧的距离不变；当方向为垂直方向时，`STARTANDEND`表示上下固定即保持图像距离容器顶部和底部的距离不变。
- `CENTER` ：居中，保持图像在容器中居中。
- `SCALE` ：跟随缩放，缩放时将以百分比形式固定图像方向上的大小和位置。

ConnectorEndpoint
DropEvent