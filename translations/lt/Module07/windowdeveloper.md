<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-23T00:43:14+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "lt"
}
-->
# Windows Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į Windows Edge AI kūrimą – išsamų vadovą, padėsiantį kurti išmaniąsias programas, kurios pasitelkia įrenginiuose veikiančią dirbtinio intelekto galią naudojant Microsoft Windows AI Foundry platformą. Šis vadovas skirtas Windows kūrėjams, norintiems integruoti pažangias Edge AI galimybes į savo programas, pasinaudojant visais Windows aparatūros pagreičio privalumais.

### Windows AI privalumai

Windows AI Foundry yra vieninga, patikima ir saugi platforma, palaikanti visą dirbtinio intelekto kūrimo ciklą – nuo modelio pasirinkimo ir pritaikymo iki optimizavimo ir diegimo CPU, GPU, NPU ir hibridinės debesų architektūros pagrindu. Ši platforma demokratizuoja dirbtinio intelekto kūrimą, siūlydama:

- **Aparatūros abstrakciją**: Sklandus diegimas AMD, Intel, NVIDIA ir Qualcomm lustuose
- **Vietinis intelektas**: Privatumo užtikrinantis dirbtinis intelektas, veikiantis tik vietinėje aparatūroje
- **Optimizuotas našumas**: Modeliai, iš anksto optimizuoti Windows aparatūros konfigūracijoms
- **Paruošta verslui**: Gamybinio lygio saugumo ir atitikties funkcijos

### Kodėl Windows Edge AI?

**Universalus aparatūros palaikymas**  
Windows ML automatiškai optimizuoja aparatūrą visoje Windows ekosistemoje, užtikrindama, kad jūsų dirbtinio intelekto programos veiktų optimaliai, nepriklausomai nuo pagrindinės lustų architektūros.

**Integruota AI vykdymo aplinka**  
Įmontuotas Windows ML inferencijos variklis pašalina sudėtingus nustatymo reikalavimus, leidžiant kūrėjams susitelkti į programos logiką, o ne infrastruktūros problemas.

**Copilot+ PC optimizacija**  
Specialiai sukurti API, skirti naujos kartos Windows įrenginiams su dedikuotais neuroniniais procesoriais (NPU), užtikrinantys išskirtinį našumą per vatą.

**Kūrėjų ekosistema**  
Platus įrankių pasirinkimas, įskaitant Visual Studio integraciją, išsamią dokumentaciją ir pavyzdines programas, kurios pagreitina kūrimo ciklus.

## Mokymosi tikslai

Baigę šį Windows Edge AI kūrimo vadovą, įgysite esminių įgūdžių, reikalingų kurti gamybai paruoštas dirbtinio intelekto programas Windows platformoje.

### Pagrindinės techninės kompetencijos

**Windows AI Foundry įvaldymas**  
- Suprasti Windows AI Foundry platformos architektūrą ir komponentus  
- Naršyti visą dirbtinio intelekto kūrimo ciklą Windows ekosistemoje  
- Įgyvendinti saugumo geriausią praktiką vietinėms dirbtinio intelekto programoms  
- Optimizuoti programas skirtingoms Windows aparatūros konfigūracijoms  

**API integracijos ekspertizė**  
- Įvaldyti Windows AI API tekstui, vaizdams ir multimodalinėms programoms  
- Įgyvendinti Phi Silica kalbos modelio integraciją tekstų generavimui ir samprotavimui  
- Diegti kompiuterinio matymo galimybes naudojant įmontuotus vaizdų apdorojimo API  
- Pritaikyti iš anksto apmokytus modelius naudojant LoRA (Low-Rank Adaptation) technikas  

**Foundry Local įgyvendinimas**  
- Naršyti, vertinti ir diegti atvirojo kodo kalbos modelius naudojant Foundry Local CLI  
- Suprasti modelių optimizavimą ir kvantizavimą vietiniam diegimui  
- Įgyvendinti neprisijungus veikiančias dirbtinio intelekto galimybes, kurios veikia be interneto ryšio  
- Valdyti modelių gyvavimo ciklus ir atnaujinimus gamybos aplinkoje  

**Windows ML diegimas**  
- Integruoti pasirinktinius ONNX modelius į Windows programas naudojant Windows ML  
- Pasinaudoti automatiniu aparatūros pagreičiu CPU, GPU ir NPU architektūrose  
- Įgyvendinti realaus laiko inferenciją su optimaliu resursų panaudojimu  
- Kurti mastelio keičiamas dirbtinio intelekto programas įvairiems Windows įrenginių tipams  

### Programų kūrimo įgūdžiai

**Kryžminės platformos Windows kūrimas**  
- Kurti dirbtinio intelekto programas naudojant .NET MAUI universaliam Windows diegimui  
- Integruoti dirbtinio intelekto galimybes į Win32, UWP ir progresyvias interneto programas  
- Įgyvendinti prisitaikančius UI dizainus, kurie reaguoja į dirbtinio intelekto apdorojimo būsenas  
- Tvarkyti asinchronines dirbtinio intelekto operacijas laikantis tinkamų vartotojo patirties modelių  

**Našumo optimizavimas**  
- Profiluoti ir optimizuoti dirbtinio intelekto inferencijos našumą skirtingose aparatūros konfigūracijose  
- Įgyvendinti efektyvų atminties valdymą dideliems kalbos modeliams  
- Kurti programas, kurios grakščiai prisitaiko prie turimų aparatūros galimybių  
- Taikyti talpyklos strategijas dažnai naudojamoms dirbtinio intelekto operacijoms  

**Paruošimas gamybai**  
- Įgyvendinti išsamų klaidų tvarkymą ir atsargines mechanizmus  
- Kurti telemetriją ir stebėjimą dirbtinio intelekto programų našumui  
- Taikyti saugumo geriausią praktiką vietiniam dirbtinio intelekto modelių saugojimui ir vykdymui  
- Planuoti diegimo strategijas verslo ir vartotojų programoms  

### Verslo ir strateginis supratimas

**Dirbtinio intelekto programų architektūra**  
- Kurti hibridines architektūras, kurios optimizuoja vietinį ir debesų dirbtinio intelekto apdorojimą  
- Vertinti kompromisus tarp modelio dydžio, tikslumo ir inferencijos greičio  
- Planuoti duomenų srautų architektūras, kurios užtikrina privatumą ir intelektą  
- Įgyvendinti ekonomiškai efektyvius dirbtinio intelekto sprendimus, kurie plečiasi pagal vartotojų poreikius  

**Rinkos pozicionavimas**  
- Suprasti Windows gimtųjų dirbtinio intelekto programų konkurencinius pranašumus  
- Identifikuoti naudojimo atvejus, kur vietinis dirbtinis intelektas suteikia pranašesnę vartotojo patirtį  
- Kurti rinkos strategijas dirbtinio intelekto praturtintoms Windows programoms  
- Pozicionuoti programas, kad jos pasinaudotų Windows ekosistemos privalumais  

## Windows AI Foundry platformos komponentai

### 1. Windows AI API

Windows AI API siūlo paruoštas naudoti dirbtinio intelekto galimybes, kurias palaiko vietiniai modeliai, optimizuoti efektyvumui ir našumui Copilot+ PC įrenginiuose, reikalaujant minimalios sąrankos.

#### Pagrindinės API kategorijos

**Phi Silica kalbos modelis**  
- Mažas, bet galingas kalbos modelis tekstų generavimui ir samprotavimui  
- Optimizuotas realaus laiko inferencijai su minimaliu energijos suvartojimu  
- Palaikymas pritaikymui naudojant LoRA technikas  
- Integracija su Windows semantine paieška ir žinių gavimu  

**Kompiuterinio matymo API**  
- **Teksto atpažinimas (OCR)**: Išgaukite tekstą iš vaizdų su dideliu tikslumu  
- **Vaizdų superrezoliucija**: Padidinkite vaizdų kokybę naudodami vietinius dirbtinio intelekto modelius  
- **Vaizdų segmentacija**: Identifikuokite ir atskirkite konkrečius objektus vaizduose  
- **Vaizdų aprašymas**: Generuokite detalius tekstinius aprašymus vizualiniam turiniui  
- **Objektų šalinimas**: Pašalinkite nereikalingus objektus iš vaizdų naudodami dirbtinio intelekto pagrindu veikiančią inpainting technologiją  

**Multimodalinės galimybės**  
- **Vaizdų ir teksto integracija**: Sujunkite teksto ir vaizdų supratimą  
- **Semantinė paieška**: Įgalinkite natūralios kalbos užklausas multimedijos turiniui  
- **Žinių gavimas**: Kurkite išmanias paieškos patirtis su vietiniais duomenimis  

### 2. Foundry Local

Foundry Local suteikia kūrėjams greitą prieigą prie paruoštų naudoti atvirojo kodo kalbos modelių Windows Silicon, siūlydamas galimybę naršyti, testuoti, sąveikauti ir diegti modelius vietinėse programose.

#### Pagrindinės funkcijos

**Modelių katalogas**  
- Išsamus iš anksto optimizuotų atvirojo kodo modelių rinkinys  
- Modeliai optimizuoti CPU, GPU ir NPU, paruošti nedelsiant diegti  
- Palaikymas populiarioms modelių šeimoms, įskaitant Llama, Mistral, Phi ir specializuotus domenų modelius  

**CLI integracija**  
- Komandinės eilutės sąsaja modelių valdymui ir diegimui  
- Automatiniai optimizavimo ir kvantizavimo darbo srautai  
- Integracija su populiariomis kūrimo aplinkomis ir CI/CD procesais  

**Vietinis diegimas**  
- Pilnas neprisijungus veikimas be debesų priklausomybių  
- Palaikymas pasirinktiniams modelių formatams ir konfigūracijoms  
- Efektyvus modelių aptarnavimas su automatiniu aparatūros optimizavimu  

### 3. Windows ML

Windows ML yra pagrindinė dirbtinio intelekto platforma ir integruota inferencijos vykdymo aplinka Windows, leidžianti kūrėjams efektyviai diegti pasirinktinius modelius visoje Windows aparatūros ekosistemoje.

#### Architektūros privalumai

**Universalus aparatūros palaikymas**  
- Automatinė optimizacija AMD, Intel, NVIDIA ir Qualcomm lustams  
- Palaikymas CPU, GPU ir NPU vykdymui su skaidriu perjungimu  
- Aparatūros abstrakcija, pašalinanti platformai specifinį optimizavimo darbą  

**Modelių lankstumas**  
- Palaikymas ONNX modelio formatui su automatiniu konvertavimu iš populiarių sistemų  
- Pasirinktinių modelių diegimas su gamybos lygio našumu  
- Integracija su esamomis Windows programų architektūromis  

**Verslo integracija**  
- Suderinamumas su Windows saugumo ir atitikties sistemomis  
- Palaikymas verslo diegimo ir valdymo įrankiams  
- Integracija su Windows įrenginių valdymo ir stebėjimo sistemomis  

## Kūrimo darbo eiga

### 1 etapas: Aplinkos paruošimas ir įrankių konfigūracija

**Kūrimo aplinkos paruošimas**  
1. Įdiekite Visual Studio su AI Toolkit plėtiniu  
2. Konfigūruokite Windows AI Foundry CLI įrankius  
3. Nustatykite vietinę modelių testavimo aplinką  
4. Įdiekite našumo profiliavimo ir stebėjimo įrankius  

**AI Dev Gallery tyrinėjimas**  
- Naršykite pavyzdines programas ir nuorodines implementacijas  
- Testuokite Windows AI API su interaktyviais demonstraciniais pavyzdžiais  
- Peržiūrėkite šaltinio kodą, kad sužinotumėte geriausią praktiką ir modelius  
- Identifikuokite aktualius pavyzdžius savo konkrečiam naudojimo atvejui  

### 2 etapas: Modelio pasirinkimas ir integracija

**Reikalavimų analizė**  
- Apibrėžkite funkcinius reikalavimus dirbtinio intelekto galimybėms  
- Nustatykite našumo apribojimus ir optimizavimo tikslus  
- Įvertinkite privatumo ir saugumo reikalavimus  
- Planuokite diegimo architektūrą ir mastelio keitimo strategijas  

**Modelio vertinimas**  
- Naudokite Foundry Local, kad testuotumėte atvirojo kodo modelius savo naudojimo atvejui  
- Lyginkite Windows AI API su pasirinktinių modelių reikalavimais  
- Įvertinkite kompromisus tarp modelio dydžio, tikslumo ir inferencijos greičio  
- Prototipuokite integracijos metodus su pasirinktais modeliais  

### 3 etapas: Programos kūrimas

**Pagrindinė integracija**  
- Įgyvendinkite Windows AI API integraciją su tinkamu klaidų tvarkymu  
- Kurkite vartotojo sąsajas, kurios prisitaiko prie dirbtinio intelekto apdorojimo darbo srautų  
- Įgyvendinkite talpyklos ir optimizavimo strategijas modelio inferencijai  
- Pridėkite telemetriją ir stebėjimą dirbtinio intelekto operacijų našumui  

**Testavimas ir validacija**  
- Testuokite programas skirtingose Windows aparatūros konfigūracijose  
- Patvirtinkite našumo metrikas įvairiomis apkrovos sąlygomis  
- Įgyvendinkite automatizuotą testavimą dirbtinio intelekto funkcionalumo patikimumui  
- Vykdykite vartotojo patirties testavimą su dirbtinio intelekto praturtintomis funkcijomis  

### 4 etapas: Optimizavimas ir diegimas

**Našumo optimizavimas**  
- Profiluoti programos našumą skirtingose tikslinėse aparatūros konfigūracijose  
- Optimizuoti atminties naudojimą ir modelio įkėlimo strategijas  
- Įgyvendinti adaptacinį elgesį pagal turimas aparatūros galimybes  
- Pritaikyti vartotojo patirtį skirtingiems našumo scenarijams  

**Gamybos diegimas**  
- Supakuokite programas su tinkamomis dirbtinio intelekto modelių priklausomybėmis  
- Įgyvendinkite atnaujinimo mechanizmus modeliams ir programos logikai  
- Konfigūruokite stebėjimą ir analizę gamybos aplinkoms  
- Planuokite diegimo strategijas verslo ir vartotojų aplinkoms  

## Praktiniai įgyvendinimo pavyzdžiai

### Pavyzdys 1: Išmanioji dokumentų apdorojimo programa

Sukurkite Windows programą, kuri apdoroja dokumentus naudodama kelias dirbtinio intelekto galimybes:

**Naudotos technologijos:**  
- Phi Silica dokumentų santraukų ir klausimų-atsakymų funkcijoms  
- OCR API tekstų išgavimo iš nuskaitytų dokumentų funkcijoms  
- Vaizdų aprašymo API diagramų ir grafikų analizei  
- Pasirinktiniai ONNX modeliai dokumentų klasifikavimui  

**Įgyvendinimo metodas:**  
- Kurkite modulinę architektūrą su prijungiamais dirbtinio intelekto komponentais  
- Įgyvendinkite asinchroninį apdorojimą didelėms dokumentų partijoms  
- Pridėkite progreso indikatorius ir atšaukimo palaikymą ilgai trunkančioms operacijoms  
- Įtraukite neprisijungus veikiančią funkciją jautrių dokumentų apdorojimui  

### Pavyzdys 2: Mažmeninės prekybos inventoriaus valdymo sistema

Sukurkite dirbtinio intelekto pagrindu veikiančią inventoriaus sistemą mažmeninės prekybos programoms:

**Naudotos technologijos:**  
- Vaizdų segmentacija produktų identifikavimui  
- Pasirinktiniai vizualiniai modeliai prekės ženklo ir kategorijos klasifikavimui  
- Foundry Local specializuotų mažmeninės prekybos kalbos modelių diegimui  
- Integracija su esamomis POS ir inventoriaus sistemomis  

**Įgyvendinimo metodas:**  
- Sukurkite kamerų integraciją realaus laiko produktų skenavimui  
- Įgyvendinkite brūkšninių kodų ir vizualinį produktų atpažinimą  
- Pridėkite natūralios
- Naudokite Foundry Local CLI modelių testavimui ir validavimui
- Pasitelkite Windows AI API testavimo įrankius integracijos patikrinimui
- Įgyvendinkite individualų logavimą AI operacijų stebėjimui
- Sukurkite automatizuotą testavimą AI funkcionalumo patikimumui užtikrinti

## Ateities užtikrinimas jūsų programoms

### Naujos technologijos

**Kitos kartos aparatinė įranga**
- Kurkite programas, kurios išnaudoja būsimus NPU pajėgumus
- Planuokite didesnius modelių dydžius ir sudėtingumą
- Įgyvendinkite prisitaikančias architektūras, pritaikytas besikeičiančiai aparatinei įrangai
- Apsvarstykite kvantinius algoritmus, kad užtikrintumėte ateities suderinamumą

**Pažangios AI galimybės**
- Pasiruoškite multimodalinės AI integracijai su daugiau duomenų tipų
- Planuokite realaus laiko bendradarbiavimo AI tarp kelių įrenginių
- Kurkite federacinio mokymosi galimybes
- Apsvarstykite hibridines edge-cloud intelekto architektūras

### Nuolatinis mokymasis ir prisitaikymas

**Modelių atnaujinimai**
- Įgyvendinkite sklandžius modelių atnaujinimo mechanizmus
- Kurkite programas, kurios prisitaiko prie patobulintų modelių galimybių
- Planuokite atgalinį suderinamumą su esamais modeliais
- Įgyvendinkite A/B testavimą modelių našumo vertinimui

**Funkcijų evoliucija**
- Kurkite modulinės architektūros, kurios leidžia integruoti naujas AI galimybes
- Planuokite naujų Windows AI API integraciją
- Įgyvendinkite funkcijų vėliavėles palaipsniui diegiamoms galimybėms
- Kurkite vartotojo sąsajas, kurios prisitaiko prie patobulintų AI funkcijų

## Išvada

Windows Edge AI kūrimas atspindi galingų AI galimybių susiliejimą su patikima, saugia ir mastelio keičiamą Windows platforma. Įvaldę Windows AI Foundry ekosistemą, kūrėjai gali kurti intelektualias programas, kurios suteikia išskirtinę vartotojo patirtį, išlaikant aukščiausius privatumo, saugumo ir našumo standartus.

Windows AI API, Foundry Local ir Windows ML derinys suteikia neprilygstamą pagrindą kurti naujos kartos intelektualias Windows programas. Kadangi AI toliau vystosi, Windows platforma užtikrina, kad jūsų programos prisitaikys prie naujų technologijų, išlaikant suderinamumą ir našumą įvairioje Windows aparatūros ekosistemoje.

Nesvarbu, ar kuriate vartotojų programas, verslo sprendimus, ar specializuotus pramonės įrankius, Windows Edge AI kūrimas suteikia galimybę kurti intelektualias, reaguojančias ir giliai integruotas patirtis, kurios išnaudoja visą modernių Windows įrenginių potencialą.

## Papildomi ištekliai

Norėdami gauti žingsnis po žingsnio Windows Foundry Local vadovą (instaliacija, CLI, dinaminiai galiniai taškai, SDK naudojimas), žiūrėkite repo vadovą: [foundrylocal.md](./foundrylocal.md).

### Dokumentacija ir mokymasis
- [Windows AI Foundry dokumentacija](https://learn.microsoft.com/windows/ai/)
- [Windows AI API nuoroda](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local pradžia](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML apžvalga](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Kūrimo įrankiai
- [AI įrankių rinkinys Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI kūrėjų galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI pavyzdžiai](https://learn.microsoft.com/windows/ai/samples/)

### Bendruomenė ir palaikymas
- [Windows kūrėjų bendruomenė](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry tinklaraštis](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI mokymai](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Šis vadovas sukurtas taip, kad evoliucionuotų kartu su sparčiai besivystančia Windows AI ekosistema. Reguliarūs atnaujinimai užtikrina suderinamumą su naujausiomis platformos galimybėmis ir geriausia kūrimo praktika.*

---

