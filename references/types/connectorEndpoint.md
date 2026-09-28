# ConnectorEndpoint
连接线端点代表连接线的两个端点，当连接点没有连接图层时，其类型为ConnectorEndpointPosition，当连接点有连接图层时，其类型为ConnectorEndpointConnected。

```
type ConnectorEndpoint =
| ConnectorEndpointPosition
| ConnectorEndpointConnected
```

## ConnectorEndpointPosition
连接点没有连接图层

```
interface ConnectorEndpointPosition {
    // 相对画布的坐标
	position: { x: number; y: number }
}
```

## ConnectorEndpointConnected
连接点有连接图层

```
interface ConnectorEndpointConnected {
  position: { x: number; y: number }
  endpointNodeId: string
  magnet: 'TOP' | 'LEFT' | 'BOTTOM' | 'RIGHT'
```

- `position` : 相对于连接线的坐标。
- `endpointNodeId` : 连接图层id。
- `magnet` : 连接到图层的位置。

ComponentPropertiesRelated
Constraints