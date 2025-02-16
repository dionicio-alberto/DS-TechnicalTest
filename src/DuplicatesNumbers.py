import time
import tracemalloc
import random

def medir_tiempo_memoria(func, lista):
    """
    Mide el tiempo de ejecución y la memoria utilizada por una función.
    """
    tracemalloc.start()
    inicio_tiempo = time.perf_counter()
    resultado = func(lista.copy())  # Copiamos la lista para evitar modificaciones inesperadas
    fin_tiempo = time.perf_counter()
    memoria_usada = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return resultado, fin_tiempo - inicio_tiempo, memoria_usada

# MÉTODO 1: Usando un conjunto (set)
def encontrar_duplicado_set(lista):
    """
    Usa un conjunto para encontrar duplicados en la lista.
    Complejidad: O(N) tiempo, O(N) espacio.
    """
    seen = set()
    for num in lista:
        if num in seen:
            return num
        seen.add(num)
    return None

# MÉTODO 2: Modificando la lista con valores negativos
def encontrar_duplicado_rango(lista):
    """
    Modifica la lista marcando valores como negativos.
    Complejidad: O(N) tiempo, O(1) espacio.
    """
    for i in range(len(lista)):
        indice = abs(lista[i]) - 1
        if lista[indice] < 0:
            return abs(lista[i])
        lista[indice] = -lista[indice]
    return None

# MÉTODO 3: Ordenando la lista primero
def encontrar_duplicado_ordenando(lista):
    """
    Ordena la lista y busca valores consecutivos repetidos.
    Complejidad: O(N log N) tiempo, O(1) espacio.
    """
    lista.sort()
    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            return lista[i]
    return None

# MÉTODO 4: Algoritmo de Floyd (Tortuga y Liebre)
def encontrar_duplicado_floyd(lista):
    """
    Usa el ciclo de Floyd (tortuga y liebre) para encontrar duplicados.
    Complejidad: O(N) tiempo, O(1) espacio.
    """
    tortuga = liebre = lista[0]
    while True:
        tortuga = lista[tortuga]
        liebre = lista[lista[liebre]]
        if tortuga == liebre:
            break
    
    tortuga = lista[0]
    while tortuga != liebre:
        tortuga = lista[tortuga]
        liebre = lista[liebre]
    
    return tortuga

def comparacion(lista_prueba): 
    # Ejecutar y medir cada método
    metodos = {
        "Set": encontrar_duplicado_set,
        "Rango (Negativos)": encontrar_duplicado_rango,
        "Ordenando": encontrar_duplicado_ordenando,
        "Floyd": encontrar_duplicado_floyd
    }

    # Resultados
    for nombre, metodo in metodos.items():
        resultado, tiempo, memoria = medir_tiempo_memoria(metodo, lista_prueba)
        print(f"{nombre}:")
        print(f"  → Duplicado encontrado: {resultado}")
        print(f"  → Tiempo de ejecución: {tiempo:.6f} segundos")
        print(f"  → Memoria usada: {memoria / 1024:.2f} KB")
        print("-" * 50)
