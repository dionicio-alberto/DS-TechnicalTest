import re

def incrementar_cadena(cadena: str) -> str:
    """
    Incrementa una cadena agregando o incrementando el número al final de la misma.
    
    Si la cadena ya termina en un número, el número se incrementa en 1, respetando los ceros iniciales.
    Si la cadena no termina en número, se agrega el número 1 al final.
    
    Args:
        cadena (str): La cadena a procesar.
    
    Returns:
        str: La nueva cadena con el número incrementado o agregado.
    """
    # Buscar si hay un número al final de la cadena
    match = re.search(r"(\d+)$", cadena)
    
    if match:
        # Extraer la parte numérica
        numero_original = match.group(1)
        # Incrementar el número en 1
        numero_incrementado = str(int(numero_original) + 1)
        # Mantener los ceros iniciales
        numero_incrementado = numero_original[:-len(numero_incrementado)] + numero_incrementado \
            if len(numero_original) > len(numero_incrementado) else numero_incrementado
        # Reemplazar el número en la cadena original
        return cadena[:match.start()] + numero_incrementado
    else:
        # Si no hay número, simplemente agregar "1" al final de la cadena
        return cadena + "1"
