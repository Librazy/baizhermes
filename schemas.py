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


_IMAGE_FILTER_SCHEMA = {
    "type": "object",
    "properties": {
        "width_min": {
            "type": "integer",
            "description": "Minimum image width in pixels.",
            "minimum": 1,
        },
        "height_min": {
            "type": "integer",
            "description": "Minimum image height in pixels.",
            "minimum": 1,
        },
        "width_max": {
            "type": "integer",
            "description": "Maximum image width in pixels.",
            "minimum": 1,
        },
        "height_max": {
            "type": "integer",
            "description": "Maximum image height in pixels.",
            "minimum": 1,
        },
    },
}


BAIZHI_IMG_SEARCH = {
    "name": "baizhi_img_search",
    "description": (
        "Use Baizhi.Cloud image search to retrieve image results by keyword. "
        "Best for finding image URLs with width and height metadata for display or material selection."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Image search query text.",
            },
            "count": {
                "type": "integer",
                "description": "Number of image results to return, from 1 to 5. Default is 5.",
                "minimum": 1,
                "maximum": 5,
                "default": 5,
            },
            "image": _IMAGE_FILTER_SCHEMA,
        },
        "required": ["query"],
    },
}
