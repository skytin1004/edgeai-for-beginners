<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T20:34:59+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "de"
}
-->
# Änderungsprotokoll

Alle wichtigen Änderungen an EdgeAI for Beginners sind hier dokumentiert. Dieses Projekt verwendet ein datumsbasiertes Format und den Stil von Keep a Changelog (Hinzugefügt, Geändert, Behoben, Entfernt, Dokumentation, Verschoben).

## 2025-10-08

### Hinzugefügt - Umfassendes Workshop-Update
- **Komplette Neufassung der Workshop README.md**:
  - Umfassende Einführung hinzugefügt, die den Mehrwert von Edge AI erklärt (Datenschutz, Leistung, Kosten)
  - Sechs zentrale Lernziele mit detaillierten Kompetenzen erstellt
  - Tabelle mit Lernergebnissen, Liefergegenständen und Kompetenzmatrix hinzugefügt
  - Abschnitt zu berufsrelevanten Fähigkeiten für die Industrie hinzugefügt
  - Schnellstartanleitung mit Voraussetzungen und 3-Schritt-Setup hinzugefügt
  - Ressourcentabellen für Python-Beispiele erstellt (8 Dateien mit Laufzeiten)
  - Tabelle für Jupyter-Notebooks hinzugefügt (8 Notebooks mit Schwierigkeitsbewertungen)
  - Dokumentationstabelle erstellt (7 wichtige Dokumente mit „Wann verwenden“-Hinweisen)
  - Lernpfadempfehlungen für verschiedene Fähigkeitsstufen hinzugefügt

- **Validierungs- und Testinfrastruktur für den Workshop**:
  - `scripts/validate_samples.py` erstellt – Umfassendes Validierungstool für Syntax, Imports und Best Practices
  - `scripts/test_samples.py` erstellt – Smoke-Test-Runner für alle Python-Beispiele
  - Validierungsdokumentation zu `scripts/README.md` hinzugefügt

- **Umfassende Dokumentation**:
  - `SAMPLES_UPDATE_SUMMARY.md` erstellt – 400+ Zeilen umfassender Leitfaden zu allen Verbesserungen
  - `UPDATE_COMPLETE.md` erstellt – Zusammenfassung der abgeschlossenen Updates
  - `QUICK_REFERENCE.md` erstellt – Schnellreferenzkarte für den Workshop

### Geändert - Modernisierung der Python-Beispiele im Workshop
- **Alle 8 Python-Beispiele mit Best Practices aktualisiert**:
  - Verbesserte Fehlerbehandlung mit try-except-Blöcken für alle I/O-Operationen
  - Typ-Hinweise und umfassende Docstrings hinzugefügt
  - Konsistentes [INFO]/[ERROR]/[RESULT]-Logging-Muster implementiert
  - Optionale Imports mit Installationshinweisen geschützt
  - Benutzerfeedback in allen Beispielen verbessert

- **session01/chat_bootstrap.py**:
  - Verbesserte Client-Initialisierung mit umfassenden Fehlermeldungen
  - Verbesserte Fehlerbehandlung beim Streaming mit Chunk-Validierung
  - Bessere Ausnahmebehandlung bei Nichtverfügbarkeit des Dienstes hinzugefügt

- **session02/rag_pipeline.py**:
  - Importguards für sentence-transformers mit Installationshinweisen hinzugefügt
  - Verbesserte Fehlerbehandlung bei Einbettungs- und Generierungsoperationen
  - Verbesserte Ausgabeformatierung mit strukturierten Ergebnissen

- **session02/rag_eval_ragas.py**:
  - Optionale Imports (ragas, datasets) mit benutzerfreundlichen Fehlermeldungen geschützt
  - Fehlerbehandlung für Bewertungsmetriken hinzugefügt
  - Verbesserte Ausgabeformatierung für Bewertungsergebnisse

- **session03/benchmark_oss_models.py**:
  - Graceful Degradation implementiert (Fortsetzung bei Modellfehlern)
  - Detaillierte Fortschrittsberichte und Fehlerbehandlung pro Modell hinzugefügt
  - Verbesserte Statistikberechnung mit umfassender Fehlerbehebung

- **session04/model_compare.py**:
  - Typ-Hinweise hinzugefügt (Tuple-Rückgabetypen)
  - Verbesserte Ausgabeformatierung mit strukturierten JSON-Ergebnissen
  - Fehlerbehandlung pro Modell mit Wiederherstellung implementiert

- **session05/agents_orchestrator.py**:
  - Agent.act() mit umfassenden Docstrings verbessert
  - Fehlerbehandlung in der Pipeline mit stufenweiser Protokollierung hinzugefügt
  - Verbesserte Speicherverwaltung und Statusverfolgung

- **session06/models_router.py**:
  - Funktionsdokumentation für alle Routing-Komponenten verbessert
  - Detailliertes Logging in der route()-Funktion hinzugefügt
  - Verbesserte Testausgabe mit strukturierten Ergebnissen

- **session06/models_pipeline.py**:
  - Fehlerbehandlung für die chat()-Hilfsfunktion hinzugefügt
  - pipeline() mit Stufenprotokollierung und Fortschrittsberichten verbessert
  - main() mit umfassender Fehlerbehebung verbessert

### Dokumentation - Verbesserungen der Workshop-Dokumentation
- Haupt-README.md mit Workshop-Abschnitt aktualisiert, der den praktischen Lernpfad hervorhebt
- STUDY_GUIDE.md mit umfassendem Workshop-Abschnitt verbessert, einschließlich:
  - Lernziele und Studienschwerpunkte
  - Selbstbewertungsfragen
  - Praktische Übungen mit Zeitangaben
  - Zeitaufteilung für konzentriertes und Teilzeitstudium
  - Workshop zur Fortschrittsverfolgungsvorlage hinzugefügt
- Zeitaufteilung von 20 Stunden auf 30 Stunden aktualisiert (einschließlich Workshop)
- Workshop-Beispielbeschreibungen und Lernergebnisse zur README hinzugefügt

### Behoben
- Inkonsistente Fehlerbehandlungsmuster in Workshop-Beispielen behoben
- Fehler bei optionalen Abhängigkeitsimports mit geeigneten Guards behoben
- Fehlende Typ-Hinweise in kritischen Funktionen korrigiert
- Unzureichendes Benutzerfeedback in Fehlerszenarien behoben
- Validierungsprobleme mit umfassender Testinfrastruktur behoben

---

## 2025-09-23

### Geändert - Große Modernisierung von Modul 08
- **Umfassende Angleichung an Microsoft Foundry-Local Repository-Muster**:
  - Alle Codebeispiele aktualisiert, um moderne `FoundryLocalManager`- und OpenAI-SDK-Integration zu verwenden
  - Veraltete manuelle `requests`-Aufrufe durch korrekte SDK-Nutzung ersetzt
  - Implementierungsmuster an offizielle Microsoft-Dokumentation und Beispiele angepasst

- **05.AIPoweredAgents.md Modernisierung**:
  - Multi-Agent-Orchestrierung aktualisiert, um moderne SDK-Muster zu verwenden
  - Koordinator-Implementierung mit erweiterten Funktionen (Feedback-Schleifen, Leistungsüberwachung) verbessert
  - Umfassende Fehlerbehandlung und Dienstgesundheitsprüfung hinzugefügt
  - Korrekte Verweise auf lokale Beispiele integriert (`samples/05/multi_agent_orchestration.ipynb`)
  - Funktionsaufrufbeispiele aktualisiert, um moderne `tools`-Parameter anstelle veralteter `functions` zu verwenden
  - Produktionsreife Muster mit Überwachung und Statistikverfolgung hinzugefügt

- **06.ModelsAsTools.md komplette Neufassung**:
  - Basis-Tool-Registry durch intelligente Modell-Router-Implementierung ersetzt
  - Schlüsselwortbasierte Modellauswahl für verschiedene Aufgabentypen (allgemein, logisches Denken, Code, kreativ) hinzugefügt
  - Umgebungskonfiguration mit flexibler Modellzuweisung integriert
  - Umfassende Dienstgesundheitsüberwachung und Fehlerbehandlung hinzugefügt
  - Produktionsbereitstellungsmuster mit Anforderungsüberwachung und Leistungsüberwachung hinzugefügt
  - Angleichung an lokale Implementierung in `samples/06/router.py` und `samples/06/model_router.ipynb`

- **Verbesserungen der Dokumentationsstruktur**:
  - Überblicksabschnitte hinzugefügt, die Modernisierung und SDK-Angleichung hervorheben
  - Verbesserte Lesbarkeit durch Emojis und bessere Formatierung
  - Korrekte Verweise auf lokale Beispieldateien in der gesamten Dokumentation hinzugefügt
  - Produktionsreife Implementierungsleitfäden und Best Practices integriert

### Hinzugefügt
- Umfassende Überblicksabschnitte in Modul-08-Dateien, die moderne SDK-Integration hervorheben
- Architektur-Highlights mit erweiterten Funktionen (Multi-Agent-Systeme, intelligentes Routing)
- Direkte Verweise auf lokale Beispielimplementierungen für praktische Erfahrungen
- Produktionsbereitstellungshinweise mit Überwachungs- und Fehlerbehandlungsmustern
- Interaktive Jupyter-Notebook-Beispiele mit erweiterten Funktionen und Benchmarks

### Behoben
- Abweichungen zwischen Dokumentation und tatsächlichen Beispielimplementierungen behoben
- Veraltete SDK-Nutzungsmuster in Modul 08 aktualisiert
- Fehlende Verweise auf umfassende lokale Beispielbibliothek korrigiert
- Inkonsistente Implementierungsansätze in verschiedenen Abschnitten behoben

---

## 2025-09-18

### Hinzugefügt
- Modul 08: Microsoft Foundry Local – Komplettes Entwickler-Toolkit
  - Sechs Sitzungen: Einrichtung, Azure AI Foundry-Integration, Open-Source-Modelle, fortschrittliche Demos, Agenten und Modelle-als-Tools
  - Ausführbare Beispiele unter `Module08/samples/01`–`06` mit Windows-Cmd-Anweisungen:
    - `01` REST-Schnellchat (`chat_quickstart.py`)
    - `02` SDK-Schnellstart mit OpenAI/Foundry Local und Azure OpenAI-Unterstützung (`sdk_quickstart.py`)
    - `03` CLI List-and-Bench (`list_and_bench.cmd`)
    - `04` Chainlit-Demo (`app.py`)
    - `05` Multi-Agent-Orchestrierung (`python -m samples.05.agents.coordinator`)
    - `06` Modelle-als-Tools-Router (`router.py`)
- Azure OpenAI-Unterstützung im SDK-Beispiel der Sitzung 2 mit Umgebungsvariablenkonfiguration
- `.vscode/settings.json`, um auf `Module08/.venv` zu verweisen und die Python-Analyseauflösung zu verbessern
- `.env` mit `PYTHONPATH`-Hinweis für VS Code/Pylance-Erkennung

### Geändert
- Standardmodell auf `phi-4-mini` in Modul-08-Dokumenten und -Beispielen aktualisiert; verbleibende Erwähnungen von `phi-3.5` in Modul 08 entfernt
- Verbesserungen am Router (`Module08/samples/06/router.py`):
  - Endpunkt-Erkennung über `foundry service status` mit Regex-Parsing
  - `/v1/models`-Gesundheitsprüfung beim Start
  - Umgebungskonfigurierbare Modell-Registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Anforderungen aktualisiert: `Module08/requirements.txt` enthält jetzt `openai` (neben `requests`, `chainlit`)
- Chainlit-Beispielanleitung klargestellt und Fehlerbehebung hinzugefügt; Importauflösung über Arbeitsbereichseinstellungen

### Behoben
- Importprobleme gelöst:
  - Router hängt nicht mehr von einem nicht existierenden `utils`-Modul ab; Funktionen sind integriert
  - Koordinator verwendet relative Imports (`from .specialists import ...`) und wird über den Modulpfad aufgerufen
  - VS Code/Pylance-Konfiguration zur Auflösung von `chainlit` und Paketimports
- Kleinere Tippfehler in `STUDY_GUIDE.md` korrigiert und Modul-08-Abdeckung hinzugefügt

### Entfernt
- Nicht verwendetes `Module08/infra/obs.py` gelöscht und das leere `infra/`-Verzeichnis entfernt; Beobachtungsmuster als optional in der Dokumentation beibehalten

### Verschoben
- Modul-08-Demos unter `Module08/samples` mit nummerierten Sitzungsordnern konsolidiert
  - Chainlit-App nach `samples/04` verschoben
  - Agenten nach `samples/05` verschoben und `__init__.py`-Dateien für Paketauflösung hinzugefügt

### Dokumentation
- Modul-08-Sitzungsdokumente und alle Beispiel-READMEs mit Microsoft Learn und vertrauenswürdigen Anbieterreferenzen angereichert
- `Module08/README.md` mit Übersicht über Beispiele, Router-Konfiguration und Validierungstipps aktualisiert
- `Module07/README.md` Windows Foundry Local-Abschnitt gegen Learn-Dokumente validiert
- `STUDY_GUIDE.md` aktualisiert:
  - Modul 08 zur Übersicht, Zeitplänen, Fortschrittsverfolgung hinzugefügt
  - Umfassender Referenzabschnitt hinzugefügt (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (Zusammenfassung)
- Kursarchitektur und Module etabliert (Module 01–07)
- Iterative Inhaltsmodernisierung, Formatierungsstandardisierung und hinzugefügte Fallstudien
- Erweiterte Abdeckung von Optimierungsframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unveröffentlicht / Backlog (Vorschläge)
- Optionale Smoke-Tests pro Beispiel, um die Verfügbarkeit von Foundry Local zu validieren
- Übersetzungen überprüfen, um Modellreferenzen (z. B. `phi-4-mini`) entsprechend abzugleichen
- Minimalen Pyright-Konfigurationsvorschlag hinzufügen, falls Teams arbeitsbereichsweite Strenge bevorzugen

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.