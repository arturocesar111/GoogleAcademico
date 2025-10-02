# GoogleAcademico

Web scraper para buscar información de artículos científicos en Google Scholar.

## Descripción

Este proyecto proporciona una herramienta de web scraping para extraer información de artículos científicos desde Google Scholar (Google Académico). Permite buscar artículos, filtrar por autor, título y obtener información relevante como citaciones, autores, enlaces y resúmenes.

## Características

- 🔍 Búsqueda de artículos científicos por términos generales
- 👤 Búsqueda de artículos por autor específico
- 📄 Búsqueda de artículos por título
- 📊 Extracción de información relevante:
  - Título del artículo
  - Enlace al artículo
  - Autores y publicación
  - Resumen
  - Número de citaciones
  - Versiones disponibles

## Requisitos

- Python 3.6 o superior
- beautifulsoup4
- requests
- lxml

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

### Uso Básico

```python
from google_academico import GoogleScholarScraper, imprimir_articulos

# Crear instancia del scraper
scraper = GoogleScholarScraper()

# Buscar artículos
articulos = scraper.buscar_articulos("machine learning", num_resultados=10)

# Mostrar resultados
imprimir_articulos(articulos)
```

### Búsqueda por Autor

```python
from google_academico import GoogleScholarScraper

scraper = GoogleScholarScraper()

# Buscar artículos de un autor específico
articulos = scraper.buscar_por_autor("Andrew Ng", num_resultados=5)

for articulo in articulos:
    print(f"Título: {articulo['titulo']}")
    print(f"Autores: {articulo['autores_info']}")
    print(f"Citado por: {articulo['citado_por']}")
    print("-" * 80)
```

### Búsqueda por Título

```python
from google_academico import GoogleScholarScraper

scraper = GoogleScholarScraper()

# Buscar artículos con un título específico
articulos = scraper.buscar_por_titulo("deep learning", num_resultados=5)
```

### Ejemplo Completo

Ejecuta el script de ejemplo incluido:

```bash
python ejemplo.py
```

## Estructura del Proyecto

```
GoogleAcademico/
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
├── google_academico.py    # Módulo principal del scraper
└── ejemplo.py            # Script de ejemplo
```

## API Reference

### Clase GoogleScholarScraper

#### `__init__(user_agent=None)`
Inicializa el scraper con un user agent opcional.

#### `buscar_articulos(query, num_resultados=10, delay=2)`
Busca artículos científicos en Google Scholar.

**Parámetros:**
- `query` (str): Término de búsqueda
- `num_resultados` (int): Número de resultados a retornar (default: 10)
- `delay` (int): Tiempo de espera entre peticiones en segundos (default: 2)

**Retorna:**
- Lista de diccionarios con información de los artículos

#### `buscar_por_autor(autor, num_resultados=10)`
Busca artículos de un autor específico.

**Parámetros:**
- `autor` (str): Nombre del autor
- `num_resultados` (int): Número de resultados a retornar

#### `buscar_por_titulo(titulo, num_resultados=10)`
Busca artículos por título específico.

**Parámetros:**
- `titulo` (str): Título del artículo
- `num_resultados` (int): Número de resultados a retornar

### Función imprimir_articulos

```python
imprimir_articulos(articulos)
```

Función auxiliar para imprimir artículos de forma legible.

## Estructura de Datos

Cada artículo retornado es un diccionario con la siguiente estructura:

```python
{
    'titulo': 'Título del artículo',
    'enlace': 'https://...',
    'autores_info': 'Autores - Publicación - Año',
    'resumen': 'Resumen del artículo...',
    'citado_por': 'Citado por X',
    'versiones': 'Todas las X versiones'
}
```

## Consideraciones Importantes

- ⚠️ **Rate Limiting**: Google Scholar puede bloquear IPs que hacen demasiadas peticiones. El scraper incluye delays entre peticiones para minimizar este riesgo.
- 🔒 **Uso Responsable**: Este scraper es para uso educativo y de investigación. Respeta los términos de servicio de Google Scholar.
- 🌐 **User Agent**: El scraper usa un user agent genérico. Puedes personalizarlo si lo necesitas.
- 📡 **Conexión a Internet**: Se requiere conexión a internet activa para realizar las búsquedas.

## Solución de Problemas

### Error de conexión
Si obtienes errores de conexión, verifica:
- Tu conexión a internet
- Que no estés siendo bloqueado por hacer demasiadas peticiones (aumenta el `delay`)

### No se encuentran resultados
- Verifica que la consulta de búsqueda sea correcta
- Prueba con términos de búsqueda diferentes

### Estructura HTML ha cambiado
Google Scholar puede cambiar la estructura de su HTML. Si los resultados no se extraen correctamente, el módulo puede necesitar actualizaciones.

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

Este proyecto es solo para propósitos educativos. El uso de web scraping debe cumplir con los términos de servicio del sitio web objetivo. Google Scholar tiene políticas sobre el uso automatizado de su servicio.