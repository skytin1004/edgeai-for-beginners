<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-23T00:45:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ro"
}
-->
# Jurnal de modificări

Toate modificările importante ale EdgeAI pentru Începători sunt documentate aici. Acest proiect folosește intrări bazate pe date și stilul Keep a Changelog (Adăugat, Modificat, Reparat, Eliminat, Documentație, Mutat).

## 2025-09-18

### Adăugat
- Modulul 08: Microsoft Foundry Local – Kit complet pentru dezvoltatori
  - Șase sesiuni: configurare, integrare Azure AI Foundry, modele open-source, demonstrații de ultimă generație, agenți și modele ca instrumente
  - Exemple executabile sub `Module08/samples/01`–`06` cu instrucțiuni pentru Windows cmd
    - `01` REST chat rapid (`chat_quickstart.py`)
    - `02` SDK quickstart cu OpenAI/Foundry Local și suport Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demonstrație Chainlit (`app.py`)
    - `05` Orchestrare multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router pentru modele ca instrumente (`router.py`)
- Suport Azure OpenAI în exemplul SDK din Sesiunea 2 cu configurare variabilă de mediu
- `.vscode/settings.json` pentru a indica către `Module08/.venv` și a îmbunătăți rezoluția analizei Python
- `.env` cu sugestie `PYTHONPATH` pentru conștientizarea VS Code/Pylance

### Modificat
- Modelul implicit actualizat la `phi-4-mini` în documentația și exemplele Modulului 08; eliminat mențiunile rămase despre `phi-3.5` în cadrul Modulului 08
- Îmbunătățiri ale routerului (`Module08/samples/06/router.py`):
  - Descoperirea punctelor de acces prin `foundry service status` cu analiză regex
  - Verificare de sănătate `/v1/models` la pornire
  - Registru de modele configurabil prin mediu (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cerințe actualizate: `Module08/requirements.txt` include acum `openai` (alături de `requests`, `chainlit`)
- Ghidul pentru exemplul Chainlit clarificat și adăugate soluții pentru probleme; rezoluția importurilor prin setările workspace-ului

### Reparat
- Probleme de import rezolvate:
  - Routerul nu mai depinde de un modul inexistent `utils`; funcțiile sunt incluse direct
  - Coordinator folosește import relativ (`from .specialists import ...`) și este invocat prin calea modulului
  - Configurația VS Code/Pylance pentru a rezolva importurile `chainlit` și ale pachetelor
- Corectat o eroare minoră de tipar în `STUDY_GUIDE.md` și adăugată acoperirea Modulului 08

### Eliminat
- Șters `Module08/infra/obs.py` neutilizat și eliminat directorul gol `infra/`; modelele de observabilitate păstrate ca opționale în documentație

### Mutat
- Demonstrațiile Modulului 08 consolidate sub `Module08/samples` cu foldere numerotate pe sesiuni
  - Aplicația Chainlit mutată la `samples/04`
  - Agenții mutați la `samples/05` și adăugate fișiere `__init__.py` pentru rezoluția pachetelor

### Documentație
- Documentația sesiunilor Modulului 08 și toate fișierele README ale exemplelor îmbogățite cu referințe Microsoft Learn și furnizori de încredere
- `Module08/README.md` actualizat cu Prezentare generală a exemplelor, configurarea routerului și sfaturi de validare
- Secțiunea Windows Foundry Local din `Module07/README.md` validată conform documentației Learn
- `STUDY_GUIDE.md` actualizat:
  - Adăugat Modulul 08 la prezentare generală, programe, tracker de progres
  - Adăugată secțiunea cuprinzătoare de Referințe (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istoric (rezumat)
- Arhitectura cursului și modulele stabilite (Modulele 01–07)
- Modernizarea iterativă a conținutului, standardizarea formatării și adăugarea studiilor de caz
- Extinderea acoperirii cadrelor de optimizare (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nerelease / Backlog (propuneri)
- Teste opționale per exemplu pentru validarea disponibilității Foundry Local
- Revizuirea traducerilor pentru a alinia referințele modelelor (de ex., `phi-4-mini`) unde este cazul
- Adăugarea unei configurații minimale pyright dacă echipele preferă strictețe la nivel de workspace

---

