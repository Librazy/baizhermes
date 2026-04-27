"""Baizhi.Cloud search handlers for Hermes."""

import json
import os
from typing import Any
from urllib import error, request


_WEB_BASE_URL = "https://websearch.app.baizhi.cloud"
_WEB_API_KEY_ENV = "BAIZHI_WEB_SEARCH_API_KEY"
_IMG_BASE_URL = "https://imgsearch.app.baizhi.cloud"
_IMG_API_KEY_ENV = "BAIZHI_IMG_SEARCH_API_KEY"
_VALID_TIME_RANGES = {"day", "week", "month", "year"}


def has_web_search_api_key() -> bool:
    return bool(os.getenv(_WEB_API_KEY_ENV))


def has_img_search_api_key() -> bool:
    return bool(os.getenv(_IMG_API_KEY_ENV))


def _error(message: str) -> str:
    return json.dumps({"error": message}, ensure_ascii=False)


def _normalize_web_args(args: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    query = str(args.get("query", "")).strip()
    if not query:
        return None, "query is required"

    count = args.get("count", 10)
    try:
        count = int(count)
    except (TypeError, ValueError):
        return None, "count must be an integer between 1 and 50"
    if count < 1 or count > 50:
        return None, "count must be an integer between 1 and 50"

    time_range = str(args.get("time_range", "month")).strip() or "month"
    if time_range not in _VALID_TIME_RANGES:
        return None, "time_range must be one of: day, week, month, year"

    payload: dict[str, Any] = {
        "query": query,
        "count": count,
        "time_range": time_range,
    }

    raw_filter = args.get("filter")
    if raw_filter is not None:
        if not isinstance(raw_filter, dict):
            return None, "filter must be an object"

        normalized_filter: dict[str, list[str]] = {}
        for key in ("domains", "exclude_domains"):
            values = raw_filter.get(key)
            if values is None:
                continue
            if not isinstance(values, list) or not all(isinstance(item, str) and item.strip() for item in values):
                return None, f"filter.{key} must be a non-empty string array"
            normalized_filter[key] = [item.strip() for item in values]

        if normalized_filter:
            payload["filter"] = normalized_filter

    return payload, None


def _normalize_img_args(args: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    query = str(args.get("query", "")).strip()
    if not query:
        return None, "query is required"

    count = args.get("count", 5)
    try:
        count = int(count)
    except (TypeError, ValueError):
        return None, "count must be an integer between 1 and 5"
    if count < 1 or count > 5:
        return None, "count must be an integer between 1 and 5"

    payload: dict[str, Any] = {
        "query": query,
        "count": count,
    }

    raw_image = args.get("image")
    if raw_image is not None:
        if not isinstance(raw_image, dict):
            return None, "image must be an object"

        image: dict[str, int] = {}
        for key in ("width_min", "height_min", "width_max", "height_max"):
            value = raw_image.get(key)
            if value is None:
                continue
            try:
                value = int(value)
            except (TypeError, ValueError):
                return None, f"image.{key} must be a positive integer"
            if value < 1:
                return None, f"image.{key} must be a positive integer"
            image[key] = value

        if image:
            payload["image"] = image

    return payload, None


def _build_request(
    base_url: str,
    path: str,
    payload: dict[str, Any],
    api_key_env: str,
    accept: str = "application/json",
) -> request.Request:
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise RuntimeError(f"{api_key_env} not configured")

    return request.Request(
        url=f"{base_url}{path}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": accept,
        },
        method="POST",
    )


def _parse_http_error(exc: error.HTTPError) -> str:
    try:
        body = exc.read().decode("utf-8", errors="replace")
    except Exception:
        body = exc.reason or ""

    detail = body.strip() or str(exc.reason)
    return f"Baizhi API request failed with status {exc.code}: {detail}"


def baizhi_web_search(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs

    if not has_web_search_api_key():
        return _error(f"{_WEB_API_KEY_ENV} not configured")

    payload, validation_error = _normalize_web_args(args)
    if validation_error:
        return _error(validation_error)

    try:
        req = _build_request(_WEB_BASE_URL, "/openapi/search", payload, _WEB_API_KEY_ENV)
        with request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi web search failed: {exc}")

    if data.get("code") != 0:
        return _error(data.get("message") or "Baizhi API returned an error")

    return json.dumps(data, ensure_ascii=False)


def baizhi_ai_web_search(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs

    if not has_web_search_api_key():
        return _error(f"{_WEB_API_KEY_ENV} not configured")

    payload, validation_error = _normalize_web_args(args)
    if validation_error:
        return _error(validation_error)

    summary_parts: list[str] = []
    latest_results: list[dict[str, Any]] = []
    request_id = None
    done_payload: dict[str, Any] | None = None

    try:
        req = _build_request(
            _WEB_BASE_URL,
            "/openapi/ai_search",
            payload,
            _WEB_API_KEY_ENV,
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

                    if payload_obj.get("request_id") is not None:
                        request_id = payload_obj.get("request_id")
                    if event_name == "summary_delta":
                        summary_parts.append(payload_obj.get("delta", ""))
                    elif event_name == "results":
                        latest_results = payload_obj.get("results", [])
                    elif event_name == "done":
                        done_payload = payload_obj
                        latest_results = payload_obj.get("results", latest_results)
                        if payload_obj.get("summary_text"):
                            summary_parts = [payload_obj["summary_text"]]
                    elif event_name == "error":
                        return _error(payload_obj.get("error_message") or "Baizhi AI search returned an error")

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

            if data_lines:
                payload_obj = json.loads("\n".join(data_lines))
                if payload_obj.get("type") == "done":
                    done_payload = payload_obj
                    latest_results = payload_obj.get("results", latest_results)
                    if payload_obj.get("summary_text"):
                        summary_parts = [payload_obj["summary_text"]]
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi AI web search failed: {exc}")

    result = {
        "request_id": request_id,
        "summary_text": "".join(summary_parts),
        "results": latest_results,
    }
    if done_payload and done_payload.get("latency_ms") is not None:
        result["latency_ms"] = done_payload["latency_ms"]

    return json.dumps(result, ensure_ascii=False)


def baizhi_img_search(args: dict[str, Any], **kwargs: Any) -> str:
    del kwargs

    if not has_img_search_api_key():
        return _error(f"{_IMG_API_KEY_ENV} not configured")

    payload, validation_error = _normalize_img_args(args)
    if validation_error:
        return _error(validation_error)

    try:
        req = _build_request(_IMG_BASE_URL, "/openapi/search", payload, _IMG_API_KEY_ENV)
        with request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        return _error(_parse_http_error(exc))
    except error.URLError as exc:
        return _error(f"Baizhi API network error: {exc.reason}")
    except Exception as exc:
        return _error(f"Baizhi image search failed: {exc}")

    if data.get("code") != 0:
        return _error(data.get("message") or "Baizhi API returned an error")

    return json.dumps(data, ensure_ascii=False)
