# Baizhi Web Search API 文档

## 概述

Baizhi Web Search 提供两类 OpenAPI 接口：

| 接口 | 适用场景 |
|------|---------|
| 通用搜索 `POST /openapi/search` | 返回原始网页结果列表（JSON），适合自行处理或喂给大模型 |
| AI 搜索 `POST /openapi/ai_search` | 流式返回 AI 生成答案 + 来源引用（SSE），适合问答机器人 |

**Base URL**

```
https://websearch.app.baizhi.cloud
```

**认证**

所有请求均需在 Header 中携带 API Key：

```
Authorization: Bearer <BAIZHI_WEB_SEARCH_API_KEY>
```

---

## 1. 通用搜索

### 请求

```
POST /openapi/search
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 要搜索的关键词或问题 |
| `count` | integer | 否 | 返回结果数，默认 `10`，最大 `50` |
| `time_range` | string | 否 | 时间范围过滤，可选值见下表，默认 `month` |
| `filter` | object | 否 | 可选筛选对象，可包含/排除特定站点 |
| `filter.domains` | string[] | 否 | 仅返回这些域名下的结果，如 `["example.com", "openai.com"]`，支持主域名匹配 |
| `filter.exclude_domains` | string[] | 否 | 从结果中排除这些域名，如 `["ads.example.com", "spam.com"]` |

**`time_range` 可选值**

| 值 | 含义 |
|----|------|
| `day` | 最近一天 |
| `week` | 最近一周 |
| `month` | 最近一月（默认） |
| `year` | 最近一年 |

#### 请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://websearch.app.baizhi.cloud/openapi/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SEARCH_API_KEY}" \
  -d '{
    "query": "Kimi K2.6 模型用户体验",
    "count": 10
  }'
```

带域名过滤：

```bash
curl -SL --fail-with-body -X POST \
  https://websearch.app.baizhi.cloud/openapi/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SEARCH_API_KEY}" \
  -d '{
    "query": "大模型最新进展",
    "count": 5,
    "time_range": "week",
    "filter": {
      "domains": ["36kr.com", "techcrunch.com"],
      "exclude_domains": ["spam.com"]
    }
  }'
```

---

### 响应

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | integer | 状态码，`0` 表示成功 |
| `message` | string | 状态描述，成功时固定为 `"success"` |
| `trace_id` | string | 请求链路追踪 ID |
| `data.request_id` | integer | 本次搜索请求 ID |
| `data.status` | string | 搜索状态，如 `"succeeded"` |
| `data.query` | string | 原始查询词 |
| `data.normalized_query` | string | 经过规范化处理的查询词 |
| `data.result_count` | integer | 实际返回结果数 |
| `data.latency_ms` | integer | 本次搜索耗时（毫秒） |
| `data.results` | array | 搜索结果列表 |
| `data.results[].rank` | integer | 结果排名，从 `1` 开始 |
| `data.results[].title` | string | 结果标题 |
| `data.results[].url` | string | 结果链接 |
| `data.results[].site_name` | string | 站点名称 |
| `data.results[].published_at` | string | 发布时间，RFC3339 格式 |
| `data.results[].score` | float | 相关性评分 |

#### 响应示例

```json
{
  "code": 0,
  "message": "success",
  "trace_id": "trc_dc052e45f228742671b33ab5",
  "data": {
    "request_id": 2525,
    "status": "succeeded",
    "query": "Kimi K2.6 模型用户体验",
    "normalized_query": "Kimi K2.6 模型用户体验",
    "result_count": 10,
    "latency_ms": 396,
    "results": [
      {
        "rank": 1,
        "title": "国家超算互联网AI社区上线Kimi K2.6",
        "url": "http://m.163.com/dy/article/KR2045100550WHYR.html",
        "published_at": "2026-04-21T14:30:00+08:00",
        "score": 0.9903837442398071,
        "site_name": "网易"
      },
      {
        "rank": 2,
        "title": "月之暗面新模型Kimi K2.6发布并开源",
        "url": "http://news.qq.com/rain/a/20260421A0200C00",
        "published_at": "2026-04-21T08:58:00+08:00",
        "score": 0.9806209206581116,
        "site_name": "腾讯网"
      }
    ]
  }
}
```

---

## 2. AI 搜索（流式）

### 请求

```
POST /openapi/ai_search
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

响应格式为 `text/event-stream`（SSE），答案和引用来源按事件逐块推送。

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 要提给 AI 的问题 |
| `count` | integer | 否 | 返回引用结果数，默认 `10`，最大 `50` |
| `time_range` | string | 否 | 时间范围过滤，可选值同通用搜索，默认 `month` |
| `filter` | object | 否 | 可选筛选对象 |
| `filter.domains` | string[] | 否 | 仅返回这些域名下的结果 |
| `filter.exclude_domains` | string[] | 否 | 从结果中排除这些域名 |

#### 请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://websearch.app.baizhi.cloud/openapi/ai_search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SEARCH_API_KEY}" \
  --no-buffer \
  -d '{
    "query": "天空为什么是蓝色的？",
    "count": 5
  }'
```

---

### 响应（SSE 事件流）

响应为标准 SSE 格式，每条消息由 `event:` 和 `data:` 两行组成，空行分隔。

#### 事件类型

| 事件名 | 触发时机 | 说明 |
|--------|---------|------|
| `start` | 流式响应开始 | 携带 `request_id`，表示服务端已接受请求 |
| `summary_delta` | AI 答案生成中 | 每次推送一个增量文本片段 `data.delta`，客户端需按序拼接 |
| `results` | 引用结果就绪 | 携带当前阶段可用的引用结果列表 |
| `done` | 搜索完成 | 携带完整答案 `data.summary_text`、最终结果列表及总耗时 `data.latency_ms` |
| `error` | 发生错误 | `data.error_message` 包含错误描述 |

#### 响应字段

| 字段 | 类型 | 出现事件 | 说明 |
|------|------|---------|------|
| `event` | string | 所有 | SSE 事件名 |
| `data.type` | string | 所有 | 事件类型，通常与 `event` 一致 |
| `data.request_id` | integer | 所有 | 本次 AI 搜索请求 ID |
| `data.delta` | string | `summary_delta` | 增量答案文本片段 |
| `data.results` | array | `results`、`done` | 引用结果列表，结构同通用搜索结果 |
| `data.summary_text` | string | `done` | 完整答案文本 |
| `data.latency_ms` | integer | `done` | 总耗时（毫秒） |
| `data.error_message` | string | `error` | 错误描述 |

#### 响应示例

```
event: start
data: {"type":"start","request_id":123456}

event: summary_delta
data: {"type":"summary_delta","request_id":123456,"delta":"天空之所以看起来是蓝色，"}

event: summary_delta
data: {"type":"summary_delta","request_id":123456,"delta":"主要是因为大气对短波长蓝光的瑞利散射更强。"}

event: results
data: {"type":"results","request_id":123456,"results":[{"rank":1,"title":"Rayleigh scattering","url":"https://example.com/rayleigh","site_name":"example.com"}]}

event: done
data: {"type":"done","request_id":123456,"latency_ms":532}
```

---

## 错误处理

当 `code != 0` 或出现 `error` 事件时表示请求失败。常见情况：

- **认证失败**：检查 `Authorization` Header 中的 API Key 是否正确。
- **参数错误**：检查必填字段 `query` 是否存在，`count` 是否在 1–50 范围内。
- **流式错误**：监听 `event: error` 事件，读取 `data.error_message` 获取具体原因。

---

## 使用建议

- **通用搜索**：适合将搜索结果作为上下文注入 LLM Prompt，或自行实现结果排序、过滤逻辑。
- **AI 搜索**：适合直接面向用户展示答案，流式输出可提升体验；客户端需按顺序拼接所有 `summary_delta` 片段才能得到完整答案。
- **域名过滤**：`filter.domains` 和 `filter.exclude_domains` 可同时使用，精确控制来源可信度。
- **时间范围**：实时性要求高时使用 `time_range: "day"`；综合性查询可使用默认的 `month`。
