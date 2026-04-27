"""Local regression test for Baizhi Hermes plugin tools."""

import json
import os
import sys
from pathlib import Path

from tools.baizhi_search import baizhi_ai_web_search, baizhi_img_search, baizhi_web_search


def load_dotenv(env_path: Path) -> None:
    """Load a minimal .env file without external dependencies."""
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def main() -> int:
    root = Path(__file__).resolve().parent
    load_dotenv(root / ".env")

    has_web_key = bool(os.getenv("BAIZHI_WEB_SEARCH_API_KEY"))
    has_img_key = bool(os.getenv("BAIZHI_IMG_SEARCH_API_KEY"))

    if not has_web_key and not has_img_key:
        print(
            json.dumps(
                {"error": "No Baizhi API key is configured in .env"},
                ensure_ascii=False,
            )
        )
        return 1

    summary = {}

    if has_web_key:
        web_result = json.loads(
            baizhi_web_search({"query": "Kimi K2.6 模型用户体验", "count": 3})
        )
        if "error" in web_result:
            print(json.dumps({"web_search": web_result}, ensure_ascii=False))
            return 1

        ai_result = json.loads(
            baizhi_ai_web_search({"query": "天空为什么是蓝色的？", "count": 3})
        )
        if "error" in ai_result:
            print(json.dumps({"ai_web_search": ai_result}, ensure_ascii=False))
            return 1

        summary["web_search"] = {
            "ok": web_result.get("code") == 0,
            "request_id": web_result.get("data", {}).get("request_id"),
            "result_count": web_result.get("data", {}).get("result_count"),
            "first_title": (web_result.get("data", {}).get("results") or [{}])[0].get("title"),
        }
        summary["ai_web_search"] = {
            "ok": bool(ai_result.get("summary_text")),
            "request_id": ai_result.get("request_id"),
            "latency_ms": ai_result.get("latency_ms"),
            "results_count": len(ai_result.get("results") or []),
            "summary_preview": (ai_result.get("summary_text") or "")[:120],
        }

    if has_img_key:
        img_result = json.loads(baizhi_img_search({"query": "北京国家会议中心", "count": 3}))
        if "error" in img_result:
            print(json.dumps({"img_search": img_result}, ensure_ascii=False))
            return 1

        results = img_result.get("data", {}).get("results") or [{}]
        first_image = results[0].get("image") or {}
        summary["img_search"] = {
            "ok": img_result.get("code") == 0,
            "request_id": img_result.get("data", {}).get("request_id"),
            "result_count": img_result.get("data", {}).get("result_count"),
            "first_title": results[0].get("title"),
            "first_image_width": first_image.get("width"),
            "first_image_height": first_image.get("height"),
        }

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
