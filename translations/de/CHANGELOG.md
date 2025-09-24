<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T11:40:22+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "de"
}
-->
# Änderungsprotokoll

Alle wichtigen Änderungen an EdgeAI for Beginners sind hier dokumentiert. Dieses Projekt verwendet datumsbasierte Einträge und den Keep a Changelog-Stil (Hinzugefügt, Geändert, Behoben, Entfernt, Dokumentation, Verschoben).

## 2025-09-23

### Geändert - Hauptmodul 08 Modernisierung
- **Umfassende Anpassung an Microsoft Foundry-Local Repository-Muster**
  - Alle Codebeispiele aktualisiert, um moderne `FoundryLocalManager`- und OpenAI-SDK-Integration zu nutzen
  - Veraltete manuelle `requests`-Aufrufe durch korrekte SDK-Nutzung ersetzt
  - Implementierungsmuster an die offizielle Microsoft-Dokumentation und Beispiele angepasst

- **05.AIPoweredAgents.md Modernisierung**:
  - Multi-Agent-Orchestrierung aktualisiert, um moderne SDK-Muster zu verwenden
  - Koordinator-Implementierung mit erweiterten Funktionen (Feedback-Schleifen, Leistungsüberwachung) verbessert
  - Umfassende Fehlerbehandlung und Service-Gesundheitsprüfung hinzugefügt
  - Korrekte Verweise auf lokale Beispiele integriert (`samples/05/multi_agent_orchestration.ipynb`)
  - Funktionsaufruf-Beispiele aktualisiert, um moderne `tools`-Parameter anstelle der veralteten `functions` zu verwenden
  - Produktionsreife Muster mit Überwachung und Statistik-Tracking hinzugefügt

- **06.ModelsAsTools.md vollständige Überarbeitung**:
  - Basis-Tool-Registry durch intelligente Modell-Router-Implementierung ersetzt
  - Schlüsselwortbasierte Modellauswahl für verschiedene Aufgabentypen (allgemein, logisches Denken, Code, Kreativität) hinzugefügt
  - Umgebungskonfiguration mit flexibler Modellzuweisung integriert
  - Verbesserte Service-Gesundheitsüberwachung und Fehlerbehandlung hinzugefügt
  - Produktionsbereitstellungsmuster mit Anfragenüberwachung und Leistungs-Tracking hinzugefügt
  - An lokale Implementierung in `samples/06/router.py` und `samples/06/model_router.ipynb` angepasst

- **Verbesserungen der Dokumentationsstruktur**:
  - Übersichtskapitel hinzugefügt, die Modernisierung und SDK-Ausrichtung hervorheben
  - Mit Emojis und besserer Formatierung für verbesserte Lesbarkeit angereichert
  - Korrekte Verweise auf lokale Beispieldateien in der gesamten Dokumentation hinzugefügt
  - Produktionsreife Implementierungsrichtlinien und Best Practices integriert

### Hinzugefügt
- Umfassende Übersichtskapitel in Modul 08-Dateien, die moderne SDK-Integration hervorheben
- Architektur-Highlights mit erweiterten Funktionen (Multi-Agent-Systeme, intelligentes Routing)
- Direkte Verweise auf lokale Beispielimplementierungen für praktische Erfahrungen
- Produktionsbereitstellungshinweise mit Überwachungs- und Fehlerbehandlungsmustern
- Interaktive Jupyter-Notebook-Beispiele mit erweiterten Funktionen und Benchmarks

### Behoben
- Abweichungen zwischen Dokumentation und tatsächlichen Beispielimplementierungen
- Veraltete SDK-Nutzungsmuster im gesamten Modul 08
- Fehlende Verweise auf umfassende lokale Beispielbibliothek
- Inkonsistente Implementierungsansätze in verschiedenen Abschnitten

---

## 2025-09-18

### Hinzugefügt
- Modul 08: Microsoft Foundry Local – Komplettes Entwickler-Toolkit
  - Sechs Sitzungen: Einrichtung, Azure AI Foundry-Integration, Open-Source-Modelle, modernste Demos, Agenten und Modelle-als-Tools
  - Ausführbare Beispiele unter `Module08/samples/01`–`06` mit Windows-Cmd-Anweisungen
    - `01` REST-Schnellchat (`chat_quickstart.py`)
    - `02` SDK-Schnellstart mit OpenAI/Foundry Local und Azure OpenAI-Unterstützung (`sdk_quickstart.py`)
    - `03` CLI Liste-und-Benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-Demo (`app.py`)
    - `05` Multi-Agent-Orchestrierung (`python -m samples.05.agents.coordinator`)
    - `06` Modelle-als-Tools-Router (`router.py`)
- Azure OpenAI-Unterstützung im SDK-Beispiel der Sitzung 2 mit Umgebungsvariablenkonfiguration
- `.vscode/settings.json`, um auf `Module08/.venv` zu verweisen und die Python-Analyseauflösung zu verbessern
- `.env` mit `PYTHONPATH`-Hinweis für VS Code/Pylance-Erkennung

### Geändert
- Standardmodell auf `phi-4-mini` in Modul 08-Dokumenten und Beispielen aktualisiert; verbleibende `phi-3.5`-Erwähnungen innerhalb von Modul 08 entfernt
- Verbesserungen am Router (`Module08/samples/06/router.py`):
  - Endpunkt-Erkennung über `foundry service status` mit Regex-Parsing
  - `/v1/models`-Gesundheitsprüfung beim Start
  - Umgebungskonfigurierbare Modell-Registry (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Anforderungen aktualisiert: `Module08/requirements.txt` enthält jetzt `openai` (neben `requests`, `chainlit`)
- Chainlit-Beispielanleitung klargestellt und Fehlerbehebung hinzugefügt; Importauflösung über Arbeitsbereichseinstellungen

### Behoben
- Importprobleme gelöst:
  - Router hängt nicht mehr von einem nicht existierenden `utils`-Modul ab; Funktionen sind integriert
  - Koordinator verwendet relative Importe (`from .specialists import ...`) und wird über den Modulpfad aufgerufen
  - VS Code/Pylance-Konfiguration zur Auflösung von `chainlit` und Paketimporten
- Kleinere Tippfehler in `STUDY_GUIDE.md` korrigiert und Modul 08-Abdeckung hinzugefügt

### Entfernt
- Nicht verwendetes `Module08/infra/obs.py` gelöscht und das leere `infra/`-Verzeichnis entfernt; Beobachtungsmuster als optional in der Dokumentation beibehalten

### Verschoben
- Modul 08-Demos unter `Module08/samples` mit nach Sitzungen nummerierten Ordnern konsolidiert
  - Chainlit-App nach `samples/04` verschoben
  - Agenten nach `samples/05` verschoben und `__init__.py`-Dateien für Paketauflösung hinzugefügt

### Dokumentation
- Modul 08-Sitzungsdokumente und alle Beispiel-READMEs mit Microsoft Learn- und vertrauenswürdigen Anbieterreferenzen angereichert
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

## Unveröffentlicht / Rückstand (Vorschläge)
- Optionale Smoke-Tests pro Beispiel, um die Verfügbarkeit von Foundry Local zu validieren
- Übersetzungen überprüfen, um Modellreferenzen (z. B. `phi-4-mini`) entsprechend anzupassen
- Minimalen Pyright-Konfigurationsvorschlag hinzufügen, falls Teams arbeitsbereichsweite Strenge bevorzugen

---

