<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:48:16+00:00",
  "source_file": "Module08/README.md",
  "language_code": "cs"
}
-->
# Modul 08: Praktické zkušenosti s Microsoft Foundry Local - Kompletní sada nástrojů pro vývojáře

## Přehled

Microsoft Foundry Local představuje novou generaci vývoje AI na okraji sítě, která poskytuje vývojářům výkonné nástroje pro vytváření, nasazení a škálování AI aplikací lokálně, přičemž zajišťuje bezproblémovou integraci s Azure AI Foundry. Tento modul nabízí komplexní přehled Foundry Local od instalace až po pokročilý vývoj agentů.

**Klíčové technologie:**
- Microsoft Foundry Local CLI a SDK
- Integrace s Azure AI Foundry
- Lokální inferenční modely
- Lokální ukládání a optimalizace modelů
- Architektury založené na agentech

## Cíle modulu

Po dokončení tohoto modulu budete schopni:

- **Ovládnout nastavení Foundry Local**: Instalovat, konfigurovat a optimalizovat Foundry Local pro vývoj na Windows 11
- **Nasadit různé modely**: Spouštět modely phi, qwen, deepseek a GPT-OSS-20B lokálně pomocí CLI příkazů
- **Vytvářet produkční řešení**: Vytvářet AI aplikace s pokročilým návrhem promptů a integrací dat
- **Využívat open-source ekosystém**: Integrovat modely Hugging Face a příspěvky komunity
- **Porovnávat AI architektury**: Porozumět kompromisům mezi LLMs a SLMs a strategiím nasazení
- **Vyvíjet AI agenty**: Vytvářet inteligentní agenty pomocí architektury Foundry Local a technik uzemnění
- **Implementovat modely jako nástroje**: Vytvářet modulární, přizpůsobitelné AI řešení pro podnikové aplikace

## Struktura modulu

### [1: Začínáme s Foundry Local](./01.FoundryLocalSetup.md)
**Zaměření**: Instalace, nastavení CLI, ukládání modelů a hardwarová akcelerace

**Co se naučíte:**
- Kompletní instalace Foundry Local na Windows 11
- Konfigurace CLI a struktura příkazů
- Strategie ukládání modelů pro optimální výkon
- Nastavení a optimalizace hardwarové akcelerace
- Praktické nasazení modelů phi, qwen, deepseek a GPT-OSS-20B

**Délka**: 2-3 hodiny  
**Předpoklady**: Windows 11, základní znalost příkazového řádku

---

### [2: Vytváření AI řešení s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Zaměření**: Pokročilé návrhy promptů, integrace dat a akční úkoly

**Co se naučíte:**
- Pokročilé techniky návrhu promptů
- Vzory integrace dat a osvědčené postupy
- Vytváření akčních AI úkolů s Foundry Local
- Bezproblémové pracovní postupy integrace Azure AI Foundry
- Optimalizace výkonu a monitorování

**Délka**: 2-3 hodiny  
**Předpoklady**: Dokončení 1. lekce, účet Azure (volitelný)

---

### [3: Open-Source modely ve Foundry Local](./03.OpenSourceModels.md)
**Zaměření**: Integrace Hugging Face, strategie výběru modelů a příspěvky komunity

**Co se naučíte:**
- Integrace modelů Hugging Face s Foundry Local
- Strategie a implementace BYOM (Bring-Your-Own-Model)
- Postřehy ze série Model Mondays a příspěvky komunity
- Nasazení a optimalizace vlastních modelů
- Kritéria pro hodnocení a výběr modelů komunity

**Délka**: 2-3 hodiny  
**Předpoklady**: Dokončení lekcí 1-2, účet Hugging Face

---

### [4: Prozkoumání špičkových modelů - LLMs, SLMs a lokální inference](./04.CuttingEdgeModels.md)
**Zaměření**: Porovnání modelů, EdgeAI s Phi a ONNX Runtime, pokročilé ukázky

**Co se naučíte:**
- Komplexní porovnání LLMs vs SLMs a jejich využití
- Kompromisy mezi lokální a cloudovou inferencí a rozhodovací rámce
- Implementace EdgeAI s Phi a ONNX Runtime
- Vývoj a nasazení Chainlit RAG Chat App
- Optimalizační techniky pro inference pomocí WebGPU
- Integrace a schopnosti AI PC SDK

**Délka**: 3-4 hodiny  
**Předpoklady**: Dokončení lekcí 1-3, porozumění konceptům inference

---

### [5: Rychlý vývoj AI agentů s Foundry Local](./05.AIPoweredAgents.md)
**Zaměření**: Rychlý vývoj aplikací GenAI, systémové prompty, uzemnění a architektury agentů

**Co se naučíte:**
- Architektura agentů Foundry Local a návrhové vzory
- Návrh systémových promptů pro chování agentů
- Techniky uzemnění pro spolehlivé odpovědi agentů
- Pracovní postupy pro rychlý vývoj aplikací GenAI
- Orchestrace agentů a systémy s více agenty
- Strategie nasazení AI agentů do produkce

**Délka**: 3-4 hodiny  
**Předpoklady**: Dokončení lekcí 1-4, základní porozumění AI agentům

---

### [6: Foundry Local - Modely jako nástroje](./06.ModelsAsTools.md)
**Zaměření**: Modulární AI řešení, lokální nasazení a podnikové škálování

**Co se naučíte:**
- Používání AI modelů jako modulárních, přizpůsobitelných nástrojů
- Lokální nasazení bez závislosti na cloudu
- Inferenční řešení s nízkou latencí, efektivními náklady a ochranou soukromí
- Vzory integrace SDK, API a CLI
- Přizpůsobení modelů pro specifické případy použití
- Strategie škálování od lokálního nasazení po Azure AI Foundry
- Architektury AI aplikací připravené pro podnikové prostředí

**Délka**: 3-4 hodiny  
**Předpoklady**: Všechny předchozí lekce, zkušenosti s podnikovým vývojem výhodou

## Předpoklady

### Požadavky na systém
- **Operační systém**: Windows 11 (22H2 nebo novější)
- **Paměť**: 16GB RAM (doporučeno 32GB pro větší modely)
- **Úložiště**: 50GB volného místa pro ukládání modelů
- **Hardware**: Doporučeno zařízení s podporou NPU (Copilot+ PC), GPU volitelné
- **Síť**: Rychlé připojení k internetu pro počáteční stažení modelů

### Vývojové prostředí
- Visual Studio Code s rozšířením AI Toolkit
- Python 3.10+ a pip
- Git pro správu verzí
- PowerShell nebo příkazový řádek
- Azure CLI (volitelné pro integraci s cloudem)

### Znalostní předpoklady
- Základní porozumění konceptům AI/ML
- Znalost příkazového řádku
- Základy programování v Pythonu
- Koncepty REST API
- Základní znalost návrhu promptů a inference modelů

## Časový plán modulu

**Celkový odhadovaný čas**: 15-20 hodin

| Lekce | Oblast zaměření | Čas | Náročnost |
|-------|-----------------|-----|-----------|
|  1 | Nastavení a základy | 2-3 hodiny | Začátečník |
|  2 | AI řešení | 2-3 hodiny | Středně pokročilý |
|  3 | Open Source | 2-3 hodiny | Středně pokročilý |
|  4 | Pokročilé modely | 3-4 hodiny | Pokročilý |
|  5 | AI agenti | 3-4 hodiny | Pokročilý |
|  6 | Podnikové nástroje | 3-4 hodiny | Expert |

## Klíčové zdroje

### Primární dokumentace
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentace](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Série Model Mondays](https://aka.ms/model-mondays)

### Zdroje komunity
- [Diskuze komunity Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Ukázky Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Výsledky učení

Po dokončení tohoto modulu budete schopni:

### Technické dovednosti
- **Nasazení a správa**: Instalace Foundry Local v prostředí vývoje i produkce
- **Integrace modelů**: Práce s různými rodinami modelů od Microsoftu, Hugging Face a komunity
- **Vytváření aplikací**: Tvorba produkčně připravených AI aplikací s pokročilými funkcemi a optimalizacemi
- **Vývoj agentů**: Implementace sofistikovaných AI agentů s uzemněním, logikou a integrací nástrojů

### Strategické porozumění
- **Rozhodování o architektuře**: Informované volby mezi lokálním a cloudovým nasazením
- **Optimalizace výkonu**: Optimalizace výkonu inference na různých hardwarových konfiguracích
- **Podnikové škálování**: Návrh aplikací, které škálují od lokálních prototypů po podnikové nasazení
- **Ochrana soukromí a bezpečnost**: Implementace AI řešení s ochranou soukromí pomocí lokální inference

### Inovační schopnosti
- **Rychlé prototypování**: Rychlá tvorba a testování konceptů AI aplikací
- **Integrace komunity**: Využití open-source modelů a přispívání do ekosystému
- **Pokročilé vzory**: Implementace špičkových AI vzorů včetně RAG, agentů a integrace nástrojů
- **Vývoj připravený na budoucnost**: Tvorba aplikací připravených na nové AI technologie a vzory

## Jak začít

1. **Připravte si prostředí**: Zajistěte Windows 11 s doporučenými hardwarovými specifikacemi
2. **Nainstalujte předpoklady**: Nastavte vývojové nástroje a závislosti
3. **Začněte s lekcí 1**: Začněte instalací Foundry Local a základním nastavením
4. **Postupujte postupně**: Dokončete lekce v pořadí pro optimální postup učení
5. **Praktikujte průběžně**: Aplikujte koncepty prostřednictvím praktických cvičení a projektů

## Metriky úspěchu

Sledujte svůj pokrok v modulu:

- [ ] Úspěšně nainstalovat a nakonfigurovat Foundry Local
- [ ] Nasadit a spustit alespoň 4 různé rodiny modelů
- [ ] Vytvořit kompletní AI řešení s integrací dat
- [ ] Integrovat alespoň 2 open-source modely
- [ ] Vytvořit funkční RAG chat aplikaci
- [ ] Vyvinout a nasadit AI agenta
- [ ] Implementovat architekturu modelů jako nástrojů

## Rychlý start pro ukázky

### 1) Nastavení prostředí (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Spuštění lokálního modelu (nový terminál)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Spuštění ukázky Chainlit (lekce 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Spuštění koordinátoru pro více agentů (lekce 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Pokud se objeví chyby připojení, ověřte Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfigurace routeru (lekce 6)
Router provádí rychlou kontrolu stavu a podporuje konfiguraci na základě prostředí:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Tento modul představuje špičku vývoje AI na okraji sítě, kombinující podnikové nástroje Microsoftu s flexibilitou a inovací open-source ekosystému. Ovládnutím Foundry Local se ocitnete na čele vývoje AI aplikací.

Pro Azure OpenAI (lekce 2) si přečtěte README ukázky pro požadované proměnné prostředí a nastavení verze API.

## Přehled ukázek

- `samples/01`: Rychlý REST chat s Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integrace OpenAI SDK (`sdk_quickstart.py`).
- `samples/03`: Objevování modelů + rychlý benchmark (`list_and_bench.cmd`).
- `samples/04`: Ukázka Chainlit RAG (`app.py`).
- `samples/05`: Orchestrace více agentů (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router pro modely jako nástroje (`python samples\06\router.py`).

---

