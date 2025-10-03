# Funcionalidad CSV Agregada

## 📄 Nueva Funcionalidad: Exportación a CSV

Se ha agregado funcionalidad completa para exportar los resultados de las búsquedas a archivos CSV con separador `|` (pipe).

### 🆕 Nuevas Funciones

#### `guardar_articulos_csv(articulos, nombre_archivo=None, query="")`
- **Propósito**: Guarda artículos en archivo CSV
- **Separador**: `|` (pipe)
- **Codificación**: UTF-8
- **Nombre automático**: Si no se especifica, genera nombre con timestamp

#### `imprimir_y_guardar_csv(articulos, nombre_archivo=None, query="", mostrar_en_pantalla=True)`
- **Propósito**: Función combinada que muestra en pantalla Y guarda en CSV
- **Configurable**: Puede desactivar mostrar en pantalla

### 📊 Estructura del CSV

El archivo CSV incluye las siguientes columnas separadas por `|`:

1. **numero** - Número secuencial del artículo
2. **titulo** - Título del artículo científico
3. **autores_info** - Información de autores y publicación
4. **enlace** - URL del artículo (si disponible)
5. **resumen** - Resumen del artículo
6. **citado_por** - Número de citaciones
7. **versiones** - Información de versiones disponibles
8. **fecha_extraccion** - Timestamp de cuando se extrajo la información

### 🚀 Cómo Usar

#### Opción 1: Script Interactivo
```bash
python ejecutar.py
```
- El menú ahora pregunta si deseas guardar en CSV
- Puedes especificar nombre del archivo o usar generación automática

#### Opción 2: Ejemplo Automático
```bash
python ejemplo_seguro.py
```
- Automáticamente guarda resultados en CSV

#### Opción 3: En Tu Código Python

```python
from google_academico import GoogleScholarScraper, imprimir_y_guardar_csv, guardar_articulos_csv

# Crear scraper
scraper = GoogleScholarScraper()

# Buscar artículos
articulos = scraper.buscar_articulos("machine learning", num_resultados=5, delay=3)

# Opción A: Mostrar Y guardar en CSV
archivo_csv = imprimir_y_guardar_csv(articulos, query="machine learning")

# Opción B: Solo guardar en CSV (sin mostrar)
archivo = guardar_articulos_csv(articulos, "mi_busqueda.csv", "machine learning")

# Opción C: Guardar con nombre automático
archivo = guardar_articulos_csv(articulos, query="deep learning")
# Genera: articulos_deep_learning_20251002_123456.csv
```

### 🧪 Probar Funcionalidad

Para probar la funcionalidad CSV con datos de ejemplo:

```bash
python prueba_csv.py
```

Este script:
- Crea datos de ejemplo
- Genera varios archivos CSV de prueba
- Muestra estadísticas de los archivos creados
- Visualiza el contenido CSV

### 📁 Archivos Generados

Los archivos CSV se guardan en el directorio del proyecto con nombres como:
- `articulos_machine_learning_20251002_143022.csv`
- `articulos_autor_Andrew_Ng_20251002_143045.csv`
- `mi_archivo_personalizado.csv`

### 💡 Ventajas del Formato

- **Separador `|`**: Evita conflictos con comas en el texto
- **UTF-8**: Soporte completo para caracteres especiales y acentos
- **Compatible**: Funciona con Excel, LibreOffice, Python pandas, R, etc.
- **Timestamp**: Cada entrada incluye fecha/hora de extracción
- **Metadata**: Incluye información completa de cada artículo

### 📖 Ejemplo de Contenido CSV

```csv
numero|titulo|autores_info|enlace|resumen|citado_por|versiones|fecha_extraccion
1|Deep Learning|Ian Goodfellow, Yoshua Bengio - MIT Press - 2016|https://example.com/paper|Deep learning is a form of machine learning...|Citado por 87,542|Todas las 12 versiones|2025-10-02 21:56:23
```

### 🔧 Abriendo en Excel/LibreOffice

1. **Excel**: 
   - Archivo → Abrir → Seleccionar CSV
   - En "Separador" elegir "Otro" y escribir `|`
   - Seleccionar codificación UTF-8

2. **LibreOffice Calc**:
   - Se detecta automáticamente el separador `|`
   - Mantener codificación UTF-8

### ⚠️ Notas Importantes

- Los archivos se guardan en el directorio actual del proyecto
- Si no especificas nombre, se genera automáticamente con timestamp
- La funcionalidad funciona incluso cuando Google Scholar bloquea (usando datos de ejemplo para pruebas)
- Todos los caracteres especiales se preservan correctamente en UTF-8