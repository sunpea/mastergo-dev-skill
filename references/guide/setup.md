# 开发指南
在 简介 中，我们详细地介绍了插件的运行机制。在本节中，我们将带你从零开始构建一个可运行的插件。我们将要创建的插件能够接收用户输入的数字，并创建指定数量的椭圆图层。本节将涉及以下知识点：

- 什么是 `manifest.json` 文件，以及它的作用。
- 如何构建用户界面
- 如何调用插件 API
- 如何使用模板
- 如何使用 TypeScript 提升开发体验
- 如何在用户界面与主线程之间进行消息传递

## manifest.json
manifest.json 文件非常重要，并且是每个插件必须包含的文件。它包含了插件的重要信息。下面是 manifest.json 文件的内容示例：

```
{
  "name": "my-first-mastergo-plugin",
  "id": 1234567890,
  "api": "1.0.0",
  "main": "./main.js",
  "ui": "./ui.html",
  "menu": [
    {
      "name": "打开主页面",
      "command": "home"
    },
    {
      "name": "执行B功能",
      "command": "run"
    },
  ],
  "permissions": ["currentuser"]
}
```

- `name: string`
用来指定插件的名称，该名称会出现在 “插件” 菜单栏。

- `id?: number`
id 通常不需要手动指定，它用于插件的发布更新和通信隔离等，每个插件唯一。导入的manifest.json没有id，或者创建新插件时，系统会帮生成不重复的id。

- `api: string`
用于指定插件所使用的 API 版本，我们推荐你总是使用最新的插件版本号，当前可使用 1.0.0。

- `main: string`
main 选项是一个相对路径，用来指定运行在沙箱中的 JavaScript 脚本。如：main: "./main.js"。

- `ui: string`
与 main 选项类似，ui 选项用来指定用户界面要加载的 HTML 文件路径，例如：ui: "./ui.html"。

- `menu?: ManifestMenu[]`
menu 选项是一个json数组，设置menu可以为插件添加子菜单入口，并调整菜单结构和分割线的位置。在运行时触发插件的 run 事件，其参数为选中的菜单中设置command值，也可以通过 mg.command 获取。
若不设置menu，则为一级菜单入口，对应的command值为空串

```
type ManifestMenuItem = 
  { name: string; command: string; } // 设置可点击运行的子菜单结构
  | { name: string; menu: ManifestMenuItem[] } // 设置子菜单结构
  | { separator: true } // 设置分割线
```

- `permissions?: PluginPermissionType[]`
permissions 属性设置后，该插件可使用该权限对应的接口。

```
type PluginPermissionType = "currentuser"
```

currentuser: 设置后插件可使用mg.currentUser接口。

## 创建一个插件
了解了 manifest.json 文件的作用之后，我们就可以着手创建插件了。
我们可以通过点击 “插件 -> 开发者模式 -> 创建/添加插件” ，输入插件名称来使用工程模板生成插件，这样的话，只需要跟随引导一步步来就可以了。
当然，我们也可以先在本地创建好插件，然后导入。这样的话，就需要我们先准备一下目录结构及文件：

```
my-plugin
├── manifest.json
├── main.js
├── ui.html
```

其中，manifest.json 的内容如下：

```
// manifest.json
{
  "name": "my-plugin",
  "id": "",
  "api": "1.0.0",
  "main": "./main.js",
  "ui": "./ui.html"
}
```

没错，一个最小的插件已经创建完毕了，仅需要三个文件。接下来我们就开始构建用户界面。

## 构建用户界面
本质上，构建用户界面与开发传统 Web 应用没有任何区别。你甚至可以使用现代 Web 框架，如 Vue、React、Svelte 等等。不过，在本节的示例中，我们一切从简，即使用原生技术构建用户界面。
首先，在 ui.html 文件中编写如下 HTML 内容：

```css
<!DOCTYPE html>
<body>
  <div class="content">
    <div style="margin-bottom: 20px; color: #fff;">
      输入椭圆的数量：<input type="text" />
    </div>
    <button id="btn">创建</button>
  </div>
</body>
```

然后在 main.js 中编写如下 JavaScript 代码：

```
// main.js
mg.showUI(__html__) // 用于展示插件用户界面
```

## 调试插件
下一步我们要做的，就是运行插件代码，看它是否按预期的那样来展示用户界面。为了调试插件，我们需要下载 MasterGo 客户端：点击下载
开发客户端下载完毕后，运行客户端。点击顶部 “插件” 菜单按钮，或在文件页画布内点击鼠标右键，调出 “插件” 菜单，点击 “开发者模式 -> 创建/添加插件”。如下图所示：

或在画布中右键菜单：“插件 -> 开发者模式 -> 创建/添加插件”：

此时，会弹出插件创建面板，如下图所示：

如上图所示，你既可以选择通过模板生成一个全新的插件；也可以选择已有的插件。由于我们已经创建了自己的插件，因此点击 "点击或拖动上传 manifest.json 文件" 按钮，并选择插件的 manifest.json 文件。如下图所示：

选择 manifest.json 文件后，不出意外的话会跳转到如下界面。

创建成功后的插件会出现在 顶栏菜单栏 和 具有编辑权限的 画布右键菜单 中 “插件 -> 开发者模式” 菜单下，点击插件名称运行此插件。

或在画布中右键菜单 “插件 -> 开发者模式”：

不出意外的话，我们将看到如下用户界面：

## 向主线程代码传递消息
现在，我们已经有了用户界面，并且可以通过 input 输入框接收用户输入。接下来我们要做的是，将用户输入的数量数据传递给主线程的 JavaScript 代码。
为了完成消息传递的任务，我们需要在 iframe 中调用 parent.postMessage 函数。如下面的代码所示：

```css
<!DOCTYPE html>
<body>
  <div class="content">
    <div style="margin-bottom: 20px; color: #fff;">
      输入椭圆的数量：<input type="text" />
    </div>
    <button id="btn">创建</button>
  </div>

  <script>
    // 获取 input 表单
    const input = document.querySelector('input')
    // 为按钮绑定 click 事件
    document.getElementById('btn').addEventListener('click', (ev) => {
      // 当点击按钮时，将表单的值转为数字类型，并发送给主线程
      parent.postMessage({ count: Number(input.value) }, '*')
    })
  </script>
</body>
```

主线程的代码需要监听 onmessage 事件，从而有能力接收由 iframe 发送过来的数据。这需要我们修改 main.js 代码，如下代码所示：

```
mg.showUI(__html__)

mg.ui.onmessage = (msg) => {
  console.log(msg) // { count: 3 }，假设用户在 input 框中输入数字 3
}
```

最后，重新运行插件并打开的开发者工具，如下图所示：

打开控制台后效果如下：

此时，如果你在输入框中输入数字 3，并点击“创建”按钮，将会在控制台中看到主线程接收并打印出来的数据：{ count: 3 }。

## 调用插件 API 创建椭圆图层
现在，主线程已经能够接收来自用户界面的数据了。接下来，只需要在主线程的代码中调用 MasterGo 插件 API 来创建椭圆图层即可。具体实现如下：

```
// main.js
mg.showUI(__html__)

mg.ui.onmessage = (msg) => {
  const count = msg.count
  for (let i = 0; i < count; i++) {
    // mg 是全局变量，用来访问 MasterGo 提供的 API 接口
    // mg.createEllipse() 可以创建椭圆图层
    mg.createEllipse()
  }
}
```

在调试过程中，我们可以使用快捷键来运行最近一次运行过的插件：
Windows 快捷键： Ctrl + Alt + P Mac 快捷键： Command + Option + P

## 插件管理与插件发布
插件开发完成后就可以将插件发布到应用市场，让所有的 MasterGo 用户了解并安装你的插件。下面将介绍如何管理和发布插件。

### 插件发布
首先，打开 MasterGo 客户端，点击插件菜单，选择管理插件，如下图所示。

或在画布中通过右键菜单打开：

插件开发完成后就可以将插件发布到应用市场，让所有的 MasterGo 用户了解并安装你的插件。下面将介绍如何发布你的插件。
我们需要在 开发中 面板中找到我们要发布的插件，点击右侧按钮，点击发布。

选择发布到团队或是发布到社区，然后填写对应的发布信息，完成后点击发布按钮。
发布到社区的插件，会被所有用户看到，但需要先经过审核，审核通过后，方可在插件社区搜索到。
发布到团队的插件无需审核，发布成功后即可出现在团队成员的已安装列表中。

如果需要发布到社区，我们需要填写插件的详细信息，如插件 LOGO、插件名称、插件封面、插件介绍等：

如果需要发布到团队，则需要先选择目标团队：

然后填写插件的基本信息：

### 插件管理
我们安装的所有插件，均可在 已安装 列表中找到，包括团队插件和社区插件。
但是我们仅可以卸载社区插件，团队插件在 已安装 列表中是无法卸载的。
开发中 列表展示了所有我们正在开发的插件，开发中的插件我们可以选择发布或是移除，注意：移除不会删掉本地的代码，移除后的插件如果后续还想发布，只需要再导入即可。
在 审核中 列表中，我们可以选择取消发布插件。
在 未通过 列表中，我们可以查看插件被拒绝的原因。
已通过 的社区插件，将会出现在插件社区，并且不可下架或移除。当然，团队插件是可以从相关团队下架的。

## 模板的使用
在上面的教程中，我们已经详细了解了html模板的使用，接下来，我们来了解一下vue模板和react模板的创建和使用：
首先，我们在菜单中选择 “插件 -> 开发者模式 -> 创建/添加插件”，输入要创建的插件名字后点击下一步，进入到模板选择界面：

### vue模板

选中 vue 模板并保存到本地之后，在 开发中 面板中，找到我们刚刚创建的模板：

可以看到，此时的插件是不可以直接运行的，提示 无法读取main文件 ，不要慌张，出现这个提示是正常的，这是因为创建的模板需要先 build 一下，才能正常运行。
此时，我们需要在编辑器中打开刚刚创建好的模板项目，开始编写插件~
首先我们需要安装一下依赖，我们推荐使用 yarn 来进行安装：

```
yarn install
```

我们还是以上面的创建圆形代码为例
首先，我们在 ui/App.vue 中编写代码

```css
<template>
  <div style="margin-bottom: 20px; color: #fff;">
      输入椭圆的数量：<input type="number" v-model="count" />
  </div>
  <button @click="create">创建</button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  setup() {
    return {
      count: 0,
    }
  },
  methods: {
    create() {
      parent.postMessage({ count: this.count }, '*')
    }
  }
})
</script>
```

然后，在 lib/main.ts中编写代码

```
mg.showUI(__html__)

mg.ui.onmessage = (msg) => {
  const count = msg.count
  for (let i = 0; i < count; i++) {
    // mg 是全局变量，用来访问 MasterGo 提供的 API 接口
    // mg.createEllipse() 可以创建椭圆图层
    mg.createEllipse()
  }
}
```

编写完成~
现在让我们来 build 一下~

```
yarn build
```

build完成后，可以看到，出现了一个新的文件夹： dist 文件夹，文件夹下面有两个文件：main.js 和 index.html，就是我们刚刚新鲜出炉的插件代码~
此时，我们再打开 MasterGo 客户端，打开插件管理面板，可以看到，刚刚的红色提示 请配置main文件 已经消失不见啦，这就意味着，现在我们的代码可以正常运行了~

我们可以选择顶部插件菜单，或是画布右键 “插件 -> 开发者模式” ，点击我们刚刚编写完的插件 vue-plugin, 运行插件：

当当当当！大功告成~

### react模板

选中 react 模板并保存到本地之后，在 开发中 面板中，找到我们刚刚创建的模板：

可以看到，此时的插件是不可以直接运行的，提示 无法读取main文件 ，不要慌张，出现这个提示是正常的，这是因为创建的模板需要先 build 一下，才能正常运行。
此时，我们需要在编辑器中打开刚刚创建好的模板项目，开始编写插件~
首先我们需要安装一下依赖，我们推荐使用 yarn 来进行安装：

```
yarn install
```

我们还是以上面的创建圆形代码为例
首先，我们在 ui/App.tsx 中编写代码

```javascript
import { useState, useCallback } from 'react'

function App(){
    const [value, setValue] = useState<number>(0);
  
    const handleChange = useCallback((event) => {
      setValue(parseInt(event.target.value));
    }, []);
    const create = () => {
      parent.postMessage({ count: value }, '*');
    }
  
    return (
      <div>
        <div className="hello">
        输入椭圆的数量：
            <input type="number" value={value} onChange={handleChange} />
        </div>
        <button onClick={create}>创建</button>
      </div>
    );
  }
export default App
```

然后，在 lib/main.ts中编写代码

```
mg.showUI(__html__)

mg.ui.onmessage = (msg) => {
  const count = msg.count
  for (let i = 0; i < count; i++) {
    // mg 是全局变量，用来访问 MasterGo 提供的 API 接口
    // mg.createEllipse() 可以创建椭圆图层
    mg.createEllipse()
  }
}
```

编写完成~
现在让我们来 build 一下~

```
yarn build
```

build完成后，可以看到，出现了一个新的文件夹： dist 文件夹，文件夹下面有两个文件：main.js 和 index.html，就是我们刚刚新鲜出炉的插件代码~
此时，我们再打开 MasterGo 客户端，打开插件管理面板，可以看到，刚刚的红色提示 请配置main文件 已经消失不见啦，这就意味着，现在我们的代码可以正常运行了~

我们可以选择顶部插件菜单，或是画布右键 “插件 -> 开发者模式” ，点击我们刚刚编写完的插件 react-plugin, 运行插件：

当当当当！大功告成~

## @mastergo/plugin-typings

### TypeScript 类型支持
TypeScript 是一种可以编译到 JavaScript 的编程语言，它是 JavaScript 的超集，为 JavaScript 提供了类型支持。使用 TypeScript 的好处之一是它带来的类型提示和自动补全功能。MasterGo 的插件 API 提供了良好的 TypeScript 类型支持，因此配合 TypeScript 和 VSCode，你能得到极佳的开发体验：
为了获取到插件的类型文件，你需要安装 @mastergo/plugin-typings：

```
yarn add @mastergo/plugin-typings
```

接着配置 tsconfig.json 文件：

```
{
  "compilerOptions": {
    // ...
    "types": ["@mastergo/plugin-typings"]
  }
  // ...
}
```

### 便于开发插件的辅助函数
@mastergo/plugin-typings 除了为插件开发提供类型支持外，还提供了很多工具函数，这些工具函数可以提升你的开发效率。请查阅 Plugin Typings 文档

简介
教程