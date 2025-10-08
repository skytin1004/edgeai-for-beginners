<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T14:25:50+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "hr"
}
-->
# Skripte za radionicu

Ovaj direktorij sadrži skripte za automatizaciju i podršku koje se koriste za održavanje kvalitete i dosljednosti materijala radionice.

## Sadržaj

| Datoteka | Namjena |
|----------|---------|
| `lint_markdown_cli.py` | Provjerava kodne blokove u Markdownu kako bi blokirao zastarjele obrasce naredbi Foundry Local CLI. |
| `export_benchmark_markdown.py` | Pokreće višemodelni test latencije i generira izvješća u Markdownu i JSON formatu. |

## 1. Provjera obrazaca Markdown CLI

`lint_markdown_cli.py` skenira sve `.md` datoteke koje nisu prijevodi u potrazi za zabranjenim obrascima Foundry Local CLI **unutar ograničenih kodnih blokova** (``` ... ```). Informativni tekst i dalje može spominjati zastarjele naredbe radi povijesnog konteksta.

### Zastarjeli obrasci (blokirani unutar kodnih blokova)

Provjera blokira zastarjele CLI obrasce. Koristite moderne alternative.

### Potrebne zamjene
| Zastarjelo | Koristite umjesto toga |
|------------|------------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skripta za testiranje + sistemski alati (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Izlazni kodovi
| Kod | Značenje |
|-----|----------|
| 0 | Nisu pronađene povrede |
| 1 | Pronađen je jedan ili više zastarjelih obrazaca |

### Lokalno pokretanje
Iz korijena repozitorija (preporučeno):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-commit Hook (Opcionalno)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Ovo blokira commitove koji uvode zastarjele obrasce.

### CI integracija
GitHub Action workflow (`.github/workflows/markdown-cli-lint.yml`) pokreće provjeru pri svakom pushu i pull requestu na grane `main` i `Reactor`. Neuspjeli zadaci moraju se popraviti prije spajanja.

### Dodavanje novih zastarjelih obrazaca
1. Otvorite `lint_markdown_cli.py`.
2. Dodajte tuple `(regex, suggestion)` na popis `DEPRECATED`. Koristite raw string i uključite granice riječi `\b` gdje je prikladno.
3. Pokrenite provjeru lokalno kako biste provjerili detekciju.
4. Commitajte i pushajte; CI će provesti novo pravilo.

Primjer dodavanja:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Dopuštanje objašnjavajućih spominjanja
Budući da se provjera primjenjuje samo na ograničene kodne blokove, zastarjele naredbe možete opisati u narativnom tekstu bez problema. Ako ih *morate* prikazati unutar bloka radi kontrasta, dodajte blok **bez** trostrukih backtickova (npr. uvucite ili citirajte) ili preoblikujte u pseudo-oblik.

### Preskakanje specifičnih datoteka (Napredno)
Ako je potrebno, stavite primjere u zasebnu datoteku izvan repozitorija ili preimenujte s drugačijom ekstenzijom dok radite na nacrtu. Namjerno preskakanje za prevedene kopije je automatsko (putanje koje sadrže `translations`).

### Rješavanje problema
| Problem | Uzrok | Rješenje |
|---------|-------|----------|
| Provjera označava liniju koju ste ažurirali | Regex preširok | Sužite obrazac dodatnom granicom riječi (`\b`) ili sidrima |
| CI ne uspijeva, ali lokalno prolazi | Različita verzija Pythona ili necommitane promjene | Ponovno pokrenite lokalno, osigurajte čist radni direktorij, provjerite verziju Pythona u workflowu (3.11) |
| Potrebno privremeno zaobići | Hitni popravak | Primijenite popravak odmah nakon; razmislite o korištenju privremene grane i naknadnog PR-a (izbjegavajte dodavanje prekidača za zaobilaženje) |

### Razlog
Održavanje dokumentacije usklađene s *trenutnim* stabilnim CLI sučeljem sprječava probleme na radionici, izbjegava zbunjenost sudionika i centralizira mjerenje performansi kroz održavane Python skripte umjesto zastarjelih CLI podnaredbi.

---
Održava se kao dio alata za kvalitetu radionice. Za poboljšanja (npr. automatsko popravljanje prijedloga ili generiranje HTML izvješća), otvorite problem ili pošaljite PR.

## 2. Skripta za validaciju uzoraka

`validate_samples.py` provjerava sve Python uzorke za sintaksu, uvoze i usklađenost s najboljim praksama.

### Upotreba
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

### Što provjerava
- ✅ Valjanost Python sintakse
- ✅ Prisutnost potrebnih uvoza
- ✅ Implementacija obrade pogrešaka (detaljni način)
- ✅ Korištenje tipova (detaljni način)
- ✅ Dokumentacijski stringovi funkcija (detaljni način)
- ✅ SDK referentne poveznice (detaljni način)

### Varijable okruženja
- `SKIP_IMPORT_CHECK=1` - Preskoči provjeru uvoza
- `SKIP_SYNTAX_CHECK=1` - Preskoči provjeru sintakse

### Izlazni kodovi
- `0` - Svi uzorci prošli validaciju
- `1` - Jedan ili više uzoraka nisu prošli

## 3. Skripta za testiranje uzoraka

`test_samples.py` pokreće osnovne testove na svim uzorcima kako bi provjerila da se izvršavaju bez pogrešaka.

### Upotreba
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

### Preduvjeti
- Pokrenuta Foundry Local usluga: `foundry service start`
- Učitani modeli: `foundry model run phi-4-mini`
- Instalirane ovisnosti: `pip install -r requirements.txt`

### Što testira
- ✅ Uzorak se može izvršiti bez pogrešaka u izvođenju
- ✅ Generira se potrebni izlaz
- ✅ Ispravna obrada pogrešaka u slučaju neuspjeha
- ✅ Performanse (vrijeme izvođenja)

### Varijable okruženja
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model koji se koristi za testiranje
- `TEST_TIMEOUT=30` - Timeout po uzorku u sekundama

### Očekivani neuspjesi
Neki testovi mogu ne uspjeti ako opcionalne ovisnosti nisu instalirane (npr. `ragas`, `sentence-transformers`). Instalirajte s:
```bash
pip install sentence-transformers ragas datasets
```

### Izlazni kodovi
- `0` - Svi testovi prošli
- `1` - Jedan ili više testova nisu prošli

## 4. Izvoznik za benchmark u Markdownu

Skripta: `export_benchmark_markdown.py`

Generira reproducibilnu tablicu performansi za skup modela.

### Upotreba
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Izlazi
| Datoteka | Opis |
|----------|------|
| `benchmark_report.md` | Tablica u Markdownu (prosjek, p95, tokeni/sek, opcionalno prvi token) |
| `benchmark_report.json` | Niz sirovih metrika za usporedbu i povijest |

### Opcije
| Zastavica | Opis | Zadano |
|-----------|------|--------|
| `--models` | Alias modela odvojen zarezima | (obavezno) |
| `--prompt` | Prompt korišten u svakom krugu | (obavezno) |
| `--rounds` | Broj krugova po modelu | 3 |
| `--output` | Datoteka za izlaz u Markdownu | `benchmark_report.md` |
| `--json` | Datoteka za izlaz u JSON formatu | `benchmark_report.json` |
| `--fail-on-empty` | Izlazni kod različit od nule ako svi benchmark testovi ne uspiju | isključeno |

Varijabla okruženja `BENCH_STREAM=1` dodaje mjerenje latencije prvog tokena.

### Napomene
- Ponovno koristi `workshop_utils` za dosljedno pokretanje modela i predmemoriranje.
- Ako se pokreće iz drugog radnog direktorija, skripta pokušava pronaći `workshop_utils` putem rezervnih putanja.
- Za usporedbu GPU performansi: pokrenite jednom, omogućite ubrzanje putem CLI konfiguracije, ponovno pokrenite i usporedite JSON.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.