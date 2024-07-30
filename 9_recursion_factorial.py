#Recursión Factorial: Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5).
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)
    
n = 5
resultado = Factorial(n)
print(f"El factorail de {n} es {resultado}")