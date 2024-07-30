#Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.

lista = [2, 21, 2, 10, 11, 12, 14, 16, 22, 16]

def eliminardupli(lista):
    lista_sin_duplicados = []
    for i in lista:
        if i not in lista_sin_duplicados:
            lista_sin_duplicados.append(i)

    print(lista_sin_duplicados)

eliminardupli(lista)