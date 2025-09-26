<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:45:08+00:00",
  "source_file": "Module07/README.md",
  "language_code": "hr"
}
-->
# Poglavlje 07: EdgeAI Primjeri

Edge AI predstavlja spoj umjetne inteligencije i edge računalstva, omogućujući inteligentnu obradu izravno na uređajima bez oslanjanja na povezivost s oblakom. Ovo poglavlje istražuje pet različitih implementacija EdgeAI-a na različitim platformama i okvirima, pokazujući svestranost i snagu pokretanja AI modela na rubu mreže.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano predstavlja prekretnicu u pristupačnom edge AI računalstvu, pružajući do 67 TOPS AI performansi u kompaktnom formatu veličine kreditne kartice. Ova moćna Edge AI platforma demokratizira razvoj generativne AI za hobiste, studente i profesionalne programere.

### Ključne značajke
- Pruža do 67 TOPS AI performansi—1,7 puta bolje od svog prethodnika
- 1024 CUDA jezgre i do 32 Tensor jezgre za AI obradu
- 6-jezgreni Arm Cortex-A78AE v8.2 64-bitni CPU s maksimalnom frekvencijom od 1,5 GHz
- Cijena od samo 249 USD, čineći je najpristupačnijom platformom za programere, studente i entuzijaste

### Primjene
Jetson Orin Nano briljira u pokretanju modernih generativnih AI modela, uključujući vizijske transformatore, velike jezične modele i modele za viziju i jezik. Posebno je dizajniran za GenAI slučajeve upotrebe, a sada možete pokretati nekoliko LLM-ova na uređaju veličine dlana. Popularni slučajevi upotrebe uključuju AI-pokretane robote, pametne dronove, inteligentne kamere i autonomne edge uređaje.

**Saznajte više**: [NVIDIA-ov Jetson Orin Nano Superračunalo: Sljedeća velika stvar u EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI u mobilnim aplikacijama s .NET MAUI i ONNX Runtime GenAI

Ovo rješenje pokazuje kako integrirati Generativnu AI i Velike Jezične Modele (LLM-ove) u mobilne aplikacije koje rade na više platformi koristeći .NET MAUI (Multi-platform App UI) i ONNX Runtime GenAI. Ovaj pristup omogućuje .NET programerima izradu sofisticiranih AI-pokretanih mobilnih aplikacija koje rade nativno na Android i iOS uređajima.

### Ključne značajke
- Izgrađeno na .NET MAUI okviru, omogućujući jedinstvenu bazu koda za Android i iOS aplikacije
- Integracija ONNX Runtime GenAI omogućuje pokretanje generativnih AI modela izravno na mobilnim uređajima
- Podrška za različite hardverske akceleratore prilagođene mobilnim uređajima, uključujući CPU, GPU i specijalizirane mobilne AI procesore
- Optimizacije specifične za platformu poput CoreML za iOS i NNAPI za Android putem ONNX Runtime-a
- Implementira cijeli generativni AI ciklus uključujući predobradu i postobradu, inferenciju, obradu logita, pretraživanje i uzorkovanje te upravljanje KV predmemorijom

### Prednosti razvoja
Pristup putem .NET MAUI omogućuje programerima korištenje postojećih C# i .NET vještina dok izrađuju AI aplikacije za više platformi. ONNX Runtime GenAI okvir podržava više arhitektura modela, uključujući Llama, Mistral, Phi, Gemma i mnoge druge. Optimizirane ARM64 jezgre ubrzavaju INT4 kvantiziranu matricnu multiplikaciju, osiguravajući učinkovite performanse na mobilnom hardveru uz zadržavanje poznatog .NET iskustva razvoja.

### Slučajevi upotrebe
Ovo rješenje idealno je za programere koji žele izraditi AI-pokretane mobilne aplikacije koristeći .NET tehnologije, uključujući inteligentne chatbotove, aplikacije za prepoznavanje slika, alate za prevođenje jezika i personalizirane sustave preporuka koji rade potpuno na uređaju za poboljšanu privatnost i mogućnost rada izvan mreže.

**Saznajte više**: [.NET MAUI ONNX Runtime GenAI Primjer](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI u Azureu s motorom za male jezične modele

Microsoftovo Azure EdgeAI rješenje fokusira se na učinkovito implementiranje malih jezičnih modela (SLM-ova) u hibridnim okruženjima oblaka i edge-a. Ovaj pristup premošćuje jaz između AI usluga u oblaku i zahtjeva za implementaciju na rubu mreže.

### Prednosti arhitekture
- Besprijekorna integracija s Azure AI uslugama
- Pokretanje SLM-ova/LLM-ova i multimodalnih modela na uređaju i u oblaku putem ONNX Runtime-a
- Optimizirano za implementaciju na razini poduzeća
- Podrška za kontinuirana ažuriranja i upravljanje modelima

### Slučajevi upotrebe
Azure EdgeAI implementacija briljira u scenarijima koji zahtijevaju AI implementaciju na razini poduzeća s mogućnostima upravljanja u oblaku. To uključuje inteligentnu obradu dokumenata, analitiku u stvarnom vremenu i hibridne AI tijekove rada koji koriste resurse oblaka i edge-a.

**Saznajte više**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI s Windows ML](./windowdeveloper.md)

Windows ML predstavlja Microsoftov napredni runtime optimiziran za učinkovitu inferenciju modela na uređaju i pojednostavljenu implementaciju, služeći kao temelj Windows AI Foundryja. Ova platforma omogućuje programerima izradu AI-pokretanih Windows aplikacija koje koriste puni potencijal PC hardvera.

### Sposobnosti platforme
- Radi na svim Windows 11 računalima s verzijom 24H2 (build 26100) ili novijom
- Radi na svim x64 i ARM64 PC hardverima, čak i na računalima bez NPU-ova ili GPU-ova
- Omogućuje programerima da koriste vlastite modele i učinkovito ih implementiraju kroz ekosustav hardverskih partnera, uključujući AMD, Intel, NVIDIA i Qualcomm, na CPU, GPU i NPU
- Zahvaljujući infrastrukturnim API-jevima, programeri više ne moraju stvarati više verzija svojih aplikacija za različite hardverske platforme

### Prednosti za programere
Windows ML apstrahira hardver i pružatelje izvršenja, omogućujući vam da se fokusirate na pisanje koda. Osim toga, Windows ML se automatski ažurira kako bi podržao najnovije NPU-ove, GPU-ove i CPU-ove čim postanu dostupni. Platforma pruža jedinstveni okvir za AI razvoj na raznolikom Windows hardverskom ekosustavu.

**Saznajte više**: 
- [Pregled Windows ML-a](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Vodič za razvoj Windows EdgeAI-a](./windowdeveloper.md) - Sveobuhvatan vodič za razvoj Windows Edge AI-a

## [5. EdgeAI s Foundry Local aplikacijama](./foundrylocal.md)

Foundry Local omogućuje Windows i Mac programerima izradu Retrieval Augmented Generation (RAG) aplikacija koristeći lokalne resurse u .NET-u, kombinirajući lokalne jezične modele sa semantičkim pretraživanjem. Ovaj pristup pruža AI rješenja usmjerena na privatnost koja rade isključivo na lokalnoj infrastrukturi.

### Tehnička arhitektura
- Kombinira Phi jezični model, lokalne ugrađene podatke i Semantic Kernel za stvaranje RAG scenarija
- Koristi ugrađene podatke kao vektore (nizove) vrijednosti s pomičnim zarezom koji predstavljaju sadržaj i njegovo semantičko značenje
- Semantic Kernel djeluje kao glavni orkestrator, integrirajući Phi i pametne komponente za stvaranje besprijekorne RAG cjelokupne obrade
- Podrška za lokalne vektorske baze podataka, uključujući SQLite i Qdrant

### Prednosti implementacije
RAG, ili Retrieval Augmented Generation, jednostavno znači "pronađi neke podatke i uključi ih u upit". Ova lokalna implementacija osigurava privatnost podataka dok pruža inteligentne odgovore temeljene na prilagođenim bazama znanja. Pristup je posebno vrijedan za scenarije u poduzećima koji zahtijevaju suverenitet podataka i mogućnost rada izvan mreže.

**Saznajte više**: 
- [Foundry Local](./foundrylocal.md)
- [Primjeri Foundry Local RAG-a](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local pruža REST poslužitelj kompatibilan s OpenAI-jem, pokretan ONNX Runtime-om za pokretanje modela lokalno na Windowsu. Ispod je brzi, potvrđeni sažetak; za potpune detalje pogledajte službenu dokumentaciju.

- Početak rada: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI referenca: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Cijeli Windows vodič u ovom repozitoriju: [foundrylocal.md](./foundrylocal.md)

Instalirajte ili nadogradite na Windowsu (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Istražite CLI kategorije:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Pokrenite model i otkrijte dinamičku krajnju točku:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Brza REST provjera za popis modela (zamijenite PORT iz statusa):
```cmd
curl -s http://localhost:PORT/v1/models
```

Savjeti:
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Donosite vlastiti model (kompilacija): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Resursi za razvoj Windows EdgeAI-a

Za programere koji ciljaju Windows platformu, kreirali smo sveobuhvatan vodič koji pokriva cijeli Windows EdgeAI ekosustav. Ovaj resurs pruža detaljne informacije o Windows AI Foundryju, uključujući API-je, alate i najbolje prakse za razvoj EdgeAI-a na Windowsu.

### Windows AI Foundry platforma
Windows AI Foundry platforma pruža sveobuhvatan skup alata i API-ja posebno dizajniranih za razvoj Edge AI-a na Windows uređajima. To uključuje specijaliziranu podršku za NPU-akcelerirani hardver, integraciju Windows ML-a i tehnike optimizacije specifične za platformu.

**Sveobuhvatan vodič**: [Vodič za razvoj Windows EdgeAI-a](../windowdeveloper.md)

Ovaj vodič pokriva:
- Pregled i komponente Windows AI Foundry platforme
- Phi Silica API za učinkovitu inferenciju na NPU hardveru
- API-je za računalni vid za obradu slika i OCR
- Integraciju i optimizaciju Windows ML runtime-a
- Foundry Local CLI za lokalni razvoj i testiranje
- Strategije optimizacije hardvera za Windows uređaje
- Praktične primjere implementacije i najbolje prakse

### [AI alat za razvoj Edge AI-a](./aitoolkit.md)
Za programere koji koriste Visual Studio Code, AI Toolkit ekstenzija pruža sveobuhvatno razvojno okruženje posebno dizajnirano za izradu, testiranje i implementaciju Edge AI aplikacija. Ovaj alat pojednostavljuje cijeli tijek rada razvoja Edge AI-a unutar VS Code-a.

**Vodič za razvoj**: [AI alat za razvoj Edge AI-a](./aitoolkit.md)

Vodič za AI Toolkit pokriva:
- Otkrivanje i odabir modela za implementaciju na rubu mreže
- Lokalno testiranje i optimizacijski tijekovi rada
- Integraciju ONNX-a i Ollame za edge modele
- Tehnike konverzije i kvantizacije modela
- Razvoj agenata za edge scenarije
- Procjenu performansi i praćenje
- Pripremu za implementaciju i najbolje prakse

## Zaključak

Ovih pet EdgeAI implementacija demonstrira zrelost i raznolikost Edge AI rješenja dostupnih danas. Od uređaja s hardverskim ubrzanjem poput Jetson Orin Nano do softverskih okvira poput ONNX Runtime GenAI i Windows ML-a, programeri imaju neviđene mogućnosti za implementaciju inteligentnih aplikacija na rubu mreže.

Zajednička nit svih ovih platformi je demokratizacija AI mogućnosti, čineći sofisticirano strojno učenje dostupnim programerima različitih razina vještina i slučajeva upotrebe. Bilo da gradite mobilne aplikacije, desktop softver ili ugrađene sustave, ova EdgeAI rješenja pružaju temelj za sljedeću generaciju inteligentnih aplikacija koje rade učinkovito i privatno na rubu mreže.

Svaka platforma nudi jedinstvene prednosti: Jetson Orin Nano za hardverski ubrzano edge računalstvo, ONNX Runtime GenAI za razvoj mobilnih aplikacija na više platformi, Azure EdgeAI za integraciju oblaka i edge-a na razini poduzeća, Windows ML za nativne Windows aplikacije i Foundry Local za implementacije RAG-a usmjerene na privatnost. Zajedno, one predstavljaju sveobuhvatan ekosustav za razvoj EdgeAI-a.

---

