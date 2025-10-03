<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:22:26+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ru"
}
-->
# AGENTS.md

## Обзор проекта

EdgeAI for Beginners — это образовательный репозиторий, посвященный разработке Edge AI с использованием малых языковых моделей (SLMs). Курс охватывает основы EdgeAI, развертывание моделей, методы оптимизации и готовые к производству реализации с использованием Microsoft Foundry Local и различных AI-фреймворков.

**Ключевые технологии:**
- Python 3.8+ (основной язык для примеров AI/ML)
- .NET C# (примеры AI/ML)
- JavaScript/Node.js с Electron (для настольных приложений)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-фреймворки: LangChain, Semantic Kernel, Chainlit
- Оптимизация моделей: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Тип репозитория:** Образовательный контент с 8 модулями и 10 комплексными примерами приложений

**Архитектура:** Многомодульный учебный путь с практическими примерами, демонстрирующими шаблоны развертывания Edge AI

## Структура репозитория

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

## Команды настройки

### Настройка репозитория

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Настройка Python-примеров (Модуль08 и примеры на Python)

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

### Настройка примеров на Node.js (Пример 08 - Windows Chat App)

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

### Настройка Foundry Local

Foundry Local необходим для запуска примеров из Модуля08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Рабочий процесс разработки

### Разработка контента

Этот репозиторий содержит преимущественно **образовательный контент в формате Markdown**. При внесении изменений:

1. Редактируйте файлы `.md` в соответствующих директориях модулей
2. Следуйте существующим шаблонам форматирования
3. Убедитесь, что примеры кода точны и протестированы
4. Обновите соответствующий переведенный контент, если необходимо (или доверьте это автоматизации)

### Разработка примеров приложений

Для примеров на Python (примеры 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Для примера на Electron (пример 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Тестирование примеров приложений

Примеры на Python не имеют автоматических тестов, но их можно проверить, запустив:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Пример на Electron имеет инфраструктуру тестирования:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Инструкции по тестированию

### Проверка контента

Репозиторий использует автоматизированные рабочие процессы перевода. Ручное тестирование переводов не требуется.

**Ручная проверка изменений контента:**
1. Просмотрите рендеринг Markdown, предварительно открыв файлы `.md`
2. Убедитесь, что все ссылки ведут на действительные цели
3. Протестируйте любые фрагменты кода, включенные в документацию
4. Проверьте, что изображения загружаются корректно

### Тестирование примеров приложений

**Модуль08/примеры/08 (приложение Electron) имеет комплексное тестирование:**
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

**Примеры на Python должны быть протестированы вручную:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Руководство по стилю кода

### Контент в Markdown

- Используйте последовательную иерархию заголовков (# для заголовка, ## для основных разделов, ### для подразделов)
- Включайте блоки кода с указанием языка: ```python, ```bash, ```javascript
- Следуйте существующему форматированию для таблиц, списков и выделений
- Делайте строки читаемыми (стремитесь к ~80-100 символам, но не строго)
- Используйте относительные ссылки для внутренних ссылок

### Стиль кода Python

- Следуйте соглашениям PEP 8
- Используйте подсказки типов, где это уместно
- Включайте docstrings для функций и классов
- Используйте осмысленные имена переменных
- Делайте функции сфокусированными и лаконичными

### Стиль кода JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Основные соглашения:**
- Конфигурация ESLint предоставлена в примере 08
- Prettier для форматирования кода
- Используйте современный синтаксис ES6+
- Следуйте существующим шаблонам в кодовой базе

## Руководство по Pull Request

### Формат заголовка
```
[ModuleXX] Brief description of change
```
или
```
[Module08/samples/XX] Description for sample changes
```

### Перед отправкой

**Для изменений контента:**
- Просмотрите все измененные файлы Markdown
- Убедитесь, что ссылки и изображения работают
- Проверьте наличие опечаток и грамматических ошибок

**Для изменений примеров кода (Модуль08/примеры/08):**
```bash
npm run lint
npm test
```

**Для изменений примеров на Python:**
- Убедитесь, что пример успешно запускается
- Проверьте обработку ошибок
- Убедитесь в совместимости с Foundry Local

### Процесс проверки

- Изменения образовательного контента проверяются на точность и ясность
- Примеры кода тестируются на функциональность
- Обновления перевода обрабатываются автоматически через GitHub Actions

## Система перевода

**ВАЖНО:** Этот репозиторий использует автоматизированный перевод через GitHub Actions.

- Переводы находятся в директории `/translations/` (50+ языков)
- Автоматизация через рабочий процесс `co-op-translator.yml`
- **НЕ редактируйте файлы перевода вручную** — они будут перезаписаны
- Редактируйте только исходные файлы на английском языке в корневой директории и директориях модулей
- Переводы автоматически генерируются при пуше в ветку `main`

## Интеграция Foundry Local

Большинство примеров из Модуля08 требуют запуска Microsoft Foundry Local:

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

### Проверка Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Переменные окружения для примеров

Большинство примеров используют следующие переменные окружения:
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

## Сборка и развертывание

### Развертывание контента

Этот репозиторий в основном содержит документацию — процесс сборки для контента не требуется.

### Сборка примеров приложений

**Приложение Electron (Модуль08/примеры/08):**
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

**Примеры на Python:**
Процесс сборки отсутствует — примеры запускаются напрямую через интерпретатор Python.

## Частые проблемы и их устранение

### Foundry Local не запущен
**Проблема:** Примеры завершаются ошибками подключения

**Решение:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Проблемы с виртуальной средой Python
**Проблема:** Ошибки импорта модулей

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

### Проблемы со сборкой Electron
**Проблема:** Ошибки npm install или сборки

**Решение:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Конфликты рабочего процесса перевода
**Проблема:** PR перевода конфликтует с вашими изменениями

**Решение:**
- Редактируйте только исходные файлы на английском языке
- Доверьте автоматизированному рабочему процессу перевода обработку переводов
- Если возникают конфликты, объедините `main` с вашей веткой после слияния переводов

## Дополнительные ресурсы

### Учебные пути
- **Начальный уровень:** Модули 01-02 (7-9 часов)
- **Средний уровень:** Модули 03-04 (9-11 часов)
- **Продвинутый уровень:** Модули 05-07 (12-15 часов)
- **Экспертный уровень:** Модуль 08 (8-10 часов)

### Основной контент модулей
- **Модуль01:** Основы EdgeAI и реальные примеры
- **Модуль02:** Семейства и архитектуры малых языковых моделей (SLM)
- **Модуль03:** Стратегии локального и облачного развертывания
- **Модуль04:** Оптимизация моделей с использованием различных фреймворков
- **Модуль05:** SLMOps — эксплуатация в производстве
- **Модуль06:** AI-агенты и вызов функций
- **Модуль07:** Реализации для конкретных платформ
- **Модуль08:** Инструментарий Foundry Local с 10 комплексными примерами

### Внешние зависимости
- [Microsoft Foundry Local](https://foundry.microsoft.com/) — локальная среда выполнения AI-моделей
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) — фреймворк оптимизации
- [Microsoft Olive](https://microsoft.github.io/Olive/) — инструментарий оптимизации моделей
- [OpenVINO](https://docs.openvino.ai/) — инструментарий оптимизации от Intel

## Примечания, специфичные для проекта

### Примеры приложений из Модуля08

Репозиторий включает 10 комплексных примеров приложений:

1. **01-REST Chat Quickstart** — базовая интеграция OpenAI SDK
2. **02-OpenAI SDK Integration** — расширенные функции SDK
3. **03-Model Discovery & Benchmarking** — инструменты сравнения моделей
4. **04-Chainlit RAG Application** — генерация с дополнением извлечения
5. **05-Multi-Agent Orchestration** — базовая координация агентов
6. **06-Models-as-Tools Router** — интеллектуальная маршрутизация моделей
7. **07-Direct API Client** — низкоуровневая интеграция API
8. **08-Windows 11 Chat App** — нативное настольное приложение на Electron
9. **09-Advanced Multi-Agent System** — сложная оркестрация агентов
10. **10-Foundry Tools Framework** — интеграция LangChain/Semantic Kernel

Каждый пример демонстрирует различные аспекты разработки Edge AI с Foundry Local.

### Учет производительности

- SLM оптимизированы для развертывания на периферии (2-16 ГБ ОЗУ)
- Локальное выполнение обеспечивает время отклика 50-500 мс
- Техники квантования достигают 75% сокращения размера при сохранении 85% производительности
- Возможности для реального времени в локальных моделях

### Безопасность и конфиденциальность

- Вся обработка происходит локально — данные не отправляются в облако
- Подходит для приложений, требующих конфиденциальности (медицина, финансы)
- Соответствует требованиям суверенитета данных
- Foundry Local полностью работает на локальном оборудовании

---

**Это образовательный репозиторий, ориентированный на обучение разработке Edge AI. Основной вклад — улучшение образовательного контента и добавление/улучшение примеров приложений, демонстрирующих концепции Edge AI.**

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.