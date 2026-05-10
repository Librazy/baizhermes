"""Baizhi.Cloud RAG and document parser handlers for Hermes."""

import base64
import json
import os
import uuid
from typing import Any
from urllib import error, parse, request


_RAG_BASE_URL = "https://ragcloud.app.baizhi.cloud/openapi/v1"
_DOC_BASE_URL = "https://beeparser.app.baizhi.cloud/openapi/v1"
_RAG_API_KEY_ENV = "BAIZHI_RAG_API_KEY"
_DOC_API_KEY_ENV = "BAIZHI_DOC_PARSER_API_KEY"


def has_rag_api_key() -> bool:
    return bool(os.getenv(_RAG_API_KEY_ENV))


def has_doc_parser_api_key() -> bool:
    return bool(os.getenv(_DOC_API_KEY_ENV))


def _error(message: str) -> str:
    return json.dumps({"error": message}, ensure_ascii=False)


def _parse_http_error(exc: error.HTTPError) -> str:
    try:
        body = exc.read().decode("utf-8", errors="replace")
    except Exception:
        body = exc.reason or ""
    detail = body.strip() or str(exc.reason)
    return f"Baizhi API request failed with status {exc.code}: {detail}"


def _json_request(
    *,
    base_url: str,
    path: str,
    payload: dict[str, Any] | None,
    api_key_env: str,
    method: str,
    accept: str = "application/json",
) -> request.Request:
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise RuntimeError(f"{api_key_env} not configured")

    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": accept,
    }
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"

    return request.Request(
        url=f"{base_url}{path}",
        data=data,
        headers=headers,
        method=method,
    )


def _require_str(args: dict[str, Any], key: str) -> str | None:
    value = str(args.get(key, "")).strip()
    return value or None


def baizhi_rag_create_document(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    title = _require_str(args, "title")
    content = _require_str(args, "content")
    if not title or not content:
        return _error("title and content are required")

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path="/documents/text",
            payload={"title": title, "content": content},
            api_key_env=_RAG_API_KEY_ENV,
            method="POST",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG create document failed: {exc}")


def baizhi_rag_update_document(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    document_id = _require_str(args, "document_id")
    title = _require_str(args, "title")
    content = _require_str(args, "content")
    if not document_id or not title or not content:
        return _error("document_id, title and content are required")

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path=f"/documents/{parse.quote(document_id, safe='')}/text",
            payload={"title": title, "content": content},
            api_key_env=_RAG_API_KEY_ENV,
            method="PUT",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG update document failed: {exc}")


def baizhi_rag_delete_document(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    document_id = _require_str(args, "document_id")
    if not document_id:
        return _error("document_id is required")

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path=f"/documents/{parse.quote(document_id, safe='')}",
            payload=None,
            api_key_env=_RAG_API_KEY_ENV,
            method="DELETE",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG delete document failed: {exc}")


def baizhi_rag_get_document_status(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    document_id = _require_str(args, "document_id")
    if not document_id:
        return _error("document_id is required")

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path=f"/documents/{parse.quote(document_id, safe='')}/status",
            payload=None,
            api_key_env=_RAG_API_KEY_ENV,
            method="GET",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG get document status failed: {exc}")


def baizhi_rag_retrieve(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    query = _require_str(args, "query")
    if not query:
        return _error("query is required")

    payload: dict[str, Any] = {"query": query}
    for key in ("top_k", "score_threshold", "group_by_document", "include_score_detail"):
        if key in args and args[key] is not None:
            payload[key] = args[key]

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path="/retrieve",
            payload=payload,
            api_key_env=_RAG_API_KEY_ENV,
            method="POST",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG retrieve failed: {exc}")


def baizhi_rag_chat_stream(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_rag_api_key():
        return _error(f"{_RAG_API_KEY_ENV} not configured")

    query = _require_str(args, "query")
    if not query:
        return _error("query is required")

    payload: dict[str, Any] = {"query": query}
    if args.get("top_k") is not None:
        payload["top_k"] = args["top_k"]

    answer_parts: list[str] = []
    retrieval_items: list[dict[str, Any]] = []
    citations: list[dict[str, Any]] = []
    final_answer = ""

    try:
        req = _json_request(
            base_url=_RAG_BASE_URL,
            path="/chat/stream",
            payload=payload,
            api_key_env=_RAG_API_KEY_ENV,
            method="POST",
            accept="text/event-stream",
        )
        with request.urlopen(req, timeout=60) as response:
            current_event = None
            data_lines: list[str] = []
            for raw_line in response:
                line = raw_line.decode("utf-8", errors="replace").rstrip("\r\n")
                if not line:
                    if not data_lines:
                        current_event = None
                        continue
                    payload_obj = json.loads("\n".join(data_lines))
                    event_name = current_event or payload_obj.get("type")

                    if event_name == "retrieval_done":
                        retrieval_items = payload_obj.get("items", [])
                    elif event_name == "delta":
                        answer_parts.append(payload_obj.get("content", ""))
                    elif event_name == "citations":
                        if isinstance(payload_obj, list):
                            citations = payload_obj
                        else:
                            citations = payload_obj.get("citations", [])
                    elif event_name == "done":
                        final_answer = payload_obj.get("answer", "")

                    current_event = None
                    data_lines = []
                    continue

                if line.startswith(":"):
                    continue
                if line.startswith("event:"):
                    current_event = line.partition(":")[2].strip()
                    continue
                if line.startswith("data:"):
                    data_lines.append(line.partition(":")[2].lstrip())
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi RAG chat stream failed: {exc}")

    return json.dumps(
        {
            "answer": final_answer or "".join(answer_parts),
            "retrieval_items": retrieval_items,
            "citations": citations,
        },
        ensure_ascii=False,
    )


def _download_file(url: str) -> tuple[bytes, str]:
    req = request.Request(url=url, method="GET")
    with request.urlopen(req, timeout=60) as resp:
        content_type = resp.headers.get("Content-Type") or "application/octet-stream"
        return resp.read(), content_type


def _build_multipart_body(field_name: str, filename: str, file_data: bytes, content_type: str) -> tuple[bytes, str]:
    boundary = f"----HermesBoundary{uuid.uuid4().hex}"
    chunks = [
        f"--{boundary}\r\n".encode("utf-8"),
        (
            f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
        ).encode("utf-8"),
        f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"),
        file_data,
        b"\r\n",
        f"--{boundary}--\r\n".encode("utf-8"),
    ]
    return b"".join(chunks), boundary


def baizhi_doc_parser_upload(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_doc_parser_api_key():
        return _error(f"{_DOC_API_KEY_ENV} not configured")

    file_url = _require_str(args, "file_url")
    filename = _require_str(args, "filename")
    if not file_url:
        return _error("file_url is required")

    try:
        file_data, content_type = _download_file(file_url)
    except Exception as exc:
        return _error(f"Failed to download file_url: {exc}")

    if not filename:
        url_path = parse.urlparse(file_url).path
        filename = (url_path.rsplit("/", 1)[-1] or "document.bin").strip()

    body, boundary = _build_multipart_body("file", filename, file_data, content_type)
    api_key = os.getenv(_DOC_API_KEY_ENV)

    try:
        req = request.Request(
            url=f"{_DOC_BASE_URL}/documents",
            data=body,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Accept": "application/json",
            },
            method="POST",
        )
        with request.urlopen(req, timeout=60) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi doc parser upload failed: {exc}")


def baizhi_doc_parser_get_document(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_doc_parser_api_key():
        return _error(f"{_DOC_API_KEY_ENV} not configured")

    document_id = args.get("document_id")
    if document_id is None:
        return _error("document_id is required")

    try:
        req = _json_request(
            base_url=_DOC_BASE_URL,
            path=f"/documents/{document_id}",
            payload=None,
            api_key_env=_DOC_API_KEY_ENV,
            method="GET",
        )
        with request.urlopen(req, timeout=30) as resp:
            return json.dumps(json.loads(resp.read().decode("utf-8")), ensure_ascii=False)
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi doc parser get document failed: {exc}")


def baizhi_doc_parser_download(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    if not has_doc_parser_api_key():
        return _error(f"{_DOC_API_KEY_ENV} not configured")

    document_id = args.get("document_id")
    key = _require_str(args, "key")
    if document_id is None or not key:
        return _error("document_id and key are required")

    api_key = os.getenv(_DOC_API_KEY_ENV)
    quoted_key = parse.quote(key, safe="/")
    try:
        req = request.Request(
            url=f"{_DOC_BASE_URL}/documents/{document_id}/proxy/{quoted_key}",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "*/*",
            },
            method="GET",
        )
        with request.urlopen(req, timeout=60) as resp:
            binary = resp.read()
            content_type = resp.headers.get("Content-Type") or "application/octet-stream"

        if content_type.startswith("text/") or key.endswith((".md", ".txt", ".json")):
            try:
                return json.dumps(
                    {
                        "content_type": content_type,
                        "text": binary.decode("utf-8"),
                    },
                    ensure_ascii=False,
                )
            except Exception:
                pass

        return json.dumps(
            {
                "content_type": content_type,
                "base64": base64.b64encode(binary).decode("ascii"),
            },
            ensure_ascii=False,
        )
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi doc parser download failed: {exc}")
