# mg.variables
下面给出的属性和方法可以通过全局对象 mg.variables 来访问，用于管理 MasterGo 中的设计变量（Design Variables）。

## 变量集合

### `getCollections`

- Type: `(includeExternal?: boolean) => Collection[]`
获取所有变量集合。可选参数 includeExternal 默认为 false，设为 true 可包含外部集合。

```
const collections = mg.variables.getCollections();
const allCollections = mg.variables.getCollections(true);
```

### `getCollectionById`

- Type: `(id?: string) => Collection | null`
通过 ID 获取单个集合。不传 ID 时返回当前选中的集合。

```
const collection = mg.variables.getCollectionById('collectionId');
```

### `createCollection`

- Type: `(name?: string) => Promise`
创建新的变量集合。不传名称时使用默认名称。

```
const collection = await mg.variables.createCollection('我的颜色变量');
```

### `renameCollection`

- Type: `(id: string, name: string) => void`
重命名集合。

```
mg.variables.renameCollection('collectionId', '新名称');
```

### `deleteCollection`

- Type: `(id: string) => void`
删除集合。

```
mg.variables.deleteCollection('collectionId');
```

### `moveCollection`

- Type: `(collectionId: string, options?: { afterId?: string; index?: number }) => void`
集合排序，支持两种方式：

- `afterId`：插入到指定集合之后
- `index`：插入到指定索引位置（0 为首位）

```
mg.variables.moveCollection('collectionId', { afterId: 'otherCollectionId' });
mg.variables.moveCollection('collectionId', { index: 0 });
```

### Collection 类型

```
interface Collection {
  id: string
  name: string
  isExternal: boolean
  modes: Mode[]
}
```

## 变量模式

### `getModes`

- Type: `(collectionId?: string) => Mode[]`
获取指定集合的所有模式。不传 collectionId 时使用当前集合。

```
const modes = mg.variables.getModes('collectionId');
```

### `getModeById`

- Type: `(collectionId?: string, modeId?: string) => Mode | null`
通过 ID 获取单个模式。

```
const mode = mg.variables.getModeById('collectionId', 'modeId');
```

### `addMode`

- Type: `(collectionId: string, name?: string) => Promise`
为集合添加新模式。返回新创建的模式对象。

```
const newMode = await mg.variables.addMode('collectionId', 'Dark Mode');
```

### `renameMode`

- Type: `(collectionId: string, modeId: string, name: string) => void`
重命名模式。

```
mg.variables.renameMode('collectionId', 'modeId', '新模式名');
```

### `deleteMode`

- Type: `(collectionId: string, modeId: string) => void`
删除模式。

```
mg.variables.deleteMode('collectionId', 'modeId');
```

### `setVariableMode`

- Type: `(collectionId: string, modeId: string) => void`
切换当前集合的变量模式。

```
mg.variables.setVariableMode('collectionId', 'modeId');
```

### `setPageVariableMode`

- Type: `(collectionId: string, modeId: string, pageId?: string) => void`
设置指定页面的变量模式。不传 pageId 则使用当前页面。

```
mg.variables.setPageVariableMode('collectionId', 'modeId');
mg.variables.setPageVariableMode('collectionId', 'modeId', 'pageId');
```

### `getLayerVariableModes`

- Type: `(layerId: string) => LayerVariableMode[]`
获取指定图层上使用的变量集合及其生效模式。返回数组中每一项对应图层使用到的一个变量集合：

- `modeId` 为当前实际生效（渲染）的模式 id
- `modeName` 为生效模式的名称，从集合的模式列表中解析（团队库集合同样支持）；`modeId` 为 `null`（多值）或模式已被删除等无法解析时缺失
- `isExplicit` 为 `true` 表示该图层通过 `setVariableMode` 或右侧面板显式指定了模式；为 `false` 表示跟随父级/页面默认（自动）
- 跟随父级时可通过 `parentModeId` 获取父级的模式 id

```
const modes = mg.variables.getLayerVariableModes(node.id);
modes.forEach((item) => {
  console.log(item.collectionId, item.modeId, item.modeName, item.isExplicit);
});
// → '47:492' '1:6' '模式 1' false
```

### Mode 类型

```
interface Mode {
  id: string
  name: string
  collectionId: string
}

interface LayerVariableMode {
  /** 集合 id */
  collectionId: string
  /** 当前实际生效（渲染）的模式 id，为 null 时表示多值 */
  modeId: string | null
  /** 模式名称，modeId 为 null 或模式无法解析时缺失 */
  modeName?: string
  /** 是否为图层显式指定的模式，false 表示跟随父级（自动） */
  isExplicit: boolean
  /** 跟随父级时，父级的模式 id */
  parentModeId: string | null
}
```

## 变量分组

### `getGroupList`

- Type: `(collectionId?: string) => GroupNode[]`
获取指定集合下的变量分组树。

```
const groups = mg.variables.getGroupList('collectionId');
```

### `createGroup`

- Type: `(collectionId: string, variableIds: string[], groupName?: string) => void`
创建变量分组。

```
const boolIds = mg.variables.getVariables({ type: 'BOOLEAN' }).map(v => v.id);
mg.variables.createGroup('collectionId', boolIds, '布尔变量组');
```

### `addVariablesToGroup`

- Type: `(collectionId: string, groupPath: string, variableIds: string[]) => void`
将变量添加到已有分组中。

```
mg.variables.addVariablesToGroup('collectionId', '分组路径', ['varId1', 'varId2']);
```

### `removeVariablesFromGroup`

- Type: `(collectionId: string, groupPath: string, variableIds: string[]) => void`
将变量从分组中移除。

```
mg.variables.removeVariablesFromGroup('collectionId', '分组路径', ['varId1']);
```

### `renameGroup`

- Type: `(collectionId: string, newName: string, groupPath?: string, variableIds?: string[]) => void`
重命名分组。可通过 groupPath 或 variableIds 指定要重命名的分组。

```
mg.variables.renameGroup('collectionId', '新名称', '旧分组路径');
mg.variables.renameGroup('collectionId', '新名称', null, ['varId1', 'varId2']);
```

### `disbandGroup`

- Type: `(collectionId: string, groupPath?: string, variableIds?: string[]) => void`
解散分组（变量不会被删除，只是取消分组）。

```
mg.variables.disbandGroup('collectionId', '分组路径');
mg.variables.disbandGroup('collectionId', null, ['varId1', 'varId2']);
```

### `deleteGroup`

- Type: `(collectionId: string, groupPath?: string, variableIds?: string[]) => void`
删除分组（同时删除分组内所有变量）。

```
mg.variables.deleteGroup('collectionId', '分组路径');
mg.variables.deleteGroup('collectionId', null, ['varId1', 'varId2']);
```

### GroupNode 类型

```
interface GroupNode {
  id: string
  name: string
  currentPath?: string
  level: number
  isLeaf: boolean
  children?: GroupNode[]
}
```

## 变量管理

### `getVariables`

- Type: `(options?: { collectionId?: string; groupPath?: string; type?: PluginVariableType; scopeType?: string }) => Variable[]`
获取文件中的所有本地变量，支持以下过滤条件：

- `collectionId`：按集合过滤
- `groupPath`：按分组路径过滤
- `type`：按变量类型过滤
- `scopeType`：按作用域过滤

```
// 获取所有变量
const allVars = mg.variables.getVariables();

// 获取指定集合下的变量
const collectionVars = mg.variables.getVariables({ collectionId: 'colId' });

// 获取指定分组下的变量
const groupVars = mg.variables.getVariables({ groupPath: '布尔变量组' });

// 获取指定类型的变量
const colorVars = mg.variables.getVariables({ type: 'COLOR' });
const boolVars = mg.variables.getVariables({ type: 'BOOLEAN', collectionId: 'colId' });
```

### `getVariableById`

- Type: `(id: string) => Variable | null`
通过 ID 获取单个变量。

```
const variable = mg.variables.getVariableById('variableId');
```

### `createVariable`

- Type: `(options: CreateVariableOptions) => Promise`
创建新变量。支持创建单值变量（BOOLEAN / NUMBER / STRING / COLOR）和复合样式变量（PAINT / TEXT / EFFECT / GRID / STROKE_WIDTH / CORNER_RADIUS / PADDING）。

```
// 创建布尔变量
const boolVar = await mg.variables.createVariable({
  name: 'isDarkMode',
  type: 'BOOLEAN',
  value: true,
  description: '是否暗色模式',
  collectionId: 'colId',
});

// 创建数值变量
const numVar = await mg.variables.createVariable({
  name: 'spacing',
  type: 'NUMBER',
  value: 8,
  collectionId: 'colId',
});

// 创建字符串变量
const strVar = await mg.variables.createVariable({
  name: 'buttonText',
  type: 'STRING',
  value: 'Click me',
  collectionId: 'colId',
});

// 创建颜色变量（rgba 格式，值范围 0-1）
const colorVar = await mg.variables.createVariable({
  name: 'primaryColor',
  type: 'COLOR',
  value: { r: 0.2, g: 0.4, b: 0.8, a: 1 },
  collectionId: 'colId',
});

// 创建复合样式变量（不需要传 value，创建后默认为空样式）
const paintVar = await mg.variables.createVariable({
  name: '填充样式',
  type: 'PAINT',
  collectionId: 'colId',
});

const textVar = await mg.variables.createVariable({
  name: '文字样式',
  type: 'TEXT',
  collectionId: 'colId',
});
```

CreateVariableOptions 类型：

```
interface CreateVariableOptions {
  name: string
  type: PluginVariableType
  value?: any
  description?: string
  collectionId?: string
}
```

### `renameVariable`

- Type: `(id: string, newName: string) => void`
重命名变量。

```
mg.variables.renameVariable('variableId', '新变量名');
```

### `deleteVariable`

- Type: `(id: string) => void`
删除变量。

```
mg.variables.deleteVariable('variableId');
```

### `moveVariable`

- Type: `(variableId: string, options?: { afterId?: string; index?: number }) => Promise`
排序变量，支持两种方式：

- `afterId`：插入到指定变量之后
- `index`：插入到指定索引位置（0 为首位）

```
await mg.variables.moveVariable('variableId', { afterId: 'otherVarId' });
await mg.variables.moveVariable('variableId', { index: 0 });
```

### `addVariableValue`

- Type: `(options: { id: string; value?: any; modeId: string }) => Promise`
为复合样式变量（PAINT / EFFECT / GRID）新增子项。不传 value 时添加默认子项。

```
// 新增一个填充子项（默认灰色）
await mg.variables.addVariableValue({ id: 'paintVarId', modeId: 'modeId' });

// 新增一个指定颜色的填充子项
await mg.variables.addVariableValue({
  id: 'paintVarId',
  value: { type: 0, color: { r: 1, g: 0, b: 0, a: 1 } },
  modeId: 'modeId',
});
```

### `deleteVariableValue`

- Type: `(options: { id: string; index: string | string[]; modeId: string }) => Promise`
删除复合样式变量的子项。支持单个或批量删除。

```
// 删除单个子项
await mg.variables.deleteVariableValue({ id: 'paintVarId', index: '741:0', modeId: 'modeId' });

// 批量删除子项
await mg.variables.deleteVariableValue({ id: 'paintVarId', index: ['741:0', '741:1'], modeId: 'modeId' });
```

### `getVariableIndexes`

- Type: `(variableId: string, modeId?: string) => string[]`
获取复合样式变量（PAINT / EFFECT / GRID）在某模式下的子项 index 列表。不传 modeId 时使用集合的第一个模式。

```
const indexes = mg.variables.getVariableIndexes('paintVarId');
const indexesWithMode = mg.variables.getVariableIndexes('paintVarId', 'modeId');
```

### PluginVariableType
变量类型枚举：

| 类型 | 值 | 说明 |
|---|---|---|
| BOOLEAN | `'BOOLEAN'` | 布尔变量 |
| NUMBER | `'NUMBER'` | 数值变量 |
| STRING | `'STRING'` | 字符串变量 |
| COLOR | `'COLOR'` | 颜色变量 |
| PAINT | `'PAINT'` | 填充样式变量（复合） |
| TEXT | `'TEXT'` | 文本样式变量（复合） |
| EFFECT | `'EFFECT'` | 特效样式变量（复合） |
| GRID | `'GRID'` | 网格样式变量（复合） |
| STROKE_WIDTH | `'STROKE_WIDTH'` | 描边宽度样式变量（复合） |
| CORNER_RADIUS | `'CORNER_RADIUS'` | 圆角样式变量（复合） |
| PADDING | `'PADDING'` | 内边距样式变量（复合） |

### Variable 类型

```
interface Variable {
  id: string
  name: string
  description: string
  alias: string
  type: PluginVariableType
  collectionId: string
  isExternal: boolean
  supportScope: boolean
  codeSyntax?: { web?: string; android?: string; ios?: string }
  scopes?: string[]
  modes: Record<string, any[]>
}
```

## 变量值

### `setVariableValue`

- Type: `(options: { id: string; value: any; modeId?: string }) => Promise`
修改变量值并等待数据刷新完成。对于复合样式变量（PAINT / EFFECT / TEXT / GRID / STROKE_WIDTH / CORNER_RADIUS / PADDING），value 支持部分更新，即只需要传要修改的字段。

```
// 修改布尔变量值
mg.variables.setVariableValue({ id: 'varId', modeId: 'modeId', value: true });

// 修改数值变量值
mg.variables.setVariableValue({ id: 'varId', modeId: 'modeId', value: 12 });

// 修改字符串变量值
mg.variables.setVariableValue({ id: 'varId', modeId: 'modeId', value: 'new text' });

// 修改颜色变量值
mg.variables.setVariableValue({
  id: 'varId',
  modeId: 'modeId',
  value: { r: 1, g: 1, b: 1, a: 1 },
});
```

#### 复合样式变量值格式
填充变量（PAINT）值结构：
modes[modeId] 是一个数组，每个元素代表一个填充项：

| 字段 | 类型 | 说明 |
|---|---|---|
| type | number | 0=纯色, 1=线性渐变, 2=径向渐变, 3=旋转渐变, 4=菱形渐变, 5=图片 |
| color |  | 颜色值（0-1 范围） |
| alpha | number | 透明度 |
| blendMode | string | 混合模式 |
| isVisible | boolean | 是否可见 |
| index | string | 子项索引（用于定位具体哪个填充项） |
| colorStyleId | string | 颜色引用 ID |

```
// 修改为纯色（不传 index 时自动匹配 type=0 的填充项）
mg.variables.setVariableValue({
  id: 'paintVarId',
  value: { type: 0, color: { r: 1, g: 0, b: 0, a: 1 } },
  modeId: 'modeId',
});

// 指定 index 修改特定填充项
mg.variables.setVariableValue({
  id: 'paintVarId',
  value: { index: '612:1', type: 0, color: { r: 0, g: 0.5, b: 1, a: 0.8 } },
  modeId: 'modeId',
});
```

描边变量（STROKE_WIDTH）和圆角变量（CORNER_RADIUS） 传 number[]（4 个值）：

```
mg.variables.setVariableValue({ id: 'varId', modeId: 'modeId', value: [1, 2, 1, 2] });
```

内边距变量（PADDING） 传 number[]（4 个值对应上右下左）：

```
mg.variables.setVariableValue({ id: 'varId', modeId: 'modeId', value: [10, 20, 10, 20] });
```

特效变量（EFFECT）值结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| index | string | 特效项索引 |
| type | number | 0=内阴影, 1=投影, 2=图层模糊, 3=背景模糊, 4=液态玻璃, 5=动感模糊 |
| x | number | X 偏移（阴影类） |
| y | number | Y 偏移（阴影类） |
| radius | number | 模糊半径 |
| spread | number | 扩展（阴影类） |
| color |  | 颜色（0-1 范围） |
| blendMode | number | 混合模式 |
| isVisible | boolean | 是否可见 |

```
// 修改投影阴影
mg.variables.setVariableValue({
  id: 'effectVarId',
  modeId: 'modeId',
  value: { index: '685:0', x: 10, y: 10, radius: 5, spread: 2 },
});

// 不指定 index 时自动匹配同 type 的特效项
mg.variables.setVariableValue({
  id: 'effectVarId',
  modeId: 'modeId',
  value: { type: 1, color: { r: 1, g: 0, b: 0, a: 1 } },
});

// 修改图层模糊
mg.variables.setVariableValue({
  id: 'effectVarId',
  modeId: 'modeId',
  value: { type: 2, radius: 20 },
});

// 修改背景模糊
mg.variables.setVariableValue({
  id: 'effectVarId',
  modeId: 'modeId',
  value: { type: 3, saturate: 50, radius: 10 },
});
```

文本变量（TEXT）值结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| decoration | `TextDecoration` | 文字装饰，支持 `NONE`、`UNDERLINE`、`STRIKETHROUGH` |
| textCase | `TextCase` | 字母大小写，支持 `ORIGINAL`、`UPPER`、`LOWER`、`TITLE` |
| features | `TextVariableFeatures` | OpenType 字体特性，支持 `liga`（连笔）、`kern`（字偶距）、`fwid`（全宽）、`hwid`（半宽），值为 `0` 或 `1` |
| fontSize | number | 字号 |
| height | number \| string | 行高，支持像素值或百分比 |
| letterSpacing | number \| string | 字间距，支持像素值或百分比 |
| fontWeight | number \| string | 字重 |
| fontFamily | string | 字体族 |

features 使用 OpenType 特性标签作为字段名，除上述字段外也支持其他特性标签：

```
interface TextVariableFeatures {
  liga?: number // 连笔
  kern?: number // 字偶距
  fwid?: number // 全宽
  hwid?: number // 半宽
  [feature: string]: number | undefined
}
```

以上字段均支持部分更新。setVariableValue 返回更新后的变量，调用方可以使用 await 等待数据刷新完成。例如，设置文字样式时只传入需要修改的字段即可：

```
await mg.variables.setVariableValue({
  id: 'textVarId',
  modeId: 'modeId',
  value: {
    decoration: 'STRIKETHROUGH',
    textCase: 'UPPER',
    features: {
      liga: 1,
      kern: 1,
      fwid: 1,
      hwid: 1,
    },
    fontSize: 14,
    height: 200,           // 行高，整数或百分比 '10%'
    letterSpacing: '10%',   // 字间距，整数或百分比
    fontWeight: 400,
    fontFamily: 'Anek Latin',
  },
});
```

网格变量（GRID）值结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| index | string | 网格项索引 |
| gridType | number | 0=网格, 1=栅格行, 2=栅格列 |
| color |  | 颜色（0-1 范围） |
| sectionSize | number | 行高/列宽 |
| count | number | 行/列数量 |
| gutterSize | number | 间距 |
| offset | number | 偏移 |
| alignment | number | 对齐方式 |
| isVisible | boolean | 是否可见 |

```
// 修改网格颜色
mg.variables.setVariableValue({
  id: 'gridVarId',
  value: { gridType: 0, color: { r: 1, g: 0, b: 0, a: 0.5 } },
  modeId: 'modeId',
});

// 修改网格尺寸参数
mg.variables.setVariableValue({
  id: 'gridVarId',
  value: { gridType: 1, sectionSize: 8, count: 12, gutterSize: 20, offset: 0 },
  modeId: 'modeId',
});
```

## 变量绑定与解绑

### `setVariableReference`

- Type: `(options: SetVariableReferenceOptions) => void`
将变量绑定到另一个变量引用（跨类型绑定）。支持复合样式变量的子属性绑定。

```
// 基本绑定：变量 A 引用变量 B
mg.variables.setVariableReference({
  id: 'boolVarId',       // 被引用的变量 ID
  reference: 'otherVarId', // 要绑定的变量 ID
  modeId: 'modeId',
});
```

填充绑定颜色变量：

```
mg.variables.setVariableReference({
  id: 'paintVarId',           // PAINT 样式 ID
  reference: 'colorVarId',    // COLOR 单值变量 ID
  modeId: 'modeId',
  index: '741:0',             // 填充项 index
});
```

文字属性绑定：
通过 textProperty 指定绑定到 TEXT 变量的具体属性：

| textProperty | 支持绑定的变量类型 |
|---|---|
| fontFamily | STRING |
| fontWeight | STRING / NUMBER |
| fontSize | NUMBER |
| lineHeight | NUMBER |
| letterSpacing | NUMBER |
| paragraphSpacing | NUMBER |

```
// TEXT 变量字体族绑定到 STRING 变量
mg.variables.setVariableReference({
  id: 'textVarId',
  reference: 'stringVarId',
  modeId: 'modeId',
  textProperty: 'fontFamily',
});

// TEXT 变量字号绑定到 NUMBER 变量
mg.variables.setVariableReference({
  id: 'textVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  textProperty: 'fontSize',
});
```

描边属性绑定：
通过 strokeProperty 指定绑定的边：

| strokeProperty | 支持变量类型 | 说明 |
|---|---|---|
| all | NUMBER | 四边统一绑定 |
| top | NUMBER | 顶部描边 |
| right | NUMBER | 右侧描边 |
| bottom | NUMBER | 底部描边 |
| left | NUMBER | 左侧描边 |

```
mg.variables.setVariableReference({
  id: 'strokeVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  strokeProperty: 'all',
});
```

圆角属性绑定：
通过 radiusProperty 指定绑定的角：

| radiusProperty | 支持变量类型 |
|---|---|
| all | NUMBER |
| topLeft | NUMBER |
| topRight | NUMBER |
| bottomRight | NUMBER |
| bottomLeft | NUMBER |

```
mg.variables.setVariableReference({
  id: 'radiusVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  radiusProperty: 'topLeft',
});
```

内边距属性绑定：
通过 paddingProperty 指定绑定的边：

| paddingProperty | 支持变量类型 | 说明 |
|---|---|---|
| all | NUMBER | 四边统一 |
| topBottom | NUMBER | 上下两边 |
| leftRight | NUMBER | 左右两边 |
| top | NUMBER | 顶部 |
| right | NUMBER | 右侧 |
| bottom | NUMBER | 底部 |
| left | NUMBER | 左侧 |

```
mg.variables.setVariableReference({
  id: 'paddingVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  paddingProperty: 'all',
});
```

特效属性绑定：
通过 effectProperty 配合 index 指定要绑定的特效项属性：

| effectProperty | 支持变量类型 | 说明 |
|---|---|---|
| x | NUMBER | 水平偏移（仅阴影） |
| y | NUMBER | 垂直偏移（仅阴影） |
| blur | NUMBER | 模糊半径 |
| spread | NUMBER | 扩展（仅阴影） |
| color | COLOR | 颜色 |

```
mg.variables.setVariableReference({
  id: 'effectVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  index: '685:0',
  effectProperty: 'x',
});

mg.variables.setVariableReference({
  id: 'effectVarId',
  reference: 'colorVarId',
  modeId: 'modeId',
  index: '685:0',
  effectProperty: 'color',
});
```

网格属性绑定：
通过 gridProperty 配合 index 指定要绑定的网格项属性：

| gridProperty | 变量类型 | 网格(GRID) | 栅格行/列 |
|---|---|---|---|
| color | COLOR | 支持 | 支持 |
| sectionSize | NUMBER | 支持 | 支持 |
| count | NUMBER | - | 支持 |
| gutterSize | NUMBER | - | 支持 |
| offset | NUMBER | - | 支持 |

```
mg.variables.setVariableReference({
  id: 'gridVarId',
  reference: 'numberVarId',
  modeId: 'modeId',
  index: '608:0',
  gridProperty: 'sectionSize',
});
```

SetVariableReferenceOptions 类型：

```
interface SetVariableReferenceOptions {
  id: string
  reference: string | object
  modeId?: string
  index?: string
  textProperty?: string
  strokeProperty?: string
  radiusProperty?: string
  paddingProperty?: string
  gridProperty?: string
  effectProperty?: string
}
```

### `unlinkVariable`

- Type: `(options: { id: string; modeId?: string }) => Promise`
解绑变量引用。

```
await mg.variables.unlinkVariable({ id: 'varId', modeId: 'modeId' });
```

## 变量作用域

### `getVariableScopes`

- Type: `(variableId: string) => string[]`
获取变量的作用域列表。

```
const scopes = mg.variables.getVariableScopes('variableId');
```

### `setVariableScopes`

- Type: `(variableId: string, scopes: string[]) => Promise`
设置变量的作用域。不同变量类型支持的作用域不同：
颜色变量（COLOR）：

| Scope | 含义 |
|---|---|
| `'all'` | 所有可用属性 |
| `'fillAll'` | 所有填充（fill + shapeFill + textFill） |
| `'fill'` | 容器图层填充 |
| `'shapeFill'` | 形状图层填充 |
| `'textFill'` | 文字图层填充 |
| `'stroke'` | 描边 |
| `'effect'` | 特效 |
| `'grid'` | 网格 |

数值变量（NUMBER）：

| Scope | 含义 |
|---|---|
| `'all'` | 所有可用属性 |
| `'widthHeight'` | 宽度、高度 |
| `'cornerRadius'` | 圆角 |
| `'layoutSpacing'` | 间距（自动布局） |
| `'layoutPadding'` | 边距（自动布局） |
| `'stroke'` | 描边 |
| `'opacity'` | 图层透明度 |
| `'effect'` | 特效 |
| `'grid'` | 网格 |
| `'fontWeight'` | 文字字重 |
| `'fontSize'` | 文字字号 |
| `'textLineHeight'` | 文字行高 |
| `'textLetterSpacing'` | 文字字间距 |
| `'textParagraphSpacing'` | 文字段落间距 |

字符串变量（STRING）：

| Scope | 含义 |
|---|---|
| `'all'` | 所有可用属性 |
| `'fontWeight'` | 文字字重 |
| `'fontFamily'` | 文字字体 |
| `'textContent'` | 文字内容 |

填充变量（PAINT）：

| Scope | 含义 |
|---|---|
| `'all'` | 所有可用属性 |
| `'fillAll'` | 所有填充 |
| `'fill'` | 容器图层填充 |
| `'shapeFill'` | 形状图层填充 |
| `'textFill'` | 文字图层填充 |
| `'stroke'` | 描边颜色 |

```
// 设置所有作用域
await mg.variables.setVariableScopes('variableId', ['all']);

// 设置所有填充色（仅 COLOR 和 PAINT 有效）
await mg.variables.setVariableScopes('variableId', ['fillAll']);
```

## 变量描述与别名

### `getVariableDescription`

- Type: `(variableId: string) => string`
获取变量描述。

```
const desc = mg.variables.getVariableDescription('variableId');
```

### `setVariableDescription`

- Type: `(variableId: string, description: string) => Promise`
设置变量描述。

```
await mg.variables.setVariableDescription('variableId', '这是主色调变量');
```

### `resetVariableDescription`

- Type: `(variableId: string) => Promise`
重置（清空）变量描述。

```
await mg.variables.resetVariableDescription('variableId');
```

### `getVariableAlias`

- Type: `(variableId: string) => string`
获取变量别名。

```
const alias = mg.variables.getVariableAlias('variableId');
```

### `setVariableAlias`

- Type: `(variableId: string, alias: string) => Promise`
设置变量别名。

```
await mg.variables.setVariableAlias('variableId', 'primary-color');
```

### `resetVariableAlias`

- Type: `(variableId: string) => Promise`
重置（清空）变量别名。

```
await mg.variables.resetVariableAlias('variableId');
```

## 变量代码语法

### `getCodeSyntax`

- Type: `(variableId: string) => { web?: string; android?: string; ios?: string } | null`
获取变量的代码语法。

```
const codeSyntax = mg.variables.getCodeSyntax('variableId');
// → { web: '--primary', android: 'primaryColor', ios: 'primaryColor' }
```

### `setCodeSyntax`

- Type: `(variableId: string, codeSyntax: { web?: string; android?: string; ios?: string }) => Promise`
设置变量的代码语法。只允许字母、数字、连字符和下划线。

```
await mg.variables.setCodeSyntax('variableId', {
  web: '--primary-color',
  android: 'primaryColor',
  ios: 'primaryColor',
});
```

### `resetCodeSyntax`

- Type: `(variableId: string, platform?: string) => Promise`
重置变量代码语法。可选 platform 参数单独重置某个平台（'web' | 'android' | 'ios'）。

```
// 重置所有平台的代码语法
await mg.variables.resetCodeSyntax('variableId');

// 只重置 web 平台的
await mg.variables.resetCodeSyntax('variableId', 'web');
```

## 组件属性变量

### `setVariableInComponent`

- Type: `(options: { id: string; propertyId: string; type: 'BOOLEAN' | 'CONTENT' }) => void`
将一个已有的变量绑定到组件属性上。

```
// 绑定布尔变量到组件布尔属性
mg.variables.setVariableInComponent({
  id: 'variableId',
  propertyId: 'propId',
  type: 'BOOLEAN',
});

// 绑定字符串变量到组件文本内容属性
mg.variables.setVariableInComponent({
  id: 'variableId',
  propertyId: 'propId',
  type: 'CONTENT',
});
```

### `unlinkVariableInComponent`

- Type: `(options: { propertyId: string; type: 'BOOLEAN' | 'CONTENT' }) => void`
从组件属性上解绑变量。

```
mg.variables.unlinkVariableInComponent({ propertyId: 'propId', type: 'BOOLEAN' });
mg.variables.unlinkVariableInComponent({ propertyId: 'propId', type: 'CONTENT' });
```

### `createVariableInComponent`

- Type: `(options: CreateVariableInComponentOptions) => Promise`
创建新变量并自动绑定到新创建的组件属性上（一步完成：创建变量 + 创建组件属性 + 绑定）。返回新创建的组件属性 ID。

```
// 创建布尔变量 + 布尔组件属性
const boolPropId = await mg.variables.createVariableInComponent({
  name: 'isVisible',
  layerId: 'componentLayerId',
  type: 'BOOLEAN',
  value: true,
  collectionId: 'collectionId',
});

// 创建字符串变量 + 文本内容组件属性
const textPropId = await mg.variables.createVariableInComponent({
  name: 'buttonText',
  layerId: 'componentLayerId',
  type: 'CONTENT',
  value: 'Click Me',
  collectionId: 'collectionId',
});
```

CreateVariableInComponentOptions 类型：

```
interface CreateVariableInComponentOptions {
  name: string
  layerId: string
  type: 'BOOLEAN' | 'CONTENT'
  value?: any
  collectionId?: string
  description?: string
}
```

## 图层属性变量

### `createVariableInLayer`

- Type: `(options: CreateVariableInLayerOptions) => Promise`
在图层上创建变量并自动绑定到指定属性。一步完成（创建变量 + 绑定到图层）。

```
// 基础属性 — 透明度
await mg.variables.createVariableInLayer({
  name: '图层透明度',
  layerId: '2:1',
  baseProperty: 'opacity',
  collectionId: 'collectionId',
});

// 基础属性 — 填充颜色
await mg.variables.createVariableInLayer({
  name: '填充颜色',
  layerId: '2:1',
  baseProperty: 'fillColor',
  index: 0,
  collectionId: 'collectionId',
});

// 描边宽度
await mg.variables.createVariableInLayer({
  name: '描边宽度',
  layerId: '2:1',
  strokeProperty: 'all',
  collectionId: 'collectionId',
});

// 圆角
await mg.variables.createVariableInLayer({
  name: '圆角',
  layerId: '2:1',
  radiusProperty: 'all',
  collectionId: 'collectionId',
});

// 图层尺寸
await mg.variables.createVariableInLayer({
  name: '宽度',
  layerId: '2:1',
  dimensionProperty: 'width',
  collectionId: 'collectionId',
});

// 特效
await mg.variables.createVariableInLayer({
  name: '模糊半径',
  layerId: '2:1',
  effectProperty: 'blur',
  index: 0,
  collectionId: 'collectionId',
});
```

属性参数一览：

| 参数 | 可选值 | 变量类型 |
|---|---|---|
| baseProperty | `'opacity'` / `'fillColor'` / `'visible'` | NUMBER / COLOR / BOOLEAN |
| strokeProperty | `'top'` / `'right'` / `'bottom'` / `'left'` / `'all'` / `'color'` | NUMBER / COLOR |
| radiusProperty | `'topLeft'` / `'topRight'` / `'bottomRight'` / `'bottomLeft'` / `'all'` | NUMBER |
| paddingProperty | `'top'` / `'right'` / `'bottom'` / `'left'` / `'topBottom'` / `'leftRight'` / `'all'` | NUMBER |
| dimensionProperty | `'width'` / `'height'` / `'maxWidth'` / `'maxHeight'` / `'minWidth'` / `'minHeight'` | NUMBER |
| effectProperty | `'x'` / `'y'` / `'blur'` / `'spread'` / `'color'` | NUMBER / COLOR |
| gridProperty | `'sectionSize'` / `'count'` / `'gutterSize'` / `'offset'` / `'color'` | NUMBER / COLOR |
| textProperty | `'fontFamily'` / `'fontWeight'` / `'fontSize'` / `'lineHeight'` / `'letterSpacing'` / `'paragraphSpacing'` | STRING / NUMBER |

### `setVariableReferenceInLayer`

- Type: `(options: SetVariableInLayerOptions) => Promise`
将变量绑定到图层属性。
id 参数支持两种取值：

- **本地变量 id**：如 `getVariables()` 返回的 `Variable.id`
- **团队库变量 ukey**：`getTeamLibraryAsync()` 返回的 `style.colors/numbers/strings/bools` 等条目的 `ukey`。传入 ukey 时会自动将该团队库变量导入当前文件后再绑定，无需先手动导入
index 为目标数组属性的数据下标（如 node.fills 的下标）。注意 fills[0] 是最底层填充，与右侧面板的显示顺序相反（面板最上面一行对应数组最后一项）。

```
// 描边宽度绑定
await mg.variables.setVariableReferenceInLayer({
  id: 'numberVarId',
  layerId: 'layerId',
  strokeProperty: 'all',
});

// 描边颜色绑定（需指定 index）
await mg.variables.setVariableReferenceInLayer({
  id: 'colorVarId',
  layerId: 'layerId',
  strokeProperty: 'color',
  index: 0,
});

// 圆角绑定
await mg.variables.setVariableReferenceInLayer({
  id: 'numberVarId',
  layerId: 'layerId',
  radiusProperty: 'all',
});

// 内边距绑定
await mg.variables.setVariableReferenceInLayer({
  id: 'numberVarId',
  layerId: 'layerId',
  paddingProperty: 'all',
});

// 图层尺寸绑定
await mg.variables.setVariableReferenceInLayer({
  id: 'numberVarId',
  layerId: 'layerId',
  dimensionProperty: 'width',
});

// 图层透明度绑定（需要数值变量，值范围 0~1）
await mg.variables.setVariableReferenceInLayer({
  id: 'numberVarId',
  layerId: 'layerId',
  baseProperty: 'opacity',
});

// 绑定团队库变量（自动导入，无需先手动导入）
const libraries = await mg.getTeamLibraryAsync();
const colorVar = libraries[0]?.style.colors[0];
if (colorVar) {
  await mg.variables.setVariableReferenceInLayer({
    id: colorVar.ukey, // 团队库变量使用 ukey
    layerId: 'layerId',
    baseProperty: 'fillColor',
  });
}
```

> > **绑定团队库变量的注意事项**
>
- 需要当前文件已订阅对应团队库，未订阅或 ukey 无效时静默返回
- 变量二进制数据下载失败或变量 scope 不支持目标属性时，Promise 会 reject
- 若团队库已发布新版本，绑定时会自动升级本地副本，文件内其他使用该变量的图层会一并更新

### `unlinkVariableReferenceInLayer`

- Type: `(options: UnlinkVariableInLayerOptions) => Promise`
解除图层属性的变量绑定。

```
// 解绑描边宽度
await mg.variables.unlinkVariableReferenceInLayer({
  layerId: 'layerId',
  strokeProperty: 'all',
});

// 解绑描边颜色
await mg.variables.unlinkVariableReferenceInLayer({
  layerId: 'layerId',
  strokeProperty: 'color',
  index: 0,
});

// 解绑圆角
await mg.variables.unlinkVariableReferenceInLayer({
  layerId: 'layerId',
  radiusProperty: 'all',
});
```

## 字体

### `getFontFamilies`

- Type: `() => FontFamilyInfo[]`
获取所有可用字体系列。

```
const families = mg.variables.getFontFamilies();
// → [{ family: 'Anek Latin', label: 'Anek Latin', lang: 'en', isVariable: true }, ...]
```

### `getFontWeights`

- Type: `(family: string) => FontWeightInfo[]`
根据字体系列获取对应的字体样式。

```
const weights = mg.variables.getFontWeights('Anek Latin');
// → [{ postscriptName: '...', label: 'Regular', style: 'Regular', weight: 400, slant: 0 }, ...]
```

mastergo
mastergo.ui