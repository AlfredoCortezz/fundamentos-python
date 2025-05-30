'''
Clase:        Clase 5
Tema:         Fortalecimeinto 
Ejercicio:    5.4.1 Adivina el número
Descripción:  numeros random

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

import random
y = random.randint(1, 100)

while True:
    x = int(input("Adivina el número (entre 1 y 100): "))
    
    if x < y:
        print("El número secreto es mayor.")
    elif x > y:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")
        break