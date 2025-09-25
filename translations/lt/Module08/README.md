<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50d80c321803b5170d9a9cd9bbfb37a3",
  "translation_date": "2025-09-25T02:40:11+00:00",
  "source_file": "Module08/README.md",
  "language_code": "lt"
}
-->
# Modulis 08: Praktinis darbas su Microsoft Foundry Local – Pilnas kūrėjo įrankių rinkinys

## Apžvalga

Microsoft Foundry Local yra naujos kartos Edge AI kūrimo platforma, suteikianti kūrėjams galingus įrankius kurti, diegti ir plėsti AI programas vietoje, išlaikant sklandžią integraciją su Azure AI Foundry. Šiame modulyje pateikiama išsami Foundry Local apžvalga – nuo diegimo iki pažangių agentų kūrimo.

**Pagrindinės technologijos:**
- Microsoft Foundry Local CLI ir SDK
- Azure AI Foundry integracija
- Modelių įžvalgos įrenginyje
- Vietinis modelių talpinimas ir optimizavimas
- Agentų pagrindu sukurtos architektūros

## Mokymosi tikslai

Baigę šį modulį, jūs:

- **Įvaldysite Foundry Local**: Įdiegsite, sukonfigūruosite ir optimizuosite Windows 11 kūrimui
- **Diegsite įvairius modelius**: Vietoje vykdysite phi, qwen, deepseek ir GPT modelius naudodami CLI komandas
- **Kursite gamybinius sprendimus**: Sukursite AI programas su pažangiu promptų kūrimu ir duomenų integracija
- **Pasinaudosite atvirojo kodo ekosistema**: Integruosite Hugging Face modelius ir bendruomenės indėlius
- **Kursite AI agentus**: Sukursite intelektualius agentus su pagrindimo ir orkestravimo galimybėmis
- **Įgyvendinsite įmonės šablonus**: Kursite moduliarius, plečiamus AI sprendimus gamybai

## Sesijų struktūra

### [1: Pradžia su Foundry Local](./01.FoundryLocalSetup.md)
**Dėmesys**: Diegimas, CLI nustatymas, modelių diegimas ir aparatūros optimizavimas

**Pagrindinės temos**: Pilnas diegimas • CLI komandos • Modelių talpinimas • Aparatūros pagreitinimas • Kelių modelių diegimas

**Pavyzdys**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK integracija](./samples/02/README.md) • [Modelių atradimas ir testavimas](./samples/03/README.md)

**Trukmė**: 2-3 valandos | **Lygis**: Pradedantysis

---

### [2: AI sprendimų kūrimas su Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Dėmesys**: Pažangus promptų kūrimas, duomenų integracija ir debesų ryšys

**Pagrindinės temos**: Promptų kūrimas • Duomenų integracija • Azure darbo eiga • Našumo optimizavimas • Stebėjimas

**Pavyzdys**: [Chainlit RAG programa](./samples/04/README.md)

**Trukmė**: 2-3 valandos | **Lygis**: Vidutinis

---

### [3: Atvirojo kodo modeliai Foundry Local](./03.OpenSourceModels.md)
**Dėmesys**: Hugging Face integracija, BYOM strategijos ir bendruomenės modeliai

**Pagrindinės temos**: Hugging Face integracija • Bring-your-own-model • Model Mondays įžvalgos • Bendruomenės indėliai • Modelių pasirinkimas

**Pavyzdys**: [Daugiagentinis orkestravimas](./samples/05/README.md)

**Trukmė**: 2-3 valandos | **Lygis**: Vidutinis

---

### [4: Pažangiausių modelių tyrinėjimas](./04.CuttingEdgeModels.md)
**Dėmesys**: LLMs vs SLMs, EdgeAI įgyvendinimas ir pažangūs demonstraciniai pavyzdžiai

**Pagrindinės temos**: Modelių palyginimas • Edge vs debesų įžvalgos • Phi + ONNX Runtime • Chainlit RAG programa • WebGPU optimizavimas

**Pavyzdys**: [Modeliai kaip įrankiai maršrutizatorius](./samples/06/README.md)

**Trukmė**: 3-4 valandos | **Lygis**: Pažengęs

---

### [5: Greitas AI agentų kūrimas](./05.AIPoweredAgents.md)
**Dėmesys**: Agentų architektūros, sisteminiai promptai, pagrindimas ir orkestravimas

**Pagrindinės temos**: Agentų dizaino šablonai • Sisteminių promptų kūrimas • Pagrindimo technikos • Daugiagentinės sistemos • Gamybos diegimas

**Pavyzdys**: [Daugiagentinis orkestravimas](./samples/05/README.md) • [Pažangi daugiagentinė sistema](./samples/09/README.md)

**Trukmė**: 3-4 valandos | **Lygis**: Pažengęs

---

### [6: Foundry Local – Modeliai kaip įrankiai](./06.ModelsAsTools.md)
**Dėmesys**: Moduliniai AI sprendimai, įmonės mastelio didinimas ir gamybos šablonai

**Pagrindinės temos**: Modeliai kaip įrankiai • Vietinis diegimas • SDK/API integracija • Įmonės architektūros • Mastelio didinimo strategijos

**Pavyzdys**: [Modeliai kaip įrankiai maršrutizatorius](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Trukmė**: 3-4 valandos | **Lygis**: Ekspertas

---

### [7: Tiesioginės API integracijos šablonai](./samples/07/README.md)
**Dėmesys**: Gryna REST API integracija be SDK priklausomybių, siekiant maksimalaus valdymo

**Pagrindinės temos**: HTTP klientų įgyvendinimas • Individuali autentifikacija • Modelių sveikatos stebėjimas • Atsakymų srautinimas • Gamybos klaidų tvarkymas

**Pavyzdys**: [Tiesioginis API klientas](./samples/07/README.md)

**Trukmė**: 2-3 valandos | **Lygis**: Vidutinis

---

### [8: Windows 11 vietinė pokalbių programa](./samples/08/README.md)
**Dėmesys**: Modernių vietinių pokalbių programų kūrimas su Foundry Local integracija

**Pagrindinės temos**: Electron kūrimas • Fluent Design System • Vietinė Windows integracija • Real-time srautinimas • Pokalbių sąsajos dizainas

**Pavyzdys**: [Windows 11 pokalbių programa](./samples/08/README.md)

**Trukmė**: 3-4 valandos | **Lygis**: Pažengęs

---

### [9: Pažangus daugiagentinis orkestravimas](./samples/09/README.md)
**Dėmesys**: Sudėtinga agentų koordinacija, specializuotų užduočių delegavimas ir bendradarbiavimo AI darbo eigos

**Pagrindinės temos**: Intelektuali agentų koordinacija • Funkcijų kvietimo šablonai • Kryžminė agentų komunikacija • Darbo eigos orkestravimas • Kokybės užtikrinimo mechanizmai

**Pavyzdys**: [Pažangi daugiagentinė sistema](./samples/09/README.md)

**Trukmė**: 4-5 valandos | **Lygis**: Ekspertas

---

### [10: Foundry Local kaip įrankių sistema](./samples/10/README.md)
**Dėmesys**: Įrankių pirmumo architektūra, integruojant Foundry Local į esamas programas ir sistemas

**Pagrindinės temos**: LangChain integracija • Semantinės branduolio funkcijos • REST API sistemos • CLI įrankiai • Jupyter integracija • Gamybos diegimo šablonai

**Pavyzdys**: [Foundry Tools Framework](./samples/10/README.md)

**Trukmė**: 4-5 valandos | **Lygis**: Ekspertas

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
- Pagrindinės AI/ML koncepcijos
- Komandų eilutės pagrindai
- Python programavimo pagrindai
- REST API koncepcijos
- Pagrindinės promptų ir modelių įžvalgų žinios

## Modulio laiko planas

**Bendra numatoma trukmė**: 30-38 valandos

| Sesija | Dėmesio sritis | Pavyzdžiai | Laikas | Sudėtingumas |
|--------|----------------|------------|--------|--------------|
|  1 | Diegimas ir pagrindai | 01, 02, 03 | 2-3 valandos | Pradedantysis |
|  2 | AI sprendimai | 04 | 2-3 valandos | Vidutinis |
|  3 | Atvirojo kodo | 05 | 2-3 valandos | Vidutinis |
|  4 | Pažangūs modeliai | 06 | 3-4 valandos | Pažengęs |
|  5 | AI agentai | 05, 09 | 3-4 valandos | Pažengęs |
|  6 | Įmonės įrankiai | 06, 10 | 3-4 valandos | Ekspertas |
|  7 | Tiesioginė API integracija | 07 | 2-3 valandos | Vidutinis |
|  8 | Windows 11 pokalbių programa | 08 | 3-4 valandos | Pažengęs |
|  9 | Pažangus daugiagentinis | 09 | 4-5 valandos | Ekspertas |
| 10 | Įrankių sistema | 10 | 4-5 valandos | Ekspertas |

## Pagrindiniai ištekliai

**Oficiali dokumentacija:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) – Šaltinio kodas ir oficialūs pavyzdžiai
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) – Pilnas diegimo ir naudojimo vadovas
- [Model Mondays serija](https://aka.ms/model-mondays) – Savaitiniai modelių akcentai ir mokymai

**Bendruomenė ir palaikymas:**
- [Foundry Local diskusijos](https://github.com/microsoft/Foundry-Local/discussions) – Bendruomenės klausimai ir funkcijų prašymai
- [Microsoft AI kūrėjų bendruomenė](https://techcommunity.microsoft.com/category/artificialintelligence) – Naujausios naujienos ir geriausios praktikos

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
- **Įmonės mastelio didinimas**: Kurti programas, kurios plečiasi nuo vietinių prototipų iki įmonės diegimų
- **Privatumas ir saugumas**: Įgyvendinti privatumo išsaugojimo AI sprendimus su vietinėmis įžvalgomis

### Inovacijų gebėjimai
- **Greitas prototipų kūrimas**: Greitai kurti ir testuoti AI programų koncepcijas pagal visus 10 pavyzdžių šablonų
- **Bendruomenės integracija**: Pasinaudoti atvirojo kodo modeliais ir prisidėti prie ekosistemos
- **Pažangūs šablonai**: Įgyvendinti pažangius AI šablonus, įskaitant RAG, agentus ir įrankių integraciją
- **Sistemos meistriškumas**: Ekspertų lygio integracija su LangChain, Semantic Kernel, Chainlit ir Electron
- **Gamybos diegimas**: Diegti plečiamus AI sprendimus nuo vietinių prototipų iki įmonės sistemų
- **Ateities kūrimas**: Kurti programas, pasiruošusias naujoms AI technologijoms ir šablonams

## Pradžia

1. **Aplinkos paruošimas**: Užtikrinkite Windows 11 su rekomenduojama aparatūra (žr. Reikalavimus)
2. **Įdiekite Foundry Local**: Sekite 1 sesiją, kad pilnai įdiegtumėte ir sukonfigūruotumėte
3. **Vykdykite 01 pavyzdį**: Pradėkite nuo pagrindinės REST API integracijos, kad patikrintumėte nustatymus
4. **Eikite per pavyzdžius**: Užbaikite 01-10 pavyzdžius, kad pilnai įvaldytumėte

## Sėkmės rodikliai

Sekite savo pažangą per visus 10 išsamių pavyzdžių:

### Pagrindinis lygis (Pavyzdžiai 01-03)
- [ ] Sėkmingai įdiegti ir sukonfigūruoti Foundry Local
- [ ] Užbaigti REST API integraciją (Pavyzdys 01)
- [ ] Įgyvendinti OpenAI SDK suderinamumą (Pavyzdys 02)
- [ ] Atlikti modelių atradimą ir testavimą (Pavyzdys 03)

### Programų lygis (Pavyzdžiai 04-06)
- [ ] Diegti ir vykdyti bent 4 skirtingas modelių šeimas
- [ ] Sukurti funkcionalią RAG pokalbių programą (Pavyzdys 04)
- [ ] Sukurti daugiagentinę orkestravimo sistemą (Pavyzdys 05)
- [ ] Įgyvendinti intelektualų modelių maršrutizavimą (Pavyzdys 06)

### Pažangios integracijos lygis (Pavyzdžiai 07-10)
- [ ] Sukurti gamybai paruoštą API klientą (Pavyzdys 07)
- [ ] Sukurti Windows 11 vietinę pokalbių programą (Pavyzdys 08)
- [ ] Įgyvendinti pažangią daugiagentinę sistemą (Pavyzdys 09)
- [ ] Sukurti išsamią įrankių sistemą (Pavyzdys 10)

### Meistriškumo rodikliai
- [ ] Sėkmingai vykdyti visus 10 pavyzdžių be klaidų
- [ ] Pritaikyti bent 3 pavyzdžius specifiniams naudojimo atvejams
- [ ] Diegti 2+ pavyzdžius gamybos aplinkose
- [ ] Prisidėti prie pavyzdžių kodo patobulinimų ar plėtinių
- [ ] Integruoti Foundry Local šablonus į asmeninius/profesinius projektus

## Greito starto vadovas – visi 10 pavyzdžių

### Aplinkos paruošimas (Reikalinga visiems pavyzdžiams)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Pagrindiniai pavyzdžiai (01-06)

**Pavyzdys 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Pavyzdys 02: OpenAI SDK integracija**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Pavyzdys 03: Modelių atradimas ir testavimas**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**P
Šis modulis atspindi pažangiausius dirbtinio intelekto (DI) technologijų vystymosi pasiekimus, derindamas „Microsoft“ verslo lygio įrankius su atvirojo kodo ekosistemos lankstumu ir inovatyvumu. Įvaldę Foundry Local per visus 10 išsamių pavyzdžių, būsite DI taikymo kūrimo priešakyje.

**Pilnas mokymosi kelias:**
- **Pagrindai** (Pavyzdžiai 01-03): API integracija ir modelių valdymas
- **Taikymas** (Pavyzdžiai 04-06): RAG, agentai ir išmanus maršrutizavimas
- **Pažangus lygis** (Pavyzdžiai 07-10): Gamybos struktūros ir verslo integracija

Dėl „Azure OpenAI“ integracijos (2 sesija) žr. atskirų pavyzdžių README failus, kuriuose pateikiami reikalingi aplinkos kintamieji ir API versijos nustatymai.

---

