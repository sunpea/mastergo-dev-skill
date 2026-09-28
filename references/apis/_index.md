# API Reference
MasterGo 的插件代码运行在受限的沙盒中，你无法在插件代码中访问浏览器 API。但我们仍然为你暴露了一些非常有用且常用的全局 API。

## [mg](./mastergo.html)
大部分插件 API 都需要通过全局变量 mg 来访问，包括对节点的增删改查等操作。例如：

```
mg.createRectangle
mg.clientStorage
```

## `setTimeout`

- Type: `function setTimeout(callback: Function, timeout: number): number`
设置一个定时器，当到期时执行指定的回调函数。参考：https://developer.mozilla.org/en-US/docs/Web/API/setTimeout。

## `setInterval`

- Type: `function setInterval(callback: Function, timeout: number): number`
设置一个定时器，会在指定的时间间隔内重复地调用回调函数。参考：https://developer.mozilla.org/en-US/docs/Web/API/setInterval。

## `clearTimeout`

- Type: `function clearTimeout(timeoutID: number): void`
清除由 setTimeout 函数创建的定时器。参考：https://developer.mozilla.org/en-US/docs/Web/API/clearTimeout。

## `clearInterval`

- Type: `function clearInterval(timeoutID: number): void`
清除由 setInterval 函数创建的定时器。参考：https://developer.mozilla.org/en-US/docs/Web/API/clearInterval。

## `requestAnimationFrame`

- Type: `function requestAnimationFrame(cb: (ts: number) => void): number`
请求动画帧。参考：https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame。

## `cancelAnimationFrame`

- Type: `function cancelAnimationFrame(requestID: number): void`
清除/取消由 requestAnimationFrame 请求的动画帧。参考：https://developer.mozilla.org/en-US/docs/Web/API/Window/cancelAnimationFrame。

## `console`

- Type:

```
interface Console {
  log(message?: any, ...optionalParams: any[]): void
  error(message?: any, ...optionalParams: any[]): void
  assert(condition?: boolean, message?: string, ...data: any[]): void
  info(message?: any, ...optionalParams: any[]): void
  warn(message?: any, ...optionalParams: any[]): void
  clear(): void
}
```

参考：https://developer.mozilla.org/en-US/docs/Web/API/console。

mastergo