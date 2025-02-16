import re

def validar_direccion_ip(direccion: str) -> str:
    """
    Verifica si una dirección IP es IPv4, IPv6 o inválida.
    
    Args:
        direccion (str): Dirección IP a verificar.
    
    Returns:
        str: "IPV4" si es una dirección IPv4 válida, "IPV6" si es IPv6 válida, "Neither" si es inválida.
    """
    # Expresión regular para IPv4 (4 números de 0 a 255 separados por puntos)
    ipv4_regex = re.compile(r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$")
    
    # Expresión regular para IPv6 (8 grupos de 4 caracteres hexadecimales separados por ':')
    ipv6_regex = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    
    if ipv4_regex.match(direccion):
        return "IPV4"
    elif ipv6_regex.match(direccion):
        return "IPV6"
    else:
        return "Neither"

# Casos de prueba

if __name__== "__main__":
    pruebas = [
        "172.16.254.1",       # IPv4
        "2001:0db8:85a3:0:0:8A2E:0370:7334", # IPv6
        "256.256.256.256",   # Inválida
        "192.168.1.01",      # Inválida (ceros a la izquierda en IPv4)
        "2001:db8::8a2e:370:7334"  # IPv6 válido con omisión de ceros
    ]

    for prueba in pruebas:
        print(f"{prueba} -> {validar_direccion_ip(prueba)}")
