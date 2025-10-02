<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T14:50:08+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "sl"
}
-->
# AI orodje za Visual Studio Code - Vodnik za razvoj Edge AI

## Uvod

Dobrodošli v celovitem vodniku za uporabo AI orodja za Visual Studio Code pri razvoju Edge AI. Ker se umetna inteligenca premika od centraliziranega računalništva v oblaku k razpršenim napravam na robu, razvijalci potrebujejo zmogljiva, integrirana orodja, ki lahko obvladajo edinstvene izzive robne uporabe - od omejitev virov do zahtev po delovanju brez povezave.

AI orodje za Visual Studio Code zapolnjuje to vrzel z zagotavljanjem celotnega razvojnega okolja, posebej zasnovanega za gradnjo, testiranje in optimizacijo AI aplikacij, ki učinkovito delujejo na robnih napravah. Ne glede na to, ali razvijate za IoT senzorje, mobilne naprave, vgrajene sisteme ali robne strežnike, to orodje poenostavi celoten razvojni proces znotraj znanega okolja VS Code.

Ta vodnik vas bo popeljal skozi ključne koncepte, orodja in najboljše prakse za uporabo AI orodja v vaših Edge AI projektih, od začetne izbire modela do produkcijske uporabe.

## Pregled

AI orodje za Visual Studio Code je zmogljiva razširitev, ki poenostavi razvoj agentov in ustvarjanje AI aplikacij. Orodje ponuja celovite zmogljivosti za raziskovanje, ocenjevanje in uporabo AI modelov iz širokega nabora ponudnikov—vključno z Anthropic, OpenAI, GitHub, Google—hkrati pa podpira lokalno izvajanje modelov z uporabo ONNX in Ollama.

Kar AI orodje ločuje od drugih je njegov celovit pristop k celotnemu življenjskemu ciklu razvoja AI. Za razliko od tradicionalnih orodij za razvoj AI, ki se osredotočajo na posamezne vidike, AI orodje zagotavlja integrirano okolje, ki pokriva odkrivanje modelov, eksperimentiranje, razvoj agentov, ocenjevanje in uporabo—vse znotraj znanega okolja VS Code.

Platforma je posebej zasnovana za hitro prototipiranje in produkcijsko uporabo, z značilnostmi, kot so generiranje pozivov, hitri začetki, brezhibne integracije MCP (Model Context Protocol) orodij in obsežne zmogljivosti ocenjevanja. Za razvoj Edge AI to pomeni, da lahko učinkovito razvijate, testirate in optimizirate AI aplikacije za robne scenarije uporabe, hkrati pa ohranjate celoten razvojni proces znotraj VS Code.

## Cilji učenja

Do konca tega vodnika boste sposobni:

### Osnovne kompetence
- **Namestiti in konfigurirati** AI orodje za Visual Studio Code za delovne procese razvoja Edge AI
- **Navigirati in uporabljati** vmesnik AI orodja, vključno s katalogom modelov, igriščem in graditeljem agentov
- **Izbrati in oceniti** AI modele, primerne za robno uporabo, glede na zmogljivost in omejitve virov
- **Pretvoriti in optimizirati** modele z uporabo ONNX formata in tehnik kvantizacije za robne naprave

### Spretnosti razvoja Edge AI
- **Oblikovati in implementirati** Edge AI aplikacije z uporabo integriranega razvojnega okolja
- **Izvajati testiranje modelov** v robnih pogojih z uporabo lokalnega sklepanja in spremljanja virov
- **Ustvariti in prilagoditi** AI agente, optimizirane za robne scenarije uporabe
- **Oceniti zmogljivost modelov** z uporabo metrik, pomembnih za robno računalništvo (zakasnitev, poraba pomnilnika, natančnost)

### Optimizacija in uporaba
- **Uporabiti kvantizacijo in obrezovanje** za zmanjšanje velikosti modela ob ohranjanju sprejemljive zmogljivosti
- **Optimizirati modele** za specifične robne strojne platforme, vključno s CPU, GPU in NPU pospeševanjem
- **Uvesti najboljše prakse** za razvoj Edge AI, vključno z upravljanjem virov in strategijami za izpad
- **Pripraviti modele in aplikacije** za produkcijsko uporabo na robnih napravah

### Napredni koncepti Edge AI
- **Integrirati z robnimi AI ogrodji** vključno z ONNX Runtime, Windows ML in TensorFlow Lite
- **Implementirati večmodelne arhitekture** in scenarije federativnega učenja za robna okolja
- **Odpravljati pogoste težave Edge AI** vključno z omejitvami pomnilnika, hitrostjo sklepanja in združljivostjo strojne opreme
- **Oblikovati strategije spremljanja in beleženja** za Edge AI aplikacije v produkciji

### Praktična uporaba
- **Zgraditi celovite Edge AI rešitve** od izbire modela do uporabe
- **Demonstrirati usposobljenost** v robno specifičnih delovnih procesih razvoja in tehnikah optimizacije
- **Uporabiti naučene koncepte** v resničnih primerih uporabe Edge AI, vključno z IoT, mobilnimi in vgrajenimi aplikacijami
- **Oceniti in primerjati** različne strategije uporabe Edge AI ter njihove kompromise

## Ključne značilnosti za razvoj Edge AI

### 1. Katalog modelov in odkrivanje
- **Podpora več ponudnikom**: Brskajte in dostopajte do AI modelov iz Anthropic, OpenAI, GitHub, Google in drugih ponudnikov
- **Integracija lokalnih modelov**: Poenostavljeno odkrivanje ONNX in Ollama modelov za robno uporabo
- **GitHub modeli**: Neposredna integracija z gostovanjem modelov na GitHubu za poenostavljen dostop
- **Primerjava modelov**: Primerjajte modele med seboj, da najdete optimalno ravnovesje za omejitve robnih naprav

### 2. Interaktivno igrišče
- **Interaktivno testno okolje**: Hitro eksperimentiranje z zmogljivostmi modelov v nadzorovanem okolju
- **Podpora več modalnostim**: Testiranje z slikami, besedilom in drugimi vnosi, značilnimi za robne scenarije
- **Eksperimentiranje v realnem času**: Takojšen povratni odziv na odgovore modelov in zmogljivost
- **Optimizacija parametrov**: Fino nastavljanje parametrov modela za zahteve robne uporabe

### 3. Graditelj pozivov (agentov)
- **Generiranje naravnega jezika**: Ustvarjanje začetnih pozivov z uporabo opisov v naravnem jeziku
- **Iterativno izboljšanje**: Izboljšanje pozivov na podlagi odgovorov modelov in zmogljivosti
- **Razčlenitev nalog**: Razdelitev kompleksnih nalog z veriženjem pozivov in strukturiranimi izhodi
- **Podpora spremenljivkam**: Uporaba spremenljivk v pozivih za dinamično vedenje agentov
- **Generiranje produkcijske kode**: Ustvarjanje kode, pripravljene za produkcijo, za hitro razvijanje aplikacij

### 4. Masovno izvajanje in ocenjevanje
- **Testiranje več modelov**: Izvajanje več pozivov hkrati na izbranih modelih
- **Učinkovito testiranje na velikem obsegu**: Testiranje različnih vhodov in konfiguracij učinkovito
- **Prilagojeni testni primeri**: Izvajanje agentov s testnimi primeri za preverjanje funkcionalnosti
- **Primerjava zmogljivosti**: Primerjava rezultatov med različnimi modeli in konfiguracijami

### 5. Ocenjevanje modelov z nabori podatkov
- **Standardne metrike**: Testiranje AI modelov z vgrajenimi ocenjevalniki (F1 rezultat, ustreznost, podobnost, koherenca)
- **Prilagojeni ocenjevalniki**: Ustvarjanje lastnih metrik ocenjevanja za specifične primere uporabe
- **Integracija nabora podatkov**: Testiranje modelov proti obsežnim naborom podatkov
- **Merjenje zmogljivosti**: Kvantifikacija zmogljivosti modelov za odločitve o robni uporabi

### 6. Zmožnosti prilagajanja
- **Prilagoditev modelov**: Prilagoditev modelov za specifične primere uporabe in domene
- **Specializirana prilagoditev**: Prilagoditev modelov za specializirane zahteve in domene
- **Optimizacija za rob**: Fino nastavljanje modelov posebej za omejitve robne uporabe
- **Usposabljanje za specifične domene**: Ustvarjanje modelov, prilagojenih specifičnim robnim primerom uporabe

### 7. Integracija MCP orodij
- **Povezljivost z zunanjimi orodji**: Povezovanje agentov z zunanjimi orodji prek strežnikov Model Context Protocol
- **Dejanja v resničnem svetu**: Omogočanje agentom, da poizvedujejo podatkovne baze, dostopajo do API-jev ali izvajajo prilagojeno logiko
- **Obstoječi MCP strežniki**: Uporaba orodij iz ukaznih (stdio) ali HTTP (server-sent event) protokolov
- **Razvoj prilagojenih MCP**: Gradnja in priprava novih MCP strežnikov z testiranjem v graditelju agentov

### 8. Razvoj in testiranje agentov
- **Podpora klicanju funkcij**: Omogočanje agentom, da dinamično kličejo zunanje funkcije
- **Testiranje integracij v realnem času**: Testiranje integracij z izvajanjem v realnem času in uporabo orodij
- **Različice agentov**: Nadzor različic agentov z zmogljivostjo primerjanja rezultatov ocenjevanja
- **Odpravljanje napak in sledenje**: Lokalno sledenje in odpravljanje napak pri razvoju agentov

## Delovni proces razvoja Edge AI

### Faza 1: Odkrivanje in izbira modelov
1. **Raziskovanje kataloga modelov**: Uporabite katalog modelov za iskanje modelov, primernih za robno uporabo
2. **Primerjava zmogljivosti**: Ocenite modele glede na velikost, natančnost in hitrost sklepanja
3. **Lokalno testiranje**: Uporabite Ollama ali ONNX modele za lokalno testiranje pred robno uporabo
4. **Ocena zahtev virov**: Določite potrebe po pomnilniku in računalniški moči za ciljne robne naprave

### Faza 2: Optimizacija modelov
1. **Pretvorba v ONNX**: Pretvorite izbrane modele v ONNX format za združljivost z robom
2. **Uporaba kvantizacije**: Zmanjšajte velikost modela z INT8 ali INT4 kvantizacijo
3. **Optimizacija strojne opreme**: Optimizirajte za ciljno robno strojno opremo (ARM, x86, specializirani pospeševalniki)
4. **Validacija zmogljivosti**: Preverite, ali optimizirani modeli ohranjajo sprejemljivo natančnost

### Faza 3: Razvoj aplikacij
1. **Oblikovanje agentov**: Uporabite graditelja agentov za ustvarjanje AI agentov, optimiziranih za rob
2. **Inženiring pozivov**: Razvijte pozive, ki učinkovito delujejo z manjšimi robnimi modeli
3. **Testiranje integracij**: Testirajte agente v simuliranih robnih pogojih
4. **Generiranje kode**: Ustvarite produkcijsko kodo, optimizirano za robno uporabo

### Faza 4: Ocenjevanje in testiranje
1. **Masovno ocenjevanje**: Testirajte več konfiguracij za iskanje optimalnih robnih nastavitev
2. **Profiliranje zmogljivosti**: Analizirajte hitrost sklepanja, porabo pomnilnika in natančnost
3. **Simulacija robnih pogojev**: Testirajte v pogojih, podobnih ciljnemu robnemu okolju
4. **Testiranje obremenitve**: Ocenite zmogljivost pod različnimi pogoji obremenitve

### Faza 5: Priprava na uporabo
1. **Končna optimizacija**: Uporabite končne optimizacije na podlagi rezultatov testiranja
2. **Pakiranje za uporabo**: Zapakirajte modele in kodo za robno uporabo
3. **Dokumentacija**: Dokumentirajte zahteve za uporabo in konfiguracijo
4. **Priprava spremljanja**: Pripravite spremljanje in beleženje za robno uporabo

## Ciljna publika za razvoj Edge AI

### Razvijalci Edge AI
- Razvijalci aplikacij, ki gradijo naprave z AI na robu in IoT rešitve
- Razvijalci vgrajenih sistemov, ki vključujejo AI zmogljivosti v naprave z omejenimi viri
- Mobilni razvijalci, ki ustvarjajo AI aplikacije na napravi za pametne telefone in tablice

### Inženirji Edge AI
- AI inženirji, ki optimizirajo modele za robno uporabo in upravljajo sklepalne procese
- DevOps inženirji, ki uvajajo in upravljajo AI modele v razpršeni robni infrastrukturi
- Inženirji zmogljivosti, ki optimizirajo AI delovne obremenitve za omejitve robne strojne opreme

### Raziskovalci in izobraževalci
- Raziskovalci AI, ki razvijajo učinkovite modele in algoritme za robno računalništvo
- Izobraževalci, ki poučujejo koncepte Edge AI in demonstrirajo tehnike optimizacije
- Študenti, ki se učijo o izzivih in rešitvah pri uporabi Edge AI

## Primeri uporabe Edge AI

### Pametne IoT naprave
- **Prepoznavanje slik v realnem času**: Uporaba modelov računalniškega vida na IoT kamerah in senzorjih
- **Obdelava glasu**: Implementacija prepoznavanja govora in obdelave naravnega jezika na pametnih zvočnikih
- **Prediktivno vzdrževanje**: Uporaba modelov za zaznavanje anomalij na industrijskih robnih napravah
- **Okoljsko spremljanje**: Uporaba modelov za analizo podatkov senzorjev v okoljskih aplikacijah

### Mobilne in vgrajene aplikacije
- **Prevajanje na napravi**: Implementacija modelov za prevajanje jezika, ki delujejo brez povezave
- **Razširjena resničnost**: Uporaba modelov za prepoznavanje in sledenje objektov v realnem času za AR aplikacije
- **Spremljanje zdravja**: Uporaba modelov za analizo zdravja na nosljivih napravah in medicinski opremi
- **Avtonomni sistemi**: Implementacija modelov za odločanje za drone, robote in vozila

### Robna računalniška infrastruktura
- **Robni podatkovni centri**: Uporaba AI modelov v robnih podatkovnih centrih za aplikacije z nizko zakasnitvijo
- **Integracija CDN**: Integracija zmogljivosti AI obdelave v omrežja za dostavo vsebin
- **5G rob**: Uporaba robnega računalništva 5G za aplikacije, ki jih poganja AI
- **Fog računalništvo**: Implementacija AI obdelave v okoljih fog računalništva

## Namestitev in nastavitev

### Namestitev razširitve
Namestite razširitev AI orodja neposredno iz tržnice Visual Studio Code:

**ID razširitve**: `ms-windows-ai-studio.windows-ai-studio`

**Metode namestitve**:
1. **Tržnica VS Code**: Poiščite "AI Toolkit" v pogledu razširitev
2. **Ukazna vrstica**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Neposredna namestitev**: Prenesite z [tržnice VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Predpogoji za razvoj Edge AI
- **Visual Studio Code**: Priporočena najnovejša različica
- **Python okolje**: Python 3.8+ z zahtevanimi knjižnicami AI
- **ONNX Runtime** (neobvezno): Za sklepanja ONNX modelov
- **Ollama** (neobvezno): Za lokalno gostovanje modelov
- **Orodja za pospeševanje strojne opreme**: CUDA, OpenVINO ali pospeševalniki, specifični za platformo

### Začetna konfiguracija
1. **Aktivacija razširitve**: Odprite VS Code in preverite, ali se AI orodje pojavi v vrst
2. Ustvarite začetne pozive z uporabo opisov v naravnem jeziku  
3. Iterirajte in izboljšajte pozive na podlagi odzivov modela  
4. Integrirajte MCP orodja za izboljšane zmogljivosti agentov  

#### Korak 3: Testiranje in ocenjevanje  
1. Uporabite **Bulk Run** za testiranje več pozivov na izbranih modelih  
2. Zaženite agente s testnimi primeri za preverjanje funkcionalnosti  
3. Ocenite natančnost in zmogljivost z vgrajenimi ali prilagojenimi metričnimi orodji  
4. Primerjajte različne modele in konfiguracije  

#### Korak 4: Fina nastavitev in optimizacija  
1. Prilagodite modele za specifične robne primere uporabe  
2. Uporabite fino nastavitev, specifično za domeno  
3. Optimizirajte za omejitve pri robni uporabi  
4. Verzionirajte in primerjajte različne konfiguracije agentov  

#### Korak 5: Priprava na uvedbo  
1. Ustvarite produkcijsko pripravljeno kodo z Agent Builderjem  
2. Nastavite povezave MCP strežnika za produkcijsko uporabo  
3. Pripravite pakete za uvedbo na robnih napravah  
4. Konfigurirajte metrike za spremljanje in ocenjevanje  

## Najboljše prakse za razvoj Edge AI  

### Izbira modela  
- **Omejitve velikosti**: Izberite modele, ki ustrezajo pomnilniškim omejitvam ciljnih naprav  
- **Hitrost sklepanja**: Dajte prednost modelom s hitro sklepalno hitrostjo za aplikacije v realnem času  
- **Kompromisi pri natančnosti**: Uravnotežite natančnost modela z omejitvami virov  
- **Združljivost formatov**: Prednost dajte ONNX ali strojno optimiziranim formatom za robno uvedbo  

### Tehnike optimizacije  
- **Kvantizacija**: Uporabite kvantizacijo INT8 ali INT4 za zmanjšanje velikosti modela in izboljšanje hitrosti  
- **Obrezovanje**: Odstranite nepotrebne parametre modela za zmanjšanje računalniških zahtev  
- **Distilacija znanja**: Ustvarite manjše modele, ki ohranjajo zmogljivost večjih  
- **Strojna pospešitev**: Izkoristite NPUs, GPUs ali specializirane pospeševalnike, kadar so na voljo  

### Delovni tok razvoja  
- **Iterativno testiranje**: Pogosto testirajte v pogojih, podobnih robnim, med razvojem  
- **Spremljanje zmogljivosti**: Nenehno spremljajte porabo virov in hitrost sklepanja  
- **Nadzor verzij**: Spremljajte verzije modelov in nastavitve optimizacije  
- **Dokumentacija**: Dokumentirajte vse odločitve o optimizaciji in kompromise pri zmogljivosti  

### Upoštevanje pri uvedbi  
- **Spremljanje virov**: Spremljajte pomnilnik, CPU in porabo energije v produkciji  
- **Strategije za izpad**: Implementirajte mehanizme za izpad modela  
- **Mehanizmi za posodobitve**: Načrtujte posodobitve modelov in upravljanje verzij  
- **Varnost**: Implementirajte ustrezne varnostne ukrepe za aplikacije Edge AI  

## Integracija z Edge AI okviri  

### ONNX Runtime  
- **Uvedba na več platformah**: Uvedite ONNX modele na različnih robnih platformah  
- **Strojna optimizacija**: Izkoristite strojno specifične optimizacije ONNX Runtime  
- **Podpora za mobilne naprave**: Uporabite ONNX Runtime Mobile za aplikacije na pametnih telefonih in tablicah  
- **Integracija z IoT**: Uvedite na IoT napravah z uporabo lahkih distribucij ONNX Runtime  

### Windows ML  
- **Windows naprave**: Optimizirajte za robne naprave in računalnike na osnovi Windows  
- **Pospešitev z NPU**: Izkoristite nevronske procesne enote na Windows napravah  
- **DirectML**: Uporabite DirectML za pospešitev GPU na Windows platformah  
- **Integracija z UWP**: Integrirajte z aplikacijami Universal Windows Platform  

### TensorFlow Lite  
- **Optimizacija za mobilne naprave**: Uvedite TensorFlow Lite modele na mobilnih in vgrajenih napravah  
- **Strojni delegati**: Uporabite specializirane strojne delegate za pospešitev  
- **Mikrokrmilniki**: Uvedite na mikrokrmilnikih z uporabo TensorFlow Lite Micro  
- **Podpora na več platformah**: Uvedite na Android, iOS in vgrajenih Linux sistemih  

### Azure IoT Edge  
- **Hibrid oblak-rob**: Združite učenje v oblaku z sklepanjem na robu  
- **Uvedba modulov**: Uvedite AI modele kot IoT Edge module  
- **Upravljanje naprav**: Upravljajte robne naprave in posodobitve modelov na daljavo  
- **Telemetrija**: Zbirajte podatke o zmogljivosti in metrike modelov iz robnih uvedb  

## Napredni scenariji Edge AI  

### Uvedba več modelov  
- **Modelni ansambli**: Uvedite več modelov za izboljšano natančnost ali redundanco  
- **A/B testiranje**: Hkrati testirajte različne modele na robnih napravah  
- **Dinamična izbira**: Izberite modele glede na trenutne pogoje naprave  
- **Deljenje virov**: Optimizirajte uporabo virov med več uvedenimi modeli  

### Federativno učenje  
- **Porazdeljeno učenje**: Učite modele na več robnih napravah  
- **Ohranjanje zasebnosti**: Ohranite podatke za učenje lokalno, medtem ko delite izboljšave modela  
- **Sodelovalno učenje**: Omogočite napravam učenje iz kolektivnih izkušenj  
- **Koordinacija rob-oblak**: Koordinirajte učenje med robnimi napravami in infrastrukturo v oblaku  

### Procesiranje v realnem času  
- **Procesiranje tokov**: Procesirajte neprekinjene podatkovne tokove na robnih napravah  
- **Sklepanja z nizko zakasnitvijo**: Optimizirajte za minimalno zakasnitev sklepanja  
- **Procesiranje paketov**: Učinkovito procesirajte pakete podatkov na robnih napravah  
- **Prilagodljivo procesiranje**: Prilagodite procesiranje glede na trenutne zmogljivosti naprave  

## Odpravljanje težav pri razvoju Edge AI  

### Pogoste težave  
- **Omejitve pomnilnika**: Model je prevelik za pomnilnik ciljne naprave  
- **Hitrost sklepanja**: Sklepanje modela je prepočasno za zahteve v realnem času  
- **Poslabšanje natančnosti**: Optimizacija nesprejemljivo zmanjša natančnost modela  
- **Združljivost strojne opreme**: Model ni združljiv s ciljno strojno opremo  

### Strategije za odpravljanje napak  
- **Profiliranje zmogljivosti**: Uporabite funkcije sledenja AI Toolkit za identifikacijo ozkih grl  
- **Spremljanje virov**: Spremljajte pomnilnik in uporabo CPU med razvojem  
- **Postopno testiranje**: Testirajte optimizacije postopoma za izolacijo težav  
- **Simulacija strojne opreme**: Uporabite razvojna orodja za simulacijo ciljne strojne opreme  

### Rešitve za optimizacijo  
- **Dodatna kvantizacija**: Uporabite bolj agresivne tehnike kvantizacije  
- **Arhitektura modela**: Razmislite o različnih arhitekturah modelov, optimiziranih za rob  
- **Optimizacija predprocesiranja**: Optimizirajte predprocesiranje podatkov za robne omejitve  
- **Optimizacija sklepanja**: Uporabite strojno specifične optimizacije sklepanja  

## Viri in naslednji koraki  

### Uradna dokumentacija  
- [Dokumentacija za razvijalce AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Vodnik za namestitev in nastavitev](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentacija za inteligentne aplikacije VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentacija Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Skupnost in podpora  
- [GitHub repozitorij AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub težave in zahteve za funkcije](https://aka.ms/AIToolkit/feedback)  
- [Skupnost Azure AI Foundry na Discordu](https://aka.ms/azureaifoundry/discord)  
- [Tržnica razširitev VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tehnični viri  
- [Dokumentacija ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentacija Ollama](https://ollama.ai/)  
- [Dokumentacija Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentacija Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Učne poti  
- [Tečaj osnov Edge AI](../Module01/README.md)  
- [Vodnik za majhne jezikovne modele](../Module02/README.md)  
- [Strategije uvedbe na robu](../Module03/README.md)  
- [Razvoj Edge AI na Windows](./windowdeveloper.md)  

### Dodatni viri  
- **Statistika repozitorija**: 1.8k+ zvezdic, 150+ vilic, 18+ sodelavcev  
- **Licenca**: MIT licenca  
- **Varnost**: Veljajo Microsoftove varnostne politike  
- **Telemetrija**: Upošteva nastavitve telemetrije VS Code  

## Zaključek  

AI Toolkit za Visual Studio Code predstavlja celovito platformo za sodoben razvoj AI, ki ponuja poenostavljene zmogljivosti razvoja agentov, posebej dragocene za aplikacije Edge AI. S svojim obsežnim katalogom modelov, ki podpira ponudnike, kot so Anthropic, OpenAI, GitHub in Google, v kombinaciji z lokalnim izvajanjem prek ONNX in Ollama, orodje ponuja prilagodljivost, potrebno za raznolike scenarije uvedbe na robu.

Moč orodja je v integriranem pristopu—od odkrivanja modelov in eksperimentiranja v Playgroundu do sofisticiranega razvoja agentov z Prompt Builderjem, celovitih zmogljivosti ocenjevanja in brezhibne integracije MCP orodij. Za razvijalce Edge AI to pomeni hitro prototipiranje in testiranje AI agentov pred uvedbo na robu, z možnostjo hitrega iteriranja in optimizacije za okolja z omejenimi viri.

Ključne prednosti za razvoj Edge AI vključujejo:  
- **Hitro eksperimentiranje**: Hitro testiranje modelov in agentov pred uvedbo na robu  
- **Prilagodljivost več ponudnikov**: Dostop do modelov iz različnih virov za optimalne rešitve na robu  
- **Lokalni razvoj**: Testiranje z ONNX in Ollama za razvoj brez povezave in ohranjanje zasebnosti  
- **Pripravljenost na produkcijo**: Ustvarjanje produkcijsko pripravljene kode in integracija z zunanjimi orodji prek MCP  
- **Celovito ocenjevanje**: Uporaba vgrajenih in prilagojenih metrik za validacijo zmogljivosti Edge AI  

Ker AI še naprej napreduje proti scenarijem uvedbe na robu, AI Toolkit za VS Code zagotavlja razvojno okolje in delovni tok, potreben za gradnjo, testiranje in optimizacijo inteligentnih aplikacij za okolja z omejenimi viri. Ne glede na to, ali razvijate IoT rešitve, mobilne AI aplikacije ali vgrajene inteligentne sisteme, celovit nabor funkcij orodja in integriran delovni tok podpirata celoten življenjski cikel razvoja Edge AI.

Z nenehnim razvojem in aktivno skupnostjo (1.8k+ zvezdic na GitHubu) AI Toolkit ostaja v ospredju orodij za razvoj AI, ki se nenehno razvijajo, da bi zadovoljili potrebe sodobnih razvijalcev AI, ki gradijo za scenarije uvedbe na robu.

[Next Foundry Local](./foundrylocal.md)  

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.