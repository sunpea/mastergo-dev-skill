# Hyperlink
超链接。

```
interface Hyperlink {
  type: 'PAGE' | 'NODE' | 'URL'
  value: string
}
```

表示超链接目标的对象。类型的可能值为：

- `PAGE` ：超链接对象为一个页面。value值为当前文件中的pageId。
- `NODE` ：超链接对象为一个**容器**节点。value值为当前文件中的frameId。
- `URL` ：超链接对象为一个链接。value值为任意url。

## HyperlinkWithRange
分段超链接。

```
interface HyperlinkWithRange {
  start: number
  end: number
  hyperlink: Hyperlink
}
```

- `start` ：分段开始的位置。
- `end` ：分段结束的位置。
- `hyperlink` ：超链接对象，具体可查看类型 [Hyperlink](/types/hyperlink.html)。

Font
Image