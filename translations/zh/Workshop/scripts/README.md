<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T16:37:02+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "zh"
}
-->
# 工作坊脚本

此目录包含用于维护工作坊材料质量和一致性的自动化和支持脚本。

## 内容

| 文件 | 用途 |
|------|------|
| `lint_markdown_cli.py` | 检查 Markdown 代码块中是否存在已弃用的 Foundry Local CLI 命令模式。 |
| `export_benchmark_markdown.py` | 运行多模型延迟基准测试并生成 Markdown 和 JSON 报告。 |

## 1. Markdown CLI 模式检查器

`lint_markdown_cli.py` 会扫描所有非翻译的 `.md` 文件，查找 **代码块**（``` ... ```）中不允许的 Foundry Local CLI 模式。信息性文本仍可提及已弃用的命令以提供历史背景。

### 已弃用模式（代码块中禁止使用）

检查器会阻止使用已弃用的 CLI 模式，请使用现代替代方案。

### 必须替换的内容
| 已弃用 | 替代方案 |
|--------|----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | 基准测试脚本 + 系统工具（如 `任务管理器`、`nvidia-smi`） |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 退出代码
| 代码 | 含义 |
|------|------|
| 0 | 未检测到违规 |
| 1 | 检测到一个或多个已弃用模式 |

### 本地运行
从仓库根目录运行（推荐）：

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### 预提交钩子（可选）
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
此功能会阻止引入已弃用模式的提交。

### CI 集成
GitHub Action 工作流（`.github/workflows/markdown-cli-lint.yml`）会在每次推送和对 `main` 和 `Reactor` 分支的拉取请求时运行检查器。失败的任务必须修复后才能合并。

### 添加新的已弃用模式
1. 打开 `lint_markdown_cli.py`。
2. 将一个元组 `(regex, suggestion)` 添加到 `DEPRECATED` 列表中。使用原始字符串，并在适当位置包含 `\b` 单词边界。
3. 本地运行检查器以验证检测效果。
4. 提交并推送；CI 将强制执行新规则。

示例添加：
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### 允许解释性提及
由于仅强制代码块，您可以在叙述性文本中安全地描述已弃用的命令。如果您 *必须* 在代码块中展示它们以作对比，请使用 **非三引号** 的代码块（例如，缩进或引用），或改写为伪形式。

### 跳过特定文件（高级）
如有需要，可将遗留示例放在仓库外的单独文件中，或在草稿阶段重命名为其他扩展名。翻译副本的意图性跳过是自动的（路径包含 `translations`）。

### 故障排除
| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 检查器标记了您更新的行 | 正则表达式过于宽泛 | 使用额外的单词边界（`\b`）或锚点缩小模式范围 |
| CI 失败但本地通过 | Python 版本不同或未提交的更改 | 本地重新运行，确保工作树干净，检查工作流 Python 版本（3.11） |
| 需要临时绕过 | 紧急修复 | 修复后立即应用；考虑使用临时分支和后续 PR（避免添加绕过开关） |

### 原因
保持文档与 *当前* 稳定的 CLI 接口一致，可以减少工作坊中的摩擦，避免学习者的困惑，并通过维护的 Python 脚本集中性能测量，而不是使用不一致的 CLI 子命令。

---
作为工作坊质量工具链的一部分进行维护。如需增强功能（例如自动修复建议或 HTML 报告生成），请提交问题或 PR。

## 2. 示例验证脚本

`validate_samples.py` 验证所有 Python 示例文件的语法、导入和最佳实践合规性。

### 使用方法
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### 检查内容
- ✅ Python 语法有效性
- ✅ 必需的导入是否存在
- ✅ 错误处理实现（详细模式）
- ✅ 类型提示使用（详细模式）
- ✅ 函数文档字符串（详细模式）
- ✅ SDK 参考链接（详细模式）

### 环境变量
- `SKIP_IMPORT_CHECK=1` - 跳过导入验证
- `SKIP_SYNTAX_CHECK=1` - 跳过语法验证

### 退出代码
- `0` - 所有示例通过验证
- `1` - 一个或多个示例未通过验证

## 3. 示例测试运行器

`test_samples.py` 对所有示例运行冒烟测试，以验证它们是否可以正常执行。

### 使用方法
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### 前提条件
- Foundry Local 服务正在运行：`foundry service start`
- 模型已加载：`foundry model run phi-4-mini`
- 依赖已安装：`pip install -r requirements.txt`

### 测试内容
- ✅ 示例可以正常执行，无运行时错误
- ✅ 生成所需输出
- ✅ 失败时正确的错误处理
- ✅ 性能（执行时间）

### 环境变量
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - 用于测试的模型
- `TEST_TIMEOUT=30` - 每个示例的超时时间（秒）

### 预期失败
如果未安装可选依赖项（例如 `ragas`、`sentence-transformers`），某些测试可能会失败。安装方法：
```bash
pip install sentence-transformers ragas datasets
```

### 退出代码
- `0` - 所有测试通过
- `1` - 一个或多个测试失败

## 4. 基准测试 Markdown 导出器

脚本：`export_benchmark_markdown.py`

为一组模型生成可复现的性能表。

### 使用方法
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### 输出
| 文件 | 描述 |
|------|------|
| `benchmark_report.md` | Markdown 表格（平均值、p95、每秒令牌数、可选首令牌） |
| `benchmark_report.json` | 原始指标数组，用于差异比较和历史记录 |

### 选项
| 标志 | 描述 | 默认值 |
|------|------|--------|
| `--models` | 逗号分隔的模型别名 | （必需） |
| `--prompt` | 每轮使用的提示 | （必需） |
| `--rounds` | 每个模型的轮数 | 3 |
| `--output` | Markdown 输出文件 | `benchmark_report.md` |
| `--json` | JSON 输出文件 | `benchmark_report.json` |
| `--fail-on-empty` | 如果所有基准测试失败则返回非零退出码 | 关闭 |

环境变量 `BENCH_STREAM=1` 添加首令牌延迟测量。

### 注意事项
- 重用 `workshop_utils` 以确保模型启动和缓存的一致性。
- 如果从不同的工作目录运行，脚本会尝试路径回退以定位 `workshop_utils`。
- 对于 GPU 比较：运行一次，启用 CLI 配置中的加速功能，重新运行并比较 JSON。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。