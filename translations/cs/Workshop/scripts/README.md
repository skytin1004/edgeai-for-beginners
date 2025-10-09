<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T21:44:50+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "cs"
}
-->
# Skripty Workshopu

Tento adresář obsahuje automatizační a podpůrné skripty používané k udržení kvality a konzistence materiálů Workshopu.

## Obsah

| Soubor | Účel |
|--------|------|
| `lint_markdown_cli.py` | Kontroluje bloky kódu v Markdownu, aby zablokoval zastaralé vzory příkazů Foundry Local CLI. |
| `export_benchmark_markdown.py` | Spouští benchmark latence pro více modelů a generuje zprávy ve formátu Markdown + JSON. |

## 1. Kontrola vzorů CLI v Markdownu

`lint_markdown_cli.py` prohledává všechny `.md` soubory, které nejsou překlady, a hledá zakázané vzory Foundry Local CLI **uvnitř bloků kódu** (``` ... ```). Informační text může stále zmiňovat zastaralé příkazy pro historický kontext.

### Zastaralé vzory (blokované uvnitř bloků kódu)

Kontrola blokuje zastaralé vzory CLI. Používejte moderní alternativy.

### Požadované náhrady
| Zastaralé | Použijte místo toho |
|-----------|---------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skript benchmarku + systémové nástroje (`Správce úloh`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Výstupní kódy
| Kód | Význam |
|-----|--------|
| 0 | Nebyly nalezeny žádné porušení |
| 1 | Byly nalezeny jeden nebo více zastaralých vzorů |

### Spuštění lokálně
Z kořenového adresáře repozitáře (doporučeno):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit hook (volitelné)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Tím se zablokují commity, které zavádějí zastaralé vzory.

### Integrace CI
Workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) spouští kontrolu při každém pushi a pull requestu do větví `main` a `Reactor`. Neúspěšné úlohy musí být opraveny před sloučením.

### Přidání nových zastaralých vzorů
1. Otevřete `lint_markdown_cli.py`.
2. Přidejte dvojici `(regex, suggestion)` do seznamu `DEPRECATED`. Použijte raw string a zahrňte hranice slov `\b`, kde je to vhodné.
3. Spusťte kontrolu lokálně, abyste ověřili detekci.
4. Commitujte a pushněte; CI bude vynucovat nové pravidlo.

Příklad přidání:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Povolení vysvětlujících zmínek
Protože jsou vynucovány pouze bloky kódu, můžete bezpečně popisovat zastaralé příkazy v narativním textu. Pokud je *nutné* je ukázat uvnitř bloku, použijte blok **bez** trojitých zpětných apostrofů (např. odsazení nebo citaci) nebo přepište do pseudo formy.

### Přeskakování specifických souborů (pokročilé)
Pokud je to nutné, umístěte příklady do samostatného souboru mimo repozitář nebo přejmenujte s jinou příponou během návrhu. Záměrné přeskakování pro překlady je automatické (cesty obsahující `translations`).

### Řešení problémů
| Problém | Příčina | Řešení |
|---------|---------|--------|
| Kontrola označuje řádek, který jste upravili | Regex je příliš obecný | Zúžte vzor přidáním dalších hranic slov (`\b`) nebo kotv |
| CI selhává, ale lokálně prochází | Odlišná verze Pythonu nebo necommitované změny | Spusťte znovu lokálně, zajistěte čistý pracovní strom, zkontrolujte verzi Pythonu ve workflow (3.11) |
| Potřeba dočasného obejití | Nouzová oprava | Aplikujte opravu ihned poté; zvažte použití dočasné větve a následného PR (vyhněte se přidávání přepínačů pro obejití) |

### Důvod
Udržování dokumentace v souladu s *aktuálním* stabilním CLI povrchem zabraňuje problémům při workshopu, vyhýbá se zmatení účastníků a centralizuje měření výkonu prostřednictvím udržovaných Python skriptů místo zastaralých CLI podpříkazů.

---
Udržováno jako součást nástrojového řetězce kvality workshopu. Pro vylepšení (např. automatické opravy návrhů nebo generování HTML zpráv) otevřete issue nebo odešlete PR.

## 2. Skript pro validaci ukázek

`validate_samples.py` validuje všechny Python ukázkové soubory z hlediska syntaxe, importů a souladu s nejlepšími postupy.

### Použití
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

### Co kontroluje
- ✅ Platnost syntaxe Pythonu
- ✅ Přítomnost požadovaných importů
- ✅ Implementace zpracování chyb (verbose režim)
- ✅ Použití typových anotací (verbose režim)
- ✅ Dokumentace funkcí (verbose režim)
- ✅ Odkazy na SDK (verbose režim)

### Proměnné prostředí
- `SKIP_IMPORT_CHECK=1` - Přeskočí validaci importů
- `SKIP_SYNTAX_CHECK=1` - Přeskočí validaci syntaxe

### Výstupní kódy
- `0` - Všechny ukázky prošly validací
- `1` - Jedna nebo více ukázek neprošla

## 3. Testovací skript pro ukázky

`test_samples.py` provádí základní testy všech ukázek, aby ověřil, že se spouštějí bez chyb.

### Použití
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

### Předpoklady
- Běží služba Foundry Local: `foundry service start`
- Načtené modely: `foundry model run phi-4-mini`
- Nainstalované závislosti: `pip install -r requirements.txt`

### Co testuje
- ✅ Ukázka se spustí bez chyb za běhu
- ✅ Generuje požadovaný výstup
- ✅ Správné zpracování chyb při selhání
- ✅ Výkon (doba provedení)

### Proměnné prostředí
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model použitý pro testování
- `TEST_TIMEOUT=30` - Časový limit na ukázku v sekundách

### Očekávané chyby
Některé testy mohou selhat, pokud nejsou nainstalovány volitelné závislosti (např. `ragas`, `sentence-transformers`). Nainstalujte pomocí:
```bash
pip install sentence-transformers ragas datasets
```

### Výstupní kódy
- `0` - Všechny testy prošly
- `1` - Jeden nebo více testů selhal

## 4. Exportér benchmarků do Markdownu

Skript: `export_benchmark_markdown.py`

Generuje reprodukovatelnou tabulku výkonu pro sadu modelů.

### Použití
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Výstupy
| Soubor | Popis |
|--------|-------|
| `benchmark_report.md` | Tabulka v Markdownu (průměr, p95, tokeny/sekundu, volitelně první token) |
| `benchmark_report.json` | Surové metriky pro porovnání a historii |

### Volby
| Přepínač | Popis | Výchozí |
|----------|-------|---------|
| `--models` | Alias modelů oddělený čárkou | (povinné) |
| `--prompt` | Prompt použitý v každém kole | (povinné) |
| `--rounds` | Počet kol na model | 3 |
| `--output` | Výstupní soubor Markdownu | `benchmark_report.md` |
| `--json` | Výstupní soubor JSON | `benchmark_report.json` |
| `--fail-on-empty` | Neúspěšný výstup, pokud všechny benchmarky selžou | vypnuto |

Proměnná prostředí `BENCH_STREAM=1` přidává měření latence prvního tokenu.

### Poznámky
- Využívá `workshop_utils` pro konzistentní inicializaci modelů a cachování.
- Pokud je spuštěn z jiného pracovního adresáře, skript se pokusí o fallback cesty k nalezení `workshop_utils`.
- Pro porovnání GPU: spusťte jednou, povolte akceleraci přes konfiguraci CLI, spusťte znovu a porovnejte JSON.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.