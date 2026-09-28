# ArcData

```
interface ArcData {
  readonly startingAngle: number
  readonly endingAngle: number
  readonly innerRadius: number
}
```

ArcData属性描述椭圆的弧度属性，包括startingAngle（起点弧度），endingAngle（终点弧度）和innerRadius（内径），与画布面板关系如下：

其中innerRadius与面板中内径相同，startingAngle为面板起点角度对应的弧度，endingAngle与面板弧度的转换关系为 弧度 = (endingAngle - startingAngle) / 2π * 100%。
可以通过赋值ArcData对象，改变椭圆的弧度属性获得指定图形，例如：

```
// 圆环
ellipseNode.arcData = {innerRadius: 0.5, startingAngle: 0, endingAngle: 2 * Math.PI}
```

```
// 半圆
ellipseNode.arcData = {innerRadius: 0, startingAngle: 0, endingAngle: Math.PI}
```

Action
BlendMode