<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-17T13:23:07+00:00",
  "source_file": "Module04/README.md",
  "language_code": "de"
}
-->
# Kapitel 04: Modellformatkonvertierung und Quantisierung - Kapitelübersicht

Die Entwicklung von EdgeAI hat Modellformatkonvertierung und Quantisierung zu unverzichtbaren Technologien gemacht, um anspruchsvolle maschinelle Lernfähigkeiten auf ressourcenbeschränkten Geräten bereitzustellen. Dieses umfassende Kapitel bietet eine vollständige Anleitung zum Verständnis, zur Implementierung und zur Optimierung von Modellen für Edge-Deployment-Szenarien.

## 📚 Kapitelstruktur und Lernpfad

Dieses Kapitel ist in sechs aufeinander aufbauende Abschnitte gegliedert, die zusammen ein umfassendes Verständnis der Modelloptimierung für Edge-Computing schaffen:

---

## [Abschnitt 1: Grundlagen der Modellformatkonvertierung und Quantisierung](./01.Introduce.md)

### 🎯 Überblick
Dieser grundlegende Abschnitt schafft das theoretische Fundament für die Modelloptimierung in Edge-Computing-Umgebungen. Er behandelt Quantisierungsgrenzen von 1-Bit bis 8-Bit Präzisionsstufen sowie wichtige Strategien zur Formatkonvertierung.

**Wichtige Themen:**
- Präzisionsklassifizierungsrahmen (ultra-niedrig, niedrig, mittel)
- Vorteile und Anwendungsfälle von GGUF- und ONNX-Formaten
- Vorteile der Quantisierung für Betriebseffizienz und Flexibilität bei der Bereitstellung
- Leistungsbenchmarks und Vergleich des Speicherbedarfs

**Lernziele:**
- Verständnis der Quantisierungsgrenzen und Klassifikationen
- Identifikation geeigneter Formatkonvertierungstechniken
- Erlernen fortgeschrittener Optimierungsstrategien für Edge-Deployments

---

## [Abschnitt 2: Llama.cpp Implementierungsanleitung](./02.Llamacpp.md)

### 🎯 Überblick
Eine umfassende Anleitung zur Implementierung von Llama.cpp, einem leistungsstarken C++-Framework, das effiziente Inferenz von großen Sprachmodellen mit minimalem Setup auf verschiedenen Hardwarekonfigurationen ermöglicht.

**Wichtige Themen:**
- Installation auf Windows-, macOS- und Linux-Plattformen
- GGUF-Formatkonvertierung und verschiedene Quantisierungsstufen (Q2_K bis Q8_0)
- Hardwarebeschleunigung mit CUDA, Metal, OpenCL und Vulkan
- Python-Integration und Strategien für die Produktionsbereitstellung

**Lernziele:**
- Beherrschung der plattformübergreifenden Installation und des Build-Prozesses
- Implementierung von Modellquantisierungs- und Optimierungstechniken
- Bereitstellung von Modellen im Servermodus mit REST-API-Integration

---

## [Abschnitt 3: Microsoft Olive Optimierungssuite](./03.MicrosoftOlive.md)

### 🎯 Überblick
Erkundung von Microsoft Olive, einem hardwarebewussten Modelloptimierungstoolkit mit über 40 integrierten Optimierungskomponenten, das für die unternehmensgerechte Bereitstellung von Modellen auf verschiedenen Hardwareplattformen entwickelt wurde.

**Wichtige Themen:**
- Auto-Optimierungsfunktionen mit dynamischer und statischer Quantisierung
- Hardwarebewusste Intelligenz für CPU-, GPU- und NPU-Bereitstellung
- Unterstützung beliebter Modelle (Llama, Phi, Qwen, Gemma) direkt nach der Installation
- Unternehmensintegration mit Azure ML und Produktionsworkflows

**Lernziele:**
- Nutzung automatisierter Optimierung für verschiedene Modellarchitekturen
- Implementierung plattformübergreifender Bereitstellungsstrategien
- Aufbau unternehmensgerechter Optimierungspipelines

---

## [Abschnitt 4: OpenVINO Toolkit Optimierungssuite](./04.openvino.md)

### 🎯 Überblick
Umfassende Erkundung des OpenVINO-Toolkits von Intel, einer Open-Source-Plattform für die Bereitstellung leistungsstarker KI-Lösungen in Cloud-, On-Premises- und Edge-Umgebungen mit fortschrittlichen Funktionen des Neural Network Compression Framework (NNCF).

**Wichtige Themen:**
- Plattformübergreifende Bereitstellung mit Hardwarebeschleunigung (CPU, GPU, VPU, KI-Beschleuniger)
- Neural Network Compression Framework (NNCF) für fortschrittliche Quantisierung und Pruning
- OpenVINO GenAI für die Optimierung und Bereitstellung großer Sprachmodelle
- Unternehmensgerechte Modellserver-Funktionen und skalierbare Bereitstellungsstrategien

**Lernziele:**
- Beherrschung der OpenVINO-Modellkonvertierungs- und Optimierungsworkflows
- Implementierung fortschrittlicher Quantisierungstechniken mit NNCF
- Bereitstellung optimierter Modelle auf verschiedenen Hardwareplattformen mit Model Server

---

## [Abschnitt 5: Apple MLX Framework im Detail](./05.AppleMLX.md)

### 🎯 Überblick
Umfassende Abdeckung von Apple MLX, einem revolutionären Framework, das speziell für effizientes maschinelles Lernen auf Apple Silicon entwickelt wurde, mit Schwerpunkt auf großen Sprachmodellen und lokaler Bereitstellung.

**Wichtige Themen:**
- Vorteile der einheitlichen Speicherarchitektur und Metal Performance Shaders
- Unterstützung für LLaMA, Mistral, Phi-3, Qwen und Code Llama Modelle
- LoRA-Feinabstimmung für effiziente Modellanpassung
- Integration mit Hugging Face und Unterstützung für Quantisierung (4-Bit und 8-Bit)

**Lernziele:**
- Optimierung von Apple Silicon für die Bereitstellung von großen Sprachmodellen
- Implementierung von Feinabstimmungs- und Modellanpassungstechniken
- Aufbau von Unternehmens-KI-Anwendungen mit erweiterten Datenschutzfunktionen

---

## [Abschnitt 6: Synthese des Edge AI Entwicklungsworkflows](./06.workflow-synthesis.md)

### 🎯 Überblick
Umfassende Synthese aller Optimierungsframeworks in einheitliche Workflows, Entscheidungsbäume und Best Practices für produktionsreife Edge-AI-Bereitstellung auf verschiedenen Plattformen und Anwendungsfällen.

**Wichtige Themen:**
- Einheitliche Workflow-Architektur, die mehrere Optimierungsframeworks integriert
- Entscheidungsbäume zur Auswahl von Frameworks und Analyse von Leistungsabstrichen
- Validierung der Produktionsreife und umfassende Bereitstellungsstrategien
- Zukunftssichere Strategien für aufkommende Hardware und Modellarchitekturen

**Lernziele:**
- Systematische Auswahl von Frameworks basierend auf Anforderungen und Einschränkungen
- Implementierung produktionsreifer Edge-AI-Pipelines mit umfassendem Monitoring
- Gestaltung anpassungsfähiger Workflows, die sich mit neuen Technologien und Anforderungen weiterentwickeln

---

## 🎯 Lernziele des Kapitels

Nach Abschluss dieses umfassenden Kapitels werden die Leser folgende Fähigkeiten erlangen:

### **Technische Kompetenz**
- Tiefes Verständnis der Quantisierungsgrenzen und praktischen Anwendungen
- Praktische Erfahrung mit verschiedenen Optimierungsframeworks
- Fähigkeiten zur Produktionsbereitstellung in Edge-Computing-Umgebungen

### **Strategisches Verständnis**
- Auswahl hardwarebewusster Optimierungsstrategien
- Informierte Entscheidungsfindung bei Leistungsabstrichen
- Unternehmensgerechte Bereitstellungs- und Überwachungsstrategien

### **Leistungsbenchmarks**

| Framework   | Quantisierung | Speicherbedarf | Geschwindigkeitsverbesserung | Anwendungsfall                |
|-------------|---------------|----------------|------------------------------|-------------------------------|
| Llama.cpp   | Q4_K_M        | ~4GB           | 2-3x                         | Plattformübergreifende Bereitstellung |
| Olive       | INT4          | 60-75% Reduktion | 2-6x                         | Unternehmensworkflows         |
| OpenVINO    | INT8/INT4     | 50-75% Reduktion | 2-5x                         | Intel-Hardware-Optimierung    |
| MLX         | 4-Bit         | ~4GB           | 2-4x                         | Optimierung für Apple Silicon |

## 🚀 Nächste Schritte und fortgeschrittene Anwendungen

Dieses Kapitel bietet eine vollständige Grundlage für:
- Entwicklung benutzerdefinierter Modelle für spezifische Domänen
- Forschung im Bereich Edge-AI-Optimierung
- Entwicklung kommerzieller KI-Anwendungen
- Großflächige Unternehmensbereitstellungen von Edge-AI

Das Wissen aus diesen sechs Abschnitten bietet ein umfassendes Toolkit, um sich in der sich schnell entwickelnden Landschaft der Edge-AI-Modelloptimierung und -Bereitstellung zurechtzufinden.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.