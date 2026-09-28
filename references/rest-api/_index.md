# MasterGo OpenAPI
MasterGo OpenAPI 文档

## 说明

### 标签说明

| 标签 | 说明 |
|---|---|
| 私有化 | 标签在接口标题前，说明该接口仅私有化部署可用 标签在字段中标识，说明该字段仅私有化部署可用 |
| 已废弃 已弃用 | 接口或请求参数或响应参数已有其他替代，不推荐使用 |
| Beta | 接口或请求参数或响应参数处于 Beta 阶段，可能会有变动 |

### 排序说明
OpenAPI 中排序相关的字段，一般默认使用 -updated_at 排序，表示按更新时间降序排序。
 对于某个排序字段，如果没有前置排序符号则说明是按升序排序，否则按倒序排序。
例如 created_at 表示按创建时间升序排序，-created_at 表示按创建时间降序排序。

### 其他说明

- 当前所有的 OpenAPI 接口都可以使用 X-MG-Authentication 这个 HTTP Header 来进行鉴权； X-MG-INT-Authentication 是非必要的鉴权头，仅用于少数的私有化集成场景，非私有化场景忽略 X-MG-INT-Authentication 即可。

## 接口鉴权

### 获取 AccessToken
请求方法: POST
请求路径: /openapi/v1/organization/application/token
接口描述: 根据 app_id 和 app_secret 获取 AccessToken, 请求 /openapi/v1 开头的开放接口时，需要将调用本接口获取的 token 作为 X-MG-Authentication 头传入

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| app_id |  | string | 是 |  | 企业应用 ID； 可在企业管理后台的【应用管理】页面中获取 |
| app_secret |  | string | 是 |  | 企业应用密钥； 可在企业管理后台的【应用管理】页面中获取 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "expire": 0,
    "token": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ expire | integer | 否 |  |
| └─ token | string | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

状态码 400: code - Bad Request

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 登录注册

### 私有化 注册用户
请求方法: POST
请求路径: /openapi/v1/signup
接口描述: 注册用户仅支持私有化环境使用，且仅支持通过邮箱注册，调用接口后会在后台登录并返回登录信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| email |  | string | 是 |  | 邮箱 |
| sourceId |  | string | 否 |  | 三方(客户)系统唯一的用户 ID |
| username |  | string | 否 |  | 用户名 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "createdAt": "string",
    "email": "string",
    "id": 0,
    "job": "string",
    "name": "string",
    "phoneNumber": "string",
    "session_id": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ email | string | 否 | 邮箱 |
| └─ id | integer | 否 | 用户 ID |
| └─ job | string | 否 | 职位 |
| └─ name | string | 否 | 用户名 |
| └─ phoneNumber | string | 否 | 手机号 |
| └─ session_id | string | 否 | 会话 ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 用户

### 获取企业成员列表
请求方法: GET
请求路径: /openapi/v1/organization/users
接口描述: 分页获取企业成员信息列表，不包含企业访客

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| pageNum |  | Query | integer | 是 |  | 当前页数，从1开始 |
| pageSize |  | Query | integer | 是 |  | 每页大小，最大为 500 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "avatar": "string",
      "email": "string",
      "id": 0,
      "name": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ avatar | string | 否 | 头像 |
| └─ email | string | 否 | 邮箱 |
| └─ id | integer | 否 | 用户ID |
| └─ name | string | 否 | 用户名 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队成员
请求方法: GET
请求路径: /openapi/v1/team/:teamId/users
接口描述: 获取指定团队下的所有成员信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "avatar": "string",
      "email": "string",
      "id": 0,
      "name": "string",
      "sourceId": "string",
      "teamRole": {
        "documentPermission": "string",
        "role": "string"
      }
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ avatar | string | 否 | 头像 |
| └─ email | string | 否 | 邮箱 |
| └─ id | integer | 否 | 用户ID |
| └─ name | string | 否 | 用户名 |
| └─ sourceId | string | 否 | 所有者三方 ID（仅私有化集成返回） |
| └─ teamRole | object | 否 | 团队角色 |
| └─ documentPermission | string | 否 | 团队编辑权限 |
| └─ role | string | 否 | 团队角色 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 查询用户 ID
请求方法: GET
请求路径: /openapi/v1/user
接口描述: 根据 userCode 或 identity 信息查询用户ID

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userCode | 已弃用私有化 | Query | string | 否 |  | *三方(客户)系统唯一的用户 ID，推荐使用 identityType 和 identityId 进行查询* |
| identityType |  | Query | string | 否 |  | 用户身份类型；email：identityId 为邮箱userId：identityId 为用户 IDsourceId：identityId 为三方(客户)系统唯一的用户 ID（仅私有化） |
| identityId |  | Query | string | 否 |  | 用户身份ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "isDeleted": true,
    "userId": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ isDeleted | boolean | 否 | 是否已被删除 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户信息
请求方法: GET
请求路径: /openapi/v1/users/:userId
接口描述: 获取指定用户的信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "avatar": "string",
    "email": "string",
    "id": 0,
    "name": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ avatar | string | 否 | 头像 |
| └─ email | string | 否 | 邮箱 |
| └─ id | integer | 否 | 用户ID |
| └─ name | string | 否 | 用户名 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取文件成员权限
请求方法: POST
请求路径: /openapi/v1/document/members/permissions
接口描述: 获取文件成员权限

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userIds |  | array<integer> | 是 |  | 用户ID列表 |
| documentId |  | integer | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "permissions": [
      {
        "docPerm": "string",
        "role": "string",
        "userId": 0
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ permissions | array<object> | 否 |  |
| └─ docPerm | string | 否 | 权限 |
| └─ role | string | 否 | 角色 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 根据三方系统信息获取用户信息
请求方法: POST
请求路径: /openapi/v1/oauth/users
接口描述: 根据三方系统信息批量获取用户信息，仅对私有化开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| sourceType |  | string | 是 |  | 三方系统类型，目前仅支持 `integration` |
| sourceIds |  | array<string> | 是 |  | 三方系统用户ID列表 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "sourceId": {
      "userId": 0
    }
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ sourceId | object | 否 | 三方系统用户ID，**这里的返回结构实际上是一个 map 结构**  **如 `{"sourceId1": {"userId": userId1}, "sourceId2": {"userId": userId2}}`** |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 搜索企业成员信息
请求方法: POST
请求路径: /openapi/v1/organization/users
接口描述: 搜索企业用户，目前仅对私有化部署开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| keyword |  | string | 否 |  | 关键词，用于搜索用户名或邮箱 |
| userIds |  | array<integer> | 否 |  | 用户ID列表 |
| pageNum |  | integer | 是 |  | 当前页数，从1开始 |
| pageSize |  | integer | 是 |  | 每页大小 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "avatar": "string",
      "email": "string",
      "id": 0,
      "name": "string",
      "nickname": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ avatar | string | 否 | 头像 |
| └─ email | string | 否 | 邮箱 |
| └─ id | integer | 否 | 用户ID |
| └─ name | string | 否 | 用户名 |
| └─ nickname | string | 否 | 昵称/企业成员名称 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取项目成员权限
请求方法: POST
请求路径: /openapi/v1/project/members/permissions
接口描述: 获取项目成员权限

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userIds |  | array<integer> | 是 |  | 用户ID列表 |
| projectId |  | integer | 是 |  | 项目ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "permissions": [
      {
        "docPerm": "string",
        "role": "string",
        "userId": 0
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ permissions | array<object> | 否 |  |
| └─ docPerm | string | 否 | 权限 |
| └─ role | string | 否 | 角色 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取团队成员权限
请求方法: POST
请求路径: /openapi/v1/team/members/permissions
接口描述: 获取团队成员权限

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userIds |  | array<integer> | 是 |  | 用户ID列表 |
| teamId |  | integer | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "permissions": [
      {
        "docPerm": "string",
        "role": "string",
        "userId": 0
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ permissions | array<object> | 否 |  |
| └─ docPerm | string | 否 | 权限 |
| └─ role | string | 否 | 角色 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 更新用户基础信息
请求方法: PUT
请求路径: /openapi/v1/user
接口描述: 更新用户基础信息，仅对私有化开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| identityType |  | string | 是 |  | 用户身份类型；email：identityId 为邮箱userId：identityId 为用户 IDsourceId：identityId 为三方(客户)系统唯一的用户 ID（仅私有化） |
| identityId |  | string | 是 |  | 用户身份ID |
| username |  | string | 否 |  | 更新的用户名 |
| email |  | string | 否 |  | 更新的邮箱 |
| orgStructure |  | string | 否 |  | 更新的组织结构 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "email": "string",
    "userId": 0,
    "username": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ email | string | 否 | 更新后的邮箱 |
| └─ userId | integer | 否 | 用户ID |
| └─ username | string | 否 | 更新后的用户名 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 删除用户
请求方法: DELETE
请求路径: /openapi/v1/user
接口描述: 删除用户，仅对私有化开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| identityType |  | string | 是 |  | 用户身份类型；email：identityId 为邮箱userId：identityId 为用户 IDsourceId：identityId 为三方(客户)系统唯一的用户 ID（仅私有化） |
| identityId |  | string | 是 |  | 用户身份ID |
| forceDelete |  | boolean | 否 |  | 是否强制删除; 为 true 的情况下，删除的用户可再次注册 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "userId": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取用户访问令牌
请求方法: GET
请求路径: /openapi/v1/user/access-token
接口描述: 获取指定用户的访问令牌

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Query | integer | 是 |  | 用户ID |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": {
    "accessTokens": [
      {
        "accessToken": "string",
        "name": "string",
        "userId": 0
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ accessTokens | array<object> | 否 |  |
| └─ accessToken | string | 否 | 访问令牌 |
| └─ name | string | 否 | 令牌名称 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 创建用户访问令牌
请求方法: POST
请求路径: /openapi/v1/user/access-token
接口描述: 为指定用户创建访问令牌

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userId |  | integer | 是 |  | 用户ID |
| name |  | string | 否 |  | 可选，默认为 “令牌1” |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": {
    "accessToken": "string",
    "name": "string",
    "userId": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ accessToken | string | 否 | 访问令牌 |
| └─ name | string | 否 | 令牌名称 |
| └─ userId | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 删除用户访问令牌
请求方法: DELETE
请求路径: /openapi/v1/user/access-token
接口描述: 删除指定用户的访问令牌

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userId |  | integer | 是 |  | 用户ID |
| accessToken |  | string | 是 |  | 访问令牌 |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 企业

### 查询资产交接任务状态
请求方法: GET
请求路径: /openapi/v1/assets-transfer-result

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Query | integer | 是 |  | 用户ID，被移除的企业成员 ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "operator": 0,
    "status": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ operator | integer | 否 | 资产交接操作人ID |
| └─ status | integer | 否 | 任务状态，0: 已提交，1: 进行中，2: 失败，3: 已完成 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取企业信息
请求方法: GET
请求路径: /openapi/v1/organization

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "OrganizationSSOType": 0,
    "abbr": "string",
    "allowPublicDocs": true,
    "allowPublicEmail": true,
    "createAt": "string",
    "creatorId": 0,
    "description": "string",
    "id": 0,
    "isPublic": true,
    "logo": "string",
    "name": "string",
    "openForbidAnonymousAccess": 0,
    "openOrgStructure": true,
    "openOrganizationEmail": 0,
    "openOrganizationSSO": 0,
    "openOrganizationSpace": 0,
    "openSharingTimeLimit": 0,
    "orgStructureName": "string",
    "organFBindOrgEmailizationSaml": 0,
    "organizationEmail": "string",
    "organizationLogin": 0,
    "ownerId": 0,
    "teamJoinApproval": true,
    "updateAt": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ OrganizationSSOType | integer | 否 | SSO类型 |
| └─ abbr | string | 否 | 企业简称 |
| └─ allowPublicDocs | boolean | 否 | 是否允许文档公开访问 |
| └─ allowPublicEmail | boolean | 否 | 是否允许非企业邮箱注册 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID，最初创建者记录 |
| └─ description | string | 否 | 企业描述 |
| └─ id | integer | 否 | ID |
| └─ isPublic | boolean | 否 | 公开邀请链接 |
| └─ logo | string | 否 | 企业logo |
| └─ name | string | 否 | 企业名称 |
| └─ openForbidAnonymousAccess | integer | 否 | 打开禁止匿名访问 |
| └─ openOrgStructure | boolean | 否 | 是否打开企业组织架构 |
| └─ openOrganizationEmail | integer | 否 | 是否打开企业邮箱 |
| └─ openOrganizationSSO | integer | 否 | 是否打开SSO |
| └─ openOrganizationSpace | integer | 否 | 打开企业空间, 默认1 |
| └─ openSharingTimeLimit | integer | 否 | 打开文件分享时间限制 |
| └─ orgStructureName | string | 否 | 企业组织架构名称 |
| └─ organFBindOrgEmailizationSaml | integer | 否 | 是否开启 SAML |
| └─ organizationEmail | string | 否 | 企业邮箱域 |
| └─ organizationLogin | integer | 否 | 企业登录方式 |
| └─ ownerId | integer | 否 | 拥有者ID，是具有企业最高权限，能转让 |
| └─ teamJoinApproval | boolean | 否 | 团队邀请是否需要管理员审批 |
| └─ updateAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取企业操作日志列表
请求方法: POST
请求路径: /openapi/v1/organization/operation-log/list

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| start_time |  | integer | 是 |  | 开始时间时间戳(秒) |
| end_time |  | integer | 是 |  | 结束时间时间戳(秒) |
| page_no |  | integer | 是 |  | 页码 |
| page_size |  | integer | 是 |  | 每页记录数 |
| keyword |  | string | 是 |  | 搜索关键字，支持所有用户名和邮箱 |
| teamids |  | array<integer> | 是 |  | 团队ID列表 |
| actions |  | array<string> | 是 |  | 操作类型列表 |
| operator |  | integer | 是 |  | 操作人ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "latestSignIn": "string",
    "operationLogs": [
      {
        "action": "string",
        "actionGroup": "string",
        "actionGroupJoinAction": "string",
        "actionGroupName": "string",
        "actionName": "string",
        "createdAt": "string",
        "description": "string",
        "id": 0,
        "operatorAvatar": "string",
        "operatorEmail": "string",
        "operatorID": 0,
        "operatorIP": "string",
        "operatorName": "string",
        "operatorObject": [0],
        "operatorObjectTeamID": 0,
        "operatorObjectTeamName": "string",
        "operatorType": 0,
        "organizationID": 0
      }
    ],
    "total": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ latestSignIn | string | 否 | 最新登录时间 |
| └─ operationLogs | array<object> | 否 | 操作日志列表 |
| └─ action | string | 否 | 操作类型 |
| └─ actionGroup | string | 否 | 操作组 |
| └─ actionGroupJoinAction | string | 否 | 操作组关联操作 |
| └─ actionGroupName | string | 否 | 操作组名称 |
| └─ actionName | string | 否 | 操作名称 |
| └─ createdAt | string | 否 | 操作时间 |
| └─ description | string | 否 | 操作描述 |
| └─ id | integer | 否 | 操作日志ID |
| └─ operatorAvatar | string | 否 | 操作人头像 |
| └─ operatorEmail | string | 否 | 操作人邮箱 |
| └─ operatorID | integer | 否 | 操作人ID |
| └─ operatorIP | string | 否 | 操作人IP |
| └─ operatorName | string | 否 | 操作人名称 |
| └─ operatorObject | array<integer> | 否 | 操作对象 |
| └─ operatorObjectTeamID | integer | 否 | 操作对象团队ID |
| └─ operatorObjectTeamName | string | 否 | 操作对象团队名称 |
| └─ operatorType | integer | 否 | 操作人类型 |
| └─ organizationID | integer | 否 | 企业ID |
| └─ total | integer | 否 | 总记录数 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 更新企业成员状态
请求方法: PUT
请求路径: /openapi/v1/organization/users/status

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| status |  | string | 是 |  | 状态，enable: 启用，disable: 禁用 |
| userIds |  | array<integer> | 是 |  | 被操作用户ID列表 |
| operatorId |  | integer | 是 |  | 操作人ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 企业成员资产交接
请求方法: DELETE
请求路径: /openapi/v1/orginzation/users
接口描述: 移除企业成员时进行的资产交接操作

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userId |  | integer | 是 |  | 被移除人ID |
| operator |  | integer | 是 |  | 操作人ID |
| receiverId |  | integer | 否 |  | 接收人ID，默认转交给操作人，可以指定企业管理员作为交接人，不可指定为企业成员或访客 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "result": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ result | string | 否 | 交接任务结果，成功时返回 "commit success" |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 设置企业自启动插件
请求方法: PUT
请求路径: /openapi/v1/plugin/org/settings
接口描述: 配置企业自启动插件

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体
参数名: pluginSettings - 插件自启动配置，canvas 和devMode 至少有一个

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| canvas | object | 否 | 设计模式插件自启动配置 |
| └─ plugin | string | 否 | 插件id |
| └─ pluginApply | integer | 是 | 应用范围 1代表企业维度 |
| └─ pluginAuto | boolean | 否 | 自启动开关 true代表开 false代表关 |
| └─ pluginEnableClose | integer | 是 | 强制启动，1代表是，2代表否 |
| devMode | object | 否 | 研发模式插件自启动配置 |
| └─ plugin | string | 否 | 插件id |
| └─ pluginApply | integer | 是 | 应用范围 1代表企业维度 |
| └─ pluginAuto | boolean | 否 | 自启动开关 true代表开 false代表关 |
| └─ pluginEnableClose | integer | 是 | 强制启动，1代表是，2代表否 |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 分配席位
请求方法: PUT
请求路径: /openapi/v1/seat/change/batch

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体
参数名: userList - 详细划分用户分配的席位，批量给不同的用户分配不同的席位；可以搭配 userIds 和 seatType 进行使用，不互相干扰
类型: 数组＜object＞

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| seatType | string | 否 | 请参考非数组中的 `seatType` 参数说明 |
| userId | integer | 否 | 用户ID |

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| operator |  | integer | 是 |  | 操作人ID |
| userIds |  | array<integer> | 是 |  | 分配席位用户 ID 列表 |
| seatType |  | string | 是 |  | 分配席位类型，搭配 userIds 进行使用； 给 userIds 中的用户分配对应类型的席位 支持的席位类型有：edit - 设计席位viewAudit - 查看席位(审批)viewAuto - 查看席位(自由)dev - 研发席位prototype - 产品席位 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取企业成员详情信息
请求方法: POST
请求路径: /openapi/v1/team-users

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| no_team |  | boolean | 否 |  | 不查询团队信息 |
| team_id |  | integer | 否 |  | 团队ID |
| page_no |  | integer | 否 |  | 页码，从1开始 |
| page_size |  | integer | 否 |  | 每页数量 |
| keyword |  | string | 否 |  | 关键字搜索，支持用户名、邮箱和企业组织架构搜索 |
| user_status |  | array<integer> | 否 |  | 用户状态，0: 正常，1: 禁用 |
| roles |  | array<string> | 否 |  | 角色，owner: 企业创建者，admin: 企业管理员，member: 企业成员，guest: 企业访客 |
| jobs |  | array<string> | 否 |  | 职位，支持多个职位搜索：manager - 管理者producter - 产品经理ui - UI 设计师graphic - 平面设计师ux - 交互设计师developer - 研发工程师qa - 测试工程师operator - 运营freelancer - 自由职业者student - 学生other - 其他 |
| seats |  | array<string> | 否 |  | 席位，支持多个席位搜索，多个席位用逗号分隔 |
| sort |  | string | 否 |  | 排序，支持字段为：name - 用户名job - 职位role - 角色seat - 席位timeActivity - 最后活跃时间joinTime - 加入时间 |
| with_last_edit_time | 私有化 | boolean | 否 |  | 是否返回最后编辑时间 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "total": 0,
    "users_info": [
      {
        "avatar": "string",
        "email": "string",
        "job": "string",
        "name": "string",
        "nickname": "string",
        "orgStructure": "string",
        "role": "string",
        "seat_permission_type": "string",
        "status": 0,
        "teams": [
          {
            "id": 0,
            "name": "string",
            "team_role": "string",
            "user_id": 0
          }
        ],
        "time_activity": "string",
        "time_edit": "string",
        "time_joined_org": "string",
        "uid": 0
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ total | integer | 否 | 总记录数 |
| └─ users_info | array<object> | 否 | 企业成员详情信息列表 |
| └─ avatar | string | 否 | 头像 |
| └─ email | string | 否 | 邮箱 |
| └─ job | string | 否 | 职位 |
| └─ name | string | 否 | 用户名 |
| └─ nickname | string | 否 | 昵称/企业成员名称 |
| └─ orgStructure | string | 否 | 企业组织架构 |
| └─ role | string | 否 | 角色 |
| └─ seat_permission_type | string | 否 | 席位权限类型 |
| └─ status | integer | 否 | 用户状态，0: 正常，1: 禁用 |
| └─ teams | array<object> | 否 | 团队信息列表 |
| └─ id | integer | 否 | 团队id |
| └─ name | string | 否 | 团队名 |
| └─ team_role | string | 否 |  |
| └─ user_id | integer | 否 |  |
| └─ time_activity | string | 否 | 最后活跃时间 |
| └─ time_edit | string | 否 | 最后编辑时间 |
| └─ time_joined_org | string | 否 | 加入时间 |
| └─ uid | integer | 否 | 用户ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 团队

### 获取企业团队列表
请求方法: GET
请求路径: /openapi/v1/organization/teams
接口描述: 获取企业团队列表，可以指定是否包含项目列表

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| withProjects |  | Query | boolean | 否 |  | 是否包含项目列表 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createAt": "string",
      "description": "string",
      "ext": 0,
      "id": 0,
      "logo": "string",
      "name": "string",
      "ownerId": 0,
      "projects": [
        {
          "createAt": "string",
          "id": 0,
          "isPersonal": true,
          "isPublic": 0,
          "name": "string",
          "shareCode": "string",
          "teamId": 0,
          "updateAt": "string",
          "visitControl": 0
        }
      ],
      "updateAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ description | string | 否 | 团队描述 |
| └─ ext | integer | 否 | 团队扩展字段 从右至左: 第1位: 为1则是否是公开团队 默认0:不是公开团队 第2位: 为1则是初始化的我的团队 第4位: 为1则是隐藏团队状态 1 隐藏 0 不隐藏 |
| └─ id | integer | 否 | ID |
| └─ logo | string | 否 | 团队Logo |
| └─ name | string | 否 | 团队名称 |
| └─ ownerId | integer | 否 | 团队所有者ID |
| └─ projects | array<object> | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ isPersonal | boolean | 否 | 是否草稿箱 |
| └─ isPublic | integer | 否 | 是否公开 |
| └─ name | string | 否 | 项目名 |
| └─ shareCode | string | 否 | 分享码 |
| └─ teamId | integer | 否 | 团队 ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ visitControl | integer | 否 | 项目访问范围 |
| └─ updateAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 设置团队自启动插件
请求方法: PUT
请求路径: /openapi/v1/plugin/team/settings
接口描述: 配置团队自启动插件

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| teamId |  | integer | 是 |  | 团队id |
| pluginSettings |  | object | 否 |  | 插件自启动配置 |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 转移团队所有者
请求方法: PUT
请求路径: /openapi/v1/teams/:teamId/owner
接口描述: 转移指定团队所有者到新所有者，两个用户必须都在团队中

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| oldOwnerId |  | integer | 是 |  | 旧所有者ID |
| newOwnerId |  | integer | 是 |  | 新所有者ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 创建团队
请求方法: POST
请求路径: /openapi/v1/users/:userId/team
接口描述: 给指定用户创建团队

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| name |  | string | 是 |  | 团队名称 |
| description |  | string | 否 |  | 团队描述 |
| siteLink |  | string | 否 |  | 团队网站链接 |
| isHidden |  | boolean | 否 |  | 是否隐藏团队 |
| sourceId | 私有化 | string | 否 |  | 集成团队来源ID |
| sourceType | 私有化 | string | 否 |  | 集成团队来源类型 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "createAt": "string",
    "description": "string",
    "ext": 0,
    "id": 0,
    "logo": "string",
    "name": "string",
    "organizationId": 0,
    "ownerId": 0,
    "sourceId": "string",
    "sourceType": "string",
    "updateAt": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ description | string | 否 | 团队描述 |
| └─ ext | integer | 否 | 团队扩展字段 从右至左: 第1位: 为1则是否是公开团队 默认0:不是公开团队 第2位: 为1则是初始化的我的团队 第4位: 为1则是隐藏团队状态 1 隐藏 0 不隐藏 |
| └─ id | integer | 否 | ID |
| └─ logo | string | 否 | 团队Logo |
| └─ name | string | 否 | 团队名称 |
| └─ organizationId | integer | 否 |  |
| └─ ownerId | integer | 否 | 团队所有者ID |
| └─ sourceId | string | 否 |  |
| └─ sourceType | string | 否 |  |
| └─ updateAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 更新团队
请求方法: PUT
请求路径: /openapi/v1/users/:userId/team/:teamId
接口描述: 更新指定团队信息，需要指定更新用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| name |  | string | 否 |  | 团队名称 |
| description |  | string | 否 |  | 团队描述 |
| siteLink |  | string | 否 |  | 团队网站链接 |
| logo |  | string | 否 |  | 团队logo |
| isHidden |  | boolean | 否 |  | 是否隐藏团队 |
| setIntegration | 私有化 | boolean | 否 |  | 是否设置为集成团队 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 删除团队
请求方法: DELETE
请求路径: /openapi/v1/users/:userId/team/:teamId
接口描述: 删除指定团队，需要指定删除用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户的团队列表
请求方法: GET
请求路径: /openapi/v1/users/:userId/teams
接口描述: 获取指定用户的团队列表，包含【草稿箱团队】

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createAt": "string",
      "description": "string",
      "ext": 0,
      "id": 0,
      "logo": "string",
      "name": "string",
      "ownerId": 0,
      "updateAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ description | string | 否 | 团队描述 |
| └─ ext | integer | 否 | 团队扩展字段 从右至左: 第1位: 为1则是否是公开团队 默认0:不是公开团队 第2位: 为1则是初始化的我的团队 第4位: 为1则是隐藏团队状态 1 隐藏 0 不隐藏 |
| └─ id | integer | 否 | ID |
| └─ logo | string | 否 | 团队Logo |
| └─ name | string | 否 | 团队名称 |
| └─ ownerId | integer | 否 | 团队所有者ID |
| └─ updateAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 项目

### 移动项目
请求方法: PUT
请求路径: /openapi/v1/project/project-move/:userId
接口描述: 在团队间移动项目

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| projectId |  | integer | 是 |  | 项目ID |
| destTeamId |  | integer | 是 |  | 目标团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 批量获取项目信息
请求方法: POST
请求路径: /openapi/v1/projects

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体
参数名: ids - 项目ID列表
类型: 数组＜integer＞

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createAt": "string",
      "id": 0,
      "isPersonal": true,
      "isPublic": 0,
      "name": "string",
      "shareCode": "string",
      "teamId": 0,
      "updateAt": "string",
      "visitControl": 0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ isPersonal | boolean | 否 | 是否草稿箱 |
| └─ isPublic | integer | 否 | 是否公开 |
| └─ name | string | 否 | 项目名 |
| └─ shareCode | string | 否 | 分享码 |
| └─ teamId | integer | 否 | 团队 ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ visitControl | integer | 否 | 项目访问范围 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下所有项目
请求方法: GET
请求路径: /openapi/v1/team/:teamId/projects
接口描述: 获取指定团队下的所有项目，仅包含基础信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Query | integer | 否 |  | 用户ID |
| page[number] |  | Query | integer | 否 |  | 页码 |
| page[size] |  | Query | integer | 否 |  | 页宽，最大支持5000 |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createAt": "string",
      "id": 0,
      "isPersonal": true,
      "isPublic": 0,
      "name": "string",
      "shareCode": "string",
      "teamId": 0,
      "updateAt": "string",
      "visitControl": 0
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ isPersonal | boolean | 否 | 是否草稿箱 |
| └─ isPublic | integer | 否 | 是否公开 |
| └─ name | string | 否 | 项目名 |
| └─ shareCode | string | 否 | 分享码 |
| └─ teamId | integer | 否 | 团队 ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ visitControl | integer | 否 | 项目访问范围 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 创建项目
请求方法: POST
请求路径: /openapi/v1/users/:userId/project

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| teamId |  | integer | 是 |  | 团队ID |
| name |  | string | 是 |  | 项目名称 |
| visitControl |  | number | 否 | 1 | 项目的访问范围；1：当前团队成员可访问3：仅受邀协作者可访问 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "createAt": "string",
    "id": 0,
    "isPersonal": true,
    "isPublic": 0,
    "name": "string",
    "shareCode": "string",
    "teamId": 0,
    "updateAt": "string",
    "visitControl": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ isPersonal | boolean | 否 | 是否草稿箱 |
| └─ isPublic | integer | 否 | 是否公开 |
| └─ name | string | 否 | 项目名 |
| └─ shareCode | string | 否 | 分享码 |
| └─ teamId | integer | 否 | 团队 ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ visitControl | integer | 否 | 项目访问范围 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 更新项目信息
请求方法: PUT
请求路径: /openapi/v1/users/:userId/project/:projectId
接口描述: 更新项目基础息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| projectId |  | Path | string | 是 |  | 项目ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| name |  | string | 否 |  | 项目名称 |
| visitControl |  | integer | 否 |  | 项目的访问范围；项目的访问权限；1：当前团队成员可访问3：仅受邀协作者可访问 |
| isPublic |  | boolean | 否 |  | 是否公开 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "createAt": "string",
    "id": 0,
    "isPersonal": true,
    "isPublic": 0,
    "name": "string",
    "shareCode": "string",
    "teamId": 0,
    "updateAt": "string",
    "visitControl": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ isPersonal | boolean | 否 | 是否草稿箱 |
| └─ isPublic | integer | 否 | 是否公开 |
| └─ name | string | 否 | 项目名 |
| └─ shareCode | string | 否 | 分享码 |
| └─ teamId | integer | 否 | 团队 ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ visitControl | integer | 否 | 项目访问范围 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 删除项目
请求方法: DELETE
请求路径: /openapi/v1/users/:userId/project/:projectId

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| projectId |  | Path | string | 是 |  | 项目ID |

#### 请求体
参数名: teamId - 团队ID
类型: integer

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户在团队下的项目列表
请求方法: GET
请求路径: /openapi/v1/users/:userId/projects
接口描述: 获取用户在团队下的项目列表，仅包含基础信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Query | string | 是 |  | 团队ID |
| userId |  | Path | string | 是 |  | 用户ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createdAt": "string",
      "id": 0,
      "name": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | 项目ID |
| └─ name | string | 否 | 项目名称 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户所有可访问的项目
请求方法: POST
请求路径: /openapi/v1/users/:userId/projects/accessible
接口描述: 分页获取用户所有可访问的项目列表，仅包含基础信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| keyword |  | string | 否 |  | 关键词，用于搜索项目名 |
| sort |  | string | 否 | -updated_at | 排序字段； 支持 name, created_at, updated_at; 默认 -updated_at |
| number |  | integer | 否 | 1 | 当前页数，从1开始 |
| size |  | integer | 否 | 20 | 每页大小 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createdAt": "string",
      "id": 0,
      "isPersonal": true,
      "name": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | 项目ID |
| └─ isPersonal | boolean | 否 | 是否为草稿箱 |
| └─ name | string | 否 | 项目名称 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 文件

### 移动文档所属项目
请求方法: PUT
请求路径: /openapi/v1/document/:userId/document-move

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| documentId |  | integer | 是 |  | 文件ID |
| destProjectId |  | integer | 是 |  | 目标项目ID，需要填写当前文件所属团队下的项目 ID，否则移动失败 |
| withGroup |  | boolean | 否 |  | 是否保留分组信息 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "documentId": 0,
    "projectId": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ documentId | integer | 否 | 文件ID |
| └─ projectId | integer | 否 | 移动后的项目ID |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 创建文件副本
请求方法: POST
请求路径: /openapi/v1/document/copy
接口描述: 创建文件副本，创建出的副本文件所有者为原文件所有者

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| documentId |  | integer | 是 |  | 文件ID |
| versionId |  | integer | 否 |  | 版本号 |
| projectId |  | integer | 否 |  | 项目ID，指定副本创建到的项目 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "allowCopy": true,
    "allowCopyRole": "string",
    "cover": "string",
    "coverBgColor": "string",
    "createAt": "string",
    "creatorId": 0,
    "fileMode": 0,
    "id": 0,
    "name": "string",
    "ownerId": 0,
    "projectId": 0,
    "teamId": 0,
    "updateAt": "string",
    "updateUserId": 0,
    "visitControl": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ allowCopy | boolean | 否 | 是否允许复制 |
| └─ allowCopyRole | string | 否 | 允许复制角色 |
| └─ cover | string | 否 | 文档封面 |
| └─ coverBgColor | string | 否 | 文档封面背景颜色 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文档模式 0：设计文件 1：原型文件 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 文档名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ projectId | integer | 否 | 项目ID |
| └─ teamId | integer | 否 | 团队ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ updateUserId | integer | 否 | 更新者ID |
| └─ visitControl | integer | 否 | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 批量获取文件信息
请求方法: POST
请求路径: /openapi/v1/documents

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体
参数名: ids - 文件ID列表
类型: 数组＜integer＞

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "allowCopy": true,
      "allowCopyRole": "string",
      "cover": "string",
      "coverBgColor": "string",
      "createAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "name": "string",
      "ownerId": 0,
      "projectId": 0,
      "teamId": 0,
      "updateAt": "string",
      "updateUserId": 0,
      "visitControl": 0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ allowCopy | boolean | 否 | 是否允许复制 |
| └─ allowCopyRole | string | 否 | 允许复制角色 |
| └─ cover | string | 否 | 文档封面 |
| └─ coverBgColor | string | 否 | 文档封面背景颜色 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文档模式 0：设计文件 1：原型文件 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 文档名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ projectId | integer | 否 | 项目ID |
| └─ teamId | integer | 否 | 团队ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ updateUserId | integer | 否 | 更新者ID |
| └─ visitControl | integer | 否 | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户最近访问文档
请求方法: POST
请求路径: /openapi/v1/documents/recent
接口描述: 获取指定用户最近访问的文档列表，支持分页

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userId |  | integer | 是 |  | 用户ID |
| fileMode |  | array<integer> | 是 |  | 文件类型: 0 - 设计文件, 1 - 原型文件 |
| filePathWithDomain |  | boolean | 否 |  | 文件路径是否包含域名地址 |
| limit |  | integer | 否 |  | 返回文档最大数量, 默认50, 最大200 |
| sort |  | string | 否 |  | 排序字段, 默认按打开时间降序排列, 支持: updated_at, created_at, open_at, name |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "allowCopy": true,
      "allowCopyRole": "string",
      "cover": "string",
      "coverBgColor": "string",
      "createAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "filePath": "string",
      "id": 0,
      "name": "string",
      "openAt": "string",
      "ownerId": 0,
      "permissions": {
        "edit": true,
        "read": true
      },
      "projectId": 0,
      "projectName": "string",
      "teamId": 0,
      "teamName": "string",
      "updateAt": "string",
      "updateUserId": 0,
      "visitControl": 0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ allowCopy | boolean | 否 | 是否允许复制 |
| └─ allowCopyRole | string | 否 | 允许复制角色 |
| └─ cover | string | 否 | 文档封面 |
| └─ coverBgColor | string | 否 | 文档封面背景颜色 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文档模式 0：设计文件 1：原型文件 |
| └─ filePath | string | 否 | 文件路径 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 文档名称 |
| └─ openAt | string | 否 | 最近访问时间 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ permissions | object | 否 | 文档权限, 包含查看和编辑权限 |
| └─ edit | boolean | 否 |  |
| └─ read | boolean | 否 |  |
| └─ projectId | integer | 否 | 项目ID |
| └─ projectName | string | 否 | 项目名 |
| └─ teamId | integer | 否 | 团队ID |
| └─ teamName | string | 否 | 团队名 |
| └─ updateAt | string | 否 | 更新时间 |
| └─ updateUserId | integer | 否 | 更新者ID |
| └─ visitControl | integer | 否 | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 筛选项目下文件
请求方法: GET
请求路径: /openapi/v1/project/:projectId/documents
接口描述: 分页获取指定项目下的文件，支持搜索、排序、分页

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| keyword |  | Query | string | 否 |  | 搜索关键词 |
| sort |  | Query | string | 否 | -updated_at | 排序字段 支持 name, created_at, updated_at |
| page[number] |  | Query | integer | 是 |  | 当前页数，从1开始 |
| page[size] |  | Query | integer | 是 |  | 每页大小 |
| projectId |  | Path | string | 是 |  | 项目ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "coverBgColor": "string",
      "createdAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "name": "string",
      "ownerId": 0,
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 文件封面 |
| └─ coverBgColor | string | 否 | 文件封面背景颜色 |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取项目下已发布为团队库的文件
请求方法: GET
请求路径: /openapi/v1/project/:projectId/lib/documents
接口描述: 获取指定项目下已发布为团队库的文件信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| projectId |  | Path | string | 是 |  | 项目ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createdAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "libraryId": "string",
      "name": "string",
      "ownerId": 0,
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ libraryId | string | 否 | 团队库ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### [不推荐] 根据文件名搜索文件
请求方法: GET
请求路径: /openapi/v1/searchDocs
接口描述: 根据文档名模糊搜索文档,可以指定搜索范围为团队、项目、所有者, 不推荐使用该接口, 请使用对应的POST接口继续搜索

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| key |  | Query | string | 是 |  | 关键词 |
| teamId |  | Query | string | 否 |  | 文件所属团队ID |
| projectId |  | Query | string | 否 |  | 文件所属项目ID |
| userId |  | Query | string | 否 |  | 文件所属用户ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "id": 0,
      "name": "string",
      "owner_Id": 0,
      "updated_at": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 文件封面 |
| └─ id | integer | 否 | 文件ID |
| └─ name | string | 否 | 文件名称 |
| └─ owner_Id | integer | 否 | 文件所有者ID |
| └─ updated_at | string | 否 | 文件更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 搜索用户企业内文档
请求方法: POST
请求路径: /openapi/v1/searchDocs
接口描述: 根据关键词搜索用户的企业内文档，支持分页

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| userId |  | integer | 是 |  | 用户ID |
| keyword |  | string | 是 |  | 搜索关键词 |
| entityType |  | string | 否 |  | 搜索范围类型: team, project, 分别指团队、项目, 为空时默认搜索企业下所有相关文档 |
| entityIds |  | array<integer> | 否 |  | 搜索范围ID列表 |
| fileMode |  | array<integer> | 否 |  | 文件类型: 0 - 设计文件, 1 - 原型文件 |
| filePathWithDomain |  | boolean | 否 |  | 文件路径是否包含域名地址 |
| number |  | integer | 否 |  | 分页数量, 默认1 |
| size |  | integer | 否 |  | 分页大小, 默认20 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "allowCopy": true,
      "allowCopyRole": "string",
      "cover": "string",
      "coverBgColor": "string",
      "createAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "filePath": "string",
      "id": 0,
      "name": "string",
      "openAt": "string",
      "ownerId": 0,
      "permissions": {
        "edit": true,
        "read": true
      },
      "projectId": 0,
      "projectName": "string",
      "teamId": 0,
      "teamName": "string",
      "updateAt": "string",
      "updateUserId": 0,
      "visitControl": 0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ allowCopy | boolean | 否 | 是否允许复制 |
| └─ allowCopyRole | string | 否 | 允许复制角色 |
| └─ cover | string | 否 | 文档封面 |
| └─ coverBgColor | string | 否 | 文档封面背景颜色 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文档模式 0：设计文件 1：原型文件 |
| └─ filePath | string | 否 | 文件路径 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 文档名称 |
| └─ openAt | string | 否 | 最近访问时间 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ permissions | object | 否 | 文档权限, 包含查看和编辑权限 |
| └─ edit | boolean | 否 |  |
| └─ read | boolean | 否 |  |
| └─ projectId | integer | 否 | 项目ID |
| └─ projectName | string | 否 | 项目名 |
| └─ teamId | integer | 否 | 团队ID |
| └─ teamName | string | 否 | 团队名 |
| └─ updateAt | string | 否 | 更新时间 |
| └─ updateUserId | integer | 否 | 更新者ID |
| └─ visitControl | integer | 否 | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 筛选团队下文件
请求方法: GET
请求路径: /openapi/v1/team/:teamId/documents
接口描述: 获取指定团队下的文件，支持搜索、排序、分页，仅包含基础信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |
| X-MG-INT-Authentication | 私有化 | string | 否 |  | 集成认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| keyword |  | Query | string | 否 |  | 文件名搜索关键词 |
| sort |  | Query | string | 否 | -updated_at | 排序字段 支持 name, created_at, updated_at |
| pageNum |  | Query | integer | 是 |  | 当前页数，从1开始 |
| pageSize |  | Query | integer | 是 |  | 每页大小 |
| userId |  | Query | integer | 否 |  | 用户ID，非必需参数； 当传入时，会返回该用户对团队下文件的部分权限信息 |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "coverBgColor": "string",
      "createdAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "isTeamLib": true,
      "name": "string",
      "ownerId": 0,
      "permissions": {},
      "sourceId": "string",
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 文件封面 |
| └─ coverBgColor | string | 否 | 文件封面背景颜色 |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ isTeamLib | boolean | 否 | 是否为团队库文件 |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ permissions | object | 否 | 文件权限 |
| └─ sourceId | string | 否 | 所有者三方 ID（仅私有化集成返回） |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下已发布为团队库的文件
请求方法: GET
请求路径: /openapi/v1/team/:teamId/lib/documents
接口描述: 获取指定团队下已发布为团队库的文件信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "createdAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "libraryId": "string",
      "name": "string",
      "ownerId": 0,
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ libraryId | string | 否 | 团队库ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队回收站文件列表
请求方法: GET
请求路径: /openapi/v1/team/:teamId/recycle-bins
接口描述: 获取指定团队下的回收站文件列表，支持搜索、排序、分页，仅包含基础信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Query | integer | 是 |  | 用户ID |
| page[number] |  | Query | integer | 是 | 1 | 当前页数，从1开始 |
| page[size] |  | Query | integer | 是 | 20 | 每页大小 |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "documents": [
      {
        "createdAt": "string",
        "creatorId": 0,
        "deleteSourceId": "string",
        "deleteUserId": 0,
        "fileMode": 0,
        "id": 0,
        "name": "string",
        "ownerId": 0,
        "permissions": {},
        "type": 0,
        "updatedAt": "string"
      }
    ],
    "total": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ documents | array<object> | 否 |  |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ deleteSourceId | string | 否 | 删除者三方 ID（仅私有化集成返回） |
| └─ deleteUserId | integer | 否 | 删除者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ permissions | object | 否 | 文件永久删除和恢复权限 |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| └─ total | integer | 否 | 总记录数 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 创建文档
请求方法: POST
请求路径: /openapi/v1/users/:userId/document
接口描述: 创建文档，需要指定创建用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID，文件所有者 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| projectId |  | integer | 否 |  | 项目ID，当不传入时，默认创建到用户的草稿箱中 |
| name |  | string | 否 |  | 文档名称 |
| fileMode |  | integer | 否 | 0 | 文档模式 0：设计文件 1：原型文件 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "allowCopy": true,
    "allowCopyRole": "string",
    "cover": "string",
    "coverBgColor": "string",
    "createAt": "string",
    "creatorId": 0,
    "fileMode": 0,
    "id": 0,
    "name": "string",
    "ownerId": 0,
    "projectId": 0,
    "teamId": 0,
    "updateAt": "string",
    "updateUserId": 0,
    "visitControl": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ allowCopy | boolean | 否 | 是否允许复制 |
| └─ allowCopyRole | string | 否 | 允许复制角色 |
| └─ cover | string | 否 | 文档封面 |
| └─ coverBgColor | string | 否 | 文档封面背景颜色 |
| └─ createAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文档模式 0：设计文件 1：原型文件 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 文档名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ projectId | integer | 否 | 项目ID |
| └─ teamId | integer | 否 | 团队ID |
| └─ updateAt | string | 否 | 更新时间 |
| └─ updateUserId | integer | 否 | 更新者ID |
| └─ visitControl | integer | 否 | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 删除文档
请求方法: DELETE
请求路径: /openapi/v1/users/:userId/document
接口描述: 删除指定文档，需要指定删除用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Query | string | 是 |  | 文档ID |
| userId |  | Path | string | 是 |  | 用户ID，文件所有者 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 更新文件
请求方法: PUT
请求路径: /openapi/v1/users/:userId/document/:documentId
接口描述: 更新文件，需要指定更新用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID，文件所有者 |
| documentId |  | Path | string | 是 |  | 文档ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| isPublic |  | boolean | 否 |  | 是否公开 |
| allowCopy |  | boolean | 否 |  | 是否允许复制 |
| allowOnlookerCopy |  | boolean | 否 |  | 是否允许查看者复制文件 |
| cover |  | string | 否 |  | 封面 |
| coverBgColor |  | string | 否 |  | 封面背景颜色 |
| name |  | string | 否 |  | 文档名称 |
| versionId |  | integer | 否 |  | 版本号 |
| visitControl |  | integer | 否 |  | 文件访问范围 1-当前团队成员可访问 2-当前企业成员可访问 3-仅受邀协作者可访问 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 检查用户对文件的权限
请求方法: GET
请求路径: /openapi/v1/users/:userId/document/:documentId/permission
接口描述: 检查指定用户是否对某个文件拥有读或编辑权限

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| permission |  | Query | string | 是 |  | 权限类型，支持 read (查看) 或 edit (编辑) |
| userId |  | Path | string | 是 |  | 用户ID |
| documentId |  | Path | string | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": true,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | boolean | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取用户在项目下的文档列表
请求方法: GET
请求路径: /openapi/v1/users/:userId/documents
接口描述: 分页获取用户在项目下的文档列表

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| projectId |  | Query | string | 是 |  | 项目ID |
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| keyword |  | string | 否 |  | 关键词，用于搜索文档名 |
| sort |  | string | 否 | -updated_at | 排序字段 支持 name, created_at, updated_at |
| number |  | integer | 否 | 1 | 当前页数，从1开始 |
| size |  | integer | 否 | 20 | 每页大小 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "coverBgColor": "string",
      "createdAt": "string",
      "fileMode": 0,
      "id": 0,
      "name": "string",
      "ownerId": 0,
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 文件封面 |
| └─ coverBgColor | string | 否 | 文件封面背景颜色 |
| └─ createdAt | string | 否 | 创建时间 |
| └─ fileMode | integer | 否 | 文件模式 0：设计文件 1：原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 文件所有者ID |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 从回收站恢复文件
请求方法: PUT
请求路径: /openapi/v1/users/:userId/team/:teamId/recycle-bins
接口描述: 恢复指定团队回收站中删除的文件，需要指定恢复用户

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| documentIds |  | array<integer> | 是 |  | 文件ID列表 |
| targetProjectId |  | integer | 否 |  | 目标项目ID； 若指定则回收站文件可以恢复到指定项目下 若不指定则恢复到文件所属的原项目下 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 永久删除回收站中的文件
请求方法: DELETE
请求路径: /openapi/v1/users/:userId/team/:teamId/recycle-bins
接口描述: 永久删除指定团队回收站中删除的文件，需要指定删除用户，请谨慎操作

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 请求体
参数名: documentIds - 文件ID列表
类型: 数组＜integer＞

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取文件资源预览信息
请求方法: GET
请求路径: /openapi/v1/resource/preview
接口描述: 获取文件资源预览信息（预览链接），仅对私有化开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Query | string | 是 |  | 文档ID |
| fullScreen |  | Query | boolean | 否 |  | 是否可以全屏 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "previewUrl": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ previewUrl | string | 否 | 文件资源预览链接 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 审批

### Beta 审批申请
请求方法: POST
请求路径: /openapi/v1/applies/:applyId/approval
接口描述: 审批文件编辑权限、席位申请等申请信息

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| applyId |  | Path | integer | 是 |  | 申请ID |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| status |  | string | 是 |  | 审批状态 支持参数：accepted - 通过, denied - 拒绝 |
| name |  | string | 是 |  | 审批人名称 |
| reason |  | string | 否 |  | 审批理由 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 团队库

### 获取指定组件详情
请求方法: GET
请求路径: /openapi/v1/component
接口描述: 根据组件唯一 key 获取指定组件的详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| ukey |  | Query | string | 是 |  | 组件唯一 key; 获取方式请查看文档中【团队库】中相关接口详情 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "componentSetUkey": "string",
    "cover": "string",
    "createdAt": "string",
    "description": "string",
    "documentId": 0,
    "height": 0.0,
    "lastUpdator": {
      "avatar": "string",
      "id": 0,
      "name": "string"
    },
    "layerId": "string",
    "name": "string",
    "pageInfo": {
      "backgroundColor": "string",
      "frameName": "string",
      "layerId": "string",
      "pageId": "string",
      "pageName": "string"
    },
    "type": "string",
    "ukey": "string",
    "updatedAt": "string",
    "width": 0.0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取指定组件集详情
请求方法: GET
请求路径: /openapi/v1/componentSet
接口描述: 根据组件集唯一 key 获取指定组件集的详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| ukey |  | Query | string | 是 |  | 组件集唯一 key; 获取方式请查看文档中【团队库】中相关接口详情 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "cover": "string",
    "createdAt": "string",
    "description": "string",
    "documentId": 0,
    "lastUpdator": {
      "avatar": "string",
      "id": 0,
      "name": "string"
    },
    "layerId": "string",
    "name": "string",
    "pageInfo": {
      "backgroundColor": "string",
      "frameName": "string",
      "layerId": "string",
      "pageId": "string",
      "pageName": "string"
    },
    "ukey": "string",
    "updatedAt": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取文件下已发布的组件集详情
请求方法: GET
请求路径: /openapi/v1/document/:documentId/componentSets
接口描述: 获取指定文件下所有已经发布团队库的组件集详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Path | string | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "layerId": "string",
      "name": "string",
      "pageInfo": {
        "backgroundColor": "string",
        "frameName": "string",
        "layerId": "string",
        "pageId": "string",
        "pageName": "string"
      },
      "ukey": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取文件下已经发布的组件详情
请求方法: GET
请求路径: /openapi/v1/document/:documentId/components
接口描述: 获取指定文件下已经发布的组件详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Path | string | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "componentSetUkey": "string",
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "height": 0.0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "layerId": "string",
      "name": "string",
      "pageInfo": {
        "backgroundColor": "string",
        "frameName": "string",
        "layerId": "string",
        "pageId": "string",
        "pageName": "string"
      },
      "type": "string",
      "ukey": "string",
      "updatedAt": "string",
      "width": 0.0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取文件下所有已发布的内容
请求方法: GET
请求路径: /openapi/v1/document/:documentId/library
接口描述: 获取指定文件下所有已经发布的团队库内容

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Path | string | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "componentSets": [
        {
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "layerId": "string",
          "name": "string",
          "pageInfo": {
            "backgroundColor": "string",
            "frameName": "string",
            "layerId": "string",
            "pageId": "string",
            "pageName": "string"
          },
          "ukey": "string",
          "updatedAt": "string"
        }
      ],
      "components": [
        {
          "componentSetUkey": "string",
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "height": 0.0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "layerId": "string",
          "name": "string",
          "pageInfo": {
            "backgroundColor": "string",
            "frameName": "string",
            "layerId": "string",
            "pageId": "string",
            "pageName": "string"
          },
          "type": "string",
          "ukey": "string",
          "updatedAt": "string",
          "width": 0.0
        }
      ],
      "createdAt": "string",
      "creator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "documentId": 0,
      "documentName": "string",
      "id": "string",
      "projectId": 0,
      "publishedScope": "string",
      "styles": [
        {
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "name": "string",
          "sortIndex": "string",
          "styleSubType": 0,
          "styleType": "string",
          "ukey": "string",
          "updatedAt": "string"
        }
      ],
      "teamId": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ componentSets | array<object> | 否 | 团队库组件集列表 |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| └─ components | array<object> | 否 | 团队库组件列表 |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| └─ createdAt | string | 否 | 团队库创建时间 |
| └─ creator | object | 否 | 团队库创建人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ documentId | integer | 否 | 团队库文件 ID |
| └─ documentName | string | 否 | 团队库文件名称 |
| └─ id | string | 否 | 团队库 ID |
| └─ projectId | integer | 否 | 团队库所属项目 ID |
| └─ publishedScope | string | 否 | 团队库发布范围 |
| └─ styles | array<object> | 否 | 团队库样式列表 |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| └─ teamId | integer | 否 | 团队库所属团队 ID |
| └─ updatedAt | string | 否 | 团队库更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取文件下已发布的样式详情
请求方法: GET
请求路径: /openapi/v1/document/:documentId/styles
接口描述: 获取指定文件下所有已经发布团队库的样式详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| documentId |  | Path | string | 是 |  | 文件ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "name": "string",
      "sortIndex": "string",
      "styleSubType": 0,
      "styleType": "string",
      "ukey": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取指定样式详情
请求方法: GET
请求路径: /openapi/v1/style
接口描述: 根据样式唯一 key 获取指定样式的详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| ukey |  | Query | string | 是 |  | 样式唯一 key; 获取方式请查看文档中【团队库】中相关接口详情 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "cover": "string",
    "createdAt": "string",
    "description": "string",
    "documentId": 0,
    "lastUpdator": {
      "avatar": "string",
      "id": 0,
      "name": "string"
    },
    "name": "string",
    "sortIndex": "string",
    "styleSubType": 0,
    "styleType": "string",
    "ukey": "string",
    "updatedAt": "string"
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 订阅团队库
请求方法: POST
请求路径: /openapi/v1/team-libraries/subscribe
接口描述: 为指定文档订阅团队库

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| libId |  | integer | 是 |  | 团队库id |
| documentId |  | integer | 是 |  | 文档id |

#### 响应
状态码 200: 成功

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下已发布的组件集详情
请求方法: GET
请求路径: /openapi/v1/team/:teamId/componentSets
接口描述: 获取指定团队下所有已经发布团队库的组件集详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "layerId": "string",
      "name": "string",
      "pageInfo": {
        "backgroundColor": "string",
        "frameName": "string",
        "layerId": "string",
        "pageId": "string",
        "pageName": "string"
      },
      "ukey": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下所有已发布组件详情
请求方法: GET
请求路径: /openapi/v1/team/:teamId/components
接口描述: 获取指定团队下所有已经发布团队库的组件详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "componentSetUkey": "string",
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "height": 0.0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "layerId": "string",
      "name": "string",
      "pageInfo": {
        "backgroundColor": "string",
        "frameName": "string",
        "layerId": "string",
        "pageId": "string",
        "pageName": "string"
      },
      "type": "string",
      "ukey": "string",
      "updatedAt": "string",
      "width": 0.0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下所有已发布的内容
请求方法: GET
请求路径: /openapi/v1/team/:teamId/libraries
接口描述: 获取指定团队下所有已经发布的团队库内容

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "componentSets": [
        {
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "layerId": "string",
          "name": "string",
          "pageInfo": {
            "backgroundColor": "string",
            "frameName": "string",
            "layerId": "string",
            "pageId": "string",
            "pageName": "string"
          },
          "ukey": "string",
          "updatedAt": "string"
        }
      ],
      "components": [
        {
          "componentSetUkey": "string",
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "height": 0.0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "layerId": "string",
          "name": "string",
          "pageInfo": {
            "backgroundColor": "string",
            "frameName": "string",
            "layerId": "string",
            "pageId": "string",
            "pageName": "string"
          },
          "type": "string",
          "ukey": "string",
          "updatedAt": "string",
          "width": 0.0
        }
      ],
      "createdAt": "string",
      "creator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "documentId": 0,
      "documentName": "string",
      "id": "string",
      "projectId": 0,
      "publishedScope": "string",
      "styles": [
        {
          "cover": "string",
          "createdAt": "string",
          "description": "string",
          "documentId": 0,
          "lastUpdator": {
            "avatar": "string",
            "id": 0,
            "name": "string"
          },
          "name": "string",
          "sortIndex": "string",
          "styleSubType": 0,
          "styleType": "string",
          "ukey": "string",
          "updatedAt": "string"
        }
      ],
      "teamId": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ componentSets | array<object> | 否 | 团队库组件集列表 |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| └─ components | array<object> | 否 | 团队库组件列表 |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| └─ createdAt | string | 否 | 团队库创建时间 |
| └─ creator | object | 否 | 团队库创建人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ documentId | integer | 否 | 团队库文件 ID |
| └─ documentName | string | 否 | 团队库文件名称 |
| └─ id | string | 否 | 团队库 ID |
| └─ projectId | integer | 否 | 团队库所属项目 ID |
| └─ publishedScope | string | 否 | 团队库发布范围 |
| └─ styles | array<object> | 否 | 团队库样式列表 |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| └─ teamId | integer | 否 | 团队库所属团队 ID |
| └─ updatedAt | string | 否 | 团队库更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 设置团队默认订阅的团队库
请求方法: POST
请求路径: /openapi/v1/team/:teamId/library/default
接口描述: 设置团队默认订阅的团队库, 仅可设置团队中发布的团队库，或是发布到团队的团队库；
团队的团队库数据通过 GET /openapi/v1/team/:teamId/libraries 接口获取

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | integer | 是 |  | 团队ID |

#### 请求体
参数名: libs - 团队库列表
类型: 数组＜object＞

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| id | string | 否 | 团队库ID |
| state | integer | 否 | 订阅状态 1 订阅 0 取消订阅 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": null,
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 获取团队下已发布的样式详情
请求方法: GET
请求路径: /openapi/v1/team/:teamId/styles
接口描述: 获取指定团队下所有已经发布团队库的样式详情

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "createdAt": "string",
      "description": "string",
      "documentId": 0,
      "lastUpdator": {
        "avatar": "string",
        "id": 0,
        "name": "string"
      },
      "name": "string",
      "sortIndex": "string",
      "styleSubType": 0,
      "styleType": "string",
      "ukey": "string",
      "updatedAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取文件中所有订阅的组件库详情
请求方法: GET
请求路径: /openapi/v1/document/:documentId/subscribeTeamLibraries/detail
接口描述: 获取文件中所有订阅的组件库详情，仅对私有化开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| withPresetLib |  | Query | boolean | 否 |  | 是否包含预制团队库 |
| documentId |  | Path | string | 是 |  | 文档ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "teamLibrary": [
      {
        "componentSets": [
          {
            "cover": "string",
            "createdAt": "string",
            "description": "string",
            "documentId": 0,
            "lastUpdator": {
              "avatar": "string",
              "id": 0,
              "name": "string"
            },
            "layerId": "string",
            "name": "string",
            "pageInfo": {
              "backgroundColor": "string",
              "frameName": "string",
              "layerId": "string",
              "pageId": "string",
              "pageName": "string"
            },
            "ukey": "string",
            "updatedAt": "string"
          }
        ],
        "components": [
          {
            "componentSetUkey": "string",
            "cover": "string",
            "createdAt": "string",
            "description": "string",
            "documentId": 0,
            "height": 0.0,
            "lastUpdator": {
              "avatar": "string",
              "id": 0,
              "name": "string"
            },
            "layerId": "string",
            "name": "string",
            "pageInfo": {
              "backgroundColor": "string",
              "frameName": "string",
              "layerId": "string",
              "pageId": "string",
              "pageName": "string"
            },
            "type": "string",
            "ukey": "string",
            "updatedAt": "string",
            "width": 0.0
          }
        ],
        "createdAt": "string",
        "creator": {
          "avatar": "string",
          "id": 0,
          "name": "string"
        },
        "documentId": 0,
        "documentName": "string",
        "id": "string",
        "projectId": 0,
        "publishedScope": "string",
        "styles": [
          {
            "cover": "string",
            "createdAt": "string",
            "description": "string",
            "documentId": 0,
            "lastUpdator": {
              "avatar": "string",
              "id": 0,
              "name": "string"
            },
            "name": "string",
            "sortIndex": "string",
            "styleSubType": 0,
            "styleType": "string",
            "ukey": "string",
            "updatedAt": "string"
          }
        ],
        "teamId": 0,
        "updatedAt": "string"
      }
    ]
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ teamLibrary | array<object> | 否 |  |
| └─ componentSets | array<object> | 否 | 团队库组件集列表 |
| └─ cover | string | 否 | 组件集封面 |
| └─ createdAt | string | 否 | 组件集创建时间 |
| └─ description | string | 否 | 组件集描述 |
| └─ documentId | integer | 否 | 组件集所属文档 ID |
| └─ lastUpdator | object | 否 | 组件集最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件集所属图层 ID |
| └─ name | string | 否 | 组件集名称 |
| └─ pageInfo | object | 否 | 组件集页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ ukey | string | 否 | 组件集 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件集更新时间 |
| └─ components | array<object> | 否 | 团队库组件列表 |
| └─ componentSetUkey | string | 否 | 组件所属组件集 UKey |
| └─ cover | string | 否 | 组件封面 |
| └─ createdAt | string | 否 | 组件创建时间 |
| └─ description | string | 否 | 组件描述 |
| └─ documentId | integer | 否 | 组件所属文档 ID |
| └─ height | number | 否 | 组件高度 |
| └─ lastUpdator | object | 否 | 组件最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ layerId | string | 否 | 组件所属图层 ID |
| └─ name | string | 否 | 组件名称 |
| └─ pageInfo | object | 否 | 组件页面信息 |
| └─ backgroundColor | string | 否 | 背景颜色 |
| └─ frameName | string | 否 | 容器名称 |
| └─ layerId | string | 否 | 图层 ID |
| └─ pageId | string | 否 | 页面 ID |
| └─ pageName | string | 否 | 页面名称 |
| └─ type | string | 否 | 组件类型 |
| └─ ukey | string | 否 | 组件 UKey (唯一) |
| └─ updatedAt | string | 否 | 组件更新时间 |
| └─ width | number | 否 | 组件宽度 |
| └─ createdAt | string | 否 | 团队库创建时间 |
| └─ creator | object | 否 | 团队库创建人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ documentId | integer | 否 | 团队库文件 ID |
| └─ documentName | string | 否 | 团队库文件名称 |
| └─ id | string | 否 | 团队库 ID |
| └─ projectId | integer | 否 | 团队库所属项目 ID |
| └─ publishedScope | string | 否 | 团队库发布范围 |
| └─ styles | array<object> | 否 | 团队库样式列表 |
| └─ cover | string | 否 | 样式封面 |
| └─ createdAt | string | 否 | 样式创建时间 |
| └─ description | string | 否 | 样式描述 |
| └─ documentId | integer | 否 | 样式所属文档 ID |
| └─ lastUpdator | object | 否 | 样式最后更新人信息 |
| └─ avatar | string | 否 | 用户头像 |
| └─ id | integer | 否 | 用户 ID |
| └─ name | string | 否 | 用户名 |
| └─ name | string | 否 | 样式名称 |
| └─ sortIndex | string | 否 | 样式子类型 |
| └─ styleSubType | integer | 否 | 样式子类型 |
| └─ styleType | string | 否 | 样式类型 |
| └─ ukey | string | 否 | 样式 UKey (唯一) |
| └─ updatedAt | string | 否 | 样式更新时间 |
| └─ teamId | integer | 否 | 团队库所属团队 ID |
| └─ updatedAt | string | 否 | 团队库更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 字体库

### 获取企业字体库
请求方法: GET
请求路径: /openapi/v1/organization/font

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| pageNum |  | Query | integer | 否 |  | 页码 |
| pageSize |  | Query | integer | 否 |  | 每页记录数 |
| keyword |  | Query | string | 否 |  | 搜索关键字，用于搜索字体样式、字体名称、字体家族名称 |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "family": "string",
      "localizedFamily": "string",
      "styles": [
        {
          "coverUrl": "string",
          "id": 0,
          "localizedStyle": "string",
          "style": "string",
          "url": "string"
        }
      ],
      "teamId": 0,
      "teamName": "string",
      "type": "string",
      "version": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ family | string | 否 | 字体名称 |
| └─ localizedFamily | string | 否 | 本地化字体名称 |
| └─ styles | array<object> | 否 | 字体样式列表 |
| └─ coverUrl | string | 否 | 封面URL |
| └─ id | integer | 否 | 字体ID |
| └─ localizedStyle | string | 否 | 本地化字体样式 |
| └─ style | string | 否 | 字体样式 |
| └─ url | string | 否 | 文件URL |
| └─ teamId | integer | 否 | 团队ID |
| └─ teamName | string | 否 | 团队名称 |
| └─ type | string | 否 | 字体类型，team团队字体 organization企业字体 |
| └─ version | string | 否 | 版本号 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 删除企业字体库字体
请求方法: DELETE
请求路径: /openapi/v1/organization/font

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| fontIds |  | array<integer> | 是 |  | 字体ID列表 |
| operatorId |  | integer | 是 |  | 操作人ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 删除用户所在团队字体库字体
请求方法: DELETE
请求路径: /openapi/v1/users/:userId/font-libraries/fonts
接口描述: 删除用户所在团队字体库字体

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |

#### 请求体
参数名: ids - 字体ID列表
类型: 数组＜integer＞

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {},
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 私有化 获取用户所在团队字体库
请求方法: GET
请求路径: /openapi/v1/users/:userId/font-libraries/team/:teamId
接口描述: 获取用户所在团队字体库

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| userId |  | Path | string | 是 |  | 用户ID |
| teamId |  | Path | string | 是 |  | 团队ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "coverUrl": "string",
      "createAt": "string",
      "family": "string",
      "id": 0,
      "isVariable": true,
      "italic": 0,
      "localizedFamily": "string",
      "localizedStyle": "string",
      "monoSpace": 0,
      "organizationId": 0,
      "originUrl": "string",
      "postScriptName": "string",
      "style": "string",
      "teamId": 0,
      "type": "string",
      "updateAt": "string",
      "url": "string",
      "version": "string",
      "weight": 0,
      "width": 0
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ coverUrl | string | 否 | 封面url |
| └─ createAt | string | 否 | 创建时间 |
| └─ family | string | 否 | 字体名 |
| └─ id | integer | 否 | ID |
| └─ isVariable | boolean | 否 | 是否为可变字体 |
| └─ italic | integer | 否 | 是否为斜体 |
| └─ localizedFamily | string | 否 | 本地化名字 |
| └─ localizedStyle | string | 否 | 本地化样式 |
| └─ monoSpace | integer | 否 | 是否为等宽字体 |
| └─ organizationId | integer | 否 | 企业ID |
| └─ originUrl | string | 否 | 存储TTC文件的URL |
| └─ postScriptName | string | 否 | postScriptName |
| └─ style | string | 否 | 样式 |
| └─ teamId | integer | 否 | 团队ID |
| └─ type | string | 否 | 字体类型 team团队字体 organization企业字体 |
| └─ updateAt | string | 否 | 更新时间 |
| └─ url | string | 否 | 文件url |
| └─ version | string | 否 | 版本号 |
| └─ weight | integer | 否 | 字重 |
| └─ width | integer | 否 | 字宽 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## 文件分组

### 获取项目下所有分组
请求方法: GET
请求路径: /openapi/v1/project/:projectId/group
接口描述: 获取指定项目下的所有分组

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| projectId |  | Path | string | 是 |  | 项目ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "category": "string",
      "createAt": "string",
      "id": 0,
      "name": "string",
      "projectId": 0,
      "updateAt": "string"
    }
  ],
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ category | string | 否 | 分组类型 |
| └─ createAt | string | 否 | 创建时间 |
| └─ id | integer | 否 | ID |
| └─ name | string | 否 | 分组名称 |
| └─ projectId | integer | 否 | 项目ID |
| └─ updateAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

### 筛选分组下文件列表
请求方法: GET
请求路径: /openapi/v1/project/:projectId/group/:groupId/documents
接口描述: 分页获取指定分组下的文件，支持搜索、排序、分页

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 参数

| 参数名 | 标签 | 位置 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|---|
| keyword |  | Query | string | 否 |  | 搜索关键词 |
| sort |  | Query | string | 否 | -updated_at | 排序字段 支持 name, created_at, updated_at |
| page[number] |  | Query | integer | 是 |  | 当前页数，从1开始 |
| page[size] |  | Query | integer | 是 |  | 每页大小 |
| projectId |  | Path | string | 是 |  | 项目ID |
| groupId |  | Path | string | 是 |  | 分组ID |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": [
    {
      "cover": "string",
      "coverBgColor": "string",
      "createdAt": "string",
      "creatorId": 0,
      "fileMode": 0,
      "id": 0,
      "name": "string",
      "ownerId": 0,
      "type": 0,
      "updatedAt": "string"
    }
  ],
  "meta": {
    "page": {
      "total": 0
    },
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | array<object> | 否 |  |
| └─ cover | string | 否 | 文件封面 |
| └─ coverBgColor | string | 否 | 文件封面背景颜色 |
| └─ createdAt | string | 否 | 创建时间 |
| └─ creatorId | integer | 否 | 创建者ID |
| └─ fileMode | integer | 否 | 文件模式; 0 设计文件,1 原型文件 |
| └─ id | integer | 否 | 文件ID |
| └─ name | string | 否 | 文件名称 |
| └─ ownerId | integer | 否 | 所有者ID |
| └─ type | integer | 否 | 文件类型 |
| └─ updatedAt | string | 否 | 更新时间 |
| meta | object | 否 |  |
| └─ page | object | 否 | 分页信息 |
| └─ total | integer | 否 | 总条数 |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |

## AI

### 私有化 查询 AI 积分明细
请求方法: POST
请求路径: /openapi/v1/ai/account/credit-records
接口描述: 查询 AI 积分明细，目前仅对私有化部署开放

#### 请求头

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| X-MG-Authentication |  | string | 是 |  | OPENAPI 认证头 |

#### 请求体

| 参数名 | 标签 | 类型 | 必填 | 默认值 | 描述 |
|---|---|---|---|---|---|
| source_ids |  | array<string> | 否 |  | 第三方用户ID列表 |
| start_time |  | string | 是 |  | 开始时间，格式如 |
| end_time |  | string | 是 |  | 结束时间，格式如 |
| page |  | integer | 否 |  | 页码，从1开始 |
| page_size |  | integer | 否 |  | 每页数量 |
| biz_type |  | string | 否 |  | 业务类型:gen_ui(AI快搭)、agent(Agent)、full(全量),默认为full |

#### 响应
状态码 200: code - OK

```
{
  "code": "string",
  "data": {
    "records": [
      {
        "credit": 0,
        "email": "string",
        "id": 0,
        "model_type": 0,
        "operation": "string",
        "operation_name": "string",
        "product": "string",
        "source_id": "string",
        "team_id": 0,
        "team_name": "string",
        "time": "string",
        "user_name": "string"
      }
    ],
    "total": 0
  },
  "meta": {
    "time": 0,
    "trace": "string"
  },
  "msg": "string"
}
```

| 字段名 | 类型 | 必填 | 描述 |
|---|---|---|---|
| code | string | 否 | 响应码, 成功为 OK, 其他的为错误码 |
| data | object | 否 |  |
| └─ records | array<object> | 否 | 当前页的记录 |
| └─ credit | integer | 否 | 积分变动 |
| └─ email | string | 否 | 用户邮箱 |
| └─ id | integer | 否 | 记录ID |
| └─ model_type | integer | 否 | 模型 0 大匠 1 小匠 |
| └─ operation | string | 否 | 操作类型 |
| └─ operation_name | string | 否 | 任务类型 |
| └─ product | string | 否 | 所属产品 |
| └─ source_id | string | 否 | 实体ID |
| └─ team_id | integer | 否 | 所属团队ID |
| └─ team_name | string | 否 | 所属团队名称 |
| └─ time | string | 否 | 操作时间 |
| └─ user_name | string | 否 | 用户名称 |
| └─ total | integer | 否 | 总记录数 |
| meta | object | 否 |  |
| └─ time | integer | 否 |  |
| └─ trace | string | 否 | 链路ID； 如果存在异常，可以提供该 ID 给 MasterGo 相关人员进行问题排查 |
| msg | string | 否 |  |