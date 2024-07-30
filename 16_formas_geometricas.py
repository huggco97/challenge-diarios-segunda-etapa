# Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro. 
# Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos...

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f"Área del rectángulo: {area}")
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base * self.altura)
        print(f"Perímetro del rectángulo: {perimetro}")
        
    

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14 * (self.radio ** 2)
        print(f"Área del circulo: {area}")

    def calcular_perimetro(self):
        perimetro = 2 * 3.14 * self.radio
        print(f"Perímetro del circulo: {perimetro}")

nuevo_rectangulo = Rectangulo(2, 4)
nuevo_rectangulo.calcular_area()
nuevo_rectangulo.calcular_perimetro()

nuevo_circulo = Circulo(3)
nuevo_circulo.calcular_area()
nuevo_circulo.calcular_perimetro()