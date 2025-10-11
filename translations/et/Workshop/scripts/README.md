<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-11T12:03:45+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "et"
}
-->
# Töötoa skriptid

See kataloog sisaldab automatiseerimis- ja tugiskripte, mis aitavad säilitada kvaliteeti ja järjepidevust Töötoa materjalides.

## Sisu

| Fail | Eesmärk |
|------|---------|
| `lint_markdown_cli.py` | Kontrollib markdowni koodiplokke, et blokeerida vananenud Foundry Local CLI käsumustreid. |
| `export_benchmark_markdown.py` | Käitab mitme mudeli latentsuse võrdlusuuringut ja genereerib Markdown + JSON aruandeid. |

## 1. Markdown CLI mustrite kontrollija

`lint_markdown_cli.py` skaneerib kõiki mitte-tõlgitud `.md` faile, et tuvastada keelatud Foundry Local CLI mustreid **fenced koodiplokkides** (``` ... ```). Informatiivne tekst võib siiski mainida vananenud käske ajaloolise konteksti jaoks.

### Vananenud mustrid (blokeeritud koodiplokkides)

Kontrollija blokeerib vananenud CLI mustrid. Kasutage kaasaegseid alternatiive.

### Nõutavad asendused
| Vananenud | Kasutage asemel |
|-----------|----------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Võrdlusskript + süsteemitööriistad (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Väljumiskoodid
| Kood | Tähendus |
|------|----------|
| 0 | Rikkumisi ei tuvastatud |
| 1 | Üks või rohkem vananenud mustrit leitud |

### Kohalik käitamine
Käitage repo juurkataloogist (soovitatav):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (valikuline)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
See blokeerib commit'id, mis lisavad vananenud mustreid.

### CI integratsioon
GitHub Action töövoog (`.github/workflows/markdown-cli-lint.yml`) käitab kontrollija iga push'i ja pull request'i puhul `main` ja `Reactor` harudes. Ebaõnnestunud tööd tuleb parandada enne merge'i.

### Uute vananenud mustrite lisamine
1. Ava `lint_markdown_cli.py`.
2. Lisa tuple `(regex, suggestion)` `DEPRECATED` loendisse. Kasuta raw stringi ja lisa `\b` sõna piirid, kui vajalik.
3. Käivita kontrollija kohalikult, et veenduda tuvastamises.
4. Commit'i ja push'i; CI rakendab uue reegli.

Näide lisamisest:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Selgitavate mainimiste lubamine
Kuna ainult fenced koodiplokke kontrollitakse, võite kirjeldada vananenud käske narratiivses tekstis turvaliselt. Kui *peate* neid näitama plokis kontrasti jaoks, lisage plokk **ilma** kolmekordsete tagurpidi jutumärkideta (nt indent või tsitaat) või kirjutage pseudo vormis.

### Konkreetsete failide vahelejätmine (edasijõudnutele)
Kui vajalik, paigutage vanad näited eraldi faili väljaspool repo või nimetage ümber teise laiendiga koostamise ajal. Tõlgitud koopiate tahtlikud vahelejätmised on automaatsed (teed, mis sisaldavad `translations`).

### Tõrkeotsing
| Probleem | Põhjus | Lahendus |
|----------|--------|---------|
| Kontrollija märgib rea, mida uuendasite | Regex liiga lai | Kitsendage mustrit täiendava sõna piiriga (`\b`) või ankruga |
| CI ebaõnnestub, kuid kohalikult läbib | Erinev Python versioon või commitimata muudatused | Käivitage uuesti kohalikult, veenduge puhtas tööpuus, kontrollige töövoo Python versiooni (3.11) |
| Vajad ajutist möödumist | Kiirparandus | Rakendage parandus kohe pärast; kaaluge ajutise haru ja järgneva PR-i kasutamist (vältige möödumisvõimaluste lisamist) |

### Põhjendus
Dokumentatsiooni joondamine *praeguse* stabiilse CLI pinnaga väldib töötoa takistusi, hoiab ära õppijate segaduse ja tsentraliseerib jõudluse mõõtmise hooldatud Python skriptide kaudu, mitte hajutatud CLI alamkäskude kaudu.

---
Hooldatud osana töötoa kvaliteedi tööriistaketist. Täienduste jaoks (nt automaatsete paranduste soovitused või HTML aruande genereerimine) avage probleem või esitage PR.

## 2. Näidiste valideerimise skript

`validate_samples.py` valideerib kõik Python näidiste failid süntaksi, importide ja parimate tavade järgimise osas.

### Kasutamine
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

### Mida see kontrollib
- ✅ Pythoni süntaksi kehtivus
- ✅ Nõutud importide olemasolu
- ✅ Veakäsitluse rakendamine (verbose režiim)
- ✅ Tüüpide vihjete kasutamine (verbose režiim)
- ✅ Funktsioonide docstringid (verbose režiim)
- ✅ SDK viitelinkid (verbose režiim)

### Keskkonnamuutujad
- `SKIP_IMPORT_CHECK=1` - Jätab importide valideerimise vahele
- `SKIP_SYNTAX_CHECK=1` - Jätab süntaksi valideerimise vahele

### Väljumiskoodid
- `0` - Kõik näidised läbisid valideerimise
- `1` - Üks või rohkem näidist ebaõnnestus

## 3. Näidiste testimise skript

`test_samples.py` käitab suitsuteste kõigil näidistel, et kontrollida, kas need töötavad vigadeta.

### Kasutamine
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

### Eeldused
- Foundry Local teenus töötab: `foundry service start`
- Mudelid laaditud: `foundry model run phi-4-mini`
- Sõltuvused paigaldatud: `pip install -r requirements.txt`

### Mida see testib
- ✅ Näidis saab käituda ilma käitusvigadeta
- ✅ Nõutud väljund genereeritakse
- ✅ Õige veakäsitlus ebaõnnestumise korral
- ✅ Jõudlus (käitusaeg)

### Keskkonnamuutujad
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Mudel, mida testimiseks kasutada
- `TEST_TIMEOUT=30` - Aegumistähtaeg näidise kohta sekundites

### Oodatavad ebaõnnestumised
Mõned testid võivad ebaõnnestuda, kui valikulised sõltuvused pole paigaldatud (nt `ragas`, `sentence-transformers`). Paigaldage:
```bash
pip install sentence-transformers ragas datasets
```

### Väljumiskoodid
- `0` - Kõik testid läbisid
- `1` - Üks või rohkem teste ebaõnnestus

## 4. Võrdlusuuringu Markdown eksportija

Skript: `export_benchmark_markdown.py`

Genereerib korduvkasutatava jõudlustabeli mudelite komplekti jaoks.

### Kasutamine
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Väljundid
| Fail | Kirjeldus |
|------|-----------|
| `benchmark_report.md` | Markdown tabel (keskmine, p95, tokenid/sekund, valikuline esimene token) |
| `benchmark_report.json` | Toormõõdikute massiiv võrdlemiseks ja ajaloo jaoks |

### Valikud
| Lipp | Kirjeldus | Vaikimisi |
|------|-----------|----------|
| `--models` | Komaga eraldatud mudelite alias'id | (nõutav) |
| `--prompt` | Iga vooru kasutatav prompt | (nõutav) |
| `--rounds` | Voorude arv mudeli kohta | 3 |
| `--output` | Markdown väljundfail | `benchmark_report.md` |
| `--json` | JSON väljundfail | `benchmark_report.json` |
| `--fail-on-empty` | Mitte-null väljumine, kui kõik võrdlusuuringud ebaõnnestuvad | välja lülitatud |

Keskkonnamuutuja `BENCH_STREAM=1` lisab esimese tokeni latentsuse mõõtmise.

### Märkused
- Kasutab `workshop_utils` mudelite järjepidevaks käivitamiseks ja vahemällu salvestamiseks.
- Kui käitatakse teisest töökaustast, üritab skript leida `workshop_utils` teede varuvariante.
- GPU võrdluse jaoks: käitage üks kord, lubage kiirendus CLI konfiguratsiooni kaudu, käitage uuesti ja võrrelge JSON-i.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.