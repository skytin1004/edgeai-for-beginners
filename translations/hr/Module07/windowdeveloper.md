<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ec2b092ed161fd4d3907e010f8cf544",
  "translation_date": "2025-09-19T01:56:12+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "hr"
}
-->
# Vodič za razvoj Windows Edge AI

## Uvod

Dobrodošli u razvoj Windows Edge AI - vaš sveobuhvatan vodič za izgradnju inteligentnih aplikacija koje koriste snagu AI-a na uređaju putem Microsoftove platforme Windows AI Foundry. Ovaj vodič je posebno osmišljen za Windows programere koji žele integrirati najnovije mogućnosti Edge AI-a u svoje aplikacije, koristeći puni potencijal hardverske akceleracije Windowsa.

### Prednosti Windows AI-a

Windows AI Foundry predstavlja jedinstvenu, pouzdanu i sigurnu platformu koja podržava cijeli životni ciklus AI razvoja - od odabira i prilagodbe modela do optimizacije i implementacije na CPU, GPU, NPU i hibridnim cloud arhitekturama. Ova platforma demokratizira AI razvoj pružajući:

- **Hardversku apstrakciju**: Jednostavna implementacija na AMD, Intel, NVIDIA i Qualcomm čipovima
- **Inteligenciju na uređaju**: AI koji čuva privatnost i radi isključivo na lokalnom hardveru
- **Optimizirane performanse**: Modeli unaprijed optimizirani za Windows hardverske konfiguracije
- **Spremnost za poduzeća**: Sigurnosne i usklađenosti značajke za produkcijsko okruženje

### Zašto Windows za Edge AI?

**Univerzalna podrška za hardver**  
Windows ML automatski optimizira hardver u cijelom Windows ekosustavu, osiguravajući da vaše AI aplikacije rade optimalno bez obzira na arhitekturu čipa.

**Integrirani AI Runtime**  
Ugrađeni Windows ML mehanizam za inferenciju eliminira složene zahtjeve za postavljanje, omogućujući programerima da se fokusiraju na logiku aplikacije umjesto na infrastrukturne probleme.

**Copilot+ PC Optimizacija**  
API-ji dizajnirani posebno za sljedeću generaciju Windows uređaja s posvećenim Neural Processing Units (NPUs) pružaju izvanredne performanse po vatu.

**Razvojni ekosustav**  
Bogati alati uključujući integraciju s Visual Studiom, opsežnu dokumentaciju i primjere aplikacija koji ubrzavaju razvojne cikluse.

## Ciljevi učenja

Završetkom ovog vodiča za razvoj Windows Edge AI-a, savladat ćete ključne vještine za izgradnju produkcijski spremnih AI aplikacija na Windows platformi.

### Temeljne tehničke kompetencije

**Majstorstvo Windows AI Foundry-a**  
- Razumijevanje arhitekture i komponenti platforme Windows AI Foundry  
- Navigacija kroz cijeli životni ciklus AI razvoja unutar Windows ekosustava  
- Implementacija sigurnosnih najboljih praksi za AI aplikacije na uređaju  
- Optimizacija aplikacija za različite Windows hardverske konfiguracije  

**Ekspertiza u integraciji API-ja**  
- Savladavanje Windows AI API-ja za tekst, viziju i multimodalne aplikacije  
- Implementacija Phi Silica jezičnog modela za generiranje teksta i zaključivanje  
- Primjena računalne vizije putem ugrađenih API-ja za obradu slika  
- Prilagodba unaprijed treniranih modela pomoću LoRA (Low-Rank Adaptation) tehnika  

**Lokalna implementacija Foundry-a**  
- Pregled, evaluacija i implementacija otvorenih jezičnih modela pomoću Foundry Local CLI  
- Razumijevanje optimizacije i kvantizacije modela za lokalnu implementaciju  
- Implementacija offline AI mogućnosti koje funkcioniraju bez internetske povezanosti  
- Upravljanje životnim ciklusima modela i ažuriranjima u produkcijskim okruženjima  

**Windows ML implementacija**  
- Integracija prilagođenih ONNX modela u Windows aplikacije pomoću Windows ML-a  
- Korištenje automatske hardverske akceleracije na CPU, GPU i NPU arhitekturama  
- Implementacija inferencije u stvarnom vremenu uz optimalno korištenje resursa  
- Dizajn skalabilnih AI aplikacija za različite kategorije Windows uređaja  

### Vještine razvoja aplikacija

**Razvoj za više platformi na Windowsu**  
- Izgradnja AI aplikacija pomoću .NET MAUI za univerzalnu implementaciju na Windowsu  
- Integracija AI mogućnosti u Win32, UWP i progresivne web aplikacije  
- Implementacija responzivnih UI dizajna koji se prilagođavaju AI procesima  
- Upravljanje asinkronim AI operacijama uz pravilne obrasce korisničkog iskustva  

**Optimizacija performansi**  
- Profiliranje i optimizacija performansi AI inferencije na različitim hardverskim konfiguracijama  
- Implementacija učinkovitog upravljanja memorijom za velike jezične modele  
- Dizajn aplikacija koje se prilagođavaju dostupnim hardverskim mogućnostima  
- Primjena strategija keširanja za često korištene AI operacije  

**Spremnost za produkciju**  
- Implementacija sveobuhvatnog rukovanja greškama i mehanizama za povratne opcije  
- Dizajn telemetrije i praćenja performansi AI aplikacija  
- Primjena sigurnosnih najboljih praksi za lokalno pohranjivanje i izvršavanje AI modela  
- Planiranje strategija implementacije za poduzeća i potrošačke aplikacije  

### Poslovno i strateško razumijevanje

**Arhitektura AI aplikacija**  
- Dizajn hibridnih arhitektura koje optimiziraju između lokalne i cloud AI obrade  
- Evaluacija kompromisa između veličine modela, točnosti i brzine inferencije  
- Planiranje arhitekture protoka podataka koja čuva privatnost uz omogućavanje inteligencije  
- Implementacija isplativih AI rješenja koja se skaliraju prema zahtjevima korisnika  

**Pozicioniranje na tržištu**  
- Razumijevanje konkurentskih prednosti Windows-nativnih AI aplikacija  
- Identifikacija slučajeva upotrebe gdje AI na uređaju pruža superiorno korisničko iskustvo  
- Razvoj strategija za plasiranje AI-poboljšanih Windows aplikacija na tržište  
- Pozicioniranje aplikacija za iskorištavanje prednosti Windows ekosustava  

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji pružaju gotove AI mogućnosti koje pokreću modeli na uređaju, optimizirani za učinkovitost i performanse na Copilot+ PC uređajima uz minimalne zahtjeve za postavljanje.

#### Ključne kategorije API-ja

**Phi Silica jezični model**  
- Mali, ali moćan jezični model za generiranje teksta i zaključivanje  
- Optimiziran za inferenciju u stvarnom vremenu uz minimalnu potrošnju energije  
- Podrška za prilagodbu pomoću LoRA tehnika  
- Integracija s Windows semantičkom pretragom i dohvatom znanja  

**API-ji za računalnu viziju**  
- **Prepoznavanje teksta (OCR)**: Ekstrakcija teksta iz slika s visokom točnošću  
- **Super rezolucija slike**: Poboljšanje kvalitete slika pomoću lokalnih AI modela  
- **Segmentacija slike**: Identifikacija i izolacija specifičnih objekata na slikama  
- **Opis slike**: Generiranje detaljnih tekstualnih opisa za vizualni sadržaj  
- **Brisanje objekata**: Uklanjanje neželjenih objekata sa slika pomoću AI-a  

**Multimodalne mogućnosti**  
- **Integracija vizije i jezika**: Kombinacija razumijevanja teksta i slike  
- **Semantička pretraga**: Omogućavanje prirodnih jezičnih upita za multimedijski sadržaj  
- **Dohvat znanja**: Izgradnja inteligentnih pretraživačkih iskustava s lokalnim podacima  

### 2. Foundry Local

Foundry Local omogućuje programerima brz pristup gotovim otvorenim jezičnim modelima na Windows Siliconu, nudeći mogućnost pregleda, testiranja, interakcije i implementacije modela u lokalnim aplikacijama.

#### Ključne značajke

**Katalog modela**  
- Sveobuhvatan izbor unaprijed optimiziranih otvorenih modela  
- Modeli optimizirani za CPU, GPU i NPU za trenutnu implementaciju  
- Podrška za popularne obitelji modela uključujući Llama, Mistral, Phi i specijalizirane domenske modele  

**CLI integracija**  
- Sučelje naredbenog retka za upravljanje modelima i implementaciju  
- Automatizirani radni procesi za optimizaciju i kvantizaciju  
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
- Implementacija prilagođenih modela s performansama spremnim za produkciju  
- Integracija s postojećim arhitekturama Windows aplikacija  

**Integracija za poduzeća**  
- Kompatibilnost s Windows sigurnosnim i usklađenosti okvirima  
- Podrška za implementaciju i upravljanje alatima za poduzeća  
- Integracija s alatima za upravljanje i praćenje Windows uređaja  
- Koristite Foundry Local CLI za testiranje i validaciju modela  
- Koristite Windows AI API alate za testiranje integracije  
- Implementirajte prilagođeno logiranje za praćenje AI operacija  
- Kreirajte automatizirano testiranje za pouzdanost AI funkcionalnosti  

## Priprema vaših aplikacija za budućnost  

### Tehnologije u razvoju  

**Hardver nove generacije**  
- Dizajnirajte aplikacije koje koriste buduće mogućnosti NPU-a  
- Planirajte za povećanje veličine i složenosti modela  
- Implementirajte prilagodljive arhitekture za razvoj hardvera  
- Razmotrite algoritme spremne za kvantno računarstvo za buduću kompatibilnost  

**Napredne AI mogućnosti**  
- Pripremite se za integraciju multimodalnog AI-a kroz više vrsta podataka  
- Planirajte za real-time suradnju AI-a između više uređaja  
- Dizajnirajte za mogućnosti federativnog učenja  
- Razmotrite hibridne arhitekture inteligencije između edge-a i oblaka  

### Kontinuirano učenje i prilagodba  

**Ažuriranja modela**  
- Implementirajte mehanizme za neprimjetna ažuriranja modela  
- Dizajnirajte aplikacije koje se prilagođavaju poboljšanim mogućnostima modela  
- Planirajte za povratnu kompatibilnost s postojećim modelima  
- Implementirajte A/B testiranje za evaluaciju performansi modela  

**Evolucija značajki**  
- Dizajnirajte modularne arhitekture koje omogućuju nove AI mogućnosti  
- Planirajte za integraciju novih Windows AI API-ja  
- Implementirajte zastavice značajki za postupno uvođenje mogućnosti  
- Dizajnirajte korisničke sučelja koja se prilagođavaju poboljšanim AI značajkama  

## Zaključak  

Razvoj Windows Edge AI-a predstavlja spoj moćnih AI mogućnosti s robusnom, sigurnom i skalabilnom Windows platformom. Ovladavanjem ekosustavom Windows AI Foundry, developeri mogu kreirati inteligentne aplikacije koje pružaju izvanredna korisnička iskustva uz održavanje najviših standarda privatnosti, sigurnosti i performansi.  

Kombinacija Windows AI API-ja, Foundry Local-a i Windows ML-a pruža neusporedivu osnovu za izgradnju sljedeće generacije inteligentnih Windows aplikacija. Kako AI nastavlja evoluirati, Windows platforma osigurava da vaše aplikacije rastu s novim tehnologijama, uz održavanje kompatibilnosti i performansi na raznolikom Windows hardverskom ekosustavu.  

Bez obzira razvijate li aplikacije za potrošače, poslovna rješenja ili specijalizirane industrijske alate, razvoj Windows Edge AI-a omogućuje vam stvaranje inteligentnih, responzivnih i duboko integriranih iskustava koja koriste puni potencijal modernih Windows uređaja.  

## Dodatni resursi  

### Dokumentacija i učenje  
- [Windows AI Foundry Dokumentacija](https://learn.microsoft.com/windows/ai/)  
- [Windows AI API Referenca](https://learn.microsoft.com/windows/ai/apis/)  
- [Foundry Local Početak rada](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Windows ML Pregled](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  

### Alati za razvoj  
- [AI Alatni set za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)  
- [AI Dev Galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)  
- [Windows AI Primjeri](https://learn.microsoft.com/windows/ai/samples/)  

### Zajednica i podrška  
- [Windows Developer Zajednica](https://developer.microsoft.com/en-us/windows/)  
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)  
- [Microsoft Learn AI Trening](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)  

---  

*Ovaj vodič dizajniran je da se razvija zajedno s brzo napredujućim ekosustavom Windows AI-a. Redovita ažuriranja osiguravaju usklađenost s najnovijim mogućnostima platforme i najboljim praksama razvoja.*  

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.