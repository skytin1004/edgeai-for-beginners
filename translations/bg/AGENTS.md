<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:44:37+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bg"
}
-->
# AGENTS.md

## Преглед на проекта

EdgeAI for Beginners е изчерпателно образователно хранилище, което учи разработка на Edge AI с Малки Езикови Модели (SLMs). Курсът обхваща основите на EdgeAI, внедряване на модели, техники за оптимизация и готови за производство реализации с Microsoft Foundry Local и различни AI рамки.

**Основни технологии:**
- Python 3.8+ (основен език за AI/ML примери)
- .NET C# (AI/ML примери)
- JavaScript/Node.js с Electron (за десктоп приложения)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI рамки: LangChain, Semantic Kernel, Chainlit
- Оптимизация на модели: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип хранилище:** Образователно съдържание с 8 модула и 10 изчерпателни примерни приложения

**Архитектура:** Многомодулен учебен път с практически примери, демонстриращи модели за внедряване на Edge AI

## Структура на хранилището

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

## Команди за настройка

### Настройка на хранилището

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Настройка на Python примери (Модул08 и Python примери)

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

### Настройка на Node.js примери (Пример 08 - Windows Chat App)

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

### Настройка на Foundry Local

Foundry Local е необходим за изпълнение на примерите от Модул08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Работен процес за разработка

### Разработка на съдържание

Това хранилище съдържа предимно **Markdown образователно съдържание**. При извършване на промени:

1. Редактирайте `.md` файловете в съответните директории на модулите
2. Следвайте съществуващите модели за форматиране
3. Уверете се, че примерите с код са точни и тествани
4. Актуализирайте съответното преведено съдържание, ако е необходимо (или оставете автоматизацията да го направи)

### Разработка на примерни приложения

За Python примери (примери 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

За Electron пример (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестване на примерни приложения

Python примерите нямат автоматизирани тестове, но могат да бъдат валидирани чрез изпълнение:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron примерът има инфраструктура за тестове:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Инструкции за тестване

### Валидиране на съдържание

Хранилището използва автоматизирани работни потоци за превод. Не се изисква ръчно тестване за преводи.

**Ръчна проверка за промени в съдържанието:**
1. Прегледайте рендирането на Markdown чрез предварителен преглед на `.md` файловете
2. Уверете се, че всички връзки сочат към валидни цели
3. Тествайте всички включени кодови фрагменти в документацията
4. Проверете дали изображенията се зареждат правилно

### Тестване на примерни приложения

**Модул08/примери/08 (Electron приложение) има изчерпателно тестване:**
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

**Python примерите трябва да бъдат тествани ръчно:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Насоки за стил на код

### Markdown съдържание

- Използвайте последователна йерархия на заглавията (# за заглавие, ## за основни секции, ### за подсекции)
- Включвайте кодови блокове със спецификатори за език: ```python, ```bash, ```javascript
- Следвайте съществуващото форматиране за таблици, списъци и акценти
- Поддържайте редовете четими (целете ~80-100 символа, но не строго)
- Използвайте относителни връзки за вътрешни препратки

### Стил на Python код

- Следвайте конвенциите на PEP 8
- Използвайте типови подсказки, когато е подходящо
- Включвайте docstrings за функции и класове
- Използвайте смислени имена на променливи
- Поддържайте функциите фокусирани и кратки

### Стил на JavaScript/Node.js код

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основни конвенции:**
- ESLint конфигурация, предоставена в пример 08
- Prettier за форматиране на код
- Използвайте съвременен ES6+ синтаксис
- Следвайте съществуващите модели в кодовата база

## Насоки за Pull Request

### Формат на заглавието
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Преди изпращане

**За промени в съдържанието:**
- Прегледайте всички модифицирани Markdown файлове
- Уверете се, че връзките и изображенията работят
- Проверете за правописни и граматически грешки

**За промени в примерния код (Модул08/примери/08):**
```bash
npm run lint
npm test
```

**За промени в Python примерите:**
- Тествайте дали примерът се изпълнява успешно
- Уверете се, че обработката на грешки работи
- Проверете съвместимостта с Foundry Local

### Процес на преглед

- Промените в образователното съдържание се преглеждат за точност и яснота
- Примерите с код се тестват за функционалност
- Актуализациите на преводите се обработват автоматично чрез GitHub Actions

## Система за превод

**ВАЖНО:** Това хранилище използва автоматизиран превод чрез GitHub Actions.

- Преводите се намират в директорията `/translations/` (50+ езика)
- Автоматизирано чрез работния поток `co-op-translator.yml`
- **НЕ редактирайте ръчно файловете за превод** - те ще бъдат презаписани
- Редактирайте само английските изходни файлове в основната директория и директориите на модулите
- Преводите се генерират автоматично при push към клона `main`

## Интеграция с Foundry Local

Повечето примери от Модул08 изискват Microsoft Foundry Local да бъде стартиран:

### Стартиране на Foundry Local
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

### Проверка на Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Променливи на средата за примери

Повечето примери използват тези променливи на средата:
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

## Създаване и внедряване

### Внедряване на съдържание

Това хранилище е предимно документация - не се изисква процес на създаване за съдържанието.

### Създаване на примерни приложения

**Electron приложение (Модул08/примери/08):**
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
Няма процес на създаване - примерите се изпълняват директно с Python интерпретатор.

## Чести проблеми и отстраняване на неизправности

### Foundry Local не е стартиран
**Проблем:** Примерите се провалят с грешки при връзка

**Решение:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Проблеми с Python виртуална среда
**Проблем:** Грешки при импортиране на модули

**Решение:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Проблеми със създаване на Electron
**Проблем:** npm install или грешки при създаване

**Решение:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Конфликти в работния поток за превод
**Проблем:** Преводният PR влиза в конфликт с вашите промени

**Решение:**
- Редактирайте само английските изходни файлове
- Оставете автоматизирания работен поток за превод да обработи преводите
- Ако възникнат конфликти, обединете `main` във вашия клон след като преводите бъдат обединени

## Допълнителни ресурси

### Учебни пътеки
- **Начинаещи:** Модули 01-02 (7-9 часа)
- **Средно ниво:** Модули 03-04 (9-11 часа)
- **Напреднали:** Модули 05-07 (12-15 часа)
- **Експерти:** Модул 08 (8-10 часа)

### Основно съдържание на модулите
- **Модул01:** Основи на EdgeAI и реални казуси
- **Модул02:** Семейства и архитектури на Малки Езикови Модели (SLM)
- **Модул03:** Стратегии за локално и облачно внедряване
- **Модул04:** Оптимизация на модели с множество рамки
- **Модул05:** SLMOps - операции за производство
- **Модул06:** AI агенти и извикване на функции
- **Модул07:** Имплементации, специфични за платформи
- **Модул08:** Инструментариум Foundry Local с 10 изчерпателни примера

### Външни зависимости
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Локално изпълнение на AI модели
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Рамка за оптимизация
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Инструментариум за оптимизация на модели
- [OpenVINO](https://docs.openvino.ai/) - Инструментариум за оптимизация на Intel

## Бележки, специфични за проекта

### Примерни приложения от Модул08

Хранилището включва 10 изчерпателни примерни приложения:

1. **01-REST Chat Quickstart** - Основна интеграция с OpenAI SDK
2. **02-OpenAI SDK Integration** - Разширени функции на SDK
3. **03-Model Discovery & Benchmarking** - Инструменти за сравнение на модели
4. **04-Chainlit RAG Application** - Генерация, базирана на извличане
5. **05-Multi-Agent Orchestration** - Основна координация на агенти
6. **06-Models-as-Tools Router** - Интелигентно маршрутизиране на модели
7. **07-Direct API Client** - Ниско ниво на интеграция с API
8. **08-Windows 11 Chat App** - Нативно десктоп приложение с Electron
9. **09-Advanced Multi-Agent System** - Сложна оркестрация на агенти
10. **10-Foundry Tools Framework** - Интеграция с LangChain/Semantic Kernel

Всеки пример демонстрира различни аспекти на разработката на Edge AI с Foundry Local.

### Съображения за производителност

- SLMs са оптимизирани за внедряване на Edge (2-16GB RAM)
- Локалното изпълнение осигурява времена за отговор от 50-500ms
- Техники за квантизация постигат 75% намаление на размера с 85% запазване на производителността
- Възможности за реално време в разговори с локални модели

### Сигурност и поверителност

- Цялата обработка се извършва локално - няма изпращане на данни към облака
- Подходящо за приложения, чувствителни към поверителност (здравеопазване, финанси)
- Отговаря на изискванията за суверенитет на данните
- Foundry Local работи изцяло на локален хардуер

---

**Това е образователно хранилище, фокусирано върху обучението за разработка на Edge AI. Основният модел за принос е подобряване на образователното съдържание и добавяне/усъвършенстване на примерни приложения, които демонстрират концепции за Edge AI.**

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.