<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T19:32:53+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "tl"
}
-->
# Mga Script ng Workshop

Ang direktoryong ito ay naglalaman ng mga automation at support script na ginagamit upang mapanatili ang kalidad at pagkakapare-pareho sa mga materyales ng Workshop.

## Nilalaman

| File | Layunin |
|------|---------|
| `lint_markdown_cli.py` | Sini-check ang mga markdown code fences upang harangan ang mga deprecated na Foundry Local CLI command patterns. |
| `export_benchmark_markdown.py` | Nagpapatakbo ng multi-model latency benchmark at gumagawa ng Markdown + JSON na ulat. |

## 1. Markdown CLI Pattern Linter

Ang `lint_markdown_cli.py` ay nag-scan sa lahat ng non-translation `.md` files para sa mga hindi pinapayagang Foundry Local CLI patterns **sa loob ng fenced code blocks** (``` ... ```). Ang mga impormasyong prosa ay maaari pa ring magbanggit ng mga deprecated na command para sa historical na konteksto.

### Mga Deprecated na Pattern (Ipinagbabawal sa Loob ng Code Fences)

Hinaharangan ng linter ang mga deprecated na CLI patterns. Gumamit ng mga modernong alternatibo.

### Kinakailangang Kapalit
| Deprecated | Gamitin sa Halip |
|------------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark script + system tools (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Mga Exit Code
| Code | Kahulugan |
|------|-----------|
| 0 | Walang nakitang paglabag |
| 1 | May isa o higit pang deprecated na pattern na natagpuan |

### Pagpapatakbo sa Lokal
Mula sa repository root (inirerekomenda):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Opsyonal)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Hinaharangan nito ang mga commit na nagdadala ng mga deprecated na pattern.

### CI Integration
Ang workflow ng GitHub Action (`.github/workflows/markdown-cli-lint.yml`) ay nagpapatakbo ng linter sa bawat push at pull request sa `main` at `Reactor` branches. Ang mga nabigong trabaho ay kailangang ayusin bago mag-merge.

### Pagdaragdag ng Bagong Deprecated na Pattern
1. Buksan ang `lint_markdown_cli.py`.
2. Idagdag ang tuple `(regex, suggestion)` sa listahan ng `DEPRECATED`. Gumamit ng raw string at isama ang mga word boundary na `\b` kung kinakailangan.
3. Patakbuhin ang linter sa lokal upang tiyakin ang detection.
4. I-commit at i-push; ang CI ay magpapatupad ng bagong patakaran.

Halimbawa ng karagdagan:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Pahintulot sa Pagbanggit ng Paliwanag
Dahil ang enforcement ay para lamang sa fenced code blocks, maaari mong ilarawan ang mga deprecated na command sa narrative text nang ligtas. Kung *kailangan* mong ipakita ang mga ito sa loob ng fence para sa contrast, magdagdag ng fenced block **nang walang** triple backticks (hal., indent o quote) o isulat sa pseudo form.

### Pag-skip sa Partikular na Files (Advanced)
Kung kinakailangan, ilagay ang mga legacy na halimbawa sa isang hiwalay na file sa labas ng repo o palitan ang pangalan gamit ang ibang extension habang nagda-draft. Ang mga intentional na skip para sa mga isinaling kopya ay awtomatiko (mga path na naglalaman ng `translations`).

### Pag-aayos ng Problema
| Isyu | Sanhi | Solusyon |
|------|-------|----------|
| Na-flag ng linter ang linya na binago mo | Regex masyadong malawak | Palawakin ang pattern gamit ang karagdagang word boundary (`\b`) o anchors |
| Nabigo ang CI ngunit pumasa sa lokal | Iba't ibang bersyon ng Python o hindi na-commit na mga pagbabago | Patakbuhin muli sa lokal, tiyakin ang malinis na working tree, suriin ang workflow Python version (3.11) |
| Kailangang pansamantalang i-bypass | Emergency hotfix | Ilapat ang fix kaagad pagkatapos; isaalang-alang ang paggamit ng pansamantalang branch at follow-up PR (iwasan ang pagdaragdag ng bypass switches) |

### Rationale
Ang pagpapanatili ng dokumentasyon na naka-align sa *kasalukuyang* stable CLI surface ay pumipigil sa friction sa workshop, iniiwasan ang pagkalito ng mga learner, at sentralisado ang performance measurement sa pamamagitan ng maintained Python scripts sa halip na drifting CLI subcommands.

---
Pinapanatili bilang bahagi ng workshop quality toolchain. Para sa mga pagpapahusay (hal., auto-fixing suggestions o HTML report generation), magbukas ng isyu o magsumite ng PR.

## 2. Sample Validation Script

Ang `validate_samples.py` ay nagva-validate sa lahat ng Python sample files para sa syntax, imports, at pagsunod sa best practices.

### Paggamit
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

### Ano ang sine-check
- ✅ Validity ng Python syntax
- ✅ Presensya ng kinakailangang imports
- ✅ Implementasyon ng error handling (verbose mode)
- ✅ Paggamit ng type hints (verbose mode)
- ✅ Function docstrings (verbose mode)
- ✅ SDK reference links (verbose mode)

### Mga Environment Variable
- `SKIP_IMPORT_CHECK=1` - I-skip ang import validation
- `SKIP_SYNTAX_CHECK=1` - I-skip ang syntax validation

### Mga Exit Code
- `0` - Lahat ng samples ay pumasa sa validation
- `1` - May isa o higit pang samples na nabigo

## 3. Sample Test Runner

Ang `test_samples.py` ay nagpapatakbo ng smoke tests sa lahat ng samples upang tiyakin na ito ay tumatakbo nang walang error.

### Paggamit
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

### Mga Prerequisite
- Foundry Local service na tumatakbo: `foundry service start`
- Mga model na na-load: `foundry model run phi-4-mini`
- Mga dependency na naka-install: `pip install -r requirements.txt`

### Ano ang sine-check
- ✅ Ang sample ay maaaring tumakbo nang walang runtime errors
- ✅ Ang kinakailangang output ay nalilikha
- ✅ Tamang error handling sa failure
- ✅ Performance (execution time)

### Mga Environment Variable
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model na gagamitin para sa testing
- `TEST_TIMEOUT=30` - Timeout kada sample sa segundo

### Mga Inaasahang Pagkabigo
Ang ilang tests ay maaaring mabigo kung ang mga opsyonal na dependency ay hindi naka-install (hal., `ragas`, `sentence-transformers`). I-install gamit ang:
```bash
pip install sentence-transformers ragas datasets
```

### Mga Exit Code
- `0` - Lahat ng tests ay pumasa
- `1` - May isa o higit pang tests na nabigo

## 4. Benchmark Markdown Exporter

Script: `export_benchmark_markdown.py`

Gumagawa ng reproducible performance table para sa isang set ng models.

### Paggamit
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Outputs
| File | Deskripsyon |
|------|-------------|
| `benchmark_report.md` | Markdown table (avg, p95, tokens/sec, optional first token) |
| `benchmark_report.json` | Raw metrics array para sa diffing & history |

### Mga Opsyon
| Flag | Deskripsyon | Default |
|------|-------------|---------|
| `--models` | Comma-separated model aliases | (required) |
| `--prompt` | Prompt na ginamit bawat round | (required) |
| `--rounds` | Rounds bawat model | 3 |
| `--output` | Markdown output file | `benchmark_report.md` |
| `--json` | JSON output file | `benchmark_report.json` |
| `--fail-on-empty` | Non-zero exit kung lahat ng benchmarks ay nabigo | off |

Ang environment variable na `BENCH_STREAM=1` ay nagdadagdag ng first token latency measurement.

### Mga Tala
- Ginagamit ang `workshop_utils` para sa consistent na model bootstrap & caching.
- Kung patatakbuhin mula sa ibang working directory, sinusubukan ng script ang path fallbacks upang mahanap ang `workshop_utils`.
- Para sa GPU comparison: patakbuhin nang isang beses, i-enable ang acceleration sa pamamagitan ng CLI config, muling patakbuhin at i-diff ang JSON.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.