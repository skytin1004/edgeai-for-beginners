<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec281a7cf06deda1f29140a2959ef0d2",
  "translation_date": "2025-10-09T16:59:20+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "nl"
}
-->
# Foundry Local SDK Migratienotities

## Overzicht

Alle Python-bestanden in de Workshop-map zijn bijgewerkt om te voldoen aan de nieuwste patronen van de officiële [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Samenvatting van Wijzigingen

### Kerninfrastructuur (`workshop_utils.py`)

#### Verbeterde Functies:
- **Ondersteuning voor Endpoint Override**: Toevoeging van ondersteuning voor de omgevingsvariabele `FOUNDRY_LOCAL_ENDPOINT`
- **Verbeterde Foutafhandeling**: Betere uitzonderingafhandeling met gedetailleerde foutmeldingen
- **Verbeterde Caching**: Cache-sleutels bevatten nu de endpoint voor scenario's met meerdere endpoints
- **Exponentiële Backoff**: Retry-logica maakt nu gebruik van exponentiële backoff voor betere betrouwbaarheid
- **Type Annotaties**: Uitgebreide type hints toegevoegd voor betere ondersteuning in IDE's

#### Nieuwe Mogelijkheden:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Voorbeeldtoepassingen

#### Sessie 01: Chat Bootstrap (`chat_bootstrap.py`)
- Standaardmodel bijgewerkt van `phi-3.5-mini` naar `phi-4-mini`
- Ondersteuning voor endpoint override toegevoegd
- Documentatie verbeterd met SDK-referenties

#### Sessie 02: RAG Pipeline (`rag_pipeline.py`)
- Bijgewerkt om `phi-4-mini` als standaard te gebruiken
- Ondersteuning voor endpoint override toegevoegd
- Documentatie verbeterd met details over omgevingsvariabelen

#### Sessie 02: RAG Evaluatie (`rag_eval_ragas.py`)
- Standaardmodellen bijgewerkt
- Endpointconfiguratie toegevoegd
- Foutafhandeling verbeterd

#### Sessie 03: Benchmarking (`benchmark_oss_models.py`)
- Standaardmodellijst bijgewerkt om `phi-4-mini` op te nemen
- Uitgebreide documentatie over omgevingsvariabelen toegevoegd
- Functiedocumentatie verbeterd
- Ondersteuning voor endpoint override toegevoegd

#### Sessie 04: Modelvergelijking (`model_compare.py`)
- Standaard LLM bijgewerkt van `gpt-oss-20b` naar `qwen2.5-7b`
- Endpointconfiguratie toegevoegd
- Documentatie verbeterd

#### Sessie 05: Multi-Agent Orchestratie (`agents_orchestrator.py`)
- Type hints toegevoegd (veranderd van `str | None` naar `Optional[str]`)
- Documentatie van de Agent-klasse verbeterd
- Ondersteuning voor endpoint override toegevoegd
- Initialisatiepatroon verbeterd

#### Sessie 06: Modelroutering (`models_router.py`)
- Endpointconfiguratie toegevoegd
- Documentatie over intentiedetectie verbeterd
- Documentatie over routeringslogica verbeterd

#### Sessie 06: Pipeline (`models_pipeline.py`)
- Uitgebreide functiedocumentatie toegevoegd
- Stapsgewijze documentatie verbeterd
- Foutafhandeling verbeterd

### Scripts

#### Benchmark Export (`export_benchmark_markdown.py`)
- Ondersteuning voor endpoint override toegevoegd
- Standaardmodellen bijgewerkt
- Functiedocumentatie verbeterd
- Foutafhandeling verbeterd

#### CLI Linter (`lint_markdown_cli.py`)
- SDK-referentielinks toegevoegd
- Gebruiksdocumentatie verbeterd

### Tests

#### Smoke Tests (`smoke.py`)
- Ondersteuning voor endpoint override toegevoegd
- Documentatie verbeterd
- Documentatie van testcases verbeterd
- Betere foutmeldingen

## Omgevingsvariabelen

Alle voorbeelden ondersteunen nu deze omgevingsvariabelen:

### Kernconfiguratie
- `FOUNDRY_LOCAL_ALIAS` - Modelalias om te gebruiken (standaard verschilt per voorbeeld)
- `FOUNDRY_LOCAL_ENDPOINT` - Service-endpoint overschrijven (optioneel)
- `SHOW_USAGE` - Statistieken over tokengebruik tonen (standaard: "0")
- `RETRY_ON_FAIL` - Retry-logica inschakelen (standaard: "1")
- `RETRY_BACKOFF` - Initiële retry-vertraging in seconden (standaard: "1.0")

### Specifiek voor Voorbeelden
- `EMBED_MODEL` - Embeddingmodel voor RAG-voorbeelden
- `BENCH_MODELS` - Komma-gescheiden modellen voor benchmarking
- `BENCH_ROUNDS` - Aantal benchmarkrondes
- `BENCH_PROMPT` - Testprompt voor benchmarks
- `BENCH_STREAM` - Latentie van eerste token meten
- `RAG_QUESTION` - Testvraag voor RAG-voorbeelden
- `AGENT_MODEL_PRIMARY` - Primair agentmodel
- `AGENT_MODEL_EDITOR` - Editor-agentmodel
- `SLM_ALIAS` - Alias voor klein taalmodel
- `LLM_ALIAS` - Alias voor groot taalmodel

## Geïmplementeerde SDK Best Practices

### 1. Correcte Clientinitialisatie
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Modelinformatie Opvragen
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Foutafhandeling
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Retry-logica met Exponentiële Backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Ondersteuning voor Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Migratiehandleiding voor Aangepaste Voorbeelden

Als je nieuwe voorbeelden maakt of bestaande bijwerkt:

1. **Gebruik `workshop_utils.py` helpers**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Ondersteun endpoint override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Voeg uitgebreide documentatie toe**:
   - Omgevingsvariabelen in docstring
   - SDK-referentielink
   - Gebruiksvoorbeelden

4. **Gebruik type hints**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementeer correcte foutafhandeling**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testen

Alle voorbeelden kunnen worden getest met:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
python Workshop/samples/session01/chat_bootstrap.py "Test question"
python Workshop/samples/session02/rag_pipeline.py

# Run benchmark
python Workshop/samples/session03/benchmark_oss_models.py

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK Documentatiereferenties

- **Hoofdrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Documentatie**: Raadpleeg de SDK-repository voor de nieuwste API-documentatie

## Brekende Wijzigingen

### Geen Verwacht
Alle wijzigingen zijn achterwaarts compatibel. De updates voegen voornamelijk toe:
- Nieuwe optionele functies (endpoint override)
- Verbeterde foutafhandeling
- Verbeterde documentatie
- Bijgewerkte standaardmodelnamen naar huidige aanbevelingen

### Optionele Verbeteringen
Je kunt je code bijwerken om gebruik te maken van:
- `FOUNDRY_LOCAL_ENDPOINT` voor expliciete endpointcontrole
- `SHOW_USAGE=1` voor zichtbaarheid van tokengebruik
- Bijgewerkte standaardmodellen (`phi-4-mini` in plaats van `phi-3.5-mini`)

## Veelvoorkomende Problemen & Oplossingen

### Probleem: "Clientinitialisatie mislukt"
**Oplossing**: Zorg ervoor dat de Foundry Local-service actief is:
```bash
foundry service start
foundry model run phi-4-mini
```

### Probleem: "Model niet gevonden"
**Oplossing**: Controleer beschikbare modellen:
```bash
foundry model list
```

### Probleem: Endpoint verbindingsfouten
**Oplossing**: Controleer endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Volgende Stappen

1. **Update Module08 voorbeelden**: Pas vergelijkbare patronen toe op Module08/samples
2. **Voeg integratietests toe**: Maak een uitgebreide testsuite
3. **Prestatiebenchmarking**: Vergelijk prestaties voor/na
4. **Documentatie-updates**: Werk de hoofd-README bij met nieuwe patronen

## Bijdragerichtlijnen

Bij het toevoegen van nieuwe voorbeelden:
1. Gebruik `workshop_utils.py` voor consistentie
2. Volg het patroon in bestaande voorbeelden
3. Voeg uitgebreide docstrings toe
4. Voeg SDK-referentielinks toe
5. Ondersteun endpoint override
6. Voeg correcte type hints toe
7. Voeg gebruiksvoorbeelden toe in de docstring

## Versiecompatibiliteit

Deze updates zijn compatibel met:
- `foundry-local-sdk` (laatste versie)
- `openai>=1.30.0`
- Python 3.8+

---

**Laatst Bijgewerkt**: 2025-01-08  
**Onderhouder**: EdgeAI Workshop Team  
**SDK Versie**: Foundry Local SDK (laatste 0.7.117+67073234e7)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.