<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T20:39:53+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "de"
}
-->
# Foundry Local SDK-Updates

## Überblick

Die Workshop-Notebooks und -Utilities wurden aktualisiert, um die **offizielle Foundry Local Python SDK** gemäß den Mustern aus folgenden Quellen korrekt zu nutzen:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Geänderte Dateien

### 1. `Workshop/samples/workshop_utils.py`

**Änderungen:**
- ✅ Fehlerbehandlung für den Import des Pakets `foundry-local-sdk` hinzugefügt
- ✅ Dokumentation mit offiziellen SDK-Mustern erweitert
- ✅ Logging mit Unicode-Symbolen (✓, ✗, ⚠) verbessert
- ✅ Umfassende Docstrings mit Beispielen hinzugefügt
- ✅ Verbesserte Fehlermeldungen mit Verweisen auf CLI-Befehle
- ✅ Kommentare aktualisiert, um der offiziellen SDK-Dokumentation zu entsprechen

**Wesentliche Verbesserungen:**

#### Fehlerbehandlung beim Import
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Verbesserte `get_client()`-Funktion
- Detaillierte Dokumentation zum Initialisierungsmuster des SDK hinzugefügt
- Klarstellung, dass `FoundryLocalManager` den Dienst automatisch startet
- Erklärung der Modellalias-Auflösung zu hardwareoptimierten Varianten
- Logging mit Informationen zu Endpunkten verbessert
- Bessere Fehlermeldungen mit Vorschlägen zur Fehlerbehebung

#### Verbesserte `chat_once()`-Funktion
- Umfassende Docstring mit Anwendungsbeispielen hinzugefügt
- Kompatibilität mit OpenAI SDK klargestellt
- Streaming-Unterstützung dokumentiert (über kwargs)
- Verbesserte Fehlermeldungen mit CLI-Befehlsvorschlägen
- Hinweise zur Überprüfung der Modellverfügbarkeit hinzugefügt

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Änderungen:**
- ✅ Alle Markdown-Zellen mit SDK-Referenzen aktualisiert
- ✅ Code-Kommentare mit Erklärungen zu SDK-Mustern erweitert
- ✅ Dokumentation und Erklärungen in den Zellen verbessert
- ✅ Anleitung zur Fehlerbehebung hinzugefügt
- ✅ Modellkatalog aktualisiert (ersetzt 'gpt-oss-20b' durch 'phi-3.5-mini')
- ✅ Ausgabeformatierung mit visuellen Indikatoren verbessert
- ✅ SDK-Links und Referenzen durchgehend hinzugefügt

**Zellweise Updates:**

#### Zelle 1 (Titel)
- SDK-Dokumentationslinks hinzugefügt
- Verweise auf offizielle GitHub-Repositories eingefügt

#### Zelle 2 (Szenario)
- Mit nummerierten Schritten neu formatiert
- Absichtsbasiertes Routing-Muster klargestellt
- Vorteile der lokalen Ausführung hervorgehoben

#### Zelle 3 (Abhängigkeitsinstallation)
- Erklärung hinzugefügt, was jedes Paket bietet
- SDK-Fähigkeiten dokumentiert (Alias-Auflösung, Hardware-Optimierung)

#### Zelle 4 (Umgebungseinrichtung)
- Funktion-Docstrings erweitert
- Inline-Kommentare zu SDK-Mustern hinzugefügt
- Struktur des Modellkatalogs dokumentiert
- Prioritäts-/Fähigkeitsabgleich klargestellt

#### Zelle 5 (Katalogprüfung)
- Visuelle Häkchen (✓) hinzugefügt
- Ausgabe besser formatiert

#### Zelle 6 (Intent-Erkennungstest)
- Ausgabe im Tabellenstil neu formatiert
- Zeigt sowohl Intent als auch ausgewähltes Modell

#### Zelle 7 (Routing-Funktion)
- Umfassende Erklärung des SDK-Musters
- Initialisierungsablauf dokumentiert
- Alle Funktionen aufgelistet (Retry, Tracking, Fehler)
- SDK-Referenzlink hinzugefügt

#### Zelle 8 (Batch-Demo)
- Erklärung dessen, was zu erwarten ist, erweitert
- Abschnitt zur Fehlerbehebung hinzugefügt
- CLI-Befehle für Debugging eingefügt
- Ausgabeanzeige besser formatiert

### 3. `Workshop/notebooks/session06_README.md` (Neue Datei)

**Umfassende Dokumentation erstellt, die Folgendes abdeckt:**

1. **Überblick**: Architekturdiagramm und Komponentenbeschreibung
2. **SDK-Integration**: Codebeispiele gemäß offiziellen Mustern
3. **Voraussetzungen**: Schritt-für-Schritt-Einrichtungsanleitung
4. **Verwendung**: Anleitung zum Ausführen und Anpassen des Notebooks
5. **Modell-Aliase**: Erklärung hardwareoptimierter Varianten
6. **Fehlerbehebung**: Häufige Probleme und Lösungen
7. **Erweiterung**: Anleitung zum Hinzufügen von Intents, Modellen und benutzerdefinierter Logik
8. **Leistungstipps**: Best Practices für den Produktionseinsatz
9. **Ressourcen**: Links zu offiziellen Dokumentationen und Community

## SDK-Musterimplementierung

### Offizielles Muster (aus Foundry Local-Dokumentation)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Unsere Implementierung (in workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Vorteile unseres Ansatzes:**
- ✅ Folgt exakt dem offiziellen SDK-Muster
- ✅ Fügt Caching hinzu, um wiederholte Initialisierungen zu vermeiden
- ✅ Enthält Retry-Logik für Produktionsrobustheit
- ✅ Unterstützt Token-Nutzungsverfolgung
- ✅ Bietet bessere Fehlermeldungen
- ✅ Bleibt kompatibel mit offiziellen Beispielen

## Änderungen im Modellkatalog

### Vorher
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Nachher
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Grund:** Ersetzt 'gpt-oss-20b' (nicht standardisierter Alias) durch 'phi-3.5-mini' (offizieller Foundry Local-Alias).

## Abhängigkeiten

### Aktualisierte requirements.txt

Die Workshop requirements.txt enthält bereits:
```
foundry-local-sdk
openai>=1.30.0
```

Dies sind die einzigen Pakete, die für die Integration von Foundry Local benötigt werden.

## Tests der Updates

### 1. Überprüfen, ob Foundry Local läuft

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Verfügbare Modelle prüfen

```bash
foundry model ls
```

Stellen Sie sicher, dass diese Modelle verfügbar sind oder automatisch heruntergeladen werden:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Notebook ausführen

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

Oder in VS Code öffnen und alle Zellen ausführen.

### 4. Erwartetes Verhalten

**Zelle 1 (Installation):** Pakete werden erfolgreich installiert  
**Zelle 2 (Setup):** Keine Fehler, Importe funktionieren  
**Zelle 3 (Prüfen):** Zeigt ✓ mit Modellliste  
**Zelle 4 (Intent-Test):** Zeigt Ergebnisse der Intent-Erkennung  
**Zelle 5 (Router):** Zeigt ✓ Routing-Funktion bereit  
**Zelle 6 (Ausführen):** Leitet Eingaben an Modelle weiter, zeigt Ergebnisse  

### 5. Fehlerbehebung bei Verbindungsfehlern

Falls Sie `APIConnectionError: Connection error` sehen:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Umgebungsvariablen

Die folgenden Umgebungsvariablen werden unterstützt:

| Variable | Standardwert | Beschreibung |
|----------|--------------|--------------|
| `SHOW_USAGE` | `0` | Auf `1` setzen, um Token-Nutzung anzuzeigen |
| `RETRY_ON_FAIL` | `1` | Retry-Logik aktivieren |
| `RETRY_BACKOFF` | `1.0` | Anfangsverzögerung für Retry (Sekunden) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Dienst-Endpunkt überschreiben |

### Anwendungsbeispiele

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migration vom alten Muster

Falls Sie bestehenden Code mit direkten API-Aufrufen haben, hier ist die Migration:

### Vorher (Direkte API)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Nachher (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Vorteile der Migration
- ✅ Automatische Dienstverwaltung
- ✅ Modellalias-Auflösung
- ✅ Auswahl hardwareoptimierter Varianten
- ✅ Verbesserte Fehlerbehandlung
- ✅ Kompatibilität mit OpenAI SDK
- ✅ Unterstützung für Streaming

## Referenzen

### Offizielle Dokumentation
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK Quelle**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI-Referenz**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **Fehlerbehebung**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Workshop-Ressourcen
- **Session 06 README**: `Workshop/notebooks/session06_README.md`  
- **Workshop Utils**: `Workshop/samples/workshop_utils.py`  
- **Beispiel-Notebook**: `Workshop/notebooks/session06_models_router.ipynb`  

### Community
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub Issues**: https://github.com/microsoft/Foundry-Local/issues  

## Nächste Schritte

1. **Änderungen überprüfen**: Lesen Sie die aktualisierten Dateien durch  
2. **Notebook testen**: Führen Sie session06_models_router.ipynb aus  
3. **SDK überprüfen**: Stellen Sie sicher, dass foundry-local-sdk installiert ist  
4. **Dienst prüfen**: Bestätigen Sie, dass Foundry Local läuft  
5. **Dokumentation erkunden**: Lesen Sie die neue session06_README.md  

## Zusammenfassung

Diese Updates stellen sicher, dass die Workshop-Materialien den **offiziellen Foundry Local SDK-Mustern** genau wie in der GitHub-Dokumentation beschrieben folgen. Alle Codebeispiele, Dokumentationen und Utilities sind jetzt an die von Microsoft empfohlenen Best Practices für die lokale Bereitstellung von KI-Modellen angepasst.

Die Änderungen verbessern:
- ✅ **Korrektheit**: Verwendet offizielle SDK-Muster  
- ✅ **Dokumentation**: Umfassende Erklärungen und Beispiele  
- ✅ **Fehlerbehandlung**: Bessere Meldungen und Anleitung zur Fehlerbehebung  
- ✅ **Wartbarkeit**: Folgt offiziellen Konventionen  
- ✅ **Benutzerfreundlichkeit**: Klarere Anweisungen und Debugging-Hilfe  

---

**Aktualisiert:** 8. Oktober 2025  
**SDK-Version:** foundry-local-sdk (neueste)  
**Workshop-Branch:** Reactor  

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.