<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-23T00:51:32+00:00",
  "source_file": "Module08/README.md",
  "language_code": "sl"
}
-->
# Modul 08: Praktično delo z Microsoft Foundry Local - Celovit razvojni komplet

## Pregled

Microsoft Foundry Local predstavlja naslednjo generacijo razvoja AI na robu, ki razvijalcem omogoča zmogljiva orodja za lokalno gradnjo, uvajanje in skaliranje AI aplikacij, hkrati pa ohranja brezhibno integracijo z Azure AI Foundry. Ta modul ponuja celovit pregled Foundry Local, od namestitve do naprednega razvoja agentov.

**Ključne tehnologije:**
- Microsoft Foundry Local CLI in SDK
- Integracija z Azure AI Foundry
- Lokalna inferenca modelov
- Predpomnjenje in optimizacija modelov na napravi
- Arhitekture, ki temeljijo na agentih

## Cilji učenja modula

Z zaključkom tega modula boste:

- **Obvladali nastavitev Foundry Local**: Namestili, konfigurirali in optimizirali Foundry Local za razvoj na Windows 11
- **Uvajali različne modele**: Lokalno izvajali modele phi, qwen, deepseek in GPT-OSS-20B z ukazi CLI
- **Gradili produkcijske rešitve**: Ustvarili AI aplikacije z naprednim oblikovanjem pozivov in integracijo podatkov
- **Izkoristili odprtokodni ekosistem**: Integrirali modele Hugging Face in dodatke skupnosti
- **Primerjali AI arhitekture**: Razumeli razlike med LLM in SLM ter strategije uvajanja
- **Razvijali AI agente**: Gradili inteligentne agente z arhitekturo Foundry Local in zmožnostmi utemeljevanja
- **Implementirali modele kot orodja**: Ustvarili modularne, prilagodljive AI rešitve za poslovne aplikacije

## Struktura seje

### [1: Začetek z Foundry Local](./01.FoundryLocalSetup.md)
**Osredotočenost**: Namestitev, nastavitev CLI, predpomnjenje modelov in pospeševanje strojne opreme

**Kaj se boste naučili:**
- Popolna namestitev Foundry Local na Windows 11
- Konfiguracija CLI in struktura ukazov
- Strategije predpomnjenja modelov za optimalno zmogljivost
- Nastavitev in optimizacija strojnega pospeševanja
- Praktično uvajanje modelov phi, qwen, deepseek in GPT-OSS-20B

**Trajanje**: 2-3 ure  
**Predpogoji**: Windows 11, osnovno znanje ukazne vrstice

---

### [2: Gradnja AI rešitev z Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Osredotočenost**: Napredno oblikovanje pozivov, integracija podatkov in izvedljive naloge

**Kaj se boste naučili:**
- Tehnike naprednega oblikovanja pozivov
- Vzorci integracije podatkov in najboljše prakse
- Gradnja izvedljivih AI nalog z Foundry Local
- Brezhibni delovni tokovi integracije z Azure AI Foundry
- Optimizacija zmogljivosti in spremljanje

**Trajanje**: 2-3 ure  
**Predpogoji**: Zaključek seje 1, Azure račun (neobvezno)

---

### [3: Odprtokodni modeli Foundry Local](./03.OpenSourceModels.md)
**Osredotočenost**: Integracija Hugging Face, strategije izbire modelov in dodatki skupnosti

**Kaj se boste naučili:**
- Integracija modelov Hugging Face z Foundry Local
- Strategije in implementacija "prinesi svoj model" (BYOM)
- Vpogledi iz serije Model Mondays in prispevki skupnosti
- Uvajanje in optimizacija prilagojenih modelov
- Merila za ocenjevanje in izbiro modelov skupnosti

**Trajanje**: 2-3 ure  
**Predpogoji**: Zaključek sej 1-2, Hugging Face račun

---

### [4: Raziskovanje najsodobnejših modelov - LLM, SLM in inferenca na napravi](./04.CuttingEdgeModels.md)
**Osredotočenost**: Primerjava modelov, EdgeAI s Phi in ONNX Runtime, napredni prikazi

**Kaj se boste naučili:**
- Celovita primerjava LLM in SLM ter primeri uporabe
- Lokalni vs. oblačni kompromisi pri inferenci in okvirji odločanja
- Implementacija EdgeAI s Phi in ONNX Runtime
- Razvoj in uvajanje aplikacije Chainlit RAG Chat
- Tehnike optimizacije inferenc z WebGPU
- Integracija in zmožnosti AI PC SDK

**Trajanje**: 3-4 ure  
**Predpogoji**: Zaključek sej 1-3, razumevanje konceptov inferenc

---

### [5: Hitro gradite AI-agente z Foundry Local](./05.AIPoweredAgents.md)
**Osredotočenost**: Hiter razvoj aplikacij GenAI, sistemski pozivi, utemeljevanje in arhitekture agentov

**Kaj se boste naučili:**
- Arhitektura agentov Foundry Local in vzorci oblikovanja
- Oblikovanje sistemskih pozivov za vedenje agentov
- Tehnike utemeljevanja za zanesljive odgovore agentov
- Delovni tokovi za hiter razvoj aplikacij GenAI
- Orkestracija agentov in sistemi z več agenti
- Strategije produkcijskega uvajanja za AI-agente

**Trajanje**: 3-4 ure  
**Predpogoji**: Zaključek sej 1-4, osnovno razumevanje AI-agentov

---

### [6: Foundry Local - modeli kot orodja](./06.ModelsAsTools.md)
**Osredotočenost**: Modularne AI rešitve, uvajanje na napravi in skaliranje v podjetjih

**Kaj se boste naučili:**
- Obravnavanje AI modelov kot modularnih, prilagodljivih orodij
- Uvajanje na napravi brez odvisnosti od oblaka
- Inferenca z nizko zakasnitvijo, stroškovno učinkovitostjo in ohranjanjem zasebnosti
- Vzorci integracije SDK, API in CLI
- Prilagoditev modelov za specifične primere uporabe
- Strategije skaliranja od lokalnega do Azure AI Foundry
- Arhitekture AI aplikacij, pripravljene za podjetja

**Trajanje**: 3-4 ure  
**Predpogoji**: Vse prejšnje seje, koristne izkušnje z razvojem v podjetjih

## Predpogoji

### Sistemske zahteve
- **Operacijski sistem**: Windows 11 (22H2 ali novejši)
- **Pomnilnik**: 16GB RAM (32GB priporočeno za večje modele)
- **Shramba**: 50GB prostega prostora za predpomnjenje modelov
- **Strojna oprema**: Priporočena naprava z NPU (Copilot+ PC), GPU neobvezno
- **Omrežje**: Hitra internetna povezava za začetne prenose modelov

### Razvojno okolje
- Visual Studio Code z razširitvijo AI Toolkit
- Python 3.10+ in pip
- Git za nadzor različic
- PowerShell ali ukazna vrstica
- Azure CLI (neobvezno za integracijo z oblakom)

### Zahteve glede znanja
- Osnovno razumevanje konceptov AI/ML
- Seznanjenost z ukazno vrstico
- Osnove programiranja v Pythonu
- Koncepti REST API
- Osnovno znanje oblikovanja pozivov in inferenc modelov

## Časovnica modula

**Skupni ocenjeni čas**: 15-20 ur

| Seja | Osredotočenost | Čas | Kompleksnost |
|------|----------------|-----|--------------|
|  1 | Nastavitev in osnove | 2-3 ure | Začetnik |
|  2 | AI rešitve | 2-3 ure | Srednje |
|  3 | Odprtokodni modeli | 2-3 ure | Srednje |
|  4 | Napredni modeli | 3-4 ure | Napredno |
|  5 | AI-agenti | 3-4 ure | Napredno |
|  6 | Orodja za podjetja | 3-4 ure | Strokovno |

## Ključni viri

### Primarna dokumentacija
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Serija Model Mondays](https://aka.ms/model-mondays)

### Viri skupnosti
- [Razprave skupnosti Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Vzorci](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Razvojna skupnost](https://techcommunity.microsoft.com/category/artificialintelligence)

## Rezultati učenja

Po zaključku tega modula boste opremljeni za:

### Tehnično obvladovanje
- **Uvajanje in upravljanje**: Namestitve Foundry Local v razvojnih in produkcijskih okoljih
- **Integracija modelov**: Brezhibno delo z različnimi družinami modelov Microsoft, Hugging Face in skupnosti
- **Gradnja aplikacij**: Ustvarjanje produkcijsko pripravljenih AI aplikacij z naprednimi funkcijami in optimizacijami
- **Razvoj agentov**: Implementacija sofisticiranih AI agentov z utemeljevanjem, razmišljanjem in integracijo orodij

### Strateško razumevanje
- **Odločitve o arhitekturi**: Informirane izbire med lokalnim in oblačnim uvajanjem
- **Optimizacija zmogljivosti**: Optimizacija zmogljivosti inferenc na različnih strojnih konfiguracijah
- **Skaliranje v podjetjih**: Oblikovanje aplikacij, ki se skalirajo od lokalnih prototipov do uvajanja v podjetjih
- **Zasebnost in varnost**: Implementacija rešitev AI, ki ohranjajo zasebnost z lokalno inferenco

### Inovacijske zmožnosti
- **Hitro prototipiranje**: Hitro gradnjo in testiranje konceptov AI aplikacij
- **Integracija skupnosti**: Izkoristite odprtokodne modele in prispevajte k ekosistemu
- **Napredni vzorci**: Implementacija najsodobnejših AI vzorcev, vključno z RAG, agenti in integracijo orodij
- **Razvoj, pripravljen na prihodnost**: Gradnja aplikacij, pripravljenih na nove tehnologije in vzorce AI

## Začetek

1. **Pripravite okolje**: Poskrbite za Windows 11 z priporočenimi specifikacijami strojne opreme
2. **Namestite predpogoje**: Nastavite razvojna orodja in odvisnosti
3. **Začnite s sejo 1**: Začnite z namestitvijo in osnovno nastavitvijo Foundry Local
4. **Napredujte zaporedno**: Zaključite seje po vrsti za optimalno učno napredovanje
5. **Nenehno vadite**: Uporabljajte koncepte skozi praktične vaje in projekte

## Merila uspeha

Spremljajte svoj napredek skozi modul:

- [ ] Uspešno namestite in konfigurirajte Foundry Local
- [ ] Uvajajte in izvajajte vsaj 4 različne družine modelov
- [ ] Zgradite popolno AI rešitev z integracijo podatkov
- [ ] Integrirajte vsaj 2 odprtokodna modela
- [ ] Ustvarite funkcionalno aplikacijo RAG za klepet
- [ ] Razvijte in uvedite AI agenta
- [ ] Implementirajte arhitekturo modelov kot orodij

## Hiter začetek za vzorce

### 1) Nastavitev okolja (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Zaženite lokalni model (nov terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Zaženite Chainlit demo (Seja 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Zaženite koordinatorja več agentov (Seja 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Če opazite napake povezave, preverite Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Konfiguracija usmerjevalnika (Seja 6)
Usmerjevalnik izvaja hitro preverjanje stanja in podpira konfiguracijo na osnovi okolja:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ta modul predstavlja najsodobnejši razvoj AI na robu, ki združuje Microsoftova orodja za podjetja z fleksibilnostjo in inovativnostjo odprtokodnega ekosistema. Z obvladovanjem Foundry Local boste na čelu razvoja AI aplikacij.

Za Azure OpenAI (Seja 2) si oglejte vzorčni README za potrebne spremenljivke okolja in nastavitve različice API.

## Pregled vzorcev

- `samples/01`: Hiter REST klepet s Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integracija OpenAI SDK (`sdk_quickstart.py`).
- `samples/03`: Odkritje modelov + hitra primerjava (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demo (`app.py`).
- `samples/05`: Orkestracija več agentov (`python -m samples.05.agents.coordinator`).
- `samples/06`: Usmerjevalnik modelov kot orodij (`python samples\06\router.py`).

---

