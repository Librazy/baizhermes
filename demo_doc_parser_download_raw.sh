#!/bin/bash

source .env

# Download original document
# Requires: DOC_PARSER_DOCUMENT_ID and DOC_PARSER_OBJECT_KEY environment variables
curl -vSL --fail-with-body -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}/proxy/${DOC_PARSER_OBJECT_KEY}" \
  -H "Authorization: Bearer ${BAIZHI_DOC_PARSER_API_KEY}" \
  -o $(basename $DOC_PARSER_OBJECT_KEY)

:<<'EXAMPLE_RESPONSE'
# Binary file stream saved to document.pdf
# Response headers:
# Content-Type: application/pdf
# Content-Length: 1048576
# Content-Disposition: inline; filename=beeparser/1234567890/deadbeef-dead-beef-babe-cafebabecafe/document.pdf
EXAMPLE_RESPONSE
