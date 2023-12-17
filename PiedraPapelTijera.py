import random

def gano(eleccion,computadora):
    if eleccion == 1 and computadora == 3:
       print("Ganaste")
    elif eleccion == 2 and computadora == 1:
       print("Ganaste")
    elif eleccion == 3 and computadora == 2:
       print("Ganaste")
    elif eleccion == computadora:
       print("Empate")
    else:
       print("Perdiste")

def decirQueEs(num):
    if num == 1:
       print("La computadora es Piedra")
    
    elif num == 2:
       print("La computadora es Papel")
    
    elif num == 3:
       print("La computadora es Tijera")

def convertirAnumero(eleccion):
    if eleccion == "piedra":
        return  1
    
    elif eleccion == "papel":
        return 2
    
    elif eleccion == "tijera":
         return  3

eleccion = input("Elegi Piedra, Papel o tijera: ")
eleccion = eleccion.lower()

eleccion = convertirAnumero(eleccion)

computadora = random.randint(1,3)
 
decirQueEs(computadora)   

gano(eleccion,computadora)
