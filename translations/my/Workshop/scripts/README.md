<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T12:22:55+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "my"
}
-->
# Workshop Scripts

ဒီ directory မှာ Workshop materials တွေမှာ အရည်အသွေးနဲ့ တိကျမှုကို ထိန်းသိမ်းဖို့ အသုံးပြုတဲ့ automation နဲ့ support scripts တွေ ပါဝင်ပါတယ်။

## Contents

| ဖိုင် | ရည်ရွယ်ချက် |
|------|-------------|
| `lint_markdown_cli.py` | Markdown code fences တွေကို Foundry Local CLI command patterns ရှေးမီပုံစံတွေကို ပိတ်ဆို့ဖို့ စစ်ဆေးပါတယ်။ |
| `export_benchmark_markdown.py` | Multi-model latency benchmark ကို run လုပ်ပြီး Markdown + JSON အစီရင်ခံစာတွေ ထုတ်ပေးပါတယ်။ |

## 1. Markdown CLI Pattern Linter

`lint_markdown_cli.py` က translation မဟုတ်တဲ့ `.md` ဖိုင်တွေကို Foundry Local CLI ရှေးမီ pattern တွေကို **fenced code blocks** (``` ... ```) အတွင်းမှာ စစ်ဆေးပါတယ်။ သမိုင်းနောက်ခံအနေဖြင့် ရှေးမီ command တွေကို informational prose မှာ ဖော်ပြနိုင်ပါတယ်။

### ရှေးမီပုံစံများ (Code Fences အတွင်း ပိတ်ဆို့ထားသည်)

Linter က ရှေးမီ CLI pattern တွေကို ပိတ်ဆို့ထားပါတယ်။ အခေတ်သစ် alternative တွေကို အသုံးပြုပါ။

### လိုအပ်သော အစားထိုးများ
| ရှေးမီ | အစားထိုးအသုံးပြုရန် |
|--------|---------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Exit Codes
| Code | အဓိပ္ပါယ် |
|------|----------|
| 0 | မည်သည့် ပျက်ကွက်မှုမှ မတွေ့ရှိ |
| 1 | ရှေးမီ pattern တစ်ခုခု တွေ့ရှိ |

### Local မှာ Run လုပ်ခြင်း
Repository root မှ (အကြံပြုထားသည်):

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
ဤသည်မှာ ရှေးမီ pattern တွေကို ထည့်သွင်းတဲ့ commit များကို ပိတ်ဆို့သည်။

### CI Integration
GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) က `main` နဲ့ `Reactor` branches တွေကို push နဲ့ pull request တိုင်းမှာ run လုပ်ပါတယ်။ Failing jobs တွေကို merge လုပ်မီ ပြင်ဆင်ရမည်။

### ရှေးမီ Pattern အသစ်များ ထည့်သွင်းခြင်း
1. `lint_markdown_cli.py` ကို ဖွင့်ပါ။
2. `DEPRECATED` list မှာ `(regex, suggestion)` tuple ကို ထည့်သွင်းပါ။ Raw string ကို အသုံးပြုပြီး `\b` word boundaries ကို လိုအပ်သလို ထည့်ပါ။
3. Local မှာ linter ကို run လုပ်ပြီး detection ကို စစ်ဆေးပါ။
4. Commit နဲ့ push လုပ်ပါ။ CI က rule အသစ်ကို အတည်ပြုပါမည်။

ဥပမာ ထည့်သွင်းမှု:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### ရှင်းလင်းဖော်ပြမှုများ ခွင့်ပြုခြင်း
Fenced code blocks တွေကိုသာ enforce လုပ်ထားသောကြောင့် narrative text မှာ ရှေးမီ command တွေကို ဖော်ပြနိုင်ပါတယ်။ Fence အတွင်းမှာ contrast အတွက် ဖော်ပြရန်လိုအပ်ပါက triple backticks မပါသော fenced block (ဥပမာ indent သို့မဟုတ် quote) သို့မဟုတ် pseudo form အဖြစ် ပြန်ရေးပါ။

### Specific Files ကို Skip လုပ်ခြင်း (Advanced)
လိုအပ်ပါက legacy examples တွေကို repo အပြင်မှာ သီးသန့်ဖိုင်အဖြစ် ထည့်သွင်းပါ။ သို့မဟုတ် draft လုပ်နေစဉ်မှာ extension ကို ပြောင်းပါ။ Translated copies တွေအတွက် intentional skips တွေကို automatic လုပ်ထားပါသည် (paths တွေမှာ `translations` ပါဝင်ပါက).

### Troubleshooting
| ပြဿနာ | အကြောင်းရင်း | ဖြေရှင်းနည်း |
|-------|-------------|-------------|
| Linter က သင်ပြင်ဆင်ထားသော line ကို flag လုပ်သည် | Regex အကျယ်အဝန်း များသည် | Word boundary (`\b`) သို့မဟုတ် anchors ဖြင့် pattern ကို ကျဉ်းပါ |
| CI fail ဖြစ်ပြီး Local pass ဖြစ်သည် | Python version မတူညီခြင်း သို့မဟုတ် uncommitted changes | Local မှာ ပြန် run လုပ်ပါ၊ clean working tree ဖြစ်စေပါ၊ workflow Python version (3.11) ကို စစ်ဆေးပါ |
| အချိန်ပိုင်း bypass လုပ်ရန်လိုအပ် | အရေးပေါ် hotfix | Fix ကို ချက်ချင်း ပြုလုပ်ပါ၊ temporary branch နဲ့ follow-up PR ကို အသုံးပြုပါ (bypass switches ထည့်သွင်းခြင်းကို ရှောင်ရှားပါ) |

### Rationale
Documentation ကို *လက်ရှိ* stable CLI surface နဲ့ အညီထားခြင်းက workshop friction ကို လျော့ချပြီး သင်ယူသူတွေကို ရှုပ်ထွေးမှုမဖြစ်စေဘဲ performance measurement ကို Python scripts တွေမှတစ်ဆင့် centralized လုပ်နိုင်စေပါတယ်။

---
Workshop quality toolchain ရဲ့ အစိတ်အပိုင်းအနေနဲ့ ထိန်းသိမ်းထားသည်။ အဆင့်မြှင့်တင်မှုများ (ဥပမာ auto-fixing suggestions သို့မဟုတ် HTML report generation) အတွက် issue တစ်ခု ဖွင့်ပါ သို့မဟုတ် PR တင်ပါ။

## 2. Sample Validation Script

`validate_samples.py` က Python sample ဖိုင်အားလုံးကို syntax, imports, နဲ့ best practices compliance အတွက် validate လုပ်ပါသည်။

### အသုံးပြုနည်း
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

### စစ်ဆေးသည့်အရာများ
- ✅ Python syntax မှန်ကန်မှု
- ✅ လိုအပ်သော imports ရှိမှု
- ✅ Error handling implementation (verbose mode)
- ✅ Type hints အသုံးပြုမှု (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ SDK reference links (verbose mode)

### Environment Variables
- `SKIP_IMPORT_CHECK=1` - Import validation ကို skip လုပ်ပါ
- `SKIP_SYNTAX_CHECK=1` - Syntax validation ကို skip လုပ်ပါ

### Exit Codes
- `0` - Sample အားလုံး pass ဖြစ်သည်
- `1` - Sample တစ်ခုခု fail ဖြစ်သည်

## 3. Sample Test Runner

`test_samples.py` က sample အားလုံးကို smoke test run လုပ်ပြီး error မရှိဘဲ အလုပ်လုပ်နိုင်မှုကို စစ်ဆေးသည်။

### အသုံးပြုနည်း
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

### လိုအပ်ချက်များ
- Foundry Local service run လုပ်နေသည်: `foundry service start`
- Models load လုပ်ထားသည်: `foundry model run phi-4-mini`
- Dependencies install လုပ်ထားသည်: `pip install -r requirements.txt`

### စစ်ဆေးသည့်အရာများ
- ✅ Sample က runtime errors မရှိဘဲ အလုပ်လုပ်နိုင်မှု
- ✅ လိုအပ်သော output ထုတ်ပေးမှု
- ✅ Fail ဖြစ်ပါက error handling မှန်ကန်မှု
- ✅ Performance (execution time)

### Environment Variables
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Test အတွက် အသုံးပြုမည့် model
- `TEST_TIMEOUT=30` - Sample တစ်ခုစီအတွက် timeout (seconds)

### မျှော်လင့်ထားသော Failures
Optional dependencies မရှိပါက test fail ဖြစ်နိုင်သည် (ဥပမာ `ragas`, `sentence-transformers`)။ Install လုပ်ရန်:
```bash
pip install sentence-transformers ragas datasets
```

### Exit Codes
- `0` - Test အားလုံး pass ဖြစ်သည်
- `1` - Test တစ်ခုခု fail ဖြစ်သည်

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Models အစုတစ်စုအတွက် reproducible performance table ကို ထုတ်ပေးသည်။

### အသုံးပြုနည်း
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| ဖိုင် | ဖော်ပြချက် |
|------|------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array (diffing & history အတွက်) |

### Options
| Flag | ဖော်ပြချက် | Default |
|------|------------|---------|
| `--models` | Comma-separated model aliases | (required) |
| `--prompt` | Prompt used each round | (required) |
| `--rounds` | Rounds per model | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Benchmark အားလုံး fail ဖြစ်ပါက non-zero exit | off |

Environment variable `BENCH_STREAM=1` က first token latency measurement ကို ထည့်သွင်းသည်။

### Notes
- `workshop_utils` ကို အသုံးပြုပြီး model bootstrap & caching ကို consistency ရှိစေသည်။
- အခြား working directory မှ run လုပ်ပါက script က `workshop_utils` ကို path fallbacks ဖြင့် ရှာဖွေပါမည်။
- GPU comparison အတွက်: တစ်ကြိမ် run လုပ်ပြီး CLI config မှ acceleration ကို enable လုပ်ပါ၊ ပြန် run လုပ်ပြီး JSON ကို diff လုပ်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။