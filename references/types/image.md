# Image
图片。

```
interface Image {
  href: string,
  getBytesAsync(): Promise<Uint8Array>
}
```

- `href` ：图片链接。
- `getBytesAsync()` ：异步获取图片的数据。

Hyperlink
LayoutGrid