<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ec2b092ed161fd4d3907e010f8cf544",
  "translation_date": "2025-09-19T02:02:36+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "lt"
}
-->
# Windows Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į Windows Edge AI kūrimą – išsamų vadovą, padėsiantį kurti išmaniąsias programas, kurios pasitelkia įrenginiuose veikiančią dirbtinio intelekto galią, naudojant Microsoft Windows AI Foundry platformą. Šis vadovas skirtas Windows kūrėjams, norintiems integruoti pažangias Edge AI galimybes į savo programas, pasinaudojant visapusišku Windows aparatinės įrangos pagreičiu.

### Windows AI privalumai

Windows AI Foundry yra vieninga, patikima ir saugi platforma, palaikanti visą dirbtinio intelekto kūrėjų ciklą – nuo modelio pasirinkimo ir tobulinimo iki optimizavimo ir diegimo CPU, GPU, NPU ir hibridiniuose debesų architektūrose. Ši platforma demokratizuoja dirbtinio intelekto kūrimą, siūlydama:

- **Aparatinės įrangos abstrakciją**: Sklandus diegimas AMD, Intel, NVIDIA ir Qualcomm lustuose
- **Vietinis intelektas**: Privatumo užtikrinantis dirbtinis intelektas, veikiantis tik vietinėje aparatinėje įrangoje
- **Optimizuotas našumas**: Modeliai, iš anksto optimizuoti Windows aparatinės įrangos konfigūracijoms
- **Paruošta verslui**: Gamybinio lygio saugumo ir atitikties funkcijos

### Kodėl Windows Edge AI?

**Universalus aparatinės įrangos palaikymas**  
Windows ML automatiškai optimizuoja aparatinę įrangą visoje Windows ekosistemoje, užtikrindama, kad jūsų dirbtinio intelekto programos veiktų optimaliai, nepriklausomai nuo pagrindinės lustų architektūros.

**Integruotas AI vykdymo variklis**  
Įmontuotas Windows ML inferencijos variklis pašalina sudėtingus nustatymo reikalavimus, leidžiant kūrėjams susitelkti į programos logiką, o ne infrastruktūros problemas.

**Copilot+ PC optimizacija**  
Specialiai sukurti API, skirti naujos kartos Windows įrenginiams su dedikuotais neuroniniais procesoriais (NPU), užtikrinantys išskirtinį našumą per vatą.

**Kūrėjų ekosistema**  
Platus įrankių pasirinkimas, įskaitant Visual Studio integraciją, išsamią dokumentaciją ir pavyzdines programas, kurios pagreitina kūrimo ciklus.

## Mokymosi tikslai

Baigę šį Windows Edge AI kūrimo vadovą, įgysite esminių įgūdžių, reikalingų gamybai paruoštų dirbtinio intelekto programų kūrimui Windows platformoje.

### Pagrindinės techninės kompetencijos

**Windows AI Foundry įvaldymas**  
- Suprasti Windows AI Foundry platformos architektūrą ir komponentus  
- Naršyti visą dirbtinio intelekto kūrimo ciklą Windows ekosistemoje  
- Įgyvendinti saugumo geriausią praktiką vietinėms dirbtinio intelekto programoms  
- Optimizuoti programas skirtingoms Windows aparatinės įrangos konfigūracijoms  

**API integracijos ekspertizė**  
- Įvaldyti Windows AI API tekstui, vaizdams ir multimodalinėms programoms  
- Įgyvendinti Phi Silica kalbos modelio integraciją tekstų generavimui ir samprotavimui  
- Diegti kompiuterinio matymo galimybes naudojant įmontuotus vaizdų apdorojimo API  
- Pritaikyti iš anksto apmokytus modelius naudojant LoRA (žemos rango adaptacijos) technikas  

**Foundry Local įgyvendinimas**  
- Naršyti, vertinti ir diegti atvirojo kodo kalbos modelius naudojant Foundry Local CLI  
- Suprasti modelių optimizavimą ir kvantizaciją vietiniam diegimui  
- Įgyvendinti neprisijungus veikiančias dirbtinio intelekto galimybes, kurios veikia be interneto ryšio  
- Valdyti modelių gyvavimo ciklus ir atnaujinimus gamybos aplinkoje  

**Windows ML diegimas**  
- Integruoti pasirinktinius ONNX modelius į Windows programas naudojant Windows ML  
- Pasinaudoti automatiniu aparatinės įrangos pagreičiu CPU, GPU ir NPU architektūrose  
- Įgyvendinti realaus laiko inferenciją su optimaliu resursų panaudojimu  
- Kurti mastelio keičiamas dirbtinio intelekto programas įvairioms Windows įrenginių kategorijoms  

### Programų kūrimo įgūdžiai

**Kryžminės platformos Windows kūrimas**  
- Kurti dirbtinio intelekto programas naudojant .NET MAUI universaliam Windows diegimui  
- Integruoti dirbtinio intelekto galimybes į Win32, UWP ir progresyvias interneto programas  
- Įgyvendinti prisitaikančius UI dizainus, kurie prisitaiko prie dirbtinio intelekto apdorojimo būsenų  
- Tvarkyti asinchronines dirbtinio intelekto operacijas su tinkamais vartotojo patirties modeliais  

**Našumo optimizavimas**  
- Profiluoti ir optimizuoti dirbtinio intelekto inferencijos našumą skirtingose aparatinės įrangos konfigūracijose  
- Įgyvendinti efektyvų atminties valdymą dideliems kalbos modeliams  
- Kurti programas, kurios grakščiai prisitaiko prie turimos aparatinės įrangos galimybių  
- Taikyti talpyklos strategijas dažnai naudojamoms dirbtinio intelekto operacijoms  

**Paruošimas gamybai**  
- Įgyvendinti išsamų klaidų tvarkymą ir atsargines mechanizmus  
- Kurti telemetriją ir stebėjimą dirbtinio intelekto programų našumui  
- Taikyti saugumo geriausią praktiką vietiniam dirbtinio intelekto modelių saugojimui ir vykdymui  
- Planuoti diegimo strategijas verslo ir vartotojų programoms  

### Verslo ir strateginis supratimas

**Dirbtinio intelekto programų architektūra**  
- Kurti hibridines architektūras, optimizuojančias vietinį ir debesų dirbtinio intelekto apdorojimą  
- Vertinti kompromisus tarp modelio dydžio, tikslumo ir inferencijos greičio  
- Planuoti duomenų srautų architektūras, kurios užtikrina privatumą ir intelektą  
- Įgyvendinti ekonomiškai efektyvius dirbtinio intelekto sprendimus, kurie plečiasi pagal vartotojų poreikius  

**Rinkos pozicionavimas**  
- Suprasti Windows gimtųjų dirbtinio intelekto programų konkurencinius pranašumus  
- Identifikuoti naudojimo atvejus, kur vietinis dirbtinis intelektas suteikia pranašesnę vartotojo patirtį  
- Kurti rinkos strategijas dirbtinio intelekto praturtintoms Windows programoms  
- Pozicionuoti programas, kad pasinaudotų Windows ekosistemos privalumais  

## Windows AI Foundry platformos komponentai

### 1. Windows AI API

Windows AI API siūlo paruoštas naudoti dirbtinio intelekto galimybes, paremtas vietiniais modeliais, optimizuotais efektyvumui ir našumui Copilot+ PC įrenginiuose, su minimaliu nustatymu.

#### Pagrindinės API kategorijos

**Phi Silica kalbos modelis**  
- Mažas, bet galingas kalbos modelis tekstų generavimui ir samprotavimui  
- Optimizuotas realaus laiko inferencijai su minimaliu energijos suvartojimu  
- Palaikymas pritaikymui naudojant LoRA technikas  
- Integracija su Windows semantine paieška ir žinių gavimu  

**Kompiuterinio matymo API**  
- **Teksto atpažinimas (OCR)**: Tikslus teksto išgavimas iš vaizdų  
- **Vaizdų superrezoliucija**: Vaizdų kokybės gerinimas naudojant vietinius dirbtinio intelekto modelius  
- **Vaizdų segmentacija**: Specifinių objektų identifikavimas ir atskyrimas vaizduose  
- **Vaizdų aprašymas**: Detalių tekstinių aprašymų generavimas vizualiniam turiniui  
- **Objektų šalinimas**: Nepageidaujamų objektų pašalinimas iš vaizdų naudojant dirbtinio intelekto įrankius  

**Multimodalinės galimybės**  
- **Vaizdų ir teksto integracija**: Teksto ir vaizdų supratimo derinimas  
- **Semantinė paieška**: Natūralios kalbos užklausos multimedijos turiniui  
- **Žinių gavimas**: Intelektualių paieškos patirčių kūrimas naudojant vietinius duomenis  

### 2. Foundry Local

Foundry Local suteikia kūrėjams greitą prieigą prie paruoštų naudoti atvirojo kodo kalbos modelių Windows Silicon, siūlydamas galimybę naršyti, testuoti, sąveikauti ir diegti modelius vietinėse programose.

#### Pagrindinės funkcijos

**Modelių katalogas**  
- Išsamus iš anksto optimizuotų atvirojo kodo modelių rinkinys  
- Modeliai optimizuoti CPU, GPU ir NPU, paruošti nedelsiant diegti  
- Palaikymas populiarioms modelių šeimoms, įskaitant Llama, Mistral, Phi ir specializuotus modelius  

**CLI integracija**  
- Komandinės eilutės sąsaja modelių valdymui ir diegimui  
- Automatiniai optimizavimo ir kvantizacijos procesai  
- Integracija su populiariomis kūrimo aplinkomis ir CI/CD procesais  

**Vietinis diegimas**  
- Visiškai neprisijungus veikianti operacija be debesų priklausomybių  
- Palaikymas pasirinktiniams modelių formatams ir konfigūracijoms  
- Efektyvus modelių aptarnavimas su automatiniu aparatinės įrangos optimizavimu  

### 3. Windows ML

Windows ML yra pagrindinė dirbtinio intelekto platforma ir integruotas inferencijos vykdymo variklis Windows, leidžiantis kūrėjams efektyviai diegti pasirinktinius modelius visoje Windows aparatinės įrangos ekosistemoje.

#### Architektūros privalumai

**Universalus aparatinės įrangos palaikymas**  
- Automatinė optimizacija AMD, Intel, NVIDIA ir Qualcomm lustams  
- Palaikymas CPU, GPU ir NPU vykdymui su skaidriu perjungimu  
- Aparatinės įrangos abstrakcija, pašalinanti platformos specifinio optimizavimo poreikį  

**Modelių lankstumas**  
- Palaikymas ONNX modelio formatui su automatiniu konvertavimu iš populiarių sistemų  
- Pasirinktinių modelių diegimas su gamybos lygio našumu  
- Integracija su esamomis Windows programų architektūromis  

**Verslo integracija**  
- Suderinamumas su Windows saugumo ir atitikties sistemomis  
- Palaikymas verslo diegimo ir valdymo įrankiams  
- Integracija su Windows įrenginių valdymo ir stebėjimo sistemomis  


- Naudokite Foundry Local CLI modelių testavimui ir validavimui  
- Pasinaudokite Windows AI API testavimo įrankiais integracijos patikrinimui  
- Įgyvendinkite individualų logavimą AI operacijų stebėjimui  
- Sukurkite automatizuotus testus AI funkcionalumo patikimumui  

## Ateities užtikrinimas jūsų programoms  

### Naujos technologijos  

**Naujos kartos aparatinė įranga**  
- Kurkite programas, kurios išnaudoja būsimas NPU galimybes  
- Planuokite didesnius modelių dydžius ir sudėtingumą  
- Įgyvendinkite adaptyvias architektūras, pritaikytas besikeičiančiai aparatinės įrangos aplinkai  
- Apsvarstykite kvantinius algoritmus, kad užtikrintumėte suderinamumą ateityje  

**Pažangios AI galimybės**  
- Pasiruoškite multimodalinės AI integracijai su daugiau duomenų tipų  
- Planuokite realaus laiko bendradarbiavimo AI tarp kelių įrenginių  
- Kurkite federacinio mokymosi galimybes  
- Apsvarstykite edge-cloud hibridinės intelektinės architektūros dizainą  

### Nuolatinis mokymasis ir prisitaikymas  

**Modelių atnaujinimai**  
- Įgyvendinkite sklandžius modelių atnaujinimo mechanizmus  
- Kurkite programas, kurios prisitaiko prie patobulintų modelių galimybių  
- Planuokite atgalinį suderinamumą su esamais modeliais  
- Įgyvendinkite A/B testavimą modelių našumo vertinimui  

**Funkcijų evoliucija**  
- Kurkite modulinės architektūros dizainą, kuris leidžia integruoti naujas AI galimybes  
- Planuokite naujų Windows AI API integraciją  
- Įgyvendinkite funkcijų vėliavėles palaipsniui diegiant galimybes  
- Kurkite vartotojo sąsajas, kurios prisitaiko prie patobulintų AI funkcijų  

## Išvada  

Windows Edge AI kūrimas atspindi galingų AI galimybių susiliejimą su patikima, saugia ir mastelio keičiamą Windows platforma. Įvaldę Windows AI Foundry ekosistemą, kūrėjai gali kurti intelektualias programas, kurios užtikrina išskirtinę vartotojo patirtį, išlaikant aukščiausius privatumo, saugumo ir našumo standartus.  

Windows AI API, Foundry Local ir Windows ML derinys suteikia neprilygstamą pagrindą kurti naujos kartos intelektualias Windows programas. Kadangi AI toliau vystosi, Windows platforma užtikrina, kad jūsų programos prisitaikys prie naujų technologijų, išlaikydamos suderinamumą ir našumą įvairioje Windows aparatinės įrangos ekosistemoje.  

Nesvarbu, ar kuriate vartotojų programas, verslo sprendimus, ar specializuotus pramonės įrankius, Windows Edge AI kūrimas suteikia galimybę kurti intelektualias, reaguojančias ir giliai integruotas patirtis, kurios išnaudoja visą modernių Windows įrenginių potencialą.  

## Papildomi ištekliai  

### Dokumentacija ir mokymasis  
- [Windows AI Foundry Dokumentacija](https://learn.microsoft.com/windows/ai/)  
- [Windows AI API Nuoroda](https://learn.microsoft.com/windows/ai/apis/)  
- [Foundry Local Pradžia](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Windows ML Apžvalga](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  

### Kūrimo įrankiai  
- [AI Įrankių rinkinys Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)  
- [AI Kūrėjų galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)  
- [Windows AI Pavyzdžiai](https://learn.microsoft.com/windows/ai/samples/)  

### Bendruomenė ir palaikymas  
- [Windows Kūrėjų Bendruomenė](https://developer.microsoft.com/en-us/windows/)  
- [Windows AI Foundry Tinklaraštis](https://blogs.windows.com/windowsdeveloper/)  
- [Microsoft Learn AI Mokymai](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)  

---  

*Šis vadovas sukurtas taip, kad evoliucionuotų kartu su sparčiai besivystančia Windows AI ekosistema. Reguliarūs atnaujinimai užtikrina suderinamumą su naujausiomis platformos galimybėmis ir geriausiomis kūrimo praktikomis.*  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.