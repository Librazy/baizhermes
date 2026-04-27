# Baizhi Hermes Plugin

这个仓库实现了一个 Hermes Agent 插件，将百智云搜索服务注册为 Tool Call：

- `baizhi_web_search`
- `baizhi_ai_web_search`
- `baizhi_img_search`

## 环境变量配置

插件会根据可用 API Key 动态注册 Tool Call：

- 存在 `BAIZHI_WEB_SEARCH_API_KEY` 时注册 `baizhi_web_search` 和 `baizhi_ai_web_search`
- 存在 `BAIZHI_IMG_SEARCH_API_KEY` 时注册 `baizhi_img_search`

请在项目根目录创建 `.env` 文件，并写入以下内容：

```dotenv
BAIZHI_WEB_SEARCH_API_KEY=<YOUR_BAIZHI_WEB_SEARCH_API_KEY>
BAIZHI_IMG_SEARCH_API_KEY=<YOUR_BAIZHI_IMG_SEARCH_API_KEY>
```

说明：

- 不要把真实 token 写进代码文件。
- `.env` 已在 `.gitignore` 中忽略，不会默认提交到仓库。
- 两类 API Key 相互独立，只配置其中一个时也会注册对应工具。

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

### `baizhi_img_search`

用于调用百智云图片搜索接口，返回图片 URL、宽度、高度等元数据。

支持参数：

- `query`: 图片搜索关键词，必填
- `count`: 图片结果数量，范围 `1-5`
- `image.width_min`: 最小图片宽度
- `image.height_min`: 最小图片高度
- `image.width_max`: 最大图片宽度
- `image.height_max`: 最大图片高度

## 本地回归测试

仓库提供了一个本地测试脚本：`test_baizhi_tools.py`。

执行方式：

```bash
python3 test_baizhi_tools.py
```

脚本会：

- 从项目根目录 `.env` 加载百智云 API Key
- 配置 `BAIZHI_WEB_SEARCH_API_KEY` 时，调用 `baizhi_web_search` 和 `baizhi_ai_web_search`
- 配置 `BAIZHI_IMG_SEARCH_API_KEY` 时，调用 `baizhi_img_search`
- 输出简要 JSON 结果
- 当任一测试失败时返回非零退出码

## 快速验证

在配置好 `.env` 后，可直接运行：

```bash
python3 test_baizhi_tools.py
```
