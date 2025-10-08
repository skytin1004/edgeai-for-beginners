<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "48d0fb38be925084a6ebd957d4b045e5",
  "translation_date": "2025-10-08T20:50:27+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "de"
}
-->
# EdgeAI für Einsteiger - Workshop

> **Praktischer Lernpfad für die Entwicklung produktionsreifer Edge-AI-Anwendungen**
>
> Beherrschen Sie die lokale KI-Bereitstellung mit Microsoft Foundry Local – von der ersten Chat-Komplettierung bis zur Multi-Agenten-Orchestrierung in 6 aufeinander aufbauenden Sitzungen.

---

## 🎯 Einführung

Willkommen zum **EdgeAI für Einsteiger Workshop** – Ihrem praktischen Leitfaden für die Entwicklung intelligenter Anwendungen, die vollständig auf lokaler Hardware laufen. Dieser Workshop verwandelt theoretische Edge-AI-Konzepte in praktische Fähigkeiten durch zunehmend anspruchsvollere Übungen mit Microsoft Foundry Local und Small Language Models (SLMs).

### Warum dieser Workshop?

**Die Edge-AI-Revolution ist da**

Weltweit wechseln Organisationen von cloudbasierter KI zu Edge Computing aus drei entscheidenden Gründen:

1. **Datenschutz & Compliance** – Verarbeitung sensibler Daten lokal ohne Übertragung in die Cloud (HIPAA, DSGVO, Finanzvorschriften)
2. **Leistung** – Eliminierung von Netzwerklatenz (50-500ms lokal vs. 500-2000ms Cloud-Roundtrip)
3. **Kostenkontrolle** – Wegfall von API-Kosten pro Token und Skalierung ohne Cloud-Ausgaben

**Aber Edge AI ist anders**

Die Ausführung von KI vor Ort erfordert neue Fähigkeiten:
- Modellwahl und Optimierung für ressourcenbeschränkte Umgebungen
- Verwaltung lokaler Dienste und Hardwarebeschleunigung
- Prompt-Engineering für kleinere Modelle
- Produktionsbereitstellungsmuster für Edge-Geräte

**Dieser Workshop vermittelt diese Fähigkeiten**

In 6 fokussierten Sitzungen (~3 Stunden insgesamt) entwickeln Sie sich von "Hello World" bis zur Bereitstellung produktionsreifer Multi-Agenten-Systeme – alles läuft lokal auf Ihrem Rechner.

---

## 📚 Lernziele

Nach Abschluss dieses Workshops können Sie:

### Kernkompetenzen
1. **Lokale KI-Dienste bereitstellen und verwalten**
   - Microsoft Foundry Local installieren und konfigurieren
   - Geeignete Modelle für Edge-Bereitstellungen auswählen
   - Modelllebenszyklus verwalten (herunterladen, laden, zwischenspeichern)
   - Ressourcenverbrauch überwachen und Leistung optimieren

2. **KI-gestützte Anwendungen entwickeln**
   - OpenAI-kompatible Chat-Komplettierungen lokal implementieren
   - Effektive Prompts für Small Language Models entwerfen
   - Streaming-Antworten für eine bessere Benutzererfahrung handhaben
   - Lokale Modelle in bestehende Anwendungen integrieren

3. **RAG-Systeme (Retrieval Augmented Generation) erstellen**
   - Semantische Suche mit Embeddings aufbauen
   - LLM-Antworten in domänenspezifisches Wissen einbetten
   - RAG-Qualität mit branchenüblichen Metriken bewerten
   - Skalierung vom Prototyp zur Produktion

4. **Modellleistung optimieren**
   - Mehrere Modelle für Ihren Anwendungsfall benchmarken
   - Latenz, Durchsatz und Zeit bis zum ersten Token messen
   - Optimale Modelle basierend auf Geschwindigkeits-/Qualitätskompromissen auswählen
   - SLM- vs. LLM-Abwägungen in realen Szenarien vergleichen

5. **Multi-Agenten-Systeme orchestrieren**
   - Spezialisierte Agenten für verschiedene Aufgaben entwerfen
   - Agentenspeicher und Kontextmanagement implementieren
   - Agenten in komplexen Workflows koordinieren
   - Anfragen intelligent über mehrere Modelle routen

6. **Produktionsreife Lösungen bereitstellen**
   - Fehlerbehandlung und Wiederholungslogik implementieren
   - Token-Nutzung und Systemressourcen überwachen
   - Skalierbare Architekturen mit Modell-als-Tool-Mustern erstellen
   - Migrationspfade von Edge zu Hybrid (Edge + Cloud) planen

---

## 🎓 Lernergebnisse

### Was Sie erstellen werden

Am Ende dieses Workshops haben Sie Folgendes entwickelt:

| Sitzung | Ergebnis | Demonstrierte Fähigkeiten |
|---------|----------|---------------------------|
| **1** | Chat-Anwendung mit Streaming | Dienst-Setup, grundlegende Komplettierungen, Streaming-UX |
| **2** | RAG-System mit Bewertung | Embeddings, semantische Suche, Qualitätsmetriken |
| **3** | Multi-Modell-Benchmark-Suite | Leistungsbewertung, Modellvergleich |
| **4** | SLM- vs. LLM-Vergleich | Abwägungsanalyse, Optimierungsstrategien |
| **5** | Multi-Agenten-Orchestrator | Agentendesign, Speicherverwaltung, Koordination |
| **6** | Intelligentes Routingsystem | Intent-Erkennung, Modellauswahl, Skalierbarkeit |

### Kompetenzmatrix

| Fähigkeitsniveau | Sitzung 1-2 | Sitzung 3-4 | Sitzung 5-6 |
|------------------|-------------|-------------|-------------|
| **Anfänger** | ✅ Setup & Grundlagen | ⚠️ Herausfordernd | ❌ Zu fortgeschritten |
| **Fortgeschritten** | ✅ Schnelle Überprüfung | ✅ Kernlernen | ⚠️ Stretch-Ziele |
| **Experte** | ✅ Leicht zu bewältigen | ✅ Verfeinerung | ✅ Produktionsmuster |

### Karrierefähigkeiten

**Nach diesem Workshop sind Sie bereit:**

✅ **Datenschutzorientierte Anwendungen zu entwickeln**
- Gesundheitsanwendungen, die PHI/PII lokal verarbeiten
- Finanzdienstleistungen mit Compliance-Anforderungen
- Regierungssysteme mit Anforderungen an Datenhoheit

✅ **Für Edge-Umgebungen zu optimieren**
- IoT-Geräte mit begrenzten Ressourcen
- Offline-fokussierte mobile Anwendungen
- Echtzeitsysteme mit niedriger Latenz

✅ **Intelligente Architekturen zu entwerfen**
- Multi-Agenten-Systeme für komplexe Workflows
- Hybride Edge-Cloud-Bereitstellungen
- Kostenoptimierte KI-Infrastruktur

✅ **Edge-AI-Initiativen zu leiten**
- Machbarkeit von Edge-AI für Projekte bewerten
- Geeignete Modelle und Frameworks auswählen
- Skalierbare lokale KI-Lösungen entwerfen

---

## 🗺️ Workshop-Struktur

### Sitzungsübersicht (6 Sitzungen × 30 Minuten = 3 Stunden)

| Sitzung | Thema | Fokus | Dauer |
|---------|-------|-------|-------|
| **1** | Einstieg mit Foundry Local | Installation, Validierung, erste Komplettierungen | 30 min |
| **2** | KI-Lösungen mit RAG erstellen | Prompt-Engineering, Embeddings, Bewertung | 30 min |
| **3** | Open-Source-Modelle | Modellentdeckung, Benchmarking, Auswahl | 30 min |
| **4** | Cutting-Edge-Modelle | SLM vs. LLM, Optimierung, Frameworks | 30 min |
| **5** | KI-gestützte Agenten | Agentendesign, Orchestrierung, Speicher | 30 min |
| **6** | Modelle als Werkzeuge | Routing, Verkettung, Skalierungsstrategien | 30 min |

---

## 🚀 Schnellstart

### Voraussetzungen

**Systemanforderungen:**
- **OS**: Windows 10/11, macOS 11+ oder Linux (Ubuntu 20.04+)
- **RAM**: Mindestens 8GB, empfohlen 16GB+
- **Speicherplatz**: Mindestens 10GB freier Speicherplatz für Modelle
- **CPU**: Moderner Prozessor mit AVX2-Unterstützung
- **GPU** (optional): CUDA-kompatibel oder Qualcomm NPU für Beschleunigung

**Softwareanforderungen:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installationsanleitung](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (empfohlen) ([Download](https://code.visualstudio.com/))

### Einrichtung in 3 Schritten

#### 1. Foundry Local installieren

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installation überprüfen:**
```bash
foundry --version
foundry service status
```

#### 2. Repository klonen & Abhängigkeiten installieren

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Erstes Beispiel ausführen

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Erfolg!** Sie sollten eine Streaming-Antwort zu Edge-AI sehen.

---

## 📦 Workshop-Ressourcen

### Python-Beispiele

Praktische Beispiele, die jedes Konzept demonstrieren:

| Sitzung | Beispiel | Beschreibung | Laufzeit |
|---------|----------|--------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Basis- & Streaming-Chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG mit Embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG-Qualitätsbewertung | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-Modell-Benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM- vs. LLM-Vergleich | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-Agenten-System | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-basiertes Routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-Step-Pipeline | ~60s |

### Jupyter-Notebooks

Interaktive Erkundung mit Erklärungen und Visualisierungen:

| Sitzung | Notebook | Beschreibung | Schwierigkeitsgrad |
|---------|----------|--------------|--------------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat-Grundlagen & Streaming | ⭐ Anfänger |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG-System erstellen | ⭐⭐ Fortgeschritten |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG-Qualität bewerten | ⭐⭐ Fortgeschritten |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modell-Benchmarking | ⭐⭐ Fortgeschritten |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modellvergleich | ⭐⭐ Fortgeschritten |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agenten-Orchestrierung | ⭐⭐⭐ Experte |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent-Routing | ⭐⭐⭐ Experte |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline-Orchestrierung | ⭐⭐⭐ Experte |

### Dokumentation

Umfassende Anleitungen und Referenzen:

| Dokument | Beschreibung | Wann verwenden |
|----------|--------------|----------------|
| [QUICK_START.md](./QUICK_START.md) | Schnellstart-Anleitung | Von Grund auf beginnen |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Befehls- & API-Spickzettel | Schnelle Antworten benötigen |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK-Muster & Beispiele | Code schreiben |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Anleitung zu Umgebungsvariablen | Beispiele konfigurieren |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Neueste Verbesserungen der Beispiele | Änderungen verstehen |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migrationsanleitung | Code aktualisieren |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Häufige Probleme & Lösungen | Probleme beheben |

---

## 🎓 Empfehlungen für den Lernpfad

### Für Anfänger (3-4 Stunden)
1. ✅ Sitzung 1: Einstieg (Fokus auf Setup und grundlegenden Chat)
2. ✅ Sitzung 2: RAG-Grundlagen (Bewertung zunächst überspringen)
3. ✅ Sitzung 3: Einfaches Benchmarking (nur 2 Modelle)
4. ⏭️ Sitzungen 4-6 vorerst überspringen
5. 🔄 Zu Sitzungen 4-6 zurückkehren, nachdem die erste Anwendung erstellt wurde

### Für fortgeschrittene Entwickler (3 Stunden)
1. ⚡ Sitzung 1: Schnelle Setup-Validierung
2. ✅ Sitzung 2: Vollständige RAG-Pipeline mit Bewertung
3. ✅ Sitzung 3: Vollständige Benchmarking-Suite
4. ✅ Sitzung 4: Modelloptimierung
5. ✅ Sitzungen 5-6: Fokus auf Architekturmustern

### Für Experten (2-3 Stunden)
1. ⚡ Sitzungen 1-3: Schnelle Überprüfung und Validierung
2. ✅ Sitzung 4: Optimierung im Detail
3. ✅ Sitzung 5: Multi-Agenten-Architektur
4. ✅ Sitzung 6: Produktionsmuster und Skalierung
5. 🚀 Erweiterung: Eigene Routing-Logik und hybride Bereitstellungen erstellen

---

## Workshop-Sitzungspaket (Fokussierte 30‑Minuten-Labs)

Wenn Sie dem kompakten 6-Sitzungs-Workshop-Format folgen, verwenden Sie diese speziellen Anleitungen (jede ergänzt die umfassenderen Moduldokumente oben):

| Workshop-Sitzung | Anleitung | Kernfokus |
|------------------|-----------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installation, Validierung, Ausführung von phi & GPT-OSS-20B, Beschleunigung |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt-Engineering, RAG-Muster, CSV- & Dokumenten-Einbettung, Migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face-Integration, Benchmarking, Modellauswahl |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs. LLM, WebGPU, Chainlit RAG, ONNX-Beschleunigung |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agentenrollen, Speicher, Werkzeuge, Orchestrierung |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, Verkettung, Skalierungspfad zu Azure |
Jede Sitzungsdatei enthält: Abstract, Lernziele, 30‑minütigen Demo-Ablauf, Starterprojekt, Validierungs-Checkliste, Fehlerbehebung und Verweise auf das offizielle Foundry Local Python SDK.

### Beispielskripte

Workshop-Abhängigkeiten installieren (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Falls der Foundry Local-Dienst auf einem anderen (Windows-)Rechner oder einer VM von macOS aus ausgeführt wird, exportieren Sie den Endpunkt:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sitzung | Skript(e) | Beschreibung |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap-Dienst & Streaming-Chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimaler RAG (In-Memory-Embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-Auswertung mit Ragas-Metriken |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-Modell-Latenz- & Durchsatz-Benchmarking |
| 4 | `samples/session04/model_compare.py` | Vergleich SLM vs LLM (Latenz & Beispielausgabe) |
| 5 | `samples/session05/agents_orchestrator.py` | Zwei-Agenten-Forschungs- → Redaktionspipeline |
| 6 | `samples/session06/models_router.py` | Intent-basierte Routing-Demo |
|   | `samples/session06/models_pipeline.py` | Multi-Step-Plan/Execute/Refine-Kette |

### Umgebungsvariablen (Gemeinsam für alle Beispiele)

| Variable | Zweck | Beispiel |
|----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standardalias für ein einzelnes Modell bei einfachen Beispielen | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explizites SLM vs größeres Modell für Vergleich | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Kommagetrennte Liste von Aliases für Benchmarking | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark-Wiederholungen pro Modell | `3` |
| `BENCH_PROMPT` | Eingabeaufforderung für Benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-Transformers-Embedding-Modell | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Überschreibt Testabfrage für RAG-Pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Überschreibt Abfrage für Agenten-Pipeline | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Modellalias für Forschungsagenten | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Modellalias für Redaktionsagenten (kann unterschiedlich sein) | `gpt-oss-20b` |
| `SHOW_USAGE` | Bei `1` wird die Token-Nutzung pro Abschluss angezeigt | `1` |
| `RETRY_ON_FAIL` | Bei `1` wird bei vorübergehenden Chat-Fehlern einmal erneut versucht | `1` |
| `RETRY_BACKOFF` | Sekunden, die vor erneutem Versuch gewartet werden | `1.0` |

Falls eine Variable nicht gesetzt ist, greifen die Skripte auf sinnvolle Standardwerte zurück. Für Demos mit einem einzigen Modell benötigen Sie normalerweise nur `FOUNDRY_LOCAL_ALIAS`.

### Hilfsmodul

Alle Beispiele teilen sich jetzt ein Hilfsmodul `samples/workshop_utils.py`, das Folgendes bietet:

* Zwischengespeicherte Erstellung von `FoundryLocalManager` + OpenAI-Client
* `chat_once()`-Hilfsfunktion mit optionalem erneuten Versuch + Nutzungsanzeige
* Einfache Token-Nutzungsberichte (aktivieren mit `SHOW_USAGE=1`)

Dies reduziert Duplikationen und hebt Best Practices für effiziente lokale Modellorchestrierung hervor.

## Optionale Verbesserungen (Sitzungsübergreifend)

| Thema | Verbesserung | Sitzungen | Env / Umschalter |
|-------|-------------|----------|------------------|
| Determinismus | Feste Temperatur + stabile Eingabeaufforderungen | 1–6 | Setzen Sie `temperature=0`, `top_p=1` |
| Token-Nutzungsanzeige | Konsistente Kosten-/Effizienzvermittlung | 1–6 | `SHOW_USAGE=1` |
| Streaming des ersten Tokens | Wahrgenommene Latenzmetrik | 1,3,4,6 | `BENCH_STREAM=1` (Benchmark) |
| Wiederholungsresilienz | Handhabt vorübergehende Kaltstarts | Alle | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Modell-Agenten | Heterogene Rollenspezialisierung | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptives Routing | Intent- + Kostenheuristiken | 6 | Router mit Eskalationslogik erweitern |
| Vektorspeicher | Langfristiges semantisches Erinnern | 2,5,6 | FAISS/Chroma-Embedding-Index integrieren |
| Trace-Export | Auditierung & Auswertung | 2,5,6 | JSON-Zeilen pro Schritt anhängen |
| Qualitätsrubriken | Qualitative Nachverfolgung | 3–6 | Sekundäre Bewertungsaufforderungen |
| Smoke-Tests | Schnelle Validierung vor Workshop | Alle | `python Workshop/tests/smoke.py` |

### Deterministischer Schnellstart

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Erwarten Sie stabile Token-Zahlen bei wiederholten identischen Eingaben.

### RAG-Auswertung (Sitzung 2)

Verwenden Sie `rag_eval_ragas.py`, um Antwortrelevanz, Glaubwürdigkeit und Kontextpräzision auf einem kleinen synthetischen Datensatz zu berechnen:

```powershell
python samples/session02/rag_eval_ragas.py
```

Erweitern Sie dies, indem Sie eine größere JSONL-Datei mit Fragen, Kontexten und Ground Truths bereitstellen und diese dann in ein Hugging Face `Dataset` umwandeln.

## CLI-Befehlsgenauigkeitsanhang

Der Workshop verwendet absichtlich nur derzeit dokumentierte / stabile Foundry Local CLI-Befehle.

### Referenzierte stabile Befehle

| Kategorie | Befehl | Zweck |
|-----------|--------|-------|
| Kern | `foundry --version` | Installierte Version anzeigen |
| Kern | `foundry init` | Konfiguration initialisieren |
| Dienst | `foundry service start` | Lokalen Dienst starten (falls nicht automatisch) |
| Dienst | `foundry status` | Dienststatus anzeigen |
| Modelle | `foundry model list` | Katalog / verfügbare Modelle auflisten |
| Modelle | `foundry model download <alias>` | Modellgewichte in den Cache herunterladen |
| Modelle | `foundry model run <alias>` | Modell lokal starten (laden); mit `--prompt` für Einmalaufforderung kombinieren |
| Modelle | `foundry model unload <alias>` / `foundry model stop <alias>` | Modell aus dem Speicher entladen (falls unterstützt) |
| Cache | `foundry cache list` | Zwischengespeicherte (heruntergeladene) Modelle auflisten |
| System | `foundry system info` | Snapshot der Hardware- & Beschleunigungsfähigkeiten |
| System | `foundry system gpu-info` | GPU-Diagnoseinformationen |
| Konfiguration | `foundry config list` | Aktuelle Konfigurationswerte anzeigen |
| Konfiguration | `foundry config set <key> <value>` | Konfiguration aktualisieren |

### Einmalaufforderungsmuster

Anstelle eines veralteten `model chat`-Unterbefehls verwenden Sie:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Dies führt einen einzigen Eingabe-/Antwortzyklus aus und beendet dann.

### Entfernte / Vermeidete Muster

| Veraltet / Undokumentiert | Ersatz / Anleitung |
|---------------------------|--------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Verwenden Sie einfach `foundry model list` + letzte Aktivität / Protokolle |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Verwenden Sie das Benchmark-Python-Skript + OS-Tools (Task-Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latenz, p95, Tokens/Sek.: `samples/session03/benchmark_oss_models.py`
- Erste-Token-Latenz (Streaming): Setzen Sie `BENCH_STREAM=1`
- Ressourcennutzung: OS-Monitore (Task-Manager, Aktivitätsmonitor, `nvidia-smi`) + `foundry system info`.

Sobald neue CLI-Telemetrie-Befehle stabilisiert sind, können sie mit minimalen Änderungen in die Sitzungs-Markdowns integriert werden.

### Automatisierter Lint-Schutz

Ein automatisierter Linter verhindert die Wiedereinführung veralteter CLI-Muster innerhalb von Codeblöcken in Markdown-Dateien:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Veraltete Muster werden innerhalb von Codeblöcken blockiert.

Empfohlene Ersatzmuster:
| Veraltet | Ersatz |
|----------|--------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark-Skript + Systemtools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Lokal ausführen:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` wird bei jedem Push & PR ausgeführt.

Optionaler Pre-Commit-Hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Schnelle CLI → SDK-Migrationstabelle

| Aufgabe | CLI-Einzeiler | SDK (Python) Äquivalent | Hinweise |
|---------|---------------|-------------------------|---------|
| Modell einmal ausführen (Eingabeaufforderung) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK startet Dienst & Caching automatisch |
| Modell herunterladen (Cache) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # löst Download/Laden aus` | Manager wählt die beste Variante, falls Alias mehreren Builds zugeordnet ist |
| Katalog auflisten | `foundry model list` | `# verwenden Sie Manager für jeden Alias oder pflegen Sie eine bekannte Liste` | CLI aggregiert; SDK derzeit pro Alias-Initialisierung |
| Zwischengespeicherte Modelle auflisten | `foundry cache list` | `manager.list_cached_models()` | Nach Manager-Initialisierung (beliebiger Alias) |
| GPU-Beschleunigung aktivieren | `foundry config set compute.onnx.enable_gpu true` | `# CLI-Aktion; SDK geht davon aus, dass Konfiguration bereits angewendet wurde` | Konfiguration ist externer Nebeneffekt |
| Endpunkt-URL abrufen | (implizit) | `manager.endpoint` | Wird verwendet, um OpenAI-kompatiblen Client zu erstellen |
| Modell aufwärmen | `foundry model run <alias>` dann erste Eingabeaufforderung | `chat_once(alias, messages=[...])` (Hilfsfunktion) | Hilfsfunktionen handhaben anfängliche Kaltstartlatenz |
| Latenz messen | `python benchmark_oss_models.py` | `import benchmark_oss_models` (oder neues Exportskript) | Skript bevorzugen für konsistente Metriken |
| Modell stoppen / entladen | `foundry model unload <alias>` | (Nicht verfügbar – Dienst / Prozess neu starten) | Normalerweise nicht erforderlich für Workshop-Ablauf |
| Token-Nutzung abrufen | (Ausgabe anzeigen) | `resp.usage.total_tokens` | Wird bereitgestellt, falls Backend Nutzungsobjekt zurückgibt |

## Benchmark-Markdown-Export

Verwenden Sie das Skript `Workshop/scripts/export_benchmark_markdown.py`, um einen frischen Benchmark auszuführen (gleiche Logik wie `samples/session03/benchmark_oss_models.py`) und eine GitHub-freundliche Markdown-Tabelle plus rohes JSON zu erstellen.

### Beispiel

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Erstellte Dateien:
| Datei | Inhalt |
|-------|--------|
| `benchmark_report.md` | Markdown-Tabelle + Interpretationshinweise |
| `benchmark_report.json` | Rohdaten-Metrikarray (für Diffing / Trendverfolgung) |

Setzen Sie `BENCH_STREAM=1` in der Umgebung, um die Latenz des ersten Tokens einzuschließen, falls unterstützt.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.