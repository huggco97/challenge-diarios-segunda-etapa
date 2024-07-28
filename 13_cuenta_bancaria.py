#Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.
import random

class Cuenta:
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto

   
    def deposito(self, monto, saldo):
        saldo = monto + saldo
        print(f"Su saldo actual es {saldo} ")

    def consulta(self, saldo):
        print(f"Su saldo actual es {saldo} ")

saldo = random.randint(10000, 1000000)

caja_ahorro = Cuenta(saldo, None)
caja_ahorro.consulta(saldo)

monto = int(input("Ingrese el monto que desea depositar:  "))
caja_ahorro.deposito(monto, saldo)
