<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T12:51:04+00:00",
  "source_file": "Module08/README.md",
  "language_code": "es"
}
-->
# Módulo 08: Práctica con Microsoft Foundry Local - Kit Completo para Desarrolladores

## Descripción General

Microsoft Foundry Local representa la próxima generación en desarrollo de IA en el borde, proporcionando a los desarrolladores herramientas poderosas para construir, implementar y escalar aplicaciones de IA localmente, mientras se mantiene una integración fluida con Azure AI Foundry. Este módulo ofrece una cobertura completa de Foundry Local, desde la instalación hasta el desarrollo avanzado de agentes.

**Tecnologías Clave:**
- CLI y SDK de Microsoft Foundry Local
- Integración con Azure AI Foundry
- Inferencia de modelos en el dispositivo
- Caché y optimización de modelos locales
- Arquitecturas basadas en agentes

## Objetivos de Aprendizaje del Módulo

Al completar este módulo, podrás:

- **Dominar la Configuración de Foundry Local**: Instalar, configurar y optimizar Foundry Local para desarrollo en Windows 11.
- **Implementar Modelos Diversos**: Ejecutar modelos phi, qwen, deepseek y GPT-OSS-20B localmente con comandos CLI.
- **Crear Soluciones de Producción**: Desarrollar aplicaciones de IA con ingeniería avanzada de prompts e integración de datos.
- **Aprovechar el Ecosistema Open-Source**: Integrar modelos de Hugging Face y contribuciones de la comunidad.
- **Comparar Arquitecturas de IA**: Entender las diferencias entre LLMs y SLMs, y sus estrategias de implementación.
- **Desarrollar Agentes de IA**: Construir agentes inteligentes utilizando la arquitectura y capacidades de grounding de Foundry Local.
- **Implementar Modelos como Herramientas**: Crear soluciones de IA modulares y personalizables para aplicaciones empresariales.

## Estructura de las Sesiones

### [1: Introducción a Foundry Local](./01.FoundryLocalSetup.md)
**Enfoque**: Instalación, configuración de CLI, caché de modelos y aceleración de hardware.

**Lo que Aprenderás:**
- Instalación completa de Foundry Local en Windows 11.
- Configuración de CLI y estructura de comandos.
- Estrategias de caché de modelos para un rendimiento óptimo.
- Configuración y optimización de aceleración de hardware.
- Implementación práctica de modelos phi, qwen, deepseek y GPT-OSS-20B.

**Duración**: 2-3 horas  
**Requisitos Previos**: Windows 11, conocimientos básicos de línea de comandos.

---

### [2: Construir Soluciones de IA con Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Enfoque**: Ingeniería avanzada de prompts, integración de datos y tareas accionables.

**Lo que Aprenderás:**
- Técnicas avanzadas de ingeniería de prompts.
- Patrones de integración de datos y mejores prácticas.
- Construcción de tareas accionables de IA con Foundry Local.
- Flujos de trabajo de integración fluida con Azure AI Foundry.
- Optimización y monitoreo del rendimiento.

**Duración**: 2-3 horas  
**Requisitos Previos**: Completar la sesión 1, cuenta de Azure (opcional).

---

### [3: Modelos Open-Source en Foundry Local](./03.OpenSourceModels.md)
**Enfoque**: Integración con Hugging Face, estrategias de selección de modelos y contribuciones de la comunidad.

**Lo que Aprenderás:**
- Integración de modelos de Hugging Face con Foundry Local.
- Estrategias e implementación de "trae tu propio modelo" (BYOM).
- Perspectivas de la serie Model Mondays y contribuciones de la comunidad.
- Implementación y optimización de modelos personalizados.
- Criterios de evaluación y selección de modelos de la comunidad.

**Duración**: 2-3 horas  
**Requisitos Previos**: Completar las sesiones 1-2, cuenta de Hugging Face.

---

### [4: Explorar Modelos de Vanguardia - LLMs, SLMs e Inferencia en el Dispositivo](./04.CuttingEdgeModels.md)
**Enfoque**: Comparación de modelos, EdgeAI con Phi y ONNX Runtime, demostraciones avanzadas.

**Lo que Aprenderás:**
- Comparación completa entre LLMs y SLMs y sus casos de uso.
- Trade-offs entre inferencia local y en la nube, y marcos de decisión.
- Implementación de EdgeAI con Phi y ONNX Runtime.
- Desarrollo e implementación de la aplicación Chainlit RAG Chat.
- Técnicas de optimización de inferencia con WebGPU.
- Integración y capacidades del SDK de AI PC.

**Duración**: 3-4 horas  
**Requisitos Previos**: Completar las sesiones 1-3, comprensión de conceptos de inferencia.

---

### [5: Construir Agentes Impulsados por IA Rápidamente con Foundry Local](./05.AIPoweredAgents.md)
**Enfoque**: Desarrollo rápido de aplicaciones GenAI, prompts del sistema, grounding y arquitecturas de agentes.

**Lo que Aprenderás:**
- Arquitectura de agentes de Foundry Local y patrones de diseño.
- Ingeniería de prompts del sistema para el comportamiento de agentes.
- Técnicas de grounding para respuestas confiables de agentes.
- Flujos de trabajo para desarrollo rápido de aplicaciones GenAI.
- Orquestación de agentes y sistemas multi-agente.
- Estrategias de implementación en producción para agentes de IA.

**Duración**: 3-4 horas  
**Requisitos Previos**: Completar las sesiones 1-4, comprensión básica de agentes de IA.

---

### [6: Foundry Local - Modelos como Herramientas](./06.ModelsAsTools.md)
**Enfoque**: Soluciones de IA modulares, implementación en el dispositivo y escalabilidad empresarial.

**Lo que Aprenderás:**
- Tratar los modelos de IA como herramientas modulares y personalizables.
- Implementación en el dispositivo sin dependencia de la nube.
- Inferencia de baja latencia, eficiente en costos y preservación de la privacidad.
- Patrones de integración con SDK, API y CLI.
- Personalización de modelos para casos de uso específicos.
- Estrategias de escalabilidad desde local hasta Azure AI Foundry.
- Arquitecturas de aplicaciones de IA listas para empresas.

**Duración**: 3-4 horas  
**Requisitos Previos**: Todas las sesiones anteriores, experiencia en desarrollo empresarial útil.

## Requisitos Previos

### Requisitos del Sistema
- **Sistema Operativo**: Windows 11 (22H2 o posterior).
- **Memoria**: 16GB RAM (32GB recomendados para modelos más grandes).
- **Almacenamiento**: 50GB de espacio libre para caché de modelos.
- **Hardware**: Dispositivo con NPU recomendado (Copilot+ PC), GPU opcional.
- **Red**: Internet de alta velocidad para descargas iniciales de modelos.

### Entorno de Desarrollo
- Visual Studio Code con la extensión AI Toolkit.
- Python 3.10+ y pip.
- Git para control de versiones.
- PowerShell o Command Prompt.
- Azure CLI (opcional para integración en la nube).

### Conocimientos Previos
- Comprensión básica de conceptos de IA/ML.
- Familiaridad con línea de comandos.
- Conocimientos básicos de programación en Python.
- Conceptos de REST API.
- Conocimiento básico de prompts e inferencia de modelos.

## Cronograma del Módulo

**Tiempo Estimado Total**: 15-20 horas

| Sesión | Área de Enfoque | Tiempo | Complejidad |
|--------|-----------------|--------|-------------|
|  1 | Configuración y Conceptos Básicos | 2-3 horas | Principiante |
|  2 | Soluciones de IA | 2-3 horas | Intermedio |
|  3 | Open Source | 2-3 horas | Intermedio |
|  4 | Modelos Avanzados | 3-4 horas | Avanzado |
|  5 | Agentes de IA | 3-4 horas | Avanzado |
|  6 | Herramientas Empresariales | 3-4 horas | Experto |

## Recursos Clave

### Documentación Principal
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Documentación de Azure AI Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Serie Model Mondays](https://aka.ms/model-mondays)

### Recursos Comunitarios
- [Discusiones de la Comunidad Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Ejemplos de Azure AI Foundry](https://github.com/Azure-Samples/ai-foundry)
- [Comunidad de Desarrolladores de Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence)

## Resultados de Aprendizaje

Al completar este módulo, estarás preparado para:

### Dominio Técnico
- **Implementar y Gestionar**: Instalaciones de Foundry Local en entornos de desarrollo y producción.
- **Integrar Modelos**: Trabajar sin problemas con diversas familias de modelos de Microsoft, Hugging Face y fuentes comunitarias.
- **Crear Aplicaciones**: Desarrollar aplicaciones de IA listas para producción con características avanzadas y optimizaciones.
- **Desarrollar Agentes**: Implementar agentes de IA sofisticados con grounding, razonamiento e integración de herramientas.

### Comprensión Estratégica
- **Decisiones de Arquitectura**: Tomar decisiones informadas entre implementación local y en la nube.
- **Optimización de Rendimiento**: Optimizar el rendimiento de inferencia en diferentes configuraciones de hardware.
- **Escalabilidad Empresarial**: Diseñar aplicaciones que escalen desde prototipos locales hasta implementaciones empresariales.
- **Privacidad y Seguridad**: Implementar soluciones de IA que preserven la privacidad con inferencia local.

### Capacidades de Innovación
- **Prototipado Rápido**: Construir y probar conceptos de aplicaciones de IA rápidamente.
- **Integración Comunitaria**: Aprovechar modelos open-source y contribuir al ecosistema.
- **Patrones Avanzados**: Implementar patrones de IA de vanguardia, incluyendo RAG, agentes e integración de herramientas.
- **Desarrollo Preparado para el Futuro**: Crear aplicaciones listas para tecnologías y patrones emergentes de IA.

## Cómo Empezar

1. **Prepara tu Entorno**: Asegúrate de tener Windows 11 con las especificaciones de hardware recomendadas.
2. **Instala los Requisitos Previos**: Configura herramientas de desarrollo y dependencias.
3. **Comienza con la Sesión 1**: Inicia con la instalación y configuración básica de Foundry Local.
4. **Avanza Secuencialmente**: Completa las sesiones en orden para una progresión óptima de aprendizaje.
5. **Practica Continuamente**: Aplica los conceptos a través de ejercicios prácticos y proyectos.

## Métricas de Éxito

Rastrea tu progreso a través del módulo:

- [ ] Instalar y configurar Foundry Local exitosamente.
- [ ] Implementar y ejecutar al menos 4 familias de modelos diferentes.
- [ ] Construir una solución completa de IA con integración de datos.
- [ ] Integrar al menos 2 modelos open-source.
- [ ] Crear una aplicación funcional de chat RAG.
- [ ] Desarrollar e implementar un agente de IA.
- [ ] Implementar una arquitectura de modelos como herramientas.

## Inicio Rápido para Ejemplos

### 1) Configuración del entorno (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Iniciar un modelo local (nueva terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Ejecutar la demo de Chainlit (Sesión 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Ejecutar el coordinador multi-agente (Sesión 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Si ves errores de conexión, valida Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Configuración del router (Sesión 6)
El router realiza una verificación rápida de salud y admite configuración basada en entorno:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Este módulo representa lo último en desarrollo de IA en el borde, combinando herramientas de nivel empresarial de Microsoft con la flexibilidad e innovación del ecosistema open-source. Al dominar Foundry Local, estarás posicionado a la vanguardia del desarrollo de aplicaciones de IA.

Para Azure OpenAI (Sesión 2), consulta el README de ejemplo para las variables de entorno requeridas y configuraciones de versión de API.

## Resumen de Ejemplos

- `samples/01`: Chat REST rápido con Foundry Local (`chat_quickstart.py`).
- `samples/02`: Integración con OpenAI SDK (`sdk_quickstart.py`).
- `samples/03`: Descubrimiento de modelos + benchmark rápido (`list_and_bench.cmd`).
- `samples/04`: Demo de Chainlit RAG (`app.py`).
- `samples/05`: Orquestación multi-agente (`python -m samples.05.agents.coordinator`).
- `samples/06`: Router de modelos como herramientas (`python samples\06\router.py`).

---

