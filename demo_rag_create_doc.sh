#!/bin/bash

source .env

curl -SL --fail-with-body -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/documents/text \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "产品手册",
    "content": "这里是文档正文（Markdown 或纯文本）"
  }'

:<<'EXAMPLE_RESPONSE'
{
    "document_id": "doc_abc123",
    "status": "uploaded"
}
EXAMPLE_RESPONSE
