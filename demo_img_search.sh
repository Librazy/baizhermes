#!/bin/bash

curl -SL --fail-with-body -X POST https://imgsearch.app.baizhi.cloud/openapi/search -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_IMG_SEARCH_API_KEY}" -d '{
    "query": "北京国家会议中心",
    "count": 5
  }'

:<<'EXAMPLE_RESPONSE'
{
    "code": 0,
    "message": "success",
    "data": {
        "request_id": 1234,
        "status": "succeeded",
        "query": "国家会展中心",
        "normalized_query": "国家会展中心",
        "result_count": 5,
        "latency_ms": 190,
        "results": [
            {
                "rank": 1,
                "title": "国家会展中心（上海）(上海市2011年建成的综合型建筑)###生活休闲-展馆展览-展馆-会展中心",
                "url": "",
                "published_at": "2025-12-17T11:03:53+08:00",
                "image": {
                    "url": "https://p11-volcsearch-sign.byteimg.com/tos-cn-i-xv4ileqgde/ac6382e6ddfb41389f345d53afd685b6~tplv-obj.jpeg?lk3s=1515c32d\u0026scene=volc_search\u0026x-expires=1784811338\u0026x-signature=Lor8%2FnZ%2FTJZjNnIXaf1%2FzGS1JuQ%3D",
                    "width": 640,
                    "height": 400
                }
            },
            {
                "rank": 2,
                "title": "国家会展中心（上海）(上海市2011年建成的综合型建筑)###生活休闲-展馆展览-展馆-会展中心",
                "url": "",
                "published_at": "2025-12-17T11:03:53+08:00",
                "image": {
                    "url": "https://p26-volcsearch-sign.byteimg.com/tos-cn-i-xv4ileqgde/4cd4b7de3e5f41d8811966b85c7465d5~tplv-obj.jpeg?lk3s=1515c32d\u0026scene=volc_search\u0026x-expires=1784811338\u0026x-signature=jGynNySYrFtaEsN3Ao9iTIpjPjQ%3D",
                    "width": 1332,
                    "height": 888
                }
            },
            {
                "rank": 3,
                "title": "国家会展中心（上海）(上海市2011年建成的综合型建筑)###生活休闲-展馆展览-展馆-会展中心",
                "url": "",
                "published_at": "2025-12-17T11:03:53+08:00",
                "image": {
                    "url": "https://p26-volcsearch-sign.byteimg.com/tos-cn-i-xv4ileqgde/b649d45f7742438cb1e6a878345a5324~tplv-obj.jpeg?lk3s=1515c32d\u0026scene=volc_search\u0026x-expires=1784811338\u0026x-signature=cdp75FjGnezuSiogcv2En7fXGUg%3D",
                    "width": 600,
                    "height": 435
                }
            },
            {
                "rank": 4,
                "title": "国家会展中心（上海）(上海市2011年建成的综合型建筑)###生活休闲-展馆展览-展馆-会展中心",
                "url": "",
                "published_at": "2025-12-17T11:03:53+08:00",
                "image": {
                    "url": "https://p3-volcsearch-sign.byteimg.com/tos-cn-i-xv4ileqgde/ddca370cc97ec36b2594de075ea935d7~tplv-obj.jpeg?lk3s=1515c32d\u0026scene=volc_search\u0026x-expires=1784811338\u0026x-signature=%2FcXHXTshGelootGqYCrhMoCKVYs%3D",
                    "width": 1459,
                    "height": 909
                }
            },
            {
                "rank": 5,
                "title": "国家会展中心（天津）(商务部与天津市共建的国家级会展中心)###生活休闲-展馆展览-展馆-会展中心",
                "url": "",
                "published_at": "2025-10-20T16:21:30+08:00",
                "image": {
                    "url": "https://p26-volcsearch-sign.byteimg.com/tos-cn-i-xv4ileqgde/66323bb214ba42778c1bb2dbc67554d1~tplv-obj.jpeg?lk3s=1515c32d\u0026scene=volc_search\u0026x-expires=1784811338\u0026x-signature=TvNkOiUSv186kaKXPPkKWeJtOwo%3D",
                    "width": 4656,
                    "height": 2635
                }
            }
        ]
    },
    "trace_id": "trc_deadbeefdeadbeefdeadbeef"
}

EXAMPLE_RESPONSE
