#!/bin/bash

curl -SL --fail-with-body -X POST https://websearch.app.baizhi.cloud/openapi/ai_search \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${BAIZHI_WEB_SEARCH_API_KEY}"\
  -d '{
    "query": "Kimi K2.6 模型用户体验",
    "count": 10
  }'

:<<'EXAMPLE_RESPONSE'

ent: start
data: {"type":"start","request_id":1234}

event: results
data: {"type":"results","request_id":1234,"results":[{"rank":1,"title":"KIMI升级 K2.6-code-preview 体验如何？","url":"https://post.m.smzdm.com/p/a82klq7l/","published_at":"2026-04-14T00:00:00+08:00","score":0.738827645778656,"site_name":"什么值得买社区频道"},{"rank":2,"title":"排行榜是别人的，手感是自己的：Kimi K2.6上手体感报告","url":"http://news.qq.com/rain/a/20260423A01QD800","published_at":"2026-04-23T08:17:00+08:00","score":0.6487754583358765,"site_name":"腾讯网"},{"rank":3,"title":"杨植麟交卷，Kimi K2.6抢先开源，指挥300个Agent上岗，实测手搓3D格斗游戏","url":"http://m.toutiao.com/group/7631069138756108834/?upstream_biz=VolcEngine","published_at":"2026-04-21T12:45:48+08:00","score":0.5874066352844238,"site_name":"今日头条"},{"rank":4,"title":"Kimi K2.6体验报告：更美、更牛、更壮，前端和编码能力肉眼可见的强","url":"http://news.qq.com/rain/a/20260421A0620F00","published_at":"2026-04-21T17:49:00+08:00","score":0.5758840441703796,"site_name":"腾讯网"},{"rank":5,"title":"杨植麟交卷！Kimi K2.6抢先开源，指挥300个Agent上岗，实测手搓3D格斗游戏","url":"https://fuboying.ui.cn/m=content\u0026c=index\u0026a=show\u0026catid=745\u0026id=48761","published_at":"2026-04-22T11:59:59+08:00","score":0.5359873175621033},{"rank":6,"title":"原来国产AI编程这么强了？Kimi 2.6体验，差距真没那么大","url":"http://m.toutiao.com/group/7628856599859233330/?upstream_biz=VolcEngine","published_at":"2026-04-15T13:58:59+08:00","score":0.5077458024024963,"site_name":"今日头条"},{"rank":7,"title":"Kimi K2.6 上线引发访问高峰，月之暗面致歉并宣布全额恢复用户额度","url":"http://m.toutiao.com/group/7631787211336024591/?upstream_biz=VolcEngine","published_at":"2026-04-23T11:12:30+08:00","score":0.39501193165779114,"site_name":"今日头条"},{"rank":8,"title":"Kimi 2.6‑Codes 实战｜国产编程模型从入门到精通的进阶指南","url":"https://juejin.cn/post/7628550892061409306","published_at":"2026-04-15T00:00:00+08:00","score":0.4372404217720032,"site_name":"稀土掘金"},{"rank":9,"title":"Kimi K2.6昨晚开源WorkBuddy今天就接上了","url":"http://m.toutiao.com/group/7631158945595343403/?upstream_biz=VolcEngine","published_at":"2026-04-21T18:34:46+08:00","score":0.4494432210922241,"site_name":"今日头条"},{"rank":10,"title":"Kimi K2.6 发布并开源：国产 AI 的 Agent 能力终于捅破天花板","url":"http://m.toutiao.com/group/7631021892241048107/?upstream_biz=VolcEngine","published_at":"2026-04-22T20:17:00+08:00","score":0.3429749608039856,"site_name":"今日头条"}]}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"K"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"imi"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" K"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"2"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"."}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"6"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"模型"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"在"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"性能"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"、"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"配置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"连接"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"、"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"使用"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"成本"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"等"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"方面"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"给"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"用户"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"带来"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"了"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"不同"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"体验"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"\n-"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" **"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"性能"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"与"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"响应"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"速度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"**"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"在"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"不同"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"场景"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"实测"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"中"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"新"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"模型"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"速度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"有"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"差异"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"如"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"CC"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"终端"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"响应"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"速度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"更快"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"代码"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"生成"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"与"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"处理"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"能力"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"较高"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"部分"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"用户"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"反馈"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"体验"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"感"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"接近"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"Cla"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"ude"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" Son"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"net"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"\n-"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" **"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"配置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"连接"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"**"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"升级"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"后"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"系统"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"默认"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"配置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"V"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"1"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"版本"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"的"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"URL"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"初期"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"会"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"无法"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"连接"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"需"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"手动"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"调整"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"不同"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"终端"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"配置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"难度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"不同"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"小龙虾"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"终端"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"需"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"手动"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"修改"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"CC"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"终端"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"通过"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"读取"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"code"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"文档"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"完成"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"自动"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"或"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"辅助"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"配置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"\n-"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" **"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"使用"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"成本"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"与"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"限量"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"**"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"扣费"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"速度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"减缓"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"周"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"限额"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"设置"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"宽松"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"降低"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"了"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"高频"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"使用者"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"的"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"门槛"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"\n-"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" **"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"功能"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"亮点"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"**"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"可"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"连续"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"编码"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"1"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"3"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"小时"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"、"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"处理"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"超"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"4"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"行"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"复杂"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"代码"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"支持"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"多"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"语言"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"前后"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"端"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"开发"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"融合"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"图像"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"与"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"视频"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"生成"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"工具"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"能"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"复刻"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"专业"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"级"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"Web"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"应用"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"其"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"Agent"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"集群"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"架构"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"可"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"支持"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"3"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"个子"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"Agent"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"并行"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"完成"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"4"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"个"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"协作"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"步骤"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"任务"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"完成"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"度"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"和"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"交付"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"质量"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"显著"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"提升"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"\n-"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":" **"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"视觉"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"体验"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"**"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"："}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"界面"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"暗色"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"背景"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"、"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"金色"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"分割"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"线"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"排版"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"克制"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"导航"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"栏"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"分类"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"合理"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"整体"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"视觉"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"9"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"分"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"内容"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"框架"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"8"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"0"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"分"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"，"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"拿来"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"展示"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"完全"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"够用"}

event: summary_delta
data: {"type":"summary_delta","request_id":1234,"delta":"。"}

event: done
data: {"type":"done","request_id":1234,"latency_ms":5677}

EXAMPLE_RESPONSE

echo

