# 教程
在本教程中，我们将为你介绍 MasterGo 的主要 API 的使用，以及惯用法。更完整的 API 列表可以查看 API Reference。

## 访问节点
在编写 MasterGo 插件时，最常见的两个需求是：

- 获取当前选择的节点。
- 通过对节点树进行遍历，从而找到目标节点。
根据不同的目的，我们最终找到的目标节点的类型会所有不同。例如，有些插件只关注文字图层（即文本类型的节点），而有些插件则要处理所有类型的节点。不同的节点具有不同的属性和方法，因此，在进一步处理节点之前，一定要确保该节点的类型符合预期。

### 节点类型
在 简介 一节中，我们了解到，MasterGo 文件是由节点树构成的。节点树的中每个节点都具有特定的类型，可以通过节点的 type 属性来获取该节点的类型。如下面的代码所示：

```
console.log(mg.document.type); // 'DOCUMENT'
```

mg.document 用来获取文档节点，它描述了整个 MasterGo 文件，因此它的类型永远是 'DOCUMENT'。
每个文件都会包含一或多个页面，所以文档的节点的子节点，由页面节点构成：

```
const page = mg.document.children[0];
console.log(page.type); // 'PAGE'
```

每个页面都由一或多个图层构成，图层间也可能具有父子关系，每个图层都对应了特定的节点类型，依具体情况而定。假设一个页面只包含一个矩形图层：

```
const page = mg.document.children[0];
const rect = page.children[0];
console.log(rect.type); // 'RECTANGLE'
```

### 获取当前选择的节点
在设计一个插件时，我们通常要求插件对当前所选择的内容进行处理。这时，我们可以通过 mg.document.currentPage.selection 来获取用户当前选择的图层节点。这里需要注意的是，在获取用户当前选中的图层之前，我们需要先获取到用户当前正在操作的页面。因为一个文档可能由多个页面构成，同时我们又不希望插件隐式地操作那些未展示的页面的内容，因此，我们需要使用 mg.document.currentPage 获取当前页面，再进一步获取用户选择的内容。

```
const currentPage = mg.document.currentPage;
const selectedNodes = currentPage.selection;
```

由于用户可以选中多个图层，所以 selectedNodes 将是由节点构成的数组。

### 遍历节点
对于一些插件来说，我们不仅仅希望它能够处理用户当前选择的内容，而是希望它能够处理当前页面的所有图层，或者当前页面中的某一类图层。这时，为了找到符合要求的图层节点，我们需要对整个页面或页面的一部分节点进行遍历，从而筛选出目标图层节点。
遍历节点的方式有两种，第一种方式是采用 MasterGo 的内建 API，对于任何含有子节点的节点（即带有 children 属性的节点）来说，都会存在以下用于节点查找的方法：

```
// 查找符合要求的直接子节点
findChildren(callback?: (node: SceneNode) => boolean): SceneNode[]
// 查找第一个符合要求的直接子节点
findChild(callback: (node: SceneNode) => boolean): SceneNode | null
// 查找符合要求的子代节点
findAll(callback?: (node: SceneNode) => boolean): SceneNode[]
// 查找第一个符合要求的子代节点
findOne(callback: (node: SceneNode) => boolean): SceneNode | null
```

我们以查找当前页面中所有的矩形节点为例：

```
const currentPage = mg.document.currentPage;
const rects = currentPage.findAll((node) => true);

console.log(rects); // RectangleNode[]
```

另外需要注意的一点是，findChildren 与 findChild 用于查找当前节点的直接子节点；而 findAll 和 findOne 则用于查找当前节点的所有子代节点。
除了使用 MasterGo 内建的 API 进行节点遍历与查找之外，还可以自行实现对节点的遍历。例如下面的 traveres 方法用于遍历节点并找出所有类型为 INSTANCE 的子节点：

```
function traverse(node, cb) {
  if ("children" in node) {
    if (node.type === "INSTANCE") {
      cb(node);
    }
    for (const child of node.children) {
      traverse(child, cb);
    }
  }
}
```

我们可以像如下这样使用它：

```
// 找出所有 mg.document.currentPage 下所有类型为实例的节点
traverse(mg.document.currentPage, (node) => {
  console.log(node); // node.type === 'INSTANCE'
});
```

## 属性编辑
插件不仅可以读取图层节点的属性，还可以通过设置节点的属性来改变其展示。在内部实现中，节点的属性被设置为一对 getter/setter。当修改节点的属性值时，此改动会同步到 MasterGo 文件中。例如，让某个节点的向右边位移 100 个单位距离：

```
node.x += 100; // 只需要修改节点的 x 属性值即可
```

但需要注意的是，并非所有的节点属性都像 node.x 属性这样简单（原始值），还有一部分节点属性的数据结构是对象或数组构成的。对于复杂结构的属性值（对象或数组）来说，你无法直接通过修改这些对象或数组的属性或元素来完成图层属性的修改，例如下面的代码是无效的：

```
// 无效
node.fills[0].color.r = 10;
// 无效
mg.document.currentPage.selection.push(otherNode);
```

作为代替，你应该总是使用新的属性值来“完全地替换掉”旧的属性值，下面的代码给出了正确的实现：

```
// 克隆一个新的 fills 属性值
const newFills = clone(node.fills);
newFills[0].color.r = 10;
node.fills = newFills; // 使用新的 newFills 完全替换掉 node.fills

// 克隆一个新的 selection 属性值
const newSelection = mg.document.currentPage.selection.slice();
newSelection.push(newNode);
mg.document.currentPage.selection = newSelection; // 使用新的 newSelection 完全替换掉 mg.document.currentPage.selection
```

在上面这段代码中，我们使用 clone 函数来创建一个对象或数组的拷贝，一个简单的实现方式是：

```
function clone(val) {
  return JSON.parse(JSON.stringify(val));
}
```

当然，对于更通用的情况，我们推荐使用 loadsh。

## 发送网络请求
在本节中，我们将向您展示在 MasterGo 插件中发送网络请求的基础知识。它与直接在 Web 浏览器中运行的普通 JavaScript 基本相同：唯一需要注意的是，用于发送网络请求的 API 由浏览器提供，而不是由 MasterGo 插件沙箱本身提供。您可能记得在构建用户界面部分中，您需要创建一个<iframe>来访问浏览器 API。
下面的插件演示了这一点。它创建一个不可见<iframe>的worker，然后使用它来发送网络请求。当它获得该网络请求的结果时，它会创建一个包含响应内容的文本节点。
main.ts：创建一个iframe

```
mg.showUI(__html__)
mg.ui.postMessage({ type: 'request' })

mg.ui.onmessage = (msg) => {
  const text = mg.createText()
  // 将文字图层移动到我们的视野中
  text.x = mg.viewport.center.x
  text.y = mg.viewport.center.y

  mg.loadFontAsync(text.textStyles[0].textStyle.fontName as FontName)
    .then(() => {
      text.characters = msg
      mg.closePlugin()
    })
}
```

worker（不可见的“UI”，它是<iframe>里面的内容）在一个单独的文件中实现，该文件是 manifest.json 中 ui字段引用的部分. 在这里，worker只是简单地制定一个标准XMLHttpRequest并将结果发送回主线程。
ui.html：发送网络请求

```javascript
<script>
window.onmessage = async (event) => {
  if (event.data.type === 'request') {
    const request = new XMLHttpRequest()
    request.open('GET', 'https://jsonplaceholder.typicode.com/posts')
    request.responseType = 'json'
    request.onload = () => {
      window.parent.postMessage(request.response[0].title, '*')
    };
    request.send()
  }
}
</script>
```

> > **TIP**
> 注意：

- 由于 MasterGo 和 MasterGo 插件在浏览器环境中运行，因此适用[跨域资源共享](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)策略。插件在具有空源(`origin`为`null`)的 iframe 内运行。这意味着我们将只能调用 `Access-Control-Allow-Origin: *`的APIs（即那些允许从任何来源访问的 API）。虽然使用CORS代理可以做到，但这通常不是您需要或不应该使用的东西。
- 由于MasterGo是https的环境和浏览器的安全限制(CSP), 它要求插件发出的网络必须也是https的，当我们发送http请求时，会有很大几率被浏览器限制。

## 处理文本
当我们使用文本节点时，需要以下事项：

- 多段样式
- 加载字体
- 字体缺失

### 多段样式
我们可以对单个字符设置许多文本属性。在MasterGo中，文字的分段样式都可以在textStyles数组中获取， 因此，我们会发现textStyles中会存在多个元素，此时该文字就具有多段的样式。
假设有一个文本节点包含文本 hello world。我们来看一下该节点的字体名称

```
// Output {family: 'Source Han Sans CN', style: 'Bold'}
textNode.textStyles[0].textStyle.fontName

// Output {family: 'Source Han Sans CN', style: 'Regular'}
textNode.textStyles[0].textStyle.fontName
```

通常，我们在获取文字分段样式时用 textStyles，而 setRange* 函数则用来设置特定字符范围的样式。

### 加载字体
文本节点的最重要一点是，更改文本节点的内容前需要加载其字体，并且字体并不总是可用。如果我们尝试更改 fontSize 而不先加载该文本节点的字体，插件将引发异常。
设置 fontName 或 textStyleId 属性时，只需加载当前用到的新字体。设置影响文本布局的任何其他属性时，需要加载文本节点已使用的所有字体。这包括以下属性和函数：

- `characters`
- `insertCharacters()`
- `deleteCharacters()`
- `setRangeFontSize()`
- `setRangeFontName()`
- `setRangeTextCase()`
- `setRangeTextDecoration()`
- `setRangeLetterSpacing()`
- `setRangeLineHeight()`
- `setRangeTextStyleId()`
我们无需加载字体即可更改仅影响颜色和笔划的属性，例如 .fills、.fillStyleId、.strokes、.strokeWeight、.strokeAlign、.strokeStyleId、.strokeDashes。
加载字体是通过 mg.loadFontAsync(fontname) 来完成的.

### 字体缺失
在加载字体之前，我们需要检查 text.hasMissingFont。如果我们的插件适用于文本节点，请不要忽略它。虽然在测试期间不那么频繁，但在现实世界中，我们的用户会尝试在缺少字体的文件中运行我们的插件是很常见的。

#### 文本在 MasterGo 中的工作方式（以及为什么需要加载字体）
当用户键入文本节点或更改其属性之一时，我们会生成一个路径来表示文本，并将其与文本节点一起存储。这样，共享文件（例如，共享给客户）可以让他们按原样查看设计。即使他们的系统上没有安装字体。但是，这意味着即使文本节点看起来不错，也可能无法编辑。
这是 MasterGo 需要做的许多微妙之处之一，以维护云工具的核心价值主张：每个人查看同一个文件总是看到同样的东西。
除此之外，字体文件并不总是加载到内存中，即使它可以从用户的本地计算机上获得也是如此。这是因为字体文件可能很大，可能有很多，并且在编辑文本之前不需要它们。这使得在启动时加载它们代价可能非常高。因此，必须调用 loadFontAsync 以确保字体可用。

#### 未加载字体与缺失的字体
需要注意未加载的字体与丢失的字体无关。所有字体都是未加载的，除非我们的插件通过调用 loadFontAsync 加载它们。 缺失字体是用户无法使用的字体。例如，用户创建了一个文本节点，而该用户没有在其计算机上安装此文本节点中使用的字体。

## 填充与图片处理
本节，我们将通过为一个矩形创建图片填充的例子来学习如何创建、修改一个图层的填充。在创建为图片填充之后，我们还会继续开发一个置灰图片的插件，在这个过程中，我们将学会插件开发中一些通用的范式，例如，如何利用插件 UI 实现图片数据的编码、解码。

### 创建图片填充
首先，在画布中创建并选中一个矩形图层，如下图所示：

接着，将复制如下代码到插件：

```
async function fillTheSelection() {
  // 获取当前选中的图层
  const node = mg.document.currentPage.selection[0] as RectangleNode;
  // 创建一个图片对象
  const imageHandle = await mg.createImage(
    new Uint8Array([
      137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 0, 5,
      0, 0, 0, 5, 8, 6, 0, 0, 0, 141, 111, 38, 229, 0, 0, 0, 28, 73, 68, 65, 84,
      8, 215, 99, 248, 255, 255, 63, 195, 127, 6, 32, 5, 195, 32, 18, 132, 208,
      49, 241, 130, 88, 205, 4, 0, 14, 245, 53, 203, 209, 142, 14, 31, 0, 0, 0,
      0, 73, 69, 78, 68, 174, 66, 96, 130,
    ])
  );

  // 设置图片填充
  node.fills = [
    {
      type: "IMAGE",
      scaleMode: "FILL",
      imageRef: imageHandle.href,
    },
  ];
}
fillTheSelection();
```

接着运行插件，你会发现选中的矩形会存在一个图片填充，如下图所示：

在上面的例子中，我们硬编码了图片数据。实际上，你可以结合插件 UI 和网络请求，从远程服务器中获取图片。

### 处理图片数据
假设，这里有一个存在图片填充的图层，我们希望编写一个插件，它可以对图片填充中的图片进行操作，例如将图片置灰、颜色反转等。我们的思路应该是这样的：

- 遍历图层的填充，并过滤出图片填充。
- 图片填充的数据对象中会持有图片的 `href` 路径。
- 调用 `mg.getImageByHref` 函数根据图片的 `href` 路径取得图片对象，即 `imageHandle`。
- 通过 `imageHandle.getBytesAsync` 函数取得图片的数据（`Uint8Array`）格式,，记作 `bytes`。
- 插件主线程代码调用 `mg.ui.postMessage(bytes)` 将图片数据发送给插件 UI，因为处理图片数据需要借助 `canvas`，但插件代码运行在沙盒中，无法操作 DOM 元素。
- 插件 UI 接收到图片数据后，对数据做进一步处理，再将处理过的图片数据发回插件的主线程代码。
- 插件主线程代码在接收到由插件 UI 发过来的新图片数据后，再使用新的图片数据设置此选中图层的图片填充即可。
具体的代码实现如下：

```
// 插件的主线程代码
async function run() {
  // 获取选中的图层
  const node = mg.document.currentPage.selection[0] as RectangleNode;
  const newFills: Paint[] = [];

  // 展示 UI，但对用户不可见，因为此功能无需用户与 UI 进行交互
  mg.showUI(__html__, { visible: false });

  // 遍历图层的填充数组
  node.fills.forEach(async (fill) => {
    // 过滤出图片填充
    if (fill.type === "IMAGE") {
      // 获取到图片对象
      const imageHanle = mg.getImageByHref(fill.imageRef);

      // 根据图片对象，获取到图片数据，Uint8Array 格式
      const bytes = await imageHanle.getBytesAsync();

      // 将图片数据发送给插件 UI
      mg.ui.postMessage(bytes);

      // 等待并接收插件 UI 将处理过的图片数据
      const { imageData } = await new Promise<{ imageData: Uint8Array }>(
        (resolve, reject) => {
          mg.ui.onmessage = (value) => resolve(value);
        }
      );

      // 创建新的填充
      const newFill = JSON.parse(JSON.stringify(fill));
      newFill.imageRef = (await mg.createImage(imageData)).href;
      newFills.push(newFill);
    }
  });
  
  node.fills = newFills;
}

run();
```

下面是插件 UI 中的代码实现：

```javascript
<!DOCTYPE html>
<head></head>
<body>
  <script>
    window.onmessage = async (event) => {
      // 接收由插件主线程代码发送过来的图片数据
      const bytes = event.data;

      // 创建 canvas 元素
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");

      // 使用 canvas 元素解码图片的 Uint8Array 的数据为 ImageData 数据
      const imageData = await decode(canvas, ctx, bytes);
      const pixels = imageData.data;

      // 操作像素数据，将图片置灰
      for (var i = 0; i < pixels.length; i += 4) {
        let lightness = parseInt(
          (pixels[i] + pixels[i + 1] + pixels[i + 2]) / 3
        );
        pixels[i] = lightness;
        pixels[i + 1] = lightness;
        pixels[i + 2] = lightness;
      }

      // 将 ImageData 数据再编码为 Uint8Array 数据，并发送回插件主线程的代码
      const newBytes = await encode(canvas, ctx, imageData);
      window.parent.postMessage({ imageData: newBytes }, "*");
    };
  </script>
</body>
```

在上面这段代码中提到了两个工具函数 decode 和 encode，它们的作用分别是：

- `decode` - 解码图片的 `Uint8Array` 的数据为 `ImageData` 数据
- `encode` - 将 `ImageData` 数据再编码为 `Uint8Array` 数据
它们的具体实现如下：

```
async function decode(canvas, ctx, bytes) {
  const url = URL.createObjectURL(new Blob([bytes]));
  const image = await new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => reject();
    img.src = url;
  });
  canvas.width = image.width;
  canvas.height = image.height;
  ctx.drawImage(image, 0, 0);
  const imageData = ctx.getImageData(0, 0, image.width, image.height);
  return imageData;
}

async function encode(canvas, ctx, imageData) {
  ctx.putImageData(imageData, 0, 0);
  return await new Promise((resolve, reject) => {
    canvas.toBlob((blob) => {
      const reader = new FileReader();
      reader.onload = () => resolve(new Uint8Array(reader.result));
      reader.onerror = () => reject(new Error("Could not read from blob"));
      reader.readAsArrayBuffer(blob);
    });
  });
}
```

## 动画
在主线程的代码中，可以使用 requestAnimationFrame 来完成动画。如下代码所示，它实现了让选中的第一个图层进行旋转：

```
const { cos, sin } = Math;

function run() {
  const node = mg.document.currentPage.selection[0] as RectangleNode;

  let angle = node.rotation + 180;

  function rotate() {
    angle++;
    node.rotation = (angle % 360) - 180;

    requestAnimationFrame(rotate);
  }
  requestAnimationFrame(rotate);
}

run();
```

你可能已经注意到了，在上面的代码中，为了处理角度，我们对其进行了转换。这是因为 node.rotation 的取值范围是区间：[-180, 180]。最终的效果如下：

## 操作样式
使用插件 API 也可以创建样式，就像在画布中一样。关于样式，可以通过阅读官方教程 “了解样式” 来了解其作用于用法。
我们提供了三个用于创建不同种类样式的 API：

- [mg.createStrokeStyle](/apis/mastergo.html#createstrokestyle)，创建用于描边的样式。
- [mg.createFillStyle](/apis/mastergo.html#createfillstyle)，创建用于填充的样式。
- [mg.createEffectStyle](/apis/mastergo.html#createeffectstyle)，创建用于特效的样式。
- [mg.createTextStyle](/apis/mastergo.html#createtextstyle)，创建文字样式。
下面的例子展示了如何创建样式，并将该样式设置给选中的图层：

```
// 获取当前选中的第一个图层
const node = mg.document.currentPage.selection[0];

// 创建一个 Paint 样式
const myStyle = mg.createFillStyle({ id: node.id, name: 'paint', description: '这是一个paint' });
// 设置样式的名称
myStyle.name = "styles/fill/foo";
// 创建一个纯色填充
const paints = [
  {
    type: "SOLID",
    color: {
      r: 0.7,
      g: 0.2,
      b: 0.2,
      a: 1,
    },
    isVisible: true,
    alpha: 1,
    blendMode: "NORMAL",
  },
];
// 将该填充设置到刚刚创建的 Paint 样式上
myStyle.paints = paints;

// 最后，将刚刚创建的样式的 id 设置图层节点即可
node.fillStyleId = myStyle.id;
```

这里需要注意的是，样式的名称会根据字符 / 分割为命名空间后存储，如下图所示：

## ui侧触发drop事件
如果需要将插件ui侧的图标或者元素“拖拽”渲染到画布内，然而由于插件ui是由iframe渲染，窗口不同，无法监听和换算鼠标坐标对应的画布内坐标。此时可以考虑由ui触发drop事件，来模拟“拖入”画布效果，并在插件侧监听drop事件，可以获取经过换算后的坐标信息，以及ui传递的其他原始数据。
当ui侧postMessage包含PluginDrop属性，且其值符合PluginDrop类型，则此次通信不会触发mg.ui.onmessage，而是触发drop事件，回调参数类型为DropEvent。
例如，想要将ui中的svg"拖入"画布，ui侧代码为：

```css
<div draggable="true" id="draggable" >
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="none" version="1.1" width="44" height="44" viewBox="0 0 44 44"><g style="mix-blend-mode:passthrough"><ellipse cx="22" cy="22" rx="22" ry="22" fill="#D8D8D8" fill-opacity="1"/></g></svg>
</div>
<script>
document.getElementById('draggable').addEventListener('dragend', (e) => {
  const { clientX, clientY } = e;
  parent.postMessage({
    pluginDrop: {
      clientX,
      clientY,
      dropMetadata: {
        svg: e.target.innerHTML
      },
    }
  }, '*');
})
</script>
```

主线程的代码为：

```
mg.on('drop', (dropEvent: DropEvent) => {
  const {dropMetadata, absoluteX, absoluteY} = dropEvent;
  mg.createNodeFromSvgAsync(dropMetadata.svg)
    .then((frame) => {
      mg.document.currentPage.appendChild(frame)
      frame.x = absoluteX - frame.width / 2,
      frame.y = absoluteY - frame.height / 2,
      mg.document.currentPage.selection = [frame]
      mg.commitUndo();
    })
})
```

开发指南