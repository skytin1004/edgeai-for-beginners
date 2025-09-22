<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b02a49f9b47dc500f1b4791c01bb9501",
  "translation_date": "2025-09-22T12:50:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "es"
}
-->
# Registro de cambios

Todos los cambios importantes en EdgeAI para Principiantes están documentados aquí. Este proyecto utiliza entradas basadas en fechas y el estilo Keep a Changelog (Añadido, Cambiado, Corregido, Eliminado, Documentación, Movido).

## 2025-09-18

### Añadido
- Módulo 08: Microsoft Foundry Local – Kit completo para desarrolladores
  - Seis sesiones: configuración, integración con Azure AI Foundry, modelos de código abierto, demostraciones avanzadas, agentes y modelos como herramientas
  - Ejemplos ejecutables bajo `Module08/samples/01`–`06` con instrucciones para cmd de Windows
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Inicio rápido con SDK y soporte para OpenAI/Foundry Local y Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI listar y evaluar (`list_and_bench.cmd`)
    - `04` Demostración de Chainlit (`app.py`)
    - `05` Orquestación de múltiples agentes (`python -m samples.05.agents.coordinator`)
    - `06` Enrutador de modelos como herramientas (`router.py`)
- Soporte para Azure OpenAI en el ejemplo de SDK de la Sesión 2 con configuración de variables de entorno
- `.vscode/settings.json` apuntando a `Module08/.venv` para mejorar la resolución de análisis de Python
- `.env` con sugerencia de `PYTHONPATH` para la compatibilidad con VS Code/Pylance

### Cambiado
- Modelo predeterminado actualizado a `phi-4-mini` en toda la documentación y ejemplos del Módulo 08; eliminadas las menciones restantes de `phi-3.5` dentro del Módulo 08
- Mejoras en el enrutador (`Module08/samples/06/router.py`):
  - Descubrimiento de endpoints mediante `foundry service status` con análisis de expresiones regulares
  - Verificación de salud de `/v1/models` al inicio
  - Registro de modelos configurable por entorno (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos actualizados: `Module08/requirements.txt` ahora incluye `openai` (junto con `requests`, `chainlit`)
- Clarificación de la guía de ejemplos de Chainlit y se añadieron soluciones a problemas; resolución de importaciones mediante configuraciones del espacio de trabajo

### Corregido
- Problemas de importación resueltos:
  - El enrutador ya no depende de un módulo inexistente `utils`; las funciones están integradas
  - El coordinador utiliza importación relativa (`from .specialists import ...`) y se invoca mediante la ruta del módulo
  - Configuración de VS Code/Pylance para resolver importaciones de `chainlit` y paquetes
- Corrección de un pequeño error tipográfico en `STUDY_GUIDE.md` y se añadió cobertura del Módulo 08

### Eliminado
- Eliminado `Module08/infra/obs.py` no utilizado y se eliminó el directorio vacío `infra/`; los patrones de observabilidad se mantienen como opcionales en la documentación

### Movido
- Consolidación de las demostraciones del Módulo 08 bajo `Module08/samples` con carpetas numeradas por sesión
  - Aplicación de Chainlit movida a `samples/04`
  - Agentes movidos a `samples/05` y se añadieron archivos `__init__.py` para la resolución de paquetes

### Documentación
- Documentación de las sesiones del Módulo 08 y todos los READMEs de ejemplos enriquecidos con referencias de Microsoft Learn y proveedores confiables
- `Module08/README.md` actualizado con Resumen de Ejemplos, configuración del enrutador y consejos de validación
- Sección de Windows Foundry Local en `Module07/README.md` validada contra la documentación de Learn
- `STUDY_GUIDE.md` actualizado:
  - Añadido el Módulo 08 al resumen, horarios, rastreador de progreso
  - Sección de Referencias ampliada (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumen)
- Arquitectura del curso y módulos establecidos (Módulos 01–07)
- Modernización iterativa del contenido, estandarización de formato y casos de estudio añadidos
- Cobertura ampliada de marcos de optimización (Llama.cpp, Olive, OpenVINO, Apple MLX)

## No publicado / Pendiente (propuestas)
- Pruebas opcionales por ejemplo para validar la disponibilidad de Foundry Local
- Revisar traducciones para alinear referencias de modelos (por ejemplo, `phi-4-mini`) donde sea apropiado
- Añadir configuración mínima de pyright si los equipos prefieren estrictos a nivel de espacio de trabajo

---

