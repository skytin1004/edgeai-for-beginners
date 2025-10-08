<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T15:09:40+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "ro"
}
-->
# Jurnal de modificări

Toate modificările importante ale EdgeAI pentru Începători sunt documentate aici. Acest proiect utilizează intrări bazate pe date și stilul Keep a Changelog (Adăugat, Modificat, Reparat, Eliminat, Documentație, Mutat).

## 2025-10-08

### Adăugat - Actualizare cuprinzătoare a atelierului
- **Rescriere completă a README.md pentru atelier**:
  - Adăugată o introducere cuprinzătoare care explică valoarea Edge AI (confidențialitate, performanță, cost)
  - Create 6 obiective principale de învățare cu competențe detaliate
  - Adăugat un tabel cu rezultatele învățării, livrabilele și matricea de competențe
  - Inclus secțiunea de abilități pregătite pentru carieră pentru relevanța în industrie
  - Adăugat ghid de pornire rapidă cu cerințe preliminare și configurare în 3 pași
  - Create tabele de resurse pentru exemple Python (8 fișiere cu timpi de rulare)
  - Adăugat tabel pentru notebook-uri Jupyter (8 notebook-uri cu evaluări ale dificultății)
  - Create tabel de documentație (7 documente cheie cu ghid "Când să folosești")
  - Adăugat recomandări pentru traseul de învățare pentru diferite niveluri de competență

- **Infrastructură de validare și testare a atelierului**:
  - Creat `scripts/validate_samples.py` - Instrument de validare cuprinzător pentru sintaxă, importuri și bune practici
  - Creat `scripts/test_samples.py` - Runner de teste rapide pentru toate exemplele Python
  - Adăugat documentație de validare în `scripts/README.md`

- **Documentație cuprinzătoare**:
  - Creat `SAMPLES_UPDATE_SUMMARY.md` - Ghid detaliat de peste 400 de linii care acoperă toate îmbunătățirile
  - Creat `UPDATE_COMPLETE.md` - Rezumat executiv al finalizării actualizării
  - Creat `QUICK_REFERENCE.md` - Card de referință rapidă pentru atelier

### Modificat - Modernizarea exemplelor Python din atelier
- **Toate cele 8 exemple Python actualizate cu bune practici**:
  - Îmbunătățită gestionarea erorilor cu blocuri try-except în jurul tuturor operațiunilor I/O
  - Adăugate indicii de tip și docstrings cuprinzătoare
  - Implementat model consistent de logare [INFO]/[ERROR]/[RESULT]
  - Protejate importurile opționale cu sugestii de instalare
  - Îmbunătățit feedback-ul utilizatorului în toate exemplele

- **session01/chat_bootstrap.py**:
  - Îmbunătățită inițializarea clientului cu mesaje de eroare detaliate
  - Îmbunătățită gestionarea erorilor de streaming cu validarea fragmentelor
  - Adăugat gestionarea mai bună a excepțiilor pentru indisponibilitatea serviciului

- **session02/rag_pipeline.py**:
  - Adăugat protecții pentru importurile sentence-transformers cu sugestii de instalare
  - Îmbunătățită gestionarea erorilor pentru operațiunile de generare și încorporare
  - Îmbunătățit formatul de ieșire cu rezultate structurate

- **session02/rag_eval_ragas.py**:
  - Protejate importurile opționale (ragas, datasets) cu mesaje de eroare prietenoase
  - Adăugat gestionarea erorilor pentru metricile de evaluare
  - Îmbunătățit formatul de ieșire pentru rezultatele evaluării

- **session03/benchmark_oss_models.py**:
  - Implementată degradare grațioasă (continuă în cazul eșecurilor modelelor)
  - Adăugat raportare detaliată a progresului și gestionarea erorilor per-model
  - Îmbunătățit calculul statisticilor cu recuperare cuprinzătoare a erorilor

- **session04/model_compare.py**:
  - Adăugat indicii de tip (tipuri de returnare Tuple)
  - Îmbunătățit formatul de ieșire cu rezultate JSON structurate
  - Implementată gestionarea erorilor per-model cu recuperare

- **session05/agents_orchestrator.py**:
  - Îmbunătățit Agent.act() cu docstrings cuprinzătoare
  - Adăugat gestionarea erorilor pipeline cu logare etapă cu etapă
  - Îmbunătățită gestionarea memoriei și urmărirea stării

- **session06/models_router.py**:
  - Îmbunătățită documentația funcțiilor pentru toate componentele de rutare
  - Adăugat logare detaliată în funcția route()
  - Îmbunătățit ieșirea testelor cu rezultate structurate

- **session06/models_pipeline.py**:
  - Adăugat gestionarea erorilor în funcția helper chat()
  - Îmbunătățit pipeline() cu logare etapă cu etapă și raportare a progresului
  - Îmbunătățit main() cu recuperare cuprinzătoare a erorilor

### Documentație - Îmbunătățirea documentației atelierului
- Actualizat README.md principal cu secțiunea atelierului care evidențiază traseul de învățare practic
- Îmbunătățit STUDY_GUIDE.md cu secțiunea cuprinzătoare a atelierului, incluzând:
  - Obiectivele de învățare și zonele de concentrare ale studiului
  - Întrebări de autoevaluare
  - Exerciții practice cu estimări de timp
  - Alocare de timp pentru studiu concentrat și part-time
  - Adăugat atelierul în șablonul de urmărire a progresului
- Actualizat ghidul de alocare a timpului de la 20 de ore la 30 de ore (inclusiv atelierul)
- Adăugat descrieri ale exemplelor atelierului și rezultatele învățării în README

### Reparat
- Rezolvat modele inconsistente de gestionare a erorilor în exemplele atelierului
- Reparat erori de import pentru dependențele opționale cu protecții adecvate
- Corectat lipsa indiciilor de tip în funcțiile critice
- Abordate feedback insuficient al utilizatorului în scenarii de eroare
- Reparat problemele de validare cu infrastructura de testare cuprinzătoare

---

## 2025-09-23

### Modificat - Modernizarea majoră a Modulului 08
- **Aliniere cuprinzătoare cu modelele de depozit Microsoft Foundry-Local**:
  - Actualizate toate exemplele de cod pentru a utiliza `FoundryLocalManager` modern și integrarea SDK OpenAI
  - Înlocuite apelurile manuale `requests` învechite cu utilizarea adecvată a SDK-ului
  - Aliniate modelele de implementare cu documentația oficială Microsoft și exemplele

- **Modernizarea 05.AIPoweredAgents.md**:
  - Actualizată orchestrarea multi-agent pentru a utiliza modelele SDK moderne
  - Îmbunătățită implementarea coordonatorului cu funcții avansate (buclă de feedback, monitorizare performanță)
  - Adăugat gestionarea cuprinzătoare a erorilor și verificarea sănătății serviciului
  - Integrate referințe adecvate la exemplele locale (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualizate exemplele de apelare a funcțiilor pentru a utiliza parametrul modern `tools` în locul `functions` învechit
  - Adăugat modele pregătite pentru producție cu monitorizare și urmărirea statisticilor

- **Rescriere completă a 06.ModelsAsTools.md**:
  - Înlocuit registrul de instrumente de bază cu implementarea routerului inteligent de modele
  - Adăugat selecție de modele bazată pe cuvinte cheie pentru diferite tipuri de sarcini (general, raționament, cod, creativ)
  - Integrată configurare bazată pe mediu cu alocare flexibilă de modele
  - Îmbunătățit cu monitorizarea sănătății serviciului și gestionarea erorilor
  - Adăugat modele de implementare în producție cu monitorizarea cererilor și urmărirea performanței
  - Aliniat cu implementarea locală în `samples/06/router.py` și `samples/06/model_router.ipynb`

- **Îmbunătățiri ale structurii documentației**:
  - Adăugate secțiuni de prezentare care evidențiază modernizarea și alinierea SDK-ului
  - Îmbunătățit cu emoji-uri și formatare mai bună pentru lizibilitate sporită
  - Adăugate referințe adecvate la fișierele de exemple locale în întreaga documentație
  - Inclus ghid de implementare pregătit pentru producție și bune practici

### Adăugat
- Secțiuni de prezentare cuprinzătoare în fișierele Modulului 08 care evidențiază integrarea SDK modern
- Repere arhitecturale care prezintă funcții avansate (sisteme multi-agent, rutare inteligentă)
- Referințe directe la implementările de exemple locale pentru experiență practică
- Ghid de implementare în producție cu modele de monitorizare și gestionare a erorilor
- Exemple interactive de notebook-uri Jupyter cu funcții avansate și benchmark-uri

### Reparat
- Discrepanțe de aliniere între documentație și implementările reale ale exemplelor
- Modele de utilizare SDK învechite în întreg Modulul 08
- Referințe lipsă la biblioteca locală de exemple cuprinzătoare
- Abordate abordări inconsistente de implementare în diferite secțiuni

---

## 2025-09-18

### Adăugat
- Modulul 08: Microsoft Foundry Local – Kit complet pentru dezvoltatori
  - Șase sesiuni: configurare, integrare Azure AI Foundry, modele open-source, demonstrații de ultimă generație, agenți și modele-ca-instrumente
  - Exemple rulabile sub `Module08/samples/01`–`06` cu instrucțiuni cmd Windows
    - `01` REST quick chat (`chat_quickstart.py`)
    - `02` SDK quickstart cu OpenAI/Foundry Local și suport Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demonstrație Chainlit (`app.py`)
    - `05` Orchestrare multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router modele-ca-instrumente (`router.py`)
- Suport Azure OpenAI în exemplul SDK din Sesiunea 2 cu configurare variabilă de mediu
- `.vscode/settings.json` pentru a indica `Module08/.venv` și a îmbunătăți rezoluția analizei Python
- `.env` cu sugestie `PYTHONPATH` pentru conștientizarea VS Code/Pylance

### Modificat
- Modelul implicit actualizat la `phi-4-mini` în întreaga documentație și exemple ale Modulului 08; eliminat mențiunile rămase ale `phi-3.5` din Modulul 08
- Îmbunătățiri ale routerului (`Module08/samples/06/router.py`):
  - Descoperirea punctelor finale prin `foundry service status` cu analiză regex
  - Verificare sănătate `/v1/models` la pornire
  - Registru de modele configurabil prin mediu (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cerințe actualizate: `Module08/requirements.txt` include acum `openai` (alături de `requests`, `chainlit`)
- Ghidul pentru exemplul Chainlit clarificat și adăugate soluții de depanare; rezoluția importurilor prin setările spațiului de lucru

### Reparat
- Rezolvate probleme de import:
  - Routerul nu mai depinde de un modul `utils` inexistent; funcțiile sunt incluse direct
  - Coordonatorul utilizează import relativ (`from .specialists import ...`) și este invocat prin calea modulului
  - Configurație VS Code/Pylance pentru a rezolva `chainlit` și importurile pachetelor
- Corectată o eroare minoră în `STUDY_GUIDE.md` și adăugată acoperirea Modulului 08

### Eliminat
- Șters `Module08/infra/obs.py` neutilizat și eliminat directorul gol `infra/`; modelele de observabilitate păstrate ca opționale în documentație

### Mutat
- Consolidate demonstrațiile Modulului 08 sub `Module08/samples` cu foldere numerotate pe sesiuni
  - Mutat aplicația Chainlit în `samples/04`
  - Mutat agenții în `samples/05` și adăugat fișiere `__init__.py` pentru rezoluția pachetelor

### Documentație
- Documentația sesiunilor Modulului 08 și toate README-urile exemplelor îmbogățite cu referințe Microsoft Learn și furnizori de încredere
- `Module08/README.md` actualizat cu Prezentare generală a exemplelor, configurare router și sfaturi de validare
- Secțiunea Windows Foundry Local din `Module07/README.md` validată împotriva documentației Learn
- `STUDY_GUIDE.md` actualizat:
  - Adăugat Modulul 08 la prezentare generală, programe, tracker de progres
  - Adăugat secțiune cuprinzătoare de Referințe (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istoric (rezumat)
- Arhitectura cursului și modulele stabilite (Modulele 01–07)
- Modernizarea iterativă a conținutului, standardizarea formatării și adăugarea studiilor de caz
- Extinderea acoperirii cadrelor de optimizare (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nerelease / Backlog (propuneri)
- Teste rapide opționale per-exemplu pentru a valida disponibilitatea Foundry Local
- Revizuirea traducerilor pentru a alinia referințele modelelor (ex. `phi-4-mini`) unde este cazul
- Adăugarea unei configurații minimale pyright dacă echipele preferă strictețe la nivelul spațiului de lucru

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.