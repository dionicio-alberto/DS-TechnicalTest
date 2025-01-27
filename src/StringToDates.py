import re
from datetime import datetime
from typing import Optional


class DateParser:
    """
    Clase para analizar y convertir fechas desde cadenas de texto a objetos datetime.

    Métodos:
        __init__: Inicializa la clase con patrones de fechas y configuraciones para meses.
        parse: Intenta analizar la fecha desde una cadena de texto.
    """
    
    def __init__(self) -> None:
        """
        Inicializa la clase DateParser con patrones de fechas y traducción de meses en español.
        """
        # Lista de patrones de diferentes formatos de fechas
        self.date_patterns = [
            r"(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{4})",  # 23rd August 2017
            r"(\d{1,2})/(\d{1,2})/(\d{4})",  # 12/09/2014
            r"(\d{1,2})\s+de\s+([A-Za-z]+)\s+de\s+(\d{4})"  # 29 de septiembre de 2014
        ]
        
        # Diccionario de traducción para meses en español
        self.meses_es = {
            "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
            "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
        }

    def parse(self, input_string: str) -> Optional[datetime]:
        """
        Intenta analizar una fecha en una cadena de texto y la convierte en un objeto datetime.

        Args:
            input_string (str): Cadena de texto que contiene la fecha a analizar.

        Returns:
            Optional[datetime]: Objeto datetime si se encuentra una fecha válida, 
                                None si no se encuentra una fecha válida.

        Ejemplos:
            >>> parser = DateParser()
            >>> parser.parse("foo document 23rd August 2017")
            datetime.datetime(2017, 8, 23, 0, 0)
            
            >>> parser.parse("texto texto 12/09/2014")
            datetime.datetime(2014, 9, 12, 0, 0)
            
            >>> parser.parse("Bla 29 de septiembre de 2014 bla bla")
            datetime.datetime(2014, 9, 29, 0, 0)
        """
        for pattern in self.date_patterns:
            match = re.search(pattern, input_string, re.IGNORECASE)
            if match:
                try:
                    # Caso: 23rd August 2017
                    if pattern == self.date_patterns[0]:
                        day, month_str, year = match.groups()
                        month = datetime.strptime(month_str, "%B").month  # Convierte el mes en inglés
                        return datetime(int(year), month, int(day))
                    
                    # Caso: 12/09/2014
                    elif pattern == self.date_patterns[1]:
                        day, month, year = match.groups()
                        return datetime(int(year), int(month), int(day))
                    
                    # Caso: 29 de septiembre de 2014
                    elif pattern == self.date_patterns[2]:
                        day, month_str, year = match.groups()
                        month = self.meses_es[month_str.lower()]  # Convierte el mes en español
                        return datetime(int(year), month, int(day))
                except ValueError:
                    continue  # Si hay un error en la conversión, pasa al siguiente patrón
        
        return None  # Si no encuentra una coincidencia válida, retorna None


if __name__ == "__main__":
    parser = DateParser()
    input_date: str = input("Por favor, ingresa un texto que contenga una fecha: ")
    result: Optional[datetime] = parser.parse(input_date)
    
    if result:
        print(f"Fecha válida encontrada: {result}")
    else:
        print("No se encontró una fecha válida en el texto ingresado.")
