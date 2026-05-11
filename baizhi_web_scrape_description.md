# Baizhi Web Scrape API 文档

## 概述

Baizhi Web Scrape 提供网页抓取 OpenAPI 接口，将指定 URL 的页面解析为 Markdown，适合以下场景：

- 将公开网页正文转为 Markdown，供 LLM 或下游流程消费
- 快速获取页面结构化文本，避免手写爬虫解析 HTML
- 需要同时拿到原始地址与内容字符数，便于日志与计费统计

## 基本信息

**Base URL**

```text
https://web-scrape.app.baizhi.cloud
```

**接口**

```text
POST /openapi/scrape
```

**认证**

所有请求都需要在 Header 中携带 API Key：

```text
Authorization: Bearer <BAIZHI_WEB_SCRAPE_API_KEY>
```

完整请求头示例：

```text
Content-Type: application/json
Authorization: Bearer <BAIZHI_WEB_SCRAPE_API_KEY>
```

## 请求说明

### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `url` | string | 是 | 需要抓取的 `http` 或 `https` 网页地址 |

### 参数使用建议

- `url` 请使用完整 URL（含协议），例如 `https://example.com/path`。
- 目标站点若需要登录、强反爬或动态渲染-only 内容，返回质量取决于服务端实现，建议联调验证。
- 请在合规前提下调用，勿抓取未授权或禁止爬取的资源。

### 请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://web-scrape.app.baizhi.cloud/openapi/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SCRAPE_API_KEY}" \
  -d '{
    "url": "https://example.com"
  }'
```

## 响应说明

### 顶层字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | integer | 状态码，`0` 表示成功 |
| `message` | string | 状态描述；成功时可能为空字符串，具体以前后端联调为准 |
| `data` | object | 业务数据（成功时存在） |

### `data` 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.content` | string | 网页解析后的 Markdown 内容 |
| `data.source_url` | string | 本次抓取的原始网页地址 |
| `data.characters` | number | 返回内容字符数 |

### 响应示例

```json
{
  "code": 0,
  "message": "",
  "data": {
    "content": "# Example Domain\n...",
    "source_url": "https://example.com",
    "characters": 128
  }
}
```

## 客户端接入要点

- 正文请读取 `data.content`（Markdown），按需再做清洗或分块。
- `data.source_url` 可与请求中的 `url` 对照，确认重定向或规范化后的最终来源。
- `data.characters` 可用于粗略估算长度限制或配额。

## 错误处理

当 `code != 0` 时表示请求失败。常见排查方向包括：

- API Key 缺失或无效，导致认证失败
- `url` 为空、非 http(s)，或目标不可达
- 目标站点返回异常或被服务端拒绝抓取

建议客户端在失败时至少记录：

- 请求体中的 `url`
- 服务端返回的 `message`
- 服务端返回的 `code`

## 适用场景建议

- **RAG / 问答**：抓取文档页、博客正文后切块入库
- **摘要与抽取**：先 Markdown 化再交给模型处理
- **合规采集**：仅对允许抓取的公开页面使用，并遵守 robots 与站点条款
