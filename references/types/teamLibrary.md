# TeamLibrary
已订阅的团队库数据，包含所有可用的组件和样式。

```
interface TeamLibraryItem {
  readonly name: string;
  readonly id: string;
  readonly componentList: TeamLibraryComponent[]
  readonly style: {
    paints: ReadonlyArray<TeamLibraryStyle>
    effects: ReadonlyArray<TeamLibraryStyle>
    texts: ReadonlyArray<TeamLibraryStyle>
    grids: ReadonlyArray<TeamLibraryStyle>
    strokeWidths: ReadonlyArray<TeamLibraryStyle>
    cornerRadiuses: ReadonlyArray<TeamLibraryStyle>
    paddings: ReadonlyArray<TeamLibraryStyle>
    spacings: ReadonlyArray<TeamLibraryStyle>
    numbers: ReadonlyArray<TeamLibraryStyle>
    strings: ReadonlyArray<TeamLibraryStyle>
    bools: ReadonlyArray<TeamLibraryStyle>
    colors: ReadonlyArray<TeamLibraryStyle>
  }
}

type TeamLibrary = ReadonlyArray<TeamLibraryItem>
```

- `componentList` ：组件列表，具体可查看类型 [TeamLibraryComponent](/types/teamLibrary.html#teamlibrarycomponent)。
- `style` ：样式对象，其中每个字段的值皆为 `TeamLibraryStyle` 数组，具体可查看类型 [TeamLibraryStyle](/types/teamLibrary.html#teamlibrarystyle)。`numbers`/`strings`/`bools`/`colors` 对应变量类型的样式。

## PublishedTeamLibrary
当前文件发布的团队库内容，由 getPublishedTeamLibraryAsync 返回。当前文件未发布团队库，或当前用户没有查询权限时返回 null。

```
interface PublishedTeamLibrary extends TeamLibraryItem {
  readonly version?: number
  readonly organizationId?: string | number
  readonly teamId?: string | number
  readonly teamLibType?: string | number
  readonly dsmSettings?: {
    readonly frameworkType?: string
    readonly componentTemplate?: string
  }
  readonly collections: ReadonlyArray<PublishedTeamLibraryCollection>
}

interface PublishedTeamLibraryCollection {
  readonly id: string
  readonly name: string
  readonly key?: string
  readonly modes: ReadonlyArray<{
    readonly id: string
    readonly name: string
  }>
}
```

- `componentList`：当前文件发布的组件和组件集。
- `style`：当前文件发布的样式和变量，字段结构与 `TeamLibrary.style` 一致。
- `collections`：当前文件发布的变量集合及其模式。

## TeamLibraryComponent
团队库组件/组件集。

```
interface TeamLibraryComponent {
  readonly id: string;
  readonly name: string;
  readonly ukey: string;
  readonly description: string;
  readonly type: "COMPONENT" | "COMPONENT_SET"
  readonly cover: string
  readonly width: number
  readonly height: number
  /** 如果 Component 属于某一个 ComponentSet，则 componentSetUkey 为 ComponentSet 的 ukey，否则为空字符串 */
  readonly componentSetUkey: string
  /** 组件所在容器的名称；未设置时可能缺省 */
  readonly frameName?: string
  /** 组件属性 / 变体属性，对齐 ComponentPropertyValue 结构；老库可能缺省 */
  readonly properties?: ComponentPropertyValue[]
  /** 组件所有后代 TEXT 图层的名称（去重）；老库可能缺省 */
  readonly textNodeNames?: string[]
}
```

- `width` ：组件宽度，部分旧的团队库宽度可能为0。
- `height` ：组件高度，部分旧的团队库高度可能为0。
- `properties` ：组件属性（含变体属性、组件状态等），结构为 [ComponentPropertyValue](/types/componentPropertiesRelated.html#componentpropertyvalue) 数组。**老库（该字段上线前发布的）可能缺省**，使用前请判断。
- `textNodeNames` ：组件内部所有后代 TEXT 图层的名称（已去重）。可用于组件文档、属性占位符识别等场景。**老库可能缺省**。

## TeamLibraryStyle
团队库样式/变量。

```
interface TeamLibraryStyle {
  readonly id: string;
  readonly name: string;
  readonly ukey: string;
  readonly description: string;
  readonly type: StyleType;
  /** 变量所属集合的 id，仅在变量类型（color/number/string/bool）上存在 */
  readonly collectionId?: string;
  /** 变量所属集合的名称 */
  readonly collectionName?: string;
  /** 各模式下的样式值列表，元素结构为 { modeId, modeName, value }；老库可能缺省 */
  readonly values?: ReadonlyArray<TeamLibraryStyleValue>
  /** 代码语法（web/android/ios），来自发布时 cover；老库可能缺省 */
  readonly codeSyntax?: { web?: string; android?: string; ios?: string }
}

interface TeamLibraryStyleValue {
  readonly modeId: string;
  readonly modeName: string;
  /** 该模式下的样式值，形态随 style 类型变化，见下方说明 */
  readonly value: any;
}
```

- `type` ：样式类型，具体可查看类型 [StyleType](/types/style.html#styletype)。
- `collectionId` ：变量所属集合的 id，仅在变量类型上存在。可通过此字段按集合分组变量。
- `collectionName` ：变量所属集合的名称。
- `values` ：样式在各模式下的值列表，每项为 `{ modeId, modeName, value }`。**老库（该字段上线前发布的）可能缺省**。
- `codeSyntax` ：变量的代码语法，结构为 `{ web?, android?, ios? }`。仅在变量类型（color/number/string/bool）上可能存在。**老库（该字段上线前发布的）可能缺省**。

### values 中 value 的形态
value 字段的形态随该样式所属的 style 分类变化：

| 样式分类 | value 形态 |
|---|---|
| `paints` | `Paint[]`（完整填充对象数组，含 color/alpha/blendMode/gradient/image 等） |
| `effects` | `Effect[]`（完整效果对象数组） |
| `texts` | 文本样式对象数组 |
| `grids` | `LayoutGrid[]` |
| `colors` | `Paint[]`（由变量化颜色的 floatData `[r,g,b,a]` 转换得到，与 paints 结构对齐） |
| `strokeWidths` / `numbers` / `spacings` / `paddings` / `cornerRadiuses` | `number[]`（来自 floatData） |
| `strings` | `string` |
| `bools` | `boolean` |

> **注意**：当样式为变量引用项（reference 且样式属于变量化样式），或解析过程中出现异常时，对应的 mode 项仍会保留在 `values` 数组中，但 `value` 字段为 `undefined`。使用时应先判断 `value` 是否存在。

## PublishStatus
描述可发布到团队库的元素（即样式和组件）的状态。

```
type PublishStatus = "UNPUBLISHED" | "CURRENT" | "CHANGED"
```

可能的值为：

- `UNPUBLISHED`：未发布到团队库.
- `CURRENT`：已发布，已发布版本与本地版本匹配。
- `CHANGED`：已发布，但具有本地更改。

## DocumentationLink
组件文档链接。uri应该是一个有效的uri(例如https://mastergo.com)。

```
interface DocumentationLink {
  readonly uri: string
}
```

Style
TextListStyle