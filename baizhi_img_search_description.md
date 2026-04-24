# Baizhi Image Search API 文档

## 概述

Baizhi Image Search 提供图片搜索 OpenAPI 接口，适合以下场景：

- 根据关键词检索图片素材
- 在检索时按宽高范围做基础过滤
- 获取图片 URL、宽度、高度等元数据，供前端直接展示

## 基本信息

**Base URL**

```text
https://imgsearch.app.baizhi.cloud
```

**接口**

```text
POST /openapi/search
```

**认证**

所有请求都需要在 Header 中携带 API Key：

```text
Authorization: Bearer <BAIZHI_IMG_SEARCH_API_KEY>
```

完整请求头示例：

```text
Content-Type: application/json
Authorization: Bearer <BAIZHI_IMG_SEARCH_API_KEY>
```

## 请求说明

### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | 是 | 图片搜索关键词 |
| `count` | integer | 否 | 返回图片结果数，默认 `5`，最大 `5` |
| `image` | object | 否 | 图片搜索专用筛选参数对象 |
| `image.width_min` | integer | 否 | 最小图片宽度 |
| `image.height_min` | integer | 否 | 最小图片高度 |
| `image.width_max` | integer | 否 | 最大图片宽度 |
| `image.height_max` | integer | 否 | 最大图片高度 |

### 参数使用建议

- `query` 建议使用明确的名词短语，例如“国家会展中心”“布偶猫 正脸”“城市夜景”。
- `count` 当前最多只支持返回 `5` 条，传入更大值时应预期服务端会做限制。
- `image` 过滤适合做基础尺寸筛选，例如只要横图、只要大图，或排除过小图片。
- 若同时设置最小和最大宽高，请确保区间合理，否则可能导致无结果。

### 最简单的请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://imgsearch.app.baizhi.cloud/openapi/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_IMG_SEARCH_API_KEY}" \
  -d '{
    "query": "国家会展中心",
    "count": 5
  }'
```

### 带尺寸过滤的请求示例

```bash
curl -SL --fail-with-body -X POST \
  https://imgsearch.app.baizhi.cloud/openapi/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_IMG_SEARCH_API_KEY}" \
  -d '{
    "query": "雪山 风景",
    "count": 5,
    "image": {
      "width_min": 1200,
      "height_min": 800,
      "width_max": 3000,
      "height_max": 2000
    }
  }'
```

## 响应说明

### 顶层字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | integer | 状态码，`0` 表示成功 |
| `message` | string | 状态描述，成功时固定为 `success` |
| `trace_id` | string | 请求链路追踪 ID |
| `data.request_id` | integer | 本次搜索请求 ID |
| `data.results` | array | 图片搜索结果列表 |

### 结果字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.results[].title` | string | 搜索结果标题 |
| `data.results[].url` | string | 图片搜索下该字段固定为空字符串，不应再用于跳转 |
| `data.results[].image` | object | 图片元数据对象 |
| `data.results[].image.url` | string | 图片地址，前端展示图片时应优先使用这个字段 |
| `data.results[].image.width` | integer | 图片宽度 |
| `data.results[].image.height` | integer | 图片高度 |

### 响应示例

```json
{
  "code": 0,
  "message": "success",
  "trace_id": "trace_123456",
  "data": {
    "request_id": 123456,
    "results": [
      {
        "rank": 1,
        "title": "Cat Photo",
        "url": "",
        "image": {
          "url": "https://img.example.com/cat.jpg",
          "width": 1024,
          "height": 1024
        }
      }
    ]
  }
}
```

## 客户端接入要点

- 展示图片时，请读取 `data.results[].image.url`，不要使用 `data.results[].url`。
- 如果需要做瀑布流、宫格布局或懒加载，建议同时读取 `image.width` 和 `image.height`，提前计算图片比例。
- `trace_id` 适合用于排查线上问题，客户端记录失败日志时建议一并带上。
- 响应示例中出现了 `rank` 字段，可用于表示结果排序；如果业务依赖该字段，建议以前后端联调实际返回为准。

## 错误处理

当 `code != 0` 时表示请求失败。常见排查方向包括：

- API Key 缺失或无效，导致认证失败
- `query` 为空或格式不合法
- `count` 超出服务支持范围
- `image` 中的宽高条件互相冲突，导致结果为空

建议客户端在失败时至少记录以下信息：

- 请求参数中的 `query`
- 服务端返回的 `message`
- 服务端返回的 `trace_id`

## 适用场景建议

- **前端图片搜索面板**：直接用 `image.url` 展示缩略图或原图预览
- **素材筛选**：结合 `width_min`、`height_min` 过滤小图
- **多模态流程前置检索**：先取图片列表，再将图片 URL 或元数据传给后续模型或业务流程
