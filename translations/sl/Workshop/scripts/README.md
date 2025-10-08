<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T12:22:09+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "sl"
}
-->
# Skripte za delavnico

Ta imenik vsebuje avtomatizacijske in podporne skripte, ki se uporabljajo za ohranjanje kakovosti in doslednosti gradiva za delavnico.

## Vsebina

| Datoteka | Namen |
|----------|-------|
| `lint_markdown_cli.py` | Preverja markdown kode za zastarele vzorce ukazov Foundry Local CLI znotraj blokov kode. |
| `export_benchmark_markdown.py` | Izvaja večmodelno primerjavo latenc in generira poročila v Markdown + JSON formatu. |

## 1. Preverjanje vzorcev Markdown CLI

`lint_markdown_cli.py` pregleduje vse `.md` datoteke, ki niso prevodi, za nedovoljene vzorce ukazov Foundry Local CLI **znotraj blokov kode** (``` ... ```). Informativno besedilo lahko še vedno omenja zastarele ukaze za zgodovinski kontekst.

### Zastareli vzorci (blokirani znotraj blokov kode)

Preverjevalnik blokira zastarele vzorce CLI. Uporabite sodobne alternative.

### Zahtevane zamenjave
| Zastarelo | Uporabite namesto |
|-----------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skripta za primerjavo + sistemska orodja (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Izhodne kode
| Koda | Pomen |
|------|-------|
| 0 | Ni zaznanih kršitev |
| 1 | Najdeni so bili eden ali več zastarelih vzorcev |

### Lokalno izvajanje
Iz korenskega imenika repozitorija (priporočeno):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit Hook (neobvezno)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
To blokira potrditve, ki uvajajo zastarele vzorce.

### Integracija CI
GitHub Action delovni tok (`.github/workflows/markdown-cli-lint.yml`) izvaja preverjevalnik ob vsakem potisku in zahtevi za združitev v veji `main` in `Reactor`. Neuspešne naloge je treba popraviti pred združitvijo.

### Dodajanje novih zastarelih vzorcev
1. Odprite `lint_markdown_cli.py`.
2. Dodajte par `(regex, suggestion)` v seznam `DEPRECATED`. Uporabite surovo nizovno obliko in vključite meje besed `\b`, kjer je to primerno.
3. Lokalno zaženite preverjevalnik, da preverite zaznavanje.
4. Potrdite in potisnite; CI bo uveljavil novo pravilo.

Primer dodatka:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Dovoljenje pojasnjevalnih omemb
Ker se preverjajo samo bloki kode, lahko varno opisujete zastarele ukaze v narativnem besedilu. Če jih *morate* prikazati znotraj bloka za primerjavo, dodajte blok brez trojnih nazobčanj (npr. z zamikom ali citatom) ali preoblikujte v psevdokodo.

### Preskakovanje določenih datotek (napredno)
Če je potrebno, ovijte primere v ločeno datoteko zunaj repozitorija ali preimenujte z drugačno končnico med osnutkom. Namerni preskoki za prevedene kopije so samodejni (poti, ki vsebujejo `translations`).

### Odpravljanje težav
| Težava | Vzrok | Rešitev |
|--------|-------|---------|
| Preverjevalnik označi vrstico, ki ste jo posodobili | Regex preširok | Zožite vzorec z dodatno mejo besede (`\b`) ali sidri |
| CI ne uspe, lokalno pa uspe | Različna različica Pythona ali neodložene spremembe | Ponovno zaženite lokalno, zagotovite čisto delovno drevo, preverite različico Pythona v delovnem toku (3.11) |
| Potrebno začasno obiti | Nujna hitra rešitev | Takoj po tem uporabite popravek; razmislite o uporabi začasne veje in nadaljnjem PR (izogibajte se dodajanju stikal za obhod) |

### Razlog
Ohranjanje dokumentacije usklajene s *trenutno* stabilno površino CLI preprečuje težave pri delavnici, izogiba se zmedi udeležencev in centralizira merjenje zmogljivosti prek vzdrževanih Python skript namesto razpršenih podukazov CLI.

---
Vzdrževano kot del orodij za zagotavljanje kakovosti delavnice. Za izboljšave (npr. samodejno popravljanje predlogov ali generiranje HTML poročil) odprite težavo ali predložite PR.

## 2. Skripta za validacijo vzorcev

`validate_samples.py` preverja vse Python vzorčne datoteke glede sintakse, uvozov in skladnosti z najboljšimi praksami.

### Uporaba
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

### Kaj preverja
- ✅ Veljavnost Python sintakse
- ✅ Prisotnost zahtevanih uvozov
- ✅ Implementacija obravnave napak (verbose način)
- ✅ Uporaba tipov (verbose način)
- ✅ Dokumentacija funkcij (verbose način)
- ✅ Povezave na SDK reference (verbose način)

### Okoljske spremenljivke
- `SKIP_IMPORT_CHECK=1` - Preskoči preverjanje uvozov
- `SKIP_SYNTAX_CHECK=1` - Preskoči preverjanje sintakse

### Izhodne kode
- `0` - Vsi vzorci so uspešno prestali validacijo
- `1` - Eden ali več vzorcev ni prestalo validacije

## 3. Skripta za testiranje vzorcev

`test_samples.py` izvaja osnovne teste na vseh vzorcih, da preveri, ali se izvajajo brez napak.

### Uporaba
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

### Predpogoji
- Storitev Foundry Local mora biti zagnana: `foundry service start`
- Naloženi modeli: `foundry model run phi-4-mini`
- Nameščene odvisnosti: `pip install -r requirements.txt`

### Kaj testira
- ✅ Vzorec se lahko izvede brez napak med izvajanjem
- ✅ Zahtevani izhod je generiran
- ✅ Ustrezno obravnavanje napak ob neuspehu
- ✅ Zmogljivost (čas izvajanja)

### Okoljske spremenljivke
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model, ki se uporablja za testiranje
- `TEST_TIMEOUT=30` - Časovna omejitev na vzorec v sekundah

### Pričakovane napake
Nekateri testi lahko ne uspejo, če niso nameščene neobvezne odvisnosti (npr. `ragas`, `sentence-transformers`). Namestite jih z:
```bash
pip install sentence-transformers ragas datasets
```

### Izhodne kode
- `0` - Vsi testi so uspešno prestali
- `1` - Eden ali več testov ni prestalo

## 4. Izvoznik primerjalnih podatkov v Markdown

Skripta: `export_benchmark_markdown.py`

Generira tabelo zmogljivosti za niz modelov, ki jo je mogoče reproducirati.

### Uporaba
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Izhodi
| Datoteka | Opis |
|----------|------|
| `benchmark_report.md` | Tabela v Markdown formatu (povprečje, p95, tokeni/sekundo, neobvezno prvi token) |
| `benchmark_report.json` | Surovi niz metrik za primerjavo in zgodovino |

### Možnosti
| Zastavica | Opis | Privzeto |
|-----------|------|---------|
| `--models` | Seznam modelov, ločenih z vejico | (obvezno) |
| `--prompt` | Uporabljen poziv v vsakem krogu | (obvezno) |
| `--rounds` | Število krogov na model | 3 |
| `--output` | Izhodna datoteka v Markdown formatu | `benchmark_report.md` |
| `--json` | Izhodna datoteka v JSON formatu | `benchmark_report.json` |
| `--fail-on-empty` | Ne ničelna izhodna koda, če vsi primerjalni testi ne uspejo | izklopljeno |

Okoljska spremenljivka `BENCH_STREAM=1` doda merjenje latence prvega tokena.

### Opombe
- Uporablja `workshop_utils` za dosledno inicializacijo modelov in predpomnjenje.
- Če se izvaja iz drugega delovnega imenika, skripta poskuša najti poti do `workshop_utils`.
- Za primerjavo GPU: izvedite enkrat, omogočite pospeševanje prek konfiguracije CLI, ponovno izvedite in primerjajte JSON.

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.