<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T21:43:59+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "sw"
}
-->
# Skripti za Warsha

Hii saraka ina skripti za kiotomatiki na msaada zinazotumika kudumisha ubora na uthabiti katika nyenzo za Warsha.

## Yaliyomo

| Faili | Kusudi |
|-------|--------|
| `lint_markdown_cli.py` | Hukagua uzio wa msimbo wa markdown ili kuzuia mifumo ya amri ya Foundry Local CLI iliyopitwa na wakati. |
| `export_benchmark_markdown.py` | Inaendesha kipimo cha ucheleweshaji wa modeli nyingi na kutoa ripoti za Markdown + JSON. |

## 1. Kagua Mifumo ya Markdown CLI

`lint_markdown_cli.py` huchunguza faili zote za `.md` zisizo za tafsiri kwa mifumo ya Foundry Local CLI isiyoruhusiwa **ndani ya uzio wa msimbo** (``` ... ```). Maandishi ya maelezo bado yanaweza kutaja amri zilizopitwa na wakati kwa muktadha wa kihistoria.

### Mifumo Iliyopitwa na Wakati (Iliyofungiwa Ndani ya Uzio wa Msimbo)

Kagua inazuia mifumo ya CLI iliyopitwa na wakati. Tumia mbadala za kisasa badala yake.

### Mbadala Wanaohitajika
| Iliyopitwa na Wakati | Tumia Badala Yake |
|-----------------------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skripti ya kipimo + zana za mfumo (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Nambari za Kutoka
| Nambari | Maana |
|--------|-------|
| 0 | Hakuna ukiukaji uliogunduliwa |
| 1 | Mifumo moja au zaidi iliyopitwa na wakati imepatikana |

### Kuendesha Kwa Nje
Kutoka mzizi wa hifadhi (inapendekezwa):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Kifaa cha Kabla ya Kujitolea (Hiari)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Hii inazuia kujitolea kunakoanzisha mifumo iliyopitwa na wakati.

### Ujumuishaji wa CI
Mfumo wa GitHub Action (`.github/workflows/markdown-cli-lint.yml`) huendesha kagua kwenye kila msukumo na ombi la kuvuta kwa matawi ya `main` na `Reactor`. Kazi zinazoshindwa lazima zirekebishwe kabla ya kuunganishwa.

### Kuongeza Mifumo Mpya Iliyopitwa na Wakati
1. Fungua `lint_markdown_cli.py`.
2. Ongeza jozi `(regex, suggestion)` kwenye orodha ya `DEPRECATED`. Tumia kamba mbichi na jumuisha mipaka ya neno `\b` inapofaa.
3. Endesha kagua kwa nje ili kuthibitisha kugundua.
4. Jitolee na sukuma; CI itatekeleza sheria mpya.

Mfano wa nyongeza:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Kuruhusu Maelezo ya Kifafanua
Kwa sababu uzio wa msimbo pekee unatekelezwa, unaweza kuelezea amri zilizopitwa na wakati katika maandishi ya maelezo kwa usalama. Ikiwa *lazima* uonyeshe ndani ya uzio kwa kulinganisha, ongeza uzio wa msimbo **bila** alama tatu za nyuma (mfano, weka kiingilio au nukuu) au andika upya kwa fomu ya pseudo.

### Kuruka Faili Maalum (Juu)
Ikiwa inahitajika, weka mifano ya urithi katika faili tofauti nje ya hifadhi au ubadilishe jina kwa kiendelezi tofauti wakati wa kuandika. Kuruka kwa makusudi kwa nakala za tafsiri ni kiotomatiki (njia zinazojumuisha `translations`).

### Utatuzi wa Matatizo
| Tatizo | Sababu | Suluhisho |
|--------|--------|-----------|
| Kagua inaonyesha mstari uliosasishwa | Regex pana sana | Punguza muundo na mipaka ya ziada ya neno (`\b`) au nanga |
| CI inashindwa lakini nje inafaulu | Toleo tofauti la Python au mabadiliko yasiyojitolea | Endesha tena kwa nje, hakikisha mti wa kazi safi, angalia toleo la Python la mfumo wa kazi (3.11) |
| Haja ya kupita kwa muda | Marekebisho ya dharura | Tumia marekebisho mara moja baada ya; fikiria kutumia tawi la muda na PR ya kufuatilia (epuka kuongeza swichi za kupita) |

### Sababu
Kudumisha nyaraka zinazolingana na uso wa CLI *wa sasa* thabiti huzuia msuguano wa warsha, kuepuka mkanganyiko wa wanafunzi, na kuimarisha kipimo cha utendaji kupitia skripti za Python zinazodumishwa badala ya amri za CLI zinazotofautiana.

---
Inadumishwa kama sehemu ya zana za ubora wa warsha. Kwa maboresho (mfano, mapendekezo ya kurekebisha kiotomatiki au kizazi cha ripoti ya HTML), fungua suala au wasilisha PR.

## 2. Skripti ya Uthibitishaji wa Sampuli

`validate_samples.py` inathibitisha faili zote za sampuli za Python kwa uhalali wa sintaksia, uagizaji, na uzingatiaji wa mazoea bora.

### Matumizi
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

### Kile Inachokagua
- ✅ Uhalali wa sintaksia ya Python
- ✅ Uagizaji unaohitajika upo
- ✅ Utekelezaji wa kushughulikia makosa (hali ya maelezo)
- ✅ Matumizi ya vidokezo vya aina (hali ya maelezo)
- ✅ Maelezo ya kazi (hali ya maelezo)
- ✅ Viungo vya marejeleo ya SDK (hali ya maelezo)

### Vigezo vya Mazingira
- `SKIP_IMPORT_CHECK=1` - Ruka uthibitishaji wa uagizaji
- `SKIP_SYNTAX_CHECK=1` - Ruka uthibitishaji wa sintaksia

### Nambari za Kutoka
- `0` - Sampuli zote zimepita uthibitishaji
- `1` - Sampuli moja au zaidi zimeshindwa

## 3. Kifaa cha Mtihani wa Sampuli

`test_samples.py` huendesha majaribio ya moshi kwenye sampuli zote ili kuthibitisha zinafanya kazi bila makosa.

### Matumizi
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

### Mahitaji ya Awali
- Huduma ya Foundry Local inayoendesha: `foundry service start`
- Modelle zimepakiwa: `foundry model run phi-4-mini`
- Vitegemezi vimesakinishwa: `pip install -r requirements.txt`

### Kile Inachokagua
- ✅ Sampuli inaweza kutekelezwa bila makosa ya wakati wa kukimbia
- ✅ Pato linalohitajika linazalishwa
- ✅ Kushughulikia makosa ipasavyo wakati wa kushindwa
- ✅ Utendaji (muda wa utekelezaji)

### Vigezo vya Mazingira
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modeli ya kutumia kwa majaribio
- `TEST_TIMEOUT=30` - Muda wa kusubiri kwa sampuli kwa sekunde

### Kushindwa Kunakotarajiwa
Baadhi ya majaribio yanaweza kushindwa ikiwa vitegemezi vya hiari havijasakinishwa (mfano, `ragas`, `sentence-transformers`). Sakinisha kwa:
```bash
pip install sentence-transformers ragas datasets
```

### Nambari za Kutoka
- `0` - Majaribio yote yamepita
- `1` - Jaribio moja au zaidi limeshindwa

## 4. Kifaa cha Kusafirisha Kipimo cha Markdown

Skripti: `export_benchmark_markdown.py`

Huzalisha jedwali la utendaji linaloweza kurudiwa kwa seti ya modeli.

### Matumizi
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Matokeo
| Faili | Maelezo |
|-------|---------|
| `benchmark_report.md` | Jedwali la Markdown (wastani, p95, tokeni/sec, tokeni ya kwanza ya hiari) |
| `benchmark_report.json` | Mfululizo wa vipimo ghafi kwa kulinganisha & historia |

### Chaguo
| Bendera | Maelezo | Chaguo-msingi |
|---------|---------|--------------|
| `--models` | Majina ya modeli yaliyotenganishwa kwa koma | (inayohitajika) |
| `--prompt` | Swali linalotumika kila raundi | (inayohitajika) |
| `--rounds` | Raundi kwa kila modeli | 3 |
| `--output` | Faili ya pato la Markdown | `benchmark_report.md` |
| `--json` | Faili ya pato la JSON | `benchmark_report.json` |
| `--fail-on-empty` | Kutoka isiyo ya sifuri ikiwa vipimo vyote vinashindwa | imezimwa |

Kigezo cha mazingira `BENCH_STREAM=1` kinaongeza kipimo cha ucheleweshaji wa tokeni ya kwanza.

### Vidokezo
- Inatumia tena `workshop_utils` kwa modeli thabiti za kuanzisha & kuhifadhi.
- Ikiwa imeendeshwa kutoka saraka tofauti ya kazi, skripti inajaribu njia za kurudi nyuma ili kupata `workshop_utils`.
- Kwa kulinganisha GPU: endesha mara moja, wezesha kasi kupitia usanidi wa CLI, endesha tena na linganisha JSON.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.