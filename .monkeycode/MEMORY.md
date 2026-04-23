# 用户指令记忆

本文件记录了用户的指令、偏好和教导，用于在未来的交互中提供参考。

## 格式

### 用户指令条目
用户指令条目应遵循以下格式：

[用户指令摘要]
- Date: [YYYY-MM-DD]
- Context: [提及的场景或时间]
- Instructions:
  - [用户教导或指示的内容，逐行描述]

### 项目知识条目
Agent 在任务执行过程中发现的条目应遵循以下格式：

[项目知识摘要]
- Date: [YYYY-MM-DD]
- Context: Agent 在执行 [具体任务描述] 时发现
- Category: [代码结构|代码模式|代码生成|构建方法|测试方法|依赖关系|环境配置]
- Instructions:
  - [具体的知识点，逐行描述]

## 去重策略
- 添加新条目前，检查是否存在相似或相同的指令
- 若发现重复，跳过新条目或与已有条目合并
- 合并时，更新上下文或日期信息
- 这有助于避免冗余条目，保持记忆文件整洁

## 条目

[Hermes 插件注册结构]
- Date: 2026-04-23
- Context: Agent 在执行为 Hermes Agent 实现百智云搜索插件时发现
- Category: 代码结构
- Instructions:
  - 插件入口位于仓库根目录 `__init__.py`，通过 `register(ctx)` 调用 `ctx.register_tool(...)` 完成工具注册。
  - `plugin.yaml` 负责声明插件元信息和 `provides_tools`，工具的 schema 与 handler 可在独立模块中组织。

[百智云凭据管理约定]
- Date: 2026-04-23
- Context: 用户要求使用百智云搜索 token 进行联调时
- Instructions:
  - `BAIZHI_WEB_SEARCH_API_KEY` 必须写入项目根目录 `.env`，不能硬编码到代码中。

[百智云插件本地测试方式]
- Date: 2026-04-23
- Context: Agent 在为插件补充回归验证入口时发现
- Category: 测试方法
- Instructions:
  - 使用 `python3 test_baizhi_tools.py` 进行本地回归验证。
  - 测试脚本会从项目根目录 `.env` 加载 `BAIZHI_WEB_SEARCH_API_KEY`，并分别验证通用搜索与 AI 搜索。
