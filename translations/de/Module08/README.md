<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:51:36+00:00",
  "source_file": "Module08/README.md",
  "language_code": "de"
}
-->
# Modul 08: Praxis mit Microsoft Foundry Local - Komplettes Entwickler-Toolkit

## Überblick

Microsoft Foundry Local repräsentiert die nächste Generation der Edge-AI-Entwicklung und bietet Entwicklern leistungsstarke Werkzeuge, um KI-Anwendungen lokal zu erstellen, bereitzustellen und zu skalieren, während eine nahtlose Integration mit Azure AI Foundry gewährleistet wird. Dieses Modul bietet eine umfassende Einführung in Foundry Local, von der Installation bis hin zur Entwicklung fortschrittlicher Agenten.

**Wichtige Technologien:**
- Microsoft Foundry Local CLI und SDK
- Integration mit Azure AI Foundry
- Modellinferenz auf dem Gerät
- Lokale Modell-Caching und Optimierung
- Agentenbasierte Architekturen

## Lernziele des Moduls

Nach Abschluss dieses Moduls werden Sie:

- **Foundry Local Setup meistern**: Foundry Local für die Entwicklung unter Windows 11 installieren, konfigurieren und optimieren
- **Vielfältige Modelle bereitstellen**: Phi-, Qwen-, Deepseek- und GPT-OSS-20B-Modelle lokal mit CLI-Befehlen ausführen
- **Produktionslösungen erstellen**: KI-Anwendungen mit fortschrittlichem Prompt-Engineering und Datenintegration entwickeln
- **Open-Source-Ökosystem nutzen**: Hugging Face-Modelle und Community-Erweiterungen integrieren
- **KI-Architekturen vergleichen**: Unterschiede zwischen LLMs und SLMs sowie deren Einsatzstrategien verstehen
- **KI-Agenten entwickeln**: Intelligente Agenten mit der Architektur und den Grounding-Funktionen von Foundry Local erstellen
- **Modelle als Werkzeuge implementieren**: Modulare, anpassbare KI-Lösungen für Unternehmensanwendungen entwickeln

## Sitzungsstruktur

### [1: Einstieg in Foundry Local](./01.FoundryLocalSetup.md)
**Schwerpunkt**: Installation, CLI-Setup, Modell-Caching und Hardware-Beschleunigung

**Was Sie lernen werden:**
- Vollständige Installation von Foundry Local unter Windows 11
- CLI-Konfiguration und Befehlsstruktur
- Strategien für Modell-Caching zur Leistungsoptimierung
- Einrichtung und Optimierung der Hardware-Beschleunigung
- Praxisnahe Bereitstellung von Phi-, Qwen-, Deepseek- und GPT-OSS-20B-Modellen

**Dauer**: 2-3 Stunden  
**Voraussetzungen**: Windows 11, Grundkenntnisse der Kommandozeile

---

### [2: KI-Lösungen mit Azure AI Foundry erstellen](./02.AzureAIFoundryIntegration.md)
**Schwerpunkt**: Fortgeschrittenes Prompt-Engineering, Datenintegration und umsetzbare Aufgaben

**Was Sie lernen werden:**
- Fortgeschrittene Techniken des Prompt-Engineering
- Muster und Best Practices für die Datenintegration
- Erstellung umsetzbarer KI-Aufgaben mit Foundry Local
- Nahtlose Workflows für die Integration mit Azure AI Foundry
- Leistungsoptimierung und Überwachung

**Dauer**: 2-3 Stunden  
**Voraussetzungen**: Abschluss von Sitzung 1, Azure-Konto (optional)

---

### [3: Open-Source-Modelle mit Foundry Local](./03.OpenSourceModels.md)
**Schwerpunkt**: Hugging Face-Integration, Modell-Auswahlstrategien und Community-Erweiterungen

**Was Sie lernen werden:**
- Integration von Hugging Face-Modellen mit Foundry Local
- Strategien und Implementierung für "Bring-your-own-model" (BYOM)
- Einblicke in die "Model Mondays"-Serie und Community-Beiträge
- Bereitstellung und Optimierung benutzerdefinierter Modelle
- Bewertungskriterien und Auswahl von Community-Modellen

**Dauer**: 2-3 Stunden  
**Voraussetzungen**: Abschluss von Sitzung 1-2, Hugging Face-Konto

---

### [4: Erkundung modernster Modelle - LLMs, SLMs und Inferenz auf dem Gerät](./04.CuttingEdgeModels.md)
**Schwerpunkt**: Modellvergleich, EdgeAI mit Phi und ONNX Runtime, fortgeschrittene Demos

**Was Sie lernen werden:**
- Umfassender Vergleich von LLMs und SLMs sowie deren Anwendungsfälle
- Abwägungen zwischen lokaler und Cloud-Inferenz sowie Entscheidungsrahmen
- EdgeAI-Implementierung mit Phi und ONNX Runtime
- Entwicklung und Bereitstellung der Chainlit RAG Chat App
- Optimierungstechniken für WebGPU-Inferenz
- Integration und Funktionen des AI PC SDK

**Dauer**: 3-4 Stunden  
**Voraussetzungen**: Abschluss von Sitzung 1-3, Verständnis von Inferenzkonzepten

---

### [5: Schnelle Entwicklung KI-gestützter Agenten mit Foundry Local](./05.AIPoweredAgents.md)
**Schwerpunkt**: Schnelle Entwicklung von GenAI-Apps, System-Prompts, Grounding und Agentenarchitekturen

**Was Sie lernen werden:**
- Architektur und Designmuster von Foundry Local-Agenten
- System-Prompt-Engineering für das Verhalten von Agenten
- Grounding-Techniken für zuverlässige Agentenantworten
- Workflows für die schnelle Entwicklung von GenAI-Anwendungen
- Orchestrierung von Agenten und Multi-Agenten-Systemen
- Strategien für die Produktionsbereitstellung von KI-Agenten

**Dauer**: 3-4 Stunden  
**Voraussetzungen**: Abschluss von Sitzung 1-4, Grundkenntnisse über KI-Agenten

---

### [6: Foundry Local - Modelle als Werkzeuge](./06.ModelsAsTools.md)
**Schwerpunkt**: Modulare KI-Lösungen, Bereitstellung auf dem Gerät und Skalierung für Unternehmen

**Was Sie lernen werden:**
- KI-Modelle als modulare, anpassbare Werkzeuge behandeln
- Bereitstellung auf dem Gerät ohne Cloud-Abhängigkeit
- Inferenz mit niedriger Latenz, kosteneffizient und datenschutzfreundlich
- Muster für SDK-, API- und CLI-Integration
- Anpassung von Modellen für spezifische Anwendungsfälle
- Skalierungsstrategien von lokal bis Azure AI Foundry
- Unternehmensgerechte Architekturen für KI-Anwendungen

**Dauer**: 3-4 Stunden  
**Voraussetzungen**: Alle vorherigen Sitzungen, Erfahrung in der Unternehmensentwicklung hilfreich

## Voraussetzungen

### Systemanforderungen
- **Betriebssystem**: Windows 11 (22H2 oder später)
- **Speicher**: 16GB RAM (32GB empfohlen für größere Modelle)
- **Speicherplatz**: 50GB freier Speicherplatz für Modell-Caching
- **Hardware**: NPU-fähiges Gerät empfohlen (Copilot+ PC), GPU optional
- **Netzwerk**: Hochgeschwindigkeitsinternet für den anfänglichen Modell-Download

### Entwicklungsumgebung
- Visual Studio Code mit AI Toolkit-Erweiterung
- Python 3.10+ und pip
- Git für Versionskontrolle
- PowerShell oder Kommandozeile
- Azure CLI (optional für Cloud-Integration)

### Wissensvoraussetzungen
- Grundlegendes Verständnis von KI/ML-Konzepten
- Vertrautheit mit der Kommandozeile
- Grundkenntnisse in Python-Programmierung
- REST-API-Konzepte
- Grundkenntnisse in Prompting und Modell-Inferenz

## Zeitplan des Moduls

**Gesamtdauer**: 15-20 Stunden

| Sitzung | Schwerpunkt | Zeit | Komplexität |
|---------|-------------|------|-------------|
|  1 | Einrichtung & Grundlagen | 2-3 Stunden | Anfänger |
|  2 | KI-Lösungen | 2-3 Stunden | Mittelstufe |
|  3 | Open Source | 2-3 Stunden | Mittelstufe |
|  4 | Fortgeschrittene Modelle | 3-4 Stunden | Fortgeschritten |
|  5 | KI-Agenten | 3-4 Stunden | Fortgeschritten |
|  6 | Unternehmenswerkzeuge | 3-4 Stunden | Experte |

## Wichtige Ressourcen

### Primäre Dokumentation
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Serie](https://aka.ms/model-mondays)

### Community-Ressourcen
- [Foundry Local Community Diskussionen](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Beispiele](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Entwickler-Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Lernergebnisse

Nach Abschluss dieses Moduls sind Sie in der Lage:

### Technische Fähigkeiten
- **Bereitstellen und Verwalten**: Foundry Local-Installationen in Entwicklungs- und Produktionsumgebungen
- **Modelle integrieren**: Nahtlos mit verschiedenen Modellfamilien von Microsoft, Hugging Face und Community-Quellen arbeiten
- **Anwendungen erstellen**: Produktionsreife KI-Anwendungen mit fortschrittlichen Funktionen und Optimierungen entwickeln
- **Agenten entwickeln**: Komplexe KI-Agenten mit Grounding, Argumentation und Werkzeugintegration implementieren

### Strategisches Verständnis
- **Architekturentscheidungen**: Informierte Entscheidungen zwischen lokaler und Cloud-Bereitstellung treffen
- **Leistungsoptimierung**: Inferenzleistung über verschiedene Hardware-Konfigurationen optimieren
- **Unternehmensskalierung**: Anwendungen entwerfen, die von lokalen Prototypen bis zu Unternehmensbereitstellungen skalieren
- **Datenschutz und Sicherheit**: Datenschutzfreundliche KI-Lösungen mit lokaler Inferenz implementieren

### Innovationsfähigkeiten
- **Schnelles Prototyping**: KI-Anwendungskonzepte schnell erstellen und testen
- **Community-Integration**: Open-Source-Modelle nutzen und zum Ökosystem beitragen
- **Fortgeschrittene Muster**: Modernste KI-Muster wie RAG, Agenten und Werkzeugintegration implementieren
- **Zukunftssichere Entwicklung**: Anwendungen entwickeln, die für aufkommende KI-Technologien und Muster bereit sind

## Erste Schritte

1. **Vorbereitung der Umgebung**: Stellen Sie sicher, dass Windows 11 mit den empfohlenen Hardware-Spezifikationen installiert ist
2. **Installieren Sie die Voraussetzungen**: Richten Sie Entwicklungswerkzeuge und Abhängigkeiten ein
3. **Beginnen Sie mit Sitzung 1**: Starten Sie mit der Installation und Grundkonfiguration von Foundry Local
4. **Fortschreiten in Reihenfolge**: Absolvieren Sie die Sitzungen der Reihe nach für einen optimalen Lernfortschritt
5. **Kontinuierlich üben**: Wenden Sie die Konzepte durch praktische Übungen und Projekte an

## Erfolgskriterien

Verfolgen Sie Ihren Fortschritt durch das Modul:

- [ ] Erfolgreiche Installation und Konfiguration von Foundry Local
- [ ] Bereitstellung und Ausführung von mindestens 4 verschiedenen Modellfamilien
- [ ] Erstellung einer vollständigen KI-Lösung mit Datenintegration
- [ ] Integration von mindestens 2 Open-Source-Modellen
- [ ] Erstellung einer funktionalen RAG-Chat-Anwendung
- [ ] Entwicklung und Bereitstellung eines KI-Agenten
- [ ] Implementierung einer Architektur für Modelle-als-Werkzeuge

## Schnellstart für Beispiele

### 1) Umgebung einrichten (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Lokales Modell starten (neues Terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Chainlit-Demo ausführen (Sitzung 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Multi-Agent-Koordinator ausführen (Sitzung 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Falls Verbindungsfehler auftreten, validieren Sie Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Router-Konfiguration (Sitzung 6)
Der Router führt einen schnellen Gesundheitscheck durch und unterstützt konfigurationsbasierte Umgebungen:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Dieses Modul repräsentiert den neuesten Stand der Edge-AI-Entwicklung und kombiniert die Unternehmenswerkzeuge von Microsoft mit der Flexibilität und Innovation des Open-Source-Ökosystems. Mit der Beherrschung von Foundry Local stehen Sie an der Spitze der KI-Anwendungsentwicklung.

Für Azure OpenAI (Sitzung 2) finden Sie die erforderlichen Umgebungsvariablen und API-Versionseinstellungen in der README-Datei des Beispiels.

## Übersicht der Beispiele

- `samples/01`: Schneller REST-Chat mit Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK-Integration (`sdk_quickstart.py`).
- `samples/03`: Modellentdeckung + schneller Benchmark (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG-Demo (`app.py`).
- `samples/05`: Multi-Agenten-Orchestrierung (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router für Modelle-als-Werkzeuge (`python samples\06\router.py`).

---

