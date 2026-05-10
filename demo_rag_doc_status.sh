#!/bin/bash

source .env

curl -SL --fail-with-body -X GET "https://ragcloud.app.baizhi.cloud/openapi/v1/documents/${RAG_DOCUMENT_ID}/status" \
  -H "Authorization: Bearer ${BAIZHI_RAG_API_KEY}"

:<<'EXAMPLE_RESPONSE'
{
    "status": "ready"
}
EXAMPLE_RESPONSE
