import random
import time
import tracemalloc

# Implementación básica de QuickSort
def ordenar_rapido(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    pivote = arreglo[len(arreglo) // 2]
    izquierda = [x for x in arreglo if x < pivote]
    medio = [x for x in arreglo if x == pivote]
    derecha = [x for x in arreglo if x > pivote]
    return ordenar_rapido(izquierda) + medio + ordenar_rapido(derecha)

# Implementación optimizada de QuickSort
def ordenar_rapido_optimizado(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    pivote = mediana_de_tres(arreglo)
    izquierda = [x for x in arreglo if x < pivote]
    medio = [x for x in arreglo if x == pivote]
    derecha = [x for x in arreglo if x > pivote]
    return ordenar_rapido_optimizado(izquierda) + medio + ordenar_rapido_optimizado(derecha)

def mediana_de_tres(arreglo):
    primero = arreglo[0]
    medio = arreglo[len(arreglo) // 2]
    ultimo = arreglo[-1]
    return sorted([primero, medio, ultimo])[1]

# Función para medir tiempo y memoria
def medir_rendimiento(arreglo):
    tracemalloc.start()
    tiempo_inicio = time.time()
    arreglo_ordenado = ordenar_rapido(arreglo)
    tiempo_fin = time.time()
    actual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return arreglo_ordenado, tiempo_fin - tiempo_inicio, pico

def medir_rendimiento_optimizado(arreglo):
    tracemalloc.start()
    tiempo_inicio = time.time()
    arreglo_ordenado = ordenar_rapido_optimizado(arreglo)
    tiempo_fin = time.time()
    actual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return arreglo_ordenado, tiempo_fin - tiempo_inicio, pico

# Generación de datos
conjunto_pequeno = [random.randint(0, 1000) for _ in range(100)]
conjunto_mediano = [random.randint(0, 1000) for _ in range(300)]
conjunto_grande = [random.randint(0, 1000) for _ in range(500)]

# Evaluación de la implementación estándar
print("Evaluación de QuickSort estándar:")
for conjunto, nombre in [(conjunto_pequeno, "Pequeño"), (conjunto_mediano, "Mediano"), (conjunto_grande, "Grande")]:
    arreglo_ordenado, tiempo_ejecucion, pico_memoria = medir_rendimiento(conjunto)
    print(f"Conjunto {nombre}: Tiempo de ejecución: {tiempo_ejecucion:.6f}s, Uso máximo de memoria: {pico_memoria / 1024:.2f}KB")

# Evaluación de la implementación optimizada
print("\nEvaluación de QuickSort optimizado:")
for conjunto, nombre in [(conjunto_pequeno, "Pequeño"), (conjunto_mediano, "Mediano"), (conjunto_grande, "Grande")]:
    arreglo_ordenado, tiempo_ejecucion, pico_memoria = medir_rendimiento_optimizado(conjunto)
    print(f"Conjunto {nombre}: Tiempo de ejecución: {tiempo_ejecucion:.6f}s, Uso máximo de memoria: {pico_memoria / 1024:.2f}KB")
