# Baizhi Hermes Plugin

这个仓库实现了一个 Hermes Agent 插件，将百智云搜索服务注册为两个 Tool Call：

- `baizhi_web_search`
- `baizhi_ai_web_search`

## 环境变量配置

插件依赖环境变量 `BAIZHI_WEB_SEARCH_API_KEY`。

请在项目根目录创建 `.env` 文件，并写入以下内容：

```dotenv
BAIZHI_WEB_SEARCH_API_KEY=<YOUR_BAIZHI_WEB_SEARCH_API_KEY>
```

说明：

- 不要把真实 token 写进代码文件。
- `.env` 已在 `.gitignore` 中忽略，不会默认提交到仓库。
- Hermes 加载插件时会读取 `plugin.yaml` 中声明的 `requires_env`。

## 提供的工具

### `baizhi_web_search`

用于调用百智云通用搜索接口，返回原始网页搜索结果。

支持参数：

- `query`: 搜索关键词，必填
- `count`: 结果数量，范围 `1-50`
- `time_range`: 时间范围，可选 `day`、`week`、`month`、`year`
- `filter.domains`: 只保留指定域名结果
- `filter.exclude_domains`: 排除指定域名结果

### `baizhi_ai_web_search`

用于调用百智云 AI 搜索接口，返回 AI 摘要和引用结果。

支持参数与 `baizhi_web_search` 一致。

## 本地回归测试

仓库提供了一个本地测试脚本：`test_baizhi_tools.py`。

执行方式：

```bash
python3 test_baizhi_tools.py
```

脚本会：

- 从项目根目录 `.env` 加载 `BAIZHI_WEB_SEARCH_API_KEY`
- 调用 `baizhi_web_search` 做一次真实搜索
- 调用 `baizhi_ai_web_search` 做一次真实 AI 搜索
- 输出简要 JSON 结果
- 当任一测试失败时返回非零退出码

## 快速验证

在配置好 `.env` 后，可直接运行：

```bash
python3 test_baizhi_tools.py
```
