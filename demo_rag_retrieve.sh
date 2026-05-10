#!/bin/bash

source .env

curl -SL --fail-with-body -X POST https://ragcloud.app.baizhi.cloud/openapi/v1/retrieve \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "权限管理",
    "top_k": 10,
    "score_threshold": 0.5,
    "group_by_document": false,
    "include_score_detail": true
  }'

:<<'EXAMPLE_RESPONSE'
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
EXAMPLE_RESPONSE
