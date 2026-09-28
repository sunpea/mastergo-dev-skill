# ComponentPropertiesRelated
组件(组件集)上存在的所有组件属性相关的字段和方法的集合。

## ComponentPropertiesMixin

```
interface ComponentPropertiesMixin {
    readonly componentPropertyValues: ComponentPropertyValues
    addComponentProperty(
      propertyName: string,
      type: Exclude<ComponentPropertyType, 'VARIANT'>,
      defaultValue: string | boolean,
      options?: ComponentPropertyOptions,
    ): string
    editComponentProperty(
      propertyId: string,
      newValue: {
        name?: string
        defaultValue?: string | boolean
        preferredValues?: InstanceSwapPreferredValue[]
      },
    ): string
    deleteComponentProperty(propertyId: string): void
  }

  type ComponentPropertyValues = Array<ComponentPropertyValue>
```

- `componentPropertyValues`: 组件(组件集)的组件属性集合。
- `addComponentProperty`: 添加一个组件属性。`propertyName`: 属性名称。
- `type`: 属性类型，支持`BOOLEAN`, `TEXT`, `INSTANCE_SWAP`。
- `defaultValue`: 默认值。
- `options`: 创建新组件属性时可以指定的其他选项。 `preferredValues`: 仅`type`为`INSTANCE_SWAP`时生效。设置实例切换的首选项，切换实例时可以优先设置。

- `editComponentProperty`: 修改组件属性名称和值，支持`BOOLEAN`, `TEXT`, `INSTANCE_SWAP`。`propertyId`: 组件属性id。
- `newValue`: 替换的值。 `name`: 属性名称。
- `defaultValue`: 属性默认值。
- `preferredValues`: 仅`type`为`INSTANCE_SWAP`时生效。设置实例切换的首选项，切换实例时可以优先设置。

- `deleteComponentProperty`: 删除组件属性，支持`BOOLEAN`, `TEXT`, `INSTANCE_SWAP`。`propertyId`: 组件属性id。

## ComponentPropertyValue

```
type ComponentPropertyValue = {
    name: string
    type: ComponentPropertyType
    defaultValue: string | boolean
    id?: string
    variantOptions?: string[]
    preferredValues?: InstanceSwapPreferredValue[]
    alias?: string
    variantOptionsAlias?: string[]
    variableId?: string
  }
```

单个组件属性。

- `name`: 属性名称。
- `type`: 属性类型。
- `defaultValue`: 属性默认值。
- `id`: 属性id, 当`type`为`VARIANT`时为空。
- `variantOptions`: 组件状态的变量数组。仅当`type`为`VARIANT`有值。
- `preferredValues`: 实例切换首选项数组。仅当`type`为`INSTANCE_SWAP`有值。
- `alias`: 属性别名。
- `variantOptionsAlias`: 变体属性的可选值别名数组，仅当`type`为`VARIANT`时返回。已剥离内部默认值标记（如`$default`），元素可能为空字符串。
- `variableId`: 当组件属性绑定到变量时，对应的变量 id（仅 TEXT/BOOLEAN 类型可能存在）。

## ComponentPropertyType

```
type ComponentPropertyType = 'BOOLEAN' | 'TEXT' | 'INSTANCE_SWAP' | 'VARIANT'
```

组件属性类型。

- `BOOLEAN`: 布尔值，可以用来控制图层的显示状态。
- `TEXT`: 文字，可以用来控制文字图层的文字内容。
- `INSTANCE_SWAP`: 实例继承组件，可以用来切换实例的主组件。
- `VARIANT`: 变量，可以用来切换组件状态。

## ComponentProperties

```
type ComponentProperties = {
    name: string
    id?: string
    type: ComponentPropertyType
    value: boolean | string
    preferredValues?: InstanceSwapPreferredValue[]
    alias?: string
    valueAlias?: string
    isDefaultValue?: boolean
  }
```

实例上绑定的组件属性。

- `name`: 属性名。
- `id`: 属性id, 当`type`为`VARIANT`时不存在。
- `type`: 属性类型。
- `value`: 属性值。
- `preferredValues`: 实例切换首选项数组。仅当`type`为`INSTANCE_SWAP`有值。
- `alias`: 属性名别名。
- `valueAlias`: 当前变体属性取值的别名，仅当`type`为`VARIANT`时返回。已剥离内部默认值标记（如`$default`），可能为空字符串。
- `isDefaultValue`: 当前变体取值是否为该属性的默认值，仅当`type`为`VARIANT`时返回。

## ComponentPropertyReferences

```
interface SceneNodeMixin {
    componentPropertyReferences: {
      isVisible?: string,
      characters?: string,
      mainComponent?: string
    } | null   
  }
```

子图层绑定的组件属性，仅当节点是组件子图层且未嵌套在实例节点中时，该节点才能具有组件属性引用。

- `isVisible`: 控制显隐。
- `characters`: 文字内容, 仅图层为字体图层时有效。
- `mainComponent`: 实例继承的主组件，仅图层为实例时有效。

```
// 创建组件
const component = mg.createComponent([mg.createRectangle()])

// 新增组件属性
// 图层显隐
const showId = component.addComponentProperty("show", "BOOLEAN", true)
// 返回 "7242:345"

// 文字内容
const textId = component.addComponentProperty("gender", "TEXT", 'male')
// 返回 "7242:346"

// 实例主组件
// 创建两个用于实例切换的组件
const componentSet = mg.combineAsVariants([mg.createComponent([mg.createRectangle()])])
const component1 = mg.createComponent([mg.createRectangle()])
component.addComponentProperty("mainComponent", "INSTANCE_SWAP", '4708:184', { preferredValues: [{ type: 'COMPONENT', key: component1.ukey }, { type: 'COMPONENT_SET', key: componentSet.ukey }] })
// 返回 "7242:674"

console.log(component.componentPropertyValues)
// 输出
[
  {
      "name": "show",
      "type": "BOOLEAN",
      "id": "7242:345",
      "defaultValue": true
  },
  {
      "name": "gender",
      "type": "TEXT",
      "id": "7242:346",
      "defaultValue": "male"
  },
  {
      "name": "mainComponent",
      "type": "INSTANCE_SWAP",
      "id": "7242:674",
      "defaultValue": "4708:184"
      "preferredValues": [
        { type: 'COMPONENT', key: 'XXXXXX' },
        { type: 'COMPONENT_SET', key: 'XXXXXXX' }
      ]
  }
]

// 组件修改属性名或默认值不会生成新的propertyId, 组件集会
const propertyId = component.editComponentProperty(showId, { name: 'hide', defaultValue: false  })
console.log(component.componentPropertyValues)
// 输出
[
  {
      "name": "hide",
      "type": "BOOLEAN",
      "id": "7242:345",
      "defaultValue": false
  },
  {
      "name": "gender",
      "type": "TEXT",
      "id": "7242:346",
      "defaultValue": "male"
  },
  {
      "name": "mainComponent",
      "type": "INSTANCE_SWAP",
      "id": "7242:674",
      "defaultValue": "4708:184",
      "preferredValues": [
        { type: 'COMPONENT', key: 'XXXXXX' },
        { type: 'COMPONENT_SET', key: 'XXXXXXX' }
      ]
  }
]

// 删除组件属性
component.deleteComponentProperty(textId)
console.log(component.componentPropertyValues)
// 输出
[
  {
      "name": "hide",
      "type": "BOOLEAN",
      "id": "7242:345",
      "defaultValue": false
  },
  {
      "name": "mainComponent",
      "type": "INSTANCE_SWAP",
      "id": "7242:674",
      "defaultValue": "4708:184",
      "preferredValues": [
        { type: 'COMPONENT', key: 'XXXXXX' },
        { type: 'COMPONENT_SET', key: 'XXXXXXX' }
      ]
  }
]

// 增加组件状态
component.setVariantPropertyValues({
  'status': 'awake',
})
// 获取组件集
const componentSet = component.parent
// 此时组件的组件属性移动到父级的组件集上
console.log(componentSet.componentPropertyValues);
// 输出
[
  {
    "name": "status",
    "type": "VARIANT",
    "defaultValue": "默认",
    "variantOptions": [
        "默认",
        "awake"
    ]
  },
  {
      "name": "hide",
      "type": "BOOLEAN",
      "id": "7242:345",
      "defaultValue": false
  },
  {
      "name": "mainComponent",
      "type": "INSTANCE_SWAP",
      "id": "7242:674",
      "defaultValue": "4708:184",
      "preferredValues": [
        { type: 'COMPONENT', key: 'XXXXXX' },
        { type: 'COMPONENT_SET', key: 'XXXXXXX' }
      ]
  }
]

// 获取组件的子图层
const rectangle = component.children[0]
console.log(rectangle.componentPropertyReferences) // 此时子图层没有绑定任何组件属性，所以是空对象
// 输出
// {}

// 子图层使用组件属性
rectangle.componentPropertyReferences = { isVisible: "7242:345" }
console.log(rectangle.componentPropertyReferences) // 此时子图层没有绑定任何组件属性，所以是空对象
// 输出
{
  "isVisible": "7242:345"
}


// 生成实例
const instance = component.createInstance() // 当前图层没有绑定任何组件属性，所以实例上只会有变体属性
console.log(instance.componentProperties)
// 输出
[
  {
      "name": "status",
      "type": "VARIANT",
      "value": "awake"
  },
  {
      "name": "hide",
      "id": "7249:332",
      "type": "BOOLEAN",
      "value": true
  }
]

// 实例修改属性值
instance.setProperties({"7249:332": false})
console.log(instance.componentProperties)
// 输出
[
  {
      "name": "status",
      "type": "VARIANT",
      "value": "awake"
  },
  {
      "name": "hide",
      "id": "7249:332",
      "type": "BOOLEAN",
      "value": false
  }
]
```

## ComponentItemVal

```
type ComponentItemVal = {
    id: string
    name: string
    componentSignature: string
    cover: string
    description: string
    documentationLinks: Array<{ url: string }>
    height: number
    width: number
    isExternal: boolean
    isHidden: boolean
    pageId: string
    pageName: string
    ukey: string
    version: number
    componentNameAlias: string
    parentId?: string
  }
```

getComponentListVal() 返回的数组中每个元素的数据结构。

- `id`: 组件 ID。
- `name`: 组件名称。
- `componentSignature`: 组件版本签名。
- `cover`: 组件封面图。
- `description`: 组件描述信息。
- `documentationLinks`: 组件的文档链接数组。
- `height`: 组件高度。
- `width`: 组件宽度。
- `isExternal`: 是否是团队库组件。
- `isHidden`: 组件是否隐藏。
- `pageId`: 所在页面 ID。
- `pageName`: 所在页面名称。
- `ukey`: 组件的唯一 key。
- `version`: 组件版本号。
- `componentNameAlias`: 组件名称别名。
- `parentId`: 组件父节点 ID（组件集子组件时有值）。

ChildrenMixin
ConnectorEndpoint