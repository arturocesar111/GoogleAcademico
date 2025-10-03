#!/usr/bin/env python3
"""
Script de uso práctico del Google Académico Web Scraper
Ejecuta este script para usar el scraper de forma interactiva
"""

import time
import sys
from google_academico import GoogleScholarScraper, imprimir_articulos, imprimir_y_guardar_csv, guardar_articulos_csv


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print("🎓 GOOGLE ACADÉMICO WEB SCRAPER")
    print("="*60)
    print("1. Búsqueda general de artículos")
    print("2. Búsqueda por autor")
    print("3. Búsqueda por título")
    print("4. Ver información del proyecto")
    print("5. Salir")
    print("="*60)
    print("📄 Nota: Todos los resultados se guardan automáticamente en CSV")


def busqueda_general():
    """Realiza una búsqueda general"""
    scraper = GoogleScholarScraper()
    
    print("\n📚 BÚSQUEDA GENERAL DE ARTÍCULOS")
    print("-" * 40)
    
    query = input("Ingrese términos de búsqueda: ").strip()
    if not query:
        print("❌ Debe ingresar términos de búsqueda")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-10, default=3): ") or "3")
        num_resultados = max(1, min(10, num_resultados))
    except ValueError:
        num_resultados = 3
    
    # Preguntar sobre el archivo CSV
    guardar_csv = input("¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando '{query}'...")
    print("⏳ Por favor espere (esto puede tomar unos segundos)...")
    
    try:
        articulos = scraper.buscar_articulos(
            query=query, 
            num_resultados=num_resultados,
            delay=3
        )
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                # Guardar en CSV y mostrar en pantalla
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, query)
            else:
                # Solo mostrar en pantalla
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos.")
            mostrar_consejos_bloqueo()
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "429" in str(e):
            mostrar_consejos_bloqueo()


def busqueda_por_autor():
    """Realiza una búsqueda por autor"""
    scraper = GoogleScholarScraper()
    
    print("\n👤 BÚSQUEDA POR AUTOR")
    print("-" * 40)
    
    autor = input("Ingrese el nombre del autor: ").strip()
    if not autor:
        print("❌ Debe ingresar un nombre de autor")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-10, default=3): ") or "3")
        num_resultados = max(1, min(10, num_resultados))
    except ValueError:
        num_resultados = 3
    
    # Preguntar sobre el archivo CSV
    guardar_csv = input("¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando artículos de '{autor}'...")
    print("⏳ Por favor espere...")
    
    try:
        articulos = scraper.buscar_por_autor(autor, num_resultados)
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                # Guardar en CSV y mostrar en pantalla
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, f"autor_{autor}")
            else:
                # Solo mostrar en pantalla
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos para este autor.")
            mostrar_consejos_bloqueo()
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "429" in str(e):
            mostrar_consejos_bloqueo()


def busqueda_por_titulo():
    """Realiza una búsqueda por título"""
    scraper = GoogleScholarScraper()
    
    print("\n📄 BÚSQUEDA POR TÍTULO")
    print("-" * 40)
    
    titulo = input("Ingrese palabras del título: ").strip()
    if not titulo:
        print("❌ Debe ingresar palabras del título")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-10, default=3): ") or "3")
        num_resultados = max(1, min(10, num_resultados))
    except ValueError:
        num_resultados = 3
    
    # Preguntar sobre el archivo CSV
    guardar_csv = input("¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando artículos con título que contenga '{titulo}'...")
    print("⏳ Por favor espere...")
    
    try:
        articulos = scraper.buscar_por_titulo(titulo, num_resultados)
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                # Guardar en CSV y mostrar en pantalla
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, f"titulo_{titulo}")
            else:
                # Solo mostrar en pantalla
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos con ese título.")
            mostrar_consejos_bloqueo()
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if "429" in str(e):
            mostrar_consejos_bloqueo()


def mostrar_info():
    """Muestra información del proyecto"""
    print("\n" + "="*60)
    print("ℹ️  INFORMACIÓN DEL PROYECTO")
    print("="*60)
    print("📋 Nombre: Google Académico Web Scraper")
    print("👤 Autor: arturocesar111")
    print("🎯 Propósito: Extraer información de artículos científicos de Google Scholar")
    print("\n📚 Características:")
    print("   • Búsqueda general por términos")
    print("   • Búsqueda por autor específico")
    print("   • Búsqueda por título")
    print("   • Extracción de títulos, autores, resúmenes, citaciones")
    print("\n⚠️  Limitaciones:")
    print("   • Google Scholar puede bloquear peticiones excesivas")
    print("   • Uso recomendado solo para investigación y educación")
    print("   • Respetar términos de servicio de Google Scholar")
    print("\n📁 Archivos del proyecto:")
    print("   • google_academico.py - Módulo principal")
    print("   • ejemplo.py - Ejemplos de uso")
    print("   • test_scraper.py - Pruebas básicas")
    print("   • README.md - Documentación completa")


def mostrar_consejos_bloqueo():
    """Muestra consejos para cuando Google Scholar bloquea"""
    print("\n🚫 GOOGLE SCHOLAR ESTÁ BLOQUEANDO LAS PETICIONES")
    print("-" * 50)
    print("💡 Esto es normal. Soluciones:")
    print("   1. Esperar 10-15 minutos antes de volver a intentar")
    print("   2. Usar menos búsquedas por sesión")
    print("   3. Aumentar delays entre peticiones")
    print("   4. Cambiar de red/IP si es posible")
    print("   5. Usar VPN")
    print("\n📝 Para uso en código propio:")
    print("   • Usar delays de 5+ segundos entre peticiones")
    print("   • Limitar número de resultados")
    print("   • Implementar retry con backoff exponencial")


def main():
    """Función principal"""
    print("🚀 Iniciando Google Académico Web Scraper...")
    print("⚠️  Nota: Google Scholar puede limitar peticiones automáticas")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                busqueda_general()
            elif opcion == "2":
                busqueda_por_autor()
            elif opcion == "3":
                busqueda_por_titulo()
            elif opcion == "4":
                mostrar_info()
            elif opcion == "5":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("\n❌ Opción inválida. Seleccione 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            
        input("\n📱 Presione Enter para continuar...")


if __name__ == "__main__":
    main()