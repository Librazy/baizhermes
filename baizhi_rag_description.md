# Baizhi RAG API 文档

## 概述

Baizhi RAG API 提供知识库文档管理和智能问答接口，适合以下场景：

- 创建、更新、删除知识库文档
- 查询文档处理状态
- 基于知识库的语义搜索
- 流式智能问答（带引用溯源）

## 基本信息

**Base URL**

```text
https://ragcloud.app.baizhi.cloud/openapi/v1
```

**认证**

所有请求都需要在 Header 中携带 API Key：

```text
Authorization: Bearer <BAIZHI_RAG_API_KEY>
```

完整请求头示例：

```text
Content-Type: application/json
Authorization: Bearer <BAIZHI_RAG_API_KEY>
```

---

## 1. 文档管理

### 1.1 创建文档

将文本内容创建为知识库文档。

#### 请求

```
POST https://ragcloud.app.baizhi.cloud/openapi/v1/documents
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 文档标题，系统会自动生成对应文件名 |
| `content` | string | 是 | 文档正文，支持 Markdown 或纯文本 |

#### 请求示例

```bash
curl -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/documents \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "产品手册",
    "content": "这里是文档正文（Markdown 或纯文本）"
  }'
```

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `document_id` | string | 新创建文档的 ID |
| `status` | string | 文档当前状态，`uploaded` 表示已入队等待处理 |

#### 响应示例

```json
{
  "document_id": "doc_abc123",
  "status": "uploaded"
}
```

---

### 1.2 更新文档

更新已有文档的标题和内容。

#### 请求

```
PUT https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id>
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

#### 路径参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document_id` | string | 是 | 要更新的文档 ID |

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 更新后的文档标题 |
| `content` | string | 是 | 更新后的文档正文 |

#### 请求示例

```bash
curl -X PUT https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id> \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "更新后的标题",
    "content": "更新后的文档内容"
  }'
```

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `document_id` | string | 已更新的文档 ID |
| `status` | string | 重新入队后的状态，`uploaded` 表示等待重新处理 |

#### 响应示例

```json
{
  "document_id": "doc_abc123",
  "status": "uploaded"
}
```

---

### 1.3 删除文档

删除指定文档。

#### 请求

```
DELETE https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id>
Authorization: Bearer <API_KEY>
```

#### 路径参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document_id` | string | 是 | 要删除的文档 ID |

#### 请求示例

```bash
curl -X DELETE "https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id>" \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>"
```

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `document_id` | string | 进入删除流程的文档 ID |
| `status` | string | 删除状态，`deleting` 表示后台正在清理 |

#### 响应示例

```json
{
  "document_id": "doc_abc123",
  "status": "deleting"
}
```

---

### 1.4 获取文档状态

查询文档的处理状态。

#### 请求

```
GET https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id>/status
Authorization: Bearer <API_KEY>
```

#### 路径参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `document_id` | string | 是 | 要查询状态的文档 ID |

#### 请求示例

```bash
curl -X GET "https://ragcloud.app.baizhi.cloud/openapi/v1/documents/<document_id>/status" \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>"
```

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | string | 处理状态。`processing` 表示处理中；`ready` 表示已可用；`error` 表示处理失败 |

#### 响应示例

```json
{
  "status": "ready"
}
```

---

## 2. 智能问答

### 2.1 流式智能问答

基于知识库进行流式问答，返回检索结果和 AI 生成的答案。

#### 请求

```
POST https://ragcloud.app.baizhi.cloud/openapi/v1/chat/stream
Content-Type: application/json
Accept: text/event-stream
Authorization: Bearer <API_KEY>
```

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 用户问题 |
| `top_k` | number | 否 | 控制召回候选数量，默认值：`10` |

#### 请求示例

```bash
curl -N -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/chat/stream \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>" \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "如何创建知识库？"
  }'
```

#### 响应（SSE 事件流）

响应为标准 SSE 格式，每条消息由 `event:` 和 `data:` 两行组成，空行分隔。

##### 事件类型

| 事件名 | 说明 |
|--------|------|
| `retrieval_done` | 返回检索阶段命中的结果 |
| `delta` | 逐段返回模型生成内容 |
| `citations` | 回答引用的文档片段列表 |
| `done` | 流结束，包含最终汇总答案 |

##### 响应字段

| 字段 | 类型 | 出现事件 | 说明 |
|------|------|---------|------|
| `items` | array | `retrieval_done` | 检索命中的结果列表，包含 `document_id` 和 `chunk_id` |
| `content` | string | `delta` | 增量答案文本片段 |
| `citations` | array | `citations` | 引用的文档片段列表 |
| `answer` | string | `done` | 最终汇总答案 |

#### 响应示例

```
event: retrieval_done
data: {"items":[{"document_id":"doc_01","chunk_id":"chunk_01"}]}

event: delta
data: {"content":"请先创建知识库"}

event: delta
data: {"content":"，再添加文档。"}

event: citations
data: [{"document_id":"doc_01","chunk_id":"chunk_01"}]

event: done
data: {"answer":"请先创建知识库，再添加文档。"}
```

---

### 2.2 语义搜索

基于知识库进行语义检索，返回相关文档片段。

#### 请求

```
POST https://ragcloud.app.baizhi.cloud/openapi/v1/retrieve
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 检索关键词或自然语言问题 |
| `top_k` | number | 否 | 返回的最大结果数，默认值：`10` |
| `score_threshold` | number | 否 | 最小结果分数阈值，默认值：`0` |
| `group_by_document` | boolean | 否 | 是否将同一文档命中的 chunk 按 position 顺序拼接后返回，默认值：`false` |
| `include_score_detail` | boolean | 否 | 是否返回 score_detail 细分得分说明，默认值：`false` |

#### 请求示例

```bash
curl -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/retrieve \
  -H "Authorization: Bearer <BAIZHI_RAG_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "权限管理"
  }'
```

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `latency_ms` | number | 本次检索总耗时，单位毫秒 |
| `items` | object[] | 检索命中的结果列表。聚合文档时，每项代表一个文档聚合结果 |
| `items[].chunk_id` | string | 命中的 chunk ID。聚合文档时，表示该聚合结果的锚点 chunk ID |
| `items[].chunk_ids` | string[] | 命中的 chunk ID 列表（聚合文档时） |
| `items[].document_id` | string | 命中文档 ID |
| `items[].collection_id` | string | 所属知识库 ID |
| `items[].position` | number | chunk 在文档中的顺序位置 |
| `items[].document_title` | string | 文档标题，可能为空 |
| `items[].score` | number | 融合后的最终相关性分数 |
| `items[].score_detail` | object | 细分得分说明（仅在 `include_score_detail=true` 时返回） |
| `items[].content` | string | 命中的内容 |

#### 响应示例

```json
{
  "latency_ms": 42,
  "items": [
    {
      "chunk_id": "chunk_05",
      "document_id": "doc_06",
      "collection_id": "kb_01",
      "position": 2,
      "document_title": "权限管理指南",
      "content": "权限模型说明...",
      "score": 0.95,
      "score_detail": {
        "final": 0.95,
        "reranker": 0.91
      }
    }
  ]
}
```

---

## 错误处理

当接口返回错误时，请参考以下排查方向：

- **认证失败**：检查 `Authorization` Header 中的 API Key 是否正确
- **文档不存在**：检查 `document_id` 是否有效
- **参数错误**：检查必填字段是否完整，参数类型是否正确
- **流式错误**：监听 SSE 事件中的错误信息

建议客户端在失败时记录以下信息：

- 请求参数
- 服务端返回的错误信息
- 请求链路追踪 ID（如有）

---

## 使用建议

- **文档创建后**：建议轮询 `/documents/<document_id>/status` 接口，等待状态变为 `ready` 后再进行问答
- **流式问答**：客户端需按顺序拼接所有 `delta` 片段才能得到完整答案
- **语义搜索**：可结合 `score_threshold` 过滤低相关性结果，或使用 `group_by_document` 合并同一文档的多个片段
- **聚合文档**：当 `group_by_document=true` 时，`content` 字段会包含按 position 升序拼接后的完整内容
