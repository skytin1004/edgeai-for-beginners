<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cbc822b7b1c0af38342e07c36b8cf0c4",
  "translation_date": "2025-10-08T20:30:37+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "es"
}
-->
# Registro de cambios

Todos los cambios importantes en EdgeAI para Principiantes están documentados aquí. Este proyecto utiliza entradas basadas en fechas y el estilo Keep a Changelog (Añadido, Cambiado, Corregido, Eliminado, Documentación, Movido).

## 2025-10-08

### Añadido - Actualización integral del taller
- **Reescritura completa de README.md del taller**:
  - Se añadió una introducción completa explicando la propuesta de valor de Edge AI (privacidad, rendimiento, costo).
  - Se crearon 6 objetivos de aprendizaje principales con competencias detalladas.
  - Se añadió una tabla de resultados de aprendizaje con entregables y matriz de competencias.
  - Se incluyó una sección de habilidades listas para el mercado laboral para relevancia en la industria.
  - Se añadió una guía de inicio rápido con requisitos previos y configuración en 3 pasos.
  - Se crearon tablas de recursos para ejemplos en Python (8 archivos con tiempos de ejecución).
  - Se añadió una tabla de notebooks Jupyter (8 notebooks con niveles de dificultad).
  - Se creó una tabla de documentación (7 documentos clave con orientación sobre "Cuándo usar").
  - Se añadieron recomendaciones de rutas de aprendizaje para diferentes niveles de habilidad.

- **Infraestructura de validación y pruebas del taller**:
  - Se creó `scripts/validate_samples.py` - Herramienta integral de validación para sintaxis, importaciones y mejores prácticas.
  - Se creó `scripts/test_samples.py` - Ejecutador de pruebas rápidas para todos los ejemplos en Python.
  - Se añadió documentación de validación a `scripts/README.md`.

- **Documentación integral**:
  - Se creó `SAMPLES_UPDATE_SUMMARY.md` - Guía detallada de más de 400 líneas que cubre todas las mejoras.
  - Se creó `UPDATE_COMPLETE.md` - Resumen ejecutivo de la finalización de la actualización.
  - Se creó `QUICK_REFERENCE.md` - Tarjeta de referencia rápida para el taller.

### Cambiado - Modernización de ejemplos en Python del taller
- **Actualización de los 8 ejemplos en Python con mejores prácticas**:
  - Manejo de errores mejorado con bloques try-except en todas las operaciones de entrada/salida.
  - Se añadieron sugerencias de tipos y docstrings completos.
  - Implementación de un patrón de registro consistente [INFO]/[ERROR]/[RESULT].
  - Protección de importaciones opcionales con sugerencias de instalación.
  - Mejora en la retroalimentación al usuario en todos los ejemplos.

- **session01/chat_bootstrap.py**:
  - Inicialización del cliente mejorada con mensajes de error detallados.
  - Manejo de errores en streaming mejorado con validación de fragmentos.
  - Se añadió un manejo de excepciones más robusto para la falta de disponibilidad del servicio.

- **session02/rag_pipeline.py**:
  - Se añadieron protecciones de importación para sentence-transformers con sugerencias de instalación.
  - Manejo de errores mejorado en operaciones de generación y embeddings.
  - Formateo de salida mejorado con resultados estructurados.

- **session02/rag_eval_ragas.py**:
  - Protección de importaciones opcionales (ragas, datasets) con mensajes de error amigables.
  - Manejo de errores añadido para métricas de evaluación.
  - Formateo de salida mejorado para resultados de evaluación.

- **session03/benchmark_oss_models.py**:
  - Implementación de degradación elegante (continúa en caso de fallos de modelos).
  - Reporte de progreso detallado y manejo de errores por modelo.
  - Cálculo de estadísticas mejorado con recuperación integral de errores.

- **session04/model_compare.py**:
  - Se añadieron sugerencias de tipos (tipos de retorno Tuple).
  - Formateo de salida mejorado con resultados JSON estructurados.
  - Manejo de errores por modelo implementado con recuperación.

- **session05/agents_orchestrator.py**:
  - Se mejoró Agent.act() con docstrings completos.
  - Manejo de errores en la tubería añadido con registro etapa por etapa.
  - Gestión de memoria y seguimiento de estado mejorados.

- **session06/models_router.py**:
  - Documentación de funciones mejorada para todos los componentes de enrutamiento.
  - Registro detallado añadido en la función route().
  - Salida de prueba mejorada con resultados estructurados.

- **session06/models_pipeline.py**:
  - Manejo de errores añadido a la función auxiliar chat().
  - pipeline() mejorado con registro de etapas y reporte de progreso.
  - main() mejorado con recuperación integral de errores.

### Documentación - Mejora de la documentación del taller
- README.md principal actualizado con una sección del taller destacando la ruta de aprendizaje práctico.
- STUDY_GUIDE.md mejorado con una sección completa del taller que incluye:
  - Objetivos de aprendizaje y áreas de enfoque de estudio.
  - Preguntas de autoevaluación.
  - Ejercicios prácticos con estimaciones de tiempo.
  - Asignación de tiempo para estudio concentrado y a tiempo parcial.
  - Se añadió el taller a la plantilla de seguimiento de progreso.
- Guía de asignación de tiempo actualizada de 20 horas a 30 horas (incluyendo el taller).
- Descripciones de ejemplos del taller y resultados de aprendizaje añadidos a README.

### Corregido
- Resueltos patrones inconsistentes de manejo de errores en los ejemplos del taller.
- Corregidos errores de importación de dependencias opcionales con protecciones adecuadas.
- Se añadieron sugerencias de tipos faltantes en funciones críticas.
- Se abordó la insuficiente retroalimentación al usuario en escenarios de error.
- Problemas de validación corregidos con infraestructura de pruebas integral.

---

## 2025-09-23

### Cambiado - Modernización importante del Módulo 08
- **Alineación integral con patrones del repositorio Microsoft Foundry-Local**:
  - Actualización de todos los ejemplos de código para usar `FoundryLocalManager` moderno e integración con OpenAI SDK.
  - Sustitución de llamadas manuales obsoletas a `requests` por uso adecuado del SDK.
  - Alineación de patrones de implementación con documentación oficial de Microsoft y ejemplos.

- **Modernización de 05.AIPoweredAgents.md**:
  - Orquestación de múltiples agentes actualizada para usar patrones modernos de SDK.
  - Implementación del coordinador mejorada con características avanzadas (bucles de retroalimentación, monitoreo de rendimiento).
  - Manejo de errores integral y verificación de salud del servicio añadidos.
  - Referencias adecuadas integradas a ejemplos locales (`samples/05/multi_agent_orchestration.ipynb`).
  - Ejemplos de llamadas a funciones actualizados para usar el parámetro moderno `tools` en lugar de `functions` obsoleto.
  - Patrones listos para producción añadidos con monitoreo y seguimiento de estadísticas.

- **Reescritura completa de 06.ModelsAsTools.md**:
  - Sustitución del registro básico de herramientas por implementación de enrutador inteligente de modelos.
  - Selección de modelos basada en palabras clave para diferentes tipos de tareas (general, razonamiento, código, creativo).
  - Configuración basada en entorno integrada con asignación flexible de modelos.
  - Mejorado con monitoreo integral de salud del servicio y manejo de errores.
  - Patrones de despliegue en producción añadidos con monitoreo de solicitudes y seguimiento de rendimiento.
  - Alineado con implementación local en `samples/06/router.py` y `samples/06/model_router.ipynb`.

- **Mejoras en la estructura de documentación**:
  - Se añadieron secciones de resumen destacando la modernización y alineación con SDK.
  - Mejorado con emojis y mejor formato para mayor legibilidad.
  - Referencias adecuadas añadidas a archivos de ejemplos locales en toda la documentación.
  - Incluida orientación para implementación en producción y mejores prácticas.

### Añadido
- Secciones de resumen completas en los archivos del Módulo 08 destacando la integración moderna con SDK.
- Aspectos destacados de arquitectura mostrando características avanzadas (sistemas multi-agente, enrutamiento inteligente).
- Referencias directas a implementaciones de ejemplos locales para experiencia práctica.
- Orientación para despliegue en producción con patrones de monitoreo y manejo de errores.
- Ejemplos interactivos en notebooks Jupyter con características avanzadas y benchmarks.

### Corregido
- Discrepancias de alineación entre la documentación y las implementaciones reales de los ejemplos.
- Patrones de uso de SDK obsoletos en todo el Módulo 08.
- Referencias faltantes a la biblioteca de ejemplos locales integral.
- Enfoques de implementación inconsistentes en diferentes secciones.

---

## 2025-09-18

### Añadido
- Módulo 08: Microsoft Foundry Local – Kit de herramientas completo para desarrolladores
  - Seis sesiones: configuración, integración con Azure AI Foundry, modelos de código abierto, demos de vanguardia, agentes y modelos como herramientas.
  - Ejemplos ejecutables bajo `Module08/samples/01`–`06` con instrucciones para cmd en Windows:
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Inicio rápido con SDK de OpenAI/Foundry Local y soporte para Azure OpenAI (`sdk_quickstart.py`)
    - `03` Lista y benchmark en CLI (`list_and_bench.cmd`)
    - `04` Demo de Chainlit (`app.py`)
    - `05` Orquestación de múltiples agentes (`python -m samples.05.agents.coordinator`)
    - `06` Enrutador de modelos como herramientas (`router.py`)
- Soporte para Azure OpenAI en el ejemplo de SDK de la sesión 2 con configuración de variables de entorno.
- `.vscode/settings.json` apuntando a `Module08/.venv` para mejorar la resolución de análisis en Python.
- `.env` con sugerencia de `PYTHONPATH` para reconocimiento en VS Code/Pylance.

### Cambiado
- Modelo predeterminado actualizado a `phi-4-mini` en toda la documentación y ejemplos del Módulo 08; se eliminaron las menciones restantes de `phi-3.5` dentro del Módulo 08.
- Mejoras en el enrutador (`Module08/samples/06/router.py`):
  - Descubrimiento de endpoints mediante `foundry service status` con análisis regex.
  - Verificación de salud `/v1/models` al inicio.
  - Registro de modelos configurable por entorno (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON).
- Requisitos actualizados: `Module08/requirements.txt` ahora incluye `openai` (junto con `requests`, `chainlit`).
- Guía de muestra de Chainlit aclarada y solución de problemas añadida; resolución de importaciones mediante configuración del espacio de trabajo.

### Corregido
- Problemas de importación resueltos:
  - El enrutador ya no depende de un módulo `utils` inexistente; las funciones están integradas.
  - El coordinador utiliza importación relativa (`from .specialists import ...`) y se invoca mediante la ruta del módulo.
  - Configuración de VS Code/Pylance para resolver `chainlit` e importaciones de paquetes.
- Tipos menores corregidos en `STUDY_GUIDE.md` y cobertura del Módulo 08 añadida.

### Eliminado
- Se eliminó `Module08/infra/obs.py` no utilizado y se eliminó el directorio vacío `infra/`; los patrones de observabilidad se retienen como opcionales en la documentación.

### Movido
- Demos del Módulo 08 consolidadas bajo `Module08/samples` con carpetas numeradas por sesión.
  - Aplicación de Chainlit movida a `samples/04`.
  - Agentes movidos a `samples/05` y se añadieron archivos `__init__.py` para resolución de paquetes.

### Documentación
- Documentos de sesión del Módulo 08 y todos los READMEs de ejemplos enriquecidos con referencias de Microsoft Learn y proveedores confiables.
- `Module08/README.md` actualizado con descripción general de ejemplos, configuración del enrutador y consejos de validación.
- Sección de Foundry Local en Windows del `Module07/README.md` validada contra documentos de Learn.
- `STUDY_GUIDE.md` actualizado:
  - Se añadió el Módulo 08 al resumen, horarios y rastreador de progreso.
  - Se añadió una sección de Referencias completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML).

---

## Histórico (resumen)
- Arquitectura del curso y módulos establecidos (Módulos 01–07).
- Modernización iterativa de contenido, estandarización de formato y casos de estudio añadidos.
- Cobertura ampliada de marcos de optimización (Llama.cpp, Olive, OpenVINO, Apple MLX).

## No publicado / Pendiente (propuestas)
- Pruebas rápidas opcionales por ejemplo para validar la disponibilidad de Foundry Local.
- Revisar traducciones para alinear referencias de modelos (por ejemplo, `phi-4-mini`) donde sea apropiado.
- Añadir configuración mínima de pyright si los equipos prefieren estrictos a nivel de espacio de trabajo.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.