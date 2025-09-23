<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-19T02:11:30+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "sl"
}
-->
# AI Orodje za Visual Studio Code - Vodnik za razvoj Edge AI

## Uvod

Dobrodošli v celovitem vodniku za uporabo AI Orodja za Visual Studio Code pri razvoju Edge AI. Ko se umetna inteligenca premika od centraliziranega računalništva v oblaku k razpršenim napravam na robu, razvijalci potrebujejo zmogljiva, integrirana orodja, ki lahko obvladajo edinstvene izzive robne implementacije - od omejitev virov do zahtev po delovanju brez povezave.

AI Orodje za Visual Studio Code zapolnjuje to vrzel z zagotavljanjem celotnega razvojnega okolja, posebej zasnovanega za gradnjo, testiranje in optimizacijo AI aplikacij, ki učinkovito delujejo na robnih napravah. Ne glede na to, ali razvijate za IoT senzorje, mobilne naprave, vgrajene sisteme ali robne strežnike, to orodje poenostavi celoten razvojni proces znotraj znanega okolja VS Code.

Ta vodnik vas bo popeljal skozi ključne koncepte, orodja in najboljše prakse za uporabo AI Orodja v vaših Edge AI projektih, od začetne izbire modela do implementacije v produkcijo.

## Pregled

AI Orodje ponuja integrirano razvojno okolje za celoten življenjski cikel Edge AI aplikacij znotraj VS Code. Omogoča brezhibno integracijo s priljubljenimi AI modeli ponudnikov, kot so OpenAI, Anthropic, Google in GitHub, hkrati pa podpira lokalno implementacijo modelov prek ONNX in Ollama - ključne funkcionalnosti za Edge AI aplikacije, ki zahtevajo sklepanje na napravi.

Kar AI Orodje ločuje od drugih za razvoj Edge AI, je njegov poudarek na celotnem procesu robne implementacije. Za razliko od tradicionalnih AI razvojnih orodij, ki se primarno osredotočajo na implementacijo v oblaku, AI Orodje vključuje specializirane funkcije za optimizacijo modelov, testiranje v omejenih pogojih in ocenjevanje zmogljivosti, specifične za rob. Orodje razume, da razvoj Edge AI zahteva drugačne premisleke - manjše velikosti modelov, hitrejše čase sklepanja, sposobnost delovanja brez povezave in optimizacije, specifične za strojno opremo.

Platforma podpira več scenarijev implementacije, od preprostega sklepanja na napravi do kompleksnih večmodelnih robnih arhitektur. Ponuja orodja za pretvorbo modelov, kvantizacijo in optimizacijo, ki so bistvena za uspešno implementacijo na robu, hkrati pa ohranja produktivnost razvijalcev, po kateri je VS Code znan.

## Cilji učenja

Do konca tega vodnika boste sposobni:

### Osnovne kompetence
- **Namestiti in konfigurirati** AI Orodje za Visual Studio Code za delovne procese razvoja Edge AI
- **Navigirati in uporabljati** vmesnik AI Orodja, vključno s katalogom modelov, igriščem in graditeljem agentov
- **Izbrati in oceniti** AI modele, primerne za robno implementacijo, glede na zmogljivost in omejitve virov
- **Pretvoriti in optimizirati** modele z uporabo ONNX formata in tehnik kvantizacije za robne naprave

### Veščine razvoja Edge AI
- **Oblikovati in implementirati** Edge AI aplikacije z uporabo integriranega razvojnega okolja
- **Izvajati testiranje modelov** v pogojih, podobnih robnim, z lokalnim sklepanjem in spremljanjem virov
- **Ustvariti in prilagoditi** AI agente, optimizirane za scenarije robne implementacije
- **Oceniti zmogljivost modelov** z uporabo metrik, pomembnih za robno računalništvo (zakasnitev, poraba pomnilnika, natančnost)

### Optimizacija in implementacija
- **Uporabiti kvantizacijo in obrezovanje** za zmanjšanje velikosti modela ob ohranjanju sprejemljive zmogljivosti
- **Optimizirati modele** za specifične robne strojne platforme, vključno s pospeševanjem CPU, GPU in NPU
- **Uvesti najboljše prakse** za razvoj Edge AI, vključno z upravljanjem virov in strategijami za izpad
- **Pripraviti modele in aplikacije** za implementacijo v produkcijo na robnih napravah

### Napredni koncepti Edge AI
- **Integrirati z robnimi AI ogrodji**, vključno z ONNX Runtime, Windows ML in TensorFlow Lite
- **Implementirati večmodelne arhitekture** in scenarije federativnega učenja za robna okolja
- **Odpravljati pogoste težave Edge AI**, vključno z omejitvami pomnilnika, hitrostjo sklepanja in združljivostjo strojne opreme
- **Oblikovati strategije spremljanja in beleženja** za Edge AI aplikacije v produkciji

### Praktična uporaba
- **Zgraditi celovite Edge AI rešitve** od izbire modela do implementacije
- **Demonstrirati usposobljenost** v robno specifičnih razvojnih procesih in tehnikah optimizacije
- **Uporabiti naučene koncepte** v resničnih primerih uporabe Edge AI, vključno z IoT, mobilnimi in vgrajenimi aplikacijami
- **Oceniti in primerjati** različne strategije implementacije Edge AI ter njihove kompromise

## Ključne funkcije za razvoj Edge AI

### 1. Katalog modelov in odkrivanje
- **Podpora lokalnim modelom**: Odkrijte in dostopajte do AI modelov, posebej optimiziranih za robno implementacijo
- **Integracija ONNX**: Dostopajte do modelov v ONNX formatu za učinkovito sklepanje na robu
- **Podpora Ollama**: Uporabite lokalno delujoče modele prek Ollama za zasebnost in delovanje brez povezave
- **Primerjava modelov**: Primerjajte modele med seboj, da najdete optimalno ravnovesje med zmogljivostjo in porabo virov za robne naprave

### 2. Interaktivno igrišče
- **Lokalno testno okolje**: Testirajte modele lokalno pred robno implementacijo
- **Večmodalni eksperimenti**: Testirajte z slikami, besedilom in drugimi vnosi, značilnimi za robne scenarije
- **Prilagajanje parametrov**: Eksperimentirajte z različnimi parametri modela za optimizacijo glede na omejitve robov
- **Spremljanje zmogljivosti v realnem času**: Opazujte hitrost sklepanja in porabo virov med razvojem

### 3. Graditelj agentov za robne aplikacije
- **Oblikovanje pozivov**: Ustvarite optimizirane pozive, ki učinkovito delujejo z manjšimi robnimi modeli
- **Integracija MCP orodij**: Integrirajte orodja Model Context Protocol za izboljšane zmogljivosti robnih agentov
- **Generiranje kode**: Generirajte kodo, pripravljeno za produkcijo, optimizirano za scenarije robne implementacije
- **Strukturirani izhodi**: Oblikujte agente, ki zagotavljajo dosledne, strukturirane odgovore, primerne za robne aplikacije

### 4. Ocenjevanje in testiranje modelov
- **Metrične zmogljivosti**: Ocenjujte modele z uporabo metrik, pomembnih za robno implementacijo (zakasnitev, poraba pomnilnika, natančnost)
- **Testiranje v serijah**: Testirajte več konfiguracij modelov hkrati, da najdete optimalne nastavitve za rob
- **Prilagojeno ocenjevanje**: Ustvarite prilagojena merila ocenjevanja, specifična za primere uporabe Edge AI
- **Profiliranje virov**: Analizirajte zahteve po pomnilniku in računalniških zmogljivostih za načrtovanje robne implementacije

### 5. Pretvorba in optimizacija modelov
- **Pretvorba v ONNX**: Pretvorite modele iz različnih formatov v ONNX za združljivost z robom
- **Kvantizacija**: Zmanjšajte velikost modela in izboljšajte hitrost sklepanja s tehnikami kvantizacije
- **Optimizacija strojne opreme**: Optimizirajte modele za specifično robno strojno opremo (CPU, GPU, NPU)
- **Transformacija formatov**: Pretvorite modele iz Hugging Face in drugih virov za robno implementacijo

### 6. Fino prilagajanje za robne scenarije
- **Prilagoditev domeni**: Prilagodite modele za specifične primere uporabe in okolja na robu
- **Lokalno učenje**: Učite modele lokalno z GPU podporo za specifične zahteve robov
- **Integracija Azure**: Uporabite Azure Container Apps za fino prilagajanje v oblaku pred robno implementacijo
- **Prenosno učenje**: Prilagodite predhodno naučene modele za naloge in omejitve, specifične za rob

### 7. Spremljanje zmogljivosti in sledenje
- **Analiza zmogljivosti na robu**: Spremljajte zmogljivost modela v pogojih, podobnih robnim
- **Zbiranje sledi**: Zbirajte podrobne podatke o zmogljivosti za optimizacijo
- **Prepoznavanje ozkih grl**: Prepoznajte težave z zmogljivostjo pred implementacijo na robne naprave
- **Sledenje porabi virov**: Spremljajte pomnilnik, CPU in čas sklepanja za optimizacijo robov

## Delovni proces razvoja Edge AI

### Faza 1: Odkritje in izbira modela
1. **Raziskovanje kataloga modelov**: Uporabite katalog modelov za iskanje modelov, primernih za robno implementacijo
2. **Primerjava zmogljivosti**: Ocenite modele glede na velikost, natančnost in hitrost sklepanja
3. **Lokalno testiranje**: Uporabite Ollama ali ONNX modele za lokalno testiranje pred robno implementacijo
4. **Ocena zahtev po virih**: Določite potrebe po pomnilniku in računalniških zmogljivostih za ciljne robne naprave

### Faza 2: Optimizacija modela
1. **Pretvorba v ONNX**: Pretvorite izbrane modele v ONNX format za združljivost z robom
2. **Uporaba kvantizacije**: Zmanjšajte velikost modela z INT8 ali INT4 kvantizacijo
3. **Optimizacija strojne opreme**: Optimizirajte za ciljno robno strojno opremo (ARM, x86, specializirani pospeševalniki)
4. **Validacija zmogljivosti**: Validirajte, da optimizirani modeli ohranjajo sprejemljivo natančnost

### Faza 3: Razvoj aplikacije
1. **Oblikovanje agentov**: Uporabite graditelja agentov za ustvarjanje AI agentov, optimiziranih za rob
2. **Oblikovanje pozivov**: Razvijte pozive, ki učinkovito delujejo z manjšimi modeli
3. **Testiranje integracije**: Testirajte agente v simuliranih robnih pogojih
4. **Generiranje kode**: Generirajte produkcijsko kodo, optimizirano za robno implementacijo

### Faza 4: Ocenjevanje in testiranje
1. **Serijsko ocenjevanje**: Testirajte več konfiguracij za iskanje optimalnih nastavitev za rob
2. **Profiliranje zmogljivosti**: Analizirajte hitrost sklepanja, porabo pomnilnika in natančnost
3. **Simulacija robov**: Testirajte v pogojih, podobnih ciljnemu okolju robne implementacije
4. **Testiranje obremenitve**: Ocenite zmogljivost pod različnimi pogoji obremenitve

### Faza 5: Priprava na implementacijo
1. **Končna optimizacija**: Uporabite končne optimizacije na podlagi rezultatov testiranja
2. **Pakiranje za implementacijo**: Pakirajte modele in kodo za robno implementacijo
3. **Dokumentacija**: Dokumentirajte zahteve za implementacijo in konfiguracijo
4. **Priprava spremljanja**: Pripravite spremljanje in beleženje za produkcijsko implementacijo

## Ciljna publika za razvoj Edge AI

### Razvijalci Edge AI
- Razvijalci aplikacij, ki gradijo naprave na robu z AI pogonom in IoT rešitve
- Razvijalci vgrajenih sistemov, ki integrirajo AI zmogljivosti v naprave z omejenimi viri
- Mobilni razvijalci, ki ustvarjajo AI aplikacije na napravi za pametne telefone in tablice

### Inženirji Edge AI
- AI inženirji, ki optimizirajo modele za robno implementacijo in upravljajo sklepalne procese
- DevOps inženirji, ki implementirajo in upravljajo AI modele v razpršeni robni infrastrukturi
- Inženirji zmogljivosti, ki optimizirajo AI delovne obremenitve za omejitve robne strojne opreme

### Raziskovalci in izobraževalci
- AI raziskovalci, ki razvijajo učinkovite modele in algoritme za robno računalništvo
- Izobraževalci, ki poučujejo koncepte Edge AI in demonstrirajo tehnike optimizacije
- Študenti, ki se učijo o izzivih in rešitvah pri implementaciji Edge AI

## Primeri uporabe Edge AI

### Pametne IoT naprave
- **Prepoznavanje slik v realnem času**: Implementacija modelov računalniškega vida na IoT kamerah in senzorjih
- **Obdelava glasu**: Uporaba modelov za prepoznavanje govora in naravno jezikovno obdelavo na pametnih zvočnikih
- **Prediktivno vzdrževanje**: Zagon modelov za zaznavanje anomalij na industrijskih robnih napravah
- **Okoljsko spremljanje**: Implementacija modelov za analizo podatkov senzorjev za okoljske aplikacije

### Mobilne in vgrajene aplikacije
- **Prevajanje na napravi**: Implementacija modelov za prevajanje jezikov, ki delujejo brez povezave
- **Razširjena resničnost**: Implementacija prepoznavanja in sledenja objektov v realnem času za AR aplikacije
- **Spremljanje zdravja**: Zagon modelov za analizo zdravja na nosljivih napravah in medicinski opremi
- **Avtonomni sistemi**: Implementacija modelov za odločanje za drone, robote in vozila

### Infrastruktura robnega računalništva
- **Robni podatkovni centri**: Implementacija AI modelov v robnih podatkovnih centrih za aplikacije z nizko zakasnitvijo
- **Integracija CDN**: Integracija zmogljivosti AI obdelave v omrežja za dostavo vsebin
- **5G rob**: Uporaba 5G robnega računalništva za aplikacije z AI pogonom
- **Fog računalništvo**: Implementacija AI obdelave v okoljih fog računalništva

## Namestitev in nastavitev

### Hitra namestitev
Namestite razširitev AI Orodja neposredno iz Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Predpogoji za razvoj Edge AI
- **ONNX Runtime**: Namestite ONNX Runtime za sklepanje modelov
- **Ollama** (neobvezno): Namestite Ollama za lokalno strežbo modelov
- **Python okolje**: Nastavite Python z zahtevanimi AI knjižnicami
- **Orodja za robno strojno opremo**: Namestite razvojna orodja, specifična za strojno opremo (CUDA, OpenVINO itd.)

### Začetna konfiguracija
1. Odprite VS Code in namestite razširitev AI Orodja
2. Konfigurirajte vire modelov (ONNX, Ollama, ponudniki v oblaku)
3. Nastavite lokalno razvojno okolje za testiranje na robu
4. Konfigurirajte možnosti pospeševanja strojne opreme za vaš razvojni računalnik

## Začetek razvoja Edge AI

### Korak 1: Izbira modela
1. Odprite pogled AI Orodja v Activity Bar
2. Brskajte po katalogu modelov za modele, združljive z robom
3. Filtrirajte po velikosti modela, formatu (ONNX) in značilnostih zmogljivosti
4. Primerjajte modele z uporabo vgrajenih orodij za primerjavo

### Korak 2: Lokalno testiranje
1. Uporabite igrišče za lokalno testiranje izbranih modelov
2. Eksperimentirajte z različnimi pozivi in parametri
3. Spremljajte metrike zmogljivosti med testiranjem
4.
- **Varnost**: Uvedite ustrezne varnostne ukrepe za aplikacije Edge AI

## Integracija z Edge AI okviri

### ONNX Runtime
- **Navzkrižna platformska namestitev**: Namestite ONNX modele na različnih edge platformah
- **Optimizacija strojne opreme**: Izkoristite strojno specifične optimizacije ONNX Runtime
- **Podpora za mobilne naprave**: Uporabite ONNX Runtime Mobile za aplikacije na pametnih telefonih in tablicah
- **Integracija z IoT**: Namestite na IoT naprave z uporabo lahkih distribucij ONNX Runtime

### Windows ML
- **Windows naprave**: Optimizirajte za naprave in računalnike na osnovi Windows
- **Pospeševanje z NPU**: Izkoristite nevronske procesne enote na Windows napravah
- **DirectML**: Uporabite DirectML za pospeševanje GPU na Windows platformah
- **Integracija z UWP**: Integrirajte z aplikacijami Universal Windows Platform

### TensorFlow Lite
- **Optimizacija za mobilne naprave**: Namestite TensorFlow Lite modele na mobilne in vgrajene naprave
- **Strojni delegati**: Uporabite specializirane strojne delegate za pospeševanje
- **Mikrokrmilniki**: Namestite na mikrokrmilnike z uporabo TensorFlow Lite Micro
- **Podpora za več platform**: Namestite na Android, iOS in vgrajene Linux sisteme

### Azure IoT Edge
- **Hibrid oblak-edge**: Združite učenje v oblaku z inferenco na robu
- **Namestitev modulov**: Namestite AI modele kot IoT Edge module
- **Upravljanje naprav**: Oddaljeno upravljajte edge naprave in posodobitve modelov
- **Telemetrija**: Zbirajte podatke o zmogljivosti in metrike modelov iz edge namestitev

## Napredni scenariji Edge AI

### Namestitev več modelov
- **Modelni ansambli**: Namestite več modelov za izboljšano natančnost ali redundanco
- **A/B testiranje**: Hkrati testirajte različne modele na edge napravah
- **Dinamična izbira**: Izberite modele glede na trenutne pogoje naprave
- **Deljenje virov**: Optimizirajte uporabo virov med več nameščenimi modeli

### Federativno učenje
- **Porazdeljeno učenje**: Učite modele na več edge napravah
- **Ohranjanje zasebnosti**: Podatki za učenje ostanejo lokalni, medtem ko se delijo izboljšave modelov
- **Sodelovalno učenje**: Omogočite napravam učenje iz kolektivnih izkušenj
- **Koordinacija edge-oblak**: Koordinirajte učenje med edge napravami in infrastrukturo v oblaku

### Obdelava v realnem času
- **Obdelava tokov**: Obdelujte neprekinjene podatkovne tokove na edge napravah
- **Inferenca z nizko zakasnitvijo**: Optimizirajte za minimalno zakasnitev inferenc
- **Obdelava paketov**: Učinkovito obdelujte pakete podatkov na edge napravah
- **Prilagodljiva obdelava**: Prilagodite obdelavo glede na trenutne zmogljivosti naprave

## Odpravljanje težav pri razvoju Edge AI

### Pogoste težave
- **Omejitve pomnilnika**: Model je prevelik za pomnilnik ciljne naprave
- **Hitrost inferenc**: Inferenca modela je prepočasna za zahteve v realnem času
- **Poslabšanje natančnosti**: Optimizacija nesprejemljivo zmanjša natančnost modela
- **Združljivost strojne opreme**: Model ni združljiv s ciljno strojno opremo

### Strategije odpravljanja napak
- **Profiliranje zmogljivosti**: Uporabite funkcije sledenja AI Toolkit za identifikacijo ozkih grl
- **Spremljanje virov**: Spremljajte uporabo pomnilnika in CPU med razvojem
- **Postopno testiranje**: Testirajte optimizacije postopoma, da izolirate težave
- **Simulacija strojne opreme**: Uporabite razvojna orodja za simulacijo ciljne strojne opreme

### Rešitve za optimizacijo
- **Dodatna kvantizacija**: Uporabite bolj agresivne tehnike kvantizacije
- **Arhitektura modela**: Razmislite o različnih arhitekturah modelov, optimiziranih za edge
- **Optimizacija predobdelave**: Optimizirajte predobdelavo podatkov za omejitve na robu
- **Optimizacija inferenc**: Uporabite strojno specifične optimizacije inferenc

## Viri in naslednji koraki

### Dokumentacija
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Skupnost in podpora
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Učni viri
- [Osnove Edge AI tečaja](./Module01/README.md)
- [Vodnik za majhne jezikovne modele](./Module02/README.md)
- [Strategije namestitve na robu](./Module03/README.md)
- [Razvoj Edge AI na Windows](./windowdeveloper.md)

## Zaključek

AI Toolkit za Visual Studio Code ponuja celovito platformo za razvoj Edge AI, od odkrivanja in optimizacije modelov do namestitve in spremljanja. Z uporabo integriranih orodij in delovnih tokov lahko razvijalci učinkovito ustvarjajo, testirajo in nameščajo AI aplikacije, ki učinkovito delujejo na napravah z omejenimi viri.

Podpora orodja za ONNX, Ollama in različne ponudnike oblakov, skupaj z zmogljivostmi za optimizacijo in ocenjevanje, ga naredi idealno izbiro za razvoj Edge AI. Ne glede na to, ali gradite IoT aplikacije, funkcije mobilne AI ali vgrajene inteligentne sisteme, AI Toolkit ponuja orodja in delovne tokove, potrebne za uspešno namestitev Edge AI.

Ker se Edge AI še naprej razvija, AI Toolkit za VS Code ostaja v ospredju, razvijalcem pa zagotavlja najsodobnejša orodja in zmogljivosti za gradnjo naslednje generacije inteligentnih aplikacij na robu.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.