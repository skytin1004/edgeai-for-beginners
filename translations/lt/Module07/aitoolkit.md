<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T15:13:25+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "lt"
}
-->
# AI įrankių rinkinys Visual Studio Code - Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į išsamų vadovą, kaip naudoti AI įrankių rinkinį Visual Studio Code aplinkoje Edge AI kūrimui. Kadangi dirbtinis intelektas pereina nuo centralizuoto debesų kompiuterijos prie paskirstytų kraštinių įrenginių, kūrėjams reikia galingų, integruotų įrankių, kurie galėtų spręsti unikalius kraštinių diegimo iššūkius – nuo resursų apribojimų iki reikalavimų veikti neprisijungus.

AI įrankių rinkinys Visual Studio Code aplinkoje užpildo šią spragą, suteikdamas pilną kūrimo aplinką, specialiai sukurtą AI programoms, kurios efektyviai veikia kraštiniuose įrenginiuose, kurti, testuoti ir optimizuoti. Nesvarbu, ar kuriate IoT jutikliams, mobiliesiems įrenginiams, įterptinėms sistemoms ar kraštiniams serveriams, šis įrankių rinkinys supaprastina visą kūrimo procesą pažįstamoje VS Code aplinkoje.

Šis vadovas padės jums perprasti pagrindines sąvokas, įrankius ir geriausią praktiką, kaip pasinaudoti AI įrankių rinkiniu savo Edge AI projektuose – nuo pradinio modelio pasirinkimo iki diegimo gamyboje.

## Apžvalga

AI įrankių rinkinys Visual Studio Code aplinkoje yra galingas plėtinys, kuris supaprastina agentų kūrimą ir AI programų kūrimą. Įrankių rinkinys suteikia išsamias galimybes tyrinėti, vertinti ir diegti AI modelius iš įvairių tiekėjų, įskaitant Anthropic, OpenAI, GitHub, Google, kartu palaikant vietinį modelių vykdymą naudojant ONNX ir Ollama.

Kas išskiria AI įrankių rinkinį, tai jo išsamus požiūris į visą AI kūrimo ciklą. Skirtingai nuo tradicinių AI kūrimo įrankių, kurie orientuojasi į atskirus aspektus, AI įrankių rinkinys suteikia integruotą aplinką, apimančią modelių atradimą, eksperimentavimą, agentų kūrimą, vertinimą ir diegimą – visa tai pažįstamoje VS Code aplinkoje.

Platforma yra specialiai sukurta greitam prototipų kūrimui ir diegimui gamyboje, su funkcijomis, tokiomis kaip užklausų generavimas, greiti startai, sklandžios MCP (Model Context Protocol) įrankių integracijos ir išsamios vertinimo galimybės. Edge AI kūrimui tai reiškia, kad galite efektyviai kurti, testuoti ir optimizuoti AI programas kraštiniams diegimo scenarijams, išlaikydami visą kūrimo procesą VS Code aplinkoje.

## Mokymosi tikslai

Pasibaigus šiam vadovui, jūs galėsite:

### Pagrindinės kompetencijos
- **Įdiegti ir konfigūruoti** AI įrankių rinkinį Visual Studio Code aplinkoje Edge AI kūrimo procesams
- **Naršyti ir naudoti** AI įrankių rinkinio sąsają, įskaitant Model Catalog, Playground ir Agent Builder
- **Pasirinkti ir vertinti** AI modelius, tinkamus kraštiniam diegimui, atsižvelgiant į našumą ir resursų apribojimus
- **Konvertuoti ir optimizuoti** modelius naudojant ONNX formatą ir kvantavimo technikas kraštiniams įrenginiams

### Edge AI kūrimo įgūdžiai
- **Kurti ir įgyvendinti** Edge AI programas naudojant integruotą kūrimo aplinką
- **Atlikti modelių testavimą** kraštinėmis sąlygomis, naudojant vietinį įžvalgą ir resursų stebėjimą
- **Kurti ir pritaikyti** AI agentus, optimizuotus kraštiniams diegimo scenarijams
- **Vertinti modelių našumą** naudojant kraštiniam kompiuterijos tinkamam metrikas (vėlavimas, atminties naudojimas, tikslumas)

### Optimizavimas ir diegimas
- **Taikyti kvantavimo ir genėjimo** technikas, kad sumažintumėte modelio dydį, išlaikant priimtiną našumą
- **Optimizuoti modelius** konkrečioms kraštinių įrenginių platformoms, įskaitant CPU, GPU ir NPU pagreitį
- **Įgyvendinti geriausią praktiką** Edge AI kūrimui, įskaitant resursų valdymą ir atsargines strategijas
- **Paruošti modelius ir programas** diegimui gamyboje kraštiniuose įrenginiuose

### Pažangios Edge AI sąvokos
- **Integruoti su kraštinėmis AI sistemomis**, įskaitant ONNX Runtime, Windows ML ir TensorFlow Lite
- **Įgyvendinti daugelio modelių architektūras** ir federacinio mokymosi scenarijus kraštinėse aplinkose
- **Spręsti dažnas Edge AI problemas**, tokias kaip atminties apribojimai, įžvalgos greitis ir aparatūros suderinamumas
- **Kurti stebėjimo ir registravimo** strategijas Edge AI programoms gamyboje

### Praktinis pritaikymas
- **Kurti pilnus Edge AI sprendimus** nuo modelio pasirinkimo iki diegimo
- **Demonstruoti kompetenciją** kraštiniams kūrimo procesams ir optimizavimo technikoms
- **Taikyti išmoktas sąvokas** realaus pasaulio Edge AI atvejams, įskaitant IoT, mobiliąsias ir įterptines programas
- **Vertinti ir palyginti** skirtingas Edge AI diegimo strategijas ir jų kompromisus

## Pagrindinės funkcijos Edge AI kūrimui

### 1. Modelių katalogas ir atradimas
- **Daugelio tiekėjų palaikymas**: Naršykite ir pasiekite AI modelius iš Anthropic, OpenAI, GitHub, Google ir kitų tiekėjų
- **Vietinių modelių integracija**: Supaprastintas ONNX ir Ollama modelių atradimas kraštiniam diegimui
- **GitHub modeliai**: Tiesioginė integracija su GitHub modelių talpinimu, kad būtų lengviau pasiekti
- **Modelių palyginimas**: Palyginkite modelius vienas šalia kito, kad rastumėte optimalų balansą kraštinių įrenginių apribojimams

### 2. Interaktyvi žaidimų aikštelė
- **Interaktyvi testavimo aplinka**: Greitas eksperimentavimas su modelio galimybėmis kontroliuojamoje aplinkoje
- **Daugiarūšis palaikymas**: Testavimas su vaizdais, tekstu ir kitais įvesties tipais, būdingais kraštinėms situacijoms
- **Eksperimentavimas realiu laiku**: Momentinis grįžtamasis ryšys apie modelio atsakymus ir našumą
- **Parametrų optimizavimas**: Modelio parametrų pritaikymas kraštinio diegimo reikalavimams

### 3. Užklausų (agentų) kūrėjas
- **Natūralios kalbos generavimas**: Generuokite pradinius užklausų tekstus naudodami natūralios kalbos aprašymus
- **Iteratyvus tobulinimas**: Tobulinkite užklausas pagal modelio atsakymus ir našumą
- **Užduočių skaidymas**: Suskaidykite sudėtingas užduotis naudojant užklausų grandines ir struktūrizuotus rezultatus
- **Kintamųjų palaikymas**: Naudokite kintamuosius užklausose, kad sukurtumėte dinamišką agentų elgesį
- **Gamybinio kodo generavimas**: Generuokite gamybai paruoštą kodą greitam programų kūrimui

### 4. Masinis vykdymas ir vertinimas
- **Daugelio modelių testavimas**: Vykdykite kelias užklausas pasirinktuose modeliuose vienu metu
- **Efektyvus testavimas mastu**: Testuokite įvairias įvestis ir konfigūracijas efektyviai
- **Individualūs testavimo atvejai**: Vykdykite agentus su testavimo atvejais, kad patikrintumėte funkcionalumą
- **Našumo palyginimas**: Palyginkite rezultatus skirtinguose modeliuose ir konfigūracijose

### 5. Modelio vertinimas su duomenų rinkiniais
- **Standartinės metrikos**: Testuokite AI modelius naudodami įmontuotus vertintojus (F1 balas, aktualumas, panašumas, nuoseklumas)
- **Individualūs vertintojai**: Kurkite savo vertinimo metrikas specifiniams atvejams
- **Duomenų rinkinių integracija**: Testuokite modelius su išsamiais duomenų rinkiniais
- **Našumo matavimas**: Kiekybiškai įvertinkite modelio našumą kraštinio diegimo sprendimams

### 6. Modelio pritaikymo galimybės
- **Modelio pritaikymas**: Pritaikykite modelius specifiniams atvejams ir sritims
- **Specializuotas pritaikymas**: Pritaikykite modelius specializuotoms sritims ir reikalavimams
- **Edge optimizavimas**: Pritaikykite modelius specialiai kraštinio diegimo apribojimams
- **Srities specifinis mokymas**: Kurkite modelius, pritaikytus specifiniams kraštiniams atvejams

### 7. MCP įrankių integracija
- **Išorinių įrankių prijungimas**: Prijunkite agentus prie išorinių įrankių per Model Context Protocol serverius
- **Veiksmai realiame pasaulyje**: Leiskite agentams užklausyti duomenų bazes, pasiekti API ar vykdyti individualią logiką
- **Esami MCP serveriai**: Naudokite įrankius iš komandų (stdio) arba HTTP (server-sent event) protokolų
- **Individualus MCP kūrimas**: Kurkite ir testuokite naujus MCP serverius Agent Builder aplinkoje

### 8. Agentų kūrimas ir testavimas
- **Funkcijų iškvietimo palaikymas**: Leiskite agentams dinamiškai iškviesti išorines funkcijas
- **Testavimas realiu laiku**: Testuokite integracijas su realaus laiko vykdymais ir įrankių naudojimu
- **Agentų versijavimas**: Agentų versijų kontrolė su palyginimo galimybėmis vertinimo rezultatams
- **Derinimas ir sekimas**: Vietinis sekimas ir derinimas agentų kūrimui

## Edge AI kūrimo procesas

### 1 etapas: Modelio atradimas ir pasirinkimas
1. **Naršykite modelių katalogą**: Naudokite modelių katalogą, kad rastumėte modelius, tinkamus kraštiniam diegimui
2. **Palyginkite našumą**: Vertinkite modelius pagal dydį, tikslumą ir įžvalgos greitį
3. **Testuokite vietoje**: Naudokite Ollama arba ONNX modelius, kad testuotumėte vietoje prieš kraštinį diegimą
4. **Įvertinkite resursų poreikius**: Nustatykite atminties ir skaičiavimo poreikius tiksliniams kraštiniams įrenginiams

### 2 etapas: Modelio optimizavimas
1. **Konvertuokite į ONNX**: Konvertuokite pasirinktus modelius į ONNX formatą kraštiniam suderinamumui
2. **Taikykite kvantavimą**: Sumažinkite modelio dydį naudodami INT8 arba INT4 kvantavimą
3. **Aparatūros optimizavimas**: Optimizuokite tiksliniams kraštiniams įrenginiams (ARM, x86, specializuoti pagreičiai)
4. **Našumo patvirtinimas**: Patvirtinkite, kad optimizuoti modeliai išlaiko priimtiną tikslumą

### 3 etapas: Programos kūrimas
1. **Agentų dizainas**: Naudokite Agent Builder, kad sukurtumėte kraštiniams optimizuotus AI agentus
2. **Užklausų inžinerija**: Sukurkite užklausas, kurios efektyviai veikia su mažesniais kraštiniais modeliais
3. **Integracijos testavimas**: Testuokite agentus simuliuotomis kraštinėmis sąlygomis
4. **Kodo generavimas**: Generuokite gamybai optimizuotą kodą kraštiniam diegimui

### 4 etapas: Vertinimas ir testavimas
1. **Masinis vertinimas**: Testuokite kelias konfigūracijas, kad rastumėte optimalias kraštines sąlygas
2. **Našumo profiliavimas**: Analizuokite įžvalgos greitį, atminties naudojimą ir tikslumą
3. **Kraštinė simuliacija**: Testuokite sąlygomis, panašiomis į tikslinę kraštinio diegimo aplinką
4. **Streso testavimas**: Vertinkite našumą įvairiomis apkrovos sąlygomis

### 5 etapas: Diegimo paruošimas
1. **Galutinis optimizavimas**: Taikykite galutines optimizacijas pagal testavimo rezultatus
2. **Diegimo paketavimas**: Supakuokite modelius ir kodą kraštiniam diegimui
3. **Dokumentacija**: Dokumentuokite diegimo reikalavimus ir konfigūraciją
4. **Stebėjimo paruošimas**: Paruoškite stebėjimą ir registravimą kraštiniam diegimui

## Tikslinė auditorija Edge AI kūrimui

### Edge AI kūrėjai
- Programų kūrėjai, kuriantys AI pagrįstus kraštinius įrenginius ir IoT sprendimus
- Įterptinių sistemų kūrėjai, integruojantys AI galimybes į resursų apribotus įrenginius
- Mobilieji kūrėjai, kuriantys AI programas įrenginiuose, tokiuose kaip išmanieji telefonai ir planšetės

### Edge AI inžinieriai
- AI inžinieriai, optimizuojantys modelius kraštiniam diegimui ir valdantys įžvalgos procesus
- DevOps inžinieriai, diegiantys ir valdantys AI modelius paskirstytoje kraštinėje infrastruktūroje
- Našumo inžinieriai, optimizuojantys AI darbo krūvius kraštinės aparatūros apribojimams

### Tyrėjai ir pedagogai
- AI tyrėjai, kuriantys efektyvius modelius ir algoritmus kraštinei kompiuterijai
- Pedagogai, mokantys Edge AI sąvokų ir demonstruojantys optimizavimo technikas
- Studentai, besimokantys apie Edge AI diegimo iššūkius ir sprendimus

## Edge AI naudojimo atvejai

### Išmanieji IoT įrenginiai
- **Vaizdų atpažinimas realiu laiku**: Diegti kompiuterinės regos modelius IoT kamerose ir jutikliuose
- **Balso apdorojimas**: Įgyvendinti kalbos atpažinimą ir natūralios kalbos apdorojimą išmaniuose garsiakalbiuose
- **Prognozuojama priežiūra**: Vykdyti anomalijų aptikimo modelius pramoniniuose kraštiniuose įrenginiuose
- **Aplinkos stebėjimas**: Diegti jutiklių duomenų analizės modelius aplinkos programoms

### Mobiliosios ir įterptinės programos
- **Vertimas įrenginyje**: Įgyvendinti kalbos vertimo modelius, kurie veikia neprisijungus
- **Papildyta realybė**: Diegti realaus laiko objektų atpažinimą ir sekimą AR programoms
- **Sveikatos stebėjimas**: Vykdyti sveikatos analizės modelius nešiojamuose įrenginiuose ir medicinos įrangoje
- **Autonominės sistemos**: Įgyvendinti spr
2. Sukurkite pradinius raginimus naudodami natūralios kalbos aprašymus  
3. Kartokite ir tobulinkite raginimus pagal modelio atsakymus  
4. Integruokite MCP įrankius, kad pagerintumėte agentų galimybes  

#### 3 žingsnis: Testavimas ir vertinimas  
1. Naudokite **Bulk Run**, kad išbandytumėte kelis raginimus skirtinguose modeliuose  
2. Paleiskite agentus su testavimo atvejais, kad patikrintumėte funkcionalumą  
3. Įvertinkite tikslumą ir našumą naudodami įmontuotus arba pasirinktinius metrikos įrankius  
4. Palyginkite skirtingus modelius ir konfigūracijas  

#### 4 žingsnis: Modelio tobulinimas ir optimizavimas  
1. Pritaikykite modelius specifiniams kraštutiniams naudojimo atvejams  
2. Taikykite specifinį domeno tobulinimą  
3. Optimizuokite pagal kraštutinius diegimo apribojimus  
4. Versijuokite ir palyginkite skirtingas agentų konfigūracijas  

#### 5 žingsnis: Paruošimas diegimui  
1. Sukurkite gamybai paruoštą kodą naudodami Agent Builder  
2. Nustatykite MCP serverio ryšius gamybos naudojimui  
3. Paruoškite diegimo paketus kraštutiniams įrenginiams  
4. Konfigūruokite stebėjimo ir vertinimo metrikas  

## Geriausia praktika Edge AI kūrimui  

### Modelio pasirinkimas  
- **Dydžio apribojimai**: Pasirinkite modelius, kurie atitinka tikslinių įrenginių atminties apribojimus  
- **Įžvalgos greitis**: Pirmenybę teikite modeliams su greitu įžvalgos laiku realaus laiko programoms  
- **Tikslumo kompromisai**: Subalansuokite modelio tikslumą su resursų apribojimais  
- **Formatų suderinamumas**: Rinkitės ONNX arba aparatūros optimizuotus formatus kraštutiniam diegimui  

### Optimizavimo technikos  
- **Kvantizacija**: Naudokite INT8 arba INT4 kvantizaciją, kad sumažintumėte modelio dydį ir pagerintumėte greitį  
- **Genėjimas**: Pašalinkite nereikalingus modelio parametrus, kad sumažintumėte skaičiavimo reikalavimus  
- **Žinių distiliacija**: Sukurkite mažesnius modelius, kurie išlaiko didesnių modelių našumą  
- **Aparatūros pagreitinimas**: Naudokite NPUs, GPUs arba specializuotus pagreitintuvus, jei jie yra prieinami  

### Kūrimo darbo eiga  
- **Iteratyvus testavimas**: Dažnai testuokite kraštutiniams įrenginiams panašiomis sąlygomis kūrimo metu  
- **Našumo stebėjimas**: Nuolat stebėkite resursų naudojimą ir įžvalgos greitį  
- **Versijų kontrolė**: Sekite modelio versijas ir optimizavimo nustatymus  
- **Dokumentacija**: Dokumentuokite visus optimizavimo sprendimus ir našumo kompromisus  

### Diegimo aspektai  
- **Resursų stebėjimas**: Stebėkite atminties, CPU ir energijos naudojimą gamybos metu  
- **Atsarginės strategijos**: Įgyvendinkite atsarginius mechanizmus modelio gedimams  
- **Atnaujinimo mechanizmai**: Planuokite modelio atnaujinimus ir versijų valdymą  
- **Saugumas**: Įgyvendinkite tinkamas saugumo priemones Edge AI programoms  

## Integracija su Edge AI sistemomis  

### ONNX Runtime  
- **Kryžminė platformų diegimas**: Diegkite ONNX modelius skirtingose kraštutinėse platformose  
- **Aparatūros optimizavimas**: Naudokite ONNX Runtime aparatūros specifines optimizacijas  
- **Mobilus palaikymas**: Naudokite ONNX Runtime Mobile išmaniesiems telefonams ir planšetėms  
- **IoT integracija**: Diegkite IoT įrenginiuose naudodami ONNX Runtime lengvas distribucijas  

### Windows ML  
- **Windows įrenginiai**: Optimizuokite Windows pagrindu veikiančius kraštutinius įrenginius ir kompiuterius  
- **NPU pagreitinimas**: Naudokite Neural Processing Units Windows įrenginiuose  
- **DirectML**: Naudokite DirectML GPU pagreitinimui Windows platformose  
- **UWP integracija**: Integruokite su Universal Windows Platform programomis  

### TensorFlow Lite  
- **Mobilus optimizavimas**: Diegkite TensorFlow Lite modelius mobiliuose ir įterptiniuose įrenginiuose  
- **Aparatūros delegatai**: Naudokite specializuotus aparatūros delegatus pagreitinimui  
- **Mikrovaldikliai**: Diegkite mikrovaldikliuose naudodami TensorFlow Lite Micro  
- **Kryžminė platformų palaikymas**: Diegkite Android, iOS ir įterptiniuose Linux sistemose  

### Azure IoT Edge  
- **Debesų-krašto hibridas**: Derinkite debesų mokymą su krašto įžvalga  
- **Modulių diegimas**: Diegkite AI modelius kaip IoT Edge modulius  
- **Įrenginių valdymas**: Nuotoliniu būdu valdykite kraštutinius įrenginius ir modelio atnaujinimus  
- **Telemetrija**: Rinkite našumo duomenis ir modelio metrikas iš kraštutinių diegimų  

## Pažangūs Edge AI scenarijai  

### Daugelio modelių diegimas  
- **Modelių ansambliai**: Diegkite kelis modelius, kad pagerintumėte tikslumą arba užtikrintumėte atsargą  
- **A/B testavimas**: Vienu metu testuokite skirtingus modelius kraštutiniuose įrenginiuose  
- **Dinaminis pasirinkimas**: Pasirinkite modelius pagal dabartines įrenginio sąlygas  
- **Resursų dalijimasis**: Optimizuokite resursų naudojimą tarp kelių diegtų modelių  

### Federuotas mokymasis  
- **Paskirstytas mokymas**: Mokykite modelius keliuose kraštutiniuose įrenginiuose  
- **Privatumo išsaugojimas**: Laikykite mokymo duomenis vietoje, dalindamiesi modelio patobulinimais  
- **Bendradarbiavimo mokymasis**: Leiskite įrenginiams mokytis iš kolektyvinės patirties  
- **Krašto-debesų koordinacija**: Koordinuokite mokymą tarp kraštutinių įrenginių ir debesų infrastruktūros  

### Realaus laiko apdorojimas  
- **Srautų apdorojimas**: Apdorokite nuolatinius duomenų srautus kraštutiniuose įrenginiuose  
- **Mažos delsos įžvalga**: Optimizuokite minimaliai įžvalgos delsei  
- **Partinis apdorojimas**: Efektyviai apdorokite duomenų partijas kraštutiniuose įrenginiuose  
- **Adaptuojamas apdorojimas**: Koreguokite apdorojimą pagal dabartines įrenginio galimybes  

## Edge AI kūrimo trikčių šalinimas  

### Dažnos problemos  
- **Atminties apribojimai**: Modelis per didelis tikslinio įrenginio atminčiai  
- **Įžvalgos greitis**: Modelio įžvalga per lėta realaus laiko reikalavimams  
- **Tikslumo degradacija**: Optimizavimas nepriimtinai sumažina modelio tikslumą  
- **Aparatūros suderinamumas**: Modelis nesuderinamas su tiksline aparatūra  

### Derinimo strategijos  
- **Našumo profiliavimas**: Naudokite AI Toolkit sekimo funkcijas, kad identifikuotumėte kliūtis  
- **Resursų stebėjimas**: Stebėkite atminties ir CPU naudojimą kūrimo metu  
- **Inkrementinis testavimas**: Testuokite optimizacijas palaipsniui, kad izoliuotumėte problemas  
- **Aparatūros simuliacija**: Naudokite kūrimo įrankius, kad simuliuotumėte tikslinę aparatūrą  

### Optimizavimo sprendimai  
- **Papildoma kvantizacija**: Taikykite agresyvesnes kvantizacijos technikas  
- **Modelio architektūra**: Apsvarstykite skirtingas modelio architektūras, optimizuotas kraštui  
- **Išankstinio apdorojimo optimizavimas**: Optimizuokite duomenų išankstinį apdorojimą kraštutiniams apribojimams  
- **Įžvalgos optimizavimas**: Naudokite aparatūros specifines įžvalgos optimizacijas  

## Ištekliai ir tolesni žingsniai  

### Oficialūs dokumentai  
- [AI Toolkit kūrėjo dokumentacija](https://aka.ms/AIToolkit/doc)  
- [Diegimo ir nustatymo vadovas](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentacija](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentacija](https://modelcontextprotocol.io/)  

### Bendruomenė ir palaikymas  
- [AI Toolkit GitHub saugykla](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub problemos ir funkcijų užklausos](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord bendruomenė](https://aka.ms/azureaifoundry/discord)  
- [VS Code plėtinių turgavietė](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Techniniai ištekliai  
- [ONNX Runtime dokumentacija](https://onnxruntime.ai/)  
- [Ollama dokumentacija](https://ollama.ai/)  
- [Windows ML dokumentacija](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Mokymosi keliai  
- [Edge AI pagrindų kursas](../Module01/README.md)  
- [Mažų kalbos modelių vadovas](../Module02/README.md)  
- [Edge diegimo strategijos](../Module03/README.md)  
- [Windows Edge AI kūrimas](./windowdeveloper.md)  

### Papildomi ištekliai  
- **Saugyklos statistika**: 1.8k+ žvaigždžių, 150+ šakų, 18+ bendradarbių  
- **Licencija**: MIT licencija  
- **Saugumas**: Taikomos Microsoft saugumo politikos  
- **Telemetrija**: Gerbia VS Code telemetrijos nustatymus  

## Išvada  

AI Toolkit for Visual Studio Code yra išsami platforma šiuolaikiniam AI kūrimui, suteikianti supaprastintas agentų kūrimo galimybes, kurios ypač vertingos Edge AI programoms. Su plačiu modelių katalogu, palaikančiu tiekėjų, tokių kaip Anthropic, OpenAI, GitHub ir Google, kartu su vietiniu vykdymu per ONNX ir Ollama, įrankių rinkinys siūlo lankstumą, reikalingą įvairiems kraštutiniams diegimo scenarijams.  

Įrankių rinkinio stiprybė slypi integruotame požiūryje – nuo modelių atradimo ir eksperimentavimo Playground iki sudėtingo agentų kūrimo su Prompt Builder, išsamių vertinimo galimybių ir sklandžios MCP įrankių integracijos. Edge AI kūrėjams tai reiškia greitą AI agentų prototipų kūrimą ir testavimą prieš kraštutinį diegimą, su galimybe greitai iteruoti ir optimizuoti resursų apribotoms aplinkoms.  

Pagrindiniai privalumai Edge AI kūrimui:  
- **Greitas eksperimentavimas**: Greitai testuokite modelius ir agentus prieš įsipareigojant kraštutiniam diegimui  
- **Daugelio tiekėjų lankstumas**: Pasiekite modelius iš įvairių šaltinių, kad rastumėte optimalias kraštutines sprendimus  
- **Vietinis kūrimas**: Testuokite su ONNX ir Ollama neprisijungus ir privatumo išsaugojimo kūrimui  
- **Gamybos pasirengimas**: Generuokite gamybai paruoštą kodą ir integruokite su išoriniais įrankiais per MCP  
- **Išsamus vertinimas**: Naudokite įmontuotas ir pasirinktines metrikas, kad patikrintumėte Edge AI našumą  

Kadangi AI vis labiau pereina prie kraštutinių diegimo scenarijų, AI Toolkit for VS Code suteikia kūrimo aplinką ir darbo eigą, reikalingą kurti, testuoti ir optimizuoti intelektualias programas resursų apribotoms aplinkoms. Nesvarbu, ar kuriate IoT sprendimus, mobiliąsias AI programas, ar įterptines intelektualias sistemas, įrankių rinkinio išsamus funkcijų rinkinys ir integruota darbo eiga palaiko visą Edge AI kūrimo gyvavimo ciklą.  

Su nuolatiniu vystymu ir aktyvia bendruomene (1.8k+ GitHub žvaigždžių), AI Toolkit išlieka pirmaujančiu AI kūrimo įrankiu, nuolat tobulėjančiu, kad atitiktų šiuolaikinių AI kūrėjų poreikius, kuriančių kraštutiniams diegimo scenarijams.  

[Next Foundry Local](./foundrylocal.md)  

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.