# 简介
插件继承了 MasterGo 的能力。与 MasterGo 是基于 Web 一样，MasterGo 的插件也是基于 Web 技术的。因此，想要开发 MasterGo 插件需要你至少了解以下技术：

- HTML：[https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- JavaScript：[https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- CSS：[https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
为了提供更好的开发体验，我们提供了良好的 TypeScript 类型支持。TypeScript 是一种可以编译到 JavaScript 的编程语言，配合 VSCode 可以为你带来极佳的开发体验。但对于插件开发来说，使用 TypeScript 并不是必须的，这完全取决于你。
为了便于你创建插件项目，我们提供了插件模板，请阅读开发指南以了解插件的创建、开发与发布。

## 节点树及其层级结构
在 MasterGO 的文件中，一切内容均可以节点（node）的方式来描述，甚至文件本身也是用节点来描述的（DocumentNode 节点）。如下图所示：

文件节点是所有其它节点的根节点，换句话说，其它节点将作为文件节点的子节点或子代节点存在。我们可以用下面的伪代码来描述上图所示的节点层级结构：

```
const root = {
  type: DocumentNode, // 文件节点
  children: [
    {
      type: PageNode, // 页面节点
      children: [
        {
          type: FrameNode, // 容器节点
          children: [
            {
              type: ComponentNode, // 组件节点
              children: [
                { type: EllipseNode },  // 椭圆节点
                { type: RectangleNode } // 矩形节点
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

这些节点共同构成了一棵树型数据结构，理解这一点将非常重要。在编写插件时，你总是可以通过插件 API 来按照相同的层级结构来访问特定的节点，例如：

```
// 读取页面节点
const page = mg.document.children[0]
// 读取该页面下的第一个子节点，即 FrameNode 节点
const frame = page.children[0]
// 读取该 Frame 下的第一个子节点，即 ComponentNode 节点
const component = frame.children[0]
// 读取该 Component 下的第二个子节点，即 RectangleNode 节点
const rectangle = component.children[1]
```

每个节点都由特定的属性和方法，通过这些属性和方法即可实现对 MasterGO 文件内容的增、删、改、查。具体可以查看 API Reference。

## 插件的运行机制
在开始编写插件之前，了解插件的运行机制是非常必要的。本节将带你了解 MasterGo 插件的架构和运行机制。
正如 MasterGo 是基于 Web 技术一样，插件也是基于 Web 技术的。这意味着，你可以使用 JavaScript、HTML、CSS 等技术来构建插件。但出于安全性的考虑，我们在这些 Web 技术上构建了一些规则和限制。

### 为插件构建用户界面
你可以使用 HTML 文件为你的插件创建用户界面，允许用户与插件进行可视化交互。需要指出的是，用户界面是运行在 <iframe> 中的，因此你无法直接在 HTML 文件嵌入的脚本中直接访问 MasterGo 的插件 API。但也正因为用户界面运行在 <iframe> 中，因此，你可以使用全部的 Web API 来构建用户界面。

### 访问 MasterGO 的文件内容
由于用户界面中的脚本无法访问 MasterGo 的文件内容（即无法使用 MasterGo 插件 API），因此你需要编写单独的 JavaScript 脚本来完成该任务。同样出于安全性的考虑，这个特殊的 JavaScript 脚本会运行在主线程的一个沙箱中。该沙箱是一个最小化的 JavaScript 运行环境，你无法通过运行与沙箱中的代码访问浏览器提供的 APIs，如 XMLHTTPRequest。但你仍然可以运行标准的 ES2021 代码。例如 Promise APIs、Uint8Array、JSON 等等。

### 主线程脚本与用户界面间的信息交流
正如上文描述的那样，用户界面内的脚本无法直接访问 MasterGo 文件的内容，而运行在沙箱内的脚本虽然可以调用 MasterGo 插件 API 访问 MasterGo 的文件内容，但无法访问并利用浏览器 APIs。因此为了构建强大的插件，我们需要在运行在用户界面内的脚本与运行在沙箱内的脚本之间建立信息交流的“通道”。如下图所示：

开发指南