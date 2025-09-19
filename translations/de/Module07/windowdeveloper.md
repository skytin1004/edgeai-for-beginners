<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ec2b092ed161fd4d3907e010f8cf544",
  "translation_date": "2025-09-17T13:55:03+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "de"
}
-->
# Windows Edge AI Entwicklungsleitfaden

## Einführung

Willkommen bei Windows Edge AI Development – Ihrem umfassenden Leitfaden zum Erstellen intelligenter Anwendungen, die die Leistung von KI direkt auf dem Gerät nutzen, basierend auf der Windows AI Foundry-Plattform von Microsoft. Dieser Leitfaden richtet sich speziell an Windows-Entwickler, die modernste Edge-KI-Funktionen in ihre Anwendungen integrieren möchten und dabei die gesamte Bandbreite der Windows-Hardwarebeschleunigung nutzen.

### Der Vorteil von Windows AI

Windows AI Foundry bietet eine einheitliche, zuverlässige und sichere Plattform, die den gesamten Lebenszyklus eines KI-Entwicklers unterstützt – von der Modellauswahl und Feinabstimmung bis hin zur Optimierung und Bereitstellung über CPU-, GPU-, NPU- und hybride Cloud-Architekturen. Diese Plattform demokratisiert die KI-Entwicklung durch folgende Vorteile:

- **Hardware-Abstraktion**: Nahtlose Bereitstellung auf AMD-, Intel-, NVIDIA- und Qualcomm-Chipsätzen
- **Intelligenz auf dem Gerät**: Datenschutzfreundliche KI, die vollständig auf lokaler Hardware läuft
- **Optimierte Leistung**: Modelle, die speziell für Windows-Hardwarekonfigurationen optimiert sind
- **Unternehmensbereit**: Sicherheits- und Compliance-Funktionen auf Produktionsniveau

### Warum Windows für Edge-KI?

**Universelle Hardware-Unterstützung**  
Windows ML bietet automatische Hardware-Optimierung im gesamten Windows-Ökosystem, sodass Ihre KI-Anwendungen unabhängig von der zugrunde liegenden Chip-Architektur optimal funktionieren.

**Integrierte KI-Laufzeit**  
Die integrierte Windows ML-Inferenz-Engine eliminiert komplexe Setup-Anforderungen, sodass Entwickler sich auf die Anwendungslogik statt auf Infrastrukturprobleme konzentrieren können.

**Copilot+ PC-Optimierung**  
Speziell entwickelte APIs für die nächste Generation von Windows-Geräten mit dedizierten Neural Processing Units (NPUs), die außergewöhnliche Leistung pro Watt bieten.

**Entwickler-Ökosystem**  
Umfangreiche Tools wie die Integration in Visual Studio, umfassende Dokumentation und Beispielanwendungen, die Entwicklungszyklen beschleunigen.

## Lernziele

Durch das Durcharbeiten dieses Windows Edge AI Entwicklungsleitfadens werden Sie die wesentlichen Fähigkeiten für die Erstellung produktionsreifer KI-Anwendungen auf der Windows-Plattform beherrschen.

### Kerntechnische Kompetenzen

**Beherrschung der Windows AI Foundry**  
- Verstehen der Architektur und Komponenten der Windows AI Foundry-Plattform  
- Navigation durch den gesamten KI-Entwicklungslebenszyklus im Windows-Ökosystem  
- Implementierung von Sicherheitsbest-Practices für KI-Anwendungen auf dem Gerät  
- Optimierung von Anwendungen für verschiedene Windows-Hardwarekonfigurationen  

**API-Integrationskompetenz**  
- Beherrschung der Windows AI APIs für Text-, Bild- und multimodale Anwendungen  
- Implementierung der Phi Silica Sprachmodell-Integration für Textgenerierung und logisches Denken  
- Bereitstellung von Computer-Vision-Funktionen mit integrierten Bildverarbeitungs-APIs  
- Anpassung vortrainierter Modelle mit LoRA (Low-Rank Adaptation)-Techniken  

**Lokale Implementierung der Foundry**  
- Durchsuchen, Bewerten und Bereitstellen von Open-Source-Sprachmodellen mit Foundry Local CLI  
- Verstehen von Modelloptimierung und Quantisierung für lokale Bereitstellung  
- Implementierung von Offline-KI-Funktionen, die ohne Internetverbindung funktionieren  
- Verwaltung von Modelllebenszyklen und Updates in Produktionsumgebungen  

**Windows ML-Bereitstellung**  
- Integration benutzerdefinierter ONNX-Modelle in Windows-Anwendungen mit Windows ML  
- Nutzung automatischer Hardwarebeschleunigung über CPU-, GPU- und NPU-Architekturen  
- Implementierung von Echtzeit-Inferenz mit optimaler Ressourcennutzung  
- Design skalierbarer KI-Anwendungen für verschiedene Windows-Gerätekategorien  

### Fähigkeiten in der Anwendungsentwicklung

**Plattformübergreifende Windows-Entwicklung**  
- Erstellung KI-gestützter Anwendungen mit .NET MAUI für universelle Windows-Bereitstellung  
- Integration von KI-Funktionen in Win32-, UWP- und Progressive Web Applications  
- Implementierung responsiver UI-Designs, die sich an KI-Verarbeitungszustände anpassen  
- Umgang mit asynchronen KI-Operationen unter Berücksichtigung der Benutzererfahrung  

**Leistungsoptimierung**  
- Profilierung und Optimierung der KI-Inferenzleistung über verschiedene Hardwarekonfigurationen  
- Implementierung effizienter Speicherverwaltung für große Sprachmodelle  
- Design von Anwendungen, die sich basierend auf verfügbaren Hardwarekapazitäten anpassen  
- Anwendung von Caching-Strategien für häufig genutzte KI-Operationen  

**Produktionsreife**  
- Implementierung umfassender Fehlerbehandlungs- und Fallback-Mechanismen  
- Design von Telemetrie und Monitoring für die Leistung von KI-Anwendungen  
- Anwendung von Sicherheitsbest-Practices für lokale KI-Modellspeicherung und -ausführung  
- Planung von Bereitstellungsstrategien für Unternehmens- und Verbraucheranwendungen  

### Geschäftliches und strategisches Verständnis

**Architektur von KI-Anwendungen**  
- Design hybrider Architekturen, die lokale und Cloud-KI-Verarbeitung optimieren  
- Bewertung von Kompromissen zwischen Modellgröße, Genauigkeit und Inferenzgeschwindigkeit  
- Planung von Datenflussarchitekturen, die Datenschutz gewährleisten und gleichzeitig Intelligenz ermöglichen  
- Implementierung kosteneffizienter KI-Lösungen, die sich an Benutzeranforderungen anpassen  

**Marktpositionierung**  
- Verstehen der Wettbewerbsvorteile von Windows-nativen KI-Anwendungen  
- Identifizierung von Anwendungsfällen, bei denen KI auf dem Gerät überlegene Benutzererfahrungen bietet  
- Entwicklung von Go-to-Market-Strategien für KI-gestützte Windows-Anwendungen  
- Positionierung von Anwendungen zur Nutzung der Vorteile des Windows-Ökosystems  

## Komponenten der Windows AI Foundry-Plattform

### 1. Windows AI APIs

Windows AI APIs bieten einsatzbereite KI-Funktionen, die von lokal ausgeführten Modellen unterstützt werden und für Effizienz und Leistung auf Copilot+ PC-Geräten optimiert sind – mit minimalem Setup-Aufwand.

#### Kern-API-Kategorien

**Phi Silica Sprachmodell**  
- Kleines, aber leistungsstarkes Sprachmodell für Textgenerierung und logisches Denken  
- Optimiert für Echtzeit-Inferenz mit minimalem Stromverbrauch  
- Unterstützung für benutzerdefinierte Feinabstimmung mit LoRA-Techniken  
- Integration mit Windows semantischer Suche und Wissensabruf  

**Computer-Vision-APIs**  
- **Texterkennung (OCR)**: Extrahieren von Text aus Bildern mit hoher Genauigkeit  
- **Bild-Superauflösung**: Hochskalieren von Bildern mit lokalen KI-Modellen  
- **Bildsegmentierung**: Identifizieren und Isolieren spezifischer Objekte in Bildern  
- **Bildbeschreibung**: Erstellen detaillierter Textbeschreibungen für visuelle Inhalte  
- **Objektentfernung**: Entfernen unerwünschter Objekte aus Bildern mit KI-gestütztem Inpainting  

**Multimodale Funktionen**  
- **Integration von Vision und Sprache**: Kombination von Text- und Bildverständnis  
- **Semantische Suche**: Ermöglichen natürlicher Sprachabfragen über Multimedia-Inhalte  
- **Wissensabruf**: Aufbau intelligenter Sucherlebnisse mit lokalen Daten  

### 2. Foundry Local

Foundry Local bietet Entwicklern schnellen Zugriff auf einsatzbereite Open-Source-Sprachmodelle auf Windows-Silicon und ermöglicht das Durchsuchen, Testen, Interagieren und Bereitstellen von Modellen in lokalen Anwendungen.

#### Hauptfunktionen

**Modellkatalog**  
- Umfassende Sammlung voroptimierter Open-Source-Modelle  
- Modelle, die für CPUs, GPUs und NPUs optimiert sind und sofort bereitgestellt werden können  
- Unterstützung für beliebte Modellfamilien wie Llama, Mistral, Phi und spezialisierte Domänenmodelle  

**CLI-Integration**  
- Befehlszeilenschnittstelle für Modellverwaltung und Bereitstellung  
- Automatisierte Workflows für Optimierung und Quantisierung  
- Integration mit beliebten Entwicklungsumgebungen und CI/CD-Pipelines  

**Lokale Bereitstellung**  
- Vollständiger Offline-Betrieb ohne Cloud-Abhängigkeiten  
- Unterstützung für benutzerdefinierte Modellformate und -konfigurationen  
- Effiziente Modellbereitstellung mit automatischer Hardware-Optimierung  

### 3. Windows ML

Windows ML dient als zentrale KI-Plattform und integrierte Inferenz-Laufzeit auf Windows, die es Entwicklern ermöglicht, benutzerdefinierte Modelle effizient im breiten Windows-Hardware-Ökosystem bereitzustellen.

#### Vorteile der Architektur

**Universelle Hardware-Unterstützung**  
- Automatische Optimierung für AMD-, Intel-, NVIDIA- und Qualcomm-Chipsätze  
- Unterstützung für CPU-, GPU- und NPU-Ausführung mit transparentem Wechsel  
- Hardware-Abstraktion, die plattformspezifische Optimierungsarbeit eliminiert  

**Modellflexibilität**  
- Unterstützung für das ONNX-Modellformat mit automatischer Konvertierung aus beliebten Frameworks  
- Bereitstellung benutzerdefinierter Modelle mit Leistung auf Produktionsniveau  
- Integration in bestehende Windows-Anwendungsarchitekturen  

**Unternehmensintegration**  
- Kompatibilität mit Windows-Sicherheits- und Compliance-Frameworks  
- Unterstützung für Unternehmensbereitstellungs- und Verwaltungstools  
- Integration mit Windows-Geräteverwaltung und Überwachungssystemen  

## Entwicklungsworkflow

### Phase 1: Einrichtung der Umgebung und Konfiguration der Tools

**Vorbereitung der Entwicklungsumgebung**  
1. Installation von Visual Studio mit der AI Toolkit-Erweiterung  
2. Konfiguration der Windows AI Foundry CLI-Tools  
3. Einrichtung einer lokalen Testumgebung für Modelle  
4. Einrichtung von Tools zur Leistungsprofilierung und Überwachung  

**Erkundung der AI Dev Gallery**  
- Durchsuchen von Beispielanwendungen und Referenzimplementierungen  
- Testen der Windows AI APIs mit interaktiven Demonstrationen  
- Überprüfung des Quellcodes für Best-Practices und Muster  
- Identifizierung relevanter Beispiele für Ihren spezifischen Anwendungsfall  

### Phase 2: Modellauswahl und Integration

**Anforderungsanalyse**  
- Definition funktionaler Anforderungen für KI-Funktionen  
- Festlegung von Leistungsbeschränkungen und Optimierungszielen  
- Bewertung von Datenschutz- und Sicherheitsanforderungen  
- Planung der Bereitstellungsarchitektur und Skalierungsstrategien  

**Modellbewertung**  
- Verwendung von Foundry Local zum Testen von Open-Source-Modellen für Ihren Anwendungsfall  
- Benchmarking der Windows AI APIs im Vergleich zu benutzerdefinierten Modellanforderungen  
- Bewertung von Kompromissen zwischen Modellgröße, Genauigkeit und Inferenzgeschwindigkeit  
- Prototyping von Integrationsansätzen mit ausgewählten Modellen  

### Phase 3: Anwendungsentwicklung

**Kernintegration**  
- Implementierung der Windows AI API-Integration mit ordnungsgemäßer Fehlerbehandlung  
- Design von Benutzeroberflächen, die KI-Verarbeitungsworkflows berücksichtigen  
- Implementierung von Caching- und Optimierungsstrategien für Modellinferenz  
- Hinzufügen von Telemetrie und Überwachung für die Leistung von KI-Operationen  

**Testen und Validierung**  
- Testen von Anwendungen auf verschiedenen Windows-Hardwarekonfigurationen  
- Validierung von Leistungskennzahlen unter verschiedenen Lastbedingungen  
- Implementierung automatisierter Tests für die Zuverlässigkeit von KI-Funktionen  
- Durchführung von Benutzererfahrungstests mit KI-gestützten Funktionen  

### Phase 4: Optimierung und Bereitstellung

**Leistungsoptimierung**  
- Profilierung der Anwendungsleistung über Zielhardwarekonfigurationen  
- Optimierung der Speichernutzung und Modelllade-Strategien  
- Implementierung adaptiven Verhaltens basierend auf verfügbaren Hardwarekapazitäten  
- Feinabstimmung der Benutzererfahrung für verschiedene Leistungsszenarien  

**Produktionsbereitstellung**  
- Verpackung von Anwendungen mit den richtigen KI-Modellabhängigkeiten  
- Implementierung von Aktualisierungsmechanismen für Modelle und Anwendungslogik  
- Konfiguration von Überwachung und Analytik für Produktionsumgebungen  
- Planung von Rollout-Strategien für Unternehmens- und Verbraucherbereitstellungen  

## Praktische Implementierungsbeispiele

### Beispiel 1: Intelligente Dokumentenverarbeitungsanwendung

Erstellen einer Windows-Anwendung, die Dokumente mit mehreren KI-Funktionen verarbeitet:

**Verwendete Technologien:**  
- Phi Silica für Dokumentzusammenfassung und Beantwortung von Fragen  
- OCR-APIs für Textextraktion aus gescannten Dokumenten  
- Bildbeschreibungs-APIs für Analyse von Diagrammen und Grafiken  
- Benutzerdefinierte ONNX-Modelle für Dokumentklassifizierung  

**Implementierungsansatz:**  
- Design einer modularen Architektur mit einsteckbaren KI-Komponenten  
- Implementierung asynchroner Verarbeitung für große Dokumentenstapel  
- Hinzufügen von Fortschrittsanzeigen und Abbruchunterstützung für langlaufende Operationen  
- Einschluss von Offline-Funktionen für die Verarbeitung sensibler Dokumente  

### Beispiel 2: Einzelhandels-Inventarverwaltungssystem

Erstellen eines KI-gestützten Inventarsystems für Einzelhandelsanwendungen:

**Verwendete Technologien:**  
- Bildsegmentierung für Produktidentifikation  
- Benutzerdefinierte Vision-Modelle für Marken- und Kategorienklassifizierung  
- Foundry Local-Bereitstellung spezialisierter Einzelhandels-Sprachmodelle  
- Integration mit bestehenden POS- und Inventarsystemen  

**Implementierungsansatz:**  
- Aufbau einer Kameraintegration für Echtzeit-Produktscanning  
- Implementierung von Barcode- und visueller Produktidentifikation  
- Hinzufügen natürlicher Sprachabfragen für Inventar mit lokalen Sprachmodellen  
- Design einer skalierbaren Architektur für den Einsatz in mehreren Filialen  

### Beispiel 3: Dokumentationsassistent im Gesundheitswesen

Entwicklung eines datenschutzfreundlichen Dokumentationstools für das Gesundheitswesen:

**Verwendete Technologien:**  
- Phi Silica für medizinische Notizenerstellung und klinische Entscheidungsunterstützung  
- OCR für Digitalisierung handgeschriebener medizinischer Aufzeichnungen  
- Benutzerdefinierte medizinische Sprachmodelle, bereitgestellt über Windows ML  
- Lokale Vektorspeicherung für medizinischen Wissensabruf  

**Implementierungsansatz:**  
- Sicherstellung vollständiger Offline-Funktionalität für Patientendatenschutz  
- Implementierung von Validierung und Vorschlägen für medizinische Terminologie  
- Hinzufügen von Audit-Logging für regulatorische Compliance  
- Design der Integration mit bestehenden elektronischen Patientenakten-Systemen  

## Leistungsoptimierungsstrategien

### Hardwarebewusste Entwicklung

**NPU-Optimierung**  
- Design von Anwendungen zur Nutzung von NPU-Funktionen auf Copilot+ PCs  
- Implementierung eines sanften Rückfalls auf GPU/CPU bei Geräten ohne NPU  
- Optimierung von Modellformaten für NPU-spezifische Beschleunigung  
- Überwachung der NPU-Auslastung und thermischen Eigenschaften  

**Speicherverwaltung**  
- Implementierung effizienter Modelllade- und Caching-Strategien  
- Verwendung von Speicher-Mapping für große Modelle zur Reduzierung der Startzeit  
- Design speicherbewusster Anwendungen für ressourcenbeschränkte Geräte  
- Implementierung von Modellquantisierung zur Speicheroptimierung  

**Batterieeffizienz**  
- Optimierung von KI-Operationen für minimalen Stromverbrauch  
- Implementierung adaptiver Verarbeitung basierend auf Batteriestatus  
- Design effizienter Hintergrundverarbeitung für kontinuierliche KI-Operationen  
- Verwendung von Stromprofilierungs-Tools zur Optimierung des Energieverbrauchs  

### Skalierbarkeitsüberlegungen

**Multithreading**  
- Design von threadsicheren KI-Operationen für parallele Verarbeitung  
- Implementierung effizienter Arbeitsverteilung über verfügbare Kerne  
- Verwendung von async/await-Mustern für nicht blockierende KI-Operationen  
- Planung der Threadpool-Optimierung für verschiedene Hardwarekonfigurationen  

**Caching-Strategien**  
- Implementierung intelligenter Caching-Mechanismen für häufig genutzte KI-Operationen  
- Design von Cache-Invalidierungsstrategien für Modellupdates  
- Verwendung von persistentem Caching für teure Vorverarbeitungsoperationen  
- Implementierung von verteiltem Caching für Mehrbenutzerszenarien  

## Sicherheits- und Datenschutzbest-Practices

### Datenschutz

**Lokale Verarbeitung**  
- Sicherstellen, dass sensible Daten niemals das lokale Gerät verlassen  
- Implementierung sicherer Speicherung für KI-Modelle und temporäre Daten  
- Verwendung von Windows-Sicherheitsfunktionen für Anwendungssandboxing  
- Anwendung von Verschlüsselung für gespeicherte Modelle und Zwischenergebnisse  

**Modellsicherheit**  
- Validierung der Modellintegrität vor dem Laden und der Ausführung  
- Implementierung sicherer Mechanismen für Modellupdates  
- Verwendung signierter Modelle zur Verhinderung von Manipulationen  
- Anwendung von Zugriffskontrollen für Modelfiles und Konfigurationen  

### Compliance-Überlegungen

**Regulatorische Ausrichtung**  
- Design von Anwendungen zur Einhaltung von GDPR, HIPAA und anderen Vorschriften  
- Implementierung von Audit-Logging für KI-Entscheidungsprozesse  
- Bereitstellung von Transparenzfunktionen für KI-generierte Ergebnisse  
- Ermöglichung der Benutzerkontrolle über KI-Datenverarbeitung  

**Unternehmenssicherheit**  
- Integration mit Windows-Unternehmenssicherheitsrichtlinien  
- Unterstützung verwalteter Bereitstellung durch Unternehmensverwaltungstools  
- Implementierung rollenbasierter Zugriffskontrollen für KI-Funktionen  
- Bereitstellung administrativer Steuerungen für KI-Funktionalität  

## Fehlerbehebung und Debugging

### Häufige Entwicklungsprobleme

**Probleme beim Modell-Laden**  
- Validierung der ONNX-Modellkompatibilität mit Windows ML  
- Überprüfung der Modelldatei-Integrität und Formatanforderungen  
- Verifizierung der Hardwarekapazitätsanforderungen für spezifische Modelle  
- Debugging von Speicherzuweisungsproblemen beim Modell-Laden  

**Leistungsprobleme**  
- Profilierung der Anwendungsleistung über verschiedene Hardwarekonfigurationen  
- Identifizierung von Engpässen in KI-Verarbeitungspipelines  
- Optimierung von Datenvorverarbeitungs- und Nachverarbeitungsoperationen  
- Implementierung von Leistungsüberwachung und Alarmierung  

**Integrationsschwierigkeiten**  
- Debugging von API-Integrationsproblemen mit ordnungsgemäßer Fehlerbehandlung  
- Validierung von Eingabedatenformaten und Vorverarbeitungsanforderungen  
- Umfassendes Testen von Randfällen und Fehlerbedingungen  
- Implementierung umfassender Protokollierung zur Fehlerbehebung in Produktionsumgebungen  

### Debugging-Tools und Techniken

**Visual
- Nutzen Sie das Foundry Local CLI für Modelltests und Validierung  
- Verwenden Sie die Windows AI API-Testtools zur Überprüfung der Integration  
- Implementieren Sie benutzerdefiniertes Logging zur Überwachung von KI-Operationen  
- Erstellen Sie automatisierte Tests für die Zuverlässigkeit der KI-Funktionalität  

## Zukunftssicherung Ihrer Anwendungen  

### Aufkommende Technologien  

**Hardware der nächsten Generation**  
- Entwickeln Sie Anwendungen, die zukünftige NPU-Funktionen nutzen können  
- Planen Sie für größere Modellgrößen und höhere Komplexität  
- Implementieren Sie adaptive Architekturen für sich weiterentwickelnde Hardware  
- Berücksichtigen Sie quantenfähige Algorithmen für zukünftige Kompatibilität  

**Fortschrittliche KI-Fähigkeiten**  
- Bereiten Sie sich auf die Integration multimodaler KI über mehr Datentypen vor  
- Planen Sie für Echtzeit-Kollaborationen zwischen mehreren Geräten  
- Entwickeln Sie für Fähigkeiten des föderierten Lernens  
- Berücksichtigen Sie hybride Intelligenzarchitekturen zwischen Edge und Cloud  

### Kontinuierliches Lernen und Anpassung  

**Modell-Updates**  
- Implementieren Sie nahtlose Mechanismen für Modellaktualisierungen  
- Entwickeln Sie Anwendungen, die sich an verbesserte Modellfähigkeiten anpassen  
- Planen Sie die Abwärtskompatibilität mit bestehenden Modellen  
- Führen Sie A/B-Tests zur Bewertung der Modellleistung durch  

**Feature-Entwicklung**  
- Entwickeln Sie modulare Architekturen, die neue KI-Fähigkeiten aufnehmen können  
- Planen Sie die Integration neuer Windows AI APIs  
- Implementieren Sie Feature-Flags für eine schrittweise Einführung von Funktionen  
- Entwickeln Sie Benutzeroberflächen, die sich an erweiterte KI-Funktionen anpassen  

## Fazit  

Die Entwicklung von Windows Edge AI repräsentiert die Verbindung leistungsstarker KI-Fähigkeiten mit der robusten, sicheren und skalierbaren Windows-Plattform. Durch die Beherrschung des Windows AI Foundry-Ökosystems können Entwickler intelligente Anwendungen erstellen, die außergewöhnliche Benutzererlebnisse bieten und gleichzeitig höchste Standards in Bezug auf Datenschutz, Sicherheit und Leistung einhalten.  

Die Kombination aus Windows AI APIs, Foundry Local und Windows ML bietet eine unvergleichliche Grundlage für die Entwicklung der nächsten Generation intelligenter Windows-Anwendungen. Während sich die KI weiterentwickelt, stellt die Windows-Plattform sicher, dass Ihre Anwendungen mit aufkommenden Technologien skalieren und gleichzeitig Kompatibilität und Leistung über die vielfältige Windows-Hardwarelandschaft hinweg beibehalten.  

Egal, ob Sie Verbraucheranwendungen, Unternehmenslösungen oder spezialisierte Branchenwerkzeuge entwickeln – die Windows Edge AI-Entwicklung ermöglicht es Ihnen, intelligente, reaktionsschnelle und tief integrierte Erlebnisse zu schaffen, die das volle Potenzial moderner Windows-Geräte ausschöpfen.  

## Zusätzliche Ressourcen  

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

*Dieser Leitfaden ist darauf ausgelegt, sich mit dem schnell fortschreitenden Windows AI-Ökosystem weiterzuentwickeln. Regelmäßige Updates gewährleisten die Ausrichtung an den neuesten Plattformfähigkeiten und bewährten Entwicklungspraktiken.*  

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.