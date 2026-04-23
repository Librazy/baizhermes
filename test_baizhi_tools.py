"""Local regression test for Baizhi Hermes plugin tools."""

import json
import os
import sys
from pathlib import Path

from tools.baizhi_search import baizhi_ai_web_search, baizhi_web_search


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

    if not os.getenv("BAIZHI_WEB_SEARCH_API_KEY"):
        print(
            json.dumps(
                {"error": "BAIZHI_WEB_SEARCH_API_KEY is not configured in .env"},
                ensure_ascii=False,
            )
        )
        return 1

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

    summary = {
        "web_search": {
            "ok": web_result.get("code") == 0,
            "request_id": web_result.get("data", {}).get("request_id"),
            "result_count": web_result.get("data", {}).get("result_count"),
            "first_title": (web_result.get("data", {}).get("results") or [{}])[0].get("title"),
        },
        "ai_web_search": {
            "ok": bool(ai_result.get("summary_text")),
            "request_id": ai_result.get("request_id"),
            "latency_ms": ai_result.get("latency_ms"),
            "results_count": len(ai_result.get("results") or []),
            "summary_preview": (ai_result.get("summary_text") or "")[:120],
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
