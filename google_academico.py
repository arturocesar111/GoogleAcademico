"""
Google Académico Web Scraper
Módulo para buscar información de artículos científicos en Google Scholar
"""

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus


class GoogleScholarScraper:
    """
    Clase para realizar web scraping de Google Scholar
    """
    
    def __init__(self, user_agent=None):
        """
        Inicializa el scraper
        
        Args:
            user_agent: String con el user agent a usar (opcional)
        """
        self.base_url = "https://scholar.google.com/scholar"
        self.headers = {
            'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def buscar_articulos(self, query, num_resultados=10, delay=2):
        """
        Busca artículos científicos en Google Scholar
        
        Args:
            query: Término de búsqueda
            num_resultados: Número de resultados a retornar (default: 10)
            delay: Tiempo de espera entre peticiones en segundos (default: 2)
            
        Returns:
            Lista de diccionarios con información de los artículos
        """
        articulos = []
        start = 0
        
        while len(articulos) < num_resultados:
            params = {
                'q': query,
                'start': start
            }
            
            try:
                response = requests.get(
                    self.base_url,
                    params=params,
                    headers=self.headers,
                    timeout=10
                )
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'lxml')
                resultados = soup.find_all('div', class_='gs_ri')
                
                if not resultados:
                    break
                
                for resultado in resultados:
                    if len(articulos) >= num_resultados:
                        break
                        
                    articulo = self._extraer_informacion_articulo(resultado)
                    if articulo:
                        articulos.append(articulo)
                
                start += 10
                
                # Delay para evitar ser bloqueado
                if len(articulos) < num_resultados:
                    time.sleep(delay)
                    
            except Exception as e:
                print(f"Error al buscar artículos: {e}")
                break
        
        return articulos[:num_resultados]
    
    def _extraer_informacion_articulo(self, resultado):
        """
        Extrae información de un resultado de búsqueda
        
        Args:
            resultado: Elemento BeautifulSoup con el resultado
            
        Returns:
            Diccionario con información del artículo
        """
        try:
            # Título
            titulo_elem = resultado.find('h3', class_='gs_rt')
            if not titulo_elem:
                return None
                
            # Remover tags [PDF], [HTML], etc.
            for tag in titulo_elem.find_all('span', class_='gs_ctg'):
                tag.decompose()
            
            titulo = titulo_elem.get_text(strip=True)
            
            # Enlace
            enlace_elem = titulo_elem.find('a')
            enlace = enlace_elem.get('href') if enlace_elem else None
            
            # Autores y resumen
            info_elem = resultado.find('div', class_='gs_a')
            autores_info = info_elem.get_text(strip=True) if info_elem else ""
            
            # Resumen
            resumen_elem = resultado.find('div', class_='gs_rs')
            resumen = resumen_elem.get_text(strip=True) if resumen_elem else ""
            
            # Citado por
            citado_elem = resultado.find('div', class_='gs_fl')
            citado_por = ""
            if citado_elem:
                citado_link = citado_elem.find('a', string=lambda x: x and 'Citado por' in x)
                if citado_link:
                    citado_por = citado_link.get_text(strip=True)
            
            # Versiones
            versiones = ""
            if citado_elem:
                versiones_link = citado_elem.find('a', string=lambda x: x and 'versiones' in x)
                if versiones_link:
                    versiones = versiones_link.get_text(strip=True)
            
            articulo = {
                'titulo': titulo,
                'enlace': enlace,
                'autores_info': autores_info,
                'resumen': resumen,
                'citado_por': citado_por,
                'versiones': versiones
            }
            
            return articulo
            
        except Exception as e:
            print(f"Error al extraer información del artículo: {e}")
            return None
    
    def buscar_por_autor(self, autor, num_resultados=10):
        """
        Busca artículos de un autor específico
        
        Args:
            autor: Nombre del autor
            num_resultados: Número de resultados a retornar
            
        Returns:
            Lista de artículos del autor
        """
        query = f'author:"{autor}"'
        return self.buscar_articulos(query, num_resultados)
    
    def buscar_por_titulo(self, titulo, num_resultados=10):
        """
        Busca artículos por título específico
        
        Args:
            titulo: Título del artículo
            num_resultados: Número de resultados a retornar
            
        Returns:
            Lista de artículos con ese título
        """
        query = f'intitle:"{titulo}"'
        return self.buscar_articulos(query, num_resultados)


def imprimir_articulos(articulos):
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
        if articulo['resumen']:
            print(f"Resumen: {articulo['resumen']}")
        if articulo['citado_por']:
            print(f"{articulo['citado_por']}")
        if articulo['versiones']:
            print(f"{articulo['versiones']}")
