#!/usr/bin/env python3
"""
Ejemplo de uso de la API de Semantic Scholar
"""

from semantic_scholar_api import SemanticScholarAPI, imprimir_y_guardar_csv


def ejemplo_basico():
    """Ejemplo básico de uso de la API"""
    print("🎓 EJEMPLO DE USO - SEMANTIC SCHOLAR API")
    print("=" * 60)
    
    # Crear cliente (sin API key por ahora)
    print("📡 Inicializando cliente de Semantic Scholar...")
    api = SemanticScholarAPI()
    
    # Ejemplo 1: Búsqueda general
    print("\n📚 Ejemplo 1: Búsqueda general")
    print("-" * 40)
    query = "machine learning"
    print(f"🔍 Buscando: '{query}'")
    
    articulos = api.buscar_articulos(query, num_resultados=3)
    
    if articulos:
        print(f"✅ Se encontraron {len(articulos)} artículos")
        archivo_csv = imprimir_y_guardar_csv(articulos, query=query)
    else:
        print("❌ No se encontraron artículos")
    
    # Ejemplo 1b: Búsqueda con filtro de años
    print("\n📚 Ejemplo 1b: Búsqueda con filtro de años")
    print("-" * 40)
    query = "deep learning"
    print(f"🔍 Buscando: '{query}' (años 2020-2024)")
    
    articulos_filtrados = api.buscar_articulos(query, num_resultados=3, año_desde=2020, año_hasta=2024)
    
    if articulos_filtrados:
        print(f"✅ Se encontraron {len(articulos_filtrados)} artículos (2020-2024)")
        archivo_csv = imprimir_y_guardar_csv(articulos_filtrados, query=f"{query}_2020-2024")
    else:
        print("❌ No se encontraron artículos en ese rango")
    
    # Ejemplo 2: Búsqueda por autor
    print(f"\n👤 Ejemplo 2: Búsqueda por autor")
    print("-" * 40)
    autor = "Andrew Ng"
    print(f"🔍 Buscando artículos de: '{autor}'")
    
    articulos_autor = api.buscar_por_autor(autor, num_resultados=2)
    
    if articulos_autor:
        print(f"✅ Se encontraron {len(articulos_autor)} artículos")
        archivo_csv = imprimir_y_guardar_csv(articulos_autor, query=f"autor_{autor}")
    else:
        print("❌ No se encontraron artículos del autor")
    
    # Ejemplo 2b: Búsqueda por autor con filtro
    print(f"\n👤 Ejemplo 2b: Búsqueda por autor con filtro")
    print("-" * 40)
    autor = "Geoffrey Hinton"
    print(f"🔍 Buscando artículos de: '{autor}' (desde 2010)")
    
    articulos_autor_filtrado = api.buscar_por_autor(autor, num_resultados=2, año_desde=2010)
    
    if articulos_autor_filtrado:
        print(f"✅ Se encontraron {len(articulos_autor_filtrado)} artículos (desde 2010)")
        archivo_csv = imprimir_y_guardar_csv(articulos_autor_filtrado, query=f"autor_{autor}_desde_2010")
    else:
        print("❌ No se encontraron artículos del autor en ese período")
    
    # Ejemplo 3: Búsqueda por título
    print(f"\n📄 Ejemplo 3: Búsqueda por título")
    print("-" * 40)
    titulo = "neural networks"
    print(f"🔍 Buscando artículos con título: '{titulo}'")
    
    articulos_titulo = api.buscar_por_titulo(titulo, num_resultados=2)
    
    if articulos_titulo:
        print(f"✅ Se encontraron {len(articulos_titulo)} artículos")
        archivo_csv = imprimir_y_guardar_csv(articulos_titulo, query=f"titulo_{titulo}")
    else:
        print("❌ No se encontraron artículos con ese título")


def ejemplo_programatico():
    """Ejemplo de cómo usar en tu propio código"""
    print(f"\n{'='*60}")
    print("💻 EJEMPLO DE USO PROGRAMÁTICO")
    print("="*60)
    
    codigo_ejemplo = '''
# Importar la API
from semantic_scholar_api import SemanticScholarAPI, imprimir_y_guardar_csv

# 1. Crear cliente
api = SemanticScholarAPI()  # Sin API key
# api = SemanticScholarAPI("tu_api_key_aqui")  # Con API key

# 2. Búsqueda general
articulos = api.buscar_articulos("artificial intelligence", num_resultados=5)

# 3. Búsqueda con filtro de años
articulos_recientes = api.buscar_articulos("machine learning", 5, año_desde=2020, año_hasta=2024)

# 4. Mostrar y guardar en CSV
archivo = imprimir_y_guardar_csv(articulos, query="artificial intelligence")

# 5. Solo guardar en CSV (sin mostrar)
from semantic_scholar_api import guardar_articulos_csv
archivo = guardar_articulos_csv(articulos, "mi_archivo.csv", "AI research")

# 6. Búsqueda por autor
articulos_autor = api.buscar_por_autor("Geoffrey Hinton", 10)

# 7. Búsqueda por autor con filtro
articulos_autor_recientes = api.buscar_por_autor("Yann LeCun", 5, año_desde=2015)

# 8. Búsqueda por título
articulos_titulo = api.buscar_por_titulo("neural networks", 5)

# 9. Búsqueda por título con rango específico
articulos_titulo_periodo = api.buscar_por_titulo("deep learning", 3, año_desde=2018, año_hasta=2022)

# 7. Obtener artículo específico por ID
articulo = api.obtener_articulo_por_id("204e3073870fae3d05bcbc2f6a8e263d9b72e776")

# 8. Procesar resultados
for articulo in articulos:
    print(f"Título: {articulo['titulo']}")
    print(f"Citaciones: {articulo['citation_count']}")
    print(f"Año: {articulo['year']}")
    print(f"Campos: {articulo['campos_estudio']}")
    '''
    
    print(codigo_ejemplo)


def mostrar_ventajas():
    """Muestra las ventajas de usar la API"""
    print(f"\n{'='*60}")
    print("🌟 VENTAJAS DE SEMANTIC SCHOLAR API")
    print("="*60)
    
    print("🚀 Comparación con Google Scholar scraping:")
    print()
    print("❌ Google Scholar (scraping):")
    print("   • Bloqueos frecuentes (Error 429)")
    print("   • Captchas y limitaciones de IP") 
    print("   • Estructura HTML puede cambiar")
    print("   • Delays largos necesarios")
    print("   • Riesgo de ban permanente")
    
    print("\n✅ Semantic Scholar API:")
    print("   • Sin bloqueos ni captchas")
    print("   • API oficial y estable")
    print("   • Datos estructurados consistentes") 
    print("   • Límites claros y predecibles")
    print("   • Soporte oficial")
    print("   • Información más completa")
    
    print("\n📊 Datos adicionales disponibles:")
    print("   • Campos de estudio categorizados")
    print("   • Métricas de citaciones actualizadas")
    print("   • Información de venues/conferencias")
    print("   • IDs únicos para seguimiento")
    print("   • Tipos de publicación")
    print("   • Referencias y citaciones")
    
    print("\n⚡ Rendimiento:")
    print("   • Sin API Key: 1 request/segundo")
    print("   • Con API Key: 100 requests/segundo")
    print("   • Hasta 100 resultados por búsqueda")
    print("   • Respuestas en JSON estructurado")


if __name__ == "__main__":
    print("🎓 GOOGLE ACADÉMICO - SEMANTIC SCHOLAR API")
    print("Ejemplos de uso y migración de scraping a API oficial")
    print("="*60)
    
    try:
        ejemplo_basico()
        ejemplo_programatico() 
        mostrar_ventajas()
        
        print(f"\n{'='*60}")
        print("✨ ¡EJEMPLOS COMPLETADOS!")
        print("="*60)
        print("📝 Revisa los archivos CSV generados")
        print("💡 Para uso interactivo ejecuta: python semantic_scholar_main.py")
        print("🔑 Para mejores límites obtén una API Key en:")
        print("   https://www.semanticscholar.org/product/api")
        
    except Exception as e:
        print(f"\n❌ Error durante los ejemplos: {e}")
        print("💡 Verifica tu conexión a internet y vuelve a intentar")