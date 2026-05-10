#!/bin/bash

source .env

curl -SL --fail-with-body -X GET "https://beeparser.app.baizhi.cloud/openapi/v1/documents/${DOC_PARSER_DOCUMENT_ID}" \
  -H "Authorization: Bearer ${BAIZHI_DOC_PARSER_API_KEY}"

:<<'EXAMPLE_RESPONSE'
{
    "code": 0,
    "data": {
        "document": {
            "ID": 415,
            "OriginalName": "DeepSeek_V4.pdf",
            "ObjectKey": "beeparser/115088741965893/1ffd75d6-bca9-484b-a2fc-62e07bfa8957/document.pdf",
            "PreviewKeys": "",
            "MimeType": "application/pdf",
            "SizeBytes": 4479901,
            "PageCount": 58,
            "Status": "parsed",
            "Source": "api",
            "ResultKeys": "beeparser/115088741965893/1ffd75d6-bca9-484b-a2fc-62e07bfa8957/converted/document.md",
            "ErrorMessage": "",
            "CreatedAt": "2026-04-27T13:48:59.284591+08:00",
            "UpdatedAt": "2026-04-27T13:49:11.864925+08:00"
        }
    }
}
EXAMPLE_RESPONSE
