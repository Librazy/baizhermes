#!/bin/bash

curl -SL --fail-with-body -X POST https://websearch.app.baizhi.cloud/openapi/search -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SEARCH_API_KEY}" -d '{
    "query": "Kimi K2.6 模型用户体验",
    "count": 10
  }'

:<<'EXAMPLE_RESPONSE'
{
    "code": 0,
    "message": "success",
    "data": {
        "request_id": 1234,
        "status": "succeeded",
        "query": "Kimi K2.6 模型用户体验",
        "normalized_query": "Kimi K2.6 模型用户体验",
        "result_count": 10,
        "latency_ms": 396,
        "results": [
            {
                "rank": 1,
                "title": "国家超算互联网AI社区上线Kimi K2.6",
                "url": "http://m.163.com/dy/article/KR2045100550WHYR.html",
                "published_at": "2026-04-21T14:30:00+08:00",
                "score": 0.9903837442398071,
                "site_name": "网易"
            },
            {
                "rank": 2,
                "title": "月之暗面新模型Kimi K2.6发布并开源；自变量机器人完成近20亿元B轮融资｜未来商业早参",
                "url": "https://m.nbd.com.cn/articles/2026-04-21/4349995.html",
                "published_at": "2026-04-22T07:00:00+08:00",
                "score": 0.9872570037841797,
                "site_name": "每日经济新闻"
            },
            {
                "rank": 3,
                "title": "Kimi K2.6 上线引发访问高峰，月之暗面致歉并宣布全额恢复用户额度",
                "url": "http://m.toutiao.com/group/7631787211336024591/?upstream_biz=VolcEngine",
                "published_at": "2026-04-23T11:12:30+08:00",
                "score": 0.9432878494262695,
                "site_name": "今日头条"
            },
            {
                "rank": 4,
                "title": "AI的“总指挥官”来了：Kimi K2.6能同时调动300个小弟帮你干活",
                "url": "http://m.toutiao.com/group/7631416698368721442/?upstream_biz=VolcEngine",
                "published_at": "2026-04-22T12:15:56+08:00",
                "score": 0.9859066009521484,
                "site_name": "今日头条"
            },
            {
                "rank": 5,
                "title": "Kimi K2.6模型发布！多项能力开源AI新高度",
                "url": "http://m.toutiao.com/group/7630984409423905331/?upstream_biz=VolcEngine",
                "published_at": "2026-04-21T07:23:48+08:00",
                "score": 0.9827909469604492,
                "site_name": "今日头条"
            },
            {
                "rank": 6,
                "title": "Kimi K2.6模型发布：引领AI自主执行新纪元！",
                "url": "https://m.sohu.com/a/1012261568_121956422/",
                "published_at": "2026-04-21T07:39:00+08:00",
                "score": 0.9867563247680664,
                "site_name": "手机搜狐网"
            },
            {
                "rank": 7,
                "title": "Comate搭载Kimi K2.6，长程13h！",
                "url": "https://blog.51cto.com/u_16895435/14562205",
                "published_at": "2026-04-21T17:56:16+08:00",
                "score": 0.9822576642036438,
                "site_name": "51CTO博客"
            },
            {
                "rank": 8,
                "title": "月之暗面发布并开源Kimi K2.6模型",
                "url": "https://app.myzaker.com/news/article.php?pk=69e6ea7e8e9f09630d4a257b",
                "published_at": "2026-04-21T12:00:46+08:00",
                "score": 0.9864740967750549,
                "site_name": "ZAKER"
            },
            {
                "rank": 9,
                "title": "日本青春草官方版-日本青春草2026最新N.39.92.47-好游快爆 - 雪球网",
                "url": "https://yuli.ui.cn/wapyejJwNjS.csv?article/20260417_8665206.html",
                "published_at": "2026-04-21T21:26:08+08:00",
                "score": 0.9805439114570618
            },
            {
                "rank": 10,
                "title": "月之暗面新模型Kimi K2.6发布并开源",
                "url": "http://news.qq.com/rain/a/20260421A0200C00",
                "published_at": "2026-04-21T08:58:00+08:00",
                "score": 0.9806209206581116,
                "site_name": "腾讯网"
            }
        ]
    },
    "trace_id": "trc_deadbeefdeadbeefdeadbeef"
}

EXAMPLE_RESPONSE
