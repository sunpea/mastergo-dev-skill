# mg.clientStorage

- Type:

```
interface ClientStorageAPI {
  getAsync(key: string): Promise<any | undefined>
  setAsync(key: string, value: any): Promise<void>
  keysAsync(): Promise<string[]>
  deleteAsync(key: string): Promise<void>
}
```

mg.clientStorage 对象包含了用来在用户机器上完成数据本地持久化存储的方法。它类似于 Web 中的 loaclStorage API，但不同的是，clientStorage 是异步的。可以通过 clientStorage 来存储 object、array、string、number、boolean、null、undefined 以及 Uint8Array 等类型的数据。

> > **WARNING**
> 通过 mg.clientStorage 设置的数据不会跨用户共享。另外，当用户清除浏览器缓存时，通过 clientStorage 存储的数据可能被一同清除。

## `getAsync`

- Type: `getAsync(key: string): Promise`
根据指定的 key 读取数据。

## `setAsync`

- Type: `setAsync(key: string, value: any): Promise`
根据给定的 key 将 value 存储在 clientStorage 上。

## `keysAsync`

- Type: `keysAsync(): Promise`
获取存储在clientStorage上的所有key 。

## `deleteAsync`

- Type: `deleteAsync(key: string): Promise`
删除 clientStorage 上key对应的的数据。

mastergo.viewport
mastergo.WebSocket