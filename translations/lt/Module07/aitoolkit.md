<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-19T02:17:51+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "lt"
}
-->
# AI įrankių rinkinys Visual Studio Code - Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į išsamų vadovą, kaip naudoti AI įrankių rinkinį Visual Studio Code aplinkoje Edge AI kūrimui. Kadangi dirbtinis intelektas pereina nuo centralizuoto debesų kompiuterijos prie paskirstytų kraštinių įrenginių, kūrėjams reikia galingų, integruotų įrankių, kurie galėtų spręsti unikalius kraštinių diegimo iššūkius – nuo resursų apribojimų iki reikalavimų veikti neprisijungus.

AI įrankių rinkinys Visual Studio Code aplinkoje užpildo šią spragą, suteikdamas pilną kūrimo aplinką, specialiai pritaikytą kurti, testuoti ir optimizuoti AI programas, kurios efektyviai veikia kraštiniuose įrenginiuose. Nesvarbu, ar kuriate IoT jutikliams, mobiliesiems įrenginiams, įterptinėms sistemoms ar kraštiniams serveriams, šis įrankių rinkinys supaprastina visą jūsų kūrimo procesą pažįstamoje VS Code aplinkoje.

Šis vadovas padės jums perprasti pagrindines sąvokas, įrankius ir geriausias praktikas, kaip pasinaudoti AI įrankių rinkiniu jūsų Edge AI projektuose – nuo pradinio modelio pasirinkimo iki diegimo gamyboje.

## Apžvalga

AI įrankių rinkinys suteikia integruotą kūrimo aplinką visam Edge AI programų gyvavimo ciklui VS Code aplinkoje. Jis siūlo sklandžią integraciją su populiariais AI modeliais iš tokių tiekėjų kaip OpenAI, Anthropic, Google ir GitHub, tuo pačiu palaikydamas vietinį modelių diegimą per ONNX ir Ollama – tai itin svarbios funkcijos Edge AI programoms, kurioms reikalingas įrenginio lygio inferencijos vykdymas.

Kas išskiria AI įrankių rinkinį Edge AI kūrimui, tai jo dėmesys visam kraštinio diegimo procesui. Skirtingai nuo tradicinių AI kūrimo įrankių, kurie daugiausia orientuojasi į debesų diegimą, AI įrankių rinkinys apima specializuotas funkcijas modelių optimizavimui, testavimui su ribotais resursais ir kraštiniam našumo vertinimui. Šis įrankių rinkinys supranta, kad Edge AI kūrimui reikia kitokių sprendimų – mažesnių modelių, greitesnių inferencijos laikų, galimybės veikti neprisijungus ir optimizacijų, pritaikytų konkrečiai aparatinei įrangai.

Platforma palaiko įvairius diegimo scenarijus – nuo paprastos įrenginio inferencijos iki sudėtingų daugelio modelių kraštinių architektūrų. Ji siūlo įrankius modelių konversijai, kvantizacijai ir optimizacijai, kurie yra būtini sėkmingam kraštiniam diegimui, tuo pačiu išlaikant kūrėjų produktyvumą, kuriuo garsėja VS Code.

## Mokymosi tikslai

Pasibaigus šiam vadovui, jūs galėsite:

### Pagrindinės kompetencijos
- **Įdiegti ir sukonfigūruoti** AI įrankių rinkinį Visual Studio Code aplinkoje Edge AI kūrimo procesams
- **Naršyti ir naudoti** AI įrankių rinkinio sąsają, įskaitant Modelių katalogą, Žaidimų aikštelę ir Agentų kūrimo įrankį
- **Pasirinkti ir įvertinti** AI modelius, tinkamus kraštiniam diegimui, atsižvelgiant į našumą ir resursų apribojimus
- **Konvertuoti ir optimizuoti** modelius naudojant ONNX formatą ir kvantizacijos technikas kraštiniams įrenginiams

### Edge AI kūrimo įgūdžiai
- **Kurti ir įgyvendinti** Edge AI programas naudojant integruotą kūrimo aplinką
- **Atlikti modelių testavimą** kraštinėmis sąlygomis, naudojant vietinę inferenciją ir resursų stebėjimą
- **Kurti ir pritaikyti** AI agentus, optimizuotus kraštinio diegimo scenarijams
- **Vertinti modelių našumą** naudojant metrikas, svarbias kraštiniam kompiuterijos procesui (vėlavimas, atminties naudojimas, tikslumas)

### Optimizacija ir diegimas
- **Taikyti kvantizacijos ir genėjimo** technikas, kad sumažintumėte modelio dydį, išlaikant priimtiną našumą
- **Optimizuoti modelius** konkretiems kraštiniams aparatūros platformoms, įskaitant CPU, GPU ir NPU pagreitį
- **Įgyvendinti geriausias praktikas** Edge AI kūrimui, įskaitant resursų valdymą ir atsargines strategijas
- **Paruošti modelius ir programas** diegimui gamyboje kraštiniuose įrenginiuose

### Pažangios Edge AI sąvokos
- **Integruoti su kraštinėmis AI sistemomis** įskaitant ONNX Runtime, Windows ML ir TensorFlow Lite
- **Įgyvendinti daugelio modelių architektūras** ir federuoto mokymosi scenarijus kraštinėse aplinkose
- **Spręsti dažnas Edge AI problemas** įskaitant atminties apribojimus, inferencijos greitį ir aparatūros suderinamumą
- **Kurti stebėjimo ir registravimo** strategijas Edge AI programoms gamyboje

### Praktinis pritaikymas
- **Kurti pilnus Edge AI sprendimus** nuo modelio pasirinkimo iki diegimo
- **Demonstruoti įgūdžius** kraštiniam kūrimo procesui ir optimizacijos technikoms
- **Taikyti išmoktus principus** realaus pasaulio Edge AI atvejams, įskaitant IoT, mobiliuosius ir įterptinius pritaikymus
- **Vertinti ir palyginti** skirtingas Edge AI diegimo strategijas ir jų kompromisus

## Pagrindinės funkcijos Edge AI kūrimui

### 1. Modelių katalogas ir atranka
- **Vietinių modelių palaikymas**: Atraskite ir pasiekite AI modelius, specialiai optimizuotus kraštiniam diegimui
- **ONNX integracija**: Pasiekite modelius ONNX formatu efektyviai kraštinei inferencijai
- **Ollama palaikymas**: Naudokite vietinius modelius per Ollama, užtikrinant privatumą ir galimybę veikti neprisijungus
- **Modelių palyginimas**: Palyginkite modelius, kad rastumėte optimalų našumo ir resursų sunaudojimo balansą kraštiniams įrenginiams

### 2. Interaktyvi žaidimų aikštelė
- **Vietinė testavimo aplinka**: Testuokite modelius vietoje prieš kraštinį diegimą
- **Daugiarūšis eksperimentavimas**: Testuokite su vaizdais, tekstu ir kitais įvesties tipais, būdingais kraštinėms situacijoms
- **Parametrų derinimas**: Eksperimentuokite su skirtingais modelio parametrais, kad optimizuotumėte kraštiniams apribojimams
- **Realaus laiko našumo stebėjimas**: Stebėkite inferencijos greitį ir resursų naudojimą kūrimo metu

### 3. Agentų kūrimo įrankis kraštinėms programoms
- **Užklausų inžinerija**: Kurkite optimizuotas užklausas, kurios efektyviai veikia su mažesniais kraštiniais modeliais
- **MCP įrankių integracija**: Integruokite Model Context Protocol įrankius, kad pagerintumėte kraštinių agentų galimybes
- **Kodo generavimas**: Generuokite gamybai paruoštą kodą, optimizuotą kraštinio diegimo scenarijams
- **Struktūruoti rezultatai**: Kurkite agentus, kurie pateikia nuoseklius, struktūruotus atsakymus, tinkamus kraštinėms programoms

### 4. Modelių vertinimas ir testavimas
- **Našumo metrikos**: Vertinkite modelius pagal metrikas, svarbias kraštiniam diegimui (vėlavimas, atminties naudojimas, tikslumas)
- **Grupinis testavimas**: Testuokite kelias modelio konfigūracijas vienu metu, kad rastumėte optimalias kraštines sąlygas
- **Individualus vertinimas**: Kurkite individualius vertinimo kriterijus, pritaikytus Edge AI atvejams
- **Resursų profiliavimas**: Analizuokite atminties ir skaičiavimo reikalavimus kraštinio diegimo planavimui

### 5. Modelių konversija ir optimizacija
- **ONNX konversija**: Konvertuokite modelius iš įvairių formatų į ONNX, kad jie būtų suderinami su kraštiniu diegimu
- **Kvantizacija**: Sumažinkite modelio dydį ir pagerinkite inferencijos greitį naudojant kvantizacijos technikas
- **Aparatūros optimizacija**: Optimizuokite modelius konkrečiai kraštinei aparatūrai (CPU, GPU, NPU)
- **Formatų transformacija**: Transformuokite modelius iš Hugging Face ir kitų šaltinių kraštiniam diegimui

### 6. Pritaikymas kraštinėms situacijoms
- **Srities adaptacija**: Pritaikykite modelius konkretiems kraštiniams atvejams ir aplinkoms
- **Vietinis mokymas**: Mokykite modelius vietoje su GPU palaikymu, atsižvelgiant į kraštinius reikalavimus
- **Azure integracija**: Naudokite Azure Container Apps debesų pagrindu atliekamam pritaikymui prieš kraštinį diegimą
- **Perdavimo mokymasis**: Pritaikykite iš anksto apmokytus modelius kraštiniams užduotims ir apribojimams

### 7. Našumo stebėjimas ir sekimas
- **Kraštinio našumo analizė**: Stebėkite modelio našumą kraštinėmis sąlygomis
- **Sekimo duomenų rinkimas**: Rinkite detalius našumo duomenis optimizacijai
- **Silpnųjų vietų identifikavimas**: Nustatykite našumo problemas prieš diegimą kraštiniuose įrenginiuose
- **Resursų naudojimo stebėjimas**: Stebėkite atminties, CPU ir inferencijos laiką kraštinei optimizacijai

## Edge AI kūrimo procesas

### 1 etapas: Modelių atranka ir pasirinkimas
1. **Naršykite modelių katalogą**: Naudokite modelių katalogą, kad rastumėte modelius, tinkamus kraštiniam diegimui
2. **Palyginkite našumą**: Vertinkite modelius pagal dydį, tikslumą ir inferencijos greitį
3. **Testuokite vietoje**: Naudokite Ollama arba ONNX modelius testavimui vietoje prieš kraštinį diegimą
4. **Įvertinkite resursų reikalavimus**: Nustatykite atminties ir skaičiavimo poreikius tiksliniams kraštiniams įrenginiams

### 2 etapas: Modelių optimizacija
1. **Konvertuokite į ONNX**: Konvertuokite pasirinktus modelius į ONNX formatą, kad jie būtų suderinami su kraštiniu diegimu
2. **Taikykite kvantizaciją**: Sumažinkite modelio dydį naudodami INT8 arba INT4 kvantizaciją
3. **Aparatūros optimizacija**: Optimizuokite modelius tiksliniams kraštiniams įrenginiams (ARM, x86, specializuoti pagreičiai)
4. **Našumo patvirtinimas**: Patvirtinkite, kad optimizuoti modeliai išlaiko priimtiną tikslumą

### 3 etapas: Programų kūrimas
1. **Agentų dizainas**: Naudokite Agentų kūrimo įrankį, kad sukurtumėte kraštiniams optimizuotus AI agentus
2. **Užklausų inžinerija**: Kurkite užklausas, kurios efektyviai veikia su mažesniais modeliais
3. **Integracijos testavimas**: Testuokite agentus simuliuotomis kraštinėmis sąlygomis
4. **Kodo generavimas**: Generuokite gamybai paruoštą kodą, optimizuotą kraštiniam diegimui

### 4 etapas: Vertinimas ir testavimas
1. **Grupinis vertinimas**: Testuokite kelias konfigūracijas, kad rastumėte optimalias kraštines sąlygas
2. **Našumo profiliavimas**: Analizuokite inferencijos greitį, atminties naudojimą ir tikslumą
3. **Kraštinė simuliacija**: Testuokite sąlygomis, panašiomis į tikslinę kraštinio diegimo aplinką
4. **Streso testavimas**: Vertinkite našumą įvairiomis apkrovos sąlygomis

### 5 etapas: Diegimo paruošimas
1. **Galutinė optimizacija**: Taikykite galutines optimizacijas, remdamiesi testavimo rezultatais
2. **Diegimo paketavimas**: Supakuokite modelius ir kodą kraštiniam diegimui
3. **Dokumentacija**: Dokumentuokite diegimo reikalavimus ir konfigūraciją
4. **Stebėjimo nustatymas**: Paruoškite stebėjimo ir registravimo sistemą kraštiniam diegimui

## Tikslinė auditorija Edge AI kūrimui

### Edge AI kūrėjai
- Programų kūrėjai, kuriantys AI pagrindu veikiančius kraštinius įrenginius ir IoT sprendimus
- Įterptinių sistemų kūrėjai, integruojantys AI galimybes į resursų apribotus įrenginius
- Mobilieji kūrėjai, kuriantys AI programas, veikiančias įrenginiuose, tokiuose kaip išmanieji telefonai ir planšetės

### Edge AI inžinieriai
- AI inžinieriai, optimizuojantys modelius kraštiniam diegimui ir valdantys inferencijos procesus
- DevOps inžinieriai, diegiantys ir valdantys AI modelius paskirstytoje kraštinėje infrastruktūroje
- Našumo inžinieriai, optimizuojantys AI darbo krūvius kraštinės aparatūros apribojimams

### Tyrėjai ir pedagogai
- AI tyrėjai, kuriantys efektyvius modelius ir algoritmus kraštinei kompiuterijai
- Pedagogai, mokantys Edge AI sąvokų ir demonstruojantys optimizacijos technikas
- Studentai, besimokantys apie iššūkius ir sprendimus kraštiniame AI diegime

## Edge AI pritaikymo atvejai

### Išmanieji IoT įrenginiai
- **Realaus laiko vaizdų atpažinimas**: Diegti kompiuterinės regos modelius IoT kamerose ir jutikliuose
- **Balso apdorojimas**: Įgyvendinti kalbos atpažinimą ir natūralios kalbos apdorojimą išmaniuose garsiakalbiuose
- **Prognozuojamoji priežiūra**: Vykdyti anomalijų aptikimo modelius pramoniniuose kraštiniuose įrenginiuose
- **Aplinkos stebėjimas**: Diegti jutiklių duomenų analizės modelius aplinkos programoms

### Mobiliosios ir įterptinės programos
- **Vertimas įrenginyje**: Įgyvendinti kalbos vertimo modelius, veikiančius neprisijungus
- **Papildyta realybė**: Diegti realaus laiko objektų atpažinimą ir sekimą AR programoms
- **Sveikatos stebėjimas**: Vykdyti sveikatos analizės modelius nešiojamuose įrenginiuose ir medicinos įrangoje
- **Autonominės sistemos**: Įgyvendinti sprend
- **Saugumas**: Įgyvendinkite tinkamas saugumo priemones kraštinių AI programoms

## Integracija su kraštinių AI sistemomis

### ONNX Runtime
- **Kryžminė platformų diegimas**: Diekite ONNX modelius įvairiose kraštinėse platformose
- **Aparatūros optimizavimas**: Pasinaudokite ONNX Runtime aparatūros specifinėmis optimizacijomis
- **Mobilus palaikymas**: Naudokite ONNX Runtime Mobile išmaniesiems telefonams ir planšetėms
- **IoT integracija**: Diekite IoT įrenginiuose naudodami ONNX Runtime lengvas distribucijas

### Windows ML
- **Windows įrenginiai**: Optimizuokite Windows pagrindu veikiančius kraštinius įrenginius ir kompiuterius
- **NPU pagreitinimas**: Pasinaudokite Neural Processing Units Windows įrenginiuose
- **DirectML**: Naudokite DirectML GPU pagreitinimui Windows platformose
- **UWP integracija**: Integruokite su Universal Windows Platform programomis

### TensorFlow Lite
- **Mobilus optimizavimas**: Diekite TensorFlow Lite modelius mobiliuose ir įterptiniuose įrenginiuose
- **Aparatūros delegatai**: Naudokite specializuotus aparatūros delegatus pagreitinimui
- **Mikrovaldikliai**: Diekite mikrovaldikliuose naudodami TensorFlow Lite Micro
- **Kryžminė platformų palaikymas**: Diekite Android, iOS ir įterptinėse Linux sistemose

### Azure IoT Edge
- **Debesų ir kraštų hibridas**: Derinkite debesų mokymą su kraštų inferencija
- **Modulių diegimas**: Diekite AI modelius kaip IoT Edge modulius
- **Įrenginių valdymas**: Nuotoliniu būdu valdykite kraštinius įrenginius ir modelių atnaujinimus
- **Telemetrija**: Rinkite našumo duomenis ir modelių metrikas iš kraštinių diegimų

## Pažangūs kraštinių AI scenarijai

### Daugelio modelių diegimas
- **Modelių ansambliai**: Diekite kelis modelius, kad padidintumėte tikslumą arba užtikrintumėte patikimumą
- **A/B testavimas**: Vienu metu testuokite skirtingus modelius kraštiniuose įrenginiuose
- **Dinaminis pasirinkimas**: Pasirinkite modelius pagal dabartines įrenginio sąlygas
- **Resursų dalijimasis**: Optimizuokite resursų naudojimą tarp kelių diegtų modelių

### Federacinis mokymasis
- **Paskirstytas mokymas**: Mokykite modelius keliuose kraštiniuose įrenginiuose
- **Privatumo išsaugojimas**: Laikykite mokymo duomenis vietoje, dalindamiesi modelio patobulinimais
- **Bendradarbiavimo mokymasis**: Leiskite įrenginiams mokytis iš kolektyvinės patirties
- **Kraštų ir debesų koordinacija**: Koordinuokite mokymą tarp kraštinių įrenginių ir debesų infrastruktūros

### Realaus laiko apdorojimas
- **Srautų apdorojimas**: Apdorokite nuolatinius duomenų srautus kraštiniuose įrenginiuose
- **Mažos delsos inferencija**: Optimizuokite minimaliai inferencijos delsei
- **Partinis apdorojimas**: Efektyviai apdorokite duomenų partijas kraštiniuose įrenginiuose
- **Adaptuojamas apdorojimas**: Koreguokite apdorojimą pagal dabartines įrenginio galimybes

## Kraštinių AI kūrimo trikčių šalinimas

### Dažnos problemos
- **Atminties apribojimai**: Modelis per didelis tikslinio įrenginio atminčiai
- **Inferencijos greitis**: Modelio inferencija per lėta realaus laiko reikalavimams
- **Tikslumo sumažėjimas**: Optimizavimas nepriimtinai sumažina modelio tikslumą
- **Aparatūros suderinamumas**: Modelis nesuderinamas su tiksline aparatūra

### Derinimo strategijos
- **Našumo profiliavimas**: Naudokite AI Toolkit sekimo funkcijas, kad identifikuotumėte kliūtis
- **Resursų stebėjimas**: Stebėkite atminties ir CPU naudojimą kūrimo metu
- **Inkrementinis testavimas**: Testuokite optimizacijas palaipsniui, kad izoliuotumėte problemas
- **Aparatūros simuliacija**: Naudokite kūrimo įrankius, kad simuliuotumėte tikslinę aparatūrą

### Optimizavimo sprendimai
- **Tolimesnė kvantizacija**: Taikykite agresyvesnes kvantizacijos technikas
- **Modelio architektūra**: Apsvarstykite skirtingas modelio architektūras, optimizuotas kraštams
- **Išankstinio apdorojimo optimizavimas**: Optimizuokite duomenų išankstinį apdorojimą kraštų apribojimams
- **Inferencijos optimizavimas**: Naudokite aparatūros specifines inferencijos optimizacijas

## Ištekliai ir tolesni žingsniai

### Dokumentacija
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Bendruomenė ir palaikymas
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Mokymosi ištekliai
- [Kraštinių AI pagrindų kursas](./Module01/README.md)
- [Mažų kalbos modelių vadovas](./Module02/README.md)
- [Kraštų diegimo strategijos](./Module03/README.md)
- [Windows kraštinių AI kūrimas](./windowdeveloper.md)

## Išvada

AI Toolkit for Visual Studio Code suteikia išsamų platformą kraštinių AI kūrimui – nuo modelių atradimo ir optimizavimo iki diegimo ir stebėjimo. Pasinaudodami integruotais įrankiais ir darbo eigomis, kūrėjai gali efektyviai kurti, testuoti ir diegti AI programas, kurios veiksmingai veikia resursų apribotuose kraštiniuose įrenginiuose.

Įrankių palaikymas ONNX, Ollama ir įvairiems debesų tiekėjams, kartu su optimizavimo ir vertinimo galimybėmis, daro jį idealiu pasirinkimu kraštinių AI kūrimui. Nesvarbu, ar kuriate IoT programas, mobilias AI funkcijas, ar įterptines intelekto sistemas, AI Toolkit suteikia reikalingus įrankius ir darbo eigas sėkmingam kraštinių AI diegimui.

Kai kraštinis AI toliau vystosi, AI Toolkit for VS Code išlieka priešakyje, suteikdamas kūrėjams pažangius įrankius ir galimybes kurti naujos kartos intelektualias kraštines programas.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.