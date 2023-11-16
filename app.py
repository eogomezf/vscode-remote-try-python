#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# crea un juego llamado 'Piedra, Papel o Tijera' en el que el usuario juega contra la computadora
# el usuario elige una opcion y la computadora elige otra
# las opciones son: piedra, papel o tijera
# la computadora elige una opcion al azar
# el usuario elige una opcion al azar
# el juego determina quien gana
# el juego muestra el resultado
# el juego pregunta si el usuario quiere jugar de nuevo
# Reglas: piedra gana a tijera, tijera gana a papel, papel gana a piedra
# el mini-juego es multijugador y el equipo juega el papel del oponente y elije un elemento al azar de la lista
# el juego termina cuando el usuario decide no jugar mas
# el juego muestra el numero de victorias y derrotas del usuario
# en cada ronda el jugador debe entrar en una de las opciones de la lista (piedra, papel o tijera) y ser informado si ganó o perdió o empató
# el mini-juego debe controlar las entradas del usuario, colocarlas en minuscular e informar al usuario si la opcion no es valida
# al final de cada ronda el juego debe preguntar al usuario si quiere jugar de nuevo

from random import randint

lista = ["piedra", "papel", "tijera"]
opcion = "si"
victorias = 0
derrotas = 0

while opcion == "si":
    usuario = input("Elige piedra, papel o tijera: ")
    usuario = usuario.lower()
    computadora = lista[randint(0,2)]
    print("Computadora: " + computadora)
    if usuario == computadora:
        print("Empate")
    elif usuario == "piedra":
        if computadora == "papel":
            print("Perdiste")
            derrotas += 1
        else:
            print("Ganaste")
            victorias += 1
    elif usuario == "papel":
        if computadora == "tijera":
            print("Perdiste")
            derrotas += 1
        else:
            print("Ganaste")
            victorias += 1
    elif usuario == "tijera":
        if computadora == "piedra":
            print("Perdiste")
            derrotas += 1
        else:
            print("Ganaste")
            victorias += 1
    else:
        print("Esa no es una opcion valida")
    opcion = input("Quieres jugar de nuevo? ")
    opcion = opcion.lower()
print("Victorias: " + str(victorias))
print("Derrotas: " + str(derrotas))
print("Gracias por jugar")


