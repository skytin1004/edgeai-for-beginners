<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec4ff1735cf3d48aed41d924c0a0ff29",
  "translation_date": "2025-10-03T08:21:23+00:00",
  "source_file": "AGENTS.md",
  "language_code": "es"
}
-->
# AGENTS.md

## Resumen del Proyecto

EdgeAI para Principiantes es un repositorio educativo integral que enseña el desarrollo de Edge AI con Modelos de Lenguaje Pequeños (SLMs). El curso abarca fundamentos de EdgeAI, implementación de modelos, técnicas de optimización e implementaciones listas para producción utilizando Microsoft Foundry Local y varios marcos de inteligencia artificial.

**Tecnologías Clave:**
- Python 3.8+ (lenguaje principal para ejemplos de IA/ML)
- .NET C# (ejemplos de IA/ML)
- JavaScript/Node.js con Electron (para aplicaciones de escritorio)
- SDK de Microsoft Foundry Local
- Microsoft Windows ML 
- VSCode AI Toolkit
- SDK de OpenAI
- Marcos de IA: LangChain, Semantic Kernel, Chainlit
- Optimización de Modelos: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo de Repositorio:** Repositorio de contenido educativo con 8 módulos y 10 aplicaciones de muestra completas

**Arquitectura:** Ruta de aprendizaje de múltiples módulos con ejemplos prácticos que demuestran patrones de implementación de Edge AI

## Estructura del Repositorio

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

## Comandos de Configuración

### Configuración del Repositorio

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configuración de Ejemplos en Python (Módulo08 y ejemplos en Python)

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

### Configuración de Ejemplos en Node.js (Ejemplo 08 - Aplicación de Chat en Windows)

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

### Configuración de Foundry Local

Foundry Local es necesario para ejecutar los ejemplos del Módulo08:

```bash
# Start Foundry Local service with a model
foundry model run phi-4-mini

# Verify service is running
curl http://localhost:8000/health
```

## Flujo de Trabajo de Desarrollo

### Desarrollo de Contenido

Este repositorio contiene principalmente **contenido educativo en Markdown**. Al realizar cambios:

1. Edita los archivos `.md` en los directorios de módulos correspondientes.
2. Sigue los patrones de formato existentes.
3. Asegúrate de que los ejemplos de código sean precisos y estén probados.
4. Actualiza el contenido traducido correspondiente si es necesario (o deja que la automatización lo maneje).

### Desarrollo de Aplicaciones de Muestra

Para ejemplos en Python (ejemplos 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para el ejemplo en Electron (ejemplo 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pruebas de Aplicaciones de Muestra

Los ejemplos en Python no tienen pruebas automatizadas, pero pueden validarse ejecutándolos:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

El ejemplo en Electron tiene infraestructura de pruebas:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrucciones de Pruebas

### Validación de Contenido

El repositorio utiliza flujos de trabajo de traducción automatizados. No se requieren pruebas manuales para las traducciones.

**Validación manual para cambios de contenido:**
1. Revisa la renderización de Markdown previsualizando los archivos `.md`.
2. Verifica que todos los enlaces apunten a destinos válidos.
3. Prueba cualquier fragmento de código incluido en la documentación.
4. Asegúrate de que las imágenes se carguen correctamente.

### Pruebas de Aplicaciones de Muestra

**El módulo08/ejemplos/08 (aplicación Electron) tiene pruebas completas:**
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

**Los ejemplos en Python deben probarse manualmente:**
```bash
# Each sample can be run directly
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py
```

## Directrices de Estilo de Código

### Contenido en Markdown

- Usa una jerarquía de encabezados consistente (# para título, ## para secciones principales, ### para subsecciones).
- Incluye bloques de código con especificadores de lenguaje: ```python, ```bash, ```javascript.
- Sigue el formato existente para tablas, listas y énfasis.
- Mantén las líneas legibles (apunta a ~80-100 caracteres, pero no es estricto).
- Usa enlaces relativos para referencias internas.

### Estilo de Código en Python

- Sigue las convenciones de PEP 8.
- Usa sugerencias de tipo cuando sea apropiado.
- Incluye docstrings para funciones y clases.
- Usa nombres de variables significativos.
- Mantén las funciones enfocadas y concisas.

### Estilo de Código en JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenciones clave:**
- Configuración de ESLint proporcionada en el ejemplo 08.
- Prettier para formato de código.
- Usa sintaxis moderna ES6+.
- Sigue los patrones existentes en la base de código.

## Directrices para Pull Requests

### Formato del Título
```
[ModuleXX] Brief description of change
```
o
```
[Module08/samples/XX] Description for sample changes
```

### Antes de Enviar

**Para cambios de contenido:**
- Previsualiza todos los archivos Markdown modificados.
- Verifica que los enlaces e imágenes funcionen.
- Revisa errores tipográficos y gramaticales.

**Para cambios en el código de ejemplo (Módulo08/ejemplos/08):**
```bash
npm run lint
npm test
```

**Para cambios en ejemplos de Python:**
- Prueba que el ejemplo se ejecute correctamente.
- Verifica que el manejo de errores funcione.
- Comprueba la compatibilidad con Foundry Local.

### Proceso de Revisión

- Los cambios en contenido educativo se revisan por precisión y claridad.
- Los ejemplos de código se prueban para verificar su funcionalidad.
- Las actualizaciones de traducción se manejan automáticamente mediante GitHub Actions.

## Sistema de Traducción

**IMPORTANTE:** Este repositorio utiliza traducción automatizada mediante GitHub Actions.

- Las traducciones están en el directorio `/translations/` (más de 50 idiomas).
- Automatizado mediante el flujo de trabajo `co-op-translator.yml`.
- **NO edites manualmente los archivos de traducción** - serán sobrescritos.
- Edita solo los archivos fuente en inglés en los directorios raíz y de módulos.
- Las traducciones se generan automáticamente al hacer push a la rama `main`.

## Integración de Foundry Local

La mayoría de los ejemplos del Módulo08 requieren que Microsoft Foundry Local esté en ejecución:

### Iniciar Foundry Local
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

### Verificar Foundry Local
```bash
# Check service health
curl http://127.0.0.1:55769/

# the Port and PID will be displayed when running `foundry service start`

# List loaded models
curl http://localhost:55769/v1/models
```

### Variables de Entorno para Ejemplos

La mayoría de los ejemplos utilizan estas variables de entorno:
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

## Construcción e Implementación

### Implementación de Contenido

Este repositorio es principalmente documentación - no se requiere proceso de construcción para el contenido.

### Construcción de Aplicaciones de Muestra

**Aplicación Electron (Módulo08/ejemplos/08):**
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

**Ejemplos en Python:**
No se requiere proceso de construcción - los ejemplos se ejecutan directamente con el intérprete de Python.

## Problemas Comunes y Solución de Problemas

### Foundry Local No Está Ejecutándose
**Problema:** Los ejemplos fallan con errores de conexión.

**Solución:**
```bash
# Start Foundry Local service
foundry model run phi-4-mini

# Verify it's running
curl http://localhost:55769/health
```

### Problemas con Entornos Virtuales de Python
**Problema:** Errores de importación de módulos.

**Solución:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Problemas de Construcción en Electron
**Problema:** Fallos en npm install o en la construcción.

**Solución:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Conflictos en el Flujo de Trabajo de Traducción
**Problema:** Conflictos en el PR de traducción con tus cambios.

**Solución:**
- Edita solo los archivos fuente en inglés.
- Deja que el flujo de trabajo de traducción automatizado maneje las traducciones.
- Si ocurren conflictos, fusiona `main` en tu rama después de que las traducciones sean fusionadas.

## Recursos Adicionales

### Rutas de Aprendizaje
- **Ruta para Principiantes:** Módulos 01-02 (7-9 horas).
- **Ruta Intermedia:** Módulos 03-04 (9-11 horas).
- **Ruta Avanzada:** Módulos 05-07 (12-15 horas).
- **Ruta Experta:** Módulo 08 (8-10 horas).

### Contenido Clave de los Módulos
- **Módulo01:** Fundamentos de EdgeAI y estudios de caso reales.
- **Módulo02:** Familias y arquitecturas de Modelos de Lenguaje Pequeños (SLM).
- **Módulo03:** Estrategias de implementación local y en la nube.
- **Módulo04:** Optimización de modelos con múltiples marcos.
- **Módulo05:** SLMOps - operaciones en producción.
- **Módulo06:** Agentes de IA y llamadas a funciones.
- **Módulo07:** Implementaciones específicas de plataformas.
- **Módulo08:** Herramientas de Foundry Local con 10 ejemplos completos.

### Dependencias Externas
- [Microsoft Foundry Local](https://foundry.microsoft.com/) - Runtime local de modelos de IA.
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Marco de optimización.
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Kit de herramientas de optimización de modelos.
- [OpenVINO](https://docs.openvino.ai/) - Kit de herramientas de optimización de Intel.

## Notas Específicas del Proyecto

### Aplicaciones de Muestra del Módulo08

El repositorio incluye 10 aplicaciones de muestra completas:

1. **01-REST Chat Quickstart** - Integración básica del SDK de OpenAI.
2. **02-OpenAI SDK Integration** - Funciones avanzadas del SDK.
3. **03-Model Discovery & Benchmarking** - Herramientas de comparación de modelos.
4. **04-Chainlit RAG Application** - Generación aumentada por recuperación.
5. **05-Multi-Agent Orchestration** - Coordinación básica de agentes.
6. **06-Models-as-Tools Router** - Enrutamiento inteligente de modelos.
7. **07-Direct API Client** - Integración de API de bajo nivel.
8. **08-Windows 11 Chat App** - Aplicación de escritorio nativa en Electron.
9. **09-Advanced Multi-Agent System** - Orquestación compleja de agentes.
10. **10-Foundry Tools Framework** - Integración de LangChain/Semantic Kernel.

Cada ejemplo demuestra diferentes aspectos del desarrollo de Edge AI con Foundry Local.

### Consideraciones de Rendimiento

- Los SLMs están optimizados para implementación en el borde (2-16GB RAM).
- La inferencia local proporciona tiempos de respuesta de 50-500ms.
- Las técnicas de cuantización logran una reducción del tamaño del 75% con una retención del rendimiento del 85%.
- Capacidades de conversación en tiempo real con modelos locales.

### Seguridad y Privacidad

- Todo el procesamiento ocurre localmente - no se envían datos a la nube.
- Adecuado para aplicaciones sensibles a la privacidad (salud, finanzas).
- Cumple con los requisitos de soberanía de datos.
- Foundry Local se ejecuta completamente en hardware local.

---

**Este es un repositorio educativo enfocado en enseñar el desarrollo de Edge AI. El patrón principal de contribución es mejorar el contenido educativo y agregar/mejorar aplicaciones de muestra que demuestren conceptos de Edge AI.**

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.