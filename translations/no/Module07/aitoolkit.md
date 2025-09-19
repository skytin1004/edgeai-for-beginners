<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-18T10:53:57+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "no"
}
-->
# AI Toolkit for Visual Studio Code - Veiledning for Edge AI-utvikling

## Introduksjon

Velkommen til den omfattende veiledningen for bruk av AI Toolkit for Visual Studio Code i Edge AI-utvikling. Etter hvert som kunstig intelligens beveger seg fra sentralisert skybasert databehandling til distribuerte enheter på kanten, trenger utviklere kraftige, integrerte verktøy som kan håndtere de unike utfordringene ved edge-distribusjon - fra ressursbegrensninger til krav om offline-funksjonalitet.

AI Toolkit for Visual Studio Code fyller dette gapet ved å tilby et komplett utviklingsmiljø spesielt designet for å bygge, teste og optimalisere AI-applikasjoner som kjører effektivt på edge-enheter. Enten du utvikler for IoT-sensorer, mobile enheter, innebygde systemer eller edge-servere, forenkler dette verktøyet hele utviklingsarbeidsflyten din innenfor det velkjente VS Code-miljøet.

Denne veiledningen vil ta deg gjennom de essensielle konseptene, verktøyene og beste praksisene for å utnytte AI Toolkit i dine Edge AI-prosjekter, fra valg av modell til produksjonsdistribusjon.

## Oversikt

AI Toolkit gir et integrert utviklingsmiljø for hele livssyklusen til Edge AI-applikasjoner innenfor VS Code. Det tilbyr sømløs integrasjon med populære AI-modeller fra leverandører som OpenAI, Anthropic, Google og GitHub, samtidig som det støtter lokal modell-distribusjon gjennom ONNX og Ollama - avgjørende funksjoner for Edge AI-applikasjoner som krever on-device inferens.

Det som skiller AI Toolkit for Edge AI-utvikling er fokuset på hele edge-distribusjonsprosessen. I motsetning til tradisjonelle AI-utviklingsverktøy som primært retter seg mot sky-distribusjon, inkluderer AI Toolkit spesialiserte funksjoner for modelloptimalisering, testing under ressursbegrensninger og ytelsesevaluering spesifikt for edge. Verktøyet forstår at Edge AI-utvikling krever andre hensyn - mindre modellstørrelser, raskere inferenstider, offline-funksjonalitet og maskinvare-spesifikke optimaliseringer.

Plattformen støtter flere distribusjonsscenarier, fra enkel on-device inferens til komplekse multi-modell edge-arkitekturer. Den gir verktøy for modellkonvertering, kvantisering og optimalisering som er essensielle for vellykket edge-distribusjon, samtidig som den opprettholder utviklerproduktiviteten som VS Code er kjent for.

## Læringsmål

Ved slutten av denne veiledningen vil du kunne:

### Kjernekompetanser
- **Installere og konfigurere** AI Toolkit for Visual Studio Code for Edge AI-utviklingsarbeidsflyter
- **Navigere og bruke** AI Toolkit-grensesnittet, inkludert Model Catalog, Playground og Agent Builder
- **Velge og evaluere** AI-modeller som er egnet for edge-distribusjon basert på ytelse og ressursbegrensninger
- **Konvertere og optimalisere** modeller ved hjelp av ONNX-format og kvantiseringsteknikker for edge-enheter

### Ferdigheter innen Edge AI-utvikling
- **Designe og implementere** Edge AI-applikasjoner ved hjelp av det integrerte utviklingsmiljøet
- **Utføre modelltesting** under edge-lignende forhold ved bruk av lokal inferens og ressursmonitorering
- **Skape og tilpasse** AI-agenter optimalisert for edge-distribusjonsscenarier
- **Evaluere modellytelse** ved hjelp av metrikker som er relevante for edge-databehandling (latens, minnebruk, nøyaktighet)

### Optimalisering og distribusjon
- **Bruke kvantisering og pruning** teknikker for å redusere modellstørrelse samtidig som akseptabel ytelse opprettholdes
- **Optimalisere modeller** for spesifikke edge-maskinvareplattformer, inkludert CPU-, GPU- og NPU-akselerasjon
- **Implementere beste praksis** for Edge AI-utvikling, inkludert ressursstyring og fallback-strategier
- **Forberede modeller og applikasjoner** for produksjonsdistribusjon på edge-enheter

### Avanserte Edge AI-konsepter
- **Integrere med edge AI-rammeverk** inkludert ONNX Runtime, Windows ML og TensorFlow Lite
- **Implementere multi-modell arkitekturer** og federerte læringsscenarier for edge-miljøer
- **Feilsøke vanlige Edge AI-problemer** inkludert minnebegrensninger, inferenshastighet og maskinvarekompatibilitet
- **Designe overvåkings- og loggingsstrategier** for Edge AI-applikasjoner i produksjon

### Praktisk anvendelse
- **Bygge ende-til-ende Edge AI-løsninger** fra modellvalg til distribusjon
- **Demonstrere ferdigheter** i edge-spesifikke utviklingsarbeidsflyter og optimaliseringsteknikker
- **Anvende lærte konsepter** på virkelige Edge AI-brukstilfeller, inkludert IoT, mobile og innebygde applikasjoner
- **Evaluere og sammenligne** ulike Edge AI-distribusjonsstrategier og deres avveininger

## Nøkkelfunksjoner for Edge AI-utvikling

### 1. Modellkatalog og oppdagelse
- **Støtte for lokale modeller**: Oppdag og få tilgang til AI-modeller spesifikt optimalisert for edge-distribusjon
- **ONNX-integrasjon**: Få tilgang til modeller i ONNX-format for effektiv edge-inferens
- **Ollama-støtte**: Utnytt lokalt kjørende modeller gjennom Ollama for personvern og offline-funksjonalitet
- **Modellsammenligning**: Sammenlign modeller side om side for å finne den optimale balansen mellom ytelse og ressursforbruk for edge-enheter

### 2. Interaktiv Playground
- **Lokal testmiljø**: Test modeller lokalt før edge-distribusjon
- **Multi-modal eksperimentering**: Test med bilder, tekst og andre input som er typiske i edge-scenarier
- **Parameterjustering**: Eksperimenter med ulike modellparametere for å optimalisere for edge-begrensninger
- **Sanntids ytelsesmonitorering**: Observer inferenshastighet og ressursbruk under utvikling

### 3. Agent Builder for Edge-applikasjoner
- **Prompt Engineering**: Lag optimaliserte prompts som fungerer effektivt med mindre edge-modeller
- **MCP-verktøyintegrasjon**: Integrer Model Context Protocol-verktøy for forbedrede edge-agentkapabiliteter
- **Kodegenerering**: Generer produksjonsklar kode optimalisert for edge-distribusjonsscenarier
- **Strukturerte utdata**: Design agenter som gir konsistente, strukturerte svar egnet for edge-applikasjoner

### 4. Modellvurdering og testing
- **Ytelsesmetrikker**: Evaluer modeller ved hjelp av metrikker som er relevante for edge-distribusjon (latens, minnebruk, nøyaktighet)
- **Batch-testing**: Test flere modellkonfigurasjoner samtidig for å finne optimale edge-innstillinger
- **Tilpasset evaluering**: Lag tilpassede evalueringskriterier spesifikke for Edge AI-brukstilfeller
- **Ressursprofilering**: Analyser minne- og beregningskrav for edge-distribusjonsplanlegging

### 5. Modellkonvertering og optimalisering
- **ONNX-konvertering**: Konverter modeller fra ulike formater til ONNX for edge-kompatibilitet
- **Kvantisering**: Reduser modellstørrelse og forbedre inferenshastighet gjennom kvantiseringsteknikker
- **Maskinvareoptimalisering**: Optimaliser modeller for spesifikke edge-maskinvare (CPU, GPU, NPU)
- **Formattransformasjon**: Transformér modeller fra Hugging Face og andre kilder for edge-distribusjon

### 6. Finjustering for edge-scenarier
- **Domeneadaptasjon**: Tilpass modeller for spesifikke edge-brukstilfeller og miljøer
- **Lokal trening**: Tren modeller lokalt med GPU-støtte for edge-spesifikke krav
- **Azure-integrasjon**: Utnytt Azure Container Apps for skybasert finjustering før edge-distribusjon
- **Transfer Learning**: Tilpass forhåndstrente modeller for edge-spesifikke oppgaver og begrensninger

### 7. Ytelsesmonitorering og sporing
- **Edge-ytelsesanalyse**: Overvåk modellytelse under edge-lignende forhold
- **Sporingsinnsamling**: Samle detaljerte ytelsesdata for optimalisering
- **Flaskehalsidentifikasjon**: Identifiser ytelsesproblemer før distribusjon til edge-enheter
- **Ressursbruksporing**: Overvåk minne, CPU og inferenstid for edge-optimalisering

## Edge AI-utviklingsarbeidsflyt

### Fase 1: Modelloppdagelse og valg
1. **Utforsk modellkatalogen**: Bruk modellkatalogen for å finne modeller som er egnet for edge-distribusjon
2. **Sammenlign ytelse**: Evaluer modeller basert på størrelse, nøyaktighet og inferenshastighet
3. **Test lokalt**: Bruk Ollama eller ONNX-modeller for å teste lokalt før edge-distribusjon
4. **Vurder ressurskrav**: Bestem minne- og beregningsbehov for mål-edge-enheter

### Fase 2: Modelloptimalisering
1. **Konverter til ONNX**: Konverter valgte modeller til ONNX-format for edge-kompatibilitet
2. **Bruk kvantisering**: Reduser modellstørrelse gjennom INT8 eller INT4 kvantisering
3. **Maskinvareoptimalisering**: Optimaliser for mål-edge-maskinvare (ARM, x86, spesialiserte akseleratorer)
4. **Ytelsesvalidering**: Valider at optimaliserte modeller opprettholder akseptabel nøyaktighet

### Fase 3: Applikasjonsutvikling
1. **Agentdesign**: Bruk Agent Builder for å lage edge-optimaliserte AI-agenter
2. **Prompt Engineering**: Utvikle prompts som fungerer effektivt med mindre edge-modeller
3. **Integrasjonstesting**: Test agenter under simulerte edge-forhold
4. **Kodegenerering**: Generer produksjonskode optimalisert for edge-distribusjon

### Fase 4: Evaluering og testing
1. **Batch-evaluering**: Test flere konfigurasjoner for å finne optimale edge-innstillinger
2. **Ytelsesprofilering**: Analyser inferenshastighet, minnebruk og nøyaktighet
3. **Edge-simulering**: Test under forhold som ligner mål-edge-distribusjonsmiljøet
4. **Stress-testing**: Evaluer ytelse under ulike belastningsforhold

### Fase 5: Distribusjonsforberedelse
1. **Endelig optimalisering**: Utfør endelige optimaliseringer basert på testresultater
2. **Distribusjonspakking**: Pakk modeller og kode for edge-distribusjon
3. **Dokumentasjon**: Dokumenter distribusjonskrav og konfigurasjon
4. **Overvåkingsoppsett**: Forbered overvåking og logging for edge-distribusjon

## Målgruppe for Edge AI-utvikling

### Edge AI-utviklere
- Applikasjonsutviklere som bygger AI-drevne edge-enheter og IoT-løsninger
- Utviklere av innebygde systemer som integrerer AI-funksjoner i ressursbegrensede enheter
- Mobilutviklere som lager on-device AI-applikasjoner for smarttelefoner og nettbrett

### Edge AI-ingeniører
- AI-ingeniører som optimaliserer modeller for edge-distribusjon og administrerer inferens-pipelines
- DevOps-ingeniører som distribuerer og administrerer AI-modeller på tvers av distribuert edge-infrastruktur
- Ytelsesingeniører som optimaliserer AI-arbeidsbelastninger for edge-maskinvarebegrensninger

### Forskere og lærere
- AI-forskere som utvikler effektive modeller og algoritmer for edge-databehandling
- Lærere som underviser i Edge AI-konsepter og demonstrerer optimaliseringsteknikker
- Studenter som lærer om utfordringene og løsningene innen edge-distribusjon

## Edge AI-brukstilfeller

### Smarte IoT-enheter
- **Sanntids bildegjenkjenning**: Distribuer datamodeller for datamaskinsyn på IoT-kameraer og sensorer
- **Talebehandling**: Implementer talegjenkjenning og naturlig språkbehandling på smarte høyttalere
- **Prediktivt vedlikehold**: Kjør anomalideteksjonsmodeller på industrielle edge-enheter
- **Miljøovervåking**: Distribuer modeller for sensor-dataanalyse for miljøapplikasjoner

### Mobile og innebygde applikasjoner
- **On-device oversettelse**: Implementer språkoversettelsesmodeller som fungerer offline
- **Utvidet virkelighet**: Distribuer sanntids objektgjenkjenning og sporing for AR-applikasjoner
- **Helseovervåking**: Kjør helseanalysmodeller på wearables og medisinsk utstyr
- **Autonome systemer**: Implementer beslutningsmodeller for droner, roboter og kjøretøy

### Edge-databehandlingsinfrastruktur
- **Edge-datasentre**: Distribuer AI-modeller i edge-datasentre for lav-latens applikasjoner
- **CDN-integrasjon**: Integrer AI-behandlingskapabiliteter i innholdsleveringsnettverk
- **5G Edge**: Utnytt 5G edge-databehandling for AI-drevne applikasjoner
- **Fog Computing**: Implementer AI-behandling i fog computing-miljøer

## Installasjon og oppsett

### Rask installasjon
Installer AI Toolkit-utvidelsen direkte fra Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Forutsetninger for Edge AI-utvikling
- **ONNX Runtime**: Installer ONNX Runtime for modell-inferens
- **Ollama** (valgfritt): Installer Ollama for lokal modellservering
- **Python-miljø**: Sett opp Python med nødvendige AI-biblioteker
- **Edge-maskinvareverktøy**: Installer maskinvare-spesifikke utviklingsverktøy (CUDA, OpenVINO, etc.)

### Innledende konfigurasjon
1. Åpne VS Code og installer AI Toolkit-utvidelsen
2. Konfigurer modellkilder (ONNX, Ollama, sky-leverandører)
3. Sett opp lokalt utviklingsmiljø for edge-testing
4. Konfigurer maskinvareakselerasjonsalternativer for din utviklingsmaskin

## Komme i gang med Edge AI-utvikling

### Steg 1: Modellvalg
1. Åpne AI Toolkit-visningen i aktivitetsfeltet
2. Bla gjennom modellkatalogen for edge-kompatible modeller
3. Filtrer etter modellstørrelse, format (ONNX) og ytelsesegenskaper
4. Sammenlign modeller ved hjelp av innebygde sammenligningsverktøy

### Steg 2: Lokal testing
1. Bruk Playground for å teste valgte modeller lokalt
2. Eksperimenter med ulike prompts og parametere
3. Overvåk ytelsesmetrikker under testing
4. Evaluer modellresponser for edge-brukstilfellekrav

### Steg 3: Modelloptimalisering
1. Bruk modellkonverteringsverktøyene for å optimalisere for edge-distribusjon
2. Bruk kvantisering for å redusere modellstørrelse
3. Test optimaliserte modeller for å sikre akseptabel ytelse
4. Dokumenter optimaliseringsinnstillinger og ytelsesavveininger

### Steg 4: Agentutvikling
1. Bruk Agent Builder for å lage edge-optimaliserte AI-agenter
2. Utvikle prompts som fungerer effektivt med mindre modeller
3. Integrer nødvendige verktøy og API-er for edge-scenarier
4. Test agenter under simulerte edge-forhold

### Steg 5: Evaluering og distribusjon
1. Bruk bulk-evaluering for å teste flere konfigurasjoner
2. Profilér ytelse under ulike forhold
3. Forbered distribusjonspakker for mål-edge-enheter
4. Sett opp overvåking og logging for produksjonsdistribusjon

## Beste praksis for Edge AI-utvikling

### Modellvalg
- **Størrelsesbegrensninger**: Velg modeller som passer innenfor minnebegrensningene til mål-enheter
- **Inferenshastighet**: Prioriter modeller med rask inferens for sanntidsapplikasjoner
- **Nøyaktighetsavveininger**: Balanser modellnøyaktighet med ressursbegrensninger
- **Formatkompatibilitet**: Foretrekk ONNX eller maskinvare-optimaliserte formater for edge-distribusjon

### Optimaliseringsteknikker
- **Kvantisering**: Bruk INT8 eller INT4 kvantisering for å redusere modellstørrelse og forbedre hastighet
- **Pruning**: Fjern unødvendige modellparametere for å redusere beregningskrav
- **Knowledge Distillation**: Lag mindre modeller som opprettholder ytelsen til større modeller
- **Maskinvareakselerasjon**: Utnytt NPUs, GPUs eller spesialiserte akseleratorer når tilgjengelig

### Utviklingsarbeidsflyt
- **Iter
- **Sikkerhet**: Implementer passende sikkerhetstiltak for Edge AI-applikasjoner

## Integrasjon med Edge AI-rammeverk

### ONNX Runtime
- **Plattformuavhengig distribusjon**: Distribuer ONNX-modeller på tvers av ulike edge-plattformer
- **Maskinvareoptimalisering**: Utnytt ONNX Runtime sine maskinvarespesifikke optimaliseringer
- **Mobilstøtte**: Bruk ONNX Runtime Mobile for smarttelefon- og nettbrettapplikasjoner
- **IoT-integrasjon**: Distribuer på IoT-enheter ved hjelp av ONNX Runtime sine lette distribusjoner

### Windows ML
- **Windows-enheter**: Optimaliser for Windows-baserte edge-enheter og PC-er
- **NPU-akselerasjon**: Utnytt Neural Processing Units på Windows-enheter
- **DirectML**: Bruk DirectML for GPU-akselerasjon på Windows-plattformer
- **UWP-integrasjon**: Integrer med Universal Windows Platform-applikasjoner

### TensorFlow Lite
- **Mobiloptimalisering**: Distribuer TensorFlow Lite-modeller på mobile og innebygde enheter
- **Maskinvaredelegering**: Bruk spesialiserte maskinvaredelegeringer for akselerasjon
- **Mikrokontrollere**: Distribuer på mikrokontrollere ved hjelp av TensorFlow Lite Micro
- **Plattformuavhengig støtte**: Distribuer på tvers av Android, iOS og innebygde Linux-systemer

### Azure IoT Edge
- **Sky-Edge hybrid**: Kombiner skybasert trening med edge-inferens
- **Moduldistribusjon**: Distribuer AI-modeller som IoT Edge-moduler
- **Enhetshåndtering**: Administrer edge-enheter og modelloppdateringer eksternt
- **Telemetri**: Samle inn ytelsesdata og modellmetrikker fra edge-distribusjoner

## Avanserte Edge AI-scenarier

### Multi-modell distribusjon
- **Modellensembler**: Distribuer flere modeller for forbedret nøyaktighet eller redundans
- **A/B-testing**: Test ulike modeller samtidig på edge-enheter
- **Dynamisk valg**: Velg modeller basert på gjeldende enhetsforhold
- **Ressursdeling**: Optimaliser ressursbruk på tvers av flere distribuerte modeller

### Federert læring
- **Distribuert trening**: Tren modeller på tvers av flere edge-enheter
- **Personvernbevaring**: Hold treningsdata lokalt mens modellforbedringer deles
- **Samarbeidslæring**: Gjør det mulig for enheter å lære av kollektive erfaringer
- **Edge-sky-koordinering**: Koordiner læring mellom edge-enheter og skyinfrastruktur

### Sanntidsbehandling
- **Strømbehandling**: Behandle kontinuerlige datastrømmer på edge-enheter
- **Lav latens-inferens**: Optimaliser for minimal inferenslatens
- **Batchbehandling**: Behandle datapartier effektivt på edge-enheter
- **Adaptiv behandling**: Juster behandlingen basert på gjeldende enhetskapasitet

## Feilsøking av Edge AI-utvikling

### Vanlige problemer
- **Minnebegrensninger**: Modellen er for stor for målenhetens minne
- **Inferenshastighet**: Modellen er for treg for sanntidskrav
- **Nøyaktighetsforringelse**: Optimalisering reduserer modellens nøyaktighet uakseptabelt
- **Maskinvarekompatibilitet**: Modellen er ikke kompatibel med målenheten

### Feilsøkingsstrategier
- **Ytelsesprofilering**: Bruk AI Toolkit sine sporingsfunksjoner for å identifisere flaskehalser
- **Ressursovervåking**: Overvåk minne- og CPU-bruk under utvikling
- **Inkrementell testing**: Test optimaliseringer trinnvis for å isolere problemer
- **Maskinvaresimulering**: Bruk utviklingsverktøy for å simulere målenheten

### Optimaliseringsløsninger
- **Videre kvantisering**: Bruk mer aggressive kvantiseringsteknikker
- **Modellarkitektur**: Vurder ulike modellarkitekturer optimalisert for edge
- **Forbehandlingsoptimalisering**: Optimaliser dataprosessering for edge-begrensninger
- **Inferensoptimalisering**: Bruk maskinvarespesifikke inferensoptimaliseringer

## Ressurser og neste steg

### Dokumentasjon
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Fellesskap og støtte
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Læringsressurser
- [Edge AI Fundamentals Course](./Module01/README.md)
- [Small Language Models Guide](./Module02/README.md)
- [Edge Deployment Strategies](./Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

## Konklusjon

AI Toolkit for Visual Studio Code gir en omfattende plattform for Edge AI-utvikling, fra modelloppdagelse og optimalisering til distribusjon og overvåking. Ved å utnytte de integrerte verktøyene og arbeidsflytene kan utviklere effektivt lage, teste og distribuere AI-applikasjoner som fungerer godt på ressursbegrensede edge-enheter.

Verktøyets støtte for ONNX, Ollama og ulike skyleverandører, kombinert med dets optimaliserings- og evalueringsmuligheter, gjør det til et ideelt valg for Edge AI-utvikling. Enten du bygger IoT-applikasjoner, mobile AI-funksjoner eller innebygde intelligenssystemer, gir AI Toolkit de nødvendige verktøyene og arbeidsflytene for vellykket Edge AI-distribusjon.

Etter hvert som Edge AI utvikler seg, forblir AI Toolkit for VS Code i frontlinjen og gir utviklere banebrytende verktøy og funksjoner for å bygge neste generasjons intelligente edge-applikasjoner.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.