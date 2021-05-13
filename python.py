import random


class Juan:
    nombre = "juan"
    apellido = 'volpi'
    edad = 43
    hobbie = "Pasear michis"
    numeroRandom = random.randint(1, 10)

    def adivinarNumero(x):
        if(x == Juan.numeroRandom):
            print(Juan.numeroRandom)
            return("Ganaste")
        elif (x != Juan.numeroRandom):
            print(Juan.numeroRandom)
            return("perdiste")

    def calcular(x,  y):
        suma = x + y
        return(suma)


print(Juan.adivinarNumero(input("inserte un numero")))
