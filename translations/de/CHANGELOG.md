<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T12:50:20+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "de"
}
-->
# Änderungsprotokoll

Alle wichtigen Änderungen an EdgeAI for Beginners werden hier dokumentiert. Dieses Projekt verwendet ein datumsbasiertes Eintragsformat und den Keep a Changelog-Stil (Hinzugefügt, Geändert, Behoben, Entfernt, Dokumentation, Verschoben).

## 2025-09-18

### Hinzugefügt
- Modul 08: Microsoft Foundry Local – Komplettes Entwickler-Toolkit
  - Sechs Sitzungen: Einrichtung, Azure AI Foundry-Integration, Open-Source-Modelle, fortschrittliche Demos, Agenten und Modelle-als-Werkzeuge
  - Ausführbare Beispiele unter `Module08/samples/01`–`06` mit Windows-cmd-Anweisungen
    - `01` REST Schnellstart-Chat (`chat_quickstart.py`)
    - `02` SDK Schnellstart mit OpenAI/Foundry Local und Azure OpenAI-Unterstützung (`sdk_quickstart.py`)
    - `03` CLI Liste-und-Benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-Demo (`app.py`)
    - `05` Multi-Agenten-Orchestrierung (`python -m samples.05.agents.coordinator`)
    - `06` Modelle-als-Werkzeuge-Router (`router.py`)
- Azure OpenAI-Unterstützung im SDK-Beispiel der Sitzung 2 mit Umgebungsvariablenkonfiguration
- `.vscode/settings.json`, um auf `Module08/.venv` zu verweisen und die Python-Analyseauflösung zu verbessern
- `.env` mit `PYTHONPATH`-Hinweis für VS Code/Pylance-Erkennung

### Geändert
- Standardmodell in den Modul-08-Dokumenten und -Beispielen auf `phi-4-mini` aktualisiert; verbleibende Erwähnungen von `phi-3.5` innerhalb von Modul 08 entfernt
- Verbesserungen am Router (`Module08/samples/06/router.py`):
  - Endpunkt-Erkennung über `foundry service status` mit Regex-Parsing
  - `/v1/models` Gesundheitsprüfung beim Start
  - Modell-Registry konfigurierbar über Umgebungsvariablen (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Anforderungen aktualisiert: `Module08/requirements.txt` enthält jetzt `openai` (zusätzlich zu `requests`, `chainlit`)
- Anleitung für Chainlit-Beispiele klargestellt und Fehlerbehebung hinzugefügt; Importauflösung über Arbeitsbereichseinstellungen

### Behoben
- Importprobleme gelöst:
  - Router hängt nicht mehr von einem nicht existierenden `utils`-Modul ab; Funktionen wurden integriert
  - Koordinator verwendet relativen Import (`from .specialists import ...`) und wird über den Modulpfad aufgerufen
  - VS Code/Pylance-Konfiguration zur Auflösung von `chainlit`- und Paketimporten
- Kleinere Tippfehler in `STUDY_GUIDE.md` korrigiert und Modul-08-Abdeckung hinzugefügt

### Entfernt
- Nicht verwendete Datei `Module08/infra/obs.py` gelöscht und das leere Verzeichnis `infra/` entfernt; Beobachtungsmuster bleiben optional in der Dokumentation erhalten

### Verschoben
- Modul-08-Demos unter `Module08/samples` konsolidiert mit ordnernummerierten Sitzungen
  - Chainlit-App nach `samples/04` verschoben
  - Agenten nach `samples/05` verschoben und `__init__.py`-Dateien für Paketauflösung hinzugefügt

### Dokumentation
- Modul-08-Sitzungsdokumentation und alle Beispiel-READMEs mit Microsoft Learn und vertrauenswürdigen Anbieterreferenzen angereichert
- `Module08/README.md` mit Übersicht über Beispiele, Routerkonfiguration und Validierungstipps aktualisiert
- `Module07/README.md` Windows Foundry Local Abschnitt anhand der Learn-Dokumentation validiert
- `STUDY_GUIDE.md` aktualisiert:
  - Modul 08 zur Übersicht, Zeitplänen und Fortschrittsverfolgung hinzugefügt
  - Umfassender Referenzabschnitt hinzugefügt (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (Zusammenfassung)
- Kursarchitektur und Module etabliert (Module 01–07)
- Iterative Modernisierung der Inhalte, Standardisierung des Formats und Hinzufügen von Fallstudien
- Erweiterte Abdeckung von Optimierungsframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unveröffentlicht / Rückstand (Vorschläge)
- Optionale Rauchtests pro Beispiel, um die Verfügbarkeit von Foundry Local zu validieren
- Überprüfung von Übersetzungen, um Modellreferenzen (z. B. `phi-4-mini`) abzugleichen
- Hinzufügen einer minimalen pyright-Konfiguration, falls Teams arbeitsbereichsweite Strenge bevorzugen

---

