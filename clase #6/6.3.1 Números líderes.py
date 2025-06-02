'''
Clase:        Clase 6
Tema:         Fortalecimiento
Descripción:  Números líderes 
Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros = list(map(int, input("Ingresa los números: ").split()))  # estas funcionalidades las habíamos usado antes con Ish
lideres = []

mayor = -1
for num in reversed(numeros):
    if num > mayor:
        lideres.append(num)
        mayor = num

lideres.reverse()  # Para mantener el orden original
print("Los números líderes son:", *lideres)
