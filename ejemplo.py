#!/usr/bin/env python3
"""
Ejemplo de uso del Google Académico Web Scraper
"""

from google_academico import GoogleScholarScraper, imprimir_articulos


def ejemplo_basico():
    """Ejemplo básico de búsqueda"""
    print("=" * 80)
    print("EJEMPLO 1: Búsqueda básica de artículos")
    print("=" * 80)
    
    scraper = GoogleScholarScraper()
    
    # Buscar artículos sobre machine learning
    query = "machine learning"
    print(f"\nBuscando artículos sobre: '{query}'")
    articulos = scraper.buscar_articulos(query, num_resultados=5)
    
    print(f"\nSe encontraron {len(articulos)} artículos:")
    imprimir_articulos(articulos)


def ejemplo_busqueda_por_autor():
    """Ejemplo de búsqueda por autor"""
    print("\n\n" + "=" * 80)
    print("EJEMPLO 2: Búsqueda por autor")
    print("=" * 80)
    
    scraper = GoogleScholarScraper()
    
    # Buscar artículos de un autor específico
    autor = "Andrew Ng"
    print(f"\nBuscando artículos del autor: '{autor}'")
    articulos = scraper.buscar_por_autor(autor, num_resultados=3)
    
    print(f"\nSe encontraron {len(articulos)} artículos:")
    imprimir_articulos(articulos)


def ejemplo_busqueda_por_titulo():
    """Ejemplo de búsqueda por título"""
    print("\n\n" + "=" * 80)
    print("EJEMPLO 3: Búsqueda por título")
    print("=" * 80)
    
    scraper = GoogleScholarScraper()
    
    # Buscar artículos con título específico
    titulo = "deep learning"
    print(f"\nBuscando artículos con título que contiene: '{titulo}'")
    articulos = scraper.buscar_por_titulo(titulo, num_resultados=3)
    
    print(f"\nSe encontraron {len(articulos)} artículos:")
    imprimir_articulos(articulos)


def ejemplo_personalizado():
    """Ejemplo con búsqueda personalizada"""
    print("\n\n" + "=" * 80)
    print("EJEMPLO 4: Búsqueda personalizada")
    print("=" * 80)
    
    scraper = GoogleScholarScraper()
    
    # Búsqueda con términos más específicos
    query = "neural networks computer vision"
    print(f"\nBuscando artículos sobre: '{query}'")
    articulos = scraper.buscar_articulos(query, num_resultados=3)
    
    print(f"\nSe encontraron {len(articulos)} artículos:")
    
    # Mostrar solo información básica
    for i, articulo in enumerate(articulos, 1):
        print(f"\n{i}. {articulo['titulo']}")
        print(f"   Autores: {articulo['autores_info']}")
        if articulo['citado_por']:
            print(f"   {articulo['citado_por']}")


if __name__ == "__main__":
    print("Google Académico Web Scraper - Ejemplos de Uso")
    print("=" * 80)
    print("\nNOTA: Este scraper hace peticiones a Google Scholar.")
    print("Es importante usar delays apropiados para evitar ser bloqueado.")
    print("=" * 80)
    
    # Ejecutar ejemplos
    try:
        ejemplo_basico()
        
        # Descomentar para ejecutar más ejemplos
        # ejemplo_busqueda_por_autor()
        # ejemplo_busqueda_por_titulo()
        # ejemplo_personalizado()
        
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
        print("\nAsegúrate de tener instaladas las dependencias:")
        print("pip install -r requirements.txt")
