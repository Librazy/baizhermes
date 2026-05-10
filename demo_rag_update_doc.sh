#!/bin/bash

source .env

curl -SL --fail-with-body -X PUT "https://ragcloud.app.baizhi.cloud/openapi/v1/documents/${RAG_DOCUMENT_ID}/text" \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "更新后的标题",
    "content": "更新后的文档内容"
  }'

:<<'EXAMPLE_RESPONSE'
{
    "document_id": "doc_abc123",
    "status": "uploaded"
}
EXAMPLE_RESPONSE
