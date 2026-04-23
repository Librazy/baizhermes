"""Hermes plugin entrypoint for Baizhi.Cloud tools."""

def register(ctx) -> None:
    """Register Moonshot/Kimi tools with Hermes via the plugin API."""
    registrations = ["""TODO: Add Baizhi web search tool registration"""]
    for registration in registrations:
        ctx.register_tool(**registration)
