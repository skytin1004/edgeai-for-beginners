<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-23T00:10:47+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "hr"
}
-->
# Windows Edge AI Razvojni Vodič

## Uvod

Dobrodošli u Windows Edge AI razvoj - vaš sveobuhvatan vodič za izradu inteligentnih aplikacija koje koriste snagu AI-a na uređaju putem Microsoftove platforme Windows AI Foundry. Ovaj vodič je posebno osmišljen za Windows programere koji žele integrirati najnovije Edge AI mogućnosti u svoje aplikacije, koristeći puni potencijal Windows hardverske akceleracije.

### Prednosti Windows AI-a

Windows AI Foundry predstavlja objedinjenu, pouzdanu i sigurnu platformu koja podržava cijeli životni ciklus AI razvoja - od odabira i prilagodbe modela do optimizacije i implementacije na CPU, GPU, NPU i hibridnim cloud arhitekturama. Ova platforma demokratizira AI razvoj pružajući:

- **Hardversku apstrakciju**: Jednostavna implementacija na AMD, Intel, NVIDIA i Qualcomm čipovima
- **Inteligenciju na uređaju**: AI koji čuva privatnost i radi isključivo na lokalnom hardveru
- **Optimizirane performanse**: Modeli unaprijed optimizirani za Windows hardverske konfiguracije
- **Spremnost za poduzeća**: Sigurnosne značajke i usklađenost na razini proizvodnje

### Zašto Windows za Edge AI?

**Univerzalna podrška za hardver**  
Windows ML automatski optimizira hardver u cijelom Windows ekosustavu, osiguravajući da vaše AI aplikacije rade optimalno bez obzira na temeljnu arhitekturu čipa.

**Integrirani AI Runtime**  
Ugrađeni Windows ML mehanizam za inferenciju eliminira složene zahtjeve za postavljanje, omogućujući programerima da se usredotoče na logiku aplikacije umjesto na infrastrukturne probleme.

**Copilot+ PC Optimizacija**  
API-ji dizajnirani posebno za sljedeću generaciju Windows uređaja s posvećenim Neural Processing Units (NPUs) pružaju izvanredne performanse po vatu.

**Razvojni ekosustav**  
Bogati alati uključujući integraciju s Visual Studiom, opsežnu dokumentaciju i uzorke aplikacija koji ubrzavaju razvojne cikluse.

## Ciljevi učenja

Završetkom ovog vodiča za razvoj Windows Edge AI-a, savladat ćete ključne vještine za izradu AI aplikacija spremnih za proizvodnju na Windows platformi.

### Osnovne tehničke kompetencije

**Majstorstvo Windows AI Foundry-a**  
- Razumijevanje arhitekture i komponenti platforme Windows AI Foundry  
- Navigacija kroz cijeli životni ciklus AI razvoja unutar Windows ekosustava  
- Primjena sigurnosnih najboljih praksi za AI aplikacije na uređaju  
- Optimizacija aplikacija za različite Windows hardverske konfiguracije  

**Ekspertiza u integraciji API-ja**  
- Savladavanje Windows AI API-ja za tekst, viziju i multimodalne aplikacije  
- Implementacija Phi Silica jezičnog modela za generiranje teksta i zaključivanje  
- Primjena računalne vizije koristeći ugrađene API-je za obradu slika  
- Prilagodba unaprijed treniranih modela pomoću LoRA (Low-Rank Adaptation) tehnika  

**Lokalna implementacija Foundry-a**  
- Pregled, evaluacija i implementacija otvorenih jezičnih modela pomoću Foundry Local CLI  
- Razumijevanje optimizacije modela i kvantizacije za lokalnu implementaciju  
- Primjena offline AI mogućnosti koje funkcioniraju bez internetske povezanosti  
- Upravljanje životnim ciklusima modela i ažuriranjima u proizvodnim okruženjima  

**Windows ML implementacija**  
- Integracija prilagođenih ONNX modela u Windows aplikacije koristeći Windows ML  
- Iskorištavanje automatske hardverske akceleracije na CPU, GPU i NPU arhitekturama  
- Implementacija inferencije u stvarnom vremenu s optimalnim korištenjem resursa  
- Dizajn skalabilnih AI aplikacija za različite kategorije Windows uređaja  

### Vještine razvoja aplikacija

**Razvoj za više platformi na Windowsu**  
- Izrada AI aplikacija koristeći .NET MAUI za univerzalnu implementaciju na Windowsu  
- Integracija AI mogućnosti u Win32, UWP i progresivne web aplikacije  
- Implementacija responzivnih UI dizajna koji se prilagođavaju AI procesima  
- Upravljanje asinkronim AI operacijama uz pravilne obrasce korisničkog iskustva  

**Optimizacija performansi**  
- Profiliranje i optimizacija performansi AI inferencije na različitim hardverskim konfiguracijama  
- Implementacija učinkovitog upravljanja memorijom za velike jezične modele  
- Dizajn aplikacija koje se prilagođavaju dostupnim hardverskim mogućnostima  
- Primjena strategija keširanja za često korištene AI operacije  

**Spremnost za proizvodnju**  
- Implementacija sveobuhvatnog rukovanja greškama i mehanizama za povratne opcije  
- Dizajn telemetrije i praćenja performansi AI aplikacija  
- Primjena sigurnosnih najboljih praksi za lokalno pohranjivanje i izvršavanje AI modela  
- Planiranje strategija implementacije za poduzeća i potrošačke aplikacije  

### Poslovno i strateško razumijevanje

**Arhitektura AI aplikacija**  
- Dizajn hibridnih arhitektura koje optimiziraju između lokalne i cloud AI obrade  
- Procjena kompromisa između veličine modela, točnosti i brzine inferencije  
- Planiranje arhitekture protoka podataka koja čuva privatnost uz omogućavanje inteligencije  
- Implementacija isplativih AI rješenja koja se skaliraju prema korisničkim zahtjevima  

**Pozicioniranje na tržištu**  
- Razumijevanje konkurentskih prednosti Windows-nativnih AI aplikacija  
- Identifikacija slučajeva upotrebe gdje AI na uređaju pruža superiorno korisničko iskustvo  
- Razvoj strategija za plasiranje AI-poboljšanih Windows aplikacija na tržište  
- Pozicioniranje aplikacija za iskorištavanje prednosti Windows ekosustava  

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji pružaju gotove AI mogućnosti koje pokreću modeli na uređaju, optimizirani za učinkovitost i performanse na Copilot+ PC uređajima uz minimalne zahtjeve za postavljanje.

#### Osnovne kategorije API-ja

**Phi Silica jezični model**  
- Mali, ali moćan jezični model za generiranje teksta i zaključivanje  
- Optimiziran za inferenciju u stvarnom vremenu uz minimalnu potrošnju energije  
- Podrška za prilagodbu pomoću LoRA tehnika  
- Integracija s Windows semantičkom pretragom i dohvatom znanja  

**API-ji za računalnu viziju**  
- **Prepoznavanje teksta (OCR)**: Ekstrakcija teksta iz slika s visokom točnošću  
- **Super rezolucija slike**: Povećanje kvalitete slika koristeći lokalne AI modele  
- **Segmentacija slike**: Identifikacija i izolacija specifičnih objekata na slikama  
- **Opis slike**: Generiranje detaljnih tekstualnih opisa za vizualni sadržaj  
- **Brisanje objekata**: Uklanjanje neželjenih objekata sa slika pomoću AI-a  

**Multimodalne mogućnosti**  
- **Integracija vizije i jezika**: Kombinacija razumijevanja teksta i slika  
- **Semantička pretraga**: Omogućavanje prirodnih jezičnih upita za multimedijski sadržaj  
- **Dohvat znanja**: Izgradnja inteligentnih iskustava pretraživanja s lokalnim podacima  

### 2. Foundry Local

Foundry Local omogućuje programerima brz pristup gotovim otvorenim jezičnim modelima na Windows Siliconu, nudeći mogućnost pregledavanja, testiranja, interakcije i implementacije modela u lokalnim aplikacijama.

#### Ključne značajke

**Katalog modela**  
- Sveobuhvatan izbor unaprijed optimiziranih otvorenih modela  
- Modeli optimizirani za CPU, GPU i NPU za trenutnu implementaciju  
- Podrška za popularne obitelji modela uključujući Llama, Mistral, Phi i specijalizirane domenske modele  

**CLI integracija**  
- Sučelje naredbenog retka za upravljanje modelima i implementaciju  
- Automatizirani tijekovi rada za optimizaciju i kvantizaciju  
- Integracija s popularnim razvojnim okruženjima i CI/CD alatima  

**Lokalna implementacija**  
- Potpuno offline operacija bez ovisnosti o cloudu  
- Podrška za prilagođene formate i konfiguracije modela  
- Učinkovito posluživanje modela uz automatsku hardversku optimizaciju  

### 3. Windows ML

Windows ML služi kao osnovna AI platforma i integrirani runtime za inferenciju na Windowsu, omogućujući programerima učinkovitu implementaciju prilagođenih modela u širokom Windows hardverskom ekosustavu.

#### Prednosti arhitekture

**Univerzalna podrška za hardver**  
- Automatska optimizacija za AMD, Intel, NVIDIA i Qualcomm čipove  
- Podrška za CPU, GPU i NPU izvršavanje uz transparentno prebacivanje  
- Hardverska apstrakcija koja eliminira potrebu za specifičnom optimizacijom platforme  

**Fleksibilnost modela**  
- Podrška za ONNX format modela uz automatsku konverziju iz popularnih okvira  
- Implementacija prilagođenih modela s performansama na razini proizvodnje  
- Integracija s postojećim arhitekturama Windows aplikacija  

**Integracija za poduzeća**  
- Kompatibilnost s Windows sigurnosnim i usklađenim okvirima  
- Podrška za alate za implementaciju i upravljanje u poduzećima  
- Integracija s Windows sustavima za upravljanje uređajima i praćenje  

## Tijek razvoja

### Faza 1: Postavljanje okruženja i konfiguracija alata

**Priprema razvojnog okruženja**  
1. Instalirajte Visual Studio s AI Toolkit ekstenzijom  
2. Konfigurirajte Windows AI Foundry CLI alate  
3. Postavite lokalno okruženje za testiranje modela  
4. Uspostavite alate za profiliranje performansi i praćenje  

**Istraživanje AI Dev Gallery-a**  
- Istražite uzorke aplikacija i referentne implementacije  
- Testirajte Windows AI API-je uz interaktivne demonstracije  
- Pregledajte izvorni kod za najbolje prakse i obrasce  
- Identificirajte relevantne uzorke za vaš specifični slučaj upotrebe  

### Faza 2: Odabir i integracija modela

**Analiza zahtjeva**  
- Definirajte funkcionalne zahtjeve za AI mogućnosti  
- Uspostavite ograničenja performansi i ciljeve optimizacije  
- Procijenite zahtjeve za privatnost i sigurnost  
- Planirajte arhitekturu implementacije i strategije skaliranja  

**Evaluacija modela**  
- Koristite Foundry Local za testiranje otvorenih modela za vaš slučaj upotrebe  
- Benchmarkirajte Windows AI API-je prema zahtjevima prilagođenih modela  
- Procijenite kompromise između veličine modela, točnosti i brzine inferencije  
- Prototipirajte pristupe integraciji s odabranim modelima  

### Faza 3: Razvoj aplikacije

**Osnovna integracija**  
- Implementirajte integraciju Windows AI API-ja uz pravilno rukovanje greškama  
- Dizajnirajte korisnička sučelja koja se prilagođavaju AI procesima  
- Implementirajte strategije keširanja i optimizacije za inferenciju modela  
- Dodajte telemetriju i praćenje performansi AI operacija  

**Testiranje i validacija**  
- Testirajte aplikacije na različitim Windows hardverskim konfiguracijama  
- Validirajte performanse pod različitim uvjetima opterećenja  
- Implementirajte automatizirano testiranje za pouzdanost AI funkcionalnosti  
- Provedite testiranje korisničkog iskustva s AI-poboljšanim značajkama  

### Faza 4: Optimizacija i implementacija

**Optimizacija performansi**  
- Profilirajte performanse aplikacije na ciljnim hardverskim konfiguracijama  
- Optimizirajte korištenje memorije i strategije učitavanja modela  
- Implementirajte adaptivno ponašanje na temelju dostupnih hardverskih mogućnosti  
- Fino prilagodite korisničko iskustvo za različite scenarije performansi  

**Implementacija u proizvodnju**  
- Pakirajte aplikacije s odgovarajućim AI modelima i ovisnostima  
- Implementirajte mehanizme za ažuriranje modela i logike aplikacije  
- Konfigurirajte praćenje i analitiku za proizvodna okruženja  
- Planirajte strategije uvođenja za poduzeća i potrošačke aplikacije  

## Primjeri praktične implementacije

### Primjer 1: Inteligentna aplikacija za obradu dokumenata

Izradite Windows aplikaciju koja obrađuje dokumente koristeći više AI mogućnosti:

**Korištene tehnologije:**  
- Phi Silica za sažimanje dokumenata i odgovaranje na pitanja  
- OCR API-ji za ekstrakciju teksta iz skeniranih dokumenata  
- API-ji za opis slike za analizu grafikona i dijagrama  
- Prilagođeni ONNX modeli za klasifikaciju dokumenata  

**Pristup implementaciji:**  
- Dizajnirajte modularnu arhitekturu s prilagodljivim AI komponentama  
- Implementirajte asinkronu obradu za velike serije dokumenata  
- Dodajte indikatore napretka i podršku za otkazivanje dugotrajnih operacija  
- Uključite offline mogućnosti za obradu osjetljivih dokumenata  

### Primjer 2: Sustav za upravljanje inventarom u maloprodaji

Izradite AI-poboljšan sustav inventara za maloprodajne aplikacije:

**Korištene tehnologije:**  
- Segmentacija slike za identifikaciju proizvoda  
- Prilagođeni modeli vizije za klasifikaciju brendova i kategorija  
- Foundry Local implementacija specijaliziranih jezičnih modela za maloprodaju  
- Integracija s postojećim POS i inventarskim sustavima  

**Pristup implementaciji:**  
- Izgradite integraciju s kamerama za skeniranje proizvoda u stvarnom vremenu  
- Implementirajte prepoznavanje bar kodova i vizualnih proizvoda  
- Dodajte prirodne jezične upite za inventar koristeći lokalne jezične modele  
- Dizajnirajte skalabilnu arhitekturu za implementaciju u više trgovina  

### Primjer 3: Asistent za dokumentaciju u zdravstvu

Razvijte alat za dokumentaciju u zdravstvu koji čuva privatnost:

**Korištene tehnologije:**  
- Phi Silica za generiranje medicinskih bilješki i podršku kliničkim odlukama  
- OCR za digitalizaciju rukom pisanih medicinskih zapisa  
- Prilagođeni medicinski jezični modeli implementirani putem Windows ML-a  
- Lokalno pohranjivanje vektora za dohvat medicinskog znanja  

**Pristup implementaciji:**  
- Osigurajte potpuno offline operacije za privatnost pacijenata  
- Implementirajte validaciju medicinske terminologije i prijedloge  
- Dodajte zapisivanje revizije za usklađenost s regulativama  
- Dizajnirajte integraciju s postojećim sustavima elektroničkih zdravstvenih zapisa  

## Strategije optimizacije performansi

### Razvoj svjestan hardvera

**Optimizacija za NPU**  
- Dizajnirajte aplikacije koje koriste NPU mogućnosti na Copilot+ PC-ima  
- Implementirajte elegantan povratak na GPU/CPU na uređajima bez NPU-a  
- Optimizirajte formate modela za NPU-specifičnu akceleraciju  
- Pratite korištenje NPU-a i termalne karakteristike  

**Upravljanje memorijom**  
- Implementirajte učinkovite strategije učitavanja i keširanja modela  
- Koristite mapiranje memorije za velike modele kako biste smanjili vrijeme pokretanja  
- Dizajnirajte aplikacije svjesne memorije za uređaje s ograničenim resursima  
- Implementirajte kvantizaciju modela za optimizaciju memorije  

**Učinkovitost baterije**  
- Optimizirajte AI operacije za minimalnu potrošnju energije  
- Implementirajte adaptivnu obradu na temelju statusa baterije  
- Dizajnirajte učinkovitu obradu u pozadini za kontinuirane AI operacije  
- Koristite alate za profiliranje energije za optimizaciju potrošnje  

### Razmatranja skalabilnosti

**Višestruko niti**  
- Dizajnirajte AI operacije sigurne za niti za istovremenu obradu  
- Implementirajte učinkovitu distribuciju rada na dostupne jezgre  
- Koristite async/await obrasce za neblokirajuće AI operacije  
- Planirajte optimizaciju bazena niti za različite hardverske konfiguracije  

**Strategije keširanja**  
- Implementirajte inteligentno keširanje za često korištene AI operacije  
- Dizajnirajte strategije poništavanja keša za až
- Iskoristite Foundry Local CLI za testiranje i validaciju modela
- Koristite Windows AI API alate za testiranje integracije
- Implementirajte prilagođeno logiranje za praćenje AI operacija
- Kreirajte automatizirano testiranje za pouzdanost AI funkcionalnosti

## Priprema aplikacija za budućnost

### Napredne tehnologije

**Hardver nove generacije**
- Dizajnirajte aplikacije koje koriste buduće mogućnosti NPU-a
- Planirajte za povećanje veličine i složenosti modela
- Implementirajte prilagodljive arhitekture za razvoj hardvera
- Razmotrite algoritme spremne za kvantno računalstvo za buduću kompatibilnost

**Napredne AI mogućnosti**
- Pripremite se za integraciju multimodalne AI tehnologije s više vrsta podataka
- Planirajte za real-time suradnju AI-a između više uređaja
- Dizajnirajte za mogućnosti federativnog učenja
- Razmotrite hibridne arhitekture inteligencije između edge i cloud okruženja

### Kontinuirano učenje i prilagodba

**Ažuriranja modela**
- Implementirajte mehanizme za neprimjetno ažuriranje modela
- Dizajnirajte aplikacije koje se prilagođavaju poboljšanim mogućnostima modela
- Planirajte za unatrag kompatibilnost s postojećim modelima
- Implementirajte A/B testiranje za evaluaciju performansi modela

**Evolucija značajki**
- Dizajnirajte modularne arhitekture koje omogućuju dodavanje novih AI mogućnosti
- Planirajte za integraciju novih Windows AI API-ja
- Implementirajte zastavice značajki za postupno uvođenje novih mogućnosti
- Dizajnirajte korisničke sučelje koje se prilagođava poboljšanim AI značajkama

## Zaključak

Razvoj Windows Edge AI-a predstavlja spoj moćnih AI mogućnosti s robusnom, sigurnom i skalabilnom Windows platformom. Ovladavanjem ekosustavom Windows AI Foundry, developeri mogu kreirati inteligentne aplikacije koje pružaju izvanredno korisničko iskustvo uz održavanje najviših standarda privatnosti, sigurnosti i performansi.

Kombinacija Windows AI API-ja, Foundry Local-a i Windows ML-a pruža neusporedivu osnovu za izgradnju sljedeće generacije inteligentnih Windows aplikacija. Kako AI nastavlja evoluirati, Windows platforma osigurava da vaše aplikacije rastu s novim tehnologijama, uz održavanje kompatibilnosti i performansi na raznolikom Windows hardverskom ekosustavu.

Bez obzira razvijate li aplikacije za potrošače, poslovna rješenja ili specijalizirane industrijske alate, razvoj Windows Edge AI-a omogućuje vam stvaranje inteligentnih, responzivnih i duboko integriranih iskustava koja koriste puni potencijal modernih Windows uređaja.

## Dodatni resursi

Za korak-po-korak vodič za Foundry Local (instalacija, CLI, dinamične krajnje točke, korištenje SDK-a), pogledajte vodič u repozitoriju: [foundrylocal.md](./foundrylocal.md).

### Dokumentacija i učenje
- [Windows AI Foundry Dokumentacija](https://learn.microsoft.com/windows/ai/)
- [Windows AI API Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Početak](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Pregled](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Alati za razvoj
- [AI Toolkit za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Primjeri](https://learn.microsoft.com/windows/ai/samples/)

### Zajednica i podrška
- [Windows Developer Zajednica](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Trening](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ovaj vodič je dizajniran da se razvija zajedno s brzo napredujućim Windows AI ekosustavom. Redovita ažuriranja osiguravaju usklađenost s najnovijim mogućnostima platforme i najboljim praksama razvoja.*

---

