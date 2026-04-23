"""Hermes plugin entrypoint for Baizhi.Cloud tools."""

from . import schemas
from .tools.baizhi_search import baizhi_ai_web_search, baizhi_web_search


def register(ctx) -> None:
    """Register Baizhi.Cloud search tools with Hermes via the plugin API."""
    registrations = [
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
    for registration in registrations:
        ctx.register_tool(**registration)
