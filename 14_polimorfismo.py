#Polimorfismo: Crea una clase base Animal con un método hacerSonido y una clase derivada Perro que sobrescriba este método.

class Animal:
    def __init__(self, especie, pelo, patas, color):
        self.especie = especie
        self.pelo = pelo
        self.patas = patas
        self.color = color

    def describeme(self):
        print("Soy un animal del tipo ", type(self).__name__ )

    def emitir_sonido(self):
        print("Emitiendo sonido ..... ")


class Perro(Animal):
    def emitir_sonido(self):
        print("GUAU GUAU GUAU.....")
    pass


mi_perro = Perro('mamifero', 'corto', 4, 'negro y blanco')
mi_perro.describeme()
mi_perro.emitir_sonido()
