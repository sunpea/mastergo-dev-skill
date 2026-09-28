# Font
文字。

```
interface Font {
  fontName: FontName
}
```

- `fontName` ：字体，具体可查看类型[FontName](/types/font.html#fontname)。

## FontName
字体名字。

```
interface FontName {
  readonly family: string
  readonly style: string
}
```

- `family` ：字族。
- `style` ：字重。

## FontAlias
字体别名。

```
interface FontAlias {
  title: string
  subtitle: string
}
```

- `title` ：字体标题。
- `subtitle` ：字体副标题。

FlowStartingPoint
Hyperlink