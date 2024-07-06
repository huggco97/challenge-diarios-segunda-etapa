#Búsqueda en lista ordenada: Implementa una función de búsqueda binaria 
# que determine si un número está en una lista ordenada de 10 elementos.

def obtener_lista():
    #Solicita al usuario ingresar los numeros y convierte la entrada en una lista de enteros
    entrada = input("Ingresa la cantidad de 10 numeros enteros por comas ',' por favor: ")
    lista = list(map(int, entrada.split(",")))
    return lista

def validar_lista(lista):
    #valida que la lista tenga exactamente 10 elementos
    if len(lista) != 10:
        print("La lista no tiene 10 elementos. por favor intenta de nuevo: ")
        return False
    else:
        lista.sort() #ordenar lista

#Solicita la lista al usuario
lista = obtener_lista()
dato = int(input("Ingrese el elemento que desea obtener de la lista ingresada: "))

#Valida la lista y si es correcta, imprime la lista ordenada
resultado = validar_lista(lista)
if resultado:
    print("Lista ordenada: ", resultado)
else:
    print("Intente de nuevo.")

inferior = 0
superior = 10
band = False

while (inferior <= superior):
    mitad = int((inferior + superior)/2)

    if (lista[mitad] == dato):
        band = True
        break
    if (lista[mitad] > dato ):
        sueperior = mitad
        mitad = (inferior + superior)/2
    if (lista[mitad] < dato):
        inferior = mitad
        mitad = (inferior + superior)/2
    

if band == True:
    print(f"El numero ha sido encontrado {mitad}")
else:
    print("El numero no ha sido encontrado ")