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
            r"(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\s+(\d{4})",  # 23rd August 2017 - 
            r"(([A-Za-z]+)\s+\d{1,2})(?:st|nd|rd|th)?\s+(\d{4})", # August 12nd 2912
            r"(\d{1,2})/(\d{1,2})/(\d{4})",  # 12/09/2014
            r"(\d{1,2})\s+de\s+([A-Za-z]+)\s+de\s+(\d{4})"  # 29 de septiembre de 2014
        ]
        
        # Diccionario de traducción para meses en español
        self.meses_es = {
            "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
            "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
        }
                
        self.meses_en = {
            "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
            "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
        }

    def parse(self, input_string: str) -> Optional[datetime]:
        """
        Intenta analizar una fecha en una cadena de texto y la convierte en un objeto datetime.

        Args:
            input_string (str): Cadena de texto que contiene la fecha a analizar.

        Returns:
            Optional[datetime]: Objeto datetime si se encuentra una fecha válida, 
                                None si no se encuentra una fecha válida.
        """
        
        for pattern in self.date_patterns:
            match = re.search(pattern, input_string, re.IGNORECASE)
            if match:
                try:
                    if pattern == self.date_patterns[0]:
                        day, month_str, year = match.groups()
                        month = datetime.strptime(month_str, "%B").month
                        return datetime(int(year), month, int(day))
                    
                    elif pattern == self.date_patterns[2]:
                        day, month, year = match.groups()
                        return datetime(int(year), int(month), int(day))
                    
                    elif pattern == self.date_patterns[3]:
                        day, month_str, year = match.groups()
                        month = self.meses_es[month_str.lower()]
                        return datetime(int(year), month, int(day))
                    
                    elif pattern == self.date_patterns[2]:
                        month_str, day, year = match.groups()
                        month = datetime.strptime(month_str, "%B").month
                        return datetime(int(year), month, int(day))
                        
                except ValueError:
                    continue
        
        return None


if __name__ == "__main__":
    parser = DateParser()
    input_date: str = input("Por favor, ingresa un texto que contenga una fecha: ")
    result: Optional[datetime] = parser.parse(input_date)
    
    if result:
        print(f"Fecha válida encontrada: {result}")
    else:
        print("No se encontró una fecha válida en el texto ingresado.")
