<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "906e890232c6c2e1dac4cccfeb449acd",
  "translation_date": "2025-09-24T11:32:44+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "es"
}
-->
# Registro de cambios

Todos los cambios importantes en EdgeAI para Principiantes están documentados aquí. Este proyecto utiliza entradas basadas en fechas y el estilo Keep a Changelog (Añadido, Cambiado, Corregido, Eliminado, Documentación, Movido).

## 2025-09-23

### Cambiado - Modernización importante del Módulo 08
- **Alineación integral con los patrones de repositorio Microsoft Foundry-Local**
  - Actualización de todos los ejemplos de código para usar `FoundryLocalManager` moderno e integración con OpenAI SDK
  - Sustitución de llamadas manuales obsoletas de `requests` por el uso adecuado del SDK
  - Alineación de patrones de implementación con la documentación oficial de Microsoft y ejemplos

- **Modernización de 05.AIPoweredAgents.md**:
  - Actualización de la orquestación multi-agente para usar patrones modernos de SDK
  - Mejora de la implementación del coordinador con características avanzadas (bucles de retroalimentación, monitoreo de rendimiento)
  - Adición de manejo de errores integral y verificación de salud del servicio
  - Integración de referencias adecuadas a ejemplos locales (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualización de ejemplos de llamadas a funciones para usar el parámetro moderno `tools` en lugar de `functions` obsoleto
  - Adición de patrones listos para producción con monitoreo y seguimiento de estadísticas

- **Reescritura completa de 06.ModelsAsTools.md**:
  - Sustitución del registro básico de herramientas por una implementación de enrutador de modelos inteligente
  - Adición de selección de modelos basada en palabras clave para diferentes tipos de tareas (general, razonamiento, código, creativo)
  - Integración de configuración basada en entorno con asignación flexible de modelos
  - Mejora con monitoreo integral de salud del servicio y manejo de errores
  - Adición de patrones de despliegue en producción con monitoreo de solicitudes y seguimiento de rendimiento
  - Alineación con la implementación local en `samples/06/router.py` y `samples/06/model_router.ipynb`

- **Mejoras en la estructura de la documentación**:
  - Adición de secciones de resumen destacando la modernización y alineación con el SDK
  - Mejora con emojis y mejor formato para mayor legibilidad
  - Inclusión de referencias adecuadas a archivos de ejemplos locales en toda la documentación
  - Inclusión de orientación para implementación en producción y mejores prácticas

### Añadido
- Secciones de resumen completas en los archivos del Módulo 08 destacando la integración moderna del SDK
- Resaltados de arquitectura mostrando características avanzadas (sistemas multi-agente, enrutamiento inteligente)
- Referencias directas a implementaciones de ejemplos locales para experiencia práctica
- Orientación para despliegue en producción con patrones de monitoreo y manejo de errores
- Ejemplos interactivos en Jupyter notebook con características avanzadas y benchmarks

### Corregido
- Discrepancias de alineación entre la documentación y las implementaciones reales de los ejemplos
- Patrones de uso del SDK obsoletos en todo el Módulo 08
- Referencias faltantes a la biblioteca de ejemplos locales integral
- Enfoques de implementación inconsistentes en diferentes secciones

---

## 2025-09-18

### Añadido
- Módulo 08: Microsoft Foundry Local – Kit de herramientas completo para desarrolladores
  - Seis sesiones: configuración, integración con Azure AI Foundry, modelos de código abierto, demostraciones avanzadas, agentes y modelos como herramientas
  - Ejemplos ejecutables bajo `Module08/samples/01`–`06` con instrucciones para cmd en Windows
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Inicio rápido del SDK con OpenAI/Foundry Local y soporte para Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista y benchmark (`list_and_bench.cmd`)
    - `04` Demostración de Chainlit (`app.py`)
    - `05` Orquestación multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Enrutador de Modelos como Herramientas (`router.py`)
- Soporte para Azure OpenAI en el ejemplo del SDK de la Sesión 2 con configuración de variables de entorno
- `.vscode/settings.json` apuntando a `Module08/.venv` para mejorar la resolución de análisis de Python
- `.env` con sugerencia de `PYTHONPATH` para la conciencia de VS Code/Pylance

### Cambiado
- Modelo predeterminado actualizado a `phi-4-mini` en toda la documentación y ejemplos del Módulo 08; eliminadas las menciones restantes de `phi-3.5` dentro del Módulo 08
- Mejoras en el enrutador (`Module08/samples/06/router.py`):
  - Descubrimiento de endpoints mediante `foundry service status` con análisis regex
  - Verificación de salud `/v1/models` al inicio
  - Registro de modelos configurable por entorno (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos actualizados: `Module08/requirements.txt` ahora incluye `openai` (junto con `requests`, `chainlit`)
- Orientación para el ejemplo de Chainlit aclarada y se añadió solución de problemas; resolución de importaciones mediante configuración del espacio de trabajo

### Corregido
- Problemas de importación resueltos:
  - El enrutador ya no depende de un módulo `utils` inexistente; las funciones están integradas
  - El coordinador utiliza importación relativa (`from .specialists import ...`) y se invoca mediante la ruta del módulo
  - Configuración de VS Code/Pylance para resolver `chainlit` y las importaciones de paquetes
- Corrección de un pequeño error tipográfico en `STUDY_GUIDE.md` y se añadió cobertura del Módulo 08

### Eliminado
- Eliminado `Module08/infra/obs.py` no utilizado y eliminado el directorio vacío `infra/`; los patrones de observabilidad se mantienen como opcionales en la documentación

### Movido
- Consolidación de las demostraciones del Módulo 08 bajo `Module08/samples` con carpetas numeradas por sesión
  - Aplicación de Chainlit movida a `samples/04`
  - Agentes movidos a `samples/05` y se añadieron archivos `__init__.py` para la resolución de paquetes

### Documentación
- Documentos de sesión del Módulo 08 y todos los READMEs de ejemplos enriquecidos con referencias de Microsoft Learn y proveedores confiables
- `Module08/README.md` actualizado con Resumen de Ejemplos, configuración del enrutador y consejos de validación
- Sección de Windows Foundry Local en `Module07/README.md` validada contra documentos de Learn
- `STUDY_GUIDE.md` actualizado:
  - Añadido el Módulo 08 al resumen, horarios, rastreador de progreso
  - Añadida sección de Referencias completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumen)
- Arquitectura del curso y módulos establecidos (Módulos 01–07)
- Modernización iterativa de contenido, estandarización de formato y casos de estudio añadidos
- Cobertura ampliada de marcos de optimización (Llama.cpp, Olive, OpenVINO, Apple MLX)

## No publicado / Pendiente (propuestas)
- Pruebas mínimas por ejemplo para validar la disponibilidad de Foundry Local
- Revisar traducciones para alinear referencias de modelos (por ejemplo, `phi-4-mini`) donde sea apropiado
- Añadir configuración mínima de pyright si los equipos prefieren estrictos a nivel de espacio de trabajo

---

