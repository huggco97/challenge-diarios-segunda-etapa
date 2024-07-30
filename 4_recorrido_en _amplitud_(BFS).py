#Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.
from collections import deque

grafo = {
    0 : [1, 2],
    1 : [0, 3],
    2 : [0, 4],
    3 : [1],
    4 : [2]
}

def BFS(grafo, nodo_inicio):

    cola = deque()
    visitado = [False] * len(grafo)
    nodo_inicio = 0

    visitado[nodo_inicio] = True
    cola.append(nodo_inicio)

    while cola:

        nodo_actual = cola.popleft()
        print(f"Visitado nodo{nodo_actual}")

        for vecino in grafo[nodo_actual]:
            if not visitado[vecino]:
                visitado[vecino] = True
                cola.append(vecino)

BFS(grafo, 0)