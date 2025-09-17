<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-17T13:52:35+00:00",
  "source_file": "Module07/README.md",
  "language_code": "de"
}
-->
# Kapitel 07: EdgeAI-Beispiele

Edge AI steht für die Verschmelzung von künstlicher Intelligenz mit Edge Computing und ermöglicht intelligente Verarbeitung direkt auf Geräten, ohne auf Cloud-Konnektivität angewiesen zu sein. Dieses Kapitel untersucht fünf verschiedene EdgeAI-Implementierungen auf unterschiedlichen Plattformen und Frameworks und zeigt die Vielseitigkeit und Leistungsfähigkeit von KI-Modellen am Edge.

## 1. EdgeAI mit NVIDIA Jetson Orin Nano

Der NVIDIA Jetson Orin Nano stellt einen Durchbruch im Bereich des zugänglichen Edge-AI-Computings dar und bietet bis zu 67 TOPS an KI-Leistung in einem kompakten, kreditkartengroßen Format. Diese leistungsstarke Edge-AI-Plattform demokratisiert die Entwicklung generativer KI für Hobbyisten, Studenten und professionelle Entwickler gleichermaßen.

### Hauptmerkmale
- Liefert bis zu 67 TOPS an KI-Leistung – eine 1,7-fache Verbesserung gegenüber seinem Vorgänger
- 1024 CUDA-Kerne und bis zu 32 Tensor-Kerne für KI-Verarbeitung
- 6-Kern Arm Cortex-A78AE v8.2 64-Bit-CPU mit einer maximalen Frequenz von 1,5 GHz
- Preis von nur 249 $, bietet Entwicklern, Studenten und Bastlern die erschwinglichste und zugänglichste Plattform

### Anwendungen
Der Jetson Orin Nano ist hervorragend geeignet für den Betrieb moderner generativer KI-Modelle, einschließlich Vision-Transformers, großer Sprachmodelle und Vision-Language-Modelle. Er wurde speziell für GenAI-Anwendungsfälle entwickelt und ermöglicht es, mehrere LLMs auf einem handflächengroßen Gerät auszuführen. Beliebte Anwendungsfälle sind KI-gestützte Robotik, intelligente Drohnen, intelligente Kameras und autonome Edge-Geräte.

**Mehr erfahren**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI in mobilen Anwendungen mit .NET MAUI und ONNX Runtime GenAI

Diese Lösung zeigt, wie Generative AI und Large Language Models (LLMs) in plattformübergreifende mobile Anwendungen integriert werden können, die mit .NET MAUI (Multi-platform App UI) und ONNX Runtime GenAI entwickelt wurden. Dieser Ansatz ermöglicht .NET-Entwicklern, anspruchsvolle KI-gestützte mobile Anwendungen zu erstellen, die nativ auf Android- und iOS-Geräten laufen.

### Hauptmerkmale
- Basierend auf dem .NET MAUI-Framework, das eine einzige Codebasis für Android- und iOS-Anwendungen bietet
- Integration von ONNX Runtime GenAI ermöglicht den Betrieb generativer KI-Modelle direkt auf mobilen Geräten
- Unterstützung verschiedener Hardware-Beschleuniger, die speziell für mobile Geräte entwickelt wurden, einschließlich CPU, GPU und spezialisierter mobiler KI-Prozessoren
- Plattformspezifische Optimierungen wie CoreML für iOS und NNAPI für Android über ONNX Runtime
- Implementiert den vollständigen generativen KI-Zyklus, einschließlich Vor- und Nachverarbeitung, Inferenz, Logits-Verarbeitung, Suche und Sampling sowie KV-Cache-Management

### Vorteile für Entwickler
Der .NET MAUI-Ansatz ermöglicht es Entwicklern, ihre bestehenden C#- und .NET-Kenntnisse zu nutzen, während sie plattformübergreifende KI-Anwendungen erstellen. Das ONNX Runtime GenAI-Framework unterstützt mehrere Modellarchitekturen, darunter Llama, Mistral, Phi, Gemma und viele andere. Optimierte ARM64-Kerne beschleunigen INT4-quantisierte Matrixmultiplikation und sorgen für eine effiziente Leistung auf mobiler Hardware, während die vertraute .NET-Entwicklungsumgebung erhalten bleibt.

### Anwendungsfälle
Diese Lösung eignet sich ideal für Entwickler, die KI-gestützte mobile Anwendungen mit .NET-Technologien erstellen möchten, einschließlich intelligenter Chatbots, Bildverkennungs-Apps, Sprachübersetzungstools und personalisierter Empfehlungssysteme, die vollständig auf dem Gerät laufen und so die Privatsphäre verbessern und Offline-Funktionalität bieten.

**Mehr erfahren**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI in Azure mit Small Language Models Engine

Microsofts Azure-basierte EdgeAI-Lösung konzentriert sich auf die effiziente Bereitstellung von Small Language Models (SLMs) in Cloud-Edge-Hybridumgebungen. Dieser Ansatz überbrückt die Lücke zwischen Cloud-basierten KI-Diensten und den Anforderungen an Edge-Bereitstellungen.

### Architekturvorteile
- Nahtlose Integration mit Azure AI-Diensten
- Betrieb von SLMs/LLMs und multimodalen Modellen auf Geräten und in der Cloud mit ONNX Runtime
- Optimiert für unternehmensweite Bereitstellungen
- Unterstützung für kontinuierliche Modellaktualisierungen und -verwaltung

### Anwendungsfälle
Die Azure EdgeAI-Implementierung ist besonders geeignet für Szenarien, die eine unternehmensgerechte KI-Bereitstellung mit Cloud-Management-Funktionen erfordern. Dazu gehören intelligente Dokumentenverarbeitung, Echtzeitanalysen und hybride KI-Workflows, die sowohl Cloud- als auch Edge-Computing-Ressourcen nutzen.

**Mehr erfahren**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI mit Windows ML

Windows ML ist Microsofts hochmodernes Runtime-System, das für performante Modellinferenz auf Geräten und vereinfachte Bereitstellung optimiert ist und die Grundlage der Windows AI Foundry bildet. Diese Plattform ermöglicht es Entwicklern, KI-gestützte Windows-Anwendungen zu erstellen, die die gesamte Bandbreite der PC-Hardware nutzen.

### Plattformfähigkeiten
- Funktioniert auf allen Windows 11-PCs mit Version 24H2 (Build 26100) oder höher
- Unterstützt alle x64- und ARM64-PC-Hardware, auch PCs ohne NPUs oder GPUs
- Ermöglicht es Entwicklern, ihre eigenen Modelle mitzubringen und effizient über das Partner-Ökosystem von AMD, Intel, NVIDIA und Qualcomm bereitzustellen, einschließlich CPU, GPU und NPU
- Dank Infrastruktur-APIs müssen Entwickler keine mehrfachen Builds ihrer App erstellen, um verschiedene Hardware zu unterstützen

### Vorteile für Entwickler
Windows ML abstrahiert die Hardware und Ausführungsanbieter, sodass Sie sich auf das Schreiben Ihres Codes konzentrieren können. Darüber hinaus aktualisiert sich Windows ML automatisch, um die neuesten NPUs, GPUs und CPUs zu unterstützen, sobald sie verfügbar sind. Die Plattform bietet ein einheitliches Framework für KI-Entwicklung über das vielfältige Windows-Hardware-Ökosystem hinweg.

**Mehr erfahren**: 
- [Windows ML Übersicht](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Entwicklungsleitfaden](../windowdeveloper.md) – Umfassender Leitfaden für die Windows EdgeAI-Entwicklung

## 5. EdgeAI mit Foundry Local Anwendungen

Foundry Local ermöglicht es Entwicklern, Retrieval Augmented Generation (RAG)-Anwendungen mit lokalen Ressourcen in .NET zu erstellen, indem lokale Sprachmodelle mit semantischen Suchfunktionen kombiniert werden. Dieser Ansatz bietet datenschutzorientierte KI-Lösungen, die vollständig auf lokaler Infrastruktur betrieben werden.

### Technische Architektur
- Kombination des Phi-3-Sprachmodells, lokaler Embeddings und Semantic Kernel zur Erstellung eines RAG-Szenarios
- Verwendung von Embeddings als Vektoren (Arrays) von Gleitkommawerten, die Inhalte und deren semantische Bedeutung repräsentieren
- Semantic Kernel fungiert als Hauptorchestrator, der Phi-3 und Smart Components integriert, um eine nahtlose RAG-Pipeline zu schaffen
- Unterstützung für lokale Vektordatenbanken wie SQLite und Qdrant

### Implementierungsvorteile
RAG, oder Retrieval Augmented Generation, ist im Grunde genommen eine Methode, um Informationen abzurufen und in den Prompt einzufügen. Diese lokale Implementierung gewährleistet Datenschutz und bietet intelligente Antworten, die auf benutzerdefinierten Wissensdatenbanken basieren. Der Ansatz ist besonders wertvoll für Unternehmensszenarien, die Datensouveränität und Offline-Betrieb erfordern.

**Mehr erfahren**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Windows EdgeAI Entwicklungsressourcen

Für Entwickler, die speziell die Windows-Plattform anvisieren, haben wir einen umfassenden Leitfaden erstellt, der das gesamte Windows EdgeAI-Ökosystem abdeckt. Diese Ressource bietet detaillierte Informationen über die Windows AI Foundry, einschließlich APIs, Tools und Best Practices für die EdgeAI-Entwicklung auf Windows.

### Windows AI Foundry Plattform
Die Windows AI Foundry Plattform bietet eine umfassende Suite von Tools und APIs, die speziell für die EdgeAI-Entwicklung auf Windows-Geräten entwickelt wurden. Dazu gehören spezielle Unterstützung für NPU-beschleunigte Hardware, Windows ML-Integration und plattformspezifische Optimierungstechniken.

**Umfassender Leitfaden**: [Windows EdgeAI Entwicklungsleitfaden](../windowdeveloper.md)

Dieser Leitfaden umfasst:
- Überblick und Komponenten der Windows AI Foundry Plattform
- Phi Silica API für effiziente Inferenz auf NPU-Hardware
- Computer Vision APIs für Bildverarbeitung und OCR
- Windows ML Runtime-Integration und Optimierung
- Foundry Local CLI für lokale Entwicklung und Tests
- Hardware-Optimierungsstrategien für Windows-Geräte
- Praktische Implementierungsbeispiele und Best Practices

### AI Toolkit für EdgeAI-Entwicklung
Für Entwickler, die Visual Studio Code verwenden, bietet die AI Toolkit-Erweiterung eine umfassende Entwicklungsumgebung, die speziell für die Erstellung, das Testen und die Bereitstellung von EdgeAI-Anwendungen entwickelt wurde. Dieses Toolkit vereinfacht den gesamten EdgeAI-Entwicklungsworkflow innerhalb von VS Code.

**Entwicklungsleitfaden**: [AI Toolkit für EdgeAI-Entwicklung](../aitoolkit.md)

Der AI Toolkit-Leitfaden umfasst:
- Modellentdeckung und -auswahl für Edge-Bereitstellungen
- Lokale Test- und Optimierungsworkflows
- ONNX- und Ollama-Integration für Edge-Modelle
- Modellkonvertierungs- und Quantisierungstechniken
- Agentenentwicklung für Edge-Szenarien
- Leistungsbewertung und -überwachung
- Bereitstellungsvorbereitung und Best Practices

## Fazit

Diese fünf EdgeAI-Implementierungen zeigen die Reife und Vielfalt der heute verfügbaren EdgeAI-Lösungen. Von hardwarebeschleunigten Edge-Geräten wie dem Jetson Orin Nano bis hin zu Software-Frameworks wie ONNX Runtime GenAI und Windows ML haben Entwickler beispiellose Möglichkeiten, intelligente Anwendungen am Edge bereitzustellen.

Der gemeinsame Nenner dieser Plattformen ist die Demokratisierung von KI-Fähigkeiten, die es Entwicklern mit unterschiedlichen Kenntnissen und Anwendungsfällen ermöglichen, anspruchsvolle maschinelle Lernlösungen zu erstellen. Ob mobile Anwendungen, Desktop-Software oder eingebettete Systeme – diese EdgeAI-Lösungen bilden die Grundlage für die nächste Generation intelligenter Anwendungen, die effizient und datenschutzfreundlich am Edge arbeiten.

Jede Plattform bietet einzigartige Vorteile: Jetson Orin Nano für hardwarebeschleunigtes Edge-Computing, ONNX Runtime GenAI für plattformübergreifende mobile Entwicklung, Azure EdgeAI für unternehmensweite Cloud-Edge-Integration, Windows ML für Windows-native Anwendungen und Foundry Local für datenschutzorientierte RAG-Implementierungen. Zusammen bilden sie ein umfassendes Ökosystem für die EdgeAI-Entwicklung.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.