# Baizhi News Search API 文档

## 概述

Baizhi News Search 提供面向新闻场景的 OpenAPI 检索接口，支持关键词或自然语言查询、时效过滤、域名白名单/黑名单，以及可选的 AI 总结。

| 接口 | 适用场景 |
|------|---------|
| 新闻搜索 `POST /openapi/v1/news/search` | 返回新闻列表及摘要，可选 AI 总结，适合舆情、资讯聚合或注入 LLM 上下文 |

**Base URL**

```
https://newssearch.app.baizhi.cloud/openapi/v1
```

**认证**

所有请求均需在 Header 中携带 API Key：

```
Authorization: Bearer <BAIZHI_NEWS_SEARCH_API_KEY>
```

---

## 1. 新闻搜索

### 请求

```
POST /openapi/v1/news/search
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

完整 URL：`https://newssearch.app.baizhi.cloud/openapi/v1/news/search`

#### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 新闻关键词或自然语言问题 |
| `time_range` | string | 否 | 新闻时效过滤，可选值见下表 |
| `max_results` | integer | 否 | 返回条数，范围 `1`–`20` |
| `include_answer` | boolean | 否 | 是否返回 AI 总结 |
| `include_domains` | string[] | 否 | 仅检索指定域名，最多 `300` 个 |
| `exclude_domains` | string[] | 否 | 排除指定域名，最多 `150` 个 |

**`time_range` 可选值**

| 值 | 含义 |
|----|------|
| `day` | 最近一天 |
| `week` | 最近一周 |
| `month` | 最近一月 |
| `year` | 最近一年 |

#### 请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://newssearch.app.baizhi.cloud/openapi/v1/news/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_NEWS_SEARCH_API_KEY}" \
  -d '{
    "query": "低空经济 地方政策",
    "time_range": "week",
    "max_results": 5,
    "include_answer": true,
    "include_domains": [],
    "exclude_domains": []
  }'
```

仅指定域名：

```bash
curl -SL --fail-with-body -X POST \
  https://newssearch.app.baizhi.cloud/openapi/v1/news/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_NEWS_SEARCH_API_KEY}" \
  -d '{
    "query": "大模型最新进展",
    "time_range": "month",
    "max_results": 10,
    "include_domains": ["36kr.com", "wallstreetcn.com"],
    "exclude_domains": ["spam.example.com"]
  }'
```

---

### 响应

#### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `request_id` | string | 请求 ID |
| `data.query` | string | 本次检索使用的查询内容 |
| `data.answer` | string | 可选；当 `include_answer` 为 true 时返回 AI 总结 |
| `data.results` | array | 新闻搜索结果列表 |
| `data.results[].rank` | integer | 结果排序，从 `1` 开始 |
| `data.results[].title` | string | 新闻标题 |
| `data.results[].url` | string | 新闻原文链接 |
| `data.results[].summary` | string | 新闻摘要或正文片段 |
| `data.results[].score` | number | 搜索相关性评分 |
| `data.results[].published_at` | string \| null | 发布时间；上游未返回时为 `null` |
| `data.response_time` | number | 上游搜索耗时，单位秒 |
| `data.points_cost` | integer | 本次业务积分消耗 |
| `error` | object \| null | 错误信息；成功时通常为 `null` |

#### 响应示例

```json
{
  "request_id": "req_...",
  "data": {
    "query": "低空经济 地方政策",
    "answer": "近期多地继续发布低空经济扶持政策，覆盖基础设施、应用场景和产业基金。",
    "results": [
      {
        "rank": 1,
        "title": "多地出台低空经济产业支持政策",
        "url": "https://example.com/news/low-altitude-economy",
        "summary": "地方政府围绕低空经济基础设施建设、飞行服务和场景开放推出支持措施。",
        "score": 0.91,
        "published_at": "2026-05-08"
      }
    ],
    "response_time": 0.82,
    "points_cost": 20
  },
  "error": null
}
```

---

## 错误处理

当响应中出现非空的 `error` 字段，或 HTTP 状态码非 2xx 时表示请求失败。常见情况：

- **认证失败**：检查 `Authorization` Header 中的 API Key 是否正确。
- **参数错误**：确认必填字段 `query` 存在；`max_results` 是否在 `1`–`20`；域名数组长度是否超出上限。

---

## 使用建议

- **时效性**：强时效查询使用 `time_range: "day"` 或 `"week"`；回顾性分析可使用 `"month"` 或 `"year"`。
- **AI 总结**：需要一句话摘要或可直接展示的概述时，设置 `include_answer: true`。
- **来源控制**：`include_domains` 与 `exclude_domains` 可同时使用，用于限定权威媒体或剔除噪音站点。
- **成本**：关注响应中的 `data.points_cost`，便于与配额或计费策略对齐。
