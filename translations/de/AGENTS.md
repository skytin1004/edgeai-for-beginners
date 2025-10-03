<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:21:55+00:00",
  "source_file": "AGENTS.md",
  "language_code": "de"
}
-->
# AGENTS.md

## Projektübersicht

EdgeAI for Beginners ist ein umfassendes Bildungsrepository, das die Entwicklung von Edge AI mit Small Language Models (SLMs) vermittelt. Der Kurs behandelt die Grundlagen von EdgeAI, Modellbereitstellung, Optimierungstechniken und produktionsreife Implementierungen mit Microsoft Foundry Local und verschiedenen AI-Frameworks.

**Wichtige Technologien:**
- Python 3.8+ (primäre Sprache für AI/ML-Beispiele)
- .NET C# (AI/ML-Beispiele)
- JavaScript/Node.js mit Electron (für Desktop-Anwendungen)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-Frameworks: LangChain, Semantic Kernel, Chainlit
- Modelloptimierung: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository-Typ:** Bildungsinhalts-Repository mit 8 Modulen und 10 umfassenden Beispielanwendungen

**Architektur:** Mehrmoduliger Lernpfad mit praktischen Beispielen, die Edge-AI-Bereitstellungsmuster demonstrieren

## Repository-Struktur

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Setup-Befehle

### Repository-Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-Beispiel-Setup (Modul08 und Python-Beispiele)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Node.js-Beispiel-Setup (Beispiel 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local Setup

Foundry Local ist erforderlich, um die Modul08-Beispiele auszuführen:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Entwicklungsworkflow

### Inhaltsentwicklung

Dieses Repository enthält hauptsächlich **Markdown-Bildungsinhalte**. Bei Änderungen:

1. Bearbeiten Sie `.md`-Dateien in den entsprechenden Modulverzeichnissen
2. Folgen Sie den bestehenden Formatierungsmustern
3. Stellen Sie sicher, dass Codebeispiele korrekt und getestet sind
4. Aktualisieren Sie die entsprechenden übersetzten Inhalte, falls erforderlich (oder überlassen Sie dies der Automatisierung)

### Entwicklung von Beispielanwendungen

Für Python-Beispiele (Beispiele 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Für Electron-Beispiel (Beispiel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testen von Beispielanwendungen

Python-Beispiele haben keine automatisierten Tests, können aber durch Ausführung validiert werden:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Das Electron-Beispiel verfügt über eine Testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testanweisungen

### Inhaltsvalidierung

Das Repository verwendet automatisierte Übersetzungsworkflows. Manuelles Testen ist für Übersetzungen nicht erforderlich.

**Manuelle Validierung für Inhaltsänderungen:**
1. Überprüfen Sie die Markdown-Darstellung durch Vorschau der `.md`-Dateien
2. Stellen Sie sicher, dass alle Links auf gültige Ziele verweisen
3. Testen Sie alle in der Dokumentation enthaltenen Code-Snippets
4. Überprüfen Sie, ob Bilder korrekt geladen werden

### Testen von Beispielanwendungen

**Modul08/samples/08 (Electron-App) verfügt über umfassende Tests:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python-Beispiele sollten manuell getestet werden:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Richtlinien für Code-Stil

### Markdown-Inhalte

- Verwenden Sie eine konsistente Überschriftenhierarchie (# für Titel, ## für Hauptabschnitte, ### für Unterabschnitte)
- Fügen Sie Codeblöcke mit Sprachspezifikatoren ein: ```python, ```bash, ```javascript
- Folgen Sie den bestehenden Formatierungen für Tabellen, Listen und Hervorhebungen
- Halten Sie die Zeilen lesbar (zielen Sie auf ~80-100 Zeichen, aber nicht strikt)
- Verwenden Sie relative Links für interne Verweise

### Python-Code-Stil

- Befolgen Sie die PEP 8-Konventionen
- Verwenden Sie Typ-Hinweise, wo angebracht
- Fügen Sie Docstrings für Funktionen und Klassen hinzu
- Verwenden Sie aussagekräftige Variablennamen
- Halten Sie Funktionen fokussiert und prägnant

### JavaScript/Node.js-Code-Stil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Wichtige Konventionen:**
- ESLint-Konfiguration im Beispiel 08 bereitgestellt
- Prettier für Codeformatierung
- Verwenden Sie moderne ES6+-Syntax
- Folgen Sie den bestehenden Mustern im Codebestand

## Richtlinien für Pull Requests

### Titel-Format
```
[ModuleXX] Brief description of change
```
oder
```
[Module08/samples/XX] Description for sample changes
```

### Vor dem Einreichen

**Für Inhaltsänderungen:**
- Vorschau aller geänderten Markdown-Dateien
- Überprüfen Sie Links und Bilder
- Prüfen Sie auf Tippfehler und grammatikalische Fehler

**Für Änderungen am Beispielcode (Modul08/samples/08):**
```bash
npm run lint
npm test
```

**Für Änderungen an Python-Beispielen:**
- Testen Sie, ob das Beispiel erfolgreich ausgeführt wird
- Überprüfen Sie die Fehlerbehandlung
- Stellen Sie die Kompatibilität mit Foundry Local sicher

### Überprüfungsprozess

- Änderungen an Bildungsinhalten werden auf Genauigkeit und Klarheit überprüft
- Codebeispiele werden auf Funktionalität getestet
- Übersetzungsaktualisierungen werden automatisch von GitHub Actions gehandhabt

## Übersetzungssystem

**WICHTIG:** Dieses Repository verwendet automatisierte Übersetzung über GitHub Actions.

- Übersetzungen befinden sich im Verzeichnis `/translations/` (50+ Sprachen)
- Automatisiert über den Workflow `co-op-translator.yml`
- **Bearbeiten Sie Übersetzungsdateien NICHT manuell** - sie werden überschrieben
- Bearbeiten Sie nur englische Quelldateien im Root- und Modulverzeichnis
- Übersetzungen werden automatisch bei Pushes in den `main`-Branch generiert

## Foundry Local Integration

Die meisten Modul08-Beispiele erfordern, dass Microsoft Foundry Local ausgeführt wird:

### Foundry Local starten
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Foundry Local überprüfen
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Umgebungsvariablen für Beispiele

Die meisten Beispiele verwenden diese Umgebungsvariablen:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Build und Bereitstellung

### Inhaltsbereitstellung

Dieses Repository besteht hauptsächlich aus Dokumentation - kein Build-Prozess für Inhalte erforderlich.

### Build von Beispielanwendungen

**Electron-Anwendung (Modul08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python-Beispiele:**
Kein Build-Prozess - Beispiele werden direkt mit dem Python-Interpreter ausgeführt.

## Häufige Probleme und Fehlerbehebung

### Foundry Local läuft nicht
**Problem:** Beispiele schlagen mit Verbindungsfehlern fehl

**Lösung:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Probleme mit der Python-virtuellen Umgebung
**Problem:** Modulimportfehler

**Lösung:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Electron-Build-Probleme
**Problem:** npm install oder Build-Fehler

**Lösung:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Konflikte im Übersetzungsworkflow
**Problem:** Übersetzungs-PR steht im Konflikt mit Ihren Änderungen

**Lösung:**
- Bearbeiten Sie nur englische Quelldateien
- Lassen Sie den automatisierten Übersetzungsworkflow die Übersetzungen übernehmen
- Wenn Konflikte auftreten, führen Sie `main` in Ihren Branch zusammen, nachdem die Übersetzungen zusammengeführt wurden

## Zusätzliche Ressourcen

### Lernpfade
- **Anfängerpfad:** Module 01-02 (7-9 Stunden)
- **Fortgeschrittener Pfad:** Module 03-04 (9-11 Stunden)
- **Expertenpfad:** Module 05-07 (12-15 Stunden)
- **Meisterpfad:** Modul 08 (8-10 Stunden)

### Wichtige Modul-Inhalte
- **Modul01:** Grundlagen von EdgeAI und Fallstudien aus der Praxis
- **Modul02:** Small Language Model (SLM)-Familien und Architekturen
- **Modul03:** Strategien für lokale und Cloud-Bereitstellung
- **Modul04:** Modelloptimierung mit verschiedenen Frameworks
- **Modul05:** SLMOps - Produktionsbetrieb
- **Modul06:** KI-Agenten und Funktionsaufrufe
- **Modul07:** Plattform-spezifische Implementierungen
- **Modul08:** Foundry Local Toolkit mit 10 umfassenden Beispielen

### Externe Abhängigkeiten
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Lokale AI-Modell-Laufzeit
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimierungsframework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelloptimierungstoolkit
- [OpenVINO](https://docs.openvino.ai/) - Intels Optimierungstoolkit

## Projektspezifische Hinweise

### Modul08 Beispielanwendungen

Das Repository enthält 10 umfassende Beispielanwendungen:

1. **01-REST Chat Quickstart** - Grundlegende OpenAI SDK-Integration
2. **02-OpenAI SDK Integration** - Erweiterte SDK-Funktionen
3. **03-Model Discovery & Benchmarking** - Modellvergleichstools
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Grundlegende Agentenkoordination
6. **06-Models-as-Tools Router** - Intelligentes Modellrouting
7. **07-Direct API Client** - Low-Level API-Integration
8. **08-Windows 11 Chat App** - Native Electron-Desktopanwendung
9. **09-Advanced Multi-Agent System** - Komplexe Agentenkoordination
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel-Integration

Jedes Beispiel demonstriert verschiedene Aspekte der Edge-AI-Entwicklung mit Foundry Local.

### Leistungserwägungen

- SLMs sind für Edge-Bereitstellung optimiert (2-16GB RAM)
- Lokale Inferenz bietet Antwortzeiten von 50-500ms
- Quantisierungstechniken erreichen eine Größenreduzierung von 75% bei 85% Leistungsbeibehaltung
- Echtzeit-Gesprächsfähigkeiten mit lokalen Modellen

### Sicherheit und Datenschutz

- Alle Verarbeitung erfolgt lokal - keine Daten werden in die Cloud gesendet
- Geeignet für datenschutzsensible Anwendungen (Gesundheitswesen, Finanzen)
- Erfüllt Anforderungen an Datenhoheit
- Foundry Local läuft vollständig auf lokaler Hardware

---

**Dies ist ein Bildungsrepository, das sich auf die Vermittlung der Entwicklung von Edge AI konzentriert. Das Hauptbeitragsmuster besteht darin, Bildungsinhalte zu verbessern und Beispielanwendungen hinzuzufügen oder zu erweitern, die Edge-AI-Konzepte demonstrieren.**

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.