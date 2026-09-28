# PageNode
PageNode 代表页面节点，即 DocumentNode 的直接子节点。可以通过 mg.document.currentPage 获取当前页面节点。

## Base node properties

### `type`

- Readonly: `true`
- Type: `'PAGE'`
节点类型，对于页面节点来说，其值为字符串 'PAGE'。

### `clone`

- Type: `clone(): PageNode`
克隆当前页面，并作为 mg.document 的子节点。页面内的组件节点将被复制为实例节点，该实例节点以原组件节点作为主组件。

### `id`

- Readonly: `true`
- Type: `string`
pageNode节点的 ID。

### `remove`

- Type: `remove():void`
将当前节点从parent节点中移除。

### `removed`

- Type: `boolean`
如果节点被移除了，则值为 true。如果插件保持运行状态，并且插件代码对某个节点存在引用，那么您应该始终检查节点的 removed 属性，在对节点进行操作之前先确保它没有被移除。

### `parent`

- Readonly: `true`
- Type: `(BaseNode & ChildrenMixin) | void`

### `name`

- Type: `string`
读取或设置节点的名字，即图层面板中所展示的图层名称。

### `selection`

- Type: `ReadonlyArray`
获取当前页面选中的节点。例如，可以使用下面的代码来获取当前页面中选中的节点：

```
const selectedNodes = mg.document.currentPage.selection
```

page.selection 返回的节点数组是只读的，你无法通过 push、pop 等方法来操作选中。为了改变选中，你需要完整地设置 selection 属性值，如下面的代码所示：

```
page.selection = page.selection.concat(newNode)
```

> > **INFO**
> 使用 selection 读取或设置选中的节点时需要注意，该属性仅包含直接选中的节点，而不会包含选中节点的子代节点。

### `selectAll`

- Type: `selectAll(): void`
选中当前页面所有节点。

### `flowStartingPoints`

- Readonly: `true`
- Type: [`ReadonlyArray`](/types/flowStartingPoint.html)
获取该页面所有原型的头节点信息。

### `label`

- Type: `'NONE' | 'BLUE' | 'GREEN' | 'RED' | 'YELLOW' | 'PURPLE' | 'GRAY'`
读取/设置当前页面的标签。
获取当前节点的父节点。parent 属性为只读属性，如果你想要更换当前节点的父节点，请参考 appentChild 方法。

### `bgColor`

- Type: [RGBA](/types/rgb.html)
page的背景颜色。

### `getExportList`

- Type: `getExportList(): ReadonlyArray`
获取当前页面的所有导出项。返回结果同时包含页面导出项和页面内图层的导出项；一个图层配置了多个导出设置时，会返回多个导出项。

```
const exportList = mg.document.currentPage.getExportList();

for (const item of exportList) {
  const node = item.isLayer ? mg.getNodeById(item.layerId) : null;
  if (node && item.format !== 'SOURCE') {
    const bytes = await node.exportAsync(item);
  }
}
```

返回项的 format、constraint 字段可以直接转换为节点 exportAsync 所需的导出设置。format 为 SOURCE 的项表示源文件，不应传给 exportAsync。

## Children-related properties

### `children`

- Readonly: `true`
- Type: `ReadonlyArray`
当前页面节点的直接子节点。

### `appendChild`

- Type: `appendChild(child: SceneNode): void`
将给定的节点 child 添加为当前节点的子节点。

### `insertChild`

- Type: `insertChild(index: number, child: SceneNode): void`
在指定的位置 index 处插入子节点 child。假设一个组有三个子节点 A、B、C，现在调用 insertChild 方法将插入图层节点 D：

- `insertChild(0, D)`，子节点顺序为：**`D`**、A、B、C。
- `insertChild(1, D)`，子节点顺序为：A、**`D`**、B、C。
- `insertChild(2, D)`，子节点顺序为：A、B、**`D`**、C。
- `insertChild(3, D)`，子节点顺序为：A、B、C、**`D`**。

### `findAll`

- Type: `findAll(callback?: (node: SceneNode) => boolean): ReadonlyArray`
从当前页面节点开始查找整个节点树，对每个节点调用 callback 函数，并返回所有对于 callback 函数的返回值为 true 的节点。例如，查找所有矩形节点：

```
const rectNodes = mg.document.currentPage.findAll((node) => node.type === 'RECTANGLE')
```

### `findOne`

- Type: `findOne(callback: (node: SceneNode) => boolean): SceneNode | null`
从当前页面节点开始查找整个节点树，对每个节点调用 callback 函数，并返回第一个对于 callback 函数的返回值为 true 的节点。例如，查找第一个遇到的矩形节点：

```
const rectNode = mg.document.findOne((node) => node.type === 'RECTANGLE')
```

### `findChildren`

- Type: `findChildren(callback?: (node: SceneNode) => boolean): ReadonlyArray`
与 findAll 类似，不同之处在于，findChildren 仅会在当前节点的直接子节点（不包括子节点的子节点）中进行查找。

### `findChild`

- Type: `findChild(callback: (node: SceneNode) => boolean): SceneNode | null`
与 findOne 类似，不同之处在于，findChild 仅会在当前节点的直接子节点（不包括子节点的子节点）中进行查找。

### `findAllWithCriteria`

- Type: `findAllWithCriteria(criteria: { types: T }): Array`
从当前页面节点开始查找整个节点树，返回所有类型符合的节点。

```
const nodes = mg.document.currentPage.findAllWithCriteria({types: ['FRAME', 'COMPONENT']})
```

LineNode
PenNode