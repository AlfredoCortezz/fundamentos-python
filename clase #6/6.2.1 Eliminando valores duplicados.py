'''
Clase:        Clase 6
Tema:         Fortalecimeinto 
Ejercicio:    6.2.1 Eliminando valores duplicados 
Descripción:  Eliminar elementos duplicados

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros = input("Ingresa tus datos: ").split()
vacio = []

for num in numeros:
    if num not in vacio:
        vacio.append(num)

print(' '.join(vacio))
