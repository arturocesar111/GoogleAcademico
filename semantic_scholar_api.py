"""
Semantic Scholar API Client
Módulo para buscar artículos científicos usando la API oficial de Semantic Scholar
"""

import requests
import time
from datetime import datetime
import csv
import os
from typing import List, Dict, Optional


class SemanticScholarAPI:
    """
    Cliente para la API de Semantic Scholar
    Documentación: https://api.semanticscholar.org/
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Inicializa el cliente de la API
        
        Args:
            api_key: API key opcional para mayor límite de rate (recomendado)
        """
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.headers = {
            'User-Agent': 'GoogleAcademicoScraper/1.0',
        }
        
        if api_key:
            self.headers['x-api-key'] = api_key
            
        # Límites de rate (con API key: 100 req/s, sin API key: 1 req/s)
        self.rate_limit_delay = 0.1 if api_key else 1.1
        
    def buscar_articulos(self, query: str, num_resultados: int = 10, campos: Optional[List[str]] = None, 
                        año_desde: Optional[int] = None, año_hasta: Optional[int] = None) -> List[Dict]:
        """
        Busca artículos científicos por término de búsqueda
        
        Args:
            query: Término de búsqueda
            num_resultados: Número de resultados a retornar (máximo 100)
            campos: Lista de campos a incluir en la respuesta
            año_desde: Año mínimo de publicación (opcional)
            año_hasta: Año máximo de publicación (opcional)
            
        Returns:
            Lista de diccionarios con información de los artículos
        """
        if campos is None:
            campos = [
                'paperId', 'title', 'abstract', 'authors', 'year', 
                'citationCount', 'url', 'venue', 'publicationDate',
                'publicationTypes', 'fieldsOfStudy'
            ]
        
        # Limitar número de resultados
        num_resultados = min(num_resultados, 100)
        
        # Construir query con filtros de año si se especifican
        query_final = query
        if año_desde is not None or año_hasta is not None:
            if año_desde is not None and año_hasta is not None:
                query_final += f" year:{año_desde}-{año_hasta}"
            elif año_desde is not None:
                query_final += f" year:{año_desde}-"
            elif año_hasta is not None:
                query_final += f" year:-{año_hasta}"
        
        params = {
            'query': query_final,
            'limit': num_resultados,
            'fields': ','.join(campos)
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/paper/search",
                headers=self.headers,
                params=params,
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            # Procesar y normalizar resultados
            articulos = []
            if 'data' in data:
                for paper in data['data']:
                    articulo = self._procesar_articulo(paper)
                    if articulo:
                        articulos.append(articulo)
            
            # Respetar límites de rate
            time.sleep(self.rate_limit_delay)
            
            return articulos
            
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar artículos: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado: {e}")
            return []
    
    def buscar_por_autor(self, autor: str, num_resultados: int = 10, 
                        año_desde: Optional[int] = None, año_hasta: Optional[int] = None) -> List[Dict]:
        """
        Busca artículos de un autor específico
        
        Args:
            autor: Nombre del autor
            num_resultados: Número de resultados a retornar
            año_desde: Año mínimo de publicación (opcional)
            año_hasta: Año máximo de publicación (opcional)
            
        Returns:
            Lista de artículos del autor
        """
        # Primero buscar el autor
        try:
            response = requests.get(
                f"{self.base_url}/author/search",
                headers=self.headers,
                params={'query': autor, 'limit': 1},
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            if not data.get('data'):
                print(f"No se encontró el autor: {autor}")
                return []
            
            author_id = data['data'][0]['authorId']
            time.sleep(self.rate_limit_delay)
            
            # Obtener papers del autor
            campos = [
                'paperId', 'title', 'abstract', 'authors', 'year', 
                'citationCount', 'url', 'venue', 'publicationDate'
            ]
            
            # Preparar parámetros con filtros de año
            params = {
                'limit': min(num_resultados, 100),
                'fields': ','.join(campos)
            }
            
            # Agregar filtros de año si se especifican
            if año_desde is not None or año_hasta is not None:
                if año_desde is not None and año_hasta is not None:
                    params['year'] = f"{año_desde}-{año_hasta}"
                elif año_desde is not None:
                    params['year'] = f"{año_desde}-"
                elif año_hasta is not None:
                    params['year'] = f"-{año_hasta}"
            
            response = requests.get(
                f"{self.base_url}/author/{author_id}/papers",
                headers=self.headers,
                params=params,
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            # Procesar resultados
            articulos = []
            if 'data' in data:
                for paper in data['data']:
                    articulo = self._procesar_articulo(paper)
                    if articulo:
                        articulos.append(articulo)
            
            time.sleep(self.rate_limit_delay)
            return articulos
            
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar por autor: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado: {e}")
            return []
    
    def buscar_por_titulo(self, titulo: str, num_resultados: int = 10,
                         año_desde: Optional[int] = None, año_hasta: Optional[int] = None) -> List[Dict]:
        """
        Busca artículos por título específico
        
        Args:
            titulo: Título del artículo (puede ser parcial)
            num_resultados: Número de resultados a retornar
            año_desde: Año mínimo de publicación (opcional)
            año_hasta: Año máximo de publicación (opcional)
            
        Returns:
            Lista de artículos con ese título
        """
        # Usar búsqueda general pero con título entrecomillado para mayor precisión
        query_titulo = f'"{titulo}"'
        return self.buscar_articulos(query_titulo, num_resultados, año_desde=año_desde, año_hasta=año_hasta)
    
    def obtener_articulo_por_id(self, paper_id: str, campos: Optional[List[str]] = None) -> Optional[Dict]:
        """
        Obtiene un artículo específico por su ID de Semantic Scholar
        
        Args:
            paper_id: ID del paper en Semantic Scholar
            campos: Lista de campos a incluir
            
        Returns:
            Diccionario con información del artículo o None si no se encuentra
        """
        if campos is None:
            campos = [
                'paperId', 'title', 'abstract', 'authors', 'year', 
                'citationCount', 'url', 'venue', 'publicationDate',
                'publicationTypes', 'fieldsOfStudy', 'references', 'citations'
            ]
        
        try:
            response = requests.get(
                f"{self.base_url}/paper/{paper_id}",
                headers=self.headers,
                params={'fields': ','.join(campos)},
                timeout=30
            )
            
            response.raise_for_status()
            paper = response.json()
            
            time.sleep(self.rate_limit_delay)
            return self._procesar_articulo(paper)
            
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener artículo {paper_id}: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None
    
    def _procesar_articulo(self, paper: Dict) -> Dict:
        """
        Procesa un artículo de la API y lo convierte al formato estándar
        
        Args:
            paper: Datos del artículo de la API
            
        Returns:
            Diccionario con formato normalizado
        """
        try:
            # Procesar autores
            autores = []
            if paper.get('authors'):
                autores = [autor.get('name', 'Autor desconocido') for autor in paper['authors']]
            autores_str = ', '.join(autores[:3])  # Máximo 3 autores
            if len(paper.get('authors', [])) > 3:
                autores_str += ' et al.'
            
            # Procesar información de publicación
            venue = paper.get('venue', '')
            year = paper.get('year', '')
            pub_info = f"{autores_str}"
            if venue:
                pub_info += f" - {venue}"
            if year:
                pub_info += f" - {year}"
            
            # Procesar citaciones
            citation_count = paper.get('citationCount', 0)
            citado_por = f"Citado por {citation_count:,}" if citation_count else "Sin citaciones"
            
            # Procesar campos de estudio
            campos_estudio = []
            if paper.get('fieldsOfStudy'):
                campos_estudio = [campo for campo in paper['fieldsOfStudy'] if campo]
            
            # URL del artículo
            url = paper.get('url', '')
            if not url and paper.get('paperId'):
                url = f"https://www.semanticscholar.org/paper/{paper['paperId']}"
            
            # Procesar campos de forma segura
            resumen = paper.get('abstract')
            if resumen is None:
                resumen = 'Resumen no disponible'
                
            pub_date = paper.get('publicationDate')
            if pub_date is None:
                pub_date = ''
                
            pub_types = paper.get('publicationTypes', [])
            if pub_types is None:
                pub_types = []
                
            articulo = {
                'titulo': paper.get('title', 'Título no disponible'),
                'enlace': url,
                'autores_info': pub_info,
                'resumen': resumen,
                'citado_por': citado_por,
                'versiones': f"Semantic Scholar ID: {paper.get('paperId', 'N/A')}",
                'year': year or '',
                'venue': venue or '',
                'campos_estudio': ', '.join(campos_estudio),
                'paper_id': paper.get('paperId', ''),
                'citation_count': citation_count,
                'publication_date': pub_date,
                'publication_types': ', '.join(pub_types)
            }
            
            return articulo
            
        except Exception as e:
            print(f"Error al procesar artículo: {e}")
            return None


def guardar_articulos_csv(articulos: List[Dict], nombre_archivo: Optional[str] = None, query: str = "") -> str:
    """
    Guarda los artículos en un archivo CSV separado por |
    
    Args:
        articulos: Lista de diccionarios con información de artículos
        nombre_archivo: Nombre del archivo CSV (opcional)
        query: Consulta de búsqueda para incluir en el nombre del archivo
        
    Returns:
        str: Ruta del archivo creado
    """
    # Crear carpeta data si no existe
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    if not nombre_archivo:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        query_safe = "".join(c for c in query if c.isalnum() or c in (' ', '-', '_')).rstrip()
        query_safe = query_safe.replace(' ', '_')[:30]
        if query_safe:
            nombre_archivo = f"semantic_scholar_{query_safe}_{timestamp}.csv"
        else:
            nombre_archivo = f"semantic_scholar_{timestamp}.csv"
    
    if not nombre_archivo.endswith('.csv'):
        nombre_archivo += '.csv'
    
    # Guardar en la carpeta data
    ruta_completa = os.path.join(data_dir, nombre_archivo)
    
    with open(ruta_completa, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'numero', 'titulo', 'autores_info', 'enlace', 'resumen', 
            'citado_por', 'year', 'venue', 'campos_estudio', 'paper_id',
            'citation_count', 'publication_date', 'publication_types',
            'fecha_extraccion'
        ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i, articulo in enumerate(articulos, 1):
            # Función auxiliar para limpiar campos de forma segura
            def safe_strip(value):
                if value is None:
                    return ''
                return str(value).strip()
            
            row = {
                'numero': i,
                'titulo': safe_strip(articulo.get('titulo', '')),
                'autores_info': safe_strip(articulo.get('autores_info', '')),
                'enlace': safe_strip(articulo.get('enlace', '')),
                'resumen': safe_strip(articulo.get('resumen', '')),
                'citado_por': safe_strip(articulo.get('citado_por', '')),
                'year': safe_strip(articulo.get('year', '')),
                'venue': safe_strip(articulo.get('venue', '')),
                'campos_estudio': safe_strip(articulo.get('campos_estudio', '')),
                'paper_id': safe_strip(articulo.get('paper_id', '')),
                'citation_count': articulo.get('citation_count', 0),
                'publication_date': safe_strip(articulo.get('publication_date', '')),
                'publication_types': safe_strip(articulo.get('publication_types', '')),
                'fecha_extraccion': fecha_actual
            }
            writer.writerow(row)
    
    return os.path.abspath(ruta_completa)


def imprimir_articulos(articulos: List[Dict]):
    """
    Función auxiliar para imprimir artículos de forma legible
    
    Args:
        articulos: Lista de diccionarios con información de artículos
    """
    for i, articulo in enumerate(articulos, 1):
        print(f"\n{'='*80}")
        print(f"Artículo {i}")
        print(f"{'='*80}")
        print(f"Título: {articulo['titulo']}")
        if articulo['enlace']:
            print(f"Enlace: {articulo['enlace']}")
        print(f"Autores: {articulo['autores_info']}")
        if articulo['year']:
            print(f"Año: {articulo['year']}")
        if articulo['venue']:
            print(f"Venue: {articulo['venue']}")
        if articulo['resumen'] and articulo['resumen'] != 'Resumen no disponible':
            print(f"Resumen: {articulo['resumen'][:300]}...")
        if articulo['citado_por']:
            print(f"{articulo['citado_por']}")
        if articulo['campos_estudio']:
            print(f"Campos: {articulo['campos_estudio']}")
        if articulo['paper_id']:
            print(f"Semantic Scholar ID: {articulo['paper_id']}")


def imprimir_y_guardar_csv(articulos: List[Dict], nombre_archivo: Optional[str] = None, 
                          query: str = "", mostrar_en_pantalla: bool = True) -> Optional[str]:
    """
    Función combinada que imprime artículos y los guarda en CSV
    
    Args:
        articulos: Lista de diccionarios con información de artículos
        nombre_archivo: Nombre del archivo CSV (opcional)
        query: Consulta de búsqueda para incluir en el nombre del archivo
        mostrar_en_pantalla: Si mostrar los artículos en pantalla (default: True)
        
    Returns:
        str: Ruta del archivo CSV creado
    """
    if mostrar_en_pantalla and articulos:
        imprimir_articulos(articulos)
    
    if articulos:
        archivo_csv = guardar_articulos_csv(articulos, nombre_archivo, query)
        print(f"\n📄 ¡Artículos guardados en CSV!")
        print(f"📁 Archivo: {archivo_csv}")
        print(f"📊 Total de artículos: {len(articulos)}")
        return archivo_csv
    else:
        print("\n⚠️ No hay artículos para guardar en CSV")
        return None