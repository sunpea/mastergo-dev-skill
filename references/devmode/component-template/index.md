## 什么是配置模型？
配置模型是一种将已有的代码组件库和设计组件库进行关联的一种方式，他在generate阶段之前运行，根据组件的id进行关联，通过配置（如给出配置方式可以完成完成转换）和解析（如为展示型组件，如表格，列表等，无法通过配置完成映射，可以通过解析方式完成映射）的方式完成组件映射，在生成代码时，对应设计组件的数据会直接生成代码组件。

## 调试阶段

```
mg.codegen.setComponentTemplate(compTemp: MGTMP.ComponentTemplate)
```

## 接口规范

```
setComponentTemplate(compTemp: MGTMP.ComponentTemplate): void
```

开发指南