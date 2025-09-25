<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-25T01:32:31+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ro"
}
-->
# Jurnal de modificări

Toate modificările notabile ale EdgeAI pentru Începători sunt documentate aici. Acest proiect utilizează intrări bazate pe date și stilul Keep a Changelog (Adăugat, Modificat, Reparat, Eliminat, Documentație, Mutat).

## 2025-09-23

### Modificat - Modernizare majoră a Modulului 08
- **Aliniere cu modelele de depozit Microsoft Foundry-Local**
  - Actualizate toate exemplele de cod pentru a utiliza `FoundryLocalManager` modern și integrarea SDK OpenAI
  - Înlocuite apelurile manuale `requests` depreciate cu utilizarea corespunzătoare a SDK-ului
  - Aliniate modelele de implementare cu documentația oficială Microsoft și exemplele

- **Modernizare 05.AIPoweredAgents.md**:
  - Actualizată orchestrarea multi-agent pentru a utiliza modelele moderne SDK
  - Îmbunătățită implementarea coordonatorului cu funcții avansate (buclă de feedback, monitorizare performanță)
  - Adăugată gestionare cuprinzătoare a erorilor și verificarea sănătății serviciului
  - Integrate referințe corespunzătoare la exemplele locale (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualizate exemplele de apelare a funcțiilor pentru a utiliza parametrul modern `tools` în locul `functions` depreciat
  - Adăugate modele pregătite pentru producție cu monitorizare și urmărirea statisticilor

- **Rescriere completă 06.ModelsAsTools.md**:
  - Înlocuit registrul de instrumente de bază cu o implementare inteligentă de rutare a modelelor
  - Adăugată selecție de modele bazată pe cuvinte cheie pentru diferite tipuri de sarcini (general, raționament, cod, creativ)
  - Integrată configurare bazată pe mediu cu atribuirea flexibilă a modelelor
  - Îmbunătățită cu monitorizarea sănătății serviciului și gestionarea erorilor
  - Adăugate modele de implementare în producție cu monitorizarea cererilor și urmărirea performanței
  - Aliniată cu implementarea locală în `samples/06/router.py` și `samples/06/model_router.ipynb`

- **Îmbunătățiri ale structurii documentației**:
  - Adăugate secțiuni de prezentare care evidențiază modernizarea și alinierea SDK
  - Îmbunătățită cu emoji-uri și formatare mai bună pentru o lizibilitate sporită
  - Adăugate referințe corespunzătoare la fișierele de exemple locale în întreaga documentație
  - Inclusă orientare pentru implementarea în producție și cele mai bune practici

### Adăugat
- Secțiuni de prezentare cuprinzătoare în fișierele Modulului 08 care evidențiază integrarea modernă SDK
- Repere arhitecturale care prezintă funcții avansate (sisteme multi-agent, rutare inteligentă)
- Referințe directe la implementările de exemple locale pentru experiență practică
- Orientare pentru implementarea în producție cu modele de monitorizare și gestionare a erorilor
- Exemple interactive de notebook-uri Jupyter cu funcții avansate și repere

### Reparat
- Discrepanțe de aliniere între documentație și implementările reale ale exemplelor
- Modele de utilizare SDK învechite în întregul Modul 08
- Referințe lipsă la biblioteca locală de exemple cuprinzătoare
- Abordări de implementare inconsistente în diferite secțiuni

---

## 2025-09-18

### Adăugat
- Modulul 08: Microsoft Foundry Local – Kit complet pentru dezvoltatori
  - Șase sesiuni: configurare, integrare Azure AI Foundry, modele open-source, demonstrații de ultimă generație, agenți și modele-ca-instrumente
  - Exemple executabile sub `Module08/samples/01`–`06` cu instrucțiuni pentru Windows cmd
    - `01` REST chat rapid (`chat_quickstart.py`)
    - `02` SDK quickstart cu OpenAI/Foundry Local și suport Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demonstrație Chainlit (`app.py`)
    - `05` Orchestrare multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router pentru modele-ca-instrumente (`router.py`)
- Suport Azure OpenAI în exemplul SDK din Sesiunea 2 cu configurare variabilă de mediu
- `.vscode/settings.json` pentru a indica `Module08/.venv` și a îmbunătăți rezoluția analizei Python
- `.env` cu sugestie `PYTHONPATH` pentru conștientizarea VS Code/Pylance

### Modificat
- Modelul implicit actualizat la `phi-4-mini` în întreaga documentație și exemple ale Modulului 08; eliminat mențiunile rămase despre `phi-3.5` în Modulul 08
- Îmbunătățiri ale routerului (`Module08/samples/06/router.py`):
  - Descoperirea punctelor finale prin `foundry service status` cu analiză regex
  - Verificare sănătate `/v1/models` la pornire
  - Registru de modele configurabil prin mediu (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cerințe actualizate: `Module08/requirements.txt` include acum `openai` (alături de `requests`, `chainlit`)
- Orientare clarificată pentru exemplul Chainlit și adăugată depanare; rezoluție import prin setările spațiului de lucru

### Reparat
- Probleme de import rezolvate:
  - Routerul nu mai depinde de un modul `utils` inexistent; funcțiile sunt incluse direct
  - Coordonatorul utilizează import relativ (`from .specialists import ...`) și este invocat prin calea modulului
  - Configurație VS Code/Pylance pentru a rezolva importurile `chainlit` și ale pachetelor
- Corectată o eroare minoră în `STUDY_GUIDE.md` și adăugată acoperirea Modulului 08

### Eliminat
- Șters `Module08/infra/obs.py` neutilizat și eliminat directorul gol `infra/`; modelele de observabilitate păstrate ca opționale în documentație

### Mutat
- Consolidate demonstrațiile Modulului 08 sub `Module08/samples` cu foldere numerotate pe sesiuni
  - Mutată aplicația Chainlit în `samples/04`
  - Mutate agenții în `samples/05` și adăugate fișiere `__init__.py` pentru rezoluția pachetelor

### Documentație
- Documentația sesiunilor Modulului 08 și toate fișierele README ale exemplelor îmbogățite cu referințe Microsoft Learn și furnizori de încredere
- `Module08/README.md` actualizat cu Prezentare generală a exemplelor, configurarea routerului și sfaturi de validare
- Secțiunea Windows Foundry Local din `Module07/README.md` validată împotriva documentației Learn
- `STUDY_GUIDE.md` actualizat:
  - Adăugat Modulul 08 la prezentare generală, programe, tracker de progres
  - Adăugată secțiune cuprinzătoare de Referințe (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istoric (rezumat)
- Arhitectura cursului și modulele stabilite (Modulele 01–07)
- Modernizare iterativă a conținutului, standardizare a formatării și adăugare de studii de caz
- Extinderea acoperirii cadrelor de optimizare (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nerelease / Backlog (propuneri)
- Teste opționale per-exemplu pentru validarea disponibilității Foundry Local
- Revizuirea traducerilor pentru alinierea referințelor modelelor (ex. `phi-4-mini`) unde este cazul
- Adăugarea unei configurații minimale pyright dacă echipele preferă strictețe la nivelul spațiului de lucru

---

