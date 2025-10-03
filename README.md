# GoogleAcademico - Semantic Scholar API

Herramienta para buscar información de artículos científicos usando la API oficial de Semantic Scholar.

## Descripción

Este proyecto proporciona una interfaz fácil de usar para buscar y exportar información de artículos científicos desde Semantic Scholar. Incluye filtrado por años, múltiples tipos de búsqueda y exportación automática a CSV.

## Características

- 🔍 Búsqueda de artículos científicos por términos generales
- 👤 Búsqueda de artículos por autor específico  
- 📄 Búsqueda de artículos por título exacto
- 📅 **NUEVO**: Filtrado por rango de años (ej: 2020-2024)
- 📊 Extracción completa de información:
  - Título y resumen del artículo
  - Lista completa de autores
  - Año de publicación y fecha exacta
  - Número de citaciones
  - URL del artículo
  - Venue (revista/conferencia)
  - Campos de estudio
  - Tipos de publicación
- 💾 **Exportación automática a CSV** con separador "|" 
- 🚀 **Sin bloqueos**: Usa API oficial (no web scraping)

## Requisitos

- Python 3.7 o superior
- requests
- typing_extensions

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/arturocesar111/GoogleAcademico.git
cd GoogleAcademico
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Uso Principal (Interactivo)

```bash
python semantic_scholar_main.py
```

### Uso Programático

```python
from semantic_scholar_api import SemanticScholarAPI

# Crear instancia de la API
api = SemanticScholarAPI()

# Buscar artículos (con filtro de años opcional)
articulos = api.buscar_articulos("machine learning", num_resultados=10, año_desde=2020, año_hasta=2024)

# Los resultados se guardan automáticamente en CSV
```

### Búsqueda por Autor

```python
# Buscar artículos de un autor específico
articulos = api.buscar_por_autor("Geoffrey Hinton", num_resultados=5, año_desde=2020)

# Ver algunos resultados
for articulo in articulos[:3]:
    print(f"Título: {articulo['title']}")
    print(f"Año: {articulo['year']}")  
    print(f"Citaciones: {articulo['citationCount']}")
    print("-" * 50)
```

### Búsqueda por Título

```python
# Buscar artículos con título específico
articulos = api.buscar_por_titulo("Attention Is All You Need")
```

### Ejemplos Completos

```bash
python ejemplo_semantic_scholar.py
```

## Estructura del Proyecto

```
GoogleAcademico/
├── README.md                    # Este archivo  
├── requirements.txt             # Dependencias actualizadas
├── semantic_scholar_main.py     # Script principal interactivo
├── semantic_scholar_api.py      # Módulo API de Semantic Scholar
├── ejemplo_semantic_scholar.py  # Script de ejemplos
└── legacy/                      # Archivos obsoletos del scraper web
```

## Archivos de Salida

Los resultados se exportan automáticamente a archivos CSV con formato:
- **Separador**: `|` (pipe)
- **Codificación**: UTF-8
- **Nombres**: `semantic_scholar_[tipo]_[query]_[fecha]_[hora].csv`

### Columnas del CSV:
1. paperId - ID único del artículo
2. title - Título
3. abstract - Resumen
4. authors - Lista de autores  
5. year - Año de publicación
6. citationCount - Número de citaciones
7. url - Enlace al artículo
8. venue - Revista/Conferencia
9. publicationDate - Fecha completa
10. publicationTypes - Tipos de publicación
11. fieldsOfStudy - Campos de estudio

## Filtrado por Años

El sistema permite filtrar por rango de años en todos los tipos de búsqueda:

- **Rango completo**: 2020-2024
- **Solo desde**: 2022 (desde 2022 hasta ahora)  
- **Solo hasta**: -2020 (hasta 2020)

## API Reference

### Clase SemanticScholarAPI

#### `buscar_articulos(query, num_resultados=10, año_desde=None, año_hasta=None)`
Busca artículos por términos generales.

#### `buscar_por_autor(autor, num_resultados=10, año_desde=None, año_hasta=None)`  
Busca artículos de un autor específico.

#### `buscar_por_titulo(titulo, num_resultados=10, año_desde=None, año_hasta=None)`
Busca artículos por título exacto.

## Estructura de Datos

```python
{
    'paperId': 'ID único del artículo',
    'title': 'Título del artículo', 
    'abstract': 'Resumen completo...',
    'authors': ['Autor1', 'Autor2'],
    'year': 2024,
    'citationCount': 156,
    'url': 'https://...',
    'venue': 'Nombre de la revista/conferencia',
    'publicationDate': '2024-03-15',
    'publicationTypes': ['JournalArticle'],
    'fieldsOfStudy': ['Computer Science', 'Medicine']
}
```

## Consideraciones Importantes

- ✅ **API Oficial**: Usa la API oficial de Semantic Scholar, sin riesgo de bloqueos
- 🚀 **Rate Limiting Automático**: 1 request/segundo sin clave API, 100 req/s con clave
- � **Datos Completos**: Acceso a toda la información bibliográfica disponible
- 💾 **Exportación Automática**: Los resultados se guardan automáticamente en CSV
- 📡 **Conexión a Internet**: Se requiere conexión activa para acceder a la API

## API Key (Opcional)

Para mayor velocidad, puedes obtener una clave API gratuita en:
[Semantic Scholar API](https://www.semanticscholar.org/product/api)

```python
api = SemanticScholarAPI(api_key="tu_clave_api_aqui")
```

## Solución de Problemas

### Error 429 (Rate Limit)
- Normal sin API key (1 req/segundo máximo)
- Obtén una API key para mayor velocidad
- El sistema maneja automáticamente los límites

### No se encuentran resultados  
- Verifica la ortografía de los términos de búsqueda
- Prueba con sinónimos o términos relacionados
- Algunos campos muy específicos pueden tener pocos resultados

### Error de conexión
- Verifica tu conexión a internet
- Semantic Scholar API tiene alta disponibilidad

## Migración desde Web Scraping

Este proyecto migró de web scraping a API oficial para:
- ✅ Eliminar bloqueos de IP
- ✅ Obtener datos más completos y confiables  
- ✅ Mejorar velocidad y estabilidad
- ✅ Acceso a filtros avanzados (años, tipos, etc.)

Los archivos del sistema anterior están en la carpeta `legacy/`.

## Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)  
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

## Autor

- arturocesar111

## Disclaimer

Este proyecto utiliza la API pública de Semantic Scholar. Respeta los términos de uso de la API y las buenas prácticas de investigación académica.