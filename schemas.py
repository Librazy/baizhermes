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
    "description": (
        "Create a RAG document in Baizhi.Cloud knowledge base. "
        "NOTE: Document ingestion is asynchronous — status transitions from 'uploaded' → 'processing' → 'ready'. "
        "Polling with baizhi_rag_get_document_status may take 1-5 minutes. Use sleep between polls, do NOT busy-loop."
    ),
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
    "description": (
        "Get processing status of a RAG document. "
        "Returns 'uploaded', 'processing', 'ready', or 'error'. "
        "NOTE: RAG ingestion can take minutes. Call this sparingly — sleep 10-30s between checks. Do NOT busy-loop."
    ),
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
    "description": (
        "Upload or parse a document with Baizhi parser. "
        "file_url: submits remote URL via MCP docparse_parse (server-side fetch, no local download). "
        "file_path: uploads local file via OpenAPI multipart POST. "
        "Use exactly one of file_url or file_path. "
        "NOTE: Parsing is asynchronous — use baizhi_doc_parser_get_document to poll status. "
        "PDF parsing typically takes 10-60s. Sleep between polls, do NOT busy-loop."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "file_url": {
                "type": "string",
                "description": "Publicly accessible HTTP(S) URL for the source file. Server-side fetch via MCP (zero local bandwidth).",
            },
            "file_path": {
                "type": "string",
                "description": "Local file path for the source file. Uploaded via OpenAPI multipart POST.",
            },
            "filename": {"type": "string", "description": "Optional filename override (only used for file_path)."},
        },
        "required": [],
    },
}


BAIZHI_DOC_PARSER_GET_DOCUMENT = {
    "name": "baizhi_doc_parser_get_document",
    "description": (
        "Get parser document details by ID. "
        "Check the 'Status' field: 'uploaded' → 'parsing' → 'parsed'. "
        "NOTE: Parsing takes 10-60s for typical PDFs. Sleep between polls, do NOT busy-loop."
    ),
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


_NEWS_FILTER_SCHEMA = {
    "type": "object",
    "properties": {
        "include_domains": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Optional allowlist of news domains (max 300).",
            "maxItems": 300,
        },
        "exclude_domains": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Optional blocklist of news domains (max 150).",
            "maxItems": 150,
        },
    },
}


BAIZHI_NEWS_SEARCH = {
    "name": "baizhi_news_search",
    "description": (
        "Use Baizhi.Cloud news search to retrieve news articles with optional AI summary. "
        "Best for current news lookup, media monitoring, and news-based research."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "News search query text or natural language question.",
            },
            "max_results": {
                "type": "integer",
                "description": "Number of news results to return, from 1 to 20. Default is 10.",
                "minimum": 1,
                "maximum": 20,
                "default": 10,
            },
            "time_range": {
                "type": "string",
                "description": "Freshness filter for news results.",
                "enum": ["day", "week", "month", "year"],
                "default": "month",
            },
            "include_answer": {
                "type": "boolean",
                "description": "Whether to include AI-generated summary of the news results.",
                "default": False,
            },
            "include_domains": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional allowlist of news domains (max 300).",
                "maxItems": 300,
            },
            "exclude_domains": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional blocklist of news domains (max 150).",
                "maxItems": 150,
            },
        },
        "required": ["query"],
    },
}


BAIZHI_RAG_UPLOAD_LOCAL_FILE = {
    "name": "baizhi_rag_upload_local_file",
    "description": (
        "Upload a local file to Baizhi.Cloud RAG knowledge base. "
        "Handles the full workflow internally: gets presigned upload URL via MCP, "
        "uploads the file via HTTP PUT, then creates the RAG document from the uploaded URL. "
        "Supports PDF, Word, Excel, images, Markdown, and text files. "
        "NOTE: Processing is asynchronous and can take 1-10 minutes depending on file size. "
        "Use baizhi_rag_get_document_status to check progress. Sleep 10-30s between polls — do NOT busy-loop."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {"type": "string", "description": "Absolute path to the local file to upload."},
            "title": {"type": "string", "description": "Document title for the RAG knowledge base. Defaults to filename if not provided."},
            "file_name": {"type": "string", "description": "Optional filename override. Defaults to basename of file_path."},
        },
        "required": ["file_path"],
    },
}


BAIZHI_RAG_CREATE_DOCUMENT_FROM_URL = {
    "name": "baizhi_rag_create_document_from_url",
    "description": (
        "Create a RAG knowledge base document from a remote HTTP(S) file URL. "
        "The server fetches and processes the file directly. "
        "Supports PDF, Word, Excel, images, Markdown, and text files. "
        "NOTE: Processing is asynchronous and can take 1-10 minutes depending on file size. "
        "Use baizhi_rag_get_document_status to check progress. Sleep 10-30s between polls — do NOT busy-loop."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "Downloadable HTTP(S) absolute URL of the file."},
            "file_name": {"type": "string", "description": "Optional filename override when URL lacks a stable name."},
            "file_type": {"type": "string", "description": "Optional file type/extension override."},
            "mime_type": {"type": "string", "description": "Optional MIME type override."},
        },
        "required": ["url"],
    },
}


BAIZHI_RAG_GET_DOC_UPLOAD_URL = {
    "name": "baizhi_rag_get_doc_upload_url",
    "description": (
        "Get a presigned upload URL for local files. "
        "Returns upload_url (for PUT upload) and read_url (for subsequent create_document_from_url). "
        "This tool does NOT upload the file or create a document — it only prepares the URLs."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "file_name": {"type": "string", "description": "Filename with extension (e.g., report.pdf)."},
            "file_type": {"type": "string", "description": "Optional file type/extension override."},
            "mime_type": {"type": "string", "description": "Optional MIME type override."},
        },
        "required": ["file_name"],
    },
}


BAIZHI_RAG_GREP = {
    "name": "baizhi_rag_grep",
    "description": (
        "Exact text or regex search in the RAG knowledge base. "
        "Best for field names, error messages, paths, API aliases, version numbers, command snippets, "
        "and other content requiring exact matching. Use when semantic search is not precise enough."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "pattern": {"type": "string", "description": "Text or regex pattern to search for."},
            "is_regex": {"type": "boolean", "description": "Whether to interpret pattern as a regex."},
            "case_sensitive": {"type": "boolean", "description": "Whether to match case-sensitively."},
            "max_results": {"type": "number", "description": "Maximum number of hits to return."},
            "document_ids": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional list of document IDs to limit search scope.",
            },
        },
        "required": ["pattern"],
    },
}


BAIZHI_RAG_SEARCH_SECTIONS = {
    "name": "baizhi_rag_search_sections",
    "description": (
        "Locate relevant sections or document entries by topic in the RAG knowledge base. "
        "Use to find which document/chapter covers a topic before reading full content. "
        "Returns section metadata, not full text."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Section search keyword or topic."},
            "top_k": {"type": "number", "description": "Max results. Default 10, max 20."},
            "document_ids": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional list of document IDs to limit search scope.",
            },
        },
        "required": ["query"],
    },
}


BAIZHI_RAG_GET_SECTION = {
    "name": "baizhi_rag_get_section",
    "description": (
        "Read the full content of a specific section by document_id and section_id. "
        "Use after rag_search_sections to read complete instructions, steps, config examples, "
        "and surrounding context of a located section."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "document_id": {"type": "string", "description": "Document ID."},
            "section_id": {"type": "string", "description": "Section ID."},
        },
        "required": ["document_id", "section_id"],
    },
}


BAIZHI_WEB_SCRAPE = {
    "name": "baizhi_web_scrape",
    "description": (
        "Use Baizhi.Cloud web scrape to extract webpage content as Markdown. "
        "Best for converting public web pages to structured text for LLM consumption, "
        "RAG ingestion, or downstream processing."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The HTTP or HTTPS URL of the webpage to scrape.",
            },
        },
        "required": ["url"],
    },
}