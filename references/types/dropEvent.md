# DropEvent
主线程drop事件回调参数

```
interface DropEvent {
  x: number
  y: number
  absoluteX: number
  absoluteY: number
  dropMetadata?: any
}
```

- `x` ：相对于画布左上角的页面定位x坐标。
- `y` ：相对于画布左上角的页面定位y坐标。
- `absoluteX` ：画布内x坐标。
- `absoluteY` ：画布内y坐标。
- `dropMetadata` ：来源于插件ui传输的原始数据。

## PluginDrop
ui触发drop事件pluginDrop类型。

```
interface PluginDrop {
  clientX: number
  clientY: number
  dropMetadata?: any
}
```

- `clientX` ： 原生事件的clientX，需要注意原点为文件页面左上角，而不是ui左上角。
- `clientY` ： 原生事件的clientY。
- `dropMetadata` ： 拖拽事件的原始数据。

Constraints
Easing