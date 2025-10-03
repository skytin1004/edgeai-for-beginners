<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:47:49+00:00",
  "source_file": "AGENTS.md",
  "language_code": "uk"
}
-->
# AGENTS.md

## Огляд проєкту

EdgeAI for Beginners — це всебічний освітній репозиторій, який навчає розробці Edge AI з використанням малих мовних моделей (SLMs). Курс охоплює основи EdgeAI, розгортання моделей, техніки оптимізації та готові до виробництва реалізації з використанням Microsoft Foundry Local і різних AI-фреймворків.

**Ключові технології:**
- Python 3.8+ (основна мова для зразків AI/ML)
- .NET C# (зразки AI/ML)
- JavaScript/Node.js з Electron (для настільних додатків)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-фреймворки: LangChain, Semantic Kernel, Chainlit
- Оптимізація моделей: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозиторію:** Освітній контент із 8 модулями та 10 комплексними прикладами додатків

**Архітектура:** Багатомодульний навчальний шлях із практичними прикладами, що демонструють шаблони розгортання Edge AI

## Структура репозиторію

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

## Команди налаштування

### Налаштування репозиторію

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Налаштування зразків Python (Модуль08 та зразки Python)

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

### Налаштування зразків Node.js (Зразок 08 - Windows Chat App)

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

### Налаштування Foundry Local

Foundry Local необхідний для запуску зразків Модуля08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Робочий процес розробки

### Розробка контенту

Цей репозиторій містить переважно **Markdown-освітній контент**. При внесенні змін:

1. Редагуйте файли `.md` у відповідних каталогах модулів
2. Дотримуйтесь існуючих шаблонів форматування
3. Переконайтеся, що приклади коду точні та протестовані
4. Оновіть відповідний перекладений контент, якщо необхідно (або дозвольте автоматизації це зробити)

### Розробка прикладних додатків

Для зразків Python (зразки 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Для зразка Electron (зразок 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестування прикладних додатків

Зразки Python не мають автоматизованих тестів, але їх можна перевірити, запустивши:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Зразок Electron має інфраструктуру тестування:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Інструкції з тестування

### Перевірка контенту

Репозиторій використовує автоматизовані робочі процеси перекладу. Ручне тестування перекладів не потрібне.

**Ручна перевірка змін контенту:**
1. Перегляньте рендеринг Markdown, переглядаючи файли `.md`
2. Переконайтеся, що всі посилання ведуть до дійсних цілей
3. Протестуйте будь-які фрагменти коду, включені в документацію
4. Перевірте, чи правильно завантажуються зображення

### Тестування прикладних додатків

**Модуль08/зразки/08 (додаток Electron) має комплексне тестування:**
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

**Зразки Python слід тестувати вручну:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Рекомендації щодо стилю коду

### Контент Markdown

- Використовуйте послідовну ієрархію заголовків (# для заголовка, ## для основних розділів, ### для підрозділів)
- Включайте блоки коду з вказівкою мови: ```python, ```bash, ```javascript
- Дотримуйтесь існуючого форматування для таблиць, списків і виділення
- Зберігайте читабельність рядків (прагніть до ~80-100 символів, але не строго)
- Використовуйте відносні посилання для внутрішніх референцій

### Стиль коду Python

- Дотримуйтесь конвенцій PEP 8
- Використовуйте підказки типів, де це доречно
- Включайте docstrings для функцій і класів
- Використовуйте значущі назви змінних
- Зберігайте функції сфокусованими та лаконічними

### Стиль коду JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основні конвенції:**
- Конфігурація ESLint надана в зразку 08
- Prettier для форматування коду
- Використовуйте сучасний синтаксис ES6+
- Дотримуйтесь існуючих шаблонів у кодовій базі

## Рекомендації щодо Pull Request

### Формат заголовка
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Перед поданням

**Для змін контенту:**
- Перегляньте всі змінені файли Markdown
- Переконайтеся, що посилання та зображення працюють
- Перевірте на наявність орфографічних і граматичних помилок

**Для змін зразків коду (Модуль08/зразки/08):**
```bash
npm run lint
npm test
```

**Для змін зразків Python:**
- Перевірте, чи зразок успішно запускається
- Переконайтеся, що обробка помилок працює
- Перевірте сумісність із Foundry Local

### Процес перегляду

- Зміни освітнього контенту перевіряються на точність і ясність
- Зразки коду тестуються на функціональність
- Оновлення перекладів обробляються автоматично через GitHub Actions

## Система перекладу

**ВАЖЛИВО:** Цей репозиторій використовує автоматизований переклад через GitHub Actions.

- Переклади знаходяться в каталозі `/translations/` (50+ мов)
- Автоматизовано через робочий процес `co-op-translator.yml`
- **НЕ редагуйте файли перекладу вручну** - вони будуть перезаписані
- Редагуйте лише англійські вихідні файли в кореневих і модульних каталогах
- Переклади автоматично генеруються при пуші в гілку `main`

## Інтеграція Foundry Local

Більшість зразків Модуля08 вимагають запуску Microsoft Foundry Local:

### Запуск Foundry Local
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

### Перевірка Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Змінні середовища для зразків

Більшість зразків використовують ці змінні середовища:
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

## Збірка та розгортання

### Розгортання контенту

Цей репозиторій переважно документаційний — процес збірки для контенту не потрібен.

### Збірка прикладних додатків

**Додаток Electron (Модуль08/зразки/08):**
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

**Зразки Python:**
Процес збірки відсутній — зразки запускаються безпосередньо через інтерпретатор Python.

## Поширені проблеми та усунення несправностей

### Foundry Local не запущений
**Проблема:** Зразки не працюють через помилки з'єднання

**Рішення:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Проблеми з віртуальним середовищем Python
**Проблема:** Помилки імпорту модулів

**Рішення:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Проблеми зі збіркою Electron
**Проблема:** Помилки npm install або збірки

**Рішення:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Конфлікти робочого процесу перекладу
**Проблема:** Конфлікт PR перекладу з вашими змінами

**Рішення:**
- Редагуйте лише англійські вихідні файли
- Дозвольте автоматизованому робочому процесу перекладу обробляти переклади
- Якщо виникають конфлікти, об'єднайте `main` у вашу гілку після злиття перекладів

## Додаткові ресурси

### Навчальні шляхи
- **Шлях для початківців:** Модулі 01-02 (7-9 годин)
- **Середній рівень:** Модулі 03-04 (9-11 годин)
- **Просунутий рівень:** Модулі 05-07 (12-15 годин)
- **Експертний рівень:** Модуль 08 (8-10 годин)

### Основний контент модулів
- **Модуль01:** Основи EdgeAI та реальні кейси
- **Модуль02:** Сімейства та архітектури малих мовних моделей (SLM)
- **Модуль03:** Стратегії локального та хмарного розгортання
- **Модуль04:** Оптимізація моделей за допомогою різних фреймворків
- **Модуль05:** SLMOps - операції у виробництві
- **Модуль06:** AI-агенти та виклик функцій
- **Модуль07:** Реалізації для конкретних платформ
- **Модуль08:** Інструментарій Foundry Local із 10 комплексними зразками

### Зовнішні залежності
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Локальне середовище виконання AI-моделей
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Фреймворк оптимізації
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Інструментарій оптимізації моделей
- [OpenVINO](https://docs.openvino.ai/) - Інструментарій оптимізації від Intel

## Примітки щодо проєкту

### Зразки прикладних додатків Модуля08

Репозиторій містить 10 комплексних зразків прикладних додатків:

1. **01-REST Chat Quickstart** - Базова інтеграція OpenAI SDK
2. **02-OpenAI SDK Integration** - Розширені функції SDK
3. **03-Model Discovery & Benchmarking** - Інструменти порівняння моделей
4. **04-Chainlit RAG Application** - Генерація з підкріпленням
5. **05-Multi-Agent Orchestration** - Базова координація агентів
6. **06-Models-as-Tools Router** - Інтелектуальне маршрутизування моделей
7. **07-Direct API Client** - Низькорівнева інтеграція API
8. **08-Windows 11 Chat App** - Нативний настільний додаток Electron
9. **09-Advanced Multi-Agent System** - Складна оркестрація агентів
10. **10-Foundry Tools Framework** - Інтеграція LangChain/Semantic Kernel

Кожен зразок демонструє різні аспекти розробки Edge AI з Foundry Local.

### Міркування щодо продуктивності

- SLM оптимізовані для розгортання на краю (2-16 ГБ оперативної пам'яті)
- Локальне виконання забезпечує час відгуку 50-500 мс
- Техніки квантування досягають 75% зменшення розміру з 85% збереження продуктивності
- Можливості реального часу для розмов із локальними моделями

### Безпека та конфіденційність

- Усі обробки виконуються локально — дані не надсилаються в хмару
- Підходить для додатків, чутливих до конфіденційності (охорона здоров'я, фінанси)
- Відповідає вимогам щодо суверенітету даних
- Foundry Local працює повністю на локальному обладнанні

---

**Це освітній репозиторій, орієнтований на навчання розробці Edge AI. Основний шаблон внеску — покращення освітнього контенту та додавання/розширення зразків прикладних додатків, які демонструють концепції Edge AI.**

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.