"""Local regression test for Baizhi Hermes plugin tools."""

import json
import os
import sys
import time
from pathlib import Path

from tools.baizhi_search import (
    baizhi_ai_web_search,
    baizhi_img_search,
    baizhi_news_search,
    baizhi_web_search,
    baizhi_web_scrape,
)
from tools.baizhi_rag_doc import (
    baizhi_doc_parser_download,
    baizhi_doc_parser_get_document,
    baizhi_doc_parser_upload,
    baizhi_rag_chat_stream,
    baizhi_rag_create_document,
    baizhi_rag_delete_document,
    baizhi_rag_get_document_status,
    baizhi_rag_retrieve,
    baizhi_rag_update_document,
)


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
    has_news_key = bool(os.getenv("BAIZHI_NEWS_SEARCH_API_KEY"))
    has_rag_key = bool(os.getenv("BAIZHI_RAG_API_KEY"))
    has_doc_key = bool(os.getenv("BAIZHI_DOC_PARSER_API_KEY"))
    has_scrape_key = bool(os.getenv("BAIZHI_WEB_SCRAPE_API_KEY"))

    if not has_web_key and not has_img_key and not has_news_key and not has_rag_key and not has_doc_key and not has_scrape_key:
        print(
            json.dumps(
                {"error": "No Baizhi API key is configured in .env"},
                ensure_ascii=False,
            )
        )
        return 1

    summary = {}
    failures: dict[str, Any] = {}

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

    if has_scrape_key:
        scrape_result = json.loads(
            baizhi_web_scrape({"url": "https://36kr.com/p/3787501855136774"})
        )
        if "error" in scrape_result:
            failures["web_scrape"] = scrape_result
            summary["web_scrape"] = {"ok": False}
        else:
            data = scrape_result.get("data", {})
            summary["web_scrape"] = {
                "ok": scrape_result.get("code") == 0,
                "source_url": data.get("source_url"),
                "characters": data.get("characters"),
                "content_preview": (data.get("content") or "")[:120],
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

    if has_news_key:
        news_result = json.loads(
            baizhi_news_search({
                "query": "人工智能最新进展",
                "max_results": 5,
                "time_range": "week",
                "include_answer": True,
                "include_domains": [],
                "exclude_domains": []
            })
        )
        if "error" in news_result:
            failures["news_search"] = news_result
            summary["news_search"] = {"ok": False}
        else:
            data = news_result.get("data", {})
            results = data.get("results", [])
            summary["news_search"] = {
                "ok": bool(results),
                "request_id": news_result.get("request_id"),
                "query": data.get("query"),
                "has_answer": bool(data.get("answer")),
                "results_count": len(results),
                "first_title": results[0].get("title") if results else None,
                "first_url": results[0].get("url") if results else None,
                "points_cost": data.get("points_cost"),
            }
        doc_title = f"Hermes Test {int(time.time())}"
        doc_content = "# Hermes RAG Test\n\n权限管理使用 RBAC 模型。"

        created = json.loads(baizhi_rag_create_document({"title": doc_title, "content": doc_content}))
        if "error" in created:
            failures["rag_create"] = created
            summary["rag"] = {"ok": False}
        else:
            rag_document_id = created.get("document_id") or (created.get("data") or {}).get("document_id")
            if not rag_document_id:
                failures["rag_create"] = {"error": "missing document_id", "response": created}
                summary["rag"] = {"ok": False}
            else:
                status = json.loads(
                    baizhi_rag_get_document_status({"document_id": rag_document_id})
                )
                updated = json.loads(
                    baizhi_rag_update_document(
                        {
                            "document_id": rag_document_id,
                            "title": f"{doc_title} Updated",
                            "content": "# Hermes RAG Test Updated\n\n权限管理支持角色与资源绑定。",
                        }
                    )
                )
                retrieved = json.loads(
                    baizhi_rag_retrieve({"query": "权限管理", "top_k": 3, "group_by_document": True})
                )
                streamed = json.loads(
                    baizhi_rag_chat_stream({"query": "权限管理怎么做？", "top_k": 3})
                )
                deleted = json.loads(baizhi_rag_delete_document({"document_id": rag_document_id}))

                for key, value in {
                    "rag_status": status,
                    "rag_update": updated,
                    "rag_retrieve": retrieved,
                    "rag_chat_stream": streamed,
                    "rag_delete": deleted,
                }.items():
                    if "error" in value:
                        failures[key] = value

                summary["rag"] = {
                    "ok": not any(k.startswith("rag_") for k in failures),
                    "document_id": rag_document_id,
                    "status": status.get("status") or (status.get("data") or {}).get("status"),
                    "retrieve_items": len(retrieved.get("items") or []),
                    "chat_answer_preview": (streamed.get("answer") or "")[:120],
                    "delete_status": deleted.get("status") or (deleted.get("data") or {}).get("status"),
                }

    if has_doc_key:
        test_pdf = root / "DeepSeek_V4.pdf"
        if not test_pdf.exists():
            failures["doc_parser"] = {"error": "Missing /workspace/DeepSeek_V4.pdf"}
            summary["doc_parser"] = {"ok": False}
        else:
            uploaded = json.loads(
                baizhi_doc_parser_upload(
                    {
                        "file_url": test_pdf.resolve().as_uri(),
                        "filename": test_pdf.name,
                    }
                )
            )
            if "error" in uploaded or uploaded.get("code") != 0:
                failures["doc_upload"] = uploaded
                summary["doc_parser"] = {"ok": False}
            else:
                doc_id = ((uploaded.get("data") or {}).get("ID"))
                if not doc_id:
                    failures["doc_upload"] = {"error": "missing data.ID", "response": uploaded}
                    summary["doc_parser"] = {"ok": False}
                else:
                    detail = json.loads(baizhi_doc_parser_get_document({"document_id": doc_id}))
                    if "error" in detail or detail.get("code") != 0:
                        failures["doc_detail"] = detail
                        summary["doc_parser"] = {"ok": False, "document_id": doc_id}
                    else:
                        document = ((detail.get("data") or {}).get("document") or {})
                        object_key = document.get("ObjectKey")
                        if not object_key:
                            failures["doc_detail"] = {"error": "missing ObjectKey", "response": detail}
                            summary["doc_parser"] = {"ok": False, "document_id": doc_id}
                        else:
                            downloaded = json.loads(
                                baizhi_doc_parser_download({"document_id": doc_id, "key": object_key})
                            )
                            if "error" in downloaded:
                                failures["doc_download"] = downloaded
                                summary["doc_parser"] = {"ok": False, "document_id": doc_id}
                            else:
                                summary["doc_parser"] = {
                                    "ok": True,
                                    "document_id": doc_id,
                                    "status": document.get("Status"),
                                    "page_count": document.get("PageCount"),
                                    "download_content_type": downloaded.get("content_type"),
                                    "download_has_payload": bool(downloaded.get("text") or downloaded.get("base64")),
                                }

    if failures:
        summary["failures"] = failures

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
