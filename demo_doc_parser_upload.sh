#!/bin/bash

source .env

# Note: Replace /path/to/document.pdf with your actual file path
curl -SL --fail-with-body -X POST https://beeparser.app.baizhi.cloud/openapi/v1/documents \
  -H "Authorization: Bearer ${BAIZHI_DOC_PARSER_API_KEY}" \
  -F "file=@/path/to/document.pdf"

:<<'EXAMPLE_RESPONSE'
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
EXAMPLE_RESPONSE
