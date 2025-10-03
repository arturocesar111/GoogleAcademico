# Migración y Limpieza de Archivos - GoogleAcademico

## 📁 **Estructura del Proyecto Depurada**

### ✅ **Archivos Principales (En Uso)**

#### **API de Semantic Scholar (Principal)**
- `semantic_scholar_api.py` - **Módulo principal** de la API
- `semantic_scholar_main.py` - **Script interactivo** principal
- `ejemplo_semantic_scholar.py` - **Ejemplos** de uso
- `SEMANTIC_SCHOLAR_README.md` - **Documentación** completa

#### **Configuración y Documentación**
- `requirements.txt` - Dependencias del proyecto
- `README.md` - Documentación principal actualizada
- `.gitignore` - Configuración de Git

### 📦 **Archivos Movidos a Legacy**

Los siguientes archivos han sido movidos a la carpeta `legacy/` porque están relacionados con el scraping de Google Scholar (que causaba bloqueos):

#### **Scraping de Google Scholar (Obsoleto)**
- `google_academico.py` - Scraper original con bloqueos
- `ejecutar.py` - Script interactivo del scraper
- `ejemplo.py` - Ejemplos del scraper
- `ejemplo_seguro.py` - Versión "segura" del scraper
- `test_scraper.py` - Pruebas del scraper
- `scraper_robusto.py` - Versión con reintentos
- `diagnostico.py` - Diagnóstico de bloqueos
- `prueba_csv.py` - Pruebas de CSV del scraper

#### **Archivos CSV Antiguos**
- `busqueda_simulada.csv` - CSV de datos simulados
- `ejemplo_inteligencia_artificial.csv` - CSV de ejemplo
- `pdfpp.csv` - CSV de prueba
- Otros archivos CSV temporales del scraper

#### **Documentación Obsoleta**
- `CSV_README.md` - Documentación del CSV del scraper

### 🚀 **Cómo Usar Después de la Limpieza**

#### **Script Principal (Recomendado)**
```bash
python semantic_scholar_main.py
```

#### **Ejemplos y Pruebas**
```bash
python ejemplo_semantic_scholar.py
```

#### **En Código Python**
```python
from semantic_scholar_api import SemanticScholarAPI, imprimir_y_guardar_csv

api = SemanticScholarAPI()
articulos = api.buscar_articulos("machine learning", 10)
archivo = imprimir_y_guardar_csv(articulos, query="machine learning")
```

### 📋 **Funcionalidad Mantenida**

- ✅ **Búsquedas sin bloqueo** (Semantic Scholar API)
- ✅ **Exportación CSV** con separador `|`
- ✅ **Datos enriquecidos** (citaciones, campos, métricas)
- ✅ **Scripts interactivos**
- ✅ **Ejemplos de uso**
- ✅ **Compatibilidad con API Key**

### 🗑️ **Funcionalidad Removida**

- ❌ **Web scraping de Google Scholar** (causaba bloqueos)
- ❌ **Scripts de diagnóstico** de bloqueos
- ❌ **Delays largos** y reintentos
- ❌ **Manejo de captchas**

### 💾 **Archivos de Respaldo**

Si necesitas recuperar algún archivo del scraping original, están disponibles en:
- `legacy/` - Código original del scraper
- Repositorio Git - Historial completo

### 🔄 **Migración para Usuarios**

Si estabas usando:
- `google_academico.py` → Usa `semantic_scholar_api.py`
- `ejecutar.py` → Usa `semantic_scholar_main.py`
- `ejemplo.py` → Usa `ejemplo_semantic_scholar.py`

### 📈 **Beneficios de la Limpieza**

- 🧹 **Proyecto más limpio** y fácil de navegar
- 🚀 **Sin archivos obsoletos** que causen confusión
- 📚 **Documentación clara** sobre qué usar
- 🔧 **Mantenimiento simplificado**
- ⚡ **Mejor experiencia de usuario**

---

**Fecha de limpieza:** October 2, 2025
**Versión:** 2.0 (Semantic Scholar API)