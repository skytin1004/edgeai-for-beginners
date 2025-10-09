<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T21:44:23+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "hu"
}
-->
# Workshop Szkriptek

Ez a könyvtár automatizálási és támogatási szkripteket tartalmaz, amelyek segítenek fenntartani a Workshop anyagok minőségét és konzisztenciáját.

## Tartalom

| Fájl | Cél |
|------|-----|
| `lint_markdown_cli.py` | Ellenőrzi a markdown kódfedéseket, hogy blokkolja az elavult Foundry Local CLI parancsmintákat. |
| `export_benchmark_markdown.py` | Több modell késleltetési benchmarkot futtat, és Markdown + JSON jelentéseket generál. |

## 1. Markdown CLI Minták Ellenőrzése

A `lint_markdown_cli.py` szkenneli az összes nem fordított `.md` fájlt az elavult Foundry Local CLI minták után **kódfedésekben** (``` ... ```). Az információs szöveg továbbra is említheti az elavult parancsokat történelmi kontextusban.

### Elavult Minták (Blokkolva Kódfedésekben)

Az ellenőrző blokkolja az elavult CLI mintákat. Használj modern alternatívákat helyettük.

### Szükséges Helyettesítések
| Elavult | Használj helyette |
|---------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Benchmark szkript + rendszereszközök (`Feladatkezelő`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Kilépési Kódok
| Kód | Jelentés |
|-----|----------|
| 0 | Nincs észlelt szabálysértés |
| 1 | Egy vagy több elavult minta található |

### Helyi Futtatás
A repozitórium gyökérkönyvtárából (ajánlott):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (Opcionális)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ez blokkolja azokat a commitokat, amelyek elavult mintákat vezetnek be.

### CI Integráció
Egy GitHub Action munkafolyamat (`.github/workflows/markdown-cli-lint.yml`) futtatja az ellenőrzőt minden push és pull request esetén a `main` és `Reactor` ágakon. A hibás munkák javítása kötelező a merge előtt.

### Új Elavult Minták Hozzáadása
1. Nyisd meg a `lint_markdown_cli.py` fájlt.
2. Adj hozzá egy `(regex, suggestion)` tuple-t a `DEPRECATED` listához. Használj nyers stringet, és tartalmazz `\b` szóhatárokat, ahol szükséges.
3. Futtasd az ellenőrzőt helyileg, hogy megbizonyosodj a felismerésről.
4. Commitolj és pusholj; a CI érvényesíti az új szabályt.

Példa hozzáadás:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Magyarázó Említések Engedélyezése
Mivel csak a kódfedések vannak érvényesítve, az elavult parancsokat biztonságosan leírhatod narratív szövegben. Ha *muszáj* megmutatni őket egy fedésben kontrasztként, használj fedést **három backtick nélkül** (pl. behúzás vagy idézet), vagy írd át pszeudo formára.

### Specifikus Fájlok Kihagyása (Haladó)
Ha szükséges, helyezd a régi példákat egy külön fájlba a repozitóriumon kívül, vagy nevezd át más kiterjesztéssel tervezés közben. A fordított példányok automatikus kihagyása (a `translations` útvonalakat tartalmazó fájlok) alapértelmezett.

### Hibakeresés
| Probléma | Ok | Megoldás |
|----------|----|----------|
| Az ellenőrző megjelöl egy általad frissített sort | Regex túl általános | Szűkítsd a mintát további szóhatárral (`\b`) vagy horgonyokkal |
| CI hibázik, de helyileg sikeres | Eltérő Python verzió vagy nem commitolt változások | Futtasd újra helyileg, győződj meg a tiszta munkafáról, ellenőrizd a munkafolyamat Python verzióját (3.11) |
| Ideiglenes megkerülés szükséges | Sürgős javítás | Alkalmazd a javítást azonnal utána; fontold meg egy ideiglenes ág és követő PR használatát (kerüld a megkerülő kapcsolók hozzáadását) |

### Indoklás
A dokumentáció *aktuális* stabil CLI felülethez igazítása csökkenti a workshop nehézségeit, elkerüli a tanulók zavartságát, és központosítja a teljesítménymérést karbantartott Python szkripteken keresztül, a sodródó CLI alparancsok helyett.

---
A workshop minőségi eszközláncának részeként karbantartva. Fejlesztésekhez (pl. automatikus javítási javaslatok vagy HTML jelentés generálás), nyiss egy hibajegyet vagy küldj be egy PR-t.

## 2. Minta Ellenőrző Szkript

A `validate_samples.py` ellenőrzi az összes Python minta fájlt szintaxis, importok és legjobb gyakorlatok betartása szempontjából.

### Használat
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

### Amit ellenőriz
- ✅ Python szintaxis érvényessége
- ✅ Szükséges importok jelenléte
- ✅ Hibakezelés implementációja (részletes mód)
- ✅ Típusjelölések használata (részletes mód)
- ✅ Funkció docstringek (részletes mód)
- ✅ SDK referencia linkek (részletes mód)

### Környezeti Változók
- `SKIP_IMPORT_CHECK=1` - Import ellenőrzés kihagyása
- `SKIP_SYNTAX_CHECK=1` - Szintaxis ellenőrzés kihagyása

### Kilépési Kódok
- `0` - Minden minta megfelelt az ellenőrzésen
- `1` - Egy vagy több minta nem felelt meg

## 3. Minta Teszt Futtató

A `test_samples.py` füstteszteket futtat az összes mintán, hogy ellenőrizze, hibamentesen végrehajthatók-e.

### Használat
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

### Előfeltételek
- Foundry Local szolgáltatás fut: `foundry service start`
- Modellek betöltve: `foundry model run phi-4-mini`
- Függőségek telepítve: `pip install -r requirements.txt`

### Amit tesztel
- ✅ A minta hibamentesen végrehajtható
- ✅ A szükséges kimenet generálódik
- ✅ Megfelelő hibakezelés hiba esetén
- ✅ Teljesítmény (végrehajtási idő)

### Környezeti Változók
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Teszteléshez használt modell
- `TEST_TIMEOUT=30` - Időtúllépés mintánként másodpercben

### Várható Hibák
Néhány teszt sikertelen lehet, ha opcionális függőségek nincsenek telepítve (pl. `ragas`, `sentence-transformers`). Telepítés:
```bash
pip install sentence-transformers ragas datasets
```

### Kilépési Kódok
- `0` - Minden teszt sikeres
- `1` - Egy vagy több teszt sikertelen

## 4. Benchmark Markdown Exportáló

Szkript: `export_benchmark_markdown.py`

Reprodukálható teljesítménytáblázatot generál modellek egy csoportjához.

### Használat
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Kimenetek
| Fájl | Leírás |
|------|--------|
| `benchmark_report.md` | Markdown táblázat (átlag, p95, tokenek/másodperc, opcionális első token) |
| `benchmark_report.json` | Nyers metrikák tömbje összehasonlításhoz és történethez |

### Opciók
| Flag | Leírás | Alapértelmezett |
|------|--------|-----------------|
| `--models` | Modell aliasok vesszővel elválasztva | (kötelező) |
| `--prompt` | Minden körben használt prompt | (kötelező) |
| `--rounds` | Körök száma modellenként | 3 |
| `--output` | Markdown kimeneti fájl | `benchmark_report.md` |
| `--json` | JSON kimeneti fájl | `benchmark_report.json` |
| `--fail-on-empty` | Nem nulla kilépés, ha minden benchmark sikertelen | kikapcsolva |

A `BENCH_STREAM=1` környezeti változó hozzáadja az első token késleltetési mérést.

### Megjegyzések
- Újrahasználja a `workshop_utils`-t a konzisztens modell bootstraphez és gyorsítótárazáshoz.
- Ha más munkakönyvtárból futtatod, a szkript megpróbálja megtalálni a `workshop_utils`-t útvonal visszaesésekkel.
- GPU összehasonlításhoz: futtasd egyszer, engedélyezd a gyorsítást CLI konfiguráción keresztül, futtasd újra, és hasonlítsd össze a JSON-t.

---

**Felelősségkizárás**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.