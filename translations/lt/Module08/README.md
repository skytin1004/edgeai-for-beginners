<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:53:12+00:00",
  "source_file": "Module08/README.md",
  "language_code": "lt"
}
-->
# Modulis 08: Praktinis darbas su Microsoft Foundry Local – pilnas kūrėjo įrankių rinkinys

## Apžvalga

Microsoft Foundry Local yra naujos kartos Edge AI kūrimo platforma, suteikianti kūrėjams galingus įrankius kurti, diegti ir plėsti AI programas vietoje, išlaikant sklandžią integraciją su Azure AI Foundry. Šiame modulyje pateikiama išsami Foundry Local apžvalga – nuo diegimo iki pažangių agentų kūrimo.

**Pagrindinės technologijos:**
- Microsoft Foundry Local CLI ir SDK
- Azure AI Foundry integracija
- Modelių įžvalgos įrenginyje
- Vietinis modelių talpinimas ir optimizavimas
- Agentų architektūros

## Mokymosi tikslai

Baigę šį modulį, jūs:

- **Įvaldysite Foundry Local diegimą**: Įdiegsite, sukonfigūruosite ir optimizuosite Foundry Local Windows 11 kūrimui
- **Diegsite įvairius modelius**: Vietoje paleisite phi, qwen, deepseek ir GPT-OSS-20B modelius naudodami CLI komandas
- **Kursite gamybinius sprendimus**: Sukursite AI programas su pažangiu promptų kūrimu ir duomenų integracija
- **Pasinaudosite atvirojo kodo ekosistema**: Integruosite Hugging Face modelius ir bendruomenės papildymus
- **Lyginsite AI architektūras**: Suprasite LLM ir SLM privalumus bei diegimo strategijas
- **Kursite AI agentus**: Sukursite intelektualius agentus naudodami Foundry Local architektūrą ir pagrindimo galimybes
- **Įgyvendinsite modelius kaip įrankius**: Kursite moduliarius, pritaikomus AI sprendimus verslo programoms

## Sesijų struktūra

### [1: Pradžia su Foundry Local](./01.FoundryLocalSetup.md)
**Dėmesys**: Diegimas, CLI nustatymas, modelių talpinimas ir aparatūros spartinimas

**Ko išmoksite:**
- Pilnas Foundry Local diegimas Windows 11
- CLI konfigūracija ir komandų struktūra
- Modelių talpinimo strategijos optimaliam našumui
- Aparatūros spartinimo nustatymas ir optimizavimas
- Praktinis phi, qwen, deepseek ir GPT-OSS-20B modelių diegimas

**Trukmė**: 2–3 valandos  
**Reikalavimai**: Windows 11, pagrindinės komandinės eilutės žinios

---

### [2: AI sprendimų kūrimas su Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Dėmesys**: Pažangus promptų kūrimas, duomenų integracija ir veiksmingi uždaviniai

**Ko išmoksite:**
- Pažangios promptų kūrimo technikos
- Duomenų integracijos modeliai ir geriausios praktikos
- Veiksmingų AI uždavinių kūrimas su Foundry Local
- Sklandūs Azure AI Foundry integracijos darbo procesai
- Našumo optimizavimas ir stebėjimas

**Trukmė**: 2–3 valandos  
**Reikalavimai**: 1 sesijos baigimas, Azure paskyra (neprivaloma)

---

### [3: Atvirojo kodo modeliai Foundry Local](./03.OpenSourceModels.md)
**Dėmesys**: Hugging Face integracija, modelių pasirinkimo strategijos ir bendruomenės papildymai

**Ko išmoksite:**
- Hugging Face modelių integracija su Foundry Local
- „Bring-your-own-model“ (BYOM) strategijos ir įgyvendinimas
- „Model Mondays“ serijos įžvalgos ir bendruomenės indėlis
- Individualių modelių diegimas ir optimizavimas
- Bendruomenės modelių vertinimo ir pasirinkimo kriterijai

**Trukmė**: 2–3 valandos  
**Reikalavimai**: 1–2 sesijų baigimas, Hugging Face paskyra

---

### [4: Pažangūs modeliai – LLM, SLM ir įžvalgos įrenginyje](./04.CuttingEdgeModels.md)
**Dėmesys**: Modelių palyginimas, EdgeAI su Phi ir ONNX Runtime, pažangūs demonstraciniai projektai

**Ko išmoksite:**
- Išsamus LLM ir SLM palyginimas bei naudojimo atvejai
- Vietinių ir debesų įžvalgų privalumų ir trūkumų analizė
- EdgeAI įgyvendinimas su Phi ir ONNX Runtime
- Chainlit RAG pokalbių programos kūrimas ir diegimas
- WebGPU įžvalgų optimizavimo technikos
- AI PC SDK integracija ir galimybės

**Trukmė**: 3–4 valandos  
**Reikalavimai**: 1–3 sesijų baigimas, įžvalgų koncepcijų supratimas

---

### [5: Greitas AI agentų kūrimas su Foundry Local](./05.AIPoweredAgents.md)
**Dėmesys**: Greitas GenAI programų kūrimas, sisteminiai promptai, pagrindimas ir agentų architektūros

**Ko išmoksite:**
- Foundry Local agentų architektūra ir dizaino modeliai
- Sisteminių promptų kūrimas agentų elgsenai
- Pagrindimo technikos patikimiems agentų atsakymams
- Greiti GenAI programų kūrimo darbo procesai
- Agentų koordinavimas ir daugiagentės sistemos
- Gamybinio diegimo strategijos AI agentams

**Trukmė**: 3–4 valandos  
**Reikalavimai**: 1–4 sesijų baigimas, pagrindinės AI agentų žinios

---

### [6: Foundry Local – modeliai kaip įrankiai](./06.ModelsAsTools.md)
**Dėmesys**: Moduliarios AI sprendimai, vietinis diegimas ir verslo plėtra

**Ko išmoksite:**
- AI modelių traktavimas kaip moduliarių, pritaikomų įrankių
- Vietinis diegimas be debesų priklausomybės
- Mažos delsos, ekonomiškos ir privatumo išsaugojimo įžvalgos
- SDK, API ir CLI integracijos modeliai
- Modelių pritaikymas specifiniams naudojimo atvejams
- Plėtros strategijos nuo vietinio iki Azure AI Foundry
- Verslui paruoštos AI programų architektūros

**Trukmė**: 3–4 valandos  
**Reikalavimai**: Visos ankstesnės sesijos, naudinga verslo plėtros patirtis

## Reikalavimai

### Sistemos reikalavimai
- **Operacinė sistema**: Windows 11 (22H2 ar naujesnė)
- **Atmintis**: 16GB RAM (32GB rekomenduojama didesniems modeliams)
- **Saugykla**: 50GB laisvos vietos modelių talpinimui
- **Aparatūra**: Rekomenduojamas NPU palaikomas įrenginys (Copilot+ PC), GPU neprivalomas
- **Tinklas**: Greitas internetas pradiniam modelių atsisiuntimui

### Kūrimo aplinka
- Visual Studio Code su AI Toolkit plėtiniu
- Python 3.10+ ir pip
- Git versijų valdymui
- PowerShell arba Command Prompt
- Azure CLI (neprivaloma debesų integracijai)

### Žinių reikalavimai
- Pagrindinis AI/ML koncepcijų supratimas
- Komandinės eilutės naudojimo patirtis
- Python programavimo pagrindai
- REST API koncepcijos
- Pagrindinės promptų ir modelių įžvalgų žinios

## Modulio laiko planas

**Bendra numatoma trukmė**: 15–20 valandų

| Sesija | Dėmesio sritis | Laikas | Sudėtingumas |
|-------|----------------|-------|--------------|
|  1 | Diegimas ir pagrindai | 2–3 valandos | Pradedantysis |
|  2 | AI sprendimai | 2–3 valandos | Vidutinis |
|  3 | Atvirojo kodo modeliai | 2–3 valandos | Vidutinis |
|  4 | Pažangūs modeliai | 3–4 valandos | Pažengęs |
|  5 | AI agentai | 3–4 valandos | Pažengęs |
|  6 | Verslo įrankiai | 3–4 valandos | Ekspertas |

## Pagrindiniai ištekliai

### Pagrindinė dokumentacija
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays serija](https://aka.ms/model-mondays)

### Bendruomenės ištekliai
- [Foundry Local bendruomenės diskusijos](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry pavyzdžiai](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI kūrėjų bendruomenė](https://techcommunity.microsoft.com/category/artificialintelligence)

## Mokymosi rezultatai

Baigę šį modulį, jūs būsite pasiruošę:

### Techninis meistriškumas
- **Diegti ir valdyti**: Foundry Local diegimus kūrimo ir gamybos aplinkose
- **Integruoti modelius**: Sklandžiai dirbti su įvairiomis modelių šeimomis iš Microsoft, Hugging Face ir bendruomenės šaltinių
- **Kurti programas**: Sukurti gamybai paruoštas AI programas su pažangiomis funkcijomis ir optimizacijomis
- **Plėtoti agentus**: Įgyvendinti sudėtingus AI agentus su pagrindimu, logika ir įrankių integracija

### Strateginis supratimas
- **Architektūros sprendimai**: Priimti informuotus sprendimus tarp vietinio ir debesų diegimo
- **Našumo optimizavimas**: Optimizuoti įžvalgų našumą skirtingose aparatūros konfigūracijose
- **Verslo plėtra**: Kurti programas, kurios plečiasi nuo vietinių prototipų iki verslo diegimų
- **Privatumas ir saugumas**: Įgyvendinti privatumo išsaugojimo AI sprendimus su vietinėmis įžvalgomis

### Inovacijų galimybės
- **Greitas prototipų kūrimas**: Greitai kurti ir testuoti AI programų koncepcijas
- **Bendruomenės integracija**: Pasinaudoti atvirojo kodo modeliais ir prisidėti prie ekosistemos
- **Pažangūs modeliai**: Įgyvendinti pažangius AI modelius, įskaitant RAG, agentus ir įrankių integraciją
- **Ateities kūrimas**: Kurti programas, pasiruošusias naujoms AI technologijoms ir modeliams

## Pradžia

1. **Paruoškite aplinką**: Įsitikinkite, kad turite Windows 11 su rekomenduojamais aparatūros parametrais
2. **Įdiekite reikalavimus**: Nustatykite kūrimo įrankius ir priklausomybes
3. **Pradėkite nuo 1 sesijos**: Pradėkite nuo Foundry Local diegimo ir pagrindinio nustatymo
4. **Eikite nuosekliai**: Baikite sesijas iš eilės, kad mokymasis būtų optimalus
5. **Praktikuokite nuolat**: Taikykite koncepcijas per praktinius pratimus ir projektus

## Sėkmės rodikliai

Sekite savo pažangą per modulį:

- [ ] Sėkmingai įdiegti ir sukonfigūruoti Foundry Local
- [ ] Diegti ir paleisti bent 4 skirtingas modelių šeimas
- [ ] Sukurti pilną AI sprendimą su duomenų integracija
- [ ] Integruoti bent 2 atvirojo kodo modelius
- [ ] Sukurti funkcionalią RAG pokalbių programą
- [ ] Sukurti ir diegti AI agentą
- [ ] Įgyvendinti modelių kaip įrankių architektūrą

## Greitas pradėjimas pavyzdžiams

### 1) Aplinkos nustatymas (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Pradėkite vietinį modelį (naujas terminalas)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Paleiskite Chainlit demonstraciją (4 sesija)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Paleiskite daugiagentės koordinatorių (5 sesija)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Jei matote ryšio klaidas, patikrinkite Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Maršrutizatoriaus konfigūracija (6 sesija)
Maršrutizatorius atlieka greitą sveikatos patikrą ir palaiko aplinkos pagrindu konfigūraciją:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Šis modulis atspindi pažangiausią Edge AI kūrimą, derinant Microsoft verslo klasės įrankius su atvirojo kodo ekosistemos lankstumu ir inovacijomis. Įvaldę Foundry Local, būsite AI programų kūrimo priešakyje.

Dėl Azure OpenAI (2 sesija) žr. pavyzdžio README, kur pateikiami reikalingi aplinkos kintamieji ir API versijos nustatymai.

## Pavyzdžių apžvalga

- `samples/01`: Greitas REST pokalbis su Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK integracija (`sdk_quickstart.py`).
- `samples/03`: Modelių atradimas + greitas testavimas (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demonstracija (`app.py`).
- `samples/05`: Daugiagentės koordinacija (`python -m samples.05.agents.coordinator`).
- `samples/06`: Modelių kaip įrankių maršrutizatorius (`python samples\06\router.py`).

---

