<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:45:16+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sr"
}
-->
# AGENTS.md

## Преглед пројекта

EdgeAI for Beginners је свеобухватан едукативни репозиторијум који подучава развој Edge AI-а са малим језичким моделима (SLM). Курс обухвата основе EdgeAI-а, постављање модела, технике оптимизације и имплементације спремне за производњу користећи Microsoft Foundry Local и различите AI оквире.

**Кључне технологије:**
- Python 3.8+ (примарни језик за AI/ML примере)
- .NET C# (AI/ML примери)
- JavaScript/Node.js са Electron-ом (за десктоп апликације)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI оквири: LangChain, Semantic Kernel, Chainlit
- Оптимизација модела: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозиторијума:** Едукативни садржај са 8 модула и 10 свеобухватних примера апликација

**Архитектура:** Вишемодулни пут учења са практичним примерима који демонстрирају обрасце постављања Edge AI-а

## Структура репозиторијума

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Команде за постављање

### Постављање репозиторијума

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Постављање Python примера (Модул08 и Python примери)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies for Module08 samples
cd Module08
pip install -r requirements.txt
```

### Постављање Node.js примера (Пример 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Постављање Foundry Local-а

Foundry Local је потребан за покретање примера из Модула08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Радни ток развоја

### Развој садржаја

Овај репозиторијум углавном садржи **Markdown едукативни садржај**. Приликом измена:

1. Уређујте `.md` датотеке у одговарајућим директоријумима модула
2. Пратите постојеће обрасце форматирања
3. Осигурајте да су примери кода тачни и тестирани
4. Ажурирајте одговарајући преведени садржај ако је потребно (или дозволите аутоматизацији да то уради)

### Развој примера апликација

За Python примере (примери 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

За Electron пример (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестирање примера апликација

Python примери немају аутоматизоване тестове, али се могу проверити покретањем:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron пример има инфраструктуру за тестирање:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Упутства за тестирање

### Валидација садржаја

Репозиторијум користи аутоматизоване радне токове за превођење. Није потребно ручно тестирање превода.

**Ручна валидација за измене садржаја:**
1. Прегледајте рендеровање Markdown-а прегледом `.md` датотека
2. Проверите да ли сви линкови воде ка важећим циљевима
3. Тестирајте све укључене исечке кода у документацији
4. Проверите да ли се слике правилно учитавају

### Тестирање примера апликација

**Модул08/примери/08 (Electron апликација) има свеобухватно тестирање:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python примери треба ручно тестирати:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Упутства за стил кода

### Markdown садржај

- Користите доследну хијерархију наслова (# за наслов, ## за главне секције, ### за подсекције)
- Укључите блокове кода са спецификацијом језика: ```python, ```bash, ```javascript
- Пратите постојеће форматирање за табеле, листе и наглашавање
- Држите линије читљивим (циљајте ~80-100 карактера, али није строго)
- Користите релативне линкове за унутрашње референце

### Python стил кода

- Пратите PEP 8 конвенције
- Користите типске назнаке где је прикладно
- Укључите docstrings за функције и класе
- Користите смислене називе променљивих
- Држите функције фокусираним и концизним

### JavaScript/Node.js стил кода

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Кључне конвенције:**
- ESLint конфигурација је обезбеђена у примеру 08
- Prettier за форматирање кода
- Користите модеран ES6+ синтакс
- Пратите постојеће обрасце у бази кода

## Упутства за Pull Request

### Формат наслова
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Пре подношења

**За измене садржаја:**
- Прегледајте све модификоване Markdown датотеке
- Проверите да ли линкови и слике раде
- Проверите правописне и граматичке грешке

**За измене кода примера (Модул08/примери/08):**
```bash
npm run lint
npm test
```

**За измене Python примера:**
- Тестирајте да пример успешно ради
- Проверите да ли обрада грешака функционише
- Проверите компатибилност са Foundry Local-ом

### Процес прегледа

- Измене едукативног садржаја се прегледају ради тачности и јасноће
- Примери кода се тестирају ради функционалности
- Ажурирања превода се аутоматски обрађују преко GitHub Actions-а

## Систем превођења

**ВАЖНО:** Овај репозиторијум користи аутоматизовано превођење преко GitHub Actions-а.

- Преводи се налазе у директоријуму `/translations/` (50+ језика)
- Аутоматизовано преко `co-op-translator.yml` радног тока
- **НЕ уређујте ручно датотеке превода** - биће преписане
- Уређујте само изворне датотеке на енглеском у корену и директоријумима модула
- Преводи се аутоматски генеришу при пушу на `main` грану

## Интеграција Foundry Local-а

Већина примера из Модула08 захтева да Microsoft Foundry Local буде покренут:

### Покретање Foundry Local-а
```bash
# Start Foundry Local 
foundry service start

#foundry service host and port are displayed after running this command or `foundry service status`

# Run a specific model
foundry model run phi-4-mini

# Or run with different models
foundry model run qwen2.5-coder-0.5b
foundry model run mistral-7b
```

### Провера Foundry Local-а
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Променљиве окружења за примере

Већина примера користи ове променљиве окружења:
```bash
# Foundry Local configuration (defaults work for most cases)
set BASE_URL=http://localhost:55769
set MODEL=phi-4-mini
set API_KEY=

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Изградња и постављање

### Постављање садржаја

Овај репозиторијум је углавном документација - није потребан процес изградње за садржај.

### Изградња примера апликација

**Electron апликација (Модул08/примери/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python примери:**
Нема процеса изградње - примери се директно покрећу са Python интерпретатором.

## Уобичајени проблеми и решавање

### Foundry Local није покренут
**Проблем:** Примери не успевају са грешкама у вези

**Решење:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Проблеми са Python виртуелним окружењем
**Проблем:** Грешке при увозу модула

**Решење:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Проблеми са изградњом Electron-а
**Проблем:** npm install или грешке при изградњи

**Решење:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Конфликти у радном току превођења
**Проблем:** Translation PR у конфликту са вашим изменама

**Решење:**
- Уређујте само изворне датотеке на енглеском
- Дозволите аутоматизованом радном току превођења да обради преводе
- Ако дође до конфликта, спојите `main` у вашу грану након што се преводи споје

## Додатни ресурси

### Путеви учења
- **Почетнички пут:** Модули 01-02 (7-9 сати)
- **Средњи пут:** Модули 03-04 (9-11 сати)
- **Напредни пут:** Модули 05-07 (12-15 сати)
- **Експертски пут:** Модул 08 (8-10 сати)

### Кључни садржај модула
- **Модул01:** Основе EdgeAI-а и студије случаја из стварног света
- **Модул02:** Породице и архитектуре малих језичких модела (SLM)
- **Модул03:** Стратегије локалног и облачног постављања
- **Модул04:** Оптимизација модела са више оквира
- **Модул05:** SLMOps - операције у производњи
- **Модул06:** AI агенти и позивање функција
- **Модул07:** Имплементације специфичне за платформу
- **Модул08:** Foundry Local алат са 10 свеобухватних примера

### Спољашње зависности
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Локално окружење за AI моделе
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Оквир за оптимизацију
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Алат за оптимизацију модела
- [OpenVINO](https://docs.openvino.ai/) - Intel-ов алат за оптимизацију

## Белешке специфичне за пројекат

### Примери апликација из Модула08

Репозиторијум укључује 10 свеобухватних примера апликација:

1. **01-REST Chat Quickstart** - Основна интеграција OpenAI SDK-а
2. **02-OpenAI SDK Integration** - Напредне функције SDK-а
3. **03-Model Discovery & Benchmarking** - Алат за поређење модела
4. **04-Chainlit RAG Application** - Генерација уз помоћ претраживања
5. **05-Multi-Agent Orchestration** - Основна координација агената
6. **06-Models-as-Tools Router** - Интелигентно рутирање модела
7. **07-Direct API Client** - Клијент за ниско-ниво API интеграцију
8. **08-Windows 11 Chat App** - Нативна Electron десктоп апликација
9. **09-Advanced Multi-Agent System** - Комплексна оркестрација агената
10. **10-Foundry Tools Framework** - Интеграција LangChain/Semantic Kernel-а

Сваки пример демонстрира различите аспекте развоја Edge AI-а са Foundry Local-ом.

### Перформансе

- SLM-ови су оптимизовани за постављање на ивици (2-16GB RAM-а)
- Локално закључивање пружа време одговора од 50-500ms
- Технике квантовања постижу смањење величине од 75% уз задржавање 85% перформанси
- Способности за разговор у реалном времену са локалним моделима

### Безбедност и приватност

- Сва обрада се дешава локално - нема слања података у облак
- Погодно за апликације осетљиве на приватност (здравство, финансије)
- Испуњава захтеве за суверенитет података
- Foundry Local ради искључиво на локалном хардверу

---

**Ово је едукативни репозиторијум фокусиран на подучавање развоја Edge AI-а. Примарни образац доприноса је побољшање едукативног садржаја и додавање/унапређење примера апликација које демонстрирају концепте Edge AI-а.**

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.