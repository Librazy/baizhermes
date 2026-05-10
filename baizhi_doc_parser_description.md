# Baizhi Document Parser API 文档

## 概述

Baizhi Document Parser 支持将多种格式的文档解析为 Markdown 文件。
API 提供文档上传、解析状态查询和下载功能，适合以下场景：

- 上传文档（PDF、Word、PPT 等）进入解析队列
- 查询文档解析状态和元数据
- 下载原始文档或解析后的 Markdown 文件

## 基本信息

**Base URL**

```text
https://beeparser.app.baizhi.cloud/openapi/v1
```

**认证**

所有请求都需要在 Header 中携带 API Key：

```text
Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>
```

完整请求头示例：

```text
Content-Type: multipart/form-data
Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>
```

---

## 1. 文档上传

上传文档文件并进入解析队列。

### 请求

```
POST https://beeparser.app.baizhi.cloud/openapi/v1/documents
Content-Type: multipart/form-data
Authorization: Bearer <API_KEY>
```

### 请求体参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `file` | File | 是 | 要上传的文档文件 |

### 请求示例

```bash
curl -X POST https://beeparser.app.baizhi.cloud/openapi/v1/documents \
  -H "Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>" \
  -F "file=@/path/to/document.pdf"
```

### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | integer | 状态码，`0` 表示成功 |
| `data.ID` | uint64 | 文档唯一标识 ID |
| `data.OriginalName` | string | 原始文件名 |
| `data.ObjectKey` | string | 存储对象键 |
| `data.PreviewKeys` | string | 预览文件键（逗号分隔） |
| `data.MimeType` | string | 文件 MIME 类型 |
| `data.SizeBytes` | int64 | 文件大小（字节） |
| `data.PageCount` | int | 文档页数 |
| `data.Status` | string | 文档状态：`uploaded`（已上传）、`parsing`（解析中）、`parsed`（已解析）、`failed`（失败） |
| `data.Source` | string | 文档来源 |
| `data.ResultKeys` | string | 解析结果文件键 |
| `data.ErrorMessage` | string | 错误信息（解析失败时） |
| `data.CreatedAt` | time | 创建时间 |
| `data.UpdatedAt` | time | 更新时间 |

### 响应示例

```json
{
  "code": 0,
  "data": {
    "ID": 415,
    "OriginalName": "DeepSeek_V4.pdf",
    "ObjectKey": "beeparser/1234567890/deadbeef-dead-beef-babe-cafebabecafe/document.pdf",
    "PreviewKeys": "",
    "MimeType": "application/pdf",
    "SizeBytes": 4479901,
    "PageCount": 58,
    "Status": "uploaded",
    "Source": "api",
    "ResultKeys": "",
    "ErrorMessage": "",
    "CreatedAt": "2026-04-27T13:48:59.284591256+08:00",
    "UpdatedAt": "2026-04-27T13:48:59.284591256+08:00"
  }
}
```

### 错误响应

| HTTP 状态码 | 错误码 | 说明 |
|-------------|--------|------|
| 400 | 1002 | 缺少文件 |
| 500 | 1003 | 无法打开文件 |
| 400 | 1004 | 超出月配额限制 |
| 400 | 1004 | 不支持的文档类型 |
| 500 | 1004 | 其他错误 |

---

## 2. 文档详情

获取文档的详细信息和解析状态。

### 请求

```
GET https://beeparser.app.baizhi.cloud/openapi/v1/documents/{id}
Authorization: Bearer <API_KEY>
```

### 路径参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | uint64 | 是 | 文档 ID |

### 请求示例

```bash
export DOC_PARSER_DOCUMENT_ID=$(echo $RESULT_FROM_UPLOAD_API | jq -r '.data.ID')

curl -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}" \
  -H "Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>"
```

### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | integer | 状态码，`0` 表示成功 |
| `data.document` | object | 文档对象，字段同上传响应中的 `data` |

### 响应示例

```json
{
  "code": 0,
  "data": {
    "document": {
      "ID": 415,
      "OriginalName": "DeepSeek_V4.pdf",
      "ObjectKey": "beeparser/1234567890/deadbeef-dead-beef-babe-cafebabecafe/document.pdf",
      "PreviewKeys": "",
      "MimeType": "application/pdf",
      "SizeBytes": 4479901,
      "PageCount": 58,
      "Status": "parsed",
      "Source": "api",
      "ResultKeys": "beeparser/123456790/deadbeef-dead-beef-babe-cafebabecafe/converted/document.md",
      "ErrorMessage": "",
      "CreatedAt": "2026-04-27T13:48:59.284591+08:00",
      "UpdatedAt": "2026-04-27T13:49:11.864925+08:00"
    }
  }
}
```

### 错误响应

| HTTP 状态码 | 错误码 | 说明 |
|-------------|--------|------|
| 400 | 1005 | 无效的 ID |
| 403 | 1006 | 无权访问该文档 |
| 404 | 1010 | 文档不存在 |
| 500 | 1007 | 服务器错误 |

---

## 3. 文档下载

下载原始文档或解析后的文件。

### 请求

```
GET https://beeparser.app.baizhi.cloud/openapi/v1/documents/{id}/proxy/{*key}
Authorization: Bearer <API_KEY>
```

### 路径参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | uint64 | 是 | 文档 ID |
| `key` | string | 是 | 文件键（支持通配路径） |

### 请求示例

```bash
export DOC_PARSER_DOCUMENT_ID=$(echo $RESULT_FROM_UPLOAD_API | jq -r '.data.ID')
export DOC_PARSER_OBJECT_KEY=$(echo $RESULT_FROM_UPLOAD_API | jq -r '.data.ObjectKey')
export DOC_PARSER_RESULT_KEY=$(echo $RESULT_FROM_DETAIL_API | jq -r '.data.document.ResultKeys')

# 下载原始文件
curl -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}/proxy/${DOC_PARSER_OBJECT_KEY}" \
  -H "Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>" \
  -o document.pdf

# 下载解析完成的文件
curl -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}/proxy/${DOC_PARSER_RESULT_KEY}" \
  -H "Authorization: Bearer <BAIZHI_DOC_PARSER_API_KEY>" \
  -o document.md
```

### 响应头

| 头字段 | 说明 |
|--------|------|
| `Content-Type` | 文件 MIME 类型 |
| `Content-Length` | 文件大小 |
| `Content-Disposition` | 文件名信息 |

### 响应体

二进制文件流。

### 错误响应

| HTTP 状态码 | 错误码 | 说明 |
|-------------|--------|------|
| 400 | 1100 | 缺少文档 ID |
| 400 | 1100 | 无效的文档 ID |
| 400 | 1101 | 缺少文件键 |
| 403 | 1102 | 无权访问该文件 |
| 404 | 1104 | 文档不存在 |
| 500 | 1103 | 服务器错误 |

---

## 文档状态说明

| 状态 | 说明 |
|------|------|
| `uploaded` | 文档已上传，等待进入解析队列 |
| `parsing` | 文档正在解析中 |
| `parsed` | 文档解析完成，可以获取解析结果 |
| `failed` | 文档解析失败，可通过 `ErrorMessage` 查看原因 |

---

## 错误处理

当 `code != 0` 或 HTTP 状态码非 200 时表示请求失败。常见排查方向：

- **认证失败**：检查 `Authorization` Header 中的 API Key 是否正确
- **文档不存在**：检查文档 ID 是否有效
- **无权访问**：确认 API Key 有权限访问该文档
- **超出配额**：检查账户的月度上传配额
- **不支持的类型**：确认上传的文件格式受支持（PDF、Word、PPT 等）

建议客户端在失败时记录以下信息：

- 请求参数
- HTTP 状态码
- 错误码和错误信息

---

## 使用建议

- **上传后轮询状态**：建议上传后定期调用文档详情接口，等待 `Status` 变为 `parsed` 后再使用解析结果
- **预览文件使用**：`PreviewKeys` 包含文档各页的预览图片，可用于前端展示缩略图
- **解析结果获取**：`ResultKeys` 包含解析后的结构化数据文件路径，可通过下载接口获取
- **错误处理**：当 `Status` 为 `failed` 时，根据 `ErrorMessage` 进行相应处理
