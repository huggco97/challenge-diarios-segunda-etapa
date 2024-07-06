#Escribe una función que ordene una lista de 5 enteros utilizando 
#cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección.


lista = list(map(int, input("Ingresa la cantidad de 8 numeros enteros por comas ',' por favor: ").split(",")))

def ord_burbuja(lista) :
    longitud = len(lista) -1
    
    for i in range(0, longitud):
    #encargado del recorrido
        for j in range(0, longitud): 
        #comparaciones e intercambio
            if lista[j] > lista [j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

print("Lista sin ordenar: ")
print(lista)

print("Lista Ordenda ")
print(ord_burbuja(lista))