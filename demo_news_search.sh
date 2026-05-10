#!/bin/bash

source .env

curl -SL --fail-with-body -X POST \
  https://newssearch.app.baizhi.cloud/openapi/v1/news/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_NEWS_SEARCH_API_KEY}" \
  -d '{
    "query": "DeepSeek V4 Pro",
    "time_range": "month",
    "max_results": 5,
    "include_answer": true,
    "include_domains": [],
    "exclude_domains": []
  }'

:<<'EXAMPLE_RESPONSE'
{
    "request_id": "req_deadbeefcafebabedeadbeefcafebabe",
    "data": {
        "query": "DeepSeek V4 Pro",
        "answer": "DeepSeek unveiled preview versions of its DeepSeek V4-Pro-Max and DeepSeek V4 Flash AI models on April 24, 2026. The V4-Pro-Max boasts 1.6 trillion parameters, making it the largest open-weight model, surpassing previous versions and competitors like Moonshot AI’s Kimi K 2.6. The V4 Flash model has 284 billion parameters and is priced at $0.14 per million input tokens, undercutting rivals. DeepSeek claims its V4 models outperform open-source peers on reasoning benchmarks and rival closed-source systems like OpenAI’s GPT-5.2 and Google’s Gemini 3.0 Pro on key tasks.",
        "response_time": 1.32,
        "points_cost": 10,
        "results": [
            {
                "rank": 1,
                "title": "DeepSeek Releases Preview of New V4 AI Models - MLQ.ai",
                "url": "https://mlq.ai/news/deepseek-unveils-preview-of-new-v4-ai-models/",
                "summary": "* DeepSeek launched preview versions of DeepSeek V4-Pro-Max (1.6 trillion parameters) and V4 Flash (284 billion parameters), both mixture-of-experts models with 1 million token context windows[1][2].",
                "score": 0.9055316,
                "published_at": "Sat, 25 Apr 2026 19:52:48 GMT"
            },
            {
                "rank": 2,
                "title": "China’s DeepSeek unveils latest models a year after upending global tech - Al Jazeera",
                "url": "https://www.aljazeera.com/economy/2026/4/24/chinas-deepseek-unveils-latest-model-a-year-after-upending-global-tech",
                "summary": "# China’s DeepSeek unveils latest models a year after upending global tech. *Chinese startup says DeepSeek-V4-Pro beats all rival open models for maths and coding.",
                "score": 0.8800674,
                "published_at": "Fri, 24 Apr 2026 06:04:47 GMT"
            },
            {
                "rank": 3,
                "title": "DeepSeek 1,6 триллион параметрли V4 моделини тақдим этди - Zamin.uz",
                "url": "https://zamin.uz/en/technology/197627-deepseek-introduced-v4-model-with-1-6-trillion-parameters.html",
                "summary": "# DeepSeek introduced V4 model with 1.6 trillion parameters. The Chinese laboratory DeepSeek has announced its latest large language models — the DeepSeek V4 Flash and V4 Pro versions. ",
                "score": 0.8747745,
                "published_at": "Sat, 25 Apr 2026 10:08:12 GMT"
            },
            {
                "rank": 4,
                "title": "DeepSeek V4 Shows That The Next AI Race Is About Efficiency - Forbes",
                "url": "https://www.forbes.com/sites/geruiwang/2026/04/26/deepseek-v4-shows-that-the-next-ai-race-is-about-efficiency/",
                "summary": "# DeepSeek V4 Shows That The Next AI Race Is About Efficiency. DeepSeek V4, the long awaited update from DeepSeek, arrives at a fiercely competitive moment, when Open AI’s GPT 5.5 and Anthropic’s Opus 4.7 have just launched one after the other.",
                "score": 0.8652358,
                "published_at": "Sun, 26 Apr 2026 00:00:00 GMT"
            },
            {
                "rank": 5,
                "title": "DeepSeek previews new AI model that ‘closes the gap’ with frontier models - TechCrunch",
                "url": "https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/",
                "summary": "Chinese AI lab DeepSeek has launched two preview versions of its newest large language model, DeepSeek V4, a much-awaited update to last year’s V3.2 model and the accompanying R1 reasoning model that took the AI world by storm.",
                "score": 0.8571119,
                "published_at": "Fri, 24 Apr 2026 13:30:59 GMT"
            }
        ]
    },
    "error": null
}
EXAMPLE_RESPONSE
