"""Baizhi.Cloud RAG and document parser handlers for Hermes."""

import base64
import json
import os
import uuid
from typing import Any
from urllib import error, parse, request


_RAG_BASE_URL = "https://ragcloud.app.baizhi.cloud/openapi/v1"
_MCP_BASE_URL = "https://beeparser.app.baizhi.cloud/mcp"
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


def _mcp_request(method: str, params: dict[str, Any] | None = None, session_id: str | None = None) -> tuple[dict, str | None]:
    """Make an MCP JSON-RPC request. Returns (response_body, new_session_id)."""
    api_key = os.getenv(_DOC_API_KEY_ENV)
    if not api_key:
        raise RuntimeError(f"{_DOC_API_KEY_ENV} not configured")

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {},
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if session_id:
        headers["Mcp-Session-Id"] = session_id

    req = request.Request(url=_MCP_BASE_URL, data=data, headers=headers, method="POST")
    with request.urlopen(req, timeout=30) as resp:
        new_sid = resp.headers.get("Mcp-Session-Id")
        body = json.loads(resp.read().decode("utf-8"))
        return body, new_sid


def _mcp_call_tool(tool_name: str, arguments: dict[str, Any], session_id: str) -> dict:
    """Call an MCP tool and return the structured content."""
    payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments,
        },
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    req = request.Request(
        url=_MCP_BASE_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {os.getenv(_DOC_API_KEY_ENV)}",
            "Content-Type": "application/json",
            "Mcp-Session-Id": session_id,
        },
        method="POST",
    )
    with request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        return body.get("result", {})


def _mcp_init_session() -> str:
    """Initialize an MCP session and return the session ID."""
    _, session_id = _mcp_request("initialize", {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "hermes-baizhi-plugin", "version": "1.0.0"},
    })
    if not session_id:
        raise RuntimeError("MCP initialize response missing Mcp-Session-Id header")

    # Send initialized notification
    _mcp_request("notifications/initialized", {}, session_id=session_id)
    return session_id


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
                        answer_parts.append(payload_obj.get("text", ""))
                    elif event_name == "citations":
                        if isinstance(payload_obj, list):
                            citations = payload_obj
                        else:
                            citations = payload_obj.get("citations", [])
                    elif event_name == "done":
                        # done event only signals completion; answer is accumulated from deltas
                        pass

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
            "answer": "".join(answer_parts),
            "retrieval_items": retrieval_items,
            "citations": citations,
        },
        ensure_ascii=False,
    )


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
    file_path = _require_str(args, "file_path")
    filename = _require_str(args, "filename")

    if not file_url and not file_path:
        return _error("file_url or file_path is required")

    if file_url:
        # Remote URL: use MCP docparse_parse (server-side fetch, no local download)
        try:
            session_id = _mcp_init_session()
            result = _mcp_call_tool("docparse_parse", {"url": file_url}, session_id)
            structured = result.get("structuredContent", {})
            return json.dumps({
                "document_id": structured.get("document_id"),
                "filename": structured.get("filename"),
                "status": structured.get("status"),
                "source": "mcp",
            }, ensure_ascii=False)
        except error.HTTPError as exc:
            return _error(_parse_http_error(exc))
        except error.URLError as exc:
            return _error(f"MCP network error: {exc.reason}")
        except Exception as exc:
            return _error(f"MCP docparse_parse failed: {exc}")

    # Local file upload via OpenAPI multipart
    import mimetypes
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
    except Exception as exc:
        return _error(f"Failed to read file_path: {exc}")
    if not filename:
        filename = os.path.basename(file_path) or "document.bin"
    content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"

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
