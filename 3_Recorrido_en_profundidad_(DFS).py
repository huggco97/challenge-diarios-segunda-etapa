#Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
grafo = {
    0 : [1, 2],
    1 : [0, 3],
    2 : [0, 4],
    3 : [1],
    4 : [2]
}

visitado = [False, False, False, False, False]

pila = []

def DFS(visitado, grafo, nodo):
    visitado[nodo] = True
    print(nodo)
    pila.append(nodo)

    while pila:
        nodo_actual =  pila[-1]
        encontrado_vecino_no_visitado = False
        
        for vecino in grafo[nodo_actual]:
            if not visitado[vecino]:
                visitado[vecino] = True
                print(vecino)
                pila.append(vecino)

                encontrado_vecino_no_visitado = True

                break

        if not encontrado_vecino_no_visitado:
                pila.pop


DFS(visitado, grafo, 2)