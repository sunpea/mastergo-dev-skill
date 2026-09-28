# TextListStyle
文字列表样式

## ListType
列表类型。

```
type ListType = 'ORDERED' | 'BULLETED' | 'NONE'
```

- `ORDERED` ：有序列表。
- `BULLETED` ：无序列表。
- `NONE` ：未设置列表样式。

## TextListStyle
文字列表样式。

```
type TextListStyle = {
  readonly type: listType
  readonly level: number
  readonly start: number
  readonly end: number
}
```

- `type` ： 列表样式的类型，具体可查看类型 [ListType](/types/textListStyle.html#listType)。
- `level` ： 列表央视的层级信息，取值为 0 - 4。
- `start` ： 列表样式开始的位置，从**0**开始。
- `end` ： 列表样式结束的位置。

TeamLibrary
TextSegStyle