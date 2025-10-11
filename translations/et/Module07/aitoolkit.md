<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-11T12:36:07+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "et"
}
-->
# AI Toolkit for Visual Studio Code - Edge AI Arenduse Juhend

## Sissejuhatus

Tere tulemast põhjalikku juhendisse, kuidas kasutada AI Toolkit'i Visual Studio Code'is Edge AI arendamiseks. Kuna tehisintellekt liigub tsentraliseeritud pilvearvutustest hajutatud servaseadmetele, vajavad arendajad võimsaid ja integreeritud tööriistu, mis suudavad toime tulla serva juurutamise unikaalsete väljakutsetega – alates ressursipiirangutest kuni võrguühenduseta töö nõueteni.

AI Toolkit Visual Studio Code'ile täidab selle tühimiku, pakkudes terviklikku arenduskeskkonda, mis on spetsiaalselt loodud AI-rakenduste loomiseks, testimiseks ja optimeerimiseks, et need töötaksid tõhusalt servaseadmetel. Olenemata sellest, kas arendate IoT-sensorite, mobiilseadmete, manussüsteemide või servaserverite jaoks, lihtsustab see tööriistakomplekt kogu teie arendustöövoogu tuttavas VS Code'i keskkonnas.

See juhend viib teid läbi oluliste kontseptsioonide, tööriistade ja parimate tavade, et kasutada AI Toolkit'i oma Edge AI projektides – alates mudeli valikust kuni tootmisesse juurutamiseni.

## Ülevaade

AI Toolkit Visual Studio Code'ile on võimas laiendus, mis lihtsustab agentide arendamist ja AI-rakenduste loomist. Tööriistakomplekt pakub laiaulatuslikke võimalusi AI-mudelite uurimiseks, hindamiseks ja juurutamiseks erinevatelt pakkujatelt – sealhulgas Anthropic, OpenAI, GitHub, Google – ning toetab kohalike mudelite käitamist ONNX-i ja Ollama abil.

Mis eristab AI Toolkit'i, on selle terviklik lähenemine kogu AI arendustsüklile. Erinevalt traditsioonilistest AI arendustööriistadest, mis keskenduvad üksikutele aspektidele, pakub AI Toolkit integreeritud keskkonda, mis hõlmab mudelite avastamist, katsetamist, agentide arendamist, hindamist ja juurutamist – kõik see tuttavas VS Code'i keskkonnas.

Platvorm on spetsiaalselt loodud kiireks prototüüpimiseks ja tootmisesse juurutamiseks, pakkudes selliseid funktsioone nagu promptide genereerimine, kiirstardid, sujuvad MCP (Model Context Protocol) tööriistade integreerimised ja ulatuslikud hindamisvõimalused. Edge AI arenduse jaoks tähendab see, et saate tõhusalt arendada, testida ja optimeerida AI-rakendusi serva juurutamise stsenaariumide jaoks, säilitades samal ajal kogu arendustöövoo VS Code'is.

## Õpieesmärgid

Selle juhendi lõpuks suudate:

### Põhioskused
- **Installida ja seadistada** AI Toolkit Visual Studio Code'is Edge AI arendustöövoogude jaoks
- **Navigeerida ja kasutada** AI Toolkit'i liidest, sealhulgas Model Catalog, Playground ja Agent Builder
- **Valida ja hinnata** AI-mudeleid, mis sobivad serva juurutamiseks, arvestades jõudlust ja ressursipiiranguid
- **Mudeleid teisendada ja optimeerida** ONNX-formaati ja kvantiseerimistehnikaid kasutades servaseadmete jaoks

### Edge AI arenduse oskused
- **Kavandada ja rakendada** Edge AI rakendusi integreeritud arenduskeskkonnas
- **Testida mudeleid** servasarnastes tingimustes, kasutades kohalikku järeldamist ja ressursijälgimist
- **Luua ja kohandada** AI-agente, mis on optimeeritud serva juurutamise stsenaariumide jaoks
- **Hinnata mudelite jõudlust** servaarvutusele oluliste mõõdikute abil (latentsus, mälukasutus, täpsus)

### Optimeerimine ja juurutamine
- **Rakendada kvantiseerimist ja kärpimist**, et vähendada mudeli suurust, säilitades samal ajal vastuvõetava jõudluse
- **Optimeerida mudeleid** konkreetsete serva riistvaraplatvormide jaoks, sealhulgas CPU, GPU ja NPU kiirendus
- **Rakendada parimaid tavasid** Edge AI arenduses, sealhulgas ressursihaldus ja varuplaanid
- **Valmistada mudeleid ja rakendusi** tootmisesse juurutamiseks servaseadmetel

### Täiustatud Edge AI kontseptsioonid
- **Integreerida serva AI raamistikud**, sealhulgas ONNX Runtime, Windows ML ja TensorFlow Lite
- **Rakendada mitme mudeli arhitektuure** ja föderatiivse õppe stsenaariume servakeskkondades
- **Lahendada levinud Edge AI probleeme**, sealhulgas mälupiirangud, järeldamiskiirus ja riistvara ühilduvus
- **Kavandada monitooringu ja logimise strateegiaid** Edge AI rakenduste jaoks tootmises

### Praktiline rakendus
- **Luua otsast lõpuni Edge AI lahendusi**, alates mudeli valikust kuni juurutamiseni
- **Näidata oskusi** servaspetsiifilistes arendustöövoogudes ja optimeerimistehnikates
- **Rakendada õpitud kontseptsioone** reaalsetes Edge AI kasutusjuhtudes, sealhulgas IoT, mobiil- ja manusrakendustes
- **Hinnata ja võrrelda** erinevaid Edge AI juurutamisstrateegiaid ja nende kompromisse

## Peamised funktsioonid Edge AI arenduseks

### 1. Mudelikataloog ja avastamine
- **Mitme pakkuja tugi**: Sirvige ja pääsete ligi AI-mudelitele Anthropic, OpenAI, GitHub, Google ja teistelt pakkujatelt
- **Kohalike mudelite integreerimine**: ONNX-i ja Ollama mudelite lihtsustatud avastamine serva juurutamiseks
- **GitHubi mudelid**: Otsene integreerimine GitHubi mudelite hostimisega, et tagada sujuv juurdepääs
- **Mudelite võrdlus**: Võrrelge mudeleid kõrvuti, et leida optimaalne tasakaal servaseadmete piirangute jaoks

### 2. Interaktiivne Playground
- **Interaktiivne testimiskeskkond**: Kiire katsetamine mudelite võimalustega kontrollitud keskkonnas
- **Mitme modaalsuse tugi**: Testige pilte, teksti ja muid sisendeid, mis on tüüpilised servastsenaariumides
- **Reaalajas katsetamine**: Kohene tagasiside mudeli vastuste ja jõudluse kohta
- **Parameetrite optimeerimine**: Häälestage mudeli parameetreid serva juurutamise nõuete jaoks

### 3. Prompt (Agent) Builder
- **Loodusliku keele genereerimine**: Looge algsed promptid, kasutades looduskeele kirjeldusi
- **Iteratiivne täiustamine**: Parandage promptide kvaliteeti mudeli vastuste ja jõudluse põhjal
- **Ülesannete jaotamine**: Jagage keerulised ülesanded promptide ahelate ja struktureeritud väljundite abil
- **Muutujate tugi**: Kasutage promptides muutujaid dünaamilise agentide käitumise jaoks
- **Tootmiskoodi genereerimine**: Looge tootmiskõlblik kood kiireks rakenduste arendamiseks

### 4. Massiline testimine ja hindamine
- **Mitme mudeli testimine**: Käivitage mitu prompti valitud mudelitega samaaegselt
- **Tõhus testimine suurel skaalal**: Testige erinevaid sisendeid ja konfiguratsioone tõhusalt
- **Kohandatud testjuhtumid**: Käivitage agente testjuhtumitega, et valideerida funktsionaalsust
- **Jõudluse võrdlus**: Võrrelge tulemusi erinevate mudelite ja konfiguratsioonide vahel

### 5. Mudelite hindamine andmekogumitega
- **Standardmõõdikud**: Testige AI-mudeleid sisseehitatud hindajatega (F1-skoor, asjakohasus, sarnasus, sidusus)
- **Kohandatud hindajad**: Looge oma hindamismõõdikud konkreetsete kasutusjuhtude jaoks
- **Andmekogumite integreerimine**: Testige mudeleid ulatuslike andmekogumite vastu
- **Jõudluse mõõtmine**: Kvantifitseerige mudelite jõudlust serva juurutamise otsuste tegemiseks

### 6. Peenhäälestamise võimalused
- **Mudelite kohandamine**: Kohandage mudeleid konkreetsete kasutusjuhtude ja valdkondade jaoks
- **Spetsialiseeritud kohandamine**: Kohandage mudeleid spetsialiseeritud valdkondade ja nõuete jaoks
- **Edge optimeerimine**: Häälestage mudeleid spetsiaalselt serva juurutamise piirangute jaoks
- **Valdkonnapõhine treenimine**: Looge mudeleid, mis on kohandatud konkreetsetele serva kasutusjuhtudele

### 7. MCP tööriistade integreerimine
- **Väliste tööriistade ühenduvus**: Ühendage agendid väliste tööriistadega Model Context Protocol serverite kaudu
- **Reaalsed toimingud**: Lubage agentidel pärida andmebaase, pääseda ligi API-dele või täita kohandatud loogikat
- **Olemasolevad MCP serverid**: Kasutage tööriistu käsurea (stdio) või HTTP (server-sent event) protokollide kaudu
- **Kohandatud MCP arendus**: Looge ja seadistage uusi MCP servereid testimiseks Agent Builder'is

### 8. Agentide arendus ja testimine
- **Funktsioonikutsumise tugi**: Lubage agentidel dünaamiliselt väliseid funktsioone kutsuda
- **Reaalajas integreerimise testimine**: Testige integreerimisi reaalajas jooksude ja tööriistade kasutamisega
- **Agentide versioonihaldus**: Versioonihaldus agentidele koos võrdlusvõimalustega hindamistulemuste jaoks
- **Silumine ja jälgimine**: Kohalik jälgimine ja silumine agentide arendamiseks

## Edge AI arenduse töövoog

### Faas 1: Mudelite avastamine ja valik
1. **Uurige mudelikataloogi**: Kasutage mudelikataloogi, et leida serva juurutamiseks sobivaid mudeleid
2. **Võrrelge jõudlust**: Hinnake mudeleid suuruse, täpsuse ja järeldamiskiiruse põhjal
3. **Testige kohapeal**: Kasutage Ollama või ONNX mudeleid, et testida kohapeal enne serva juurutamist
4. **Hinnake ressursinõudeid**: Määrake sihtservaseadmete mälu- ja arvutusvajadused

### Faas 2: Mudelite optimeerimine
1. **Teisendage ONNX-i**: Teisendage valitud mudelid ONNX-formaati serva ühilduvuse jaoks
2. **Rakendage kvantiseerimist**: Vähendage mudeli suurust INT8 või INT4 kvantiseerimise abil
3. **Riistvara optimeerimine**: Optimeerige sihtserva riistvara jaoks (ARM, x86, spetsiaalsed kiirendid)
4. **Jõudluse valideerimine**: Kontrollige, kas optimeeritud mudelid säilitavad vastuvõetava täpsuse

### Faas 3: Rakenduste arendus
1. **Agentide disain**: Kasutage Agent Builder'it, et luua servaoptimeeritud AI-agente
2. **Promptide inseneeria**: Arendage promptid, mis töötavad tõhusalt väiksemate servamudelitega
3. **Integreerimise testimine**: Testige agente simuleeritud servatingimustes
4. **Koodi genereerimine**: Looge tootmiskood, mis on optimeeritud serva juurutamiseks

### Faas 4: Hindamine ja testimine
1. **Massiline hindamine**: Testige mitmeid konfiguratsioone, et leida optimaalsed servaseaded
2. **Jõudluse profileerimine**: Analüüsige järeldamiskiirust, mälukasutust ja täpsust
3. **Serva simulatsioon**: Testige tingimustes, mis sarnanevad sihtserva juurutuskeskkonnaga
4. **Koormustestimine**: Hinnake jõudlust erinevate koormustingimuste all

### Faas 5: Juurutamise ettevalmistus
1. **Lõplik optimeerimine**: Rakendage lõplikud optimeerimised testitulemuste põhjal
2. **Juurutamise pakendamine**: Pakendage mudelid ja kood serva juurutamiseks
3. **Dokumentatsioon**: Dokumenteerige juurutamise nõuded ja konfiguratsioon
4. **Monitooringu seadistamine**: Valmistage ette monitooring ja logimine serva juurutamiseks

## Sihtgrupp Edge AI arenduseks

### Edge AI arendajad
- Rakenduste arendajad, kes loovad AI-toega servaseadmeid ja IoT-lahendusi
- Manussüsteemide arendajad, kes integreerivad AI-võimekust ressursipiirangutega seadmetesse
- Mobiiliarendajad, kes loovad seadmesiseseid AI-rakendusi nutitelefonidele ja tahvelarvutitele

### Edge AI insenerid
- AI-insenerid, kes optimeerivad mudeleid serva juurutamiseks ja haldavad järeldamistorusid
- DevOps-insenerid, kes juurutavad ja haldavad AI-mudeleid hajutatud servainfrastruktuuris
- Jõudlusinsenerid, kes optimeerivad AI-töökoormusi serva riistvarapiirangute jaoks

### Teadlased ja õpetajad
- AI-teadlased, kes arendavad tõhusaid mudeleid ja algoritme servaarvutuseks
- Õpetajad, kes õpetavad Edge AI kontseptsioone ja demonstreerivad optimeerimistehnikaid
- Õpilased, kes õpivad Edge AI juurutamise väljakutsete ja lahenduste kohta

## Edge AI kasutusjuhtumid

### Nutikad IoT-seadmed
- **Reaalajas pildituvastus**: Juurutage arvutinägemise mudeleid IoT-kaameratesse ja -anduritesse
- **Hääletöötlus**: Rakendage kõnetuvastust ja loomuliku keele töötlemist nutikõlarites
- **Ennetav hooldus**: Käitage anomaaliatuvastuse mudeleid tööstuslikes servaseadmetes
- **Keskkonnaseire**: Juurutage andurite andmeanalüüsi mudeleid keskkonnarakenduste jaoks

### Mobiili- ja manusrakendused
- **Seadmesisene tõlge**: Rakendage keele tõlkemudeleid, mis töötavad võrguühenduseta
- **Liitreaalsus**: Juurutage reaalajas objektituvastust ja jälgimist AR-rakenduste jaoks
- **Tervise jälgimine**: Käitage terviseanalüüsi mudeleid kantavates seadmetes ja meditsiiniseadmetes
- **Autonoomsed süsteemid**: Rakendage otsuste tegemise mudeleid droonides, robotites ja sõidukites

### Servaarvutuse infrastruktuur
- **Serva andmekeskused**: Juurutage AI-mudeleid serva andmekeskustes madala latentsusega rakenduste jaoks
- **CDN-i integreerimine**: Integreerige AI-töötlusvõimekus sisuedastusvõrkudesse
- **5G serv**: Kasutage 5G servaarvutust AI-toega rakenduste jaoks
- **Uduarvutus**: Rakendage AI-töötlust uduarvutuse keskkondades

## Paigaldamine ja seadistamine

### Laienduse paigaldamine
Paigaldage AI Toolkit'i laiendus otse Visual Studio Code Marketplace'ist:

**Laienduse ID**: `ms-windows-ai-studio.windows-ai-studio`

**Paigaldusmeetodid**:
1. **VS Code Marketplace**: Otsige laienduste vaates "AI Toolkit"
2. **Käsurida**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Otsene paigaldus**: Laadige alla [VS Code Marketplace'ist](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Eeltingimused Edge AI arenduseks
- **Visual Studio Code**: Soovitatav uusim versioon
- **Python-keskkond**: Python 
2. Loo algsed viiped loomuliku keele kirjelduste abil  
3. Itereeri ja täiusta viipeid mudeli vastuste põhjal  
4. Integreeri MCP tööriistad agentide võimekuse suurendamiseks  

#### Samm 3: Testimine ja hindamine  
1. Kasuta **Bulk Run** funktsiooni, et testida mitut viibet valitud mudelitega  
2. Käivita agendid testjuhtumitega, et valideerida funktsionaalsust  
3. Hinda täpsust ja jõudlust sisseehitatud või kohandatud mõõdikute abil  
4. Võrdle erinevaid mudeleid ja konfiguratsioone  

#### Samm 4: Peenhäälestus ja optimeerimine  
1. Kohanda mudeleid spetsiifilisteks äärejuhtumiteks  
2. Rakenda valdkonnapõhist peenhäälestust  
3. Optimeeri ääre seadmete piirangute jaoks  
4. Versiooni ja võrdle erinevaid agentide konfiguratsioone  

#### Samm 5: Juurutamise ettevalmistus  
1. Loo tootmisvalmis kood Agent Builderi abil  
2. Sea üles MCP serveri ühendused tootmiskasutuseks  
3. Valmista juurutuspaketid ääre seadmete jaoks  
4. Konfigureeri monitooringu ja hindamise mõõdikud  

## Parimad tavad ääre AI arendamiseks  

### Mudeli valik  
- **Suuruse piirangud**: Vali mudelid, mis mahuvad sihtseadmete mälupiirangutesse  
- **Järeldamise kiirus**: Eelista mudeleid, millel on kiire järeldamise aeg reaalajas rakenduste jaoks  
- **Täpsuse kompromissid**: Tasakaalusta mudeli täpsus ja ressursipiirangud  
- **Formaadiga ühilduvus**: Eelista ONNX-i või riistvarale optimeeritud formaate ääre juurutamiseks  

### Optimeerimistehnikad  
- **Kvantiseerimine**: Kasuta INT8 või INT4 kvantiseerimist, et vähendada mudeli suurust ja parandada kiirust  
- **Pügamine**: Eemalda mittevajalikud mudeliparameetrid, et vähendada arvutusvajadusi  
- **Teadmiste destilleerimine**: Loo väiksemaid mudeleid, mis säilitavad suuremate mudelite jõudluse  
- **Riistvarakiirendus**: Kasuta NPUsid, GPUsid või spetsiaalseid kiirendeid, kui need on saadaval  

### Arendustöövoog  
- **Iteratiivne testimine**: Testi arenduse ajal sageli ääre-sarnastes tingimustes  
- **Jõudluse monitooring**: Jälgi pidevalt ressursikasutust ja järeldamise kiirust  
- **Versioonihaldus**: Jälgi mudeli versioone ja optimeerimisseadeid  
- **Dokumentatsioon**: Dokumenteeri kõik optimeerimisotsused ja jõudluse kompromissid  

### Juurutamise kaalutlused  
- **Ressursside monitooring**: Jälgi mälu, CPU ja energiakasutust tootmises  
- **Tagavarastrateegiad**: Rakenda tagavaramehhanisme mudelite rikete korral  
- **Uuenduste mehhanismid**: Planeeri mudelite uuendused ja versioonihaldus  
- **Turvalisus**: Rakenda sobivaid turvameetmeid ääre AI rakenduste jaoks  

## Integreerimine ääre AI raamistikesse  

### ONNX Runtime  
- **Platvormideülene juurutamine**: Juuruta ONNX mudeleid erinevatel ääreplatvormidel  
- **Riistvaraline optimeerimine**: Kasuta ONNX Runtime'i riistvaraspetsiifilisi optimeerimisi  
- **Mobiilitoetus**: Kasuta ONNX Runtime Mobile'i nutitelefonide ja tahvelarvutite rakendustes  
- **IoT integratsioon**: Juuruta IoT seadmetele ONNX Runtime'i kergekaaluliste jaotustega  

### Windows ML  
- **Windowsi seadmed**: Optimeeri Windowsi-põhiste ääreseadmete ja arvutite jaoks  
- **NPU kiirendus**: Kasuta Neural Processing Units kiirendust Windowsi seadmetel  
- **DirectML**: Kasuta DirectML-i GPU kiirenduseks Windowsi platvormidel  
- **UWP integratsioon**: Integreeri Universal Windows Platformi rakendustega  

### TensorFlow Lite  
- **Mobiili optimeerimine**: Juuruta TensorFlow Lite mudeleid mobiili- ja manusseadmetele  
- **Riistvaradelegaadid**: Kasuta spetsiaalseid riistvaradelegaate kiirenduseks  
- **Mikrokontrollerid**: Juuruta mikrokontrolleritele TensorFlow Lite Micro abil  
- **Platvormideülene tugi**: Juuruta Androidi, iOS-i ja manustatud Linuxi süsteemidesse  

### Azure IoT Edge  
- **Pilve-ääre hübriid**: Kombineeri pilveõpe äärejäreldustega  
- **Moodulite juurutamine**: Juuruta AI mudeleid IoT Edge moodulitena  
- **Seadmehaldus**: Halda ääreseadmeid ja mudeliuuendusi kaugelt  
- **Telemeetria**: Kogu jõudlusandmeid ja mudelimõõdikuid ääre juurutustest  

## Täiustatud ääre AI stsenaariumid  

### Mitme mudeli juurutamine  
- **Mudelite ansamblid**: Juuruta mitu mudelit täpsuse parandamiseks või redundantsuse tagamiseks  
- **A/B testimine**: Testi erinevaid mudeleid samaaegselt ääreseadmetel  
- **Dünaamiline valik**: Vali mudelid vastavalt seadme hetkeseisule  
- **Ressursside jagamine**: Optimeeri ressursside kasutust mitme juurutatud mudeli vahel  

### Federatiivne õpe  
- **Hajutatud õpe**: Õpeta mudeleid mitmel ääreseadmel  
- **Privaatsuse säilitamine**: Hoia treeningandmed lokaalsed, jagades samal ajal mudeli täiustusi  
- **Koostööõpe**: Võimalda seadmetel õppida kollektiivsetest kogemustest  
- **Ääre-pilve koordineerimine**: Koordineeri õppimist ääreseadmete ja pilve infrastruktuuri vahel  

### Reaalajas töötlemine  
- **Voogtöötlus**: Töötle pidevaid andmevooge ääreseadmetel  
- **Madal latentsus**: Optimeeri minimaalsete järeldusviivituste jaoks  
- **Partiitöötlus**: Töötle andmepartiisid tõhusalt ääreseadmetel  
- **Kohanduv töötlemine**: Kohanda töötlemist vastavalt seadme hetkekapatsiteedile  

## Ääre AI arenduse tõrkeotsing  

### Levinud probleemid  
- **Mälupiirangud**: Mudel on sihtseadme mälu jaoks liiga suur  
- **Järeldamise kiirus**: Mudeli järeldamine on reaalajas nõuete jaoks liiga aeglane  
- **Täpsuse halvenemine**: Optimeerimine vähendab mudeli täpsust vastuvõetamatult  
- **Riistvaraga ühilduvus**: Mudel ei ühildu sihtseadme riistvaraga  

### Silumisstrateegiad  
- **Jõudlusprofiilimine**: Kasuta AI Toolkit'i jälgimisfunktsioone kitsaskohtade tuvastamiseks  
- **Ressursside monitooring**: Jälgi mälu ja CPU kasutust arenduse ajal  
- **Järk-järguline testimine**: Testi optimeerimisi järk-järgult, et probleeme isoleerida  
- **Riistvarasimulatsioon**: Kasuta arendustööriistu sihtseadme riistvara simuleerimiseks  

### Optimeerimislahendused  
- **Täiendav kvantiseerimine**: Rakenda agressiivsemaid kvantiseerimistehnikaid  
- **Mudeli arhitektuur**: Kaalu erinevaid mudeliarhitektuure, mis on optimeeritud ääre jaoks  
- **Eeltöötluse optimeerimine**: Optimeeri andmete eeltöötlus ääre piirangute jaoks  
- **Järeldamise optimeerimine**: Kasuta riistvaraspetsiifilisi järeldusoptimeerimisi  

## Ressursid ja järgmised sammud  

### Ametlik dokumentatsioon  
- [AI Toolkit arendaja dokumentatsioon](https://aka.ms/AIToolkit/doc)  
- [Paigaldus- ja seadistusjuhend](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentatsioon](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentatsioon](https://modelcontextprotocol.io/)  

### Kogukond ja tugi  
- [AI Toolkit GitHubi hoidla](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHubi probleemid ja funktsioonisoovid](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discordi kogukond](https://aka.ms/azureaifoundry/discord)  
- [VS Code laienduste turg](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tehnilised ressursid  
- [ONNX Runtime dokumentatsioon](https://onnxruntime.ai/)  
- [Ollama dokumentatsioon](https://ollama.ai/)  
- [Windows ML dokumentatsioon](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Õppeteed  
- [Ääre AI põhialuste kursus](../Module01/README.md)  
- [Väikeste keelemudelite juhend](../Module02/README.md)  
- [Ääre juurutusstrateegiad](../Module03/README.md)  
- [Windowsi ääre AI arendus](./windowdeveloper.md)  

### Täiendavad ressursid  
- **Hoidla statistika**: 1.8k+ tähte, 150+ kahvlit, 18+ kaastöölist  
- **Litsents**: MIT litsents  
- **Turvalisus**: Microsofti turvapoliitikad kehtivad  
- **Telemeetria**: Austab VS Code telemeetria seadeid  

## Kokkuvõte  

AI Toolkit Visual Studio Code'i jaoks on terviklik platvorm kaasaegseks AI arenduseks, pakkudes sujuvaid agentide arendamise võimalusi, mis on eriti väärtuslikud ääre AI rakenduste jaoks. Selle ulatuslik mudelikataloog, mis toetab selliseid pakkujaid nagu Anthropic, OpenAI, GitHub ja Google, koos kohaliku täitmise võimalustega ONNX-i ja Ollama kaudu, pakub paindlikkust mitmekesiste ääre juurutusstsenaariumide jaoks.  

Tööriistakomplekti tugevus seisneb selle integreeritud lähenemises—alates mudelite avastamisest ja katsetamisest Playgroundis kuni keerukate agentide arendamiseni Prompt Builderiga, põhjalike hindamisvõimaluste ja sujuva MCP tööriistade integreerimiseni. Ääre AI arendajatele tähendab see AI agentide kiiret prototüüpimist ja testimist enne ääre juurutamist, võimalusega kiiresti iteratsiooni teha ja optimeerida ressursipiirangutega keskkondade jaoks.  

Peamised eelised ääre AI arendamiseks:  
- **Kiire katsetamine**: Testi mudeleid ja agente kiiresti enne ääre juurutamist  
- **Mitme pakkuja paindlikkus**: Juurdepääs mudelitele erinevatest allikatest, et leida optimaalsed äärelahendused  
- **Kohalik arendus**: Testi ONNX-i ja Ollama abil võrguühenduseta ja privaatsust säilitades  
- **Tootmisvalmidus**: Loo tootmisvalmis kood ja integreeri väliste tööriistadega MCP kaudu  
- **Põhjalik hindamine**: Kasuta sisseehitatud ja kohandatud mõõdikuid ääre AI jõudluse valideerimiseks  

Kuna AI liigub üha enam ääre juurutusstsenaariumide poole, pakub AI Toolkit VS Code'i jaoks arenduskeskkonda ja töövoogu, mis on vajalik intelligentsete rakenduste loomiseks, testimiseks ja optimeerimiseks ressursipiirangutega keskkondades. Olgu tegemist IoT lahenduste, mobiilsete AI rakenduste või manustatud intelligentsüsteemidega, tööriistakomplekti terviklik funktsioonide komplekt ja integreeritud töövoog toetavad kogu ääre AI arenduse elutsüklit.  

Pideva arenduse ja aktiivse kogukonnaga (1.8k+ GitHubi tähte) jääb AI Toolkit esirinda AI arendustööriistade seas, arenedes pidevalt, et vastata kaasaegsete AI arendajate vajadustele ääre juurutusstsenaariumide jaoks.  

[Next Foundry Local](./foundrylocal.md)  

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.