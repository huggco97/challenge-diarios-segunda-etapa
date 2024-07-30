#Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor con un método para describir el motor...

class Motor:
    def __init__(self, tipo, potencia, consumo):
        self.tipo = tipo
        self.potencia = potencia
        self.consumo = consumo

    def detalles_motor(self):
        print(f"Motor tipo {self.tipo} con potencia de {self.potencia} HP y consume {self.consumo}.")
    

class Auto(Motor):
    def __init__(self, marca, modelo, anho, motor):
        self.marca = marca
        self.modelo = modelo
        self.anho = anho
        self.motor = motor

    def detalles_motor(self):
        self.motor.detalles_motor()
    
mi_motor = Motor('L6 turbo nafta', '650', '20.5/100 lt combustible en ciudad')

mi_auto = Auto('Toyota', 'Supra', 2002, mi_motor)
mi_auto.detalles_motor()
print(mi_auto.marca)

        