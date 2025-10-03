#!/usr/bin/env python3
"""
Script para diagnosticar y solucionar problemas del scraper
"""

import time
import requests
from google_academico import GoogleScholarScraper, imprimir_y_guardar_csv

def diagnosticar_conectividad():
    """Diagnostica problemas de conectividad y bloqueo"""
    print("🔍 DIAGNÓSTICO DEL SCRAPER")
    print("=" * 50)
    
    # Prueba 1: Conexión a internet
    print("\n1. Probando conexión a internet...")
    try:
        response = requests.get("https://www.google.com", timeout=5)
        print(f"   ✅ Conexión OK (Status: {response.status_code})")
    except Exception as e:
        print(f"   ❌ Error de conexión: {e}")
        return False
    
    # Prueba 2: Acceso directo a Google Scholar
    print("\n2. Probando acceso a Google Scholar...")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get("https://scholar.google.com", headers=headers, timeout=10)
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Acceso directo OK")
        elif response.status_code == 429:
            print("   🚫 IP bloqueada por Google Scholar (Error 429)")
            print("   💡 Esto es temporal. Espera 15-30 minutos.")
        elif response.status_code == 403:
            print("   ⛔ Acceso denegado (Error 403)")
        else:
            print(f"   ⚠️ Respuesta inesperada: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Prueba 3: Búsqueda simple
    print("\n3. Probando búsqueda básica...")
    scraper = GoogleScholarScraper()
    try:
        # Búsqueda muy conservadora
        articulos = scraper.buscar_articulos("test", num_resultados=1, delay=10)
        if articulos:
            print("   ✅ Búsqueda exitosa")
            return True
        else:
            print("   ❌ Sin resultados - IP bloqueada")
            return False
    except Exception as e:
        if "429" in str(e):
            print("   🚫 IP bloqueada confirmada")
        else:
            print(f"   ❌ Error: {e}")
        return False

def crear_datos_simulados():
    """Crea datos simulados para probar la funcionalidad CSV"""
    return [
        {
            'titulo': 'Artificial Intelligence: A Modern Approach',
            'enlace': 'https://scholar.google.com/scholar?q=artificial+intelligence',
            'autores_info': 'Stuart Russell, Peter Norvig - Pearson - 2020',
            'resumen': 'This book provides a comprehensive, up-to-date introduction to the theory and practice of artificial intelligence.',
            'citado_por': 'Citado por 45,231',
            'versiones': 'Todas las 15 versiones'
        },
        {
            'titulo': 'Machine Learning Yearning',
            'enlace': 'https://scholar.google.com/scholar?q=machine+learning+yearning',
            'autores_info': 'Andrew Ng - deeplearning.ai - 2018',
            'resumen': 'Technical strategy guide for AI engineers in the era of deep learning.',
            'citado_por': 'Citado por 8,432',
            'versiones': 'Todas las 4 versiones'
        },
        {
            'titulo': 'Python for Data Analysis',
            'enlace': 'https://scholar.google.com/scholar?q=python+data+analysis',
            'autores_info': 'Wes McKinney - O\'Reilly Media - 2022',
            'resumen': 'Get complete instructions for manipulating, processing, cleaning, and crunching datasets in Python.',
            'citado_por': 'Citado por 12,876',
            'versiones': 'Todas las 7 versiones'
        }
    ]

def probar_con_datos_simulados():
    """Prueba la funcionalidad completa con datos simulados"""
    print("\n🧪 PROBANDO FUNCIONALIDAD CON DATOS SIMULADOS")
    print("=" * 60)
    
    # Crear datos de ejemplo
    articulos = crear_datos_simulados()
    
    print(f"📊 Creados {len(articulos)} artículos simulados")
    print("\n🔍 Simulando búsqueda: 'artificial intelligence'")
    
    # Probar función de guardado CSV
    print("\n📝 Guardando resultados en CSV...")
    try:
        archivo_csv = imprimir_y_guardar_csv(
            articulos, 
            nombre_archivo="busqueda_simulada.csv",
            query="artificial intelligence"
        )
        
        if archivo_csv:
            print(f"\n✅ ¡ÉXITO! Archivo CSV creado: {archivo_csv}")
            
            # Verificar contenido del archivo
            import os
            if os.path.exists(archivo_csv):
                size = os.path.getsize(archivo_csv)
                print(f"📏 Tamaño del archivo: {size} bytes")
                
                # Mostrar primeras líneas del CSV
                print("\n👀 Primeras líneas del CSV:")
                with open(archivo_csv, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f):
                        if i < 3:
                            print(f"   {line.strip()}")
                        else:
                            break
                
                return True
        else:
            print("❌ No se pudo crear el archivo CSV")
            return False
            
    except Exception as e:
        print(f"❌ Error al crear CSV: {e}")
        return False

def mostrar_soluciones():
    """Muestra soluciones para el problema de bloqueo"""
    print("\n🛠️ SOLUCIONES PARA BLOQUEO DE GOOGLE SCHOLAR")
    print("=" * 60)
    print("📋 Causas del bloqueo:")
    print("   • Muchas búsquedas en poco tiempo")
    print("   • Google Scholar detecta comportamiento automatizado")
    print("   • Límites de rate por IP")
    
    print("\n💡 Soluciones:")
    print("   1. ⏰ ESPERAR: 15-30 minutos antes de volver a intentar")
    print("   2. 🐌 DELAYS LARGOS: Usar delays de 10+ segundos entre búsquedas")
    print("   3. 🔄 CAMBIAR IP: Usar VPN o cambiar de red")
    print("   4. 📱 USAR DATOS MÓVILES: Cambiar a internet móvil temporalmente")
    print("   5. 🎯 BÚSQUEDAS ESPECÍFICAS: Hacer menos búsquedas, más precisas")
    
    print("\n⚙️ Configuración recomendada:")
    print("   • num_resultados=1-3 (máximo)")
    print("   • delay=10-15 segundos")
    print("   • Máximo 2-3 búsquedas por sesión")
    print("   • Esperar entre sesiones")
    
    print("\n🔧 Para desarrollo/pruebas:")
    print("   • Usar datos simulados (como en este script)")
    print("   • Probar funcionalidad CSV sin hacer búsquedas reales")
    print("   • Implementar cache local de resultados")

def main():
    """Función principal de diagnóstico"""
    print("🚀 DIAGNÓSTICO DEL GOOGLE ACADÉMICO SCRAPER")
    print("=" * 60)
    
    # Diagnóstico de conectividad
    conectividad_ok = diagnosticar_conectividad()
    
    # Siempre probar funcionalidad con datos simulados
    csv_ok = probar_con_datos_simulados()
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📋 RESUMEN DEL DIAGNÓSTICO")
    print("=" * 60)
    
    if conectividad_ok:
        print("🌐 Conectividad: ✅ OK")
        print("💡 El scraper funciona, pero Google Scholar puede estar limitando")
    else:
        print("🌐 Conectividad: ❌ BLOQUEADA")
        print("🚫 Google Scholar está bloqueando tu IP")
    
    if csv_ok:
        print("📄 Funcionalidad CSV: ✅ OK")
        print("💾 Los archivos CSV se generan correctamente")
    else:
        print("📄 Funcionalidad CSV: ❌ ERROR")
    
    # Mostrar soluciones
    mostrar_soluciones()
    
    print("\n🎯 PRÓXIMOS PASOS:")
    if not conectividad_ok:
        print("   1. Esperar 15-30 minutos")
        print("   2. Cambiar de red/IP si es posible") 
        print("   3. Probar con delays más largos")
    else:
        print("   1. El scraper funciona correctamente")
        print("   2. Usar con moderación para evitar bloqueos")
    
    print("   3. La funcionalidad CSV está operativa")
    print("   4. Revisar archivo 'busqueda_simulada.csv' generado")

if __name__ == "__main__":
    main()