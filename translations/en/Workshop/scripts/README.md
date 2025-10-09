<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T21:43:43+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "en"
}
-->
# Workshop Scripts

This directory contains automation and support scripts designed to ensure quality and consistency across the Workshop materials.

## Contents

| File | Purpose |
|------|---------|
| `lint_markdown_cli.py` | Checks markdown code fences for deprecated Foundry Local CLI command patterns. |
| `export_benchmark_markdown.py` | Executes multi-model latency benchmarks and generates Markdown + JSON reports. |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` scans all non-translation `.md` files for prohibited Foundry Local CLI patterns **within fenced code blocks** (``` ... ```). Informational text can still reference deprecated commands for historical context.

### Deprecated Patterns (Blocked Inside Code Fences)

The linter flags deprecated CLI patterns. Use updated alternatives instead.

### Required Replacements
| Deprecated | Use Instead |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit Codes
| Code | Meaning |
|------|---------|
| 0 | No violations found |
| 1 | One or more deprecated patterns detected |

### Running Locally
From the repository root (recommended):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Optional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
This prevents commits that introduce deprecated patterns.

### CI Integration
A GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) runs the linter on every push and pull request to the `main` and `Reactor` branches. Failing jobs must be resolved before merging.

### Adding New Deprecated Patterns
1. Open `lint_markdown_cli.py`.
2. Add a tuple `(regex, suggestion)` to the `DEPRECATED` list. Use raw strings and include `\b` word boundaries where applicable.
3. Run the linter locally to confirm detection.
4. Commit and push; CI will enforce the new rule.

Example addition:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Allowing Explanatory Mentions
Since enforcement applies only to fenced code blocks, you can safely describe deprecated commands in narrative text. If you *must* show them inside a fence for comparison, use a fenced block **without** triple backticks (e.g., indent or quote) or rewrite them in pseudo form.

### Skipping Specific Files (Advanced)
If necessary, place legacy examples in a separate file outside the repository or rename them with a different extension while drafting. Translated copies are automatically excluded (paths containing `translations`).

### Troubleshooting
| Issue | Cause | Resolution |
|-------|-------|-----------|
| Linter flags a line you updated | Regex too broad | Refine the pattern with additional word boundaries (`\b`) or anchors |
| CI fails but local passes | Different Python version or uncommitted changes | Re-run locally, ensure a clean working tree, and check the workflow Python version (3.11) |
| Need to temporarily bypass | Emergency hotfix | Apply the fix immediately afterward; consider using a temporary branch and follow-up PR (avoid adding bypass switches) |

### Rationale
Aligning documentation with the *current* stable CLI surface minimizes workshop friction, reduces learner confusion, and centralizes performance measurement through maintained Python scripts rather than outdated CLI subcommands.

---
Maintained as part of the workshop quality toolchain. For enhancements (e.g., auto-fixing suggestions or HTML report generation), open an issue or submit a PR.

## 2. Sample Validation Script

`validate_samples.py` checks all Python sample files for syntax, imports, and compliance with best practices.

### Usage
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

### What it checks
- ✅ Valid Python syntax
- ✅ Presence of required imports
- ✅ Implementation of error handling (verbose mode)
- ✅ Use of type hints (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ SDK reference links (verbose mode)

### Environment Variables
- `SKIP_IMPORT_CHECK=1` - Skip import validation
- `SKIP_SYNTAX_CHECK=1` - Skip syntax validation

### Exit Codes
- `0` - All samples passed validation
- `1` - One or more samples failed

## 3. Sample Test Runner

`test_samples.py` performs smoke tests on all samples to ensure they execute without errors.

### Usage
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

### Prerequisites
- Foundry Local service running: `foundry service start`
- Models loaded: `foundry model run phi-4-mini`
- Dependencies installed: `pip install -r requirements.txt`

### What it tests
- ✅ Sample executes without runtime errors
- ✅ Required output is generated
- ✅ Proper error handling in case of failure
- ✅ Performance (execution time)

### Environment Variables
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model used for testing
- `TEST_TIMEOUT=30` - Timeout per sample in seconds

### Expected Failures
Some tests may fail if optional dependencies are missing (e.g., `ragas`, `sentence-transformers`). Install them with:
```bash
pip install sentence-transformers ragas datasets
```

### Exit Codes
- `0` - All tests passed
- `1` - One or more tests failed

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Generates a reproducible performance table for a set of models.

### Usage
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| File | Description |
|------|-------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array for diffing & history |

### Options
| Flag | Description | Default |
|------|-------------|---------|
| `--models` | Comma-separated model aliases | (required) |
| `--prompt` | Prompt used for each round | (required) |
| `--rounds` | Rounds per model | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Non-zero exit if all benchmarks fail | off |

Environment variable `BENCH_STREAM=1` enables first token latency measurement.

### Notes
- Utilizes `workshop_utils` for consistent model initialization and caching.
- If executed from a different working directory, the script attempts path fallbacks to locate `workshop_utils`.
- For GPU comparison: run once, enable acceleration via CLI config, re-run, and compare the JSON outputs.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.