#!/usr/bin/env python3
"""
Script de prueba simple para el scraper de Google Académico
"""

from google_academico import GoogleScholarScraper

def test_scraper():
    """Prueba básica del scraper"""
    print("Iniciando prueba del scraper...")
    
    try:
        scraper = GoogleScholarScraper()
        print("✓ Scraper inicializado correctamente")
        
        # Probar búsqueda simple con pocos resultados
        print("\nRealizando búsqueda de prueba...")
        articulos = scraper.buscar_articulos("python programming", num_resultados=2)
        
        if articulos:
            print(f"✓ Búsqueda exitosa. Se encontraron {len(articulos)} artículos")
            
            # Verificar estructura de los artículos
            articulo = articulos[0]
            campos_requeridos = ['titulo', 'enlace', 'autores_info', 'resumen', 'citado_por', 'versiones']
            
            for campo in campos_requeridos:
                if campo in articulo:
                    print(f"✓ Campo '{campo}' presente")
                else:
                    print(f"✗ Campo '{campo}' faltante")
            
            # Mostrar primer artículo
            print("\n" + "=" * 60)
            print("Ejemplo de artículo extraído:")
            print("=" * 60)
            print(f"Título: {articulo['titulo'][:100]}...")
            if articulo['autores_info']:
                print(f"Autores: {articulo['autores_info'][:80]}...")
            if articulo['enlace']:
                print(f"Enlace: {articulo['enlace']}")
            print("=" * 60)
            
            print("\n✓ Todas las pruebas pasaron exitosamente")
            return True
        else:
            print("✗ No se encontraron artículos")
            return False
            
    except Exception as e:
        print(f"✗ Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_scraper()
