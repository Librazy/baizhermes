"""Hermes plugin entrypoint for Baizhi.Cloud tools."""

from . import schemas
from .tools.baizhi_search import (
    baizhi_ai_web_search,
    baizhi_img_search,
    baizhi_news_search,
    baizhi_web_search,
    has_img_search_api_key,
    has_news_search_api_key,
    has_web_search_api_key,
)
from .tools.baizhi_rag_doc import (
    baizhi_doc_parser_download,
    baizhi_doc_parser_get_document,
    baizhi_doc_parser_upload,
    baizhi_rag_chat_stream,
    baizhi_rag_create_document,
    baizhi_rag_create_document_from_url,
    baizhi_rag_delete_document,
    baizhi_rag_get_document_status,
    baizhi_rag_get_section,
    baizhi_rag_grep,
    baizhi_rag_retrieve,
    baizhi_rag_search_sections,
    baizhi_rag_update_document,
    baizhi_rag_upload_local_file,
    has_doc_parser_api_key,
    has_rag_api_key,
)


def register(ctx) -> None:
    """Register Baizhi.Cloud search tools with Hermes via the plugin API."""
    registrations = []

    if has_web_search_api_key():
        registrations.extend(
            [
                {
                    "name": "baizhi_web_search",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_WEB_SEARCH,
                    "handler": baizhi_web_search,
                },
                {
                    "name": "baizhi_ai_web_search",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_AI_WEB_SEARCH,
                    "handler": baizhi_ai_web_search,
                },
            ]
        )

    if has_news_search_api_key():
        registrations.append(
            {
                "name": "baizhi_news_search",
                "toolset": "baizhi",
                "schema": schemas.BAIZHI_NEWS_SEARCH,
                "handler": baizhi_news_search,
            }
        )

    if has_img_search_api_key():
        registrations.append(
            {
                "name": "baizhi_img_search",
                "toolset": "baizhi",
                "schema": schemas.BAIZHI_IMG_SEARCH,
                "handler": baizhi_img_search,
            }
        )

    if has_rag_api_key():
        registrations.extend(
            [
                {
                    "name": "baizhi_rag_create_document",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_CREATE_DOCUMENT,
                    "handler": baizhi_rag_create_document,
                },
                {
                    "name": "baizhi_rag_update_document",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_UPDATE_DOCUMENT,
                    "handler": baizhi_rag_update_document,
                },
                {
                    "name": "baizhi_rag_delete_document",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_DELETE_DOCUMENT,
                    "handler": baizhi_rag_delete_document,
                },
                {
                    "name": "baizhi_rag_get_document_status",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_GET_DOCUMENT_STATUS,
                    "handler": baizhi_rag_get_document_status,
                },
                {
                    "name": "baizhi_rag_retrieve",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_RETRIEVE,
                    "handler": baizhi_rag_retrieve,
                },
                {
                    "name": "baizhi_rag_chat_stream",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_CHAT_STREAM,
                    "handler": baizhi_rag_chat_stream,
                },
                # RAG MCP tools
                {
                    "name": "baizhi_rag_upload_local_file",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_UPLOAD_LOCAL_FILE,
                    "handler": baizhi_rag_upload_local_file,
                },
                {
                    "name": "baizhi_rag_create_document_from_url",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_CREATE_DOCUMENT_FROM_URL,
                    "handler": baizhi_rag_create_document_from_url,
                },
                {
                    "name": "baizhi_rag_grep",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_GREP,
                    "handler": baizhi_rag_grep,
                },
                {
                    "name": "baizhi_rag_search_sections",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_SEARCH_SECTIONS,
                    "handler": baizhi_rag_search_sections,
                },
                {
                    "name": "baizhi_rag_get_section",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_RAG_GET_SECTION,
                    "handler": baizhi_rag_get_section,
                },
            ]
        )

    if has_doc_parser_api_key():
        registrations.extend(
            [
                {
                    "name": "baizhi_doc_parser_upload",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_DOC_PARSER_UPLOAD,
                    "handler": baizhi_doc_parser_upload,
                },
                {
                    "name": "baizhi_doc_parser_get_document",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_DOC_PARSER_GET_DOCUMENT,
                    "handler": baizhi_doc_parser_get_document,
                },
                {
                    "name": "baizhi_doc_parser_download",
                    "toolset": "baizhi",
                    "schema": schemas.BAIZHI_DOC_PARSER_DOWNLOAD,
                    "handler": baizhi_doc_parser_download,
                },
            ]
        )

    for registration in registrations:
        ctx.register_tool(**registration)
