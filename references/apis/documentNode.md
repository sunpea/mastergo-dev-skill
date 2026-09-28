# DocumentNode
DocumentNode 是整个 MasterGo 文件的根节点，它对应整个 MasterGo 文件，不存在真实的图层与之对应。所有页面节点和图层节点都需要通过 DocumentNode 根节点来访问。该节点的所有直接子节点一定是页面节点（即 PageNode）。可以通过 mg.document 来访问根节点：

```
const root = mg.document // DocumentNode
const pages = root.children // PageNode[]
```

## Base node properties

### `id`

- Readonly: `true`
- Type: `number`
当前文档的 ID。

### `type`

- Readonly: `true`
- Type: `'DOCUMENT'`
代表该节点的类型。

### `name`

- Readonly: `true`
- Type: `string`
当前文件的名称。

### `currentPage`

- Type: `PageNode`
获取当前页面节点。

## Children-related properties

### `children`

- Readonly: `true`
- Type: `ReadonlyArray`
当前节点的子节点。对于 DocumentNode 来说，它的所有子节点都是页面节点，即 PageNode。

### `findAll`

- Type: `findAll(callback?: (node: SceneNode) => boolean): ReadonlyArray`
查找整个节点树，对每个节点调用 callback 函数，并返回所有对于 callback 函数的返回值为 true 的节点。例如，查找所有矩形节点：

```
const rectNodes = mg.document.findAll((node) => node.type === 'RECTANGLE')
```

需要注意的是，对于 DocumentNode 来说，其 findAll 方法将不会查找页面节点。因为你总是可以用更快速的办法访问或查找特定的页面节点，例如：

```
mg.document.children // 所有页面节点
mg.document.children.filter(cb) // 过滤出特定的页面节点
```

### `findOne`

- Type: `findOne(callback: (node: SceneNode) => boolean): SceneNode | null`
查找整个节点树，对每个节点调用 callback 函数，并返回第一个对于 callback 函数的返回值为 true 的节点。例如，查找第一个遇到的矩形节点：

```
const rectNode = mg.document.findOne((node) => node.type === 'RECTANGLE')
```

> > **WARNING**
> 需要注意，与 findAll 方法一样，findOne 方法也不会对页面节点进行查找。

### `findAllWithCriteria`

- Type: `findAllWithCriteria(criteria: { types: T }): Array`
查找整个节点树，返回所有类型符合的节点。

```
const nodes = mg.document.findAllWithCriteria({types: ['FRAME', 'COMPONENT']})
```

ConnectorNode
EllipseNode