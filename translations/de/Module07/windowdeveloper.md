<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T12:48:56+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "de"
}
-->
# Windows Edge AI Entwicklungsleitfaden

## Einführung

Willkommen bei der Windows Edge AI Entwicklung – Ihrem umfassenden Leitfaden zum Erstellen intelligenter Anwendungen, die die Leistung von KI direkt auf dem Gerät nutzen, basierend auf der Windows AI Foundry Plattform von Microsoft. Dieser Leitfaden richtet sich speziell an Windows-Entwickler, die modernste Edge-KI-Funktionen in ihre Anwendungen integrieren möchten und dabei die gesamte Hardware-Beschleunigung von Windows nutzen.

### Der Vorteil von Windows AI

Windows AI Foundry bietet eine einheitliche, zuverlässige und sichere Plattform, die den gesamten Lebenszyklus der KI-Entwicklung unterstützt – von der Modellauswahl und Feinabstimmung bis hin zur Optimierung und Bereitstellung auf CPU-, GPU-, NPU- und hybriden Cloud-Architekturen. Diese Plattform demokratisiert die KI-Entwicklung durch:

- **Hardware-Abstraktion**: Nahtlose Bereitstellung auf AMD-, Intel-, NVIDIA- und Qualcomm-Chips
- **Intelligenz auf dem Gerät**: Datenschutzfreundliche KI, die vollständig auf lokaler Hardware läuft
- **Optimierte Leistung**: Modelle, die speziell für Windows-Hardwarekonfigurationen optimiert sind
- **Unternehmensbereit**: Sicherheits- und Compliance-Funktionen auf Produktionsniveau

### Warum Windows für Edge AI?

**Universelle Hardware-Unterstützung**  
Windows ML bietet automatische Hardware-Optimierung im gesamten Windows-Ökosystem, sodass Ihre KI-Anwendungen unabhängig von der zugrunde liegenden Chip-Architektur optimal funktionieren.

**Integrierte KI-Laufzeit**  
Die integrierte Windows ML Inferenz-Engine eliminiert komplexe Setup-Anforderungen, sodass Entwickler sich auf die Anwendungslogik statt auf Infrastrukturprobleme konzentrieren können.

**Copilot+ PC Optimierung**  
Speziell entwickelte APIs für die nächste Generation von Windows-Geräten mit dedizierten Neural Processing Units (NPUs), die außergewöhnliche Leistung pro Watt bieten.

**Entwickler-Ökosystem**  
Umfangreiche Tools wie die Integration in Visual Studio, umfassende Dokumentation und Beispielanwendungen, die Entwicklungszyklen beschleunigen.

## Lernziele

Durch das Abschließen dieses Leitfadens zur Windows Edge AI Entwicklung werden Sie die wesentlichen Fähigkeiten für die Erstellung produktionsreifer KI-Anwendungen auf der Windows-Plattform beherrschen.

### Kerntechnische Kompetenzen

**Beherrschung der Windows AI Foundry**  
- Verstehen der Architektur und Komponenten der Windows AI Foundry Plattform  
- Navigieren durch den gesamten KI-Entwicklungszyklus im Windows-Ökosystem  
- Implementieren von Sicherheitsbest-Practices für KI-Anwendungen auf dem Gerät  
- Optimieren von Anwendungen für verschiedene Windows-Hardwarekonfigurationen  

**API-Integrationskompetenz**  
- Beherrschen der Windows AI APIs für Text-, Bild- und multimodale Anwendungen  
- Implementieren der Phi Silica Sprachmodell-Integration für Textgenerierung und logisches Denken  
- Bereitstellen von Computer-Vision-Funktionen mit integrierten Bildverarbeitungs-APIs  
- Anpassen vortrainierter Modelle mit LoRA (Low-Rank Adaptation) Techniken  

**Lokale Implementierung der Foundry**  
- Durchsuchen, Bewerten und Bereitstellen von Open-Source-Sprachmodellen mit Foundry Local CLI  
- Verstehen von Modelloptimierung und Quantisierung für lokale Bereitstellung  
- Implementieren von Offline-KI-Funktionen, die ohne Internetverbindung funktionieren  
- Verwalten von Modell-Lebenszyklen und Updates in Produktionsumgebungen  

**Windows ML Bereitstellung**  
- Eigene ONNX-Modelle in Windows-Anwendungen mit Windows ML einbringen  
- Automatische Hardware-Beschleunigung über CPU-, GPU- und NPU-Architekturen nutzen  
- Echtzeit-Inferenz mit optimaler Ressourcennutzung implementieren  
- Skalierbare KI-Anwendungen für verschiedene Windows-Gerätekategorien entwerfen  

### Fähigkeiten zur Anwendungsentwicklung

**Plattformübergreifende Windows-Entwicklung**  
- KI-gestützte Anwendungen mit .NET MAUI für universelle Windows-Bereitstellung erstellen  
- KI-Funktionen in Win32-, UWP- und Progressive Web Applications integrieren  
- Responsive UI-Designs implementieren, die sich an KI-Verarbeitungszustände anpassen  
- Asynchrone KI-Operationen mit geeigneten Benutzererfahrungsmustern handhaben  

**Leistungsoptimierung**  
- Profilieren und Optimieren der KI-Inferenzleistung über verschiedene Hardwarekonfigurationen  
- Effizientes Speichermanagement für große Sprachmodelle implementieren  
- Anwendungen entwerfen, die sich basierend auf verfügbaren Hardware-Funktionen anpassen  
- Caching-Strategien für häufig genutzte KI-Operationen anwenden  

**Produktionsreife**  
- Umfassendes Fehlerhandling und Fallback-Mechanismen implementieren  
- Telemetrie und Monitoring für die Leistung von KI-Anwendungen entwerfen  
- Sicherheitsbest-Practices für lokale KI-Modellspeicherung und -ausführung anwenden  
- Bereitstellungsstrategien für Unternehmens- und Verbraucheranwendungen planen  

### Geschäftliches und strategisches Verständnis

**Architektur von KI-Anwendungen**  
- Hybride Architekturen entwerfen, die lokale und Cloud-KI-Verarbeitung optimieren  
- Abwägungen zwischen Modellgröße, Genauigkeit und Inferenzgeschwindigkeit bewerten  
- Datenflussarchitekturen planen, die Datenschutz wahren und gleichzeitig Intelligenz ermöglichen  
- Kostenwirksame KI-Lösungen implementieren, die mit Benutzeranforderungen skalieren  

**Marktpositionierung**  
- Wettbewerbsvorteile von Windows-nativen KI-Anwendungen verstehen  
- Anwendungsfälle identifizieren, bei denen KI auf dem Gerät überlegene Benutzererfahrungen bietet  
- Go-to-Market-Strategien für KI-gestützte Windows-Anwendungen entwickeln  
- Anwendungen positionieren, um die Vorteile des Windows-Ökosystems zu nutzen  

## Komponenten der Windows AI Foundry Plattform

### 1. Windows AI APIs

Windows AI APIs bieten einsatzbereite KI-Funktionen, die von Modellen auf dem Gerät unterstützt werden und für Effizienz und Leistung auf Copilot+ PC-Geräten optimiert sind, mit minimalem Setup-Aufwand.

#### Kern-API-Kategorien

**Phi Silica Sprachmodell**  
- Kleines, aber leistungsstarkes Sprachmodell für Textgenerierung und logisches Denken  
- Optimiert für Echtzeit-Inferenz mit minimalem Stromverbrauch  
- Unterstützung für benutzerdefinierte Feinabstimmung mit LoRA-Techniken  
- Integration mit Windows semantischer Suche und Wissensabruf  

**Computer Vision APIs**  
- **Texterkennung (OCR)**: Text aus Bildern mit hoher Genauigkeit extrahieren  
- **Bild-Superauflösung**: Bilder mit lokalen KI-Modellen hochskalieren  
- **Bildsegmentierung**: Spezifische Objekte in Bildern identifizieren und isolieren  
- **Bildbeschreibung**: Detaillierte Textbeschreibungen für visuelle Inhalte generieren  
- **Objektentfernung**: Unerwünschte Objekte aus Bildern mit KI-gestütztem Inpainting entfernen  

**Multimodale Fähigkeiten**  
- **Integration von Vision und Sprache**: Text- und Bildverständnis kombinieren  
- **Semantische Suche**: Natürliche Sprachabfragen über Multimedia-Inhalte ermöglichen  
- **Wissensabruf**: Intelligente Sucherlebnisse mit lokalen Daten erstellen  

### 2. Foundry Local

Foundry Local bietet Entwicklern schnellen Zugriff auf einsatzbereite Open-Source-Sprachmodelle auf Windows-Silicon und ermöglicht das Durchsuchen, Testen, Interagieren und Bereitstellen von Modellen in lokalen Anwendungen.

#### Hauptmerkmale

**Modellkatalog**  
- Umfassende Sammlung voroptimierter Open-Source-Modelle  
- Modelle, die für CPUs, GPUs und NPUs optimiert sind und sofort bereitgestellt werden können  
- Unterstützung für beliebte Modellfamilien wie Llama, Mistral, Phi und spezialisierte Domänenmodelle  

**CLI-Integration**  
- Befehlszeilenschnittstelle für Modellverwaltung und Bereitstellung  
- Automatisierte Workflows für Optimierung und Quantisierung  
- Integration in beliebte Entwicklungsumgebungen und CI/CD-Pipelines  

**Lokale Bereitstellung**  
- Vollständiger Offline-Betrieb ohne Cloud-Abhängigkeiten  
- Unterstützung für benutzerdefinierte Modellformate und Konfigurationen  
- Effiziente Modellbereitstellung mit automatischer Hardware-Optimierung  

### 3. Windows ML

Windows ML dient als zentrale KI-Plattform und integrierte Inferenz-Laufzeit auf Windows, die es Entwicklern ermöglicht, benutzerdefinierte Modelle effizient im breiten Windows-Hardware-Ökosystem bereitzustellen.

#### Vorteile der Architektur

**Universelle Hardware-Unterstützung**  
- Automatische Optimierung für AMD-, Intel-, NVIDIA- und Qualcomm-Chips  
- Unterstützung für CPU-, GPU- und NPU-Ausführung mit transparentem Wechsel  
- Hardware-Abstraktion, die plattformspezifische Optimierungsarbeit eliminiert  

**Modellflexibilität**  
- Unterstützung für das ONNX-Modellformat mit automatischer Konvertierung aus beliebten Frameworks  
- Bereitstellung benutzerdefinierter Modelle mit Leistung auf Produktionsniveau  
- Integration in bestehende Windows-Anwendungsarchitekturen  

**Unternehmensintegration**  
- Kompatibel mit Windows-Sicherheits- und Compliance-Frameworks  
- Unterstützung für Unternehmensbereitstellungs- und Verwaltungstools  
- Integration in Windows-Geräteverwaltung und Überwachungssysteme  

## Entwicklungsworkflow

### Phase 1: Einrichtung der Umgebung und Konfiguration der Tools

**Vorbereitung der Entwicklungsumgebung**  
1. Visual Studio mit AI Toolkit-Erweiterung installieren  
2. Windows AI Foundry CLI-Tools konfigurieren  
3. Lokale Testumgebung für Modelle einrichten  
4. Tools für Leistungsprofilierung und Monitoring einrichten  

**Erkundung der AI Dev Gallery**  
- Beispielanwendungen und Referenzimplementierungen erkunden  
- Windows AI APIs mit interaktiven Demonstrationen testen  
- Quellcode für Best-Practices und Muster überprüfen  
- Relevante Beispiele für Ihren spezifischen Anwendungsfall identifizieren  

### Phase 2: Modellauswahl und Integration

**Anforderungsanalyse**  
- Funktionale Anforderungen für KI-Funktionen definieren  
- Leistungsbeschränkungen und Optimierungsziele festlegen  
- Datenschutz- und Sicherheitsanforderungen bewerten  
- Bereitstellungsarchitektur und Skalierungsstrategien planen  

**Modellbewertung**  
- Foundry Local verwenden, um Open-Source-Modelle für Ihren Anwendungsfall zu testen  
- Windows AI APIs gegen benutzerdefinierte Modellanforderungen benchmarken  
- Abwägungen zwischen Modellgröße, Genauigkeit und Inferenzgeschwindigkeit bewerten  
- Prototyp-Integrationsansätze mit ausgewählten Modellen entwickeln  

### Phase 3: Anwendungsentwicklung

**Kernintegration**  
- Integration der Windows AI APIs mit geeignetem Fehlerhandling implementieren  
- Benutzeroberflächen entwerfen, die KI-Verarbeitungsworkflows berücksichtigen  
- Caching- und Optimierungsstrategien für Modellinferenz implementieren  
- Telemetrie und Monitoring für die Leistung von KI-Operationen hinzufügen  

**Testen und Validierung**  
- Anwendungen auf verschiedenen Windows-Hardwarekonfigurationen testen  
- Leistungskennzahlen unter verschiedenen Lastbedingungen validieren  
- Automatisierte Tests für die Zuverlässigkeit der KI-Funktionalität implementieren  
- Benutzererfahrungstests mit KI-gestützten Funktionen durchführen  

### Phase 4: Optimierung und Bereitstellung

**Leistungsoptimierung**  
- Anwendungsleistung über Zielhardwarekonfigurationen profilieren  
- Speicherverbrauch und Modelllade-Strategien optimieren  
- Adaptive Verhaltensweisen basierend auf verfügbaren Hardware-Funktionen implementieren  
- Benutzererfahrung für verschiedene Leistungsszenarien feinabstimmen  

**Produktionsbereitstellung**  
- Anwendungen mit den richtigen KI-Modellabhängigkeiten paketieren  
- Aktualisierungsmechanismen für Modelle und Anwendungslogik implementieren  
- Monitoring und Analytik für Produktionsumgebungen konfigurieren  
- Rollout-Strategien für Unternehmens- und Verbraucherbereitstellungen planen  

## Praktische Implementierungsbeispiele

### Beispiel 1: Intelligente Dokumentenverarbeitungsanwendung

Erstellen Sie eine Windows-Anwendung, die Dokumente mit mehreren KI-Funktionen verarbeitet:

**Verwendete Technologien:**  
- Phi Silica für Dokumentzusammenfassung und Fragenbeantwortung  
- OCR APIs für Textextraktion aus gescannten Dokumenten  
- Bildbeschreibung APIs für Analyse von Diagrammen und Grafiken  
- Benutzerdefinierte ONNX-Modelle für Dokumentklassifikation  

**Implementierungsansatz:**  
- Modulare Architektur mit austauschbaren KI-Komponenten entwerfen  
- Asynchrone Verarbeitung für große Dokumentenstapel implementieren  
- Fortschrittsanzeigen und Abbruchunterstützung für langlaufende Operationen hinzufügen  
- Offline-Funktionalität für die Verarbeitung sensibler Dokumente einbeziehen  

### Beispiel 2: Einzelhandels-Inventarverwaltungssystem

Erstellen Sie ein KI-gestütztes Inventarsystem für Einzelhandelsanwendungen:

**Verwendete Technologien:**  
- Bildsegmentierung für Produktidentifikation  
- Benutzerdefinierte Vision-Modelle für Marken- und Kategorienklassifikation  
- Foundry Local Bereitstellung spezialisierter Einzelhandels-Sprachmodelle  
- Integration mit bestehenden POS- und Inventarsystemen  

**Implementierungsansatz:**  
- Kameraintegration für Echtzeit-Produktscanning erstellen  
- Barcode- und visuelle Produktidentifikation implementieren  
- Natürliche Sprachabfragen für Inventar mit lokalen Sprachmodellen hinzufügen  
- Skalierbare Architektur für Multi-Store-Bereitstellung entwerfen  

### Beispiel 3: Dokumentationsassistent für das Gesundheitswesen

Entwickeln Sie ein datenschutzfreundliches Dokumentationstool für das Gesundheitswesen:

**Verwendete Technologien:**  
- Phi Silica für medizinische Notizenerstellung und klinische Entscheidungsunterstützung  
- OCR für Digitalisierung handgeschriebener medizinischer Aufzeichnungen  
- Benutzerdefinierte medizinische Sprachmodelle, bereitgestellt über Windows ML  
- Lokale Vektorspeicherung für medizinischen Wissensabruf  

**Implementierungsansatz:**  
- Vollständigen Offline-Betrieb für Patientendatenschutz sicherstellen  
- Validierung und Vorschläge für medizinische Terminologie implementieren  
- Audit-Logging für regulatorische Compliance hinzufügen  
- Integration mit bestehenden elektronischen Patientenakten-Systemen entwerfen  

## Strategien zur Leistungsoptimierung

### Hardwarebewusste Entwicklung

**NPU-Optimierung**  
- Anwendungen entwerfen, die NPU-Funktionen auf Copilot+ PCs nutzen  
- Sanften Rückfall auf GPU/CPU bei Geräten ohne NPU implementieren  
- Modellformate für NPU-spezifische Beschleunigung optimieren  
- NPU-Auslastung und thermische Eigenschaften überwachen  

**Speichermanagement**  
- Effiziente Modelllade- und Caching-Strategien implementieren  
- Speicher-Mapping für große Modelle verwenden, um Startzeit zu reduzieren  
- Speicherbewusste Anwendungen für ressourcenbeschränkte Geräte entwerfen  
- Modellquantisierung für Speicheroptimierung implementieren  

**Batterieeffizienz**  
- KI-Operationen für minimalen Stromverbrauch optimieren  
- Adaptive Verarbeitung basierend auf Batteriestatus implementieren  
- Effiziente Hintergrundverarbeitung für kontinuierliche KI-Operationen entwerfen  
- Stromprofilierungs-Tools verwenden, um Energieverbrauch zu optimieren  

### Skalierbarkeitsüberlegungen

**Multithreading**  
- Thread-sichere KI-Operationen für parallele Verarbeitung entwerfen  
- Effiziente Arbeitsverteilung über verfügbare Kerne implementieren  
- Async/Await-Muster für nicht blockierende KI-Operationen verwenden  
- Thread-Pool-Optimierung für verschiedene Hardwarekonfigurationen planen  

**Caching-Strategien**  
- Intelligentes Caching für häufig genutzte KI-Operationen implementieren  
- Cache-Invalidierungsstrategien für Modellupdates entwerfen  
- Persistentes Caching für teure Vorverarbeitungsoperationen verwenden  
- Verteiltes Caching für Multi-User-Szenarien implementieren  

## Sicherheits- und Datenschutzbest-Practices

### Datenschutz

**Lokale Verarbeitung**  
- Sicherstellen, dass sensible Daten das lokale Gerät niemals verlassen  
- Sichere Speicherung für KI-Modelle und temporäre Daten implementieren  
- Windows-Sicherheitsfunktionen für Anwendungssandboxing verwenden  
- Verschlüsselung für gespeicherte Modelle und Zwischenergebnisse anwenden  

**Modellsicherheit**  
- Modellintegrität vor dem Laden und der Ausführung validieren  
- Sichere Mechanismen für Modellupdates implementieren  
- Signierte Modelle verwenden, um Manipulationen zu verhindern  
- Zugriffskontrollen für Modelldateien und Konfiguration anwenden  

### Compliance-Überlegungen

**Regulatorische Ausrichtung**  
- Anwendungen entwerfen, die GDPR-, HIPAA- und andere regulatorische Anforderungen erfüllen  
- Audit-Logging für KI-Entscheidungsprozesse implementieren  
- Transparenzfunktionen für KI-generierte Ergebnisse bereitstellen  
- Benutzerkontrolle über KI-Datenverarbeitung ermöglichen  

**Unternehmenssicherheit**  
- Integration mit Windows-Unternehmenssicherheitsrichtlinien  
- Unterstützung für verwaltete Bereitstellung durch Unternehmensverwaltungstools  
- Rollenbasierte Zugriffskontrollen für KI-Funktionen implementieren  
- Administrative Steuerungen für KI-Funktionalität bereitstellen  

## Fehlerbehebung und Debugging

### Häufige Entwicklungsprobleme

**Probleme beim Modell-Laden**  
- ONNX-Modellkompatibilität mit Windows ML validieren  
- Modelldateiintegrität und Formatanforderungen überprüfen  
- Hardwareanforderungen für spezifische Modelle verifizieren  
- Speicherzuweisungsprobleme beim Modell-Laden debuggen  

**Leistungsprobleme**  
- Anwendungsleistung über verschiedene Hardwarekonfigurationen profilieren  
- Engpässe in KI-Verarbeitungspipelines identifizieren  
- Datenvorverarbeitungs- und Nachverarbeitungsoperationen optimieren  
- Leistungsüberwachung und Alarmierung implementieren  

**Integrationsschwierigkeiten**  
- API-Integrationsprobleme mit geeignetem Fehlerhandling debuggen  
- Eingabedatenformate und Vorverarbeitungsanforderungen validieren  
- Randfälle und Fehlerbedingungen gründlich testen  
- Umfassendes Logging für Debugging von Produktionsproblemen implementieren  

### Debugging-Tools und Techniken

**Visual Studio Integration**  
- AI Toolkit-Debugger für Analyse der Modellausführung verwenden  
- Leistungsprofilierung für KI-Operationen implementieren  
- Asynchrone KI-Operationen mit geeignetem Ausnahmehandling debuggen  
- Speicherprofilierungs-Tools für Optimierung verwenden  

**Windows AI Foundry Tools**  
- Nutzen Sie die Foundry Local CLI für Modelltests und Validierung  
- Verwenden Sie die Windows AI API-Testtools zur Überprüfung der Integration  
- Implementieren Sie benutzerdefiniertes Logging zur Überwachung von KI-Operationen  
- Erstellen Sie automatisierte Tests für die Zuverlässigkeit der KI-Funktionalität  

## Zukunftssicherung Ihrer Anwendungen  

### Aufkommende Technologien  

**Hardware der nächsten Generation**  
- Entwickeln Sie Anwendungen, die zukünftige NPU-Funktionen nutzen können  
- Planen Sie für größere Modellgrößen und höhere Komplexität  
- Implementieren Sie adaptive Architekturen für sich weiterentwickelnde Hardware  
- Berücksichtigen Sie quantenbereite Algorithmen für zukünftige Kompatibilität  

**Fortschrittliche KI-Fähigkeiten**  
- Bereiten Sie sich auf die Integration multimodaler KI über mehr Datentypen hinweg vor  
- Planen Sie für Echtzeit-Kollaborationen zwischen mehreren Geräten  
- Entwickeln Sie für föderierte Lernfähigkeiten  
- Berücksichtigen Sie hybride Intelligenzarchitekturen zwischen Edge und Cloud  

### Kontinuierliches Lernen und Anpassung  

**Modell-Updates**  
- Implementieren Sie nahtlose Mechanismen für Modellaktualisierungen  
- Entwickeln Sie Anwendungen, die sich an verbesserte Modellfähigkeiten anpassen  
- Planen Sie für Abwärtskompatibilität mit bestehenden Modellen  
- Implementieren Sie A/B-Tests zur Bewertung der Modellleistung  

**Feature-Entwicklung**  
- Entwickeln Sie modulare Architekturen, die neue KI-Funktionen aufnehmen können  
- Planen Sie die Integration aufkommender Windows AI APIs  
- Implementieren Sie Feature-Flags für eine schrittweise Einführung neuer Funktionen  
- Gestalten Sie Benutzeroberflächen, die sich an erweiterte KI-Funktionen anpassen  

## Fazit  

Die Entwicklung von Windows Edge AI repräsentiert die Verbindung leistungsstarker KI-Fähigkeiten mit der robusten, sicheren und skalierbaren Windows-Plattform. Durch die Beherrschung des Windows AI Foundry-Ökosystems können Entwickler intelligente Anwendungen erstellen, die außergewöhnliche Benutzererlebnisse bieten und gleichzeitig höchste Standards in Bezug auf Datenschutz, Sicherheit und Leistung einhalten.  

Die Kombination aus Windows AI APIs, Foundry Local und Windows ML bietet eine unvergleichliche Grundlage für die Entwicklung der nächsten Generation intelligenter Windows-Anwendungen. Während sich die KI weiterentwickelt, stellt die Windows-Plattform sicher, dass Ihre Anwendungen mit aufkommenden Technologien skalieren und gleichzeitig Kompatibilität und Leistung über die vielfältige Windows-Hardwarelandschaft hinweg beibehalten.  

Egal, ob Sie Verbraucheranwendungen, Unternehmenslösungen oder spezialisierte Branchentools entwickeln – die Windows Edge AI-Entwicklung ermöglicht es Ihnen, intelligente, reaktionsfähige und tief integrierte Erlebnisse zu schaffen, die das volle Potenzial moderner Windows-Geräte ausschöpfen.  

## Zusätzliche Ressourcen  

Für eine Schritt-für-Schritt-Anleitung zur Nutzung von Foundry Local (Installation, CLI, dynamischer Endpunkt, SDK-Nutzung) sehen Sie sich die Repo-Anleitung an: [foundrylocal.md](./foundrylocal.md).  

### Dokumentation und Lernen  
- [Windows AI Foundry Dokumentation](https://learn.microsoft.com/windows/ai/)  
- [Windows AI APIs Referenz](https://learn.microsoft.com/windows/ai/apis/)  
- [Foundry Local Erste Schritte](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)  
- [Windows ML Überblick](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)  

### Entwicklungstools  
- [AI Toolkit für Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)  
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)  
- [Windows AI Beispiele](https://learn.microsoft.com/windows/ai/samples/)  

### Community und Support  
- [Windows Entwickler-Community](https://developer.microsoft.com/en-us/windows/)  
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)  
- [Microsoft Learn AI Training](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)  

---  

*Dieser Leitfaden ist darauf ausgelegt, sich mit dem schnell voranschreitenden Windows AI-Ökosystem weiterzuentwickeln. Regelmäßige Updates gewährleisten die Ausrichtung an den neuesten Plattformfähigkeiten und Entwicklungsbest-Practices.*  

---

