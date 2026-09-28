# 简介
DSL的全称是设计系统语言(Design System Language), 在MasterGo 中是能表达设计图的代码，通过代码我们能还原出设计图，也就是 Design To Code, Code To Design, 详情请见代码。
MasterGo 中的 DSL 目前具有转 React、 Vue 和 Android 的能力。

## 开始
DSL 是在设计图转成代码的前一步生成出来的抽象层的数据，基于它我们可以转成各个平台的代码，开发者可以在转成代码之前去使用插件做一层拦截，再将修改后的数据传递给 MasterGo 做展示。

## 示例

```
//插件测
  let cb = null
  function monitor() {
    mg.ui.onmessage = (msg) => {
      // 获取修改后dsl
    }
    // 监听mg的dsl数据生成
    mg.codegen.on('generateDSL', ({ data: MGDSL.MGDSLData, callback: (modifiedData: MGDSL.MGDSLData) => void }) => {
      cb = callback
      // 发送给UI侧
      sendDSLToUI(data)
    });

  }
  // 发送给UI侧进行修改
  function sendDSLToUI(dsl: MGDSL.MGDSL.MGDSLData) {
    mg.ui.postMessage({
      type: 'dsl'
      data: dsl,
    }, '*')
  }



  //UI测
  window.onmessage = async (event) => {
    const { type, data } = event
    if (type === 'dsl') {
      const info = await request()
      const modifiedData = modifyData(data, info);
      sendDSLToPlugin(modifiedData);
    }
  }

  // 一些请求操作
  function request(): Info {
    //xxxxxx
   return Promise.resolve(xxx);
  }

  // 修改dsl的数据
  function modifyData(dsl, info) {
    let newDSL = dsl
    //xxxxx
    return newDSL
  }

  function sendDSLToPlugin(dsl: MGDSL.MGDSL.MGDSLData) {
    parent.postMessage(dsl, '*')
  }
```

> > **TIP**
> 注册了generateDSL事件的插件，需要在5s以内完成回调，超时则采用原有的数据进行渲染和展示。

MGDSL