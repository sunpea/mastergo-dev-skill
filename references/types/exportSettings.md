# ExportSettings
导出设置。

```
interface ExportSettingsImage {
    readonly format: 'JPG' | 'PNG' | 'WEBP'
    readonly isSuffix?: boolean
    readonly fileName?: string
    readonly constraint?: ExportSettingsConstraints
    readonly useAbsoluteBounds?: boolean  // defaults to false
    readonly useRenderBounds?: boolean // default to true
  }
  interface ExportSettingsSVG {
    readonly format: 'SVG'
    readonly isSuffix?: boolean
    readonly fileName?: string
  }
  
  interface ExportSettingsPDF {
    readonly format: 'PDF'
    readonly isSuffix?: string
    readonly fileName?: string
    readonly useAbsoluteBounds?: boolean // defaults to false
    readonly useRenderBounds?: boolean // default to true
  }
  
  type ExportSettings = ExportSettingsImage | ExportSettingsSVG | ExportSettingsPDF
```

- `format` ：文件格式，具体可查看类型 [ExportFileFormat](/types/exportSettings.html#exportfileformat)。
- `constraint` ：导出时的约束设置，具体可查看类型 [ExportSettingsConstraints](/types/exportSettings.html#exportsettingsconstraints)。
- `isSuffix` ：是否为后缀。
- `fileName` ：导出的文件名。
- `useAbsoluteBounds`: 是否使用节点的完整尺寸，无论它是否被裁剪或它周围的空间是空的，当图层被遮挡时，设置为 `false`只会导出可见区域内的图层, 默认为 `true`。
- `useRenderBounds`: 导出是否包含节点的特效和外部描边, 默认是`true`。当前图层为包含一个被父容器剪裁后的图片，导出的容器又被其父容器剪裁 我们试着导出填充为红色的容器:当 `useAbsoluteBounds` 为 `false` 时，导出图片所见区域数据，导出图片如下 当 `useAbsoluteBounds` 为 `true` 时，导出图片原本数据，导出图片如下
- `useRenderBounds`: 控制导出时是否包含图层的外部描边和阴影绘制所占区域，默认为 **`true`**。当前图层为有绿色外描边和向外扩散阴影的图层 当 `useRenderBounds` 为 `false` 时，不包含外描边和阴影，导出图片如下 当 `useRenderBounds` 为 `true` 时，包含外表描边和阴影，导出图片如下

## ExportSettingsConstraints
导出时文件的约束设置。

```
interface ExportSettingsConstraints {
  type: 'SCALE' | 'WIDTH' | 'HEIGHT'
  value: number
}
```

- `type` ：导出时的文件的约束类型，通过`SCALE`设置导出倍率，也可通过`WIDTH`或`HEIGHT`设定一个固定的宽度或高度值，按照比例导出。
- `value` ：导出时文件的约束值，当类型是`SCALE`时，value表示倍率，默认为 1x（100%）；当类型是`WIDTH`或`HEIGHT`时，value表示宽度或高度。

## ExportFileFormat
导出文件的格式。

```
type ExportFileFormat = 'PNG' | 'JPG' | 'SVG' | 'PDF' | 'WEBP'
```

Effect
FlowStartingPoint