# Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase derivada 
# Círculo que extienda Figura y sobreescriba el método imprimir...

class Figura:
    def __init__(self, base, altura, diametro):
        self.base = base
        self.altura = altura
        self.diametro = diametro

    def imprimir(self):
        print("Soy una figura con")


class Circulo(Figura):
    def __init__(self, diametro, radio):
        super().__init__(None, None, diametro)
        self.radio = radio

    def imprimir(self):
        print(f"Soy un circulo con radio {self.diametro} y diametro {self.radio} ")
    
circulo = Circulo(10,5)
circulo.imprimir()