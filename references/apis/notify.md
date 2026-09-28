# mg.notify

- Type:

```
notify(message: string, options?: NotifyOptions): NotificationHandler
```

该方法可在画布中展示一条通知消息。

## NotifyOptions

- Type:

```
interface NotifyOptions {
  position?: 'top' | 'bottom'
  type?: 'normal' | 'highlight' | 'error' | 'warning' | 'success'
  timeout?: number
  isLoading?: boolean
}
```

- `position`：设置通知的位置，默认为`'top'`。
- `type`：设置通知的类型，默认为`'normal'`。
- `timeout`：设置通知的存在时间，单位为ms，默认为3000。
- `isLoading`：是否显示loading图标，默认为`false`。
notify的第二个参数，设置可指定通知的类型、弹出位置、显示时间和是否为loading，例如：

```
mg.notify("出错了", {
  type: "error",
  position: "bottom",
  timeout: 3000,
  isLoading: false,
});
```

## NotificationHandler

- Type：

```
interface NotificationHandler {
  cancel: () => void
}
```

mg.notify 方法的返回值，可通过调用cancel方法立即关闭notify方法生成的通知实例。例如：

```
// 设置了30s的loading提示
const notifyInstance = mg.notify("加载中", {isLoading: true, timeout: 30 * 1000});

// 2s后关闭
setTimeout(() => {
  notifyInstance.cancel(); // 关闭
}, 2000)
```

mastergo.WebSocket
mastergo.codegen