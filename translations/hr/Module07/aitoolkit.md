<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-19T02:09:28+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "hr"
}
-->
# AI Toolkit za Visual Studio Code - Vodič za razvoj Edge AI-a

## Uvod

Dobrodošli u sveobuhvatan vodič za korištenje AI Toolkit-a za Visual Studio Code u razvoju Edge AI-a. Kako umjetna inteligencija prelazi s centraliziranog računalstva u oblaku na distribuirane uređaje na rubu mreže, programerima su potrebni moćni, integrirani alati koji mogu odgovoriti na jedinstvene izazove implementacije na rubu - od ograničenja resursa do zahtjeva za rad u offline načinu.

AI Toolkit za Visual Studio Code premošćuje ovaj jaz pružajući cjelovito razvojno okruženje posebno dizajnirano za izradu, testiranje i optimizaciju AI aplikacija koje učinkovito rade na uređajima na rubu mreže. Bez obzira razvijate li za IoT senzore, mobilne uređaje, ugrađene sustave ili edge servere, ovaj alat pojednostavljuje cijeli vaš razvojni proces unutar poznatog okruženja VS Code-a.

Ovaj vodič će vas provesti kroz ključne koncepte, alate i najbolje prakse za korištenje AI Toolkit-a u vašim Edge AI projektima, od početnog odabira modela do implementacije u produkciju.

## Pregled

AI Toolkit pruža integrirano razvojno okruženje za cijeli životni ciklus Edge AI aplikacija unutar VS Code-a. Nudi besprijekornu integraciju s popularnim AI modelima od pružatelja poput OpenAI, Anthropic, Google i GitHub, uz podršku za lokalnu implementaciju modela putem ONNX-a i Ollame - ključne funkcionalnosti za Edge AI aplikacije koje zahtijevaju inferenciju na uređaju.

Ono što AI Toolkit čini posebnim za razvoj Edge AI-a je fokus na cijeli proces implementacije na rubu mreže. Za razliku od tradicionalnih AI alata koji prvenstveno ciljaju implementaciju u oblaku, AI Toolkit uključuje specijalizirane značajke za optimizaciju modela, testiranje u uvjetima ograničenih resursa i evaluaciju performansi specifičnih za rub mreže. Alat razumije da razvoj Edge AI-a zahtijeva drugačije pristupe - manje veličine modela, brže vrijeme inferencije, mogućnost rada offline i optimizacije specifične za hardver.

Platforma podržava različite scenarije implementacije, od jednostavne inferencije na uređaju do složenih arhitektura s više modela na rubu mreže. Pruža alate za konverziju modela, kvantizaciju i optimizaciju koji su ključni za uspješnu implementaciju na rubu, uz održavanje produktivnosti programera po kojoj je VS Code poznat.

## Ciljevi učenja

Na kraju ovog vodiča, moći ćete:

### Osnovne vještine
- **Instalirati i konfigurirati** AI Toolkit za Visual Studio Code za razvojne procese Edge AI-a
- **Navigirati i koristiti** sučelje AI Toolkit-a, uključujući Model Catalog, Playground i Agent Builder
- **Odabrati i evaluirati** AI modele prikladne za implementaciju na rubu mreže na temelju performansi i ograničenja resursa
- **Konvertirati i optimizirati** modele koristeći ONNX format i tehnike kvantizacije za uređaje na rubu mreže

### Vještine razvoja Edge AI-a
- **Dizajnirati i implementirati** Edge AI aplikacije koristeći integrirano razvojno okruženje
- **Testirati modele** u uvjetima sličnim rubu mreže koristeći lokalnu inferenciju i praćenje resursa
- **Kreirati i prilagoditi** AI agente optimizirane za scenarije implementacije na rubu mreže
- **Evaluirati performanse modela** koristeći metrike relevantne za rubno računalstvo (latencija, potrošnja memorije, točnost)

### Optimizacija i implementacija
- **Primijeniti kvantizaciju i obrezivanje** za smanjenje veličine modela uz održavanje prihvatljivih performansi
- **Optimizirati modele** za specifične hardverske platforme na rubu mreže, uključujući CPU, GPU i NPU akceleraciju
- **Primijeniti najbolje prakse** za razvoj Edge AI-a, uključujući upravljanje resursima i strategije za povratne mehanizme
- **Pripremiti modele i aplikacije** za implementaciju u produkciju na uređajima na rubu mreže

### Napredni koncepti Edge AI-a
- **Integrirati s Edge AI okvirima** uključujući ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementirati arhitekture s više modela** i scenarije federativnog učenja za rubne okruženja
- **Rješavati uobičajene probleme Edge AI-a** uključujući ograničenja memorije, brzinu inferencije i kompatibilnost hardvera
- **Dizajnirati strategije praćenja i zapisivanja** za Edge AI aplikacije u produkciji

### Praktična primjena
- **Izgraditi cjelovita Edge AI rješenja** od odabira modela do implementacije
- **Pokazati stručnost** u razvojnim procesima specifičnim za rub mreže i tehnikama optimizacije
- **Primijeniti naučene koncepte** na stvarne Edge AI slučajeve, uključujući IoT, mobilne i ugrađene aplikacije
- **Evaluirati i usporediti** različite strategije implementacije Edge AI-a i njihove kompromise

## Ključne značajke za razvoj Edge AI-a

### 1. Katalog modela i otkrivanje
- **Podrška za lokalne modele**: Pronađite i pristupite AI modelima posebno optimiziranim za implementaciju na rubu mreže
- **Integracija s ONNX-om**: Pristupite modelima u ONNX formatu za učinkovitu inferenciju na rubu mreže
- **Podrška za Ollamu**: Iskoristite modele koji rade lokalno putem Ollame za privatnost i rad u offline načinu
- **Usporedba modela**: Usporedite modele kako biste pronašli optimalnu ravnotežu između performansi i potrošnje resursa za uređaje na rubu mreže

### 2. Interaktivni Playground
- **Lokalno testno okruženje**: Testirajte modele lokalno prije implementacije na rubu mreže
- **Eksperimentiranje s više modaliteta**: Testirajte slike, tekst i druge ulazne podatke tipične za scenarije na rubu mreže
- **Podešavanje parametara**: Eksperimentirajte s različitim parametrima modela kako biste optimizirali za ograničenja na rubu mreže
- **Praćenje performansi u stvarnom vremenu**: Promatrajte brzinu inferencije i potrošnju resursa tijekom razvoja

### 3. Agent Builder za aplikacije na rubu mreže
- **Inženjering upita**: Kreirajte optimizirane upite koji učinkovito rade s manjim modelima na rubu mreže
- **Integracija MCP alata**: Integrirajte alate Model Context Protocol za poboljšane mogućnosti agenata na rubu mreže
- **Generiranje koda**: Generirajte kod spreman za produkciju optimiziran za scenarije implementacije na rubu mreže
- **Strukturirani izlazi**: Dizajnirajte agente koji pružaju dosljedne, strukturirane odgovore prikladne za aplikacije na rubu mreže

### 4. Evaluacija i testiranje modela
- **Metrike performansi**: Evaluirajte modele koristeći metrike relevantne za implementaciju na rubu mreže (latencija, potrošnja memorije, točnost)
- **Batch testiranje**: Testirajte više konfiguracija modela istovremeno kako biste pronašli optimalne postavke za rub mreže
- **Prilagođena evaluacija**: Kreirajte prilagođene kriterije evaluacije specifične za slučajeve Edge AI-a
- **Profiliranje resursa**: Analizirajte zahtjeve za memorijom i računalnim resursima za planiranje implementacije na rubu mreže

### 5. Konverzija i optimizacija modela
- **Konverzija u ONNX**: Konvertirajte modele iz različitih formata u ONNX za kompatibilnost s rubom mreže
- **Kvantizacija**: Smanjite veličinu modela i poboljšajte brzinu inferencije pomoću tehnika kvantizacije
- **Optimizacija hardvera**: Optimizirajte modele za specifični hardver na rubu mreže (CPU, GPU, NPU)
- **Transformacija formata**: Transformirajte modele iz Hugging Face-a i drugih izvora za implementaciju na rubu mreže

### 6. Fino podešavanje za scenarije na rubu mreže
- **Prilagodba domeni**: Prilagodite modele za specifične slučajeve i okruženja na rubu mreže
- **Lokalno treniranje**: Trenirajte modele lokalno uz podršku za GPU za zahtjeve specifične za rub mreže
- **Integracija s Azure-om**: Iskoristite Azure Container Apps za fino podešavanje u oblaku prije implementacije na rubu mreže
- **Transferno učenje**: Prilagodite unaprijed trenirane modele za zadatke i ograničenja specifična za rub mreže

### 7. Praćenje performansi i praćenje tragova
- **Analiza performansi na rubu mreže**: Pratite performanse modela u uvjetima sličnim rubu mreže
- **Prikupljanje tragova**: Prikupljajte detaljne podatke o performansama za optimizaciju
- **Identifikacija uskih grla**: Identificirajte probleme s performansama prije implementacije na uređaje na rubu mreže
- **Praćenje potrošnje resursa**: Pratite memoriju, CPU i vrijeme inferencije za optimizaciju na rubu mreže

## Radni proces razvoja Edge AI-a

### Faza 1: Otkrivanje i odabir modela
1. **Istražite katalog modela**: Koristite katalog modela za pronalaženje modela prikladnih za implementaciju na rubu mreže
2. **Usporedite performanse**: Evaluirajte modele na temelju veličine, točnosti i brzine inferencije
3. **Testirajte lokalno**: Koristite Ollama ili ONNX modele za lokalno testiranje prije implementacije na rubu mreže
4. **Procijenite zahtjeve za resursima**: Odredite potrebe za memorijom i računalnim resursima za ciljne uređaje na rubu mreže

### Faza 2: Optimizacija modela
1. **Konvertirajte u ONNX**: Konvertirajte odabrane modele u ONNX format za kompatibilnost s rubom mreže
2. **Primijenite kvantizaciju**: Smanjite veličinu modela pomoću kvantizacije INT8 ili INT4
3. **Optimizacija hardvera**: Optimizirajte za ciljni hardver na rubu mreže (ARM, x86, specijalizirani akceleratori)
4. **Validacija performansi**: Validirajte optimizirane modele kako bi zadržali prihvatljivu točnost

### Faza 3: Razvoj aplikacija
1. **Dizajn agenata**: Koristite Agent Builder za kreiranje AI agenata optimiziranih za rub mreže
2. **Inženjering upita**: Razvijte upite koji učinkovito rade s manjim modelima na rubu mreže
3. **Testiranje integracije**: Testirajte agente u simuliranim uvjetima na rubu mreže
4. **Generiranje koda**: Generirajte produkcijski kod optimiziran za implementaciju na rubu mreže

### Faza 4: Evaluacija i testiranje
1. **Batch evaluacija**: Testirajte više konfiguracija kako biste pronašli optimalne postavke za rub mreže
2. **Profiliranje performansi**: Analizirajte brzinu inferencije, potrošnju memorije i točnost
3. **Simulacija na rubu mreže**: Testirajte u uvjetima sličnim ciljnim okruženjima na rubu mreže
4. **Testiranje opterećenja**: Evaluirajte performanse pod različitim uvjetima opterećenja

### Faza 5: Priprema za implementaciju
1. **Završna optimizacija**: Primijenite završne optimizacije na temelju rezultata testiranja
2. **Pakiranje za implementaciju**: Pakirajte modele i kod za implementaciju na rubu mreže
3. **Dokumentacija**: Dokumentirajte zahtjeve za implementaciju i konfiguraciju
4. **Postavljanje praćenja**: Pripremite praćenje i zapisivanje za implementaciju u produkciji

## Ciljna publika za razvoj Edge AI-a

### Razvojni programeri Edge AI-a
- Programeri aplikacija koji izrađuju uređaje na rubu mreže i IoT rješenja s AI funkcionalnostima
- Programeri ugrađenih sustava koji integriraju AI mogućnosti u uređaje s ograničenim resursima
- Mobilni programeri koji izrađuju AI aplikacije za pametne telefone i tablete

### Inženjeri Edge AI-a
- AI inženjeri koji optimiziraju modele za implementaciju na rubu mreže i upravljaju inferencijskim procesima
- DevOps inženjeri koji implementiraju i upravljaju AI modelima na distribuiranoj infrastrukturi na rubu mreže
- Inženjeri performansi koji optimiziraju AI radne procese za ograničenja hardvera na rubu mreže

### Istraživači i edukatori
- Istraživači AI-a koji razvijaju učinkovite modele i algoritme za rubno računalstvo
- Edukatori koji podučavaju koncepte Edge AI-a i demonstriraju tehnike optimizacije
- Studenti koji uče o izazovima i rješenjima u implementaciji Edge AI-a

## Slučajevi korištenja Edge AI-a

### Pametni IoT uređaji
- **Prepoznavanje slika u stvarnom vremenu**: Implementacija modela računalnog vida na IoT kamerama i senzorima
- **Obrada glasa**: Primjena modela za prepoznavanje govora i obradu prirodnog jezika na pametnim zvučnicima
- **Prediktivno održavanje**: Pokretanje modela za otkrivanje anomalija na industrijskim uređajima na rubu mreže
- **Praćenje okoliša**: Implementacija modela za analizu podataka senzora u aplikacijama za praćenje okoliša

### Mobilne i ugrađene aplikacije
- **Prevođenje na uređaju**: Implementacija modela za prevođenje jezika koji rade offline
- **Proširena stvarnost**: Implementacija prepoznavanja i praćenja objekata u stvarnom vremenu za AR aplikacije
- **Praćenje zdravlja**: Pokretanje modela za analizu zdravlja na nosivim uređajima i medicinskoj opremi
- **Autonomni sustavi**: Implementacija modela za donošenje odluka za dronove, robote i vozila

### Infrastruktura za rubno računalstvo
- **Edge podatkovni centri**: Implementacija AI modela u podatkovnim centrima na rubu mreže za aplikacije s niskom latencijom
- **Integracija s CDN-om**: Integracija AI mogućnosti obrade u mreže za isporuku sadržaja
- **5G rub mreže**: Iskoristite 5G rubno računalstvo za aplikacije s AI funkcionalnostima
- **Fog računalstvo**: Implementacija AI obrade u okruženjima za fog računalstvo

## Instalacija i postavljanje

### Brza instalacija
Instalirajte AI Toolkit ekstenziju direktno iz Visual Studio Code Marketplace-a:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Preduvjeti za razvoj Edge AI-a
- **ONNX Runtime**: Instalirajte ONNX Runtime za inferenciju modela
- **Ollama** (opcionalno): Instalirajte Ollama za lokalno posluživanje modela
- **Python okruženje**: Postavite Python s potrebnim AI bibliotekama
- **Alati za hardver na rubu mreže**: Instalirajte alate za razvoj specifične za hardver (CUDA, OpenVINO, itd.)

### Početna konfiguracija
1. Otvorite VS Code i instalirajte AI Toolkit ekstenziju
2. Konfigurirajte izvore modela (ONNX, Ollama, pružatelji u oblaku)
3. Postavite lokalno razvojno okruženje za testiranje na rubu mreže
4. Konfigurirajte opcije hardverske akceleracije za vaš razvojni stroj

## Početak razvoja Edge AI-a

### Korak 1: Odabir modela
1. Otvorite prikaz AI Toolkit-a u Activity Baru
2. Pregledajte katalog modela za modele kompatibilne s rubom mreže
3. Filtrirajte prema veličini modela, formatu (ONNX) i karakteristikama performansi
4. Usporedite modele koristeći ugrađene alate za usporedbu

### Korak 2: Lokalno testiranje
1. Koristite Playground za testiranje odabranih modela lokalno
2. Eksperimentirajte s različitim upitima i parametrima
3. Pratite metrike performansi tijekom testiranja
4. Evaluirajte odgovore modela za zahtjeve slučajeva korištenja na rubu mre
- **Sigurnost**: Implementirajte odgovarajuće sigurnosne mjere za Edge AI aplikacije

## Integracija s Edge AI okvirima

### ONNX Runtime
- **Međuplatformsko postavljanje**: Postavite ONNX modele na različite edge platforme
- **Optimizacija hardvera**: Iskoristite hardverske optimizacije ONNX Runtime-a
- **Podrška za mobilne uređaje**: Koristite ONNX Runtime Mobile za aplikacije na pametnim telefonima i tabletima
- **Integracija s IoT-om**: Postavite na IoT uređaje koristeći lagane distribucije ONNX Runtime-a

### Windows ML
- **Windows uređaji**: Optimizirajte za edge uređaje i računala temeljena na Windowsu
- **Akceleracija NPU-a**: Iskoristite Neural Processing Units na Windows uređajima
- **DirectML**: Koristite DirectML za GPU akceleraciju na Windows platformama
- **Integracija s UWP-om**: Integrirajte s aplikacijama Universal Windows Platform

### TensorFlow Lite
- **Optimizacija za mobilne uređaje**: Postavite TensorFlow Lite modele na mobilne i ugrađene uređaje
- **Hardverski delegati**: Koristite specijalizirane hardverske delegate za ubrzanje
- **Mikrokontroleri**: Postavite na mikrokontrolere koristeći TensorFlow Lite Micro
- **Međuplatformska podrška**: Postavite na Android, iOS i ugrađene Linux sustave

### Azure IoT Edge
- **Hibrid oblak-edge**: Kombinirajte obuku u oblaku s inferencijom na edge uređajima
- **Postavljanje modula**: Postavite AI modele kao IoT Edge module
- **Upravljanje uređajima**: Daljinski upravljajte edge uređajima i ažuriranjima modela
- **Telemetrija**: Prikupljajte podatke o performansama i metrike modela s edge postavljanja

## Napredni scenariji za Edge AI

### Postavljanje više modela
- **Modelni ansambli**: Postavite više modela za poboljšanu točnost ili redundanciju
- **A/B testiranje**: Istovremeno testirajte različite modele na edge uređajima
- **Dinamički odabir**: Birajte modele na temelju trenutnih uvjeta uređaja
- **Dijeljenje resursa**: Optimizirajte korištenje resursa među više postavljenih modela

### Federativno učenje
- **Distribuirana obuka**: Obučavajte modele na više edge uređaja
- **Očuvanje privatnosti**: Zadržite podatke za obuku lokalno dok dijelite poboljšanja modela
- **Suradničko učenje**: Omogućite uređajima da uče iz kolektivnih iskustava
- **Koordinacija edge-oblaka**: Koordinirajte učenje između edge uređaja i infrastrukture oblaka

### Obrada u stvarnom vremenu
- **Obrada tokova**: Obradite kontinuirane tokove podataka na edge uređajima
- **Inferencija s niskom latencijom**: Optimizirajte za minimalnu latenciju inferencije
- **Obrada u serijama**: Učinkovito obradite serije podataka na edge uređajima
- **Adaptivna obrada**: Prilagodite obradu na temelju trenutnih mogućnosti uređaja

## Rješavanje problema u razvoju Edge AI-a

### Uobičajeni problemi
- **Ograničenja memorije**: Model je prevelik za memoriju ciljanog uređaja
- **Brzina inferencije**: Inferencija modela je prespora za zahtjeve u stvarnom vremenu
- **Degradacija točnosti**: Optimizacija neprihvatljivo smanjuje točnost modela
- **Kompatibilnost hardvera**: Model nije kompatibilan s ciljanom hardverskom opremom

### Strategije za otklanjanje grešaka
- **Profiliranje performansi**: Koristite značajke praćenja AI Toolkit-a za identifikaciju uskih grla
- **Praćenje resursa**: Pratite korištenje memorije i CPU-a tijekom razvoja
- **Postupno testiranje**: Testirajte optimizacije postupno kako biste izolirali probleme
- **Simulacija hardvera**: Koristite alate za razvoj kako biste simulirali ciljani hardver

### Rješenja za optimizaciju
- **Daljnja kvantizacija**: Primijenite agresivnije tehnike kvantizacije
- **Arhitektura modela**: Razmotrite različite arhitekture modela optimizirane za edge
- **Optimizacija predobrade**: Optimizirajte predobradu podataka za ograničenja edge uređaja
- **Optimizacija inferencije**: Koristite hardverski specifične optimizacije inferencije

## Resursi i sljedeći koraci

### Dokumentacija
- [Vodič za modele AI Toolkit-a](https://code.visualstudio.com/docs/intelligentapps/models)
- [Dokumentacija Model Playground-a](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Dokumentacija ONNX Runtime-a](https://onnxruntime.ai/)
- [Dokumentacija Windows ML-a](https://docs.microsoft.com/en-us/windows/ai/)

### Zajednica i podrška
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX zajednica](https://github.com/onnx/onnx)
- [Zajednica Edge AI developera](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Resursi za učenje
- [Osnove Edge AI-a](./Module01/README.md)
- [Vodič za male jezične modele](./Module02/README.md)
- [Strategije postavljanja na edge](./Module03/README.md)
- [Razvoj Edge AI-a na Windowsu](./windowdeveloper.md)

## Zaključak

AI Toolkit za Visual Studio Code pruža sveobuhvatnu platformu za razvoj Edge AI-a, od otkrivanja i optimizacije modela do postavljanja i praćenja. Iskorištavanjem integriranih alata i radnih tijekova, developeri mogu učinkovito kreirati, testirati i postavljati AI aplikacije koje učinkovito rade na uređajima s ograničenim resursima.

Podrška alata za ONNX, Ollama i razne pružatelje usluga u oblaku, u kombinaciji s njegovim mogućnostima optimizacije i evaluacije, čini ga idealnim izborom za razvoj Edge AI-a. Bez obzira razvijate li IoT aplikacije, AI značajke za mobilne uređaje ili ugrađene inteligentne sustave, AI Toolkit pruža alate i radne tijekove potrebne za uspješno postavljanje Edge AI-a.

Kako Edge AI nastavlja evoluirati, AI Toolkit za VS Code ostaje na čelu, pružajući developerima najnovije alate i mogućnosti za izgradnju sljedeće generacije inteligentnih edge aplikacija.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.