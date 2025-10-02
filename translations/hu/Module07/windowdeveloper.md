<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "77bb931ce93583c081cf7861f43d9662",
  "translation_date": "2025-10-02T14:05:18+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "hu"
}
-->
# Windows Edge AI Fejlesztési Útmutató

## Bevezetés

Üdvözlünk a Windows Edge AI Fejlesztési Útmutatóban – ez az átfogó útmutató segít intelligens alkalmazások létrehozásában, amelyek a Microsoft Windows AI Foundry platformjának eszközeivel kihasználják az eszközön futó mesterséges intelligencia erejét. Ez az útmutató kifejezetten azoknak a Windows fejlesztőknek készült, akik a legmodernebb Edge AI képességeket szeretnék integrálni alkalmazásaikba, miközben kihasználják a Windows hardvergyorsítás teljes spektrumát.

### A Windows AI előnyei

A Windows AI Foundry egy egységes, megbízható és biztonságos platformot kínál, amely támogatja a mesterséges intelligencia fejlesztési életciklusának minden szakaszát – a modell kiválasztásától és finomhangolásától kezdve az optimalizáláson át a CPU, GPU, NPU és hibrid felhő architektúrákon történő telepítésig. Ez a platform demokratizálja az AI fejlesztést az alábbiak biztosításával:

- **Hardver absztrakció**: Zökkenőmentes telepítés AMD, Intel, NVIDIA és Qualcomm chipeken
- **Eszközön futó intelligencia**: Adatvédelmet biztosító AI, amely teljes mértékben helyi hardveren fut
- **Optimalizált teljesítmény**: Windows hardverkonfigurációkra előoptimalizált modellek
- **Vállalati szintű megoldás**: Gyártási szintű biztonsági és megfelelőségi funkciók

### Miért válaszd a Windows-t az Edge AI-hoz?

**Univerzális hardvertámogatás**  
A Windows ML automatikus hardveroptimalizálást biztosít a teljes Windows ökoszisztémában, garantálva, hogy AI alkalmazásaid optimálisan működjenek a háttérben lévő hardverarchitektúrától függetlenül.

**Integrált AI futtatókörnyezet**  
A beépített Windows ML következtetési motor kiküszöböli a bonyolult beállítási követelményeket, lehetővé téve a fejlesztők számára, hogy az alkalmazáslogikára összpontosítsanak az infrastruktúra helyett.

**Copilot+ PC optimalizáció**  
Kifejezetten a következő generációs Windows eszközökhöz tervezett API-k, amelyek dedikált neurális feldolgozó egységekkel (NPU) kivételes teljesítményt nyújtanak watt-onként.

**Fejlesztői ökoszisztéma**  
Gazdag eszköztár, beleértve a Visual Studio integrációt, átfogó dokumentációt és mintapéldákat, amelyek felgyorsítják a fejlesztési ciklusokat.

## Tanulási célok

A Windows Edge AI fejlesztési útmutató elvégzésével elsajátíthatod azokat az alapvető készségeket, amelyek szükségesek a gyártásra kész AI alkalmazások létrehozásához a Windows platformon.

### Alapvető technikai kompetenciák

**Windows AI Foundry ismeretek**  
- Ismerd meg a Windows AI Foundry platform architektúráját és komponenseit  
- Navigálj az AI fejlesztési életciklusában a Windows ökoszisztémában  
- Valósíts meg biztonsági legjobb gyakorlatokat az eszközön futó AI alkalmazásokhoz  
- Optimalizáld az alkalmazásokat különböző Windows hardverkonfigurációkhoz  

**API integrációs szakértelem**  
- Sajátítsd el a Windows AI API-k használatát szöveg-, látás- és multimodális alkalmazásokhoz  
- Valósítsd meg a Phi Silica nyelvi modell integrációját szöveg generálásához és érveléshez  
- Telepíts számítógépes látási képességeket beépített képfeldolgozó API-k használatával  
- Testreszabott előképzett modellek létrehozása LoRA (Low-Rank Adaptation) technikákkal  

**Foundry Local implementáció**  
- Böngéssz, értékelj és telepíts nyílt forráskódú nyelvi modelleket a Foundry Local CLI segítségével  
- Értsd meg a modell optimalizálását és kvantálását a helyi telepítéshez  
- Valósíts meg offline AI képességeket, amelyek internetkapcsolat nélkül is működnek  
- Kezeld a modellek életciklusát és frissítéseit gyártási környezetben  

**Windows ML telepítés**  
- Hozz létre egyedi ONNX modelleket Windows alkalmazásokhoz a Windows ML segítségével  
- Használd ki az automatikus hardvergyorsítást CPU, GPU és NPU architektúrákon  
- Valósíts meg valós idejű következtetést optimális erőforrás-felhasználással  
- Tervezd meg a skálázható AI alkalmazásokat különböző Windows eszközkategóriákhoz  

### Alkalmazásfejlesztési készségek

**Keresztplatformos Windows fejlesztés**  
- Hozz létre AI-alapú alkalmazásokat .NET MAUI használatával univerzális Windows telepítéshez  
- Integrálj AI képességeket Win32, UWP és Progresszív Webalkalmazásokba  
- Valósíts meg reszponzív felhasználói felületeket, amelyek alkalmazkodnak az AI feldolgozási állapotaihoz  
- Kezeld az aszinkron AI műveleteket megfelelő felhasználói élmény mintákkal  

**Teljesítményoptimalizálás**  
- Profilozd és optimalizáld az AI következtetési teljesítményt különböző hardverkonfigurációkban  
- Valósíts meg hatékony memóriahasználatot nagy nyelvi modellekhez  
- Tervezd meg az alkalmazásokat, hogy azok fokozatosan csökkentsék a funkciókat a rendelkezésre álló hardver képességei alapján  
- Alkalmazz gyorsítótárazási stratégiákat a gyakran használt AI műveletekhez  

**Gyártási készenlét**  
- Valósíts meg átfogó hibakezelési és tartalék mechanizmusokat  
- Tervezd meg a telemetriát és a monitorozást az AI alkalmazások teljesítményéhez  
- Alkalmazz biztonsági legjobb gyakorlatokat a helyi AI modell tárolásához és végrehajtásához  
- Tervezd meg a telepítési stratégiákat vállalati és fogyasztói alkalmazásokhoz  

### Üzleti és stratégiai megértés

**AI alkalmazás architektúra**  
- Tervezd meg a hibrid architektúrákat, amelyek optimalizálják a helyi és felhő AI feldolgozást  
- Értékeld a kompromisszumokat a modell mérete, pontossága és következtetési sebessége között  
- Tervezd meg az adatáramlási architektúrákat, amelyek megőrzik a magánéletet, miközben intelligenciát biztosítanak  
- Valósíts meg költséghatékony AI megoldásokat, amelyek a felhasználói igényekkel skálázódnak  

**Piaci pozicionálás**  
- Értsd meg a Windows-alapú AI alkalmazások versenyelőnyeit  
- Azonosítsd azokat a felhasználási eseteket, ahol az eszközön futó AI jobb felhasználói élményt nyújt  
- Fejlessz piacra lépési stratégiákat AI-val bővített Windows alkalmazásokhoz  
- Pozicionáld az alkalmazásokat, hogy kihasználják a Windows ökoszisztéma előnyeit  

## Windows App SDK AI minták

A Windows App SDK átfogó mintákat biztosít, amelyek bemutatják az AI integrációt különböző keretrendszerekben és telepítési forgatókönyvekben. Ezek a minták alapvető referenciák a Windows AI fejlesztési minták megértéséhez.

### Windows AI Foundry minták

| Minta | Keretrendszer | Fókuszterület | Főbb jellemzők |
|-------|---------------|--------------|----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API-k integrációja | Teljes WinUI alkalmazás, amely bemutatja a Windows AI API-kat, ARM64 optimalizációt, csomagolt telepítést |

**Főbb technológiák:**  
- Windows AI API-k  
- WinUI 3 keretrendszer  
- ARM64 platform optimalizáció  
- Copilot+ PC kompatibilitás  
- Csomagolt alkalmazás telepítés  

**Előfeltételek:**  
- Windows 11 Copilot+ PC ajánlott  
- Visual Studio 2022  
- ARM64 build konfiguráció  
- Windows App SDK 1.8.1+  

### Windows ML minták

#### C++ minták

| Minta | Típus | Fókuszterület | Főbb jellemzők |
|-------|-------|--------------|----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzol alkalmazás | Alap Windows ML | EP felfedezés, parancssori opciók, modell fordítás |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzol alkalmazás | Keretrendszer telepítés | Megosztott futtatókörnyezet, kisebb telepítési lábnyom |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzol alkalmazás | Önálló telepítés | Önálló telepítés, nincs futtatókörnyezet függőség |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Könyvtár használat | WindowsML megosztott könyvtárban, memória kezelés |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet oktatóanyag | Modell konverzió, EP fordítás, Build 2025 oktatóanyag |

#### C# minták

**Konzol alkalmazások**

| Minta | Típus | Fókuszterület | Főbb jellemzők |
|-------|-------|--------------|----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzol alkalmazás | Alap C# integráció | Megosztott segédhasználat, parancssori felület |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet oktatóanyag | Modell konverzió, EP fordítás, Build 2025 oktatóanyag |

**GUI alkalmazások**

| Minta | Keretrendszer | Fókuszterület | Főbb jellemzők |
|-------|---------------|--------------|----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Asztali GUI | Képosztályozás WPF felülettel |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Hagyományos GUI | Képosztályozás Windows Forms használatával |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | Képosztályozás WinUI 3 felülettel |

#### Python minták

| Minta | Nyelv | Fókuszterület | Főbb jellemzők |
|-------|-------|--------------|----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Képosztályozás | WinML Python kötés, kötegelt képfeldolgozás |

### Minták előfeltételei

**Rendszerkövetelmények:**  
- Windows 11 PC, amely a 24H2 (build 26100) vagy újabb verziót futtatja  
- Visual Studio 2022 C++ és .NET munkaterhelésekkel  
- Windows App SDK 1.8.1 vagy újabb  
- Python 3.10-3.13 Python mintákhoz x64 és ARM64 eszközökön  

**Windows AI Foundry specifikus:**  
- Copilot+ PC ajánlott az optimális teljesítményhez  
- ARM64 build konfiguráció a Windows AI mintákhoz  
- Csomagazonosító szükséges (a csomagolatlan alkalmazások már nem támogatottak)  

### Általános minta munkafolyamat

A legtöbb Windows ML minta az alábbi szabványos mintát követi:

1. **Környezet inicializálása** – ONNX Runtime környezet létrehozása  
2. **Végrehajtási szolgáltatók regisztrálása** – Elérhető hardvergyorsítók felfedezése és regisztrálása (CPU, GPU, NPU)  
3. **Modell betöltése** – ONNX modell betöltése, opcionálisan fordítás a célhardverhez  
4. **Bemenet előfeldolgozása** – Képek/adatok átalakítása a modell bemeneti formátumára  
5. **Következtetés futtatása** – Modell végrehajtása és előrejelzések megszerzése  
6. **Eredmények feldolgozása** – Softmax alkalmazása és a legjobb előrejelzések megjelenítése  

### Használt modell fájlok

| Modell | Cél | Tartalmazott | Megjegyzések |
|-------|-----|--------------|--------------|
| SqueezeNet | Könnyű képosztályozás | ✅ Tartalmazott | Előre betanított, azonnal használható |
| ResNet-50 | Nagy pontosságú képosztályozás | ❌ Konverzió szükséges | Használja az [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) eszközt a konverzióhoz |

### Hardvertámogatás

Minden minta automatikusan felismeri és kihasználja az elérhető hardvert:  
- **CPU** – Univerzális támogatás minden Windows eszközön  
- **GPU** – Automatikus felismerés és optimalizálás az elérhető grafikus hardverhez  
- **NPU** – Neurális feldolgozó egységek kihasználása támogatott eszközökön (Copilot+ PC-k)  

## Windows AI Foundry platform komponensek

### 1. Windows AI API-k

A Windows AI API-k kész AI képességeket biztosítanak, amelyeket eszközön futó modellek hajtanak végre, optimalizálva a hatékonyságot és teljesítményt a Copilot+ PC eszközökön, minimális beállítási igénnyel.

#### Alapvető API kategóriák

**Phi Silica nyelvi modell**  
- Kicsi, de erőteljes nyelvi modell szöveg generálásához és érveléshez  
- Optimalizált valós idejű következtetéshez minimális energiafogyasztással  
- Támogatás egyedi finomhangoláshoz LoRA technikák használatával  
- Integráció a Windows szemantikus kereséssel és tudásvisszakereséssel  

**Számítógépes látás API-k**  
- **Szövegfelismerés (OCR)**: Szöveg kinyerése képekből nagy pontossággal  
- **Képszuperfelbontás**: Képek felskálázása helyi AI modellek használatával  
- **Képszegmentálás**: Specifikus objektumok azonosítása és elkülönítése képeken  
- **Képleírás**: Részletes szöveges leírások generálása vizuális tartalomhoz  
- **Objektum törlése**: Nem kívánt objektumok eltávolítása képekről AI-alapú kitöltéssel  

**Multimodális képességek**  
- **Látás-nyelv integráció**: Szöveg és kép megértésének kombinálása  
- **Szemantikus keresés**: Természetes nyelvű lekérdezések engedélyezése multimédiás tartalmakban  
- **Tudásvisszakeresés**: Intelligens keresési élmények építése helyi adatokkal  

### 2. Foundry Local

A Foundry Local gyors hozzáférést biztosít a fejlesztők számára kész nyílt for
- **Funkciók**: Modellválasztó, folyamatos válaszok, hibakezelés, platformfüggetlen telepítés
- **Architektúra**: Electron fő folyamat, IPC kommunikáció, biztonságos előtöltési szkriptek

**SDK Integrációs Példák**
- **JavaScript (Node.js)**: Alapvető modellinterakció és folyamatos válaszok
- **Python**: OpenAI-kompatibilis API használata aszinkron streaminggel
- **Rust**: Alacsony szintű integráció reqwest és tokio segítségével aszinkron műveletekhez

#### Előfeltételek a Foundry Local mintákhoz

**Rendszerkövetelmények:**
- Windows 11 Foundry Local telepítéssel
- Node.js v16+ JavaScript/Electron mintákhoz
- .NET 8.0+ C# mintákhoz
- Python 3.10+ Python mintákhoz
- Rust 1.70+ Rust mintákhoz

**Telepítés:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Mintaspecifikus beállítás

**dotNET RAG minta:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat minta:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust minták:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Főbb funkciók

**Modellkatalógus**
- Átfogó gyűjtemény előre optimalizált nyílt forráskódú modellekből
- Modellek optimalizálása CPU-k, GPU-k és NPU-k számára azonnali telepítéshez
- Támogatás népszerű modelltípusokhoz, mint például Llama, Mistral, Phi, és speciális területi modellek

**CLI Integráció**
- Parancssoros felület modellkezeléshez és telepítéshez
- Automatizált optimalizálási és kvantálási munkafolyamatok
- Integráció népszerű fejlesztési környezetekkel és CI/CD csatornákkal

**Helyi telepítés**
- Teljes offline működés felhőfüggőségek nélkül
- Támogatás egyedi modellformátumokhoz és konfigurációkhoz
- Hatékony modellkiszolgálás automatikus hardveroptimalizálással

### 3. Windows ML

A Windows ML a Windows alapvető AI platformja és integrált inferencia futtatókörnyezete, amely lehetővé teszi a fejlesztők számára, hogy hatékonyan telepítsenek egyedi modelleket a széles Windows hardverökoszisztémán.

#### Architektúra előnyei

**Univerzális hardvertámogatás**
- Automatikus optimalizálás AMD, Intel, NVIDIA és Qualcomm chipekhez
- Támogatás CPU, GPU és NPU végrehajtáshoz átlátható váltással
- Hardverabsztrakció, amely megszünteti a platformspecifikus optimalizálási munkát

**Modellrugalmasság**
- Támogatás az ONNX modellformátumhoz, automatikus konverzióval népszerű keretrendszerekből
- Egyedi modellek telepítése gyártási szintű teljesítménnyel
- Integráció meglévő Windows alkalmazásarchitektúrákkal

**Vállalati integráció**
- Kompatibilitás a Windows biztonsági és megfelelőségi keretrendszereivel
- Támogatás vállalati telepítési és kezelési eszközökhöz
- Integráció a Windows eszközkezelési és monitorozási rendszerekkel

## Fejlesztési munkafolyamat

### 1. fázis: Környezet beállítása és eszközkonfiguráció

**Fejlesztési környezet előkészítése**
1. Telepítse a Visual Studio 2022-t C++ és .NET munkaterhelésekkel
2. Telepítse a Windows App SDK 1.8.1 vagy újabb verzióját
3. Konfigurálja a Windows AI Foundry CLI eszközöket
4. Állítsa be az AI Toolkit bővítményt a Visual Studio Code-hoz
5. Hozzon létre teljesítményprofilozási és monitorozási eszközöket
6. Biztosítsa az ARM64 build konfigurációt a Copilot+ PC optimalizáláshoz

**Minta-repozitórium beállítása**
1. Klónozza a [Windows App SDK Samples repozitóriumot](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigáljon a `Samples/WindowsAIFoundry/cs-winui` mappába Windows AI API példákért
3. Navigáljon a `Samples/WindowsML` mappába átfogó Windows ML példákért
4. Tekintse át a [build követelményeket](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) a célplatformokhoz

**AI Dev Galéria felfedezése**
- Fedezze fel a mintapéldákat és referenciamegvalósításokat
- Tesztelje a Windows AI API-kat interaktív bemutatókkal
- Tekintse át a forráskódot a legjobb gyakorlatok és minták érdekében
- Azonosítsa az Ön konkrét felhasználási esetéhez releváns mintákat

### 2. fázis: Modellválasztás és integráció

**Követelményelemzés**
- Határozza meg az AI képességek funkcionális követelményeit
- Állítsa fel a teljesítménykorlátokat és optimalizálási célokat
- Értékelje a magánélet és biztonság követelményeit
- Tervezze meg a telepítési architektúrát és skálázási stratégiákat

**Modellértékelés**
- Használja a Foundry Local-t nyílt forráskódú modellek tesztelésére az Ön felhasználási esetéhez
- Benchmarkolja a Windows AI API-kat az egyedi modellkövetelményekkel szemben
- Értékelje a kompromisszumokat a modellméret, pontosság és inferencia sebesség között
- Prototípus integrációs megközelítéseket a kiválasztott modellekkel

### 3. fázis: Alkalmazásfejlesztés

**Alapvető integráció**
- Valósítsa meg a Windows AI API integrációt megfelelő hibakezeléssel
- Tervezzen felhasználói felületeket, amelyek támogatják az AI feldolgozási munkafolyamatokat
- Valósítson meg gyorsítótárazási és optimalizálási stratégiákat a modellinferencia számára
- Adjon hozzá telemetriát és monitorozást az AI működési teljesítményéhez

**Tesztelés és validáció**
- Tesztelje az alkalmazásokat különböző Windows hardverkonfigurációkon
- Validálja a teljesítménymutatókat különböző terhelési feltételek mellett
- Valósítson meg automatizált tesztelést az AI funkciók megbízhatóságához
- Végezzen felhasználói élménytesztelést AI-val bővített funkciókkal

### 4. fázis: Optimalizálás és telepítés

**Teljesítményoptimalizálás**
- Profilozza az alkalmazás teljesítményét a célhardver-konfigurációkon
- Optimalizálja a memóriahasználatot és a modellbetöltési stratégiákat
- Valósítson meg adaptív viselkedést a rendelkezésre álló hardver képességei alapján
- Finomhangolja a felhasználói élményt különböző teljesítményforgatókönyvekhez

**Gyártási telepítés**
- Csomagolja az alkalmazásokat megfelelő AI modellfüggőségekkel
- Valósítson meg frissítési mechanizmusokat a modellekhez és az alkalmazáslogikához
- Konfigurálja a monitorozást és analitikát a gyártási környezetekhez
- Tervezze meg a bevezetési stratégiákat vállalati és fogyasztói telepítésekhez

## Gyakorlati megvalósítási példák

### Példa 1: Intelligens dokumentumfeldolgozó alkalmazás

Hozzon létre egy Windows alkalmazást, amely több AI képességet használ dokumentumok feldolgozásához:

**Használt technológiák:**
- Phi Silica dokumentumösszegzéshez és kérdés-válaszhoz
- OCR API-k szövegkinyeréshez szkennelt dokumentumokból
- Képleíró API-k diagramok és grafikonok elemzéséhez
- Egyedi ONNX modellek dokumentumosztályozáshoz

**Megvalósítási megközelítés:**
- Tervezzen moduláris architektúrát cserélhető AI komponensekkel
- Valósítson meg aszinkron feldolgozást nagy dokumentumcsomagokhoz
- Adjon hozzá folyamatjelzőket és megszakítási támogatást hosszú műveletekhez
- Tartalmazzon offline képességet érzékeny dokumentumfeldolgozáshoz

### Példa 2: Kiskereskedelmi készletkezelő rendszer

Hozzon létre AI-alapú készletkezelő rendszert kiskereskedelmi alkalmazásokhoz:

**Használt technológiák:**
- Képszegmentálás termékazonosításhoz
- Egyedi látásmodellek márka- és kategóriaosztályozáshoz
- Foundry Local telepítése speciális kiskereskedelmi nyelvi modellekhez
- Integráció meglévő POS és készletkezelő rendszerekkel

**Megvalósítási megközelítés:**
- Építsen kameraintegrációt valós idejű termékszkenneléshez
- Valósítson meg vonalkód- és vizuális termékfelismerést
- Adjon hozzá természetes nyelvi készletlekérdezéseket helyi nyelvi modellek használatával
- Tervezzen skálázható architektúrát több üzlet telepítéséhez

### Példa 3: Egészségügyi dokumentációs asszisztens

Fejlesszen adatvédelmet biztosító egészségügyi dokumentációs eszközt:

**Használt technológiák:**
- Phi Silica orvosi jegyzetek generálásához és klinikai döntéstámogatáshoz
- OCR kézzel írt orvosi feljegyzések digitalizálásához
- Egyedi orvosi nyelvi modellek telepítése Windows ML-en keresztül
- Helyi vektortárolás orvosi tudás visszakereséséhez

**Megvalósítási megközelítés:**
- Biztosítsa a teljes offline működést a betegadatok védelme érdekében
- Valósítson meg orvosi terminológia validálást és javaslatokat
- Adjon hozzá auditnaplózást a szabályozási megfeleléshez
- Tervezzen integrációt meglévő elektronikus egészségügyi nyilvántartási rendszerekkel

## Teljesítményoptimalizálási stratégiák

### Hardver-tudatos fejlesztés

**NPU optimalizálás**
- Tervezzen alkalmazásokat az NPU képességek kihasználására Copilot+ PC-ken
- Valósítson meg zökkenőmentes visszaállást GPU/CPU-ra NPU nélküli eszközökön
- Optimalizálja a modellformátumokat NPU-specifikus gyorsításra
- Monitorozza az NPU kihasználtságát és hőmérsékleti jellemzőit

**Memóriakezelés**
- Valósítson meg hatékony modellbetöltési és gyorsítótárazási stratégiákat
- Használjon memóriatérképezést nagy modellekhez az indítási idő csökkentésére
- Tervezzen memória-tudatos alkalmazásokat erőforrás-korlátozott eszközökhöz
- Valósítson meg modellkvantálást a memóriaoptimalizálás érdekében

**Akkumulátorhatékonyság**
- Optimalizálja az AI műveleteket minimális energiafogyasztásra
- Valósítson meg adaptív feldolgozást az akkumulátor állapota alapján
- Tervezzen hatékony háttérfeldolgozást folyamatos AI műveletekhez
- Használjon energia-profilozó eszközöket az energiafelhasználás optimalizálására

### Skálázhatósági szempontok

**Többszálúság**
- Tervezzen szálbiztos AI műveleteket párhuzamos feldolgozáshoz
- Valósítson meg hatékony munkamegosztást a rendelkezésre álló magok között
- Használjon async/await mintákat nem blokkoló AI műveletekhez
- Tervezze meg a szálcsoport optimalizálását különböző hardverkonfigurációkhoz

**Gyorsítótárazási stratégiák**
- Valósítson meg intelligens gyorsítótárazást gyakran használt AI műveletekhez
- Tervezzen gyorsítótár érvénytelenítési stratégiákat modellfrissítésekhez
- Használjon tartós gyorsítótárazást drága előfeldolgozási műveletekhez
- Valósítson meg elosztott gyorsítótárazást többfelhasználós forgatókönyvekhez

## Biztonsági és adatvédelmi legjobb gyakorlatok

### Adatvédelem

**Helyi feldolgozás**
- Biztosítsa, hogy érzékeny adatok soha ne hagyják el a helyi eszközt
- Valósítson meg biztonságos tárolást AI modellekhez és ideiglenes adatokhoz
- Használja a Windows biztonsági funkcióit az alkalmazás sandboxolásához
- Alkalmazzon titkosítást a tárolt modellekhez és köztes feldolgozási eredményekhez

**Modellbiztonság**
- Validálja a modell integritását betöltés és végrehajtás előtt
- Valósítson meg biztonságos modellfrissítési mechanizmusokat
- Használjon aláírt modelleket a manipuláció megelőzésére
- Alkalmazzon hozzáférés-vezérlést a modellfájlokhoz és konfigurációkhoz

### Megfelelőségi szempontok

**Szabályozási igazodás**
- Tervezzen alkalmazásokat GDPR, HIPAA és más szabályozási követelményeknek megfelelően
- Valósítson meg auditnaplózást az AI döntéshozatali folyamatokhoz
- Biztosítson átláthatósági funkciókat az AI által generált eredményekhez
- Tegye lehetővé a felhasználók számára az AI adatfeldolgozás feletti kontrollt

**Vállalati biztonság**
- Integrálja a Windows vállalati biztonsági irányelveivel
- Támogassa a kezelt telepítést vállalati kezelőeszközökön keresztül
- Valósítson meg szerepkör-alapú hozzáférés-vezérlést az AI funkciókhoz
- Biztosítson adminisztratív kontrollokat az AI funkcionalitáshoz

## Hibakeresés és problémamegoldás

### Gyakori fejlesztési kihívások

**Build konfigurációs problémák**
- Biztosítsa az ARM64 platform konfigurációt a Windows AI API mintákhoz
- Ellenőrizze a Windows App SDK verziókompatibilitást (1.8.1+ szükséges)
- Ellenőrizze, hogy a csomagazonosság megfelelően van-e konfigurálva (szükséges a Windows AI API-khoz)
- Validálja, hogy a build eszközök támogatják-e a célkeretrendszer verzióját

**Modellbetöltési problémák**
- Validálja az ONNX modellkompatibilitást a Windows ML-lel
- Ellenőrizze a modellfájl integritását és formátumkövetelményeit
- Ellenőrizze a hardver képességkövetelményeket az adott modellekhez
- Hibakeresés memóriaallokációs problémák esetén modellbetöltéskor
- Biztosítsa a végrehajtási szolgáltató regisztrációját hardvergyorsításhoz

**Telepítési mód szempontok**
- **Önálló mód**: Teljesen támogatott, nagyobb telepítési mérettel
- **Keretrendszer-függő mód**: Kisebb méret, de megosztott futtatókörnyezetet igényel
- **Csomagolatlan alkalmazások**: Már nem támogatott a Windows AI API-khoz
- Használja a `dotnet run -p:Platform=ARM64 -p:SelfContained=true` parancsot önálló ARM64 telepítéshez

**Teljesítményproblémák**
- Profiloz
- [Windows App SDK Minták Tára](https://github.com/microsoft/WindowsAppSDK-Samples)

### Fejlesztői Eszközök
- [AI Eszköztár a Visual Studio Code-hoz](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Fejlesztői Galéria](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Minták](https://learn.microsoft.com/windows/ai/samples/)
- [Modellek Konvertálási Eszközei](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technikai Támogatás
- [Windows ML Dokumentáció](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentáció](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentáció](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Hibák Jelentése - Windows App SDK Minták](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Közösség és Támogatás
- [Windows Fejlesztői Közösség](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Képzések](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ez az útmutató a gyorsan fejlődő Windows AI ökoszisztémával együtt változik. A rendszeres frissítések biztosítják az összhangot a legújabb platformképességekkel és fejlesztési legjobb gyakorlatokkal.*

[08. Gyakorlati Munka a Microsoft Foundry Local-lal - Teljes Fejlesztői Eszköztár](../Module08/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.