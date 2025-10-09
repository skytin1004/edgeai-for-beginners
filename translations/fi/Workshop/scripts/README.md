<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T14:47:00+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "fi"
}
-->
# Työpajan Skriptit

Tämä hakemisto sisältää automaatio- ja tukiskriptejä, joita käytetään työpajamateriaalien laadun ja yhdenmukaisuuden ylläpitämiseen.

## Sisältö

| Tiedosto | Tarkoitus |
|----------|-----------|
| `lint_markdown_cli.py` | Tarkistaa markdown-koodilohkot estääkseen vanhentuneiden Foundry Local CLI -komentomallien käytön. |
| `export_benchmark_markdown.py` | Suorittaa monimallisen viivevertailun ja tuottaa Markdown- ja JSON-raportit. |

## 1. Markdown CLI -mallien tarkistin

`lint_markdown_cli.py` skannaa kaikki ei-käännetyt `.md`-tiedostot kiellettyjen Foundry Local CLI -mallien varalta **aidatuissa koodilohkoissa** (``` ... ```). Informatiivisessa tekstissä voi edelleen mainita vanhentuneita komentoja historiallisessa kontekstissa.

### Vanhentuneet mallit (estetty koodilohkoissa)

Tarkistin estää vanhentuneet CLI-mallit. Käytä sen sijaan nykyaikaisia vaihtoehtoja.

### Vaaditut korvaukset
| Vanhentunut | Käytä sen sijaan |
|-------------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Vertailuskripti + järjestelmätyökalut (`Tehtävienhallinta`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Poistumiskoodit
| Koodi | Merkitys |
|-------|----------|
| 0 | Ei rikkomuksia havaittu |
| 1 | Yksi tai useampi vanhentunut malli löytyi |

### Suorittaminen paikallisesti
Projektin juurihakemistosta (suositeltu):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (valinnainen)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Tämä estää sitoumukset, jotka sisältävät vanhentuneita malleja.

### CI-integraatio
GitHub Action -työnkulku (`.github/workflows/markdown-cli-lint.yml`) suorittaa tarkistimen jokaisessa `main`- ja `Reactor`-haaraan tehdyssä push- ja pull request -toiminnossa. Epäonnistuneet työt on korjattava ennen yhdistämistä.

### Uusien vanhentuneiden mallien lisääminen
1. Avaa `lint_markdown_cli.py`.
2. Lisää tuple `(regex, suggestion)` `DEPRECATED`-listaan. Käytä raakaa merkkijonoa ja sisällytä `\b` sananrajat tarvittaessa.
3. Suorita tarkistin paikallisesti varmistaaksesi tunnistuksen.
4. Tee sitoumus ja push; CI valvoo uutta sääntöä.

Esimerkki lisäyksestä:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Selittävien mainintojen salliminen
Koska vain aidatut koodilohkot tarkistetaan, voit kuvata vanhentuneita komentoja kerronnallisessa tekstissä turvallisesti. Jos *täytyy* näyttää niitä aidatussa lohkossa kontrastin vuoksi, lisää aidattu lohko **ilman** kolmoismerkkejä (esim. sisennä tai lainaa) tai kirjoita uudelleen pseudomuotoon.

### Tiettyjen tiedostojen ohittaminen (edistynyt)
Jos tarpeen, sijoita vanhat esimerkit erilliseen tiedostoon repo-ulkopuolelle tai nimeä uudelleen eri tiedostopäätteellä luonnostelun aikana. Tahalliset ohitukset käännetyille kopioille ovat automaattisia (polut, jotka sisältävät `translations`).

### Vianmääritys
| Ongelma | Syy | Ratkaisu |
|---------|-----|---------|
| Tarkistin merkitsee muokkaamasi rivin | Regex liian laaja | Rajaa mallia lisäämällä sananraja (`\b`) tai ankkureita |
| CI epäonnistuu, mutta paikallisesti toimii | Eri Python-versio tai sitouttamattomat muutokset | Suorita uudelleen paikallisesti, varmista puhdas työtila, tarkista työnkulun Python-versio (3.11) |
| Tarve ohittaa väliaikaisesti | Kiireellinen korjaus | Tee korjaus heti sen jälkeen; harkitse väliaikaisen haaran ja jatkositoumuksen käyttöä (vältä ohituskytkimien lisäämistä) |

### Perustelut
Dokumentaation pitäminen ajan tasalla *nykyisen* vakaan CLI-pinnan kanssa vähentää työpajan kitkaa, välttää oppijoiden hämmennystä ja keskittää suorituskyvyn mittauksen ylläpidettyihin Python-skripteihin sen sijaan, että käytettäisiin vanhentuneita CLI-alikomentoja.

---
Ylläpidetään osana työpajan laatutyökaluketjua. Parannuksia varten (esim. automaattiset korjausehdotukset tai HTML-raporttien luonti) avaa issue tai lähetä PR.

## 2. Esimerkkien validointiskripti

`validate_samples.py` tarkistaa kaikki Python-esimerkkitiedostot syntaksin, tuontien ja parhaiden käytäntöjen noudattamisen osalta.

### Käyttö
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

### Mitä se tarkistaa
- ✅ Python-syntaksin oikeellisuus
- ✅ Vaaditut tuonnit ovat läsnä
- ✅ Virheenkäsittelyn toteutus (yksityiskohtainen tila)
- ✅ Tyyppivihjeiden käyttö (yksityiskohtainen tila)
- ✅ Funktioiden docstringit (yksityiskohtainen tila)
- ✅ SDK-viitelinkit (yksityiskohtainen tila)

### Ympäristömuuttujat
- `SKIP_IMPORT_CHECK=1` - Ohita tuontien validointi
- `SKIP_SYNTAX_CHECK=1` - Ohita syntaksin validointi

### Poistumiskoodit
- `0` - Kaikki esimerkit läpäisivät validoinnin
- `1` - Yksi tai useampi esimerkki epäonnistui

## 3. Esimerkkien testausohjelma

`test_samples.py` suorittaa savutestit kaikille esimerkeille varmistaakseen, että ne toimivat ilman virheitä.

### Käyttö
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

### Esivaatimukset
- Foundry Local -palvelu käynnissä: `foundry service start`
- Mallit ladattu: `foundry model run phi-4-mini`
- Riippuvuudet asennettu: `pip install -r requirements.txt`

### Mitä se testaa
- ✅ Esimerkki voidaan suorittaa ilman ajonaikaisia virheitä
- ✅ Vaadittu tulos generoituu
- ✅ Oikea virheenkäsittely epäonnistumisen yhteydessä
- ✅ Suorituskyky (suoritusaika)

### Ympäristömuuttujat
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Malli, jota käytetään testauksessa
- `TEST_TIMEOUT=30` - Aikaraja per esimerkki sekunneissa

### Odotetut epäonnistumiset
Jotkin testit voivat epäonnistua, jos valinnaisia riippuvuuksia ei ole asennettu (esim. `ragas`, `sentence-transformers`). Asenna ne komennolla:
```bash
pip install sentence-transformers ragas datasets
```

### Poistumiskoodit
- `0` - Kaikki testit läpäisivät
- `1` - Yksi tai useampi testi epäonnistui

## 4. Benchmark Markdown -viejä

Skripti: `export_benchmark_markdown.py`

Luo toistettavan suorituskykytaulukon mallijoukolle.

### Käyttö
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Tulosteet
| Tiedosto | Kuvaus |
|----------|--------|
| `benchmark_report.md` | Markdown-taulukko (keskiarvo, p95, tokenit/sek, valinnainen ensimmäinen token) |
| `benchmark_report.json` | Raakametriikkataulukko vertailua ja historiaa varten |

### Valinnat
| Lippu | Kuvaus | Oletus |
|-------|--------|--------|
| `--models` | Pilkulla erotetut mallialiaset | (pakollinen) |
| `--prompt` | Käytetty kehotus jokaisella kierroksella | (pakollinen) |
| `--rounds` | Kierrokset per malli | 3 |
| `--output` | Markdown-tulostetiedosto | `benchmark_report.md` |
| `--json` | JSON-tulostetiedosto | `benchmark_report.json` |
| `--fail-on-empty` | Ei-nolla poistumiskoodi, jos kaikki vertailut epäonnistuvat | pois päältä |

Ympäristömuuttuja `BENCH_STREAM=1` lisää ensimmäisen tokenin viiveen mittauksen.

### Huomioita
- Käyttää uudelleen `workshop_utils`-kirjastoa mallien yhdenmukaiseen käynnistykseen ja välimuistiin.
- Jos suoritetaan eri työhakemistosta, skripti yrittää polkujen varajärjestelyjä löytääkseen `workshop_utils`.
- GPU-vertailua varten: suorita kerran, ota kiihdytys käyttöön CLI-asetuksista, suorita uudelleen ja vertaa JSON-tiedostoja.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.