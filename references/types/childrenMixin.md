# ChildrenMixin

```
interface ChildrenMixin<ChildrenNode = SceneNode> {
    readonly children: ReadonlyArray<ChildrenNode>
    appendChild(child: SceneNode): void
    insertChild(index: number, child: SceneNode): void

    findChildren(
      callback?: (node: SceneNode) => boolean
    ): ReadonlyArray<SceneNode>
    findChild(callback: (node: SceneNode) => boolean): SceneNode | null

    findAll(callback?: (node: SceneNode) => boolean): ReadonlyArray<SceneNode>
    findOne(callback: (node: SceneNode) => boolean): SceneNode | null
    findAllWithCriteria<T extends NodeType[]>(criteria: { types: T }): Array<{ type: T[number] } & SceneNode>
    
  }
```

- `appendChild` ： 将给定的节点添加为当前节点的直接子节点。
- `insertChild` ： 在指定的位置 `index` 处插入子节点 `child`。假设一个容器图层有三个子节点 A、B、C，现在调用 `insertChild` 方法将插入图层节点 D： `frame.insertChild(0, D)`，子节点顺序为：**`D`**、A、B、C。
- `frame.insertChild(1, D)`，子节点顺序为：A、**`D`**、B、C。
- `frame.insertChild(2, D)`，子节点顺序为：A、B、**`D`**、C。
- `frame.insertChild(3, D)`，子节点顺序为：A、B、C、**`D`**。

- `findAll` ： 从当前节点开始查找整个子树，对每个节点调用 `callback` 函数，并返回所有对于 `callback` 函数的返回值为 `true` 的节点。
- `findOne` ： 从当前节点开始查找整个节点树，对每个节点调用 `callback` 函数，并返回第一个对于 `callback` 函数的返回值为 `true` 的节点。
- `findChildren` ： 与 `findAll` 类似，不同之处在于，`findChildren` 仅会在当前节点的**直接**子节点（不包括子节点的子节点）中进行查找。
- `findChild` ： 与 `findOne` 类似，不同之处在于，`findChild` 仅会在当前节点的**直接**子节点（不包括子节点的子节点）中进行查找。
- `findAllWithCriteria` ： 查找当前节点的所有子节点，返回所有类型符合的节点。

```
const nodes = node.findAllWithCriteria({types: ['FRAME', 'COMPONENT']})
```

BlendMode
ComponentPropertiesRelated