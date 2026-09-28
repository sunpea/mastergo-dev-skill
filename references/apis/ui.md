# mg.ui
mg.ui 对象包含了用来操作用户界面并与用户界面进行信息交流的接口。

## `show`

- Type: `show(): void`
用于使 UI 界面可见。当调用 mg.showUI(__html__) 创建用户界面后，可以使用 mg.ui.show() 和 mg.ui.hide() 方法来改变 UI 界面的可见性。

## `hide`

- Type: `hide(): void`
与 mg.ui.show() 方法对立，hide() 方法用来是 UI 界面不可见，相当于 display: none。因此，用于实现 UI 界面的代码仍然可以继续运行。

## `resize`

- Type: `(width: number, height: number, withoutHeader?: boolean): void`
用来设置社区插件 UI 的尺寸
如果 withoutHeader 参数为 true，则 UI 界面的高度将不包含插件头部的高度。默认值为 false。

## `close`

- Type: `close(): void`
销毁 UI 界面。调用此方法会导致 <iframe> 被销毁，UI 界面无法再接收消息，<iframe> 内的代码将不再运行。

## `moveTo`

- Type: `moveTo(x: number, y: number): void`
用于设置插件ui视窗的定位，坐标原点为画布页面视窗的左上角，单位为像素值。

## `viewport`

- Type: `UIViewport`
可获取当前插件视窗的属性，包括定位和宽高等，具体可查看类型UIViewport。

## `postMessage`

- Type: `postMessage(message: any, origin?: string): void`
ui.postMessage 函数用于向用户界面（<iframe>）发送消息。第一个参数用于指定消息的内容，几乎可以是任何数据，只要该数据是可序列化的（serializable）对象。该限制与浏览器的 postMessage API 相同，可以参考：

- [浏览器的 `postMessage` API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
- [结构化克隆算法](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)
origin 参数是可选的，默认值为字符串 '*'。只有当 <iframe> 内的文档与 origin 匹配时才会发送消息。

## `onmessage`

- Type: `((pluginMessage: any, origin: string) => void) | undefined`
可以通过设置 mg.ui.onmessage 属性来监听由 UI 界面发送过来的消息事件。例如：

```
mg.ui.onmessage = (message, origin) => {
  // ...
}
```

事件处理函数接收两个参数：

- `message: any`：由 UI 界面发送的消息。
- `origin: string`：发送消息的文档的源。

## setHeaderVisible 私有化

- Type: `setHeaderVisible(visible: boolean): void`
用于设置插件 UI 是否显示头部。如果 visible 参数为 true，则显示头部；如果为 false，则隐藏头部。

## `setCloseConfirm`

- Type:

```
interface CloseConfirmOptions {
  enabled: boolean
  message?: string
}
setCloseConfirm(options: CloseConfirmOptions): void
```
设置插件关闭时的「离开挽留」。当插件中存在未保存的内容时，调用 enabled: true 声明需要挽留。开启后，用户点击插件关闭按钮或调用 mg.closePlugin() 时会弹出确认框；用户点击「确定关闭」后插件才真正关闭。「取消」则不关闭。宿主强制关闭（如切换编辑模式）不触发挽留。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `options.enabled` | `boolean` | 是 | `true` 开启关闭确认，`false` 关闭 |
| `options.message` | `string` | 否 | 自定义确认框文案，不传使用默认文案「当前有未保存的内容，确定要关闭插件吗？」 |

示例：

```
// 编辑器中有未保存内容时，开启挽留
mg.ui.setCloseConfirm({ enabled: true });

// 自定义挽留文案
mg.ui.setCloseConfirm({
  enabled: true,
  message: '有未保存的修改，确定关闭吗？',
});

// 内容保存完毕后关闭挽留
mg.ui.setCloseConfirm({ enabled: false });
```

mastergo.variables
mastergo.viewport