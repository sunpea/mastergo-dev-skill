# v2.6.0
发布时间: 2026/07/22

### 更新如下

- [Effect](/types/effect.html) 新增 `ReferenceEffect` 引用型特效变体： 当样式的某个 mode 引用了另一个特效样式（style 引用 style）时返回此类型，不携带具体特效值，仅保留 `reference` / `referenceSource` / `modeId`。

- [Paint](/types/paint.html) 新增 `ReferencePaint` 引用型填充变体： 当样式的某个 mode 引用了另一个填充/描边样式（style 引用 style）时返回此类型，不携带具体填充值，仅保留 `reference` / `referenceSource` / `modeId`。

- `mg.importStyleByKeyAsync(key)` 修复：首次导入团队库样式时不再返回 `null`，等待本地副本可查后再生成样式对象。

# v2.5.0
发布时间: 2026/07/31

### 更新如下

- [ComponentProperties](/types/componentPropertiesRelated.html)与[Componentpropertyvalue](/types/componentPropertiesRelated.html)中的组件属性别名字段调整 `valueAlias`、`variantOptionsAlias`不再包含内部默认值标记（如`$default`），直接返回清洗后的别名，可能为空字符串。
- `ComponentProperties`补充`alias`、`valueAlias`字段说明。
- `ComponentProperties`新增`isDefaultValue`字段，表示当前变体取值是否为该属性的默认值（仅`VARIANT`类型返回）。

- `研发模式`（DevMode）/ 研发席位下，开放节点 `pluginData` 的写入能力。在只读模式中，插件现可正常调用 `setPluginData`、`setSharedPluginData`、`clearPluginData`、`removePluginData`、`removeSharedPluginData`、`clearSharedPluginData`，用于存储与读取节点上插件私有或共享的自定义数据；画布几何与样式等属性仍保持只读。详见 [研发模式](/devmode/guide/)。
- [TeamLibrary](/types/teamLibrary.html)中的[TeamLibraryComponent](/types/teamLibrary.html#teamlibrarycomponent)新增 `properties` 组件属性 / 变体属性，结构为 [ComponentPropertyValue](/types/componentPropertiesRelated.html#componentpropertyvalue) 数组（老团队库可能缺省）。
- `textNodeNames` 组件所有后代 TEXT 图层的名称数组（去重，老团队库可能缺省）。

- [TeamLibraryStyle](/types/teamLibrary.html#teamlibrarystyle)新增 `values` 各模式下的样式值列表，元素结构为 `{ modeId, modeName, value }`。`value` 形态随样式分类变化（老团队库可能缺省）。
- `codeSyntax` 代码语法（web/android/ios），仅在变量类型上可能存在（老团队库可能缺省）。

- [ComponentPropertyValue](/types/componentPropertiesRelated.html#componentpropertyvalue)新增 `variableId` 当组件属性绑定到变量时对应的变量 id（仅 TEXT/BOOLEAN 类型可能存在）。

# v2.4.0
发布时间: 2024/04/25

### 更新如下

- `AutoLayout`新增 [flexWrap](/apis/componentNode.html#flexwrap) 表示是否折行。
- [crossaxisspacing](/apis/componentNode.html#crossaxisspacing) 换行模式下，交叉轴不同轨道之间的间距。
- [crossAxisAlignContent](/apis/componentNode.html#crossaxisaligncontent) 交叉轴的对齐方式。

# v2.3.0
发布时间: 2023/02/04

### 更新如下

- [TeamLibaray](/types/teamLibrary.html)中的[Teamlibrarycomponent](/types/teamLibrary.html#teamlibrarycomponent)新增 `cover`封面地址。
- `width`宽度(旧团队库宽度可能为0)。
- `height`高度(旧团队库高度可能为0)。

# v2.2.0
发布时间: 2023/11/30

### 更新如下

- [TextSegStyle](/types/textSegStyle.html)新增`fillStyleId`填充样式id字段。

# v2.0.0
发布时间: 2023/09/28

### 更新如下

- 新增[SectionNode](/apis/sectionNode.html)区域节点。
- `saveversionhistoryasync`增加历史版本支持可选的标题参数(/apis/mastergo.html#saveversionhistoryasync)

# v1.21.0
发布时间: 2023/07/06

### 更新如下

- [ComponentNode](/apis/componentNode.html)和[ComponentSetNode](/apis/componentSetNode.html)新增[DocumentationLinks](/apis/componentNode.html#documentationlinks)，获取和设置组件文档链接。

# v1.20.0
发布时间: 2023/04/27

### 更新如下

- 新增[node.isMaskOutline](/apis/rectangleNode.html#ismaskoutline)能力支持
- 新增[node.isMaskVisible](/apis/rectangleNode.html#ismaskvisible)能力支持
- 新增[textNode.textAutoResize = 'TRUNCATE'](/apis/textNode.html#textautoresize)能力支持。

# v1.19.0
发布时间: 2023/04/11

### 更新如下

- 新增[manifest.permissions](/guide/setup.html#manifest-json)能力支持
- 新增[mg.currentUser](/apis/mastergo.html#currentuser)接口，可获取用户信息。

# v1.18.0
发布时间: 2023/04/07

### 更新如下

- 容器图层新增[Expanded](/apis/componentNode.html#expanded)属性来控制左侧树的展开和收起
- 实例新增[Resetoverrides](/apis/instanceNode.html#resetoverrides)来重置自身所有的更改。

# v1.17.0
发布时间: 2023/03/31

### 更新如下:

- [ComponentNode](/apis/componentNode.html)和[ComponentSetNode](/apis/componentSetNode.html)的实例切换属性(instance_swap)新增首选项[PreferredValue](/types/componentPropertiesRelated.html#componentpropertiesmixin)，设置实例切换的首选项。
- [InstanceNode](/apis/instanceNode.html)新增[ExposedInstances](/apis/instanceNode.html#exposedinstances)属性，将自身的组件属性公开给父图层的组件/组件集。
- [InstanceNode](/apis/instanceNode.html)新增[isExposedInstance](/apis/instanceNode.html#isexposedinstance)表示此实例是否向包含自己的 [ComponentNode](/apis/componentNode.html) 或 [ComponentSetNode](/apis/componentSetNode.html) 公开自身的组件属性。仅在 [ComponentNode](/apis/componentNode.html) 或 [ComponentSetNode](/apis/componentSetNode.html) 中包含的主 [InstanceNode](/apis/instanceNode.html) 上可写，只在嵌套的 [InstanceNode](/apis/instanceNode.html) 上继承。
- [GroupNode](/apis/groupNode.html)和[BooleanOperationNode](/apis/booleanOperationNode.html)不再支持设置约束[Constraints](/apis/componentNode.html#constraints)，[GroupNode](/apis/groupNode.html)和[BooleanOperationNode](/apis/booleanOperationNode.html)只受子图层约束影响。

# v1.16.0
发布时间: 2023/03/21

### 更新如下:

- 新增[mg.combineAsVariants](/apis/mastergo.html#combineasvariants)方法将一组[ComponentNode](/apis/componentNode.html)节点组合成[ComponentSetNode](/apis/componentSetNode.html)节点。

# v1.15.0
发布时间: 2023/03/16

### 更新如下:

- 新增[mg.notify](/apis/notify.html)方法支持设置显示时间和loading，并且支持主动关闭。
- 新增[attachedConnectors](/apis/booleanOperationNode.html#attachedconnectors)表示吸附到节点的连接线节点数组。

# v1.14.0
发布时间: 2023/02/07

### 更新如下:

- 图层新增异步导出接口[exportAsync](/apis/componentNode.html#exportasync)，此接口在图层包含图片时会加载原图。

# v1.13.0
发布时间: 2023/01/12

### 更新如下:

- 添加了对组件属性功能的支持，在以下每种节点类型上具有新的属性和函数：**ComponentSetNode**[componentPropertyValues](/types/componentPropertiesRelated.html)
- [addComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)
- [editComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)
- [deleteComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)

- **ComponentNode(非状态组件)**[componentPropertyValues](/types/componentPropertiesRelated.html)
- [addComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)
- [editComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)
- [deleteComponentProperty](/types/componentPropertiesRelated.html#componentpropertiesmixin)

- **SceneNode(必须是组件子图层，并且不嵌套在实例节点中)**[componentPropertyReferences](/types/componentPropertiesRelated.html#componentpropertyreferences)

- **InstanceNode**[componentProperties](/types/componentPropertiesRelated.html#componentproperties)

InstanceNode 上的 setProperties 函数用作更新组件属性。
ComponentSetNode 上的 componentPropertyDefinitions 属性现已弃用。它将继续返回变量组属性，但建议使用新的组件属性定义属性。
变量属性将继续使用，设置时仍然需使用变量相关api。

- 导出设置新增 [useRenderBounds](/types/exportSettings.html) 属性来控制导出时是否包含图层的外部描边和阴影绘制所占区域，默认为 **`true`** 。
- 定位属性新增 [absoluteBoundingBox](/apis/rectangleNode.html#absoluteboundingbox)，只读属性，用来获取当前图层的绝对定位属性，返回值类型为[Rect](/types/rect.html)。
- 定位属性新增 [absoluteRenderBounds](/apis/rectangleNode.html#absoluterenderbounds)，只读属性，用来获取当前图层的绝对定位属性，其值受旋转、填充、阴影、描边等效果影响，返回值类型为[Rect](/types/rect.html)。

# v1.12.0
发布时间: 2022/12/20

### 更新如下:

- 添加[mg.ui.moveTo](/apis/ui.html#moveto)方法。
- 添加[mg.ui.viewport](/apis/ui.html#viewport)属性
提供移动插件ui视窗的接口，以及视窗的相关属性，可用于获取当前ui视窗信息、定位校验、插件ui内外的坐标系换算等场景。

# v1.11.0
发布时间: 2022/12/15

### 更新如下:

- 添加[getNodeByPosition](/apis/mastergo.html#getnodebyposition)方法。
该方法与鼠标点击画布类似，据给定的画布中的世界坐标，查找相应的节点。如果没有找到对应的节点，则返回 null。
可以用于校验画布中添加图层的定位和信息，判断目标图层是否被遮挡等场景，或者与pluginDrop功能结合，实现“拖拽”进入容器，例如：

```
const containers = new Set<(SceneNode | PageNode)['type']>(['BOOLEAN_OPERATION','FRAME', 'COMPONENT', 'GROUP', 'PAGE'])

mg.on('drop', (dropEvent: DropEvent) => {
  const {dropMetadata, absoluteX, absoluteY} = dropEvent;
  const currentPage = mg.document.currentPage;

  // 获取对应坐标的容器
  let target = mg.getNodeByPosition({x: absoluteX, y: absoluteY});
  while(target && !containers.has(target.type)){
    target = target.parent;
  }
  const parent = target || currentPage;

  mg.createNodeFromSvgAsync(dropMetadata.svg)
    .then((frame) => {
      frame.x = absoluteX - frame.width / 2,
      frame.y = absoluteY - frame.height / 2,
      parent.appendChild(frame)
      mg.document.currentPage.selection = [frame]
      mg.commitUndo();
    })
})
```

- 文字图层分段样式新增[lineHeightByPx](/types/textSegStyle.html)字段，表示文字图层在画布中以px为单位的行高数值，当`lineHeight`为百分比或自动行高时，通过这个字段能够读取文字分段样式中实际行高的像素值。

# v1.10.2
发布时间: 2022/12/13

### 更新如下:

- 废弃[teamLibrary](/apis/mastergo.html#teamlibrary), 改用异步方法[getTeamLibraryAsync](/apis/mastergo.html#getteamlibraryasync)。
- 添加[mg.mixed](/apis/mastergo.html#mixed)属性。
- 修改[rescale](/apis/rectangleNode.html#rescale)描述和边界限制，从限制单次缩放系数最小值，改成限制缩放后图层尺寸最小值

# v1.10.0
发布时间: 2022/12/01

### 更新如下:

- 文字图层和样式支持设置百分比和自动行高

```
const textNode = mg.createText();
textNode.characters = 'text'

//自动行高
textNode.setRangeLineHeight(0, 3, { unit: 'AUTO' });
console.log(textNode.textStyles[0].textStyle.lineHeight); // { unit: 'AUTO' }

//百分比行高
textNode.setRangeLineHeight(0, 3, { unit: 'PERCENT', value: 50 });
console.log(textNode.textStyles[0].textStyle.lineHeight); // { unit: 'PERCENT', value: 50 }

//创建文字样式
const textStyle = mg.createTextStyle({ id: textNode.id, name: 'textStyle', description: 'desc' })

//自动行高
textStyle.lineHeight = { unit: 'AUTO' };
console.log(textStyle.lineHeight); // { unit: 'AUTO' }

//百分比行高
textStyle.lineHeight = { unit: 'PERCENT', value: 50 };
console.log(textStyle.lineHeight); // { unit: 'PERCENT', value: 50 }
```

# v1.9.0
发布时间: 2022/11/24

### 更新如下:

- 全局新增 **拼合** 接口: [flatten](/apis/mastergo.html#flatten)
- 图层新增 **等比缩放** 接口: [rescale](/apis/frameNode.html#rescale)
- 图层新增 **水平/垂直翻转** 接口: [flip](/apis/frameNode.html#flip)
- 文件、页面和容器类图层新增 **按类型查找** 接口: [findAllWithCriteria](/apis/frameNode.html#findallwithcriteria)
- 文字新增 **设置填充样式** 接口: [setRangeFillStyleId](/apis/textNode.html#setrangefillstyleid)
- 文字新增 **设置文字样式** 接口: [setRangeTextStyleId](/apis/textNode.html#setrangetextstyleid)
- [createComponent](/apis/mastergo.html#createcomponent)和[createFrame](/apis/mastergo.html#createframe)支持传入子图层数组。
- `removed`为`true`的图层现在访问和修改属性会有提示。

# v1.8.0
发布时间: 2022/11/18

### 更新如下:

- `clientStorage`新增 [keysAsync](/apis/clientStorage.html#keysasync) 获取所有键名 和 [deleteAsync](/apis/clientStorage.html#deleteasync) 删除对应键名数据 接口。

```
async function getKeys() {
  const keys: string[] = await mg.clientStorage.keysAsync()
  console.log('AllKeys', keys)
}

async function deleteKey(key:string) {
  await mg.clientStorage.deleteAsync(key)
  const data: undefined = await mg.clientStorage.getAsync(key)
  console.log(`Data with key ${key} is removed`)
}
```

# v1.7.0
发布时间: 2022/11/11

### 更新如下:

- [mg.showUI()](/apis/mastergo.html#showui) 新增可选参数 `x` 和 `y` ，支持传入数字或百分比，自定义插件窗口展示在画布的位置。
- **全局新增团队库相关接口**: [teamLibrary](/apis/mastergo.html#teamlibrary) 获取订阅团队库数据。
- [importComponentByKeyAsync](/apis/mastergo.html#importcomponentbykeyasync) 导入订阅的团队库组件。
- [importComponentSetByKeyAsync](/apis/mastergo.html#importcomponentsetbykeyasync) 导入订阅的团队库组件集。
- [importStyleByKeyAsync](/apis/mastergo.html#importstylebykeyasync) 导入订阅的团队库样式。