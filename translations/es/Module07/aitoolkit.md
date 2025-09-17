<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-17T13:56:59+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "es"
}
-->
# Guía de Desarrollo de Edge AI con AI Toolkit para Visual Studio Code

## Introducción

Bienvenido a la guía completa para usar AI Toolkit en Visual Studio Code en el desarrollo de Edge AI. A medida que la inteligencia artificial se traslada de la computación centralizada en la nube a dispositivos distribuidos en el borde, los desarrolladores necesitan herramientas integradas y potentes que puedan manejar los desafíos únicos del despliegue en el borde, desde las limitaciones de recursos hasta los requisitos de operación sin conexión.

AI Toolkit para Visual Studio Code cierra esta brecha al proporcionar un entorno de desarrollo completo diseñado específicamente para construir, probar y optimizar aplicaciones de inteligencia artificial que funcionen eficientemente en dispositivos del borde. Ya sea que estés desarrollando para sensores IoT, dispositivos móviles, sistemas embebidos o servidores en el borde, este conjunto de herramientas simplifica todo tu flujo de trabajo de desarrollo dentro del entorno familiar de VS Code.

Esta guía te llevará a través de los conceptos esenciales, herramientas y mejores prácticas para aprovechar AI Toolkit en tus proyectos de Edge AI, desde la selección inicial del modelo hasta el despliegue en producción.

## Resumen

AI Toolkit ofrece un entorno de desarrollo integrado para todo el ciclo de vida de las aplicaciones de Edge AI dentro de VS Code. Proporciona integración fluida con modelos de inteligencia artificial populares de proveedores como OpenAI, Anthropic, Google y GitHub, mientras que también admite el despliegue local de modelos a través de ONNX y Ollama, capacidades cruciales para aplicaciones de Edge AI que requieren inferencia en el dispositivo.

Lo que distingue a AI Toolkit para el desarrollo de Edge AI es su enfoque en toda la tubería de despliegue en el borde. A diferencia de las herramientas tradicionales de desarrollo de IA que se centran principalmente en el despliegue en la nube, AI Toolkit incluye características especializadas para la optimización de modelos, pruebas en condiciones de recursos limitados y evaluación de rendimiento específica para el borde. El conjunto de herramientas entiende que el desarrollo de Edge AI requiere consideraciones diferentes: tamaños de modelos más pequeños, tiempos de inferencia más rápidos, capacidad sin conexión y optimizaciones específicas de hardware.

La plataforma admite múltiples escenarios de despliegue, desde inferencia simple en el dispositivo hasta arquitecturas complejas de múltiples modelos en el borde. Proporciona herramientas para la conversión, cuantización y optimización de modelos que son esenciales para un despliegue exitoso en el borde, mientras mantiene la productividad del desarrollador que caracteriza a VS Code.

## Objetivos de Aprendizaje

Al final de esta guía, serás capaz de:

### Competencias Básicas
- **Instalar y configurar** AI Toolkit para Visual Studio Code en flujos de trabajo de desarrollo de Edge AI
- **Navegar y utilizar** la interfaz de AI Toolkit, incluyendo el Catálogo de Modelos, Playground y Agent Builder
- **Seleccionar y evaluar** modelos de IA adecuados para el despliegue en el borde según el rendimiento y las limitaciones de recursos
- **Convertir y optimizar** modelos utilizando el formato ONNX y técnicas de cuantización para dispositivos del borde

### Habilidades de Desarrollo de Edge AI
- **Diseñar e implementar** aplicaciones de Edge AI utilizando el entorno de desarrollo integrado
- **Realizar pruebas de modelos** en condiciones similares al borde utilizando inferencia local y monitoreo de recursos
- **Crear y personalizar** agentes de IA optimizados para escenarios de despliegue en el borde
- **Evaluar el rendimiento de modelos** utilizando métricas relevantes para la computación en el borde (latencia, uso de memoria, precisión)

### Optimización y Despliegue
- **Aplicar técnicas de cuantización y poda** para reducir el tamaño del modelo mientras se mantiene un rendimiento aceptable
- **Optimizar modelos** para plataformas de hardware específicas del borde, incluyendo aceleración por CPU, GPU y NPU
- **Implementar mejores prácticas** para el desarrollo de Edge AI, incluyendo gestión de recursos y estrategias de respaldo
- **Preparar modelos y aplicaciones** para el despliegue en producción en dispositivos del borde

### Conceptos Avanzados de Edge AI
- **Integrar con frameworks de Edge AI** como ONNX Runtime, Windows ML y TensorFlow Lite
- **Implementar arquitecturas de múltiples modelos** y escenarios de aprendizaje federado para entornos del borde
- **Solucionar problemas comunes de Edge AI** como limitaciones de memoria, velocidad de inferencia y compatibilidad de hardware
- **Diseñar estrategias de monitoreo y registro** para aplicaciones de Edge AI en producción

### Aplicación Práctica
- **Construir soluciones completas de Edge AI** desde la selección del modelo hasta el despliegue
- **Demostrar competencia** en flujos de trabajo de desarrollo específicos del borde y técnicas de optimización
- **Aplicar conceptos aprendidos** a casos de uso reales de Edge AI, incluyendo IoT, móvil y aplicaciones embebidas
- **Evaluar y comparar** diferentes estrategias de despliegue en el borde y sus compensaciones

## Características Clave para el Desarrollo de Edge AI

### 1. Catálogo de Modelos y Descubrimiento
- **Soporte de Modelos Locales**: Descubre y accede a modelos de IA específicamente optimizados para el despliegue en el borde
- **Integración con ONNX**: Accede a modelos en formato ONNX para inferencia eficiente en el borde
- **Soporte de Ollama**: Aprovecha modelos que se ejecutan localmente a través de Ollama para privacidad y operación sin conexión
- **Comparación de Modelos**: Compara modelos lado a lado para encontrar el equilibrio óptimo entre rendimiento y consumo de recursos para dispositivos del borde

### 2. Playground Interactivo
- **Entorno de Pruebas Locales**: Prueba modelos localmente antes del despliegue en el borde
- **Experimentación Multimodal**: Prueba con imágenes, texto y otros tipos de entrada típicos en escenarios del borde
- **Ajuste de Parámetros**: Experimenta con diferentes parámetros de modelos para optimizar las limitaciones del borde
- **Monitoreo de Rendimiento en Tiempo Real**: Observa la velocidad de inferencia y el uso de recursos durante el desarrollo

### 3. Constructor de Agentes para Aplicaciones en el Borde
- **Ingeniería de Prompts**: Crea prompts optimizados que funcionen eficientemente con modelos más pequeños del borde
- **Integración con Herramientas MCP**: Integra herramientas de Model Context Protocol para capacidades mejoradas de agentes en el borde
- **Generación de Código**: Genera código listo para producción optimizado para escenarios de despliegue en el borde
- **Salidas Estructuradas**: Diseña agentes que proporcionen respuestas consistentes y estructuradas adecuadas para aplicaciones en el borde

### 4. Evaluación y Pruebas de Modelos
- **Métricas de Rendimiento**: Evalúa modelos utilizando métricas relevantes para el despliegue en el borde (latencia, uso de memoria, precisión)
- **Pruebas por Lotes**: Prueba múltiples configuraciones de modelos simultáneamente para encontrar configuraciones óptimas en el borde
- **Evaluación Personalizada**: Crea criterios de evaluación personalizados específicos para casos de uso de Edge AI
- **Perfil de Recursos**: Analiza los requisitos de memoria y computación para la planificación del despliegue en el borde

### 5. Conversión y Optimización de Modelos
- **Conversión a ONNX**: Convierte modelos de varios formatos a ONNX para compatibilidad en el borde
- **Cuantización**: Reduce el tamaño del modelo y mejora la velocidad de inferencia mediante técnicas de cuantización
- **Optimización de Hardware**: Optimiza modelos para hardware específico del borde (CPU, GPU, NPU)
- **Transformación de Formatos**: Transforma modelos de Hugging Face y otras fuentes para el despliegue en el borde

### 6. Ajuste Fino para Escenarios del Borde
- **Adaptación de Dominio**: Personaliza modelos para casos de uso y entornos específicos del borde
- **Entrenamiento Local**: Entrena modelos localmente con soporte de GPU para requisitos específicos del borde
- **Integración con Azure**: Aprovecha Azure Container Apps para ajuste fino basado en la nube antes del despliegue en el borde
- **Aprendizaje por Transferencia**: Adapta modelos preentrenados para tareas y limitaciones específicas del borde

### 7. Monitoreo y Trazabilidad de Rendimiento
- **Análisis de Rendimiento en el Borde**: Monitorea el rendimiento de modelos en condiciones similares al borde
- **Recopilación de Trazas**: Recopila datos detallados de rendimiento para optimización
- **Identificación de Cuellos de Botella**: Identifica problemas de rendimiento antes del despliegue en dispositivos del borde
- **Seguimiento de Uso de Recursos**: Monitorea memoria, CPU y tiempo de inferencia para optimización en el borde

## Flujo de Trabajo de Desarrollo de Edge AI

### Fase 1: Descubrimiento y Selección de Modelos
1. **Explorar el Catálogo de Modelos**: Utiliza el catálogo de modelos para encontrar modelos adecuados para el despliegue en el borde
2. **Comparar Rendimiento**: Evalúa modelos según tamaño, precisión y velocidad de inferencia
3. **Pruebas Locales**: Usa modelos de Ollama o ONNX para pruebas locales antes del despliegue en el borde
4. **Evaluar Requisitos de Recursos**: Determina las necesidades de memoria y computación para los dispositivos del borde objetivo

### Fase 2: Optimización de Modelos
1. **Convertir a ONNX**: Convierte modelos seleccionados al formato ONNX para compatibilidad en el borde
2. **Aplicar Cuantización**: Reduce el tamaño del modelo mediante cuantización INT8 o INT4
3. **Optimización de Hardware**: Optimiza para hardware específico del borde (ARM, x86, aceleradores especializados)
4. **Validación de Rendimiento**: Valida que los modelos optimizados mantengan una precisión aceptable

### Fase 3: Desarrollo de Aplicaciones
1. **Diseño de Agentes**: Usa Agent Builder para crear agentes de IA optimizados para el borde
2. **Ingeniería de Prompts**: Desarrolla prompts que funcionen eficazmente con modelos más pequeños del borde
3. **Pruebas de Integración**: Prueba agentes en condiciones simuladas del borde
4. **Generación de Código**: Genera código de producción optimizado para el despliegue en el borde

### Fase 4: Evaluación y Pruebas
1. **Evaluación por Lotes**: Prueba múltiples configuraciones para encontrar configuraciones óptimas en el borde
2. **Perfil de Rendimiento**: Analiza velocidad de inferencia, uso de memoria y precisión
3. **Simulación en el Borde**: Prueba en condiciones similares al entorno de despliegue en el borde
4. **Pruebas de Estrés**: Evalúa el rendimiento bajo diversas condiciones de carga

### Fase 5: Preparación para el Despliegue
1. **Optimización Final**: Aplica optimizaciones finales basadas en los resultados de las pruebas
2. **Empaquetado para Despliegue**: Empaqueta modelos y código para el despliegue en el borde
3. **Documentación**: Documenta los requisitos de despliegue y configuración
4. **Configuración de Monitoreo**: Prepara el monitoreo y registro para el despliegue en producción

## Público Objetivo para el Desarrollo de Edge AI

### Desarrolladores de Edge AI
- Desarrolladores de aplicaciones que construyen dispositivos del borde e IoT con capacidades de IA
- Desarrolladores de sistemas embebidos que integran capacidades de IA en dispositivos con recursos limitados
- Desarrolladores móviles que crean aplicaciones de IA en el dispositivo para smartphones y tablets

### Ingenieros de Edge AI
- Ingenieros de IA que optimizan modelos para el despliegue en el borde y gestionan tuberías de inferencia
- Ingenieros de DevOps que despliegan y gestionan modelos de IA en infraestructuras distribuidas del borde
- Ingenieros de rendimiento que optimizan cargas de trabajo de IA para las limitaciones de hardware del borde

### Investigadores y Educadores
- Investigadores de IA que desarrollan modelos y algoritmos eficientes para la computación en el borde
- Educadores que enseñan conceptos de Edge AI y demuestran técnicas de optimización
- Estudiantes que aprenden sobre los desafíos y soluciones en el despliegue de Edge AI

## Casos de Uso de Edge AI

### Dispositivos IoT Inteligentes
- **Reconocimiento de Imágenes en Tiempo Real**: Despliega modelos de visión por computadora en cámaras y sensores IoT
- **Procesamiento de Voz**: Implementa reconocimiento de voz y procesamiento de lenguaje natural en altavoces inteligentes
- **Mantenimiento Predictivo**: Ejecuta modelos de detección de anomalías en dispositivos industriales del borde
- **Monitoreo Ambiental**: Despliega modelos de análisis de datos de sensores para aplicaciones ambientales

### Aplicaciones Móviles y Embebidas
- **Traducción en el Dispositivo**: Implementa modelos de traducción de idiomas que funcionan sin conexión
- **Realidad Aumentada**: Despliega reconocimiento y seguimiento de objetos en tiempo real para aplicaciones de RA
- **Monitoreo de Salud**: Ejecuta modelos de análisis de salud en dispositivos portátiles y equipos médicos
- **Sistemas Autónomos**: Implementa modelos de toma de decisiones para drones, robots y vehículos

### Infraestructura de Computación en el Borde
- **Centros de Datos en el Borde**: Despliega modelos de IA en centros de datos del borde para aplicaciones de baja latencia
- **Integración con CDN**: Integra capacidades de procesamiento de IA en redes de entrega de contenido
- **Edge 5G**: Aprovecha la computación en el borde 5G para aplicaciones impulsadas por IA
- **Computación en la Niebla**: Implementa procesamiento de IA en entornos de computación en la niebla

## Instalación y Configuración

### Instalación Rápida
Instala la extensión AI Toolkit directamente desde el Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Requisitos Previos para el Desarrollo de Edge AI
- **ONNX Runtime**: Instala ONNX Runtime para la inferencia de modelos
- **Ollama** (Opcional): Instala Ollama para servir modelos localmente
- **Entorno de Python**: Configura Python con las bibliotecas de IA requeridas
- **Herramientas de Hardware del Borde**: Instala herramientas de desarrollo específicas de hardware (CUDA, OpenVINO, etc.)

### Configuración Inicial
1. Abre VS Code e instala la extensión AI Toolkit
2. Configura las fuentes de modelos (ONNX, Ollama, proveedores en la nube)
3. Configura el entorno de desarrollo local para pruebas en el borde
4. Configura opciones de aceleración de hardware para tu máquina de desarrollo

## Primeros Pasos con el Desarrollo de Edge AI

### Paso 1: Selección de Modelos
1. Abre la vista de AI Toolkit en la Barra de Actividades
2. Navega por el Catálogo de Modelos para modelos compatibles con el borde
3. Filtra por tamaño de modelo, formato (ONNX) y características de rendimiento
4. Compara modelos utilizando las herramientas de comparación integradas

### Paso 2: Pruebas Locales
1. Usa el Playground para probar modelos seleccionados localmente
2. Experimenta con diferentes prompts y parámetros
3. Monitorea métricas de rendimiento durante las pruebas
4. Evalúa las respuestas de los modelos para los requisitos del caso de uso en el borde

### Paso 3: Optimización de Modelos
1. Usa las herramientas de Conversión de Modelos para optimizar el despliegue en el borde
2. Aplica cuantización para reducir el tamaño del modelo
3. Prueba modelos optimizados para garantizar un rendimiento aceptable
4. Documenta configuraciones de optimización y compensaciones de rendimiento

### Paso 4: Desarrollo de Agentes
1. Usa Agent Builder para crear agentes de IA optimizados para el borde
2. Desarrolla prompts que funcionen eficazmente con modelos más pequeños
3. Integra herramientas y APIs necesarias para escenarios del borde
4. Prueba agentes en condiciones simuladas del borde

### Paso 5: Evaluación y Despliegue
1. Usa evaluación masiva para probar múltiples configuraciones
2. Perfila el rendimiento bajo diversas condiciones
3. Prepara paquetes de despliegue para dispositivos del borde objetivo
4. Configura monitoreo y registro para el despliegue en producción

## Mejores Prácticas para el Desarrollo de Edge AI

### Selección de Modelos
- **Restricciones de Tamaño**: Elige modelos que se ajusten a las limitaciones de memoria de los dispositivos objetivo
- **Velocidad de Inferencia**: Prioriza modelos con tiempos de inferencia rápidos para aplicaciones en tiempo real
- **Compensaciones de Precisión**: Equilibra la precisión del modelo con las limitaciones de recursos
- **Compatibilidad de Formatos**: Prefiere formatos ONNX o optimizados para hardware para el despliegue en el borde

### Técnicas de Optimización
- **Cuantización**: Usa cuantización INT8 o INT4 para reducir el tamaño del modelo y mejorar la velocidad
- **Poda**: Elimina parámetros innecesarios del modelo para reducir los requisitos computacionales
- **Destilación de Conocimiento**: Crea modelos más pequeños que mantengan el rendimiento de los más grandes
- **Aceleración de Hardware**: Aprovecha NPUs, GPUs o aceleradores especializados cuando estén disponibles

### Flujo de Trabajo de Desarrollo
- **Pruebas Iterativas**: Prueba frecuentemente en condiciones similares al borde durante el desarrollo
- **Monitoreo de Rendimiento**: Monitorea continuamente el uso de recursos y la velocidad de inferencia
- **Control de Versiones**: Rastrea versiones de modelos y configuraciones de optimización
- **Documentación**: Documenta todas las decisiones de optimización y compensaciones de rendimiento

### Consideraciones de Despliegue
- **Monitoreo de Recursos**: Monitorea memoria, CPU y uso de energía en producción
- **Estrategias de Respaldo**: Implementa mecanismos de respaldo para fallos de modelos
- **Mecanismos de Actualización**: Planifica actualizaciones de modelos y gestión de versiones
- **Seguridad**: Implementar medidas de seguridad adecuadas para aplicaciones de IA en el borde

## Integración con Frameworks de IA en el Borde

### ONNX Runtime
- **Despliegue Multiplataforma**: Implementar modelos ONNX en diferentes plataformas de borde
- **Optimización de Hardware**: Aprovechar las optimizaciones específicas de hardware de ONNX Runtime
- **Soporte Móvil**: Usar ONNX Runtime Mobile para aplicaciones en smartphones y tablets
- **Integración con IoT**: Desplegar en dispositivos IoT utilizando las distribuciones ligeras de ONNX Runtime

### Windows ML
- **Dispositivos Windows**: Optimizar para dispositivos de borde y PCs basados en Windows
- **Aceleración NPU**: Aprovechar las Unidades de Procesamiento Neural en dispositivos Windows
- **DirectML**: Usar DirectML para aceleración en GPU en plataformas Windows
- **Integración UWP**: Integrar con aplicaciones de la Plataforma Universal de Windows

### TensorFlow Lite
- **Optimización Móvil**: Implementar modelos de TensorFlow Lite en dispositivos móviles y embebidos
- **Delegados de Hardware**: Usar delegados de hardware especializados para aceleración
- **Microcontroladores**: Desplegar en microcontroladores utilizando TensorFlow Lite Micro
- **Soporte Multiplataforma**: Implementar en sistemas Android, iOS y Linux embebido

### Azure IoT Edge
- **Híbrido Nube-Borde**: Combinar entrenamiento en la nube con inferencia en el borde
- **Despliegue de Módulos**: Implementar modelos de IA como módulos de IoT Edge
- **Gestión de Dispositivos**: Administrar dispositivos de borde y actualizaciones de modelos de forma remota
- **Telemetría**: Recopilar datos de rendimiento y métricas de modelos desde despliegues en el borde

## Escenarios Avanzados de IA en el Borde

### Despliegue Multimodelo
- **Conjuntos de Modelos**: Implementar múltiples modelos para mejorar la precisión o redundancia
- **Pruebas A/B**: Probar diferentes modelos simultáneamente en dispositivos de borde
- **Selección Dinámica**: Elegir modelos según las condiciones actuales del dispositivo
- **Compartición de Recursos**: Optimizar el uso de recursos entre múltiples modelos desplegados

### Aprendizaje Federado
- **Entrenamiento Distribuido**: Entrenar modelos en múltiples dispositivos de borde
- **Preservación de Privacidad**: Mantener los datos de entrenamiento locales mientras se comparten mejoras de modelos
- **Aprendizaje Colaborativo**: Permitir que los dispositivos aprendan de experiencias colectivas
- **Coordinación Borde-Nube**: Coordinar el aprendizaje entre dispositivos de borde y la infraestructura en la nube

### Procesamiento en Tiempo Real
- **Procesamiento de Flujos**: Procesar flujos continuos de datos en dispositivos de borde
- **Inferencia de Baja Latencia**: Optimizar para una latencia mínima en la inferencia
- **Procesamiento por Lotes**: Procesar eficientemente lotes de datos en dispositivos de borde
- **Procesamiento Adaptativo**: Ajustar el procesamiento según las capacidades actuales del dispositivo

## Solución de Problemas en el Desarrollo de IA en el Borde

### Problemas Comunes
- **Restricciones de Memoria**: Modelo demasiado grande para la memoria del dispositivo objetivo
- **Velocidad de Inferencia**: Inferencia del modelo demasiado lenta para requisitos en tiempo real
- **Degradación de Precisión**: La optimización reduce la precisión del modelo de manera inaceptable
- **Compatibilidad de Hardware**: Modelo no compatible con el hardware objetivo

### Estrategias de Depuración
- **Perfilado de Rendimiento**: Usar las funciones de trazado del Toolkit de IA para identificar cuellos de botella
- **Monitoreo de Recursos**: Supervisar el uso de memoria y CPU durante el desarrollo
- **Pruebas Incrementales**: Probar optimizaciones de manera incremental para aislar problemas
- **Simulación de Hardware**: Usar herramientas de desarrollo para simular el hardware objetivo

### Soluciones de Optimización
- **Cuantización Adicional**: Aplicar técnicas de cuantización más agresivas
- **Arquitectura del Modelo**: Considerar diferentes arquitecturas de modelos optimizadas para el borde
- **Optimización de Preprocesamiento**: Optimizar el preprocesamiento de datos para las restricciones del borde
- **Optimización de Inferencia**: Usar optimizaciones de inferencia específicas de hardware

## Recursos y Próximos Pasos

### Documentación
- [Guía de Modelos del Toolkit de IA](https://code.visualstudio.com/docs/intelligentapps/models)
- [Documentación del Playground de Modelos](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Documentación de ONNX Runtime](https://onnxruntime.ai/)
- [Documentación de Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Comunidad y Soporte
- [GitHub del Toolkit de IA para VS Code](https://github.com/microsoft/vscode-ai-toolkit)
- [Comunidad ONNX](https://github.com/onnx/onnx)
- [Comunidad de Desarrolladores de IA en el Borde](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Marketplace de Extensiones de VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Recursos de Aprendizaje
- [Curso de Fundamentos de IA en el Borde](./Module01/README.md)
- [Guía de Modelos de Lenguaje Pequeños](./Module02/README.md)
- [Estrategias de Despliegue en el Borde](./Module03/README.md)
- [Desarrollo de IA en el Borde para Windows](./windowdeveloper.md)

## Conclusión

El Toolkit de IA para Visual Studio Code proporciona una plataforma integral para el desarrollo de IA en el borde, desde el descubrimiento y la optimización de modelos hasta el despliegue y la monitorización. Al aprovechar sus herramientas y flujos de trabajo integrados, los desarrolladores pueden crear, probar y desplegar aplicaciones de IA de manera eficiente que funcionen eficazmente en dispositivos de borde con recursos limitados.

El soporte del Toolkit para ONNX, Ollama y varios proveedores de nube, combinado con sus capacidades de optimización y evaluación, lo convierte en una opción ideal para el desarrollo de IA en el borde. Ya sea que estés construyendo aplicaciones IoT, funciones de IA móvil o sistemas de inteligencia embebida, el Toolkit de IA proporciona las herramientas y flujos de trabajo necesarios para un despliegue exitoso de IA en el borde.

A medida que la IA en el borde sigue evolucionando, el Toolkit de IA para VS Code se mantiene a la vanguardia, proporcionando a los desarrolladores herramientas y capacidades de última generación para construir la próxima generación de aplicaciones inteligentes en el borde.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.