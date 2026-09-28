# 开发指南
在开始之前，你需要对插件的开发有一定的了解，如果还没有，请移步这里。 接下来，我们将带你从零搭建一个基于配置模型的插件。

## 准备设计稿
我们以 Ant Design 开源组件库为例，首先我们需要准备一套 Ant Design 的设计稿。以按钮为例。

## 开发插件逻辑
在main.ts中添加设置配置模型代码。

```
mg.codegen.setComponentTemplate({
  documentId: '120789721220589',
  name: 'antd',
  importType: 'IMPORT',
  importPath: [],
  framework: 'REACT',
  components: []
});
```

> > **TIP**
> 其中的documentId可以使用 mg.documentId 获取。 请不要直接在代码中使用mg.documentId，通过mg.documentId获取对应静态值填入到documentId上。

在importPath字段中添加react和antd的对应导入关系。

```
[
  {
    name: 'react',
    importName: '',
    type: "script",
    path: 'https://esm.sh/react@18.2.0',
  },
  {
    name: 'react-dom',
    importName: '',
    type: "script",
    path: 'https://esm.sh/react-dom@18.2.0',
  },
  {
    name: 'antd',
    importName: 'antd',
    type: "script",
    path: 'https://esm.sh/antd@5.8.6?bundle',
  },
  {
    name: 'antd-icons',
    importName: 'icons',
    type: "script",
    path: 'https://esm.sh/@ant-design/icons@5.2.6?bundle',
  },
]
```

## 添加一个组件配置

> > **TIP**
> 如果填写path字段，则可以进行效果预览。 添加importName字段，会在代码中引入该模块

在components中加入一个组件配置

```
{
  name: 'Button',
  props: [],
  source: {
    path: 'antd',
    export: 'Button',
  },
  id: '0:77482',
},
```

> > **TIP**
> 其中的id是这个组件集的id。它会成为唯一标识标记所有使用这个组件集的组件实例都使用这套标准来进行解析

保存并运行组件，可以在D2C的tab中查看内容：

## 为组件配置属性
在props字段中加入对应属性配置

```
[
  {
    type: 'STRING',
    name: 'type',
    aliasName: 'Type',
    lowerCase: true,
  },
  {
    type: 'STRING',
    name: 'size',
    aliasName: 'Size',
    lowerCase: true,
  },
  {
    type: 'BOOLEAN',
    name: 'ghost',
    aliasName: 'Ghost',
    aliasMap: {
      True: true,
      False: false,
    },
  },
  {
    type: 'BOOLEAN',
    name: 'danger',
    aliasName: 'Danger',
    aliasMap: {
      True: true,
      False: false,
    },
  },
  {
    type: 'BOOLEAN',
    name: 'disabled',
    aliasName: 'State',
    aliasMap: {
      Disabled: true,
    },
  },
  {
    type: 'STRING',
    name: 'shape',
    aliasName: 'Shape',
    lowerCase: true,
  },
]
```

由于在设计稿中，组件集的属性字段大部分与 Ant Design 的设计匹配，因此只需将对应的属性关联起来，并配置好对应的 type。 但需要注意，如果在设计稿属性设计的与代码组件设计的不能一一对应时，就需要灵活使用组件属性配置来完成对应的映射关系。

> > **TIP**
> 例如设计师习惯将disabled和hover，focus等属性放在一个属性中。但在研发侧，只会有一个 disabled 的boolean属性。此时就需要设计一个 BOOLEAN 属性的disabled字段。它关联的是设计稿中的STATE字段，并且当STATE字段的值为Disabled时， disabled 字段的值为true

```
{
  type: 'BOOLEAN',
  name: 'disabled',
  aliasName: 'State',
  aliasMap: {
    Disabled: true,
  },
}
```

此时再运行插件，你会看到:

## 为组件配置插槽
给你的组件配置添加插槽属性

```
slots: [
  {
    name: 'default',
    relateNodeNames: [['Content', 'Button']],
    type: 'TEXT',
  },
],
```

其中 relateNodeNames 是该组件关联的节点，您可以通过图层树种的路径给出。

当类型为 TEXT 时，该插槽会抓取对应的文字作为children的内容。当没有该类型时，配置模型会根据您指定的路径抓取对应节点继续递归解析。在完成嵌套组件的使用时，您可以通过制定 slots 来完成该目的。

> > **TIP**
> relateNodeNames 支持正则，但需要通过字符串来表达正则表达式，因为在插件的沙盒中，未提供正则对象。

> > **TIP**
> 在vue中，slots 会根据name生成对应的具名插槽。 在react中，如果 slots 的name是default，则生成子节点。如果非default，会生成对应的jsx节点的属性。当然，您也可以用过 props 中type是 SLOT 来完成该目标。

保存并运行插件:

## 预览效果
如果您配置了 importPath 中的 path。则可以点击右侧的预览，查看预览效果
该预览框中是根据生成的代码运行处的效果。

## 发布配置模型
当您已经配置完对应的组件。可以点击插件开发与发布中的上传为组件模板
上传完成后，任何使用该组件库作为团队库组件的文档，也都可以通过该插件匹配对应的配置模型。
到这里，我们一个简单的配置模型插件就完成了。

简介
Component Template