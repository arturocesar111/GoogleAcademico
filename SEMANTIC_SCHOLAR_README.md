# GoogleAcademico - Migrado a Semantic Scholar API

## 🎉 **Nueva Versión - API Oficial**

Tu proyecto **GoogleAcademico** ha sido completamente migrado para usar la **API oficial de Semantic Scholar** en lugar de web scraping. Esto resuelve todos los problemas de bloqueo y proporciona datos más ricos y consistentes.

## 🆕 **¿Qué cambió?**

### ❌ **Antes (Web Scraping)**
- ⚠️ Bloqueos frecuentes de Google Scholar (Error 429)
- 🐌 Delays largos necesarios (15+ segundos)
- 🎲 Estructura HTML inestable
- ⛔ Riesgo de ban de IP
- 📉 Datos limitados

### ✅ **Ahora (API Oficial)**
- 🚀 **Sin bloqueos** - API oficial estable
- ⚡ **Más rápido** - 1 req/s (sin API key) o 100 req/s (con API key)
- 📊 **Datos más ricos** - Citaciones, campos de estudio, métricas
- 🔒 **Confiable** - Soporte oficial de Semantic Scholar
- 🌟 **Mejor experiencia** - Respuestas consistentes

## 🚀 **Cómo Usar la Nueva Versión**

### **Opción 1: Script Interactivo Completo**
```bash
python semantic_scholar_main.py
```
**Características:**
- Menú interactivo completo
- Búsqueda general, por autor, por título, por ID
- Configuración de API Key
- Exportación automática a CSV

### **Opción 2: Ejemplos Rápidos**
```bash
python ejemplo_semantic_scholar.py
```
**Incluye:**
- Ejemplos de todos los tipos de búsqueda
- Código de muestra para desarrollo
- Comparación de ventajas

### **Opción 3: En tu Código Python**
```python
from semantic_scholar_api import SemanticScholarAPI, imprimir_y_guardar_csv

# Crear cliente
api = SemanticScholarAPI()  # Sin API key
# api = SemanticScholarAPI("tu_api_key")  # Con API key

# Buscar artículos
articulos = api.buscar_articulos("machine learning", num_resultados=10)

# Mostrar y guardar en CSV
archivo = imprimir_y_guardar_csv(articulos, query="machine learning")

# Solo guardar CSV
from semantic_scholar_api import guardar_articulos_csv
archivo = guardar_articulos_csv(articulos, "mi_archivo.csv")
```

## 📊 **Nuevo Formato CSV Mejorado**

El CSV ahora incluye **más información** con separador `|`:

| Campo | Descripción |
|-------|-------------|
| `numero` | Número secuencial |
| `titulo` | Título del artículo |
| `autores_info` | Autores, venue y año |
| `enlace` | URL en Semantic Scholar |
| `resumen` | Abstract completo |
| `citado_por` | Número de citaciones |
| `year` | Año de publicación |
| `venue` | Revista/conferencia |
| `campos_estudio` | Categorías temáticas |
| `paper_id` | ID único de Semantic Scholar |
| `citation_count` | Citaciones (numérico) |
| `publication_date` | Fecha de publicación |
| `publication_types` | Tipo de publicación |
| `fecha_extraccion` | Timestamp de extracción |

## 🔑 **API Key (Recomendada)**

Para mejores límites de rate:

1. **Visita:** https://www.semanticscholar.org/product/api
2. **Regístrate** y obtén tu API Key gratuita
3. **Úsala en el código:**
   ```python
   api = SemanticScholarAPI("tu_api_key_aqui")
   ```

**Límites:**
- **Sin API Key:** 1 request/segundo
- **Con API Key:** 100 requests/segundo

## 📁 **Nuevos Archivos**

| Archivo | Propósito |
|---------|-----------|
| `semantic_scholar_api.py` | **Módulo principal** de la API |
| `semantic_scholar_main.py` | **Script interactivo** completo |
| `ejemplo_semantic_scholar.py` | **Ejemplos** de uso |

## 🔄 **Compatibilidad**

Los **archivos originales se mantienen** por compatibilidad:
- `google_academico.py` - Scraper original (puede dar errores de bloqueo)
- `ejecutar.py` - Script original
- `ejemplo.py` - Ejemplos originales

## 🎯 **Funcionalidades Disponibles**

### **1. Búsqueda General**
```python
articulos = api.buscar_articulos("artificial intelligence", 20)
```

### **2. Búsqueda por Autor**
```python
articulos = api.buscar_por_autor("Geoffrey Hinton", 15)
```

### **3. Búsqueda por Título**
```python
articulos = api.buscar_por_titulo("neural networks", 10)
```

### **4. Artículo por ID**
```python
articulo = api.obtener_articulo_por_id("paper_id_aqui")
```

## 📈 **Ventajas Adicionales**

### **🔍 Datos Más Ricos**
- **Campos de estudio** categorizados automáticamente
- **Métricas de citación** actualizadas en tiempo real
- **Información de venues** (revistas/conferencias)
- **Tipos de publicación** (Journal, Conference, etc.)
- **Fechas precisas** de publicación

### **🚀 Mejor Rendimiento**
- Respuestas en **millisegundos**
- Hasta **100 resultados** por búsqueda
- **Rate limiting** predecible y justo
- **Sin captchas** ni verificaciones

### **🔧 Más Confiable**
- API **oficialmente soportada**
- Datos **consistentes** y **estructurados**
- **Documentación completa** disponible
- **Actualizaciones** regulares de la base de datos

## 🛠️ **Instalación y Setup**

```bash
# Instalar dependencias (ya incluidas en requirements.txt)
pip install requests

# Ejecutar ejemplos
python ejemplo_semantic_scholar.py

# Usar script interactivo
python semantic_scholar_main.py
```

## 📞 **Soporte**

- **Documentación API:** https://api.semanticscholar.org/
- **Obtener API Key:** https://www.semanticscholar.org/product/api
- **Semantic Scholar:** https://www.semanticscholar.org/

---

## ⚡ **¡Prueba Ahora!**

```bash
# Script interactivo completo
python semantic_scholar_main.py

# O ejemplos rápidos
python ejemplo_semantic_scholar.py
```

**¡Tu proyecto GoogleAcademico ahora es mucho más potente y confiable!** 🎉