# mg.codegen

> > **TIP**
> 注意：该对象仅在研发模式下可使用

- Type:

```
interface CodegenAPI {
    /**
     * @param event a callback function that is triggered when the plugin generates the DSL, and the parameter of the callback function is the modified DSL data
     */
    on(type: 'generateDSL', event: (generateData: {data: MGDSL.MGDSLData, callback: (modifiedData: MGDSL.MGDSLData) => void}) => void) : void
    /**
     * @param event a callback function that is triggered when the plugin generates the DSL, and the parameter of the callback function is the custom code, and when the callback returns the custom code, the custom code will be used as the standard, and the code will not be generated according to the DSL
     */
    on(type: 'generate', event: (generateData: {data: MGDSL.MGDSLData, callback: (modifiedData: MGDSL.CustomCode) => void}) => void) : void
    /**
     * @param event a callback function that is triggered when the plugin generates the code, and the parameter of the callback function is the generated code
     */
    on(type: 'codeChange', event: (data: MGDSL.CustomCode['data']) => void) : void
    /**
     * Set the component template
     * @description used to set the component mapping relationship
     * @param template component template
     */
    setComponentTemplate(template: MGTMP.ComponentTemplate): void
    /**
     * Get code by id and framework
     * @param layerId layer id
     * @param type framework type
     * @returns code file
     */
    getCode(layerId: string, type: MGDSL.Framework): Promise<CodeFile | null>;
    /**
     * Get DSL by id and framework
     * @param layerId layer id
     * @param type framework type
     * @returns DSL data
     */
    getDSL(layerId: string, type: MGDSL.Framework): Promise<MGDSL.MGDSLData | null>;
    /**
     * Get code by DSL
     * @param data DSL data
     * @param type framework type
     * @returns code file
     */
    getCodeByDSL(data: MGDSL.MGDSLData, type: MGDSL.Framework): Promise<CodeFile | null>;
  }
```

该对象在研发模式中生成，用于通过图层信息生成DSL，进而生成代码。

## on
on方法允许注册特定事件的处理函数，当事件发生时会执行该回调函数：

### generateDSL

```
/**
 * @param event a callback function that is triggered when the plugin generates the DSL, and the parameter of the callback function is the modified DSL data
 */
on(type: 'generateDSL', event: (generateData: {data: MGDSL.MGDSLData, callback: (modifiedData: MGDSL.MGDSLData) => void}) => void) : void
```

该回调在生成DSL后运行，允许用户修改DSL并通过callback函数返回。如果用户这样做,则后续代码生成会根据返回的dsl为准。

### generate

```
/**
 * @param event a callback function that is triggered when the plugin generates the DSL, and the parameter of the callback function is the custom code, and when the callback returns the custom code, the custom code will be used as the standard, and the code will not be generated according to the DSL
 */
on(type: 'generate', event: (generateData: {data: MGDSL.MGDSLData, callback: (modifiedData: MGDSL.CustomCode) => void}) => void) : void
```

该回调在生成DSL后运行，允许用户根据DSL生成自定义代码并通过callback返回。如果用户这样做，则后续会显示用户生成的代码。暂停对应的DSL生成CODE的行为。

### codeChange

```
/**
  * @param event a callback function that is triggered when the plugin generates the code
  */
on(type: 'codeChange', event: (data: MGDSL.CustomCode['data']) => void) : void
```

该回调在生成代码后运行，返回给用户生成的对应代码。

## setComponentTemplate

```
/**
 * Set the component template
 * @description used to set the component mapping relationship
 * @param template component template
 */
setComponentTemplate(template: MGTMP.ComponentTemplate): void
```

设置组件模板。当存在组件模板时，图层的实例（instance）会根据模板映射方式生成对应的代码。

> > **TIP**
> 你可以设置一个button组件集的模板为:

```
{
  name: 'Button',
  props: [
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
      aliasMap: BOOLEANOPERATION,
    },
    {
      type: 'BOOLEAN',
      name: 'danger',
      aliasName: 'Danger',
      aliasMap: BOOLEANOPERATION,
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
    {
      type: 'SLOT',
      name: 'icon',
      ignoreClass: true,
      nodePath: ['Content', 'Icon \/ .*'],
    },
  ],
  slots: [
    {
      name: 'default',
      relateNodeNames: [['Content', 'Button']],
      type: 'TEXT',
    },
  ],
  source: {
    path: '',
    export: 'Button',
  },
  id: 'layerId',
},
```

在d2c面板中你可以得到:

## getCode

```
/**
 * Get code by id and framework
 * @param layerId layer id
 * @param type framework type
 * @returns code file
 */
getCode(layerId: string, type: MGDSL.Framework): Promise<CodeFile | null>;
```

根据图层id获取生成代码

## getDSL

```
/**
  * Get DSL by id and framework
  * @param layerId layer id
  * @param type framework type
  * @returns DSL data
  */
getDSL(layerId: string, type: MGDSL.Framework): Promise<MGDSL.MGDSLData | null>;
```

根据图层id获取DSL

## getCodeByDSL

```
/**
 * Get code by DSL
 * @param data DSL data
 * @param type framework type
 * @returns code file
 */
getCodeByDSL(data: MGDSL.MGDSLData, type: MGDSL.Framework): Promise<CodeFile | null>;
```

根据DSL生成代码

mastergo.notify
NodeTypes