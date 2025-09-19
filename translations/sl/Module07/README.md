<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-19T01:49:17+00:00",
  "source_file": "Module07/README.md",
  "language_code": "sl"
}
-->
# Poglavje 07: Primeri EdgeAI

Edge AI predstavlja združitev umetne inteligence z robnim računalništvom, kar omogoča inteligentno obdelavo neposredno na napravah, brez odvisnosti od povezave v oblak. To poglavje raziskuje pet različnih implementacij EdgeAI na različnih platformah in okvirjih, ki prikazujejo vsestranskost in moč izvajanja AI modelov na robu.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano predstavlja preboj v dostopnem robnem AI računalništvu, saj ponuja do 67 TOPS zmogljivosti AI v kompaktni obliki velikosti kreditne kartice. Ta zmogljiva platforma za robno AI demokratizira razvoj generativne AI za navdušence, študente in profesionalne razvijalce.

### Ključne značilnosti
- Ponuja do 67 TOPS zmogljivosti AI—1,7-kratno izboljšanje v primerjavi s predhodnikom
- 1024 CUDA jeder in do 32 Tensor jeder za AI obdelavo
- 6-jedrni Arm Cortex-A78AE v8.2 64-bitni CPU z največjo frekvenco 1,5 GHz
- Cena le 249 $, kar razvijalcem, študentom in ustvarjalcem omogoča najbolj dostopno platformo

### Uporabe
Jetson Orin Nano odlično izvaja sodobne generativne AI modele, vključno z vizualnimi transformatorji, velikimi jezikovnimi modeli in modeli za vizualno-jezikovne naloge. Posebej je zasnovan za primere uporabe GenAI, zdaj pa lahko več LLM-jev izvajate na napravi, ki jo držite v dlani. Priljubljeni primeri uporabe vključujejo robote, ki jih poganja AI, pametne drone, inteligentne kamere in avtonomne robne naprave.

**Več informacij**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI v mobilnih aplikacijah z .NET MAUI in ONNX Runtime GenAI

Ta rešitev prikazuje, kako integrirati generativno AI in velike jezikovne modele (LLM) v mobilne aplikacije na več platformah z uporabo .NET MAUI (Multi-platform App UI) in ONNX Runtime GenAI. Ta pristop omogoča .NET razvijalcem gradnjo naprednih mobilnih aplikacij, ki delujejo nativno na napravah Android in iOS.

### Ključne značilnosti
- Zgrajeno na .NET MAUI okvirju, ki omogoča enotno kodo za aplikacije na Androidu in iOS-u
- Integracija ONNX Runtime GenAI omogoča izvajanje generativnih AI modelov neposredno na mobilnih napravah
- Podpora za različne strojne pospeševalnike, prilagojene mobilnim napravam, vključno s CPU, GPU in specializiranimi mobilnimi AI procesorji
- Optimizacije specifične za platformo, kot so CoreML za iOS in NNAPI za Android prek ONNX Runtime
- Implementira celoten generativni AI cikel, vključno s pred- in post-obdelavo, inferenco, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika

### Prednosti razvoja
Pristop .NET MAUI omogoča razvijalcem, da izkoristijo svoje obstoječe znanje C# in .NET pri gradnji AI aplikacij na več platformah. ONNX Runtime GenAI podpira več arhitektur modelov, vključno z Llama, Mistral, Phi, Gemma in mnogimi drugimi. Optimizirana ARM64 jedra pospešujejo INT4 kvantizirano množenje matrik, kar zagotavlja učinkovito delovanje na mobilni strojni opremi ob ohranjanju znanega .NET razvojnega okolja.

### Primeri uporabe
Ta rešitev je idealna za razvijalce, ki želijo graditi mobilne aplikacije, ki jih poganja AI, z uporabo .NET tehnologij, vključno z inteligentnimi klepetalniki, aplikacijami za prepoznavanje slik, orodji za prevajanje jezikov in sistemi za personalizirana priporočila, ki delujejo povsem na napravi za izboljšano zasebnost in delovanje brez povezave.

**Več informacij**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI v Azure z motorjem za majhne jezikovne modele

Microsoftova rešitev EdgeAI, ki temelji na Azure, se osredotoča na učinkovito uvajanje majhnih jezikovnih modelov (SLM) v hibridnih okoljih oblak-rob. Ta pristop povezuje obsežne AI storitve v oblaku z zahtevami za robno uvajanje.

### Prednosti arhitekture
- Brezhibna integracija z Azure AI storitvami
- Izvajanje SLM/LLM in multimodalnih modelov na napravi in v oblaku z ONNX Runtime
- Optimizirano za uvajanje na ravni podjetja
- Podpora za stalne posodobitve in upravljanje modelov

### Primeri uporabe
Azure EdgeAI implementacija je odlična v scenarijih, ki zahtevajo AI uvajanje na ravni podjetja z zmogljivostmi upravljanja v oblaku. To vključuje inteligentno obdelavo dokumentov, analitiko v realnem času in hibridne AI delovne tokove, ki izkoriščajo tako oblak kot robno računalništvo.

**Več informacij**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI z Windows ML

Windows ML predstavlja Microsoftov napreden runtime, optimiziran za zmogljivo izvajanje modelov na napravi in poenostavljeno uvajanje, ki služi kot temelj Windows AI Foundry. Ta platforma omogoča razvijalcem ustvarjanje aplikacij za Windows, ki izkoriščajo celoten spekter strojne opreme PC.

### Zmožnosti platforme
- Deluje na vseh Windows 11 PC-jih z različico 24H2 (build 26100) ali novejšo
- Deluje na vseh x64 in ARM64 PC strojnih opremah, tudi na PC-jih brez NPU-jev ali GPU-jev
- Omogoča razvijalcem, da prinesejo svoje modele in jih učinkovito uvajajo v ekosistem strojnih partnerjev, vključno z AMD, Intel, NVIDIA in Qualcomm, ki zajema CPU, GPU, NPU
- Z uporabo infrastrukturnih API-jev razvijalcem ni več treba ustvarjati več graditev aplikacije za ciljanje na različne strojne opreme

### Prednosti za razvijalce
Windows ML abstrahira strojno opremo in izvajalne ponudnike, tako da se lahko osredotočite na pisanje kode. Poleg tega se Windows ML samodejno posodablja, da podpira najnovejše NPU-je, GPU-je in CPU-je, ko so izdani. Platforma zagotavlja enoten okvir za AI razvoj v raznolikem ekosistemu strojne opreme Windows.

**Več informacij**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Celovit vodnik za razvoj Windows Edge AI

## 5. EdgeAI z lokalnimi aplikacijami Foundry

Foundry Local omogoča razvijalcem gradnjo aplikacij za pridobivanje z obogateno generacijo (RAG) z uporabo lokalnih virov v .NET, ki združujejo lokalne jezikovne modele s semantičnimi iskalnimi zmogljivostmi. Ta pristop zagotavlja rešitve AI, osredotočene na zasebnost, ki delujejo povsem na lokalni infrastrukturi.

### Tehnična arhitektura
- Združuje jezikovni model Phi-3, lokalne vektorske predstavitve in semantično jedro za ustvarjanje scenarija RAG
- Uporablja vektorske predstavitve kot nizove plavajočih vrednosti, ki predstavljajo vsebino in njen semantični pomen
- Semantično jedro deluje kot glavni usklajevalec, ki združuje Phi-3 in pametne komponente za ustvarjanje brezhibnega RAG procesa
- Podpora za lokalne vektorske baze podatkov, vključno z SQLite in Qdrant

### Prednosti implementacije
RAG, ali pridobivanje z obogateno generacijo, je le prefinjen način za "iskanje informacij in njihovo vključitev v poziv". Ta lokalna implementacija zagotavlja zasebnost podatkov, hkrati pa ponuja inteligentne odgovore, ki temeljijo na prilagojenih bazah znanja. Pristop je še posebej dragocen za scenarije v podjetjih, ki zahtevajo suverenost podatkov in zmogljivosti delovanja brez povezave.

**Več informacij**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Razvojni viri za Windows EdgeAI

Za razvijalce, ki ciljajo na platformo Windows, smo pripravili celovit vodnik, ki pokriva celoten ekosistem Windows EdgeAI. Ta vir ponuja podrobne informacije o Windows AI Foundry, vključno z API-ji, orodji in najboljšimi praksami za razvoj EdgeAI na Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry ponuja celovit nabor orodij in API-jev, posebej zasnovanih za razvoj Edge AI na napravah Windows. To vključuje specializirano podporo za strojno opremo, pospešeno z NPU-ji, integracijo Windows ML in tehnike optimizacije specifične za platformo.

**Celovit vodnik**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Ta vodnik pokriva:
- Pregled platforme Windows AI Foundry in komponent
- Phi Silica API za učinkovito izvajanje na strojni opremi NPU
- API-ji za računalniški vid za obdelavo slik in OCR
- Integracija in optimizacija Windows ML runtime
- Foundry Local CLI za lokalni razvoj in testiranje
- Strategije optimizacije strojne opreme za naprave Windows
- Praktični primeri implementacije in najboljše prakse

### AI orodja za razvoj Edge AI
Za razvijalce, ki uporabljajo Visual Studio Code, razširitev AI Toolkit ponuja celovito razvojno okolje, posebej zasnovano za gradnjo, testiranje in uvajanje Edge AI aplikacij. Ta orodja poenostavijo celoten razvojni proces Edge AI znotraj VS Code.

**Razvojni vodnik**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Vodnik AI Toolkit pokriva:
- Iskanje in izbiro modelov za robno uvajanje
- Lokalni testni in optimizacijski procesi
- Integracija ONNX in Ollama za robne modele
- Tehnike pretvorbe in kvantizacije modelov
- Razvoj agentov za robne scenarije
- Ocena zmogljivosti in spremljanje
- Priprava na uvajanje in najboljše prakse

## Zaključek

Teh pet implementacij EdgeAI prikazuje zrelost in raznolikost robnih AI rešitev, ki so danes na voljo. Od naprav z robnim pospeševanjem, kot je Jetson Orin Nano, do programske opreme, kot sta ONNX Runtime GenAI in Windows ML, imajo razvijalci neprimerljive možnosti za uvajanje inteligentnih aplikacij na robu.

Skupna nit teh platform je demokratizacija AI zmogljivosti, ki omogoča dostop do naprednega strojnega učenja razvijalcem z različnimi stopnjami znanja in primeri uporabe. Ne glede na to, ali gradite mobilne aplikacije, namizno programsko opremo ali vgrajene sisteme, te EdgeAI rešitve zagotavljajo temelje za naslednjo generacijo inteligentnih aplikacij, ki delujejo učinkovito in zasebno na robu.

Vsaka platforma ponuja edinstvene prednosti: Jetson Orin Nano za robno računalništvo s strojno pospešitvijo, ONNX Runtime GenAI za razvoj na več platformah, Azure EdgeAI za integracijo oblak-rob na ravni podjetja, Windows ML za aplikacije, ki so nativne za Windows, in Foundry Local za implementacije RAG, osredotočene na zasebnost. Skupaj predstavljajo celovit ekosistem za razvoj EdgeAI.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.