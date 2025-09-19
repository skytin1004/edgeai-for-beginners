<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ec2b092ed161fd4d3907e010f8cf544",
  "translation_date": "2025-09-19T01:57:42+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "sl"
}
-->
# Vodnik za razvoj Windows Edge AI

## Uvod

Dobrodošli v Windows Edge AI Development - vašem celovitem vodniku za gradnjo inteligentnih aplikacij, ki izkoriščajo moč umetne inteligence na napravi z uporabo platforme Windows AI Foundry podjetja Microsoft. Ta vodnik je posebej zasnovan za razvijalce Windows, ki želijo v svoje aplikacije vključiti najnovejše zmogljivosti Edge AI in hkrati izkoristiti celoten spekter strojne pospešitve Windows.

### Prednosti Windows AI

Windows AI Foundry predstavlja enotno, zanesljivo in varno platformo, ki podpira celoten življenjski cikel razvijalca AI - od izbire in prilagajanja modelov do optimizacije in uvajanja na CPU, GPU, NPU in hibridne oblačne arhitekture. Ta platforma demokratizira razvoj AI z zagotavljanjem:

- **Abstrakcije strojne opreme**: Brezhibno uvajanje na AMD, Intel, NVIDIA in Qualcomm čipe
- **Inteligenca na napravi**: AI, ki ohranja zasebnost in deluje izključno na lokalni strojni opremi
- **Optimizirana zmogljivost**: Modeli, predhodno optimizirani za konfiguracije strojne opreme Windows
- **Pripravljenost za podjetja**: Varnostne in skladnostne funkcije na ravni produkcije

### Zakaj Windows za Edge AI?

**Univerzalna podpora strojni opremi**  
Windows ML zagotavlja samodejno optimizacijo strojne opreme po celotnem ekosistemu Windows, kar zagotavlja, da vaše AI aplikacije delujejo optimalno ne glede na osnovno arhitekturo čipov.

**Integrirano AI okolje**  
Vgrajeni Windows ML inferenčni motor odpravlja zapletene zahteve za nastavitev, kar razvijalcem omogoča, da se osredotočijo na logiko aplikacije namesto na infrastrukturne skrbi.

**Optimizacija Copilot+ PC**  
Namenjeni API-ji, zasnovani posebej za naprave Windows naslednje generacije z namensko nevronsko procesno enoto (NPU), zagotavljajo izjemno zmogljivost na vat.

**Razvijalski ekosistem**  
Bogata orodja, vključno z integracijo Visual Studio, obsežno dokumentacijo in vzorčnimi aplikacijami, ki pospešujejo razvojne cikle.

## Cilji učenja

Z zaključkom tega vodnika za razvoj Windows Edge AI boste obvladali ključne veščine za gradnjo produkcijsko pripravljenih AI aplikacij na platformi Windows.

### Osnovne tehnične kompetence

**Obvladovanje Windows AI Foundry**  
- Razumevanje arhitekture in komponent platforme Windows AI Foundry  
- Navigacija po celotnem življenjskem ciklu razvoja AI znotraj ekosistema Windows  
- Uvajanje najboljših varnostnih praks za aplikacije AI na napravi  
- Optimizacija aplikacij za različne konfiguracije strojne opreme Windows  

**Strokovno znanje o integraciji API-jev**  
- Obvladovanje Windows AI API-jev za besedilo, vizijo in multimodalne aplikacije  
- Uvajanje jezikovnega modela Phi Silica za generiranje besedila in razmišljanje  
- Uporaba zmogljivosti računalniškega vida z vgrajenimi API-ji za obdelavo slik  
- Prilagajanje predhodno usposobljenih modelov z uporabo tehnik LoRA (Low-Rank Adaptation)  

**Lokalna implementacija Foundry**  
- Brskanje, ocenjevanje in uvajanje odprtokodnih jezikovnih modelov z uporabo Foundry Local CLI  
- Razumevanje optimizacije modelov in kvantizacije za lokalno uvajanje  
- Uvajanje AI zmogljivosti brez povezave, ki delujejo brez internetne povezave  
- Upravljanje življenjskega cikla modelov in posodobitev v produkcijskih okoljih  

**Uvajanje Windows ML**  
- Uvajanje prilagojenih ONNX modelov v aplikacije Windows z uporabo Windows ML  
- Izkoristite samodejno pospeševanje strojne opreme na CPU, GPU in NPU arhitekturah  
- Uvajanje inferenc v realnem času z optimalno uporabo virov  
- Oblikovanje skalabilnih AI aplikacij za različne kategorije naprav Windows  

### Veščine razvoja aplikacij

**Razvoj Windows aplikacij na več platformah**  
- Gradnja aplikacij, ki jih poganja AI, z uporabo .NET MAUI za univerzalno uvajanje na Windows  
- Integracija AI zmogljivosti v Win32, UWP in progresivne spletne aplikacije  
- Uvajanje odzivnih UI dizajnov, ki se prilagajajo stanjem obdelave AI  
- Upravljanje asinhronih AI operacij z ustreznimi vzorci uporabniške izkušnje  

**Optimizacija zmogljivosti**  
- Profiliranje in optimizacija zmogljivosti inferenc AI na različnih konfiguracijah strojne opreme  
- Uvajanje učinkovitega upravljanja pomnilnika za velike jezikovne modele  
- Oblikovanje aplikacij, ki se prilagodljivo odzivajo glede na razpoložljive zmogljivosti strojne opreme  
- Uporaba strategij predpomnjenja za pogosto uporabljene AI operacije  

**Pripravljenost za produkcijo**  
- Uvajanje celovitega upravljanja napak in mehanizmov za povratne ukrepe  
- Oblikovanje telemetrije in spremljanja zmogljivosti AI aplikacij  
- Uvajanje najboljših varnostnih praks za lokalno shranjevanje in izvajanje AI modelov  
- Načrtovanje strategij uvajanja za podjetniške in potrošniške aplikacije  

### Poslovno in strateško razumevanje

**Arhitektura AI aplikacij**  
- Oblikovanje hibridnih arhitektur, ki optimizirajo med lokalno in oblačno obdelavo AI  
- Ocenjevanje kompromisov med velikostjo modela, natančnostjo in hitrostjo inferenc  
- Načrtovanje arhitektur podatkovnih tokov, ki ohranjajo zasebnost in omogočajo inteligenco  
- Uvajanje stroškovno učinkovitih AI rešitev, ki se prilagajajo povpraševanju uporabnikov  

**Pozicioniranje na trgu**  
- Razumevanje konkurenčnih prednosti Windows-native AI aplikacij  
- Identifikacija primerov uporabe, kjer AI na napravi zagotavlja boljšo uporabniško izkušnjo  
- Razvoj strategij za vstop na trg za AI izboljšane Windows aplikacije  
- Pozicioniranje aplikacij za izkoriščanje prednosti ekosistema Windows  

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji zagotavljajo pripravljene AI zmogljivosti, ki jih poganjajo modeli na napravi, optimizirani za učinkovitost in zmogljivost na napravah Copilot+ PC z minimalnimi zahtevami za nastavitev.

#### Osnovne kategorije API-jev

**Jezikovni model Phi Silica**  
- Majhen, a zmogljiv jezikovni model za generiranje besedila in razmišljanje  
- Optimiziran za inferenco v realnem času z minimalno porabo energije  
- Podpora za prilagajanje z uporabo tehnik LoRA  
- Integracija z iskanjem po semantiki Windows in pridobivanjem znanja  

**API-ji za računalniški vid**  
- **Prepoznavanje besedila (OCR)**: Izvleček besedila iz slik z visoko natančnostjo  
- **Super resolucija slik**: Povečanje kakovosti slik z uporabo lokalnih AI modelov  
- **Segmentacija slik**: Identifikacija in izolacija specifičnih objektov na slikah  
- **Opis slik**: Generiranje podrobnih besedilnih opisov za vizualne vsebine  
- **Odstranjevanje objektov**: Odstranjevanje neželenih objektov s slik z AI-podprtim retuširanjem  

**Multimodalne zmogljivosti**  
- **Integracija vizije in jezika**: Kombinacija razumevanja besedila in slik  
- **Semantično iskanje**: Omogočanje naravnih jezikovnih poizvedb po večpredstavnostnih vsebinah  
- **Pridobivanje znanja**: Gradnja inteligentnih iskalnih izkušenj z lokalnimi podatki  

### 2. Foundry Local

Foundry Local razvijalcem omogoča hiter dostop do pripravljenih odprtokodnih jezikovnih modelov na Windows Silicon, kar omogoča brskanje, testiranje, interakcijo in uvajanje modelov v lokalne aplikacije.

#### Ključne funkcije

**Katalog modelov**  
- Obsežna zbirka predhodno optimiziranih odprtokodnih modelov  
- Modeli optimizirani za CPU, GPU in NPU za takojšnjo uporabo  
- Podpora za priljubljene družine modelov, vključno z Llama, Mistral, Phi in specializiranimi modeli za določene domene  

**Integracija CLI**  
- Ukazna vrstica za upravljanje in uvajanje modelov  
- Avtomatizirani postopki optimizacije in kvantizacije  
- Integracija s priljubljenimi razvojnimi okolji in CI/CD procesi  

**Lokalno uvajanje**  
- Popolno delovanje brez povezave brez odvisnosti od oblaka  
- Podpora za prilagojene formate in konfiguracije modelov  
- Učinkovito serviranje modelov z avtomatsko optimizacijo strojne opreme  

### 3. Windows ML

Windows ML služi kot osrednja AI platforma in integrirano inferenčno okolje na Windows, ki razvijalcem omogoča učinkovito uvajanje prilagojenih modelov po širokem ekosistemu strojne opreme Windows.

#### Prednosti arhitekture

**Univerzalna podpora strojni opremi**  
- Samodejna optimizacija za AMD, Intel, NVIDIA in Qualcomm čipe  
- Podpora za izvajanje na CPU, GPU in NPU z transparentnim preklapljanjem  
- Abstrakcija strojne opreme, ki odpravlja delo na optimizaciji specifične platforme  

**Prilagodljivost modelov**  
- Podpora za format modelov ONNX z avtomatsko pretvorbo iz priljubljenih ogrodij  
- Uvajanje prilagojenih modelov z zmogljivostjo na ravni produkcije  
- Integracija z obstoječimi arhitekturami aplikacij Windows  

**Integracija v podjetja**  
- Združljivost z varnostnimi in skladnostnimi okviri Windows  
- Podpora za uvajanje in upravljanje orodij v podjetjih  
- Integracija z upravljanjem in spremljanjem naprav Windows  

## Potek razvoja

### Faza 1: Priprava okolja in konfiguracija orodij

**Priprava razvojnega okolja**  
1. Namestite Visual Studio z razširitvijo AI Toolkit  
2. Konfigurirajte orodja Windows AI Foundry CLI  
3. Nastavite lokalno okolje za testiranje modelov  
4. Ustanovite orodja za profiliranje zmogljivosti in spremljanje  

**Raziskovanje AI Dev Gallery**  
- Raziskovanje vzorčnih aplikacij in referenčnih implementacij  
- Testiranje Windows AI API-jev z interaktivnimi demonstracijami  
- Pregled izvorne kode za najboljše prakse in vzorce  
- Identifikacija ustreznih vzorcev za vaš specifični primer uporabe  

### Faza 2: Izbira in integracija modelov

**Analiza zahtev**  
- Določite funkcionalne zahteve za AI zmogljivosti  
- Ustanovite omejitve zmogljivosti in cilje optimizacije  
- Ocenite zahteve glede zasebnosti in varnosti  
- Načrtujte arhitekturo uvajanja in strategije skaliranja  

**Ocena modelov**  
- Uporabite Foundry Local za testiranje odprtokodnih modelov za vaš primer uporabe  
- Primerjajte Windows AI API-je z zahtevami prilagojenih modelov  
- Ocenite kompromise med velikostjo modela, natančnostjo in hitrostjo inferenc  
- Prototipirajte pristope integracije z izbranimi modeli  

### Faza 3: Razvoj aplikacij

**Osnovna integracija**  
- Uvajanje integracije Windows AI API-jev z ustreznim upravljanjem napak  
- Oblikovanje uporabniških vmesnikov, ki upoštevajo delovne tokove obdelave AI  
- Uvajanje strategij predpomnjenja in optimizacije za inferenco modelov  
- Dodajanje telemetrije in spremljanja zmogljivosti AI operacij  

**Testiranje in validacija**  
- Testiranje aplikacij na različnih konfiguracijah strojne opreme Windows  
- Validacija zmogljivostnih metrik pod različnimi pogoji obremenitve  
- Uvajanje avtomatiziranega testiranja za zanesljivost funkcionalnosti AI  
- Izvedba testiranja uporabniške izkušnje z AI izboljšanimi funkcijami  

### Faza 4: Optimizacija in uvajanje

**Optimizacija zmogljivosti**  
- Profiliranje zmogljivosti aplikacije na ciljnih konfiguracijah strojne opreme  
- Optimizacija uporabe pomnilnika in strategij nalaganja modelov  
- Uvajanje prilagodljivega vedenja glede na razpoložljive zmogljivosti strojne opreme  
- Fino prilagajanje uporabniške izkušnje za različne scenarije zmogljivosti  

**Produkcijsko uvajanje**  
- Pakiranje aplikacij z ustreznimi odvisnostmi AI modelov  
- Uvajanje mehanizmov za posodobitve modelov in logike aplikacij  
- Konfiguracija spremljanja in analitike za produkcijska okolja  
- Načrtovanje strategij uvajanja za podjetniške in potrošniške aplikacije  

## Praktični primeri implementacije

### Primer 1: Inteligentna aplikacija za obdelavo dokumentov

Razvijte Windows aplikacijo, ki obdeluje dokumente z uporabo več AI zmogljivosti:

**Uporabljene tehnologije:**  
- Phi Silica za povzetke dokumentov in odgovarjanje na vprašanja  
- OCR API-ji za izvleček besedila iz skeniranih dokumentov  
- API-ji za opis slik za analizo grafov in diagramov  
- Prilagojeni ONNX modeli za klasifikacijo dokumentov  

**Pristop implementacije:**  
- Oblikovanje modularne arhitekture s priključljivimi AI komponentami  
- Uvajanje asinhrone obdelave za velike serije dokumentov  
- Dodajanje indikatorjev napredka in podpore za preklic dolgotrajnih operacij  
- Vključitev zmogljivosti brez povezave za obdelavo občutljivih dokumentov  

### Primer 2: Sistem za upravljanje zalog v trgovini

Ustvarite sistem za upravljanje zalog, ki ga poganja AI, za trgovinske aplikacije:

**Uporabljene tehnologije:**  
- Segmentacija slik za identifikacijo izdelkov  
- Prilagojeni modeli za vizijo za klasifikacijo blagovnih znamk in kategorij  
- Lokalno uvajanje specializiranih jezikovnih modelov za trgovino prek Foundry Local  
- Integracija z obstoječimi POS in sistemi za upravljanje zalog  

**Pristop implementacije:**  
- Gradnja integracije kamer za skeniranje izdelkov v realnem času  
- Uvajanje prepoznavanja črtnih kod in vizualne identifikacije izdelkov  
- Dodajanje naravnih jezikovnih poizvedb zalog z lokalnimi jezikovnimi modeli  
- Oblikovanje skalabilne arhitekture za uvajanje v več trgovinah  

### Primer 3: Pomočnik za dokumentacijo v zdravstvu

Razvijte orodje za dokumentacijo v zdravstvu, ki ohranja zasebnost:

**Uporabljene tehnologije:**  
- Phi Silica za generiranje medicinskih zapisov in podporo kliničnim odločitvam  
- OCR za digitalizacijo ročno napisanih medicinskih zapisov  
- Prilagojeni medicinski jezikovni modeli, uvedeni prek Windows ML  
- Lokalno shranjevanje vektorjev za pridobivanje medicinskega znanja  

**Pristop implementacije:**  
- Zagotovitev popolnega delovanja brez povezave za zasebnost pacientov  
- Uvajanje validacije medicinske terminologije in predlogov  
- Dodajanje revizijskega beleženja za skladnost z regulativami  
- Oblikovanje integracije z obstoječimi sistemi elektronskih zdravstvenih zapisov  

## Strategije optimizacije zmogljivosti

### Razvoj, ki upošteva strojno opremo

**Optimizacija NPU**  
- Oblikovanje aplikacij za izkoriščanje zmogljivosti NPU na napravah Copilot+ PC  
- Uvajanje prilagodljivega preklopa na GPU/CPU na napravah brez NPU  
- Optimizacija formatov modelov za pospeševanje specifično za NPU  
- Spremljanje uporabe NPU in termičnih značilnosti  

**Upravljanje pomnilnika**  
- Uvajanje učinkovitih strategij nalaganja in predpomnjenja modelov  
- Uporaba preslikave pomnilnika za velike modele za zmanjšanje časa zagona  
- Oblikovanje aplikacij, ki so zavestne glede pomnilnika
- Uporabite Foundry Local CLI za testiranje in validacijo modelov
- Uporabite orodja za testiranje Windows AI API za preverjanje integracije
- Implementirajte prilagojeno beleženje za spremljanje delovanja AI
- Ustvarite avtomatizirano testiranje za zanesljivost funkcionalnosti AI

## Priprava aplikacij na prihodnost

### Nastajajoče tehnologije

**Strojna oprema nove generacije**
- Oblikujte aplikacije, ki izkoriščajo prihodnje zmogljivosti NPU
- Načrtujte za večje velikosti modelov in večjo kompleksnost
- Implementirajte prilagodljive arhitekture za razvijajočo se strojno opremo
- Razmislite o algoritmih, pripravljenih na kvantno računalništvo, za prihodnjo združljivost

**Napredne zmogljivosti AI**
- Pripravite se na multimodalno integracijo AI za več vrst podatkov
- Načrtujte za sodelovalno AI v realnem času med več napravami
- Oblikujte za zmogljivosti federativnega učenja
- Razmislite o arhitekturah hibridne inteligence med robom in oblakom

### Nenehno učenje in prilagajanje

**Posodobitve modelov**
- Implementirajte mehanizme za nemotene posodobitve modelov
- Oblikujte aplikacije, ki se prilagajajo izboljšanim zmogljivostim modelov
- Načrtujte za združljivost nazaj z obstoječimi modeli
- Implementirajte A/B testiranje za ocenjevanje zmogljivosti modelov

**Razvoj funkcij**
- Oblikujte modularne arhitekture, ki omogočajo nove zmogljivosti AI
- Načrtujte za integracijo nastajajočih Windows AI API-jev
- Implementirajte funkcijske zastavice za postopno uvajanje zmogljivosti
- Oblikujte uporabniške vmesnike, ki se prilagajajo izboljšanim funkcijam AI

## Zaključek

Razvoj Windows Edge AI predstavlja združitev zmogljivih zmogljivosti AI z robustno, varno in skalabilno platformo Windows. Z obvladovanjem ekosistema Windows AI Foundry lahko razvijalci ustvarijo inteligentne aplikacije, ki zagotavljajo izjemne uporabniške izkušnje ob ohranjanju najvišjih standardov zasebnosti, varnosti in zmogljivosti.

Kombinacija Windows AI API-jev, Foundry Local in Windows ML ponuja neprekosljivo osnovo za gradnjo naslednje generacije inteligentnih aplikacij za Windows. Ko se AI še naprej razvija, platforma Windows zagotavlja, da se vaše aplikacije prilagajajo nastajajočim tehnologijam, hkrati pa ohranjajo združljivost in zmogljivost v raznoliki strojni opremi ekosistema Windows.

Ne glede na to, ali gradite aplikacije za potrošnike, rešitve za podjetja ali specializirana orodja za industrijo, razvoj Windows Edge AI omogoča ustvarjanje inteligentnih, odzivnih in globoko integriranih izkušenj, ki izkoriščajo polni potencial sodobnih naprav Windows.

## Dodatni viri

### Dokumentacija in učenje
- [Windows AI Foundry Documentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Overview](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Orodja za razvoj
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Samples](https://learn.microsoft.com/windows/ai/samples/)

### Skupnost in podpora
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Training](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ta vodnik je zasnovan tako, da se razvija skupaj s hitro napredujočim ekosistemom Windows AI. Redne posodobitve zagotavljajo usklajenost z najnovejšimi zmogljivostmi platforme in najboljšimi praksami razvoja.*

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.