# TypeScript Types
为了帮助您编写插件代码，我们为整个插件 API 提供了一个 TypeScript 类型文件。
Typings 文件是可用于类型检查的类型和接口声明的集合。
你会在一些地方看到类型和接口：

- 获取和设置节点或全局对象的属性
- 在函数中作为参数传递
- 作为方法的返回
类型和接口具有不同的复杂度.

- 从值列表中选择一个选项，例如 [BlendMode](/types/blend.html).
- 支持必需和可选属性的混合。你会看到一个“？”在任何可选属性的末尾.
- 根据您想要实现的结果提供不同的属性，例如 [ConnectorEndpoint](/types/connectorEndpoint.html).
- 支持或引用其他类型和接口，如 [Paint](/types/paint.html) 和 [Effect](/types/effect.html).

Action