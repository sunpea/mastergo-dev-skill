# MGDSLFile
虚拟文件，每个组件或者页面是一个MGDSLFile，可能包含多个代码文件，例如

- `React`的`jsx`和`css`。
- `iOS`的`.h`和`.m`。

```
interface MGDSLFile {
  id: FileId
  name: string
  entryLayerId: LayerId
  chunks: FileId[]
  data: Record<string, Data>
  props: Record<string, Prop>
  methods: Record<string, Method>
  computed: Record<string, Computed>
  imports: ImportItem[]
}
```

- `id`: 虚拟文件id，可以在`fileMap`中找到对应的数据。
- `name`: 虚拟文件名称，影响最后生成的文件名。
- `entryLayerId`: 虚拟文件的入口组件。
- `chunks`: `chunks`包含所有引入的虚拟文件模块。
- `data`: 定义在代码文件内部的属性。
- `props`: 上层传入的属性或方法。
- `computed`: 计算属性，类似于`Vue`的`computed`和`React`的`useMemo`。
- `methods`: 文件内部方法。
- `imports`: 外部文件导入项。

## Data、Prop

```
type DSLNumber = {
  type: 'NUMBER'
  defaultValue?: number | undefined
  name: string
}

type DSLBoolean = {
  type: 'BOOLEAN'
  defaultValue?: boolean | undefined
  name: string
}

type DSLString = {
  type: 'STRING'
  defaultValue?: string | undefined
  name: string
}

type DSLFunction = {
  type: 'FUNCTION'
  defaultValue?: string | undefined
  name: string
}

type DSLArray = {
  type: 'ARRAY'
  defaultValue?: Array<any> | undefined
  name: string
}

type DSLObject = {
  type: 'OBJECT'
  defaultValue?: {[key: string]: any}
  name: string
}

type Data = DSLString | DSLNumber | DSLBoolean | DSLFunction | DSLArray | DSLObject
type Prop = DSLString | DSLNumber | DSLBoolean | DSLFunction | DSLArray | DSLObject
```

Prop和Data可以理解为从父级透传下来的数据和自身定义的实例。

- `type`: 属性类型。
- `defaultValue`: 默认值。
- `name`: 属性名称。

## Method

```
interface Method {
  name: string
  args: Array<string>
  content: string
  returnValue?: string
}
```

文件内定义的方法。

- `name`: 方法名称。
- `args`: 方法参数，为序列化字符串。
- `content`: 方法内容，`plain text`形式。
- `returnValue`: 方法返回值。

## Computed

```
interface Computed {
  name: string
  args: Array<string>
  content: string
  returnValue?: string
  dependencies?: Array<string>
}
```

计算属性。常见于Vue和React框架中。

## ImportItem

```
type ImportItem = {
  name: string
  path: string
  type: 'DEFAULT' | 'ALL'
}
```

虚拟文件头部引入项。

- `name`: 引入的模块名。
- `path`: 引入路径。
- `type`: 引入方式。 `DEFAULT`: 引入默认导出项。
- `ALL`: 引入全部，`js`中为`*`。

MGNode
Token