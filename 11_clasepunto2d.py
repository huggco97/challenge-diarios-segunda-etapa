#Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas...
class Punto2D:
    def __init__(self, px, py):
        self.px = px
        self.py = py
    
    def imprimir_puntos(self):
        print(f"Los valores de los puntos son: ({self.px}, {self.py})")


punto = Punto2D(5, 3)
punto.imprimir_puntos()

