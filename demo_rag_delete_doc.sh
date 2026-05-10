#!/bin/bash

source .env

curl -SL --fail-with-body -X DELETE "https://ragcloud.app.baizhi.cloud/openapi/v1/documents/${RAG_DOCUMENT_ID}" \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}"

:<<'EXAMPLE_RESPONSE'
{
    "document_id": "doc_abc123",
    "status": "deleting"
}
EXAMPLE_RESPONSE
