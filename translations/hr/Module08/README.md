<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:51:01+00:00",
  "source_file": "Module08/README.md",
  "language_code": "hr"
}
-->
# Modul 08: Praktično s Microsoft Foundry Local - Kompletan alat za razvoj

## Pregled

Microsoft Foundry Local predstavlja novu generaciju razvoja AI tehnologije na rubu, pružajući programerima moćne alate za izgradnju, implementaciju i skaliranje AI aplikacija lokalno, uz besprijekornu integraciju s Azure AI Foundry. Ovaj modul pruža sveobuhvatan pregled Foundry Local-a, od instalacije do naprednog razvoja agenata.

**Ključne tehnologije:**
- Microsoft Foundry Local CLI i SDK
- Integracija s Azure AI Foundry
- Lokalna inferencija modela
- Lokalno predmemoriranje i optimizacija modela
- Arhitekture temeljene na agentima

## Ciljevi učenja modula

Nakon završetka ovog modula, moći ćete:

- **Savladati postavljanje Foundry Local-a**: Instalirati, konfigurirati i optimizirati Foundry Local za razvoj na Windows 11
- **Implementirati raznolike modele**: Pokrenuti phi, qwen, deepseek i GPT-OSS-20B modele lokalno pomoću CLI naredbi
- **Izraditi produkcijska rješenja**: Kreirati AI aplikacije uz napredno oblikovanje upita i integraciju podataka
- **Iskoristiti ekosustav otvorenog koda**: Integrirati modele Hugging Face i dodatke koje je kreirala zajednica
- **Usporediti AI arhitekture**: Razumjeti prednosti i nedostatke LLM-a u odnosu na SLM-e te strategije implementacije
- **Razviti AI agente**: Izgraditi inteligentne agente koristeći arhitekturu Foundry Local-a i tehnike uzemljenja
- **Implementirati modele kao alate**: Kreirati modularna, prilagodljiva AI rješenja za poslovne aplikacije

## Struktura sesija

### [1: Početak rada s Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Instalacija, postavljanje CLI-a, predmemoriranje modela i ubrzanje hardvera

**Što ćete naučiti:**
- Potpuna instalacija Foundry Local-a na Windows 11
- Konfiguracija CLI-a i struktura naredbi
- Strategije predmemoriranja modela za optimalne performanse
- Postavljanje i optimizacija ubrzanja hardvera
- Praktična implementacija phi, qwen, deepseek i GPT-OSS-20B modela

**Trajanje**: 2-3 sata  
**Preduvjeti**: Windows 11, osnovno znanje naredbenog retka

---

### [2: Izgradnja AI rješenja s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Napredno oblikovanje upita, integracija podataka i primjenjivi zadaci

**Što ćete naučiti:**
- Tehnike naprednog oblikovanja upita
- Obrasci integracije podataka i najbolje prakse
- Izrada primjenjivih AI zadataka s Foundry Local-om
- Besprijekorni tijekovi integracije s Azure AI Foundry
- Optimizacija performansi i praćenje

**Trajanje**: 2-3 sata  
**Preduvjeti**: Završetak sesije 1, Azure račun (opcionalno)

---

### [3: Foundry Local i modeli otvorenog koda](./03.OpenSourceModels.md)
**Fokus**: Integracija Hugging Face modela, strategije odabira modela i doprinosi zajednice

**Što ćete naučiti:**
- Integracija Hugging Face modela s Foundry Local-om
- Strategije i implementacija "donosi svoj model" (BYOM)
- Uvidi iz serije Model Mondays i doprinosi zajednice
- Prilagodba i optimizacija modela
- Kriteriji za evaluaciju i odabir modela zajednice

**Trajanje**: 2-3 sata  
**Preduvjeti**: Završetak sesija 1-2, Hugging Face račun

---

### [4: Istraživanje najnovijih modela - LLM-i, SLM-i i lokalna inferencija](./04.CuttingEdgeModels.md)
**Fokus**: Usporedba modela, EdgeAI s Phi i ONNX Runtime-om, napredne demonstracije

**Što ćete naučiti:**
- Sveobuhvatna usporedba LLM-a i SLM-a te primjeri upotrebe
- Lokalna vs cloud inferencija: prednosti i odluke
- Implementacija EdgeAI-a s Phi i ONNX Runtime-om
- Razvoj i implementacija Chainlit RAG Chat aplikacije
- Tehnike optimizacije inferencije s WebGPU-om
- Integracija i mogućnosti AI PC SDK-a

**Trajanje**: 3-4 sata  
**Preduvjeti**: Završetak sesija 1-3, razumijevanje koncepta inferencije

---

### [5: Brza izrada AI agenata s Foundry Local-om](./05.AIPoweredAgents.md)
**Fokus**: Brzi razvoj GenAI aplikacija, sistemski upiti, uzemljenje i arhitekture agenata

**Što ćete naučiti:**
- Arhitektura agenata Foundry Local-a i obrasci dizajna
- Oblikovanje sistemskih upita za ponašanje agenata
- Tehnike uzemljenja za pouzdane odgovore agenata
- Tijekovi brzog razvoja GenAI aplikacija
- Orkestracija agenata i sustavi s više agenata
- Strategije produkcijske implementacije za AI agente

**Trajanje**: 3-4 sata  
**Preduvjeti**: Završetak sesija 1-4, osnovno razumijevanje AI agenata

---

### [6: Foundry Local - modeli kao alati](./06.ModelsAsTools.md)
**Fokus**: Modularna AI rješenja, lokalna implementacija i skaliranje za poduzeća

**Što ćete naučiti:**
- Korištenje AI modela kao modularnih, prilagodljivih alata
- Lokalna implementacija bez ovisnosti o oblaku
- Inferencija s niskom latencijom, ekonomična i uz očuvanje privatnosti
- Obrasci integracije SDK-a, API-ja i CLI-a
- Prilagodba modela za specifične slučajeve upotrebe
- Strategije skaliranja od lokalnog do Azure AI Foundry-a
- Arhitekture AI aplikacija spremne za poduzeća

**Trajanje**: 3-4 sata  
**Preduvjeti**: Sve prethodne sesije, korisno iskustvo u razvoju za poduzeća

## Preduvjeti

### Zahtjevi sustava
- **Operativni sustav**: Windows 11 (22H2 ili noviji)
- **Memorija**: 16GB RAM-a (32GB preporučeno za veće modele)
- **Pohrana**: 50GB slobodnog prostora za predmemoriranje modela
- **Hardver**: Preporučen uređaj s NPU-om (Copilot+ PC), GPU opcionalan
- **Mreža**: Brzi internet za početno preuzimanje modela

### Razvojno okruženje
- Visual Studio Code s AI Toolkit ekstenzijom
- Python 3.10+ i pip
- Git za kontrolu verzija
- PowerShell ili Command Prompt
- Azure CLI (opcionalno za integraciju s oblakom)

### Preduvjeti znanja
- Osnovno razumijevanje AI/ML koncepata
- Poznavanje naredbenog retka
- Osnove programiranja u Pythonu
- Koncepti REST API-ja
- Osnovno znanje o oblikovanju upita i inferenciji modela

## Vremenski okvir modula

**Ukupno procijenjeno vrijeme**: 15-20 sati

| Sesija | Fokus područje | Vrijeme | Složenost |
|--------|----------------|---------|-----------|
|  1 | Postavljanje i osnove | 2-3 sata | Početnik |
|  2 | AI rješenja | 2-3 sata | Srednje |
|  3 | Otvoreni kod | 2-3 sata | Srednje |
|  4 | Napredni modeli | 3-4 sata | Napredno |
|  5 | AI agenti | 3-4 sata | Napredno |
|  6 | Alati za poduzeća | 3-4 sata | Ekspert |

## Ključni resursi

### Primarna dokumentacija
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Resursi zajednice
- [Foundry Local Rasprave zajednice](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Primjeri](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Zajednica programera](https://techcommunity.microsoft.com/category/artificialintelligence)

## Ishodi učenja

Nakon završetka ovog modula, bit ćete osposobljeni za:

### Tehničko znanje
- **Implementacija i upravljanje**: Instalacije Foundry Local-a u razvojnim i produkcijskim okruženjima
- **Integracija modela**: Besprijekoran rad s raznolikim obiteljima modela iz Microsofta, Hugging Face-a i izvora zajednice
- **Izrada aplikacija**: Kreiranje AI aplikacija spremnih za produkciju s naprednim značajkama i optimizacijama
- **Razvoj agenata**: Implementacija sofisticiranih AI agenata s uzemljenjem, zaključivanjem i integracijom alata

### Strateško razumijevanje
- **Odluke o arhitekturi**: Donošenje informiranih odluka između lokalne i cloud implementacije
- **Optimizacija performansi**: Optimizacija performansi inferencije na različitim hardverskim konfiguracijama
- **Skaliranje za poduzeća**: Dizajn aplikacija koje se skaliraju od lokalnih prototipova do implementacija u poduzećima
- **Privatnost i sigurnost**: Implementacija AI rješenja koja čuvaju privatnost uz lokalnu inferenciju

### Inovacijske sposobnosti
- **Brzo prototipiranje**: Brza izrada i testiranje AI koncepta aplikacija
- **Integracija zajednice**: Iskorištavanje modela otvorenog koda i doprinos ekosustavu
- **Napredni obrasci**: Implementacija najnovijih AI obrazaca uključujući RAG, agente i integraciju alata
- **Razvoj spreman za budućnost**: Izrada aplikacija spremnih za nove AI tehnologije i obrasce

## Početak rada

1. **Pripremite svoje okruženje**: Osigurajte Windows 11 s preporučenim hardverskim specifikacijama
2. **Instalirajte preduvjete**: Postavite razvojne alate i ovisnosti
3. **Započnite sa sesijom 1**: Počnite s instalacijom i osnovnim postavljanjem Foundry Local-a
4. **Napredujte redoslijedom**: Završite sesije po redu za optimalan napredak u učenju
5. **Kontinuirano vježbajte**: Primjenjujte koncepte kroz praktične vježbe i projekte

## Metrike uspjeha

Pratite svoj napredak kroz modul:

- [ ] Uspješno instalirajte i konfigurirajte Foundry Local
- [ ] Implementirajte i pokrenite najmanje 4 različite obitelji modela
- [ ] Izradite kompletno AI rješenje s integracijom podataka
- [ ] Integrirajte najmanje 2 modela otvorenog koda
- [ ] Kreirajte funkcionalnu RAG chat aplikaciju
- [ ] Razvijte i implementirajte AI agenta
- [ ] Implementirajte arhitekturu modela kao alata

## Brzi početak za primjere

### 1) Postavljanje okruženja (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Pokrenite lokalni model (novi terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Pokrenite Chainlit demo (Sesija 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Pokrenite koordinator za više agenata (Sesija 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Ako vidite greške povezivanja, provjerite Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfiguracija routera (Sesija 6)
Router provodi brzu provjeru zdravlja i podržava konfiguraciju temeljenu na okruženju:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ovaj modul predstavlja vrhunac razvoja AI tehnologije na rubu, kombinirajući Microsoftove alate za poduzeća s fleksibilnošću i inovacijama ekosustava otvorenog koda. Savladavanjem Foundry Local-a, bit ćete na čelu razvoja AI aplikacija.

Za Azure OpenAI (Sesija 2), pogledajte README za potrebne varijable okruženja i postavke verzije API-ja.

## Pregled primjera

- `samples/01`: Brzi REST chat s Foundry Local-om (`chat_quickstart.py`).
- `samples/02`: Integracija OpenAI SDK-a (`sdk_quickstart.py`).
- `samples/03`: Otkrivanje modela + brzi test (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demo (`app.py`).
- `samples/05`: Orkestracija više agenata (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router za modele kao alate (`python samples\06\router.py`).

---

