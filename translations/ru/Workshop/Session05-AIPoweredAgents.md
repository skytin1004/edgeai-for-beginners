<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aee170a832b8870fc6eea546aa544bdb",
  "translation_date": "2025-10-09T06:44:06+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "ru"
}
-->
# Сессия 5: Быстрое создание агентов с ИИ на основе Foundry Local

## Аннотация

Разрабатывайте и управляйте многоролевыми агентами с ИИ, используя среду выполнения Foundry Local с низкой задержкой и защитой конфиденциальности. Вы определите роли агентов, стратегии памяти, шаблоны вызова инструментов и графы выполнения. В сессии представлены шаблоны, которые можно расширить с помощью Chainlit или LangGraph. Стартовый проект расширяет существующий пример архитектуры агента, добавляя сохранение памяти и оценочные хуки.

## Цели обучения

- **Определение ролей**: Системные подсказки и границы возможностей
- **Реализация памяти**: Краткосрочная (диалог), долгосрочная (вектор / файл), временные блокноты
- **Создание рабочих процессов**: Последовательные, ветвящиеся и параллельные шаги агентов
- **Интеграция инструментов**: Легковесный шаблон вызова функций
- **Оценка**: Базовый трейс + оценка результатов по рубрике

## Предварительные требования

- Завершенные сессии 1–4
- Python с `foundry-local-sdk`, `openai`, опционально `chainlit`
- Локальные модели (минимум `phi-4-mini`)

### Фрагмент для кроссплатформенной среды

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Если агенты запускаются с macOS на удаленном хосте Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Демонстрационный процесс (30 минут)

### 1. Определение ролей агентов и памяти (7 минут)

Создайте `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Шаблон CLI для создания структуры (3 минуты)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Добавление вызова инструментов (7 минут)

Расширьте с помощью `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


Измените `agents_core.py`, чтобы разрешить простой синтаксис инструментов: пользователь пишет `#tool:get_time`, и агент добавляет вывод инструмента в контекст перед генерацией.

### 4. Организованный рабочий процесс (6 минут)

Создайте `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Стартовый проект: Расширение `05-agent-architecture` (7 минут)

Добавьте:
1. Слой постоянной памяти (например, добавление строк JSON с диалогами)
2. Простую оценочную рубрику: placeholders для фактичности, ясности, стиля
3. Опциональный фронтенд Chainlit (две вкладки: диалог и трейс)
4. Опциональная машина состояний в стиле LangGraph (если добавляется зависимость) для ветвящихся решений

## Контрольный список для проверки

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Ожидайте структурированный вывод конвейера с примечанием о внедрении инструмента.

## Обзор стратегий памяти

| Слой       | Назначение            | Пример               |
|------------|-----------------------|----------------------|
| Краткосрочная | Непрерывность диалога | Последние N сообщений |
| Эпизодическая | Воспоминания сессии  | JSON для каждой сессии |
| Семантическая | Долгосрочное извлечение | Векторное хранилище резюме |
| Блокнот     | Шаги рассуждения      | Встроенная цепочка размышлений (приватная) |

## Оценочные хуки (концептуально)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Устранение неполадок

| Проблема            | Причина                  | Решение                     |
|---------------------|--------------------------|-----------------------------|
| Повторяющиеся ответы | Слишком большой/маленький контекст | Настройте параметр окна памяти |
| Инструмент не вызван | Неправильный синтаксис   | Используйте формат `#tool:tool_name` |
| Медленная оркестрация | Несколько холодных моделей | Предварительно запустите подсказки для разогрева |

## Ссылки

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (опциональная концепция): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Продолжительность сессии**: 30 минут  
**Сложность**: Продвинутая

## Пример сценария и сопоставление с воркшопом

| Скрипт воркшопа | Сценарий | Цель | Пример подсказки |
|------------------|----------|------|------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Бот для исследования знаний, создающий краткие сводки для руководства | Конвейер из двух агентов (исследование → редакционная правка) с опциональными отдельными моделями | Объясните, почему вывод на периферии важен для соблюдения требований. |
| (Расширенный) концепт `tools.py` | Добавьте инструменты оценки времени и токенов | Демонстрация легковесного шаблона вызова инструментов | #tool:get_time |

### Нарратив сценария

Команда по документации для соблюдения требований нуждается в быстрых внутренних сводках, полученных из локальных знаний, без отправки черновиков в облачные сервисы. Агент-исследователь собирает краткие фактические тезисы; агент-редактор переписывает их для ясности и удобства восприятия руководством. Можно назначить отдельные модели для оптимизации задержки (быстрая SLM) и стилистической правки (большая модель только при необходимости).

### Пример многомодельной среды

```powershell
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python Workshop\samples\session05\agents_orchestrator.py
```


### Структура трейсинга (опционально)

```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Сохраняйте каждый шаг в файл JSONL для последующей оценки по рубрике.

### Опциональные улучшения

| Тема              | Улучшение                  | Преимущество               | Эскиз реализации          |
|--------------------|----------------------------|----------------------------|---------------------------|
| Роли с несколькими моделями | Отдельные модели для агентов (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Специализация и скорость  | Выберите переменные окружения для псевдонимов, вызовите `chat_once` с псевдонимом для каждой роли |
| Структурированные трейсинги | JSON-трейс каждого действия (инструмент, ввод, задержка, токены) | Отладка и оценка          | Добавьте словарь в список; запишите `.jsonl` в конце |
| Сохранение памяти | Перезагружаемый контекст диалога | Непрерывность сессии       | Сохраните `Agent.memory` в `sessions/<ts>.json` |
| Реестр инструментов | Динамическое обнаружение инструментов | Расширяемость              | Поддерживайте словарь `TOOLS` и исследуйте имена/описания |
| Повтор и откат    | Надежные длинные цепочки   | Снижение временных сбоев   | Оберните `act` в try/except + экспоненциальный откат |
| Оценка по рубрике | Автоматические качественные метки | Отслеживание улучшений     | Вторичный проход с подсказкой модели: "Оцените ясность от 1 до 5" |
| Векторная память  | Семантическое извлечение   | Богатый долгосрочный контекст | Встраивайте резюме, извлекайте top-k в системное сообщение |
| Потоковые ответы  | Быстрее воспринимаемый ответ | Улучшение UX               | Используйте потоковую передачу, как только она станет доступной, и выводите частичные токены |
| Детерминированные тесты | Контроль регрессии       | Стабильный CI              | Запустите с `temperature=0`, фиксированными seed подсказками |
| Параллельное ветвление | Быстрее исследование     | Пропускная способность      | Используйте `concurrent.futures` для независимых шагов агентов |

#### Пример записи трейсинга

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Простая подсказка для оценки

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Сохраняйте пары (`answer`, `rating`) для построения исторического графика качества.

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования этого перевода.