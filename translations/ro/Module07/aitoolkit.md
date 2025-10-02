<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T14:21:49+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "ro"
}
-->
# AI Toolkit pentru Visual Studio Code - Ghid de Dezvoltare Edge AI

## Introducere

Bine ați venit la ghidul complet pentru utilizarea AI Toolkit în Visual Studio Code pentru dezvoltarea Edge AI. Pe măsură ce inteligența artificială se mută de la calculul centralizat în cloud la dispozitivele distribuite de tip edge, dezvoltatorii au nevoie de instrumente puternice și integrate care să gestioneze provocările unice ale implementării la margine - de la constrângerile de resurse la cerințele de funcționare offline.

AI Toolkit pentru Visual Studio Code acoperă acest gol, oferind un mediu complet de dezvoltare special conceput pentru construirea, testarea și optimizarea aplicațiilor AI care rulează eficient pe dispozitive edge. Indiferent dacă dezvoltați pentru senzori IoT, dispozitive mobile, sisteme integrate sau servere edge, acest toolkit simplifică întregul flux de lucru de dezvoltare în cadrul mediului familiar VS Code.

Acest ghid vă va conduce prin conceptele esențiale, instrumentele și cele mai bune practici pentru utilizarea AI Toolkit în proiectele Edge AI, de la selecția inițială a modelului până la implementarea în producție.

## Prezentare Generală

AI Toolkit pentru Visual Studio Code este o extensie puternică ce simplifică dezvoltarea agenților și crearea aplicațiilor AI. Toolkit-ul oferă capabilități complete pentru explorarea, evaluarea și implementarea modelelor AI de la o gamă largă de furnizori—incluzând Anthropic, OpenAI, GitHub, Google—în timp ce susține execuția locală a modelelor folosind ONNX și Ollama.

Ceea ce diferențiază AI Toolkit este abordarea sa cuprinzătoare asupra întregului ciclu de viață al dezvoltării AI. Spre deosebire de instrumentele tradiționale de dezvoltare AI care se concentrează pe aspecte individuale, AI Toolkit oferă un mediu integrat care acoperă descoperirea modelelor, experimentarea, dezvoltarea agenților, evaluarea și implementarea—totul în cadrul mediului familiar VS Code.

Platforma este special concepută pentru prototipare rapidă și implementare în producție, cu funcții precum generarea de prompturi, inițieri rapide, integrarea fără probleme a instrumentelor MCP (Model Context Protocol) și capabilități extinse de evaluare. Pentru dezvoltarea Edge AI, acest lucru înseamnă că puteți dezvolta, testa și optimiza eficient aplicații AI pentru scenarii de implementare la margine, menținând în același timp întregul flux de lucru de dezvoltare în VS Code.

## Obiective de Învățare

Până la finalul acestui ghid, veți putea:

### Competențe de Bază
- **Instala și configura** AI Toolkit pentru Visual Studio Code pentru fluxurile de lucru de dezvoltare Edge AI
- **Naviga și utiliza** interfața AI Toolkit, incluzând Catalogul de Modele, Playground și Agent Builder
- **Selecta și evalua** modele AI potrivite pentru implementarea la margine, bazate pe performanță și constrângeri de resurse
- **Converti și optimiza** modele folosind formatul ONNX și tehnici de cuantizare pentru dispozitive edge

### Abilități de Dezvoltare Edge AI
- **Proiecta și implementa** aplicații Edge AI folosind mediul integrat de dezvoltare
- **Testa modele** în condiții similare cu cele de la margine, utilizând inferența locală și monitorizarea resurselor
- **Crea și personaliza** agenți AI optimizați pentru scenarii de implementare la margine
- **Evalua performanța modelelor** utilizând metrici relevante pentru calculul la margine (latență, utilizarea memoriei, acuratețe)

### Optimizare și Implementare
- **Aplica tehnici de cuantizare și reducere** pentru a micșora dimensiunea modelelor, menținând performanța acceptabilă
- **Optimiza modele** pentru platforme hardware edge specifice, incluzând accelerarea CPU, GPU și NPU
- **Implementa cele mai bune practici** pentru dezvoltarea Edge AI, incluzând gestionarea resurselor și strategii de rezervă
- **Pregăti modele și aplicații** pentru implementarea în producție pe dispozitive edge

### Concepte Avansate Edge AI
- **Integra cu cadre Edge AI** incluzând ONNX Runtime, Windows ML și TensorFlow Lite
- **Implementa arhitecturi multi-model** și scenarii de învățare federată pentru medii edge
- **Depana probleme comune Edge AI** incluzând constrângerile de memorie, viteza inferenței și compatibilitatea hardware
- **Proiecta strategii de monitorizare și logare** pentru aplicațiile Edge AI în producție

### Aplicare Practică
- **Construi soluții Edge AI complete** de la selecția modelului până la implementare
- **Demonstra competență** în fluxurile de lucru specifice dezvoltării la margine și tehnicile de optimizare
- **Aplica conceptele învățate** la cazuri reale de utilizare Edge AI, incluzând IoT, mobil și aplicații integrate
- **Evalua și compara** diferite strategii de implementare Edge AI și compromisurile acestora

## Funcții Cheie pentru Dezvoltarea Edge AI

### 1. Catalog de Modele și Descoperire
- **Suport Multi-Furnizor**: Navigați și accesați modele AI de la Anthropic, OpenAI, GitHub, Google și alți furnizori
- **Integrare Locală a Modelelor**: Descoperire simplificată a modelelor ONNX și Ollama pentru implementarea la margine
- **Modele GitHub**: Integrare directă cu găzduirea modelelor GitHub pentru acces simplificat
- **Comparație Modele**: Comparați modele unul lângă altul pentru a găsi echilibrul optim pentru constrângerile dispozitivelor edge

### 2. Playground Interactiv
- **Mediu de Testare Interactiv**: Experimentare rapidă cu capabilitățile modelelor într-un mediu controlat
- **Suport Multi-modal**: Testați cu imagini, text și alte intrări tipice în scenarii edge
- **Experimentare în Timp Real**: Feedback imediat asupra răspunsurilor și performanței modelelor
- **Optimizare Parametri**: Ajustați parametrii modelelor pentru cerințele de implementare la margine

### 3. Builder de Prompturi (Agenți)
- **Generare Naturală de Limbaj**: Generați prompturi inițiale folosind descrieri în limbaj natural
- **Rafinare Iterativă**: Îmbunătățiți prompturile bazate pe răspunsurile și performanța modelelor
- **Decompoziție de Sarcini**: Fragmentați sarcini complexe cu lanțuri de prompturi și ieșiri structurate
- **Suport pentru Variabile**: Utilizați variabile în prompturi pentru comportament dinamic al agenților
- **Generare Cod de Producție**: Generați cod gata de producție pentru dezvoltare rapidă de aplicații

### 4. Execuție și Evaluare în Masă
- **Testare Multi-Model**: Rulați mai multe prompturi pe modele selectate simultan
- **Testare Eficientă la Scară**: Testați diverse intrări și configurații eficient
- **Cazuri de Testare Personalizate**: Rulați agenți cu cazuri de testare pentru validarea funcționalității
- **Comparație Performanță**: Comparați rezultatele între diferite modele și configurații

### 5. Evaluarea Modelelor cu Seturi de Date
- **Metrici Standard**: Testați modele AI folosind evaluatori încorporați (scor F1, relevanță, similaritate, coerență)
- **Evaluatori Personalizați**: Creați propriile metrici de evaluare pentru cazuri de utilizare specifice
- **Integrare Seturi de Date**: Testați modele împotriva seturilor de date cuprinzătoare
- **Măsurarea Performanței**: Cuantificați performanța modelelor pentru decizii de implementare la margine

### 6. Capabilități de Fine-tuning
- **Personalizare Model**: Personalizați modele pentru cazuri de utilizare și domenii specifice
- **Adaptare Specializată**: Adaptați modele la cerințe și domenii specializate
- **Optimizare Edge**: Ajustați modele special pentru constrângerile de implementare la margine
- **Antrenament Specific Domeniului**: Creați modele adaptate la cazuri de utilizare edge specifice

### 7. Integrare Instrumente MCP
- **Conectivitate Instrumente Externe**: Conectați agenți la instrumente externe prin servere Model Context Protocol
- **Acțiuni în Lumea Reală**: Permiteți agenților să interogheze baze de date, să acceseze API-uri sau să execute logică personalizată
- **Servere MCP Existente**: Utilizați instrumente din protocoale de comandă (stdio) sau HTTP (evenimente server-sent)
- **Dezvoltare MCP Personalizată**: Construiți și creați noi servere MCP cu testare în Agent Builder

### 8. Dezvoltare și Testare Agenți
- **Suport pentru Apelarea Funcțiilor**: Permiteți agenților să invoce funcții externe dinamic
- **Testare Integrare în Timp Real**: Testați integrările cu rulări în timp real și utilizarea instrumentelor
- **Versionare Agenți**: Controlul versiunilor pentru agenți cu capabilități de comparație a rezultatelor evaluării
- **Depanare și Urmărire**: Capabilități locale de urmărire și depanare pentru dezvoltarea agenților

## Flux de Lucru pentru Dezvoltarea Edge AI

### Faza 1: Descoperirea și Selecția Modelului
1. **Explorați Catalogul de Modele**: Utilizați catalogul de modele pentru a găsi modele potrivite pentru implementarea la margine
2. **Comparați Performanța**: Evaluați modelele bazate pe dimensiune, acuratețe și viteza inferenței
3. **Testați Local**: Utilizați modele Ollama sau ONNX pentru testare locală înainte de implementarea la margine
4. **Evaluați Cerințele de Resurse**: Determinați nevoile de memorie și calcul pentru dispozitivele edge țintă

### Faza 2: Optimizarea Modelului
1. **Convertiți în ONNX**: Convertiți modelele selectate în format ONNX pentru compatibilitate edge
2. **Aplicați Cuantizare**: Reduceți dimensiunea modelelor prin cuantizare INT8 sau INT4
3. **Optimizare Hardware**: Optimizați pentru hardware edge țintă (ARM, x86, acceleratoare specializate)
4. **Validare Performanță**: Validați că modelele optimizate mențin acuratețea acceptabilă

### Faza 3: Dezvoltarea Aplicației
1. **Proiectare Agenți**: Utilizați Agent Builder pentru a crea agenți AI optimizați pentru margine
2. **Inginerie Prompturi**: Dezvoltați prompturi care funcționează eficient cu modele edge mai mici
3. **Testare Integrare**: Testați agenții în condiții simulate de margine
4. **Generare Cod**: Generați cod de producție optimizat pentru implementarea la margine

### Faza 4: Evaluare și Testare
1. **Evaluare în Masă**: Testați multiple configurații pentru a găsi setările optime edge
2. **Profilare Performanță**: Analizați viteza inferenței, utilizarea memoriei și acuratețea
3. **Simulare Margine**: Testați în condiții similare cu mediul de implementare edge țintă
4. **Testare de Rezistență**: Evaluați performanța sub diverse condiții de încărcare

### Faza 5: Pregătirea pentru Implementare
1. **Optimizare Finală**: Aplicați optimizări finale bazate pe rezultatele testării
2. **Ambalare pentru Implementare**: Pregătiți modelele și codul pentru implementarea la margine
3. **Documentare**: Documentați cerințele și configurația implementării
4. **Configurare Monitorizare**: Pregătiți monitorizarea și logarea pentru implementarea la margine

## Publicul Țintă pentru Dezvoltarea Edge AI

### Dezvoltatori Edge AI
- Dezvoltatori de aplicații care construiesc dispozitive edge și soluții IoT alimentate de AI
- Dezvoltatori de sisteme integrate care integrează capabilități AI în dispozitive cu resurse limitate
- Dezvoltatori de aplicații mobile care creează aplicații AI pe dispozitive

### Ingineri Edge AI
- Ingineri AI care optimizează modele pentru implementarea la margine și gestionează fluxurile de inferență
- Ingineri DevOps care implementează și gestionează modele AI pe infrastructura edge distribuită
- Ingineri de performanță care optimizează sarcinile AI pentru constrângerile hardware edge

### Cercetători și Educatori
- Cercetători AI care dezvoltă modele și algoritmi eficienți pentru calculul la margine
- Educatori care predau concepte Edge AI și demonstrează tehnici de optimizare
- Studenți care învață despre provocările și soluțiile în implementarea Edge AI

## Cazuri de Utilizare Edge AI

### Dispozitive IoT Inteligente
- **Recunoaștere Imagine în Timp Real**: Implementați modele de viziune computerizată pe camere și senzori IoT
- **Procesare Vocală**: Implementați recunoaștere vocală și procesare de limbaj natural pe difuzoare inteligente
- **Întreținere Predictivă**: Rulați modele de detectare a anomaliilor pe dispozitive industriale edge
- **Monitorizare Ambientală**: Implementați modele de analiză a datelor senzoriale pentru aplicații de mediu

### Aplicații Mobile și Integrate
- **Traducere pe Dispozitiv**: Implementați modele de traducere lingvistică care funcționează offline
- **Realitate Augmentată**: Implementați recunoaștere și urmărire de obiecte în timp real pentru aplicații AR
- **Monitorizare Sănătate**: Rulați modele de analiză a sănătății pe dispozitive purtabile și echipamente medicale
- **Sisteme Autonome**: Implementați modele de luare a deciziilor pentru drone, roboți și vehicule

### Infrastructură de Calcul Edge
- **Centre de Date Edge**: Implementați modele AI în centre de date edge pentru aplicații cu latență redusă
- **Integrare CDN**: Integrați capabilități de procesare AI în rețelele de livrare de conținut
- **Edge 5G**: Utilizați calculul edge 5G pentru aplicații alimentate de AI
- **Calcul Fog**: Implementați procesare AI în medii de calcul fog

## Instalare și Configurare

### Instalarea Extensiei
Instalați extensia AI Toolkit direct din Visual Studio Code Marketplace:

**ID Extensie**: `ms-windows-ai-studio.windows-ai-studio`

**Metode de Instalare**:
1. **Marketplace VS Code**: Căutați "AI Toolkit" în vizualizarea Extensii
2. **Linie de Comandă**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalare Directă**: Descărcați de la [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Cerințe Prealabile pentru Dezvoltarea Edge AI
- **Visual Studio Code**: Recomandată ultima versiune
- **Mediu Python**: Python 3.8+ cu biblioteci AI necesare
- **ONNX Runtime** (Opțional): Pentru inferența modelelor ONNX
- **Ollama** (Opțional): Pentru servirea locală a modelelor
- **Instrumente de Accelerare Hardware**: CUDA, OpenVINO sau acceleratoare specifice platformei

### Configurare Inițială
1. **Activarea Extensiei**: Deschideți VS Code și verificați dacă AI Toolkit apare în Bara de Activitate
2. **Configurare Furnizori Modele**: Configurați accesul la GitHub, OpenAI, Anthropic sau alți furnizori de modele
3. **Mediu Local**: Configurați mediul Python și instalați pachetele necesare
4. **Accelerare Hardware**: Configurați accelerarea GPU/NPU dacă este disponibilă
5. **Integrare MCP**: Configurați serverele Model Context Protocol dacă este necesar

### Lista de Verificare pentru Prima Configurare
- [ ] Extensia AI Toolkit instalată și activată
- [ ] Catalogul de modele accesibil și modelele descoperibile
- [ ] Playground funcțional pentru testarea modelelor
- [ ] Agent Builder accesibil pentru dezvoltarea prompturilor
- [ ] Mediu de dezvoltare local configurat
- [ ] Accelerare hardware (dacă este disponibilă) configurată corect

## Începutul cu AI Toolkit

### Ghid de Start Rapid

Recomandăm să începeți cu modelele găzduite de Git
2. Generați prompturi de început folosind descrieri în limbaj natural  
3. Iterați și rafinați prompturile pe baza răspunsurilor modelului  
4. Integrați instrumentele MCP pentru capabilități avansate ale agenților  

#### Pasul 3: Testare și Evaluare  
1. Utilizați **Bulk Run** pentru a testa mai multe prompturi pe modele selectate  
2. Rulați agenți cu cazuri de test pentru a valida funcționalitatea  
3. Evaluați acuratețea și performanța folosind metrici integrate sau personalizate  
4. Comparați diferite modele și configurații  

#### Pasul 4: Ajustare și Optimizare  
1. Personalizați modelele pentru cazuri de utilizare specifice  
2. Aplicați ajustări specifice domeniului  
3. Optimizați pentru constrângerile de implementare la margine  
4. Versiuneați și comparați diferite configurații ale agenților  

#### Pasul 5: Pregătirea pentru Implementare  
1. Generați cod gata de producție folosind Agent Builder  
2. Configurați conexiunile serverului MCP pentru utilizare în producție  
3. Pregătiți pachetele de implementare pentru dispozitivele de margine  
4. Configurați metrici de monitorizare și evaluare  

## Cele mai bune practici pentru dezvoltarea AI la margine  

### Selectarea modelului  
- **Constrângeri de dimensiune**: Alegeți modele care se încadrează în limitele de memorie ale dispozitivelor țintă  
- **Viteză de inferență**: Prioritizați modelele cu timpi de inferență rapizi pentru aplicații în timp real  
- **Compromisuri de acuratețe**: Echilibrați acuratețea modelului cu constrângerile de resurse  
- **Compatibilitate format**: Preferă formatele ONNX sau optimizate pentru hardware pentru implementare la margine  

### Tehnici de optimizare  
- **Cuantizare**: Utilizați cuantizarea INT8 sau INT4 pentru a reduce dimensiunea modelului și a îmbunătăți viteza  
- **Pruning**: Eliminați parametrii inutili ai modelului pentru a reduce cerințele computaționale  
- **Distilarea cunoștințelor**: Creați modele mai mici care mențin performanța celor mai mari  
- **Accelerare hardware**: Folosiți NPUs, GPUs sau acceleratoare specializate, dacă sunt disponibile  

### Flux de lucru în dezvoltare  
- **Testare iterativă**: Testați frecvent în condiții similare cu cele de margine în timpul dezvoltării  
- **Monitorizarea performanței**: Monitorizați continuu utilizarea resurselor și viteza de inferență  
- **Controlul versiunilor**: Urmăriți versiunile modelului și setările de optimizare  
- **Documentare**: Documentați toate deciziile de optimizare și compromisurile de performanță  

### Considerații pentru implementare  
- **Monitorizarea resurselor**: Monitorizați memoria, CPU și consumul de energie în producție  
- **Strategii de rezervă**: Implementați mecanisme de rezervă pentru eșecurile modelului  
- **Mecanisme de actualizare**: Planificați actualizările modelului și gestionarea versiunilor  
- **Securitate**: Implementați măsuri de securitate adecvate pentru aplicațiile AI la margine  

## Integrarea cu cadrele AI la margine  

### ONNX Runtime  
- **Implementare multiplatformă**: Implementați modele ONNX pe diferite platforme de margine  
- **Optimizare hardware**: Folosiți optimizările specifice hardware ale ONNX Runtime  
- **Suport mobil**: Utilizați ONNX Runtime Mobile pentru aplicații pe smartphone-uri și tablete  
- **Integrare IoT**: Implementați pe dispozitive IoT folosind distribuțiile ușoare ale ONNX Runtime  

### Windows ML  
- **Dispozitive Windows**: Optimizați pentru dispozitive de margine și PC-uri bazate pe Windows  
- **Accelerare NPU**: Folosiți Unități de Procesare Neurală pe dispozitive Windows  
- **DirectML**: Utilizați DirectML pentru accelerare GPU pe platformele Windows  
- **Integrare UWP**: Integrați cu aplicațiile Universal Windows Platform  

### TensorFlow Lite  
- **Optimizare mobilă**: Implementați modele TensorFlow Lite pe dispozitive mobile și încorporate  
- **Delegări hardware**: Utilizați delegări hardware specializate pentru accelerare  
- **Microcontrolere**: Implementați pe microcontrolere folosind TensorFlow Lite Micro  
- **Suport multiplatformă**: Implementați pe Android, iOS și sisteme Linux încorporate  

### Azure IoT Edge  
- **Hibrid cloud-margine**: Combinați antrenarea în cloud cu inferența la margine  
- **Implementare module**: Implementați modele AI ca module IoT Edge  
- **Gestionarea dispozitivelor**: Gestionați dispozitivele de margine și actualizările modelului de la distanță  
- **Telemetrie**: Colectați date de performanță și metrici ale modelului din implementările la margine  

## Scenarii avansate AI la margine  

### Implementare multi-model  
- **Ensemble de modele**: Implementați mai multe modele pentru acuratețe îmbunătățită sau redundanță  
- **Testare A/B**: Testați simultan modele diferite pe dispozitive de margine  
- **Selecție dinamică**: Alegeți modele pe baza condițiilor curente ale dispozitivului  
- **Partajare resurse**: Optimizați utilizarea resurselor între modele implementate multiple  

### Învățare federată  
- **Antrenare distribuită**: Antrenați modele pe mai multe dispozitive de margine  
- **Păstrarea confidențialității**: Păstrați datele de antrenare local, partajând îmbunătățirile modelului  
- **Învățare colaborativă**: Permiteți dispozitivelor să învețe din experiențele colective  
- **Coordonare margine-cloud**: Coordonați învățarea între dispozitivele de margine și infrastructura cloud  

### Procesare în timp real  
- **Procesare fluxuri**: Procesați fluxuri continue de date pe dispozitive de margine  
- **Inferență cu latență redusă**: Optimizați pentru latență minimă de inferență  
- **Procesare loturi**: Procesați eficient loturi de date pe dispozitive de margine  
- **Procesare adaptivă**: Ajustați procesarea pe baza capacităților curente ale dispozitivului  

## Depanarea dezvoltării AI la margine  

### Probleme comune  
- **Constrângeri de memorie**: Modelul este prea mare pentru memoria dispozitivului țintă  
- **Viteză de inferență**: Inferența modelului este prea lentă pentru cerințele în timp real  
- **Degradarea acurateței**: Optimizarea reduce acuratețea modelului în mod inacceptabil  
- **Compatibilitate hardware**: Modelul nu este compatibil cu hardware-ul țintă  

### Strategii de depanare  
- **Profilarea performanței**: Utilizați funcțiile de trasare ale AI Toolkit pentru a identifica blocajele  
- **Monitorizarea resurselor**: Monitorizați memoria și utilizarea CPU în timpul dezvoltării  
- **Testare incrementală**: Testați optimizările incremental pentru a izola problemele  
- **Simulare hardware**: Utilizați instrumente de dezvoltare pentru a simula hardware-ul țintă  

### Soluții de optimizare  
- **Cuantizare suplimentară**: Aplicați tehnici de cuantizare mai agresive  
- **Arhitectura modelului**: Luați în considerare arhitecturi de model diferite optimizate pentru margine  
- **Optimizare preprocesare**: Optimizați preprocesarea datelor pentru constrângerile de margine  
- **Optimizare inferență**: Utilizați optimizări specifice hardware pentru inferență  

## Resurse și pași următori  

### Documentație oficială  
- [Documentația pentru dezvoltatori AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Ghid de instalare și configurare](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentația pentru aplicații inteligente VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentația Protocolului Context Model (MCP)](https://modelcontextprotocol.io/)  

### Comunitate și suport  
- [Repository GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Probleme și cereri de funcții pe GitHub](https://aka.ms/AIToolkit/feedback)  
- [Comunitatea Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Piața de extensii VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Resurse tehnice  
- [Documentația ONNX Runtime](https://onnxruntime.ai/)  
- [Documentația Ollama](https://ollama.ai/)  
- [Documentația Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentația Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Căi de învățare  
- [Cursul de bază AI la margine](../Module01/README.md)  
- [Ghidul pentru modele lingvistice mici](../Module02/README.md)  
- [Strategii de implementare la margine](../Module03/README.md)  
- [Dezvoltare AI la margine pentru Windows](./windowdeveloper.md)  

### Resurse suplimentare  
- **Statistici repository**: Peste 1.8k stele, 150+ forks, 18+ contribuitori  
- **Licență**: Licență MIT  
- **Securitate**: Se aplică politicile de securitate Microsoft  
- **Telemetrie**: Respectă setările de telemetrie VS Code  

## Concluzie  

AI Toolkit pentru Visual Studio Code reprezintă o platformă cuprinzătoare pentru dezvoltarea modernă AI, oferind capabilități simplificate de dezvoltare a agenților, care sunt deosebit de valoroase pentru aplicațiile AI la margine. Cu un catalog extins de modele care sprijină furnizori precum Anthropic, OpenAI, GitHub și Google, combinat cu execuția locală prin ONNX și Ollama, toolkit-ul oferă flexibilitatea necesară pentru diverse scenarii de implementare la margine.  

Punctul forte al toolkit-ului constă în abordarea sa integrată—de la descoperirea și experimentarea modelelor în Playground, la dezvoltarea sofisticată a agenților cu Prompt Builder, capabilități de evaluare cuprinzătoare și integrarea fără probleme a instrumentelor MCP. Pentru dezvoltatorii AI la margine, acest lucru înseamnă prototipare rapidă și testare a agenților AI înainte de implementarea la margine, cu posibilitatea de a itera rapid și de a optimiza pentru medii cu resurse limitate.  

Avantaje cheie pentru dezvoltarea AI la margine includ:  
- **Experimentare rapidă**: Testați modele și agenți rapid înainte de a decide implementarea la margine  
- **Flexibilitate multi-furnizor**: Accesați modele din diverse surse pentru a găsi soluții optime la margine  
- **Dezvoltare locală**: Testați cu ONNX și Ollama pentru dezvoltare offline și care respectă confidențialitatea  
- **Pregătire pentru producție**: Generați cod gata de producție și integrați cu instrumente externe prin MCP  
- **Evaluare cuprinzătoare**: Utilizați metrici integrate și personalizate pentru a valida performanța AI la margine  

Pe măsură ce AI continuă să se îndrepte spre scenarii de implementare la margine, AI Toolkit pentru VS Code oferă mediul de dezvoltare și fluxul de lucru necesar pentru a construi, testa și optimiza aplicații inteligente pentru medii cu resurse limitate. Fie că dezvoltați soluții IoT, aplicații AI mobile sau sisteme de inteligență încorporată, setul cuprinzător de funcții și fluxul de lucru integrat al toolkit-ului sprijină întregul ciclu de viață al dezvoltării AI la margine.  

Cu dezvoltare continuă și o comunitate activă (peste 1.8k stele pe GitHub), AI Toolkit rămâne în fruntea instrumentelor de dezvoltare AI, evoluând constant pentru a răspunde nevoilor dezvoltatorilor moderni de AI care construiesc pentru scenarii de implementare la margine.  

[Next Foundry Local](./foundrylocal.md)  

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.