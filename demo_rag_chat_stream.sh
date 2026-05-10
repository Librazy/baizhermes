#!/bin/bash

source .env

curl -N -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/chat/stream \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}" \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "如何创建知识库？",
    "top_k": 10
  }'

:<<'EXAMPLE_RESPONSE'
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
EXAMPLE_RESPONSE
