"""Hermes plugin entrypoint for Baizhi.Cloud tools."""

from . import schemas
from .tools.baizhi_search import (
    baizhi_ai_web_search,
    baizhi_img_search,
    baizhi_web_search,
    has_img_search_api_key,
    has_web_search_api_key,
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

    if has_img_search_api_key():
        registrations.append(
            {
                "name": "baizhi_img_search",
                "toolset": "baizhi",
                "schema": schemas.BAIZHI_IMG_SEARCH,
                "handler": baizhi_img_search,
            }
        )

    for registration in registrations:
        ctx.register_tool(**registration)
