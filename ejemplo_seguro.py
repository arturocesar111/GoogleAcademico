#!/usr/bin/env python3
"""
Ejemplo seguro de uso del Google Académico Web Scraper
"""

import time
from google_academico import GoogleScholarScraper, imprimir_articulos, imprimir_y_guardar_csv


def ejemplo_seguro():
    """Ejemplo con delays largos para evitar bloqueos"""
    print("=" * 80)
    print("GOOGLE ACADÉMICO WEB SCRAPER - EJEMPLO SEGURO")
    print("=" * 80)
    print("\nConfiguración:")
    print("- Pocos resultados (2 artículos)")
    print("- Delay largo entre peticiones (5 segundos)")
    print("- User agent personalizado")
    print("=" * 80)
    
    # Crear scraper con user agent personalizado
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    scraper = GoogleScholarScraper(user_agent=user_agent)
    
    try:
        # Buscar artículos sobre Python (término menos popular que machine learning)
        query = "python programming tutorial"
        print(f"\n🔍 Buscando artículos sobre: '{query}'")
        print("⏳ Esperando respuesta de Google Scholar...")
        
        articulos = scraper.buscar_articulos(
            query=query, 
            num_resultados=2,  # Solo 2 artículos para ser conservador
            delay=5  # 5 segundos entre peticiones
        )
        
        if articulos:
            print(f"\n✅ ¡Éxito! Se encontraron {len(articulos)} artículos:")
            # Imprimir y guardar en CSV automáticamente
            archivo_csv = imprimir_y_guardar_csv(articulos, query=query)
        else:
            print("\n⚠️ No se encontraron artículos o Google Scholar está bloqueando las peticiones.")
            print("\nPosibles soluciones:")
            print("1. Esperar unos minutos antes de volver a intentar")
            print("2. Cambiar de red/IP")
            print("3. Usar una VPN")
            print("4. Aumentar el delay entre peticiones")
            
    except Exception as e:
        print(f"\n❌ Error durante la búsqueda: {e}")
        if "429" in str(e) or "Too Many Requests" in str(e):
            print("\n🚫 Google Scholar está limitando las peticiones.")
            print("Esto es normal cuando se hacen muchas búsquedas.")
            print("\n💡 Soluciones:")
            print("- Esperar 10-15 minutos antes de volver a intentar")
            print("- Usar el scraper con menos frecuencia")
            print("- Aumentar los delays entre peticiones")
        else:
            print(f"\n🔧 Error técnico: {e}")


def mostrar_uso_programatico():
    """Muestra cómo usar el scraper en tu propio código"""
    print("\n\n" + "=" * 80)
    print("CÓMO USAR EL SCRAPER EN TU CÓDIGO")
    print("=" * 80)
    
    codigo_ejemplo = '''
from google_academico import GoogleScholarScraper, imprimir_y_guardar_csv, guardar_articulos_csv

# 1. Crear instancia del scraper
scraper = GoogleScholarScraper()

# 2. Buscar artículos (con delay apropiado)
articulos = scraper.buscar_articulos("inteligencia artificial", num_resultados=3, delay=3)

# 3. Opción A: Solo mostrar en pantalla
for articulo in articulos:
    print(f"Título: {articulo['titulo']}")
    print(f"Autores: {articulo['autores_info']}")
    print(f"Citaciones: {articulo['citado_por']}")

# 4. Opción B: Mostrar Y guardar en CSV automáticamente
archivo_csv = imprimir_y_guardar_csv(articulos, query="inteligencia artificial")

# 5. Opción C: Solo guardar en CSV (sin mostrar)
archivo = guardar_articulos_csv(articulos, "mi_archivo.csv", "inteligencia artificial")

# 6. Búsqueda por autor con CSV
articulos_autor = scraper.buscar_por_autor("Geoffrey Hinton", num_resultados=2)
imprimir_y_guardar_csv(articulos_autor, query="Geoffrey Hinton")

# 7. Búsqueda por título con CSV
articulos_titulo = scraper.buscar_por_titulo("deep learning", num_resultados=2) 
guardar_articulos_csv(articulos_titulo, nombre_archivo="deep_learning.csv")
    '''
    
    print("📝 Código de ejemplo:")
    print(codigo_ejemplo)


if __name__ == "__main__":
    print("🚀 Iniciando Google Académico Web Scraper...")
    
    # Mostrar información importante
    print("\n⚠️  INFORMACIÓN IMPORTANTE:")
    print("- Google Scholar puede limitar o bloquear peticiones automáticas")
    print("- Use delays apropiados entre búsquedas (3-5 segundos mínimo)")
    print("- Este scraper es solo para uso educativo e investigación")
    print("- Respete los términos de servicio de Google Scholar")
    
    # Ejecutar ejemplo
    ejemplo_seguro()
    
    # Mostrar uso programático
    mostrar_uso_programatico()
    
    print(f"\n{'='*80}")
    print("✨ ¡Scraper ejecutado! Revise los resultados arriba.")
    print("💡 Para más ejemplos, revise el archivo 'ejemplo.py'")
    print("📖 Para documentación completa, revise 'README.md'")
    print(f"{'='*80}")