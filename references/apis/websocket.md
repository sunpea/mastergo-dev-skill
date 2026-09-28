# mg.WebSocket

- Type:

```
interface WebSocketHandle {
  readonly readyState: number
  readonly url: string
  readonly protocol: string

  onopen: ((self: WebSocketHandle, event: { type: string }) => void) | undefined
  onmessage: ((self: WebSocketHandle, data: any) => void) | undefined
  onclose: ((self: WebSocketHandle, event: { code: number; reason: string; wasClean: boolean }) => void) | undefined
  onerror: ((self: WebSocketHandle, event: { type: string }) => void) | undefined

  send(data: any): void
  close(code?: number, reason?: string): void
}

interface WebSocketAPI {
  CONNECTING: 0
  OPEN: 1
  CLOSING: 2
  CLOSED: 3

  connect(url: string, protocols?: string | string[]): WebSocketHandle
}
```

mg.WebSocket 是插件运行时暴露的 WebSocket 封装，允许任意插件在画布页直接创建和管理 WebSocket 连接。其 API 设计尽量贴近浏览器原生 WebSocket 接口。

> > **WARNING**
> mg.WebSocket 依赖宿主环境（浏览器）的原生 WebSocket 实现，仅支持基于 JSON 的文本协议。二进制消息暂不支持，回调参数签名与原生 API 略有差异：每个回调的第一个参数为自身的 WebSocketHandle 对象。

## 静态常量
mg.WebSocket 上有 4 个静态常量，用于比对连接的当前状态：

| 常量 | 值 | 说明 |
|---|---|---|
| `mg.WebSocket.CONNECTING` | 0 | 连接建立中 |
| `mg.WebSocket.OPEN` | 1 | 连接已建立，可通信 |
| `mg.WebSocket.CLOSING` | 2 | 连接正在关闭 |
| `mg.WebSocket.CLOSED` | 3 | 连接已关闭（或无法打开） |

## `connect`

- Type: `connect(url: string, protocols?: string | string[]): WebSocketHandle`
创建并返回一个新的 WebSocket 连接对象。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | `string` | 是 | WebSocket 服务器地址，支持 `ws://` / `wss://` |
| `protocols` | `string` \| `string[]` | 否 | 子协议，透传给原生 `WebSocket` 构造函数 |

异常： URL 无效时抛出 Error。

```
// 基本用法
const ws = mg.WebSocket.connect('ws://localhost:50678');

// 指定子协议
const ws2 = mg.WebSocket.connect('wss://example.com/ws', ['soap', 'wamp']);
```

## WebSocketHandle
connect() 返回的对象，包含以下属性和方法：

### 属性

#### `readyState` *(只读)*

- Type: `number`
当前连接状态，对应以下常量：

| 值 | 常量 |
|---|---|
| 0 | `mg.WebSocket.CONNECTING` |
| 1 | `mg.WebSocket.OPEN` |
| 2 | `mg.WebSocket.CLOSING` |
| 3 | `mg.WebSocket.CLOSED` |

#### `url` *(只读)*

- Type: `string`
连接所用的 URL。

#### `protocol` *(只读)*

- Type: `string`
协商后的子协议名称，无则为空字符串。

#### `onopen`

- Type: `(self: WebSocketHandle, event: { type: string }) => void` | `undefined`
连接成功时的回调。self 是 WebSocketHandle 自身，方便在回调内部直接引用。

```
ws.onopen = function(self, event) {
  console.log('连接成功，url:', self.url);
};
```

#### `onmessage`

- Type: `(self: WebSocketHandle, data: any) => void` | `undefined`
收到消息时的回调。字符串类型的消息会尝试 JSON.parse；解析失败则透传原始字符串。

```
ws.onmessage = function(self, data) {
  console.log('收到消息:', data);
};
```

#### `onclose`

- Type: `(self: WebSocketHandle, event: { code: number; reason: string; wasClean: boolean }) => void` | `undefined`
连接关闭时的回调。

```
ws.onclose = function(self, event) {
  console.log('连接关闭:', event.code, event.reason, '干净关闭:', event.wasClean);
};
```

#### `onerror`

- Type: `(self: WebSocketHandle, event: { type: string }) => void` | `undefined`
连接发生错误时的回调。

```
ws.onerror = function(self, event) {
  console.error('WebSocket 错误:', event.type);
};
```

### 方法

#### `send(data)`
发送消息。对象类型会自动 JSON.stringify，字符串则直接发送。

```
// 发送字符串
ws.send('ping');

// 发送对象（自动序列化为 JSON）
ws.send({ cmd: 'canvasOp', data: { layerId: '123' } });
```

#### `close(code?, reason?)`
关闭连接。

| 参数 | 类型 | 说明 |
|---|---|---|
| `code` | `number` | 关闭状态码 |
| `reason` | `string` | 关闭原因描述 |

```
ws.close(1000, '正常关闭');
```

## 与浏览器原生 WebSocket 的差异

| 特性 | 原生 WebSocket | mg.WebSocket |
|---|---|---|
| 回调参数 | `event` 对象 | `(self, data/event)` — 第一个参数为自身 handle |
| onmessage data | 始终为字符串 / Blob / ArrayBuffer | 字符串自动 `JSON.parse`，解析失败则返回原始字符串 |
| readyState | 实例属性 | 实例属性（透传） |
| 协议常量 | `WebSocket.CONNECTING` 等 | `mg.WebSocket.CONNECTING` 等 |
| 二进制消息 | 支持 Blob / ArrayBuffer | 暂不支持 |

## 完整示例

### 插件端 (mg.WebSocket)

```
function connectMCP() {
  const ws = mg.WebSocket.connect('ws://localhost:50678');

  ws.onopen = function(self) {
    console.log('MCP WebSocket 已连接');
    self.send({ type: 'handshake', version: 1 });
  };

  ws.onmessage = function(self, data) {
    console.log('收到 MCP 消息:', data);

    switch (data.type) {
      case 'handshake_ack':
        console.log('握手成功');
        break;
      case 'canvasOp':
        handleOperation(data);
        break;
    }
  };

  ws.onclose = function(self, event) {
    if (!event.wasClean) {
      console.warn('连接异常关闭，code:', event.code);
    }
  };

  ws.onerror = function() {
    console.error('WebSocket 连接错误');
  };

  return ws;
}

// 使用静态常量检查状态
function safeSend(ws, data) {
  if (ws.readyState === mg.WebSocket.OPEN) {
    ws.send(data);
    return true;
  }
  console.warn('WebSocket 未连接，readyState:', ws.readyState);
  return false;
}
```

### 服务端示例 (Node.js)
以下是一个基于 Node.js 内置模块的 echo server，可用于开发和测试：

```
// ws-echo-server.mjs — Node.js 20+
import { createServer } from 'http';
import crypto from 'crypto';

const PORT = 50678;

function acceptKey(key) {
  const MAGIC = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';
  return crypto.createHash('sha1').update(key + MAGIC).digest('base64');
}

function encodeFrame(payload) {
  const buf = Buffer.from(payload, 'utf8');
  const len = buf.length;
  const head = [0x81]; // FIN + text opcode
  if (len < 126) head.push(len);
  else if (len < 65536) head.push(126, (len >> 8) & 0xff, len & 0xff);
  else { head.push(127); for (let i = 7; i >= 0; i--) head.push((len >> (i * 8)) & 0xff); }
  return Buffer.concat([Buffer.from(head), buf]);
}

function decodeFrame(buf) {
  if (buf.length < 2) return null;
  const first = buf[0], second = buf[1];
  const opcode = first & 0x0f;
  const masked = (second & 0x80) !== 0;
  let len = second & 0x7f, offset = 2;
  if (len === 126) { len = buf.readUInt16BE(2); offset = 4; }
  else if (len === 127) { len = Number(buf.readBigUInt64BE(2)); offset = 10; }
  const mLen = masked ? 4 : 0;
  if (buf.length < offset + mLen + len) return null;
  let payload;
  if (masked) {
    const mask = buf.slice(offset, offset + 4);
    payload = buf.slice(offset + 4, offset + 4 + len);
    for (let i = 0; i < len; i++) payload[i] ^= mask[i % 4];
  } else { payload = buf.slice(offset, offset + len); }
  return { opcode, payload, fin: (first & 0x80) !== 0 };
}

const server = createServer((req, res) => {
  res.writeHead(404); res.end();
});

server.on('upgrade', (req, socket) => {
  const key = req.headers['sec-websocket-key'];
  if (!key) { socket.destroy(); return; }
  socket.write([
    'HTTP/1.1 101 Switching Protocols',
    'Upgrade: websocket',
    'Connection: Upgrade',
    `Sec-WebSocket-Accept: ${acceptKey(key)}`,
    '', ''
  ].join('\r\n'));

  let buf = Buffer.alloc(0);
  socket.on('data', (chunk) => {
    buf = Buffer.concat([buf, chunk]);
    const frame = decodeFrame(buf);
    if (!frame) return;
    // 解析帧大小并消费
    const s1 = buf[1]; const m = (s1 & 0x80) !== 0;
    const dl = s1 & 0x7f;
    const hs = dl === 126 ? 4 : (dl === 127 ? 10 : 2);
    buf = buf.slice(hs + (m ? 4 : 0) + frame.payload.length);

    if (frame.opcode === 0x8) {
      socket.write(Buffer.from([0x88, 0x02, 0x03, 0xe8]));
      socket.end();
      return;
    }
    if (frame.opcode === 0x9) {
      socket.write(Buffer.concat([Buffer.from([0x8a, frame.payload.length]), frame.payload]));
      return;
    }
    // text frame: echo back
    const text = frame.payload.toString('utf8');
    const resp = text === 'ping' ? 'pong' : text;
    socket.write(encodeFrame(resp));
  });
  socket.on('error', () => socket.destroy());
});

server.listen(PORT, () => console.log(`ws://localhost:${PORT}`));
```

启动服务端：

```
node ws-echo-server.mjs
```

然后在插件中连接：

```
const ws = mg.WebSocket.connect('ws://localhost:50678');

ws.onopen = function(self) {
  self.send('ping');               // 服务端返回 'pong'
  self.send({ cmd: 'hello' });     // 服务端 echo 原对象
};

ws.onmessage = function(self, data) {
  console.log('收到:', data);      // 第一次收到 'pong'，第二次收到 { cmd: 'hello' }
};
```

mastergo.clientStorage
mastergo.notify