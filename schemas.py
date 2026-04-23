"""Tool schemas for the Baizhi.Cloud Hermes plugin."""

_FILTER_SCHEMA = {
    "type": "object",
    "properties": {
        "domains": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Optional allowlist of result domains.",
        },
        "exclude_domains": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Optional blocklist of result domains.",
        },
    },
}


BAIZHI_WEB_SEARCH = {
    "name": "baizhi_web_search",
    "description": (
        "Use Baizhi.Cloud general web search to retrieve raw webpage results. "
        "Best for current-event lookup, source collection, and structured search results."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text.",
            },
            "count": {
                "type": "integer",
                "description": "Number of results to return, from 1 to 50. Default is 10.",
                "minimum": 1,
                "maximum": 50,
                "default": 10,
            },
            "time_range": {
                "type": "string",
                "description": "Freshness filter for results.",
                "enum": ["day", "week", "month", "year"],
                "default": "month",
            },
            "filter": _FILTER_SCHEMA,
        },
        "required": ["query"],
    },
}


BAIZHI_AI_WEB_SEARCH = {
    "name": "baizhi_ai_web_search",
    "description": (
        "Use Baizhi.Cloud AI web search to get a synthesized answer with cited web results. "
        "Best for open-web question answering that needs a summary plus references."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Question to ask the AI web search service.",
            },
            "count": {
                "type": "integer",
                "description": "Number of cited results to request, from 1 to 50. Default is 10.",
                "minimum": 1,
                "maximum": 50,
                "default": 10,
            },
            "time_range": {
                "type": "string",
                "description": "Freshness filter for cited results.",
                "enum": ["day", "week", "month", "year"],
                "default": "month",
            },
            "filter": _FILTER_SCHEMA,
        },
        "required": ["query"],
    },
}
