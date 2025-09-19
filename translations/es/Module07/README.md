<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-17T13:52:04+00:00",
  "source_file": "Module07/README.md",
  "language_code": "es"
}
-->
# Capítulo 07: Ejemplos de EdgeAI

Edge AI representa la convergencia de la inteligencia artificial con la computación en el borde, permitiendo procesamiento inteligente directamente en los dispositivos sin depender de la conectividad en la nube. Este capítulo explora cinco implementaciones distintas de EdgeAI en diferentes plataformas y frameworks, mostrando la versatilidad y el poder de ejecutar modelos de IA en el borde.

## 1. EdgeAI en NVIDIA Jetson Orin Nano

El NVIDIA Jetson Orin Nano representa un avance en la computación accesible de Edge AI, ofreciendo hasta 67 TOPS de rendimiento de IA en un formato compacto del tamaño de una tarjeta de crédito. Esta poderosa plataforma de Edge AI democratiza el desarrollo de IA generativa para aficionados, estudiantes y desarrolladores profesionales.

### Características principales
- Ofrece hasta 67 TOPS de rendimiento de IA, una mejora de 1.7X respecto a su predecesor
- 1024 núcleos CUDA y hasta 32 núcleos Tensor para procesamiento de IA
- CPU Arm Cortex-A78AE v8.2 de 64 bits con 6 núcleos y frecuencia máxima de 1.5 GHz
- Precio de solo $249, proporcionando a desarrolladores, estudiantes y creadores una plataforma asequible y accesible

### Aplicaciones
El Jetson Orin Nano sobresale en la ejecución de modelos modernos de IA generativa, incluidos transformadores de visión, modelos de lenguaje grande y modelos de visión-lenguaje. Está diseñado específicamente para casos de uso de GenAI y ahora puedes ejecutar varios LLMs en un dispositivo de tamaño compacto. Los casos de uso populares incluyen robótica impulsada por IA, drones inteligentes, cámaras inteligentes y dispositivos autónomos en el borde.

**Más información**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI en aplicaciones móviles con .NET MAUI y ONNX Runtime GenAI

Esta solución demuestra cómo integrar IA generativa y modelos de lenguaje grande (LLMs) en aplicaciones móviles multiplataforma utilizando .NET MAUI (Interfaz de Aplicación Multiplataforma) y ONNX Runtime GenAI. Este enfoque permite a los desarrolladores de .NET crear aplicaciones móviles sofisticadas impulsadas por IA que se ejecutan de forma nativa en dispositivos Android e iOS.

### Características principales
- Basado en el framework .NET MAUI, proporcionando una única base de código para aplicaciones Android e iOS
- Integración de ONNX Runtime GenAI que permite ejecutar modelos de IA generativa directamente en dispositivos móviles
- Compatible con varios aceleradores de hardware adaptados para dispositivos móviles, incluidos CPU, GPU y procesadores de IA especializados
- Optimizaciones específicas de la plataforma como CoreML para iOS y NNAPI para Android a través de ONNX Runtime
- Implementa el ciclo completo de IA generativa, incluyendo pre y post procesamiento, inferencia, procesamiento de logits, búsqueda y muestreo, y gestión de caché KV

### Beneficios para el desarrollo
El enfoque de .NET MAUI permite a los desarrolladores aprovechar sus habilidades existentes en C# y .NET mientras crean aplicaciones de IA multiplataforma. El framework ONNX Runtime GenAI admite múltiples arquitecturas de modelos, incluidos Llama, Mistral, Phi, Gemma y muchos otros. Los núcleos ARM64 optimizados aceleran la multiplicación de matrices INT4 cuantizadas, asegurando un rendimiento eficiente en hardware móvil mientras se mantiene la experiencia familiar de desarrollo en .NET.

### Casos de uso
Esta solución es ideal para desarrolladores que desean crear aplicaciones móviles impulsadas por IA utilizando tecnologías .NET, incluyendo chatbots inteligentes, aplicaciones de reconocimiento de imágenes, herramientas de traducción de idiomas y sistemas de recomendación personalizados que se ejecutan completamente en el dispositivo para mayor privacidad y capacidad offline.

**Más información**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI en Azure con motor de modelos de lenguaje pequeño

La solución EdgeAI basada en Azure de Microsoft se centra en implementar modelos de lenguaje pequeño (SLMs) de manera eficiente en entornos híbridos de nube y borde. Este enfoque conecta los servicios de IA a escala en la nube con los requisitos de implementación en el borde.

### Ventajas de la arquitectura
- Integración perfecta con los servicios de Azure AI
- Ejecuta SLMs/LLMs y modelos multimodales en el dispositivo y en la nube con ONNX Runtime
- Optimizado para implementaciones a escala empresarial
- Soporte para actualizaciones y gestión continua de modelos

### Casos de uso
La implementación de EdgeAI en Azure sobresale en escenarios que requieren despliegues de IA de nivel empresarial con capacidades de gestión en la nube. Esto incluye procesamiento inteligente de documentos, análisis en tiempo real y flujos de trabajo híbridos de IA que aprovechan tanto la computación en la nube como en el borde.

**Más información**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI con Windows ML

Windows ML representa el runtime de vanguardia de Microsoft optimizado para inferencia de modelos en el dispositivo y despliegue simplificado, sirviendo como la base de Windows AI Foundry. Esta plataforma permite a los desarrolladores crear aplicaciones de Windows impulsadas por IA que aprovechan todo el espectro del hardware de PC.

### Capacidades de la plataforma
- Funciona en todos los PCs con Windows 11 que ejecuten la versión 24H2 (build 26100) o superior
- Compatible con todo el hardware de PC x64 y ARM64, incluso PCs sin NPUs o GPUs
- Permite a los desarrolladores traer sus propios modelos y desplegarlos eficientemente en el ecosistema de socios de silicio, incluyendo AMD, Intel, NVIDIA y Qualcomm, abarcando CPU, GPU, NPU
- Aprovechando APIs de infraestructura, los desarrolladores ya no necesitan crear múltiples versiones de su aplicación para diferentes silicios

### Beneficios para desarrolladores
Windows ML abstrae el hardware y los proveedores de ejecución, permitiéndote concentrarte en escribir tu código. Además, Windows ML se actualiza automáticamente para admitir las últimas NPUs, GPUs y CPUs a medida que se lanzan. La plataforma proporciona un marco unificado para el desarrollo de IA en el diverso ecosistema de hardware de Windows.

**Más información**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Guía completa para el desarrollo de Edge AI en Windows

## 5. EdgeAI con aplicaciones locales de Foundry

Foundry Local permite a los desarrolladores construir aplicaciones de Generación Aumentada por Recuperación (RAG) utilizando recursos locales en .NET, combinando modelos de lenguaje locales con capacidades de búsqueda semántica. Este enfoque proporciona soluciones de IA centradas en la privacidad que operan completamente en infraestructura local.

### Arquitectura técnica
- Combina el modelo de lenguaje Phi-3, Embeddings locales y Kernel semántico para crear un escenario RAG
- Utiliza embeddings como vectores (arreglos) de valores de punto flotante que representan contenido y su significado semántico
- El Kernel semántico actúa como el principal orquestador, integrando Phi-3 y Componentes Inteligentes para crear un pipeline RAG fluido
- Soporte para bases de datos vectoriales locales, incluyendo SQLite y Qdrant

### Beneficios de implementación
RAG, o Generación Aumentada por Recuperación, es simplemente una forma elegante de decir "buscar información y ponerla en el prompt". Esta implementación local asegura la privacidad de los datos mientras proporciona respuestas inteligentes basadas en bases de conocimiento personalizadas. El enfoque es particularmente valioso para escenarios empresariales que requieren soberanía de datos y capacidades de operación offline.

**Más información**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Recursos de desarrollo de Windows EdgeAI

Para desarrolladores que se centran específicamente en la plataforma Windows, hemos creado una guía completa que cubre todo el ecosistema de Windows EdgeAI. Este recurso proporciona información detallada sobre Windows AI Foundry, incluyendo APIs, herramientas y mejores prácticas para el desarrollo de EdgeAI en Windows.

### Plataforma Windows AI Foundry
La plataforma Windows AI Foundry ofrece un conjunto completo de herramientas y APIs diseñadas específicamente para el desarrollo de Edge AI en dispositivos Windows. Esto incluye soporte especializado para hardware acelerado por NPU, integración de Windows ML y técnicas de optimización específicas de la plataforma.

**Guía completa**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Esta guía cubre:
- Descripción general y componentes de la plataforma Windows AI Foundry
- API Phi Silica para inferencia eficiente en hardware NPU
- APIs de visión por computadora para procesamiento de imágenes y OCR
- Integración y optimización del runtime Windows ML
- CLI de Foundry Local para desarrollo y pruebas locales
- Estrategias de optimización de hardware para dispositivos Windows
- Ejemplos prácticos de implementación y mejores prácticas

### Toolkit de IA para desarrollo de Edge AI
Para desarrolladores que usan Visual Studio Code, la extensión AI Toolkit proporciona un entorno de desarrollo completo diseñado específicamente para construir, probar y desplegar aplicaciones de Edge AI. Este toolkit simplifica todo el flujo de trabajo de desarrollo de Edge AI dentro de VS Code.

**Guía de desarrollo**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

La guía del AI Toolkit cubre:
- Descubrimiento y selección de modelos para despliegue en el borde
- Flujos de trabajo de prueba y optimización local
- Integración de ONNX y Ollama para modelos en el borde
- Técnicas de conversión y cuantización de modelos
- Desarrollo de agentes para escenarios en el borde
- Evaluación de rendimiento y monitoreo
- Preparación para despliegue y mejores prácticas

## Conclusión

Estas cinco implementaciones de EdgeAI demuestran la madurez y diversidad de las soluciones de IA en el borde disponibles hoy en día. Desde dispositivos acelerados por hardware como el Jetson Orin Nano hasta frameworks de software como ONNX Runtime GenAI y Windows ML, los desarrolladores tienen opciones sin precedentes para desplegar aplicaciones inteligentes en el borde.

El hilo común entre todas estas plataformas es la democratización de las capacidades de IA, haciendo accesible el aprendizaje automático sofisticado a desarrolladores de diferentes niveles de habilidad y casos de uso. Ya sea construyendo aplicaciones móviles, software de escritorio o sistemas embebidos, estas soluciones de EdgeAI proporcionan la base para la próxima generación de aplicaciones inteligentes que operan de manera eficiente y privada en el borde.

Cada plataforma ofrece ventajas únicas: Jetson Orin Nano para computación acelerada por hardware en el borde, ONNX Runtime GenAI para desarrollo móvil multiplataforma, Azure EdgeAI para integración empresarial nube-borde, Windows ML para aplicaciones nativas de Windows y Foundry Local para implementaciones RAG centradas en la privacidad. Juntas, representan un ecosistema integral para el desarrollo de EdgeAI.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.