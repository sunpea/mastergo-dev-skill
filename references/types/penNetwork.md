# Pen
钢笔属性。

## PenNetwork
钢笔矢量网络属性。

```
interface PenNetwork {
  readonly ctrlNodes: ReadonlyArray<[number, number]>
  readonly nodes: ReadonlyArray<PenNetworkNode>
  readonly paths: ReadonlyArray<PenNetworkPath>
  readonly regions: ReadonlyArray<Region>
}
```

- `ctrlNodes`：控制点数组，数组元素为控制点坐标[x, y]，控制点主要用于二阶/三阶贝塞尔曲线绘制，路径无贝塞尔曲线线段则为空数组。
- `nodes`：端点数组，数组元素为端点信息。
- `paths`：线段数组，数组元素为线段的信息。
- `regions`：区域信息数组，元素表示为独立填充区域信息，若无独立填充区域则为空数组。

## PenNetworkNode
钢笔端点。

```
interface PenNetworkNode {
  readonly x: number
  readonly y: number
  readonly strokeCap: StrokeCap
  readonly cornerRadius: number
}
```

- `x`：端点横坐标。
- `y`：端点纵坐标。
- `strokeCap`：端点的装饰，具体可查看类型 [StrokeCap](/types/penNetwork.html#strokecap)。
- `cornerRadius`：端点的圆角。

## Region
钢笔的填充区域数组。

```
interface Region {
  readonly loops: number[][]
  readonly windingRule: WindingRule
}
```

- `loops`：填充区域数组，其元素描述独立填充的区域范围。loops[i]表示该填充区域所包含的封闭区域的“最大”闭环，loop[i][j]表示组成该封闭区域的边，值为paths的对应下标。
- `windingRule`：svg 填充规则，具体可查看类型 [WindingRule](/types/penNetwork.html#windingrule)。

## StrokeCap
端点的装饰。

```
type StrokeCap = 'NONE' | 'ROUND' | 'SQUARE' | 'LINE_ARROW' | 'TRIANGLE_ARROW' | 'ROUND_ARROW' | 'RING' | 'DIAMOND' | 'LINE'
```

- `NONE`: 正常。
- `ROUND`: 圆角。
- `SQUARE`: 方型。
- `LINE_ARROW`: 普通箭头。
- `TRIANGLE_ARROW`: 三角箭头。
- `ROUND_ARROW`: 圆形（实心）箭头。
- `RING`: 环形箭头。
- `DIAMOND`: 菱形箭头。
- `LINE`: 直线箭头。

## `PenNetworkPath`
钢笔路径的线段基础属性。

```
type PenNetworkPath = [number, number, number, number]
```

其值长度固定为4，其含义分别为[startNode, ctrlNode1. ctrlNode2, endNode]的装饰。

- `startNode`: 线段起点，值是nodes对应下标。
- `ctrlNode1`: 第一个控制点，值是`ctrlNodes`对应下标，若该线段不是贝塞尔曲线则为-1。
- `ctrlNode2`: 第二个控制点，值是`ctrlNodes`对应下标，若该线段不是三阶贝塞尔曲线则为-1。
- `endNode`: 线段终点，值是nodes对应下标。

## WindingRule

```
type WindingRule = 'Nonzero' | 'Evenodd'
```

- `Nonzero` ：非零规则。
- `Evenodd` ：奇偶规则。
svg 填充规则 fill-rule

Paint
PenPaths