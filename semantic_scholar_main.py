#!/usr/bin/env python3
"""
Google Académico Scraper - Versión con API de Semantic Scholar
Script principal que usa la API oficial de Semantic Scholar
"""

import sys
import time
from semantic_scholar_api import SemanticScholarAPI, imprimir_y_guardar_csv, imprimir_articulos


def obtener_rango_años():
    """Solicita rango de años para filtrar búsquedas"""
    print("\n📅 FILTRO POR RANGO DE AÑOS")
    print("-" * 40)
    print("Especifica un rango de años para filtrar los resultados:")
    print("Puedes:")
    print("  • Dejar ambos vacíos para buscar en todos los años")
    print("  • Solo especificar 'desde' para artículos desde ese año")
    print("  • Solo especificar 'hasta' para artículos hasta ese año")
    print("  • Especificar ambos para un rango exacto")
    
    año_desde = None
    año_hasta = None
    
    try:
        desde_input = input("\n📅 Año desde (ej: 2020) [Enter=todos]: ").strip()
        if desde_input:
            año_desde = int(desde_input)
            if año_desde < 1900 or año_desde > 2025:
                print("⚠️ Año debe estar entre 1900-2025, usando valor por defecto")
                año_desde = None
                
        hasta_input = input("📅 Año hasta (ej: 2024) [Enter=todos]: ").strip()
        if hasta_input:
            año_hasta = int(hasta_input)
            if año_hasta < 1900 or año_hasta > 2025:
                print("⚠️ Año debe estar entre 1900-2025, usando valor por defecto")
                año_hasta = None
                
        # Validar que el rango tenga sentido
        if año_desde and año_hasta and año_desde > año_hasta:
            print("⚠️ El año 'desde' no puede ser mayor que 'hasta'. Intercambiando valores...")
            año_desde, año_hasta = año_hasta, año_desde
            
    except ValueError:
        print("⚠️ Formato de año inválido, buscando en todos los años")
        año_desde = año_hasta = None
    
    # Mostrar filtro aplicado
    if año_desde and año_hasta:
        print(f"🔍 Filtro aplicado: {año_desde} - {año_hasta}")
    elif año_desde:
        print(f"🔍 Filtro aplicado: desde {año_desde}")
    elif año_hasta:
        print(f"🔍 Filtro aplicado: hasta {año_hasta}")
    else:
        print("🔍 Sin filtro de años - buscando en todos los períodos")
    
    return año_desde, año_hasta


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*70)
    print("🎓 GOOGLE ACADÉMICO - SEMANTIC SCHOLAR API")
    print("="*70)
    print("1. Búsqueda general de artículos")
    print("2. Búsqueda por autor")
    print("3. Búsqueda por título")
    print("4. Obtener artículo por ID")
    print("5. Configurar API Key")
    print("6. Ver información de la API")
    print("7. Salir")
    print("="*70)
    print("📊 Powered by Semantic Scholar API - Sin límites de bloqueo!")
    print("📅 Todas las búsquedas (1-3) incluyen filtro opcional por años")


def busqueda_general(api_client):
    """Realiza una búsqueda general"""
    print("\n📚 BÚSQUEDA GENERAL DE ARTÍCULOS")
    print("-" * 50)
    
    query = input("Ingrese términos de búsqueda: ").strip()
    if not query:
        print("❌ Debe ingresar términos de búsqueda")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-100, default=10): ") or "10")
        num_resultados = max(1, min(100, num_resultados))
    except ValueError:
        num_resultados = 10
    
    # Obtener filtro de años
    año_desde, año_hasta = obtener_rango_años()
    
    # Preguntar sobre CSV
    guardar_csv = input("\n¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    nombre_archivo = None
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando '{query}' en Semantic Scholar...")
    print("⏳ Consultando API...")
    
    try:
        articulos = api_client.buscar_articulos(query, num_resultados, año_desde=año_desde, año_hasta=año_hasta)
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, query)
            else:
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos para esa búsqueda.")
            
    except Exception as e:
        print(f"\n❌ Error durante la búsqueda: {e}")


def busqueda_por_autor(api_client):
    """Realiza una búsqueda por autor"""
    print("\n👤 BÚSQUEDA POR AUTOR")
    print("-" * 40)
    
    autor = input("Ingrese el nombre del autor: ").strip()
    if not autor:
        print("❌ Debe ingresar un nombre de autor")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-100, default=10): ") or "10")
        num_resultados = max(1, min(100, num_resultados))
    except ValueError:
        num_resultados = 10
    
    # Obtener filtro de años
    año_desde, año_hasta = obtener_rango_años()
    
    # Preguntar sobre CSV
    guardar_csv = input("\n¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    nombre_archivo = None
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando artículos de '{autor}'...")
    print("⏳ Consultando API...")
    
    try:
        articulos = api_client.buscar_por_autor(autor, num_resultados, año_desde=año_desde, año_hasta=año_hasta)
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, f"autor_{autor}")
            else:
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos para este autor.")
            
    except Exception as e:
        print(f"\n❌ Error durante la búsqueda: {e}")


def busqueda_por_titulo(api_client):
    """Realiza una búsqueda por título"""
    print("\n📄 BÚSQUEDA POR TÍTULO")
    print("-" * 40)
    
    titulo = input("Ingrese palabras del título: ").strip()
    if not titulo:
        print("❌ Debe ingresar palabras del título")
        return
    
    try:
        num_resultados = int(input("Número de resultados (1-100, default=10): ") or "10")
        num_resultados = max(1, min(100, num_resultados))
    except ValueError:
        num_resultados = 10
    
    # Obtener filtro de años
    año_desde, año_hasta = obtener_rango_años()
    
    # Preguntar sobre CSV
    guardar_csv = input("\n¿Guardar en archivo CSV? (S/n): ").strip().lower()
    guardar_csv = guardar_csv != 'n'
    
    nombre_archivo = None
    if guardar_csv:
        nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
        if not nombre_archivo:
            nombre_archivo = None
    
    print(f"\n🔍 Buscando artículos con título que contenga '{titulo}'...")
    print("⏳ Consultando API...")
    
    try:
        articulos = api_client.buscar_por_titulo(titulo, num_resultados, año_desde=año_desde, año_hasta=año_hasta)
        
        if articulos:
            print(f"\n✅ Se encontraron {len(articulos)} artículos:")
            
            if guardar_csv:
                archivo_csv = imprimir_y_guardar_csv(articulos, nombre_archivo, f"titulo_{titulo}")
            else:
                imprimir_articulos(articulos)
        else:
            print("\n⚠️ No se encontraron artículos con ese título.")
            
    except Exception as e:
        print(f"\n❌ Error durante la búsqueda: {e}")


def buscar_por_id(api_client):
    """Busca un artículo específico por su ID"""
    print("\n🆔 BÚSQUEDA POR ID DE SEMANTIC SCHOLAR")
    print("-" * 50)
    
    paper_id = input("Ingrese el Paper ID de Semantic Scholar: ").strip()
    if not paper_id:
        print("❌ Debe ingresar un Paper ID")
        return
    
    print(f"\n🔍 Buscando artículo con ID '{paper_id}'...")
    print("⏳ Consultando API...")
    
    try:
        articulo = api_client.obtener_articulo_por_id(paper_id)
        
        if articulo:
            print(f"\n✅ Artículo encontrado:")
            imprimir_articulos([articulo])
            
            # Preguntar si guardar en CSV
            guardar_csv = input("\n¿Guardar en archivo CSV? (S/n): ").strip().lower()
            if guardar_csv != 'n':
                nombre_archivo = input("Nombre del archivo CSV (opcional): ").strip()
                if not nombre_archivo:
                    nombre_archivo = None
                archivo_csv = imprimir_y_guardar_csv([articulo], nombre_archivo, f"paper_{paper_id}", False)
        else:
            print("\n⚠️ No se encontró artículo con ese ID.")
            
    except Exception as e:
        print(f"\n❌ Error durante la búsqueda: {e}")


def configurar_api_key():
    """Permite configurar la API Key"""
    print("\n🔑 CONFIGURAR API KEY")
    print("-" * 40)
    print("Para obtener mejores límites de rate (100 req/s vs 1 req/s):")
    print("1. Visita: https://www.semanticscholar.org/product/api")
    print("2. Regístrate y obtén tu API Key")
    print("3. Ingresa tu API Key aquí")
    print("\nNota: La API Key se usará solo para esta sesión.")
    print("Para uso permanente, modifica el código del script.")
    
    api_key = input("\nIngrese su API Key (o Enter para continuar sin ella): ").strip()
    
    if api_key:
        print("✅ API Key configurada para esta sesión")
        return api_key
    else:
        print("ℹ️ Continuando sin API Key (límite de 1 request/segundo)")
        return None


def mostrar_info_api():
    """Muestra información sobre la API"""
    print("\n" + "="*70)
    print("ℹ️  INFORMACIÓN DE LA API DE SEMANTIC SCHOLAR")
    print("="*70)
    print("📋 Características:")
    print("   • API oficial y gratuita")
    print("   • Sin bloqueos como Google Scholar")
    print("   • Datos académicos de alta calidad")
    print("   • Información de citaciones en tiempo real")
    print("   • Campos de estudio categorizados")
    
    print("\n📊 Límites:")
    print("   • Sin API Key: 1 request por segundo")
    print("   • Con API Key: 100 requests por segundo")
    print("   • Máximo 100 resultados por búsqueda")
    
    print("\n🔗 Enlaces útiles:")
    print("   • Documentación: https://api.semanticscholar.org/")
    print("   • Obtener API Key: https://www.semanticscholar.org/product/api")
    print("   • Semantic Scholar: https://www.semanticscholar.org/")
    
    print("\n📄 Datos incluidos en CSV:")
    print("   • Información básica (título, autores, resumen)")
    print("   • Métricas (citaciones, año)")
    print("   • Metadatos (venue, campos de estudio)")
    print("   • IDs únicos para seguimiento")
    
    print("\n💡 Ventajas vs Google Scholar scraping:")
    print("   ✅ Sin riesgo de bloqueo de IP")
    print("   ✅ Datos estructurados y consistentes")
    print("   ✅ Información de citaciones actualizada")
    print("   ✅ API oficial soportada")
    print("   ✅ Mejor para automatización")


def main():
    """Función principal"""
    print("🚀 Iniciando Google Académico con Semantic Scholar API...")
    
    # Configuración inicial
    api_key = None
    api_client = SemanticScholarAPI(api_key)
    
    print("\n✨ ¡Nueva versión con API oficial de Semantic Scholar!")
    print("📈 Sin límites de bloqueo, datos de alta calidad")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                busqueda_general(api_client)
            elif opcion == "2":
                busqueda_por_autor(api_client)
            elif opcion == "3":
                busqueda_por_titulo(api_client)
            elif opcion == "4":
                buscar_por_id(api_client)
            elif opcion == "5":
                nueva_api_key = configurar_api_key()
                if nueva_api_key:
                    api_client = SemanticScholarAPI(nueva_api_key)
                    print("🔄 Cliente API actualizado con nueva API Key")
            elif opcion == "6":
                mostrar_info_api()
            elif opcion == "7":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("\n❌ Opción inválida. Seleccione 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            
        input("\n📱 Presione Enter para continuar...")


if __name__ == "__main__":
    main()