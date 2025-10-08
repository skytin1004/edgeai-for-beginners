<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T20:39:30+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "es"
}
-->
# Actualizaciones del SDK Local de Foundry

## Resumen

Se han actualizado los notebooks y utilidades del Workshop para utilizar correctamente el **SDK oficial de Python de Foundry Local**, siguiendo los patrones de:
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Archivos Modificados

### 1. `Workshop/samples/workshop_utils.py`

**Cambios:**
- ✅ Añadido manejo de errores de importación para el paquete `foundry-local-sdk`
- ✅ Documentación mejorada con patrones oficiales del SDK
- ✅ Registro mejorado con símbolos Unicode (✓, ✗, ⚠)
- ✅ Añadidos docstrings completos con ejemplos
- ✅ Mensajes de error más detallados que hacen referencia a comandos CLI
- ✅ Comentarios actualizados para coincidir con la documentación oficial del SDK

**Mejoras Clave:**

#### Manejo de Errores de Importación
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### Función Mejorada `get_client()`
- Documentación detallada sobre el patrón de inicialización del SDK
- Aclaración de que `FoundryLocalManager` inicia el servicio automáticamente
- Explicación de la resolución de alias de modelos a variantes optimizadas para hardware
- Registro mejorado con información del endpoint
- Mensajes de error más útiles con sugerencias de pasos de solución de problemas

#### Función Mejorada `chat_once()`
- Añadido docstring completo con ejemplos de uso
- Aclarada la compatibilidad con el SDK de OpenAI
- Documentado soporte de streaming (a través de kwargs)
- Mensajes de error mejorados con sugerencias de comandos CLI
- Añadidas notas sobre la verificación de disponibilidad de modelos

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**Cambios:**
- ✅ Actualizadas todas las celdas de markdown con referencias al SDK
- ✅ Comentarios de código mejorados con explicaciones de patrones del SDK
- ✅ Documentación y explicaciones de celdas mejoradas
- ✅ Añadida guía de solución de problemas
- ✅ Actualizado catálogo de modelos (reemplazado 'gpt-oss-20b' por 'phi-3.5-mini')
- ✅ Formateo de salida mejorado con indicadores visuales
- ✅ Añadidos enlaces y referencias al SDK en todo el notebook

**Actualizaciones Celda por Celda:**

#### Celda 1 (Título)
- Añadidos enlaces a la documentación del SDK
- Referenciados repositorios oficiales de GitHub

#### Celda 2 (Escenario)
- Reformateado con pasos numerados
- Aclarado el patrón de enrutamiento basado en intención
- Enfatizados los beneficios de la ejecución local

#### Celda 3 (Instalación de Dependencias)
- Añadida explicación de lo que proporciona cada paquete
- Documentadas capacidades del SDK (resolución de alias, optimización de hardware)

#### Celda 4 (Configuración del Entorno)
- Docstrings de funciones mejorados
- Comentarios en línea añadidos explicando patrones del SDK
- Documentada la estructura del catálogo de modelos
- Aclarada la coincidencia de prioridad/capacidad

#### Celda 5 (Verificación del Catálogo)
- Añadidas marcas visuales (✓)
- Salida mejor formateada

#### Celda 6 (Prueba de Detección de Intención)
- Salida reformateada como estilo tabla
- Muestra tanto la intención como el modelo seleccionado

#### Celda 7 (Función de Enrutamiento)
- Explicación completa del patrón del SDK
- Documentado el flujo de inicialización
- Listadas todas las características (reintento, seguimiento, errores)
- Añadido enlace de referencia al SDK

#### Celda 8 (Demostración por Lotes)
- Explicación mejorada de lo que se espera
- Añadida sección de solución de problemas
- Incluidos comandos CLI para depuración
- Salida mejor formateada

### 3. `Workshop/notebooks/session06_README.md` (Nuevo Archivo)

**Documentación completa creada que cubre:**

1. **Resumen**: Diagrama de arquitectura y explicación de componentes
2. **Integración del SDK**: Ejemplos de código siguiendo patrones oficiales
3. **Requisitos Previos**: Instrucciones paso a paso para la configuración
4. **Uso**: Cómo ejecutar y personalizar el notebook
5. **Alias de Modelos**: Explicación de variantes optimizadas para hardware
6. **Solución de Problemas**: Problemas comunes y soluciones
7. **Extensión**: Cómo añadir intenciones, modelos y lógica personalizada
8. **Consejos de Rendimiento**: Mejores prácticas para uso en producción
9. **Recursos**: Enlaces a documentación oficial y comunidad

## Implementación de Patrones del SDK

### Patrón Oficial (de la documentación de Foundry Local)

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### Nuestra Implementación (en workshop_utils)

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**Beneficios de Nuestra Aproximación:**
- ✅ Sigue exactamente el patrón oficial del SDK
- ✅ Añade caché para evitar inicializaciones repetidas
- ✅ Incluye lógica de reintento para mayor robustez en producción
- ✅ Soporta seguimiento de uso de tokens
- ✅ Proporciona mejores mensajes de error
- ✅ Permanece compatible con ejemplos oficiales

## Cambios en el Catálogo de Modelos

### Antes
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### Después
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**Razón:** Se reemplazó 'gpt-oss-20b' (alias no estándar) por 'phi-3.5-mini' (alias oficial de Foundry Local).

## Dependencias

### Archivo requirements.txt Actualizado

El archivo requirements.txt del Workshop ya incluye:
```
foundry-local-sdk
openai>=1.30.0
```

Estos son los únicos paquetes necesarios para la integración con Foundry Local.

## Pruebas de las Actualizaciones

### 1. Verificar que Foundry Local está en Ejecución

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. Comprobar Modelos Disponibles

```bash
foundry model ls
```

Asegúrate de que estos modelos estén disponibles o se descarguen automáticamente:
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. Ejecutar el Notebook

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

O abrir en VS Code y ejecutar todas las celdas.

### 4. Comportamiento Esperado

**Celda 1 (Instalación):** Instala los paquetes correctamente  
**Celda 2 (Configuración):** Sin errores, las importaciones funcionan  
**Celda 3 (Verificación):** Muestra ✓ con la lista de modelos  
**Celda 4 (Prueba de Intención):** Muestra resultados de detección de intención  
**Celda 5 (Enrutador):** Muestra ✓ Función de enrutamiento lista  
**Celda 6 (Ejecutar):** Enruta los prompts a los modelos y muestra resultados  

### 5. Solución de Problemas de Errores de Conexión

Si ves `APIConnectionError: Connection error`:

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## Variables de Entorno

Las siguientes variables de entorno son compatibles:

| Variable | Predeterminado | Descripción |
|----------|---------------|-------------|
| `SHOW_USAGE` | `0` | Configura en `1` para imprimir el uso de tokens |
| `RETRY_ON_FAIL` | `1` | Habilita la lógica de reintento |
| `RETRY_BACKOFF` | `1.0` | Retraso inicial de reintento (segundos) |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Sobrescribe el endpoint del servicio |

### Ejemplos de Uso

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## Migración desde el Patrón Antiguo

Si tienes código existente que utiliza llamadas directas a la API, aquí está cómo migrar:

### Antes (API Directa)
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### Después (SDK)
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### Beneficios de la Migración
- ✅ Gestión automática del servicio
- ✅ Resolución de alias de modelos
- ✅ Selección de optimización de hardware
- ✅ Mejor manejo de errores
- ✅ Compatibilidad con el SDK de OpenAI
- ✅ Soporte de streaming

## Referencias

### Documentación Oficial
- **GitHub de Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Fuente del SDK de Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Referencia CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **API REST**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md
- **Solución de Problemas**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

### Recursos del Workshop
- **README de la Sesión 06**: `Workshop/notebooks/session06_README.md`
- **Utilidades del Workshop**: `Workshop/samples/workshop_utils.py`
- **Notebook de Ejemplo**: `Workshop/notebooks/session06_models_router.ipynb`

### Comunidad
- **Discord**: https://aka.ms/foundry-local-discord
- **Problemas en GitHub**: https://github.com/microsoft/Foundry-Local/issues

## Próximos Pasos

1. **Revisar Cambios**: Leer los archivos actualizados  
2. **Probar el Notebook**: Ejecutar session06_models_router.ipynb  
3. **Verificar el SDK**: Asegurarse de que foundry-local-sdk está instalado  
4. **Comprobar el Servicio**: Confirmar que Foundry Local está en ejecución  
5. **Explorar Documentación**: Leer el nuevo session06_README.md  

## Resumen

Estas actualizaciones aseguran que los materiales del Workshop sigan exactamente los **patrones oficiales del SDK Local de Foundry** tal como se documentan en el repositorio de GitHub. Todos los ejemplos de código, documentación y utilidades ahora están alineados con las mejores prácticas recomendadas por Microsoft para el despliegue local de modelos de IA.

Las mejoras incluyen:
- ✅ **Corrección**: Uso de patrones oficiales del SDK  
- ✅ **Documentación**: Explicaciones y ejemplos completos  
- ✅ **Manejo de Errores**: Mensajes y guía de solución de problemas mejorados  
- ✅ **Mantenibilidad**: Sigue convenciones oficiales  
- ✅ **Experiencia del Usuario**: Instrucciones más claras y ayuda para depuración  

---

**Actualizado:** 8 de octubre de 2025  
**Versión del SDK:** foundry-local-sdk (última)  
**Rama del Workshop:** Reactor  

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.