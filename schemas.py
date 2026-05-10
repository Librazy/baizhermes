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


BAIZHI_RAG_CREATE_DOCUMENT = {
    "name": "baizhi_rag_create_document",
    "description": "Create a RAG document in Baizhi.Cloud knowledge base.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Document title."},
            "content": {"type": "string", "description": "Document content in markdown or plain text."},
        },
        "required": ["title", "content"],
    },
}


BAIZHI_RAG_UPDATE_DOCUMENT = {
    "name": "baizhi_rag_update_document",
    "description": "Update an existing RAG document.",
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "string", "description": "RAG document ID."},
            "title": {"type": "string", "description": "Updated title."},
            "content": {"type": "string", "description": "Updated document content."},
        },
        "required": ["document_id", "title", "content"],
    },
}


BAIZHI_RAG_DELETE_DOCUMENT = {
    "name": "baizhi_rag_delete_document",
    "description": "Delete a RAG document by ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "string", "description": "RAG document ID."},
        },
        "required": ["document_id"],
    },
}


BAIZHI_RAG_GET_DOCUMENT_STATUS = {
    "name": "baizhi_rag_get_document_status",
    "description": "Get processing status of a RAG document.",
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "string", "description": "RAG document ID."},
        },
        "required": ["document_id"],
    },
}


BAIZHI_RAG_RETRIEVE = {
    "name": "baizhi_rag_retrieve",
    "description": "Retrieve relevant chunks from Baizhi RAG knowledge base.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Semantic retrieval query."},
            "top_k": {"type": "number", "description": "Max number of results."},
            "score_threshold": {"type": "number", "description": "Minimum accepted score."},
            "group_by_document": {"type": "boolean", "description": "Whether to merge chunks by document."},
            "include_score_detail": {"type": "boolean", "description": "Whether to include detailed score fields."},
        },
        "required": ["query"],
    },
}


BAIZHI_RAG_CHAT_STREAM = {
    "name": "baizhi_rag_chat_stream",
    "description": "Ask a question against RAG and return merged stream result.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Question for the RAG chat API."},
            "top_k": {"type": "number", "description": "Optional retrieval candidate count."},
        },
        "required": ["query"],
    },
}


BAIZHI_DOC_PARSER_UPLOAD = {
    "name": "baizhi_doc_parser_upload",
    "description": "Upload a document file (via URL) to Baizhi parser.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_url": {"type": "string", "description": "Publicly accessible URL for the source file."},
            "filename": {"type": "string", "description": "Optional filename override."},
        },
        "required": ["file_url"],
    },
}


BAIZHI_DOC_PARSER_GET_DOCUMENT = {
    "name": "baizhi_doc_parser_get_document",
    "description": "Get parser document details by ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "integer", "description": "Parser document ID."},
        },
        "required": ["document_id"],
    },
}


BAIZHI_DOC_PARSER_DOWNLOAD = {
    "name": "baizhi_doc_parser_download",
    "description": "Download original or parsed file from parser storage.",
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "integer", "description": "Parser document ID."},
            "key": {"type": "string", "description": "Object key or result key to download."},
        },
        "required": ["document_id", "key"],
    },
}
