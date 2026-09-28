# 开发指南
在开始之前，你需要对插件的开发有一定的了解，如果还没有，请移步这里。 接下来，我们将带你从零搭建一个开发模式下的插件。我们将通过提供的接口来显示对应的代码。

## manifest.json 配置

> > **TIP**
> 如果你还对manifest不了解，请移步这里

如果你想在开发模式下运行组件，你需要添加manifest的配置如下：

```
{
  "name": "test-dsl",
  "main": "dist/main.js",
  "ui": "dist/index.html",
  "editor_type": "devMode",
  "capabilities": [
    "codegen",
  ]
}
```

其中editor_type:devMode提供在开发模式下运行的权限。 capabilities中，codegen提供codegen对象。

简介