# User

```
interface User {
    id: string | null 
    name: string
    photoUrl: string | null 
    email?: string // 私有化特有
}
```

User对象用于描述用户的基本信息。

- `id` ：系统生成的用户id，具有唯一性。用户为游客则会返回`null`。
- `name` ：用户名称。用户为游客则会返回`'Anonymous'`。
- `photoUrl` ：用户设置的头像地址。用户为游客或未设置头像则会返回`null`。
- `email` 私有化：用户邮箱。用户未设置邮箱则返回`undefined`。

UIViewport