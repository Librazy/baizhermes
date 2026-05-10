#!/bin/bash

source .env

DOC_PARSER_MD_KEY="$(dirname $DOC_PARSER_OBJECT_KEY)/converted/document.md"

# Download original document
# Requires: DOC_PARSER_DOCUMENT_ID and DOC_PARSER_OBJECT_KEY environment variables
curl -vSL --fail-with-body -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}/proxy/${DOC_PARSER_MD_KEY}" \
  -H "Authorization: Bearer ${BAIZHI_DOC_PARSER_API_KEY}" \
  -o downloaded_document.md

:<<'EXAMPLE_RESPONSE'
# Binary file stream saved to downloaded_document.md
# Response headers:
# Content-Type: text/markdown
# Content-Length: 1048576
# Content-Disposition: inline; filename=beeparser/1234567890/deadbeef-dead-beef-babe-cafebabecafe/converted/document.md
EXAMPLE_RESPONSE
