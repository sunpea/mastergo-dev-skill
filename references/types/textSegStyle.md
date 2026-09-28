# TextSegStyle

```
interface TextSegStyle {
  start: number;
  end: number;
  textStyleId: string;
  textStyle: {
    fontName: FontName;
    fontSize: number;
    fontWeight: number;
    letterSpacing: LetterSpacing;
    lineHeight: LineHeight;
    textDecoration: TextDecoration;
    textCase: TextCase;
    lineHeightByPx: number;
  };
  fillStyleId: string;
  fills: Paint[];
}
```

- `start` ： 文字样式开始的位置，从**0**开始。
- `end` ： 文字样式结束的位置。
- `textStyleId` ： 文字样式id。
- `textStyle` ： 文字样式。 `fontName` ：字体，具体可查看类型 [FontName](/types/font.html#fontname)。
- `fontSize` ：文字尺寸。
- `fontWeight` ：字重。
- `letterSpacing` ：字间距，具体可查看类型 [LetterSpacing](/types/textSegStyle.html#letterspacing)。
- `lineHeight` ：行高，具体可查看类型 [LineHeight](/types/textSegStyle.html#lineheight)。
- `lineHeightByPx`: 文字图层以px为单位的行高像素值.
- `textDecoration` ：文字装饰线，具体可查看类型 [TextDecoration](/types/textSegStyle.html#textdecoration)。
- `textCase` ：字母大小写，具体可查看类型 [TextCase](/types/textSegStyle.html#textcase)。

- `fillStyleId` 填充样式id。
- `fills` ： 文字填充，具体可查看类型 [Paint](/types/paint.html)。

## LetterSpacing
字间距。

```
type LetterSpacing = {
  readonly value: number
  readonly unit: 'PIXELS' | 'PERCENT'
}
```

- `value` ： 文字字间距值。
- `unit` ： 字间距单位，取值为 `PIXELS` 像素，或 `PERCENT` 百分比。

## LineHeight
文字行高。

```
type LineHeight =
| {
    readonly value: number
    readonly unit: 'PIXELS' | 'PERCENT'
  }
| {
    readonly unit: 'AUTO'
  }
```

- `value` ： 文字行高值。
- `unit` ： 行高单位，取值为 `PIXELS` 像素或 `PERCENT` 百分比，或 `AUTO`自动，当取值为 `AUTO` 自动时，则没有 `value` 属性。

## TextDecoration
装饰线。

```
type TextDecoration = 'NONE' | 'UNDERLINE' | 'STRIKETHROUGH'
```

- `NONE` ： 无装饰线。
- `UNDERLINE` ： 下划线。
- `STRIKETHROUGH` ： 删除线。

## TextCase
字母大小写。

```
type TextCase = 'ORIGINAL'
              | 'UPPER'
              | 'LOWER'
              | 'TITLE'
```

- `ORIGINAL` ： 正常。
- `UPPER` ： 全大写。
- `LOWER` ： 全小写。
- `TITLE` ： 首字母大写。

TextListStyle
Transform