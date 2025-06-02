
'''
clase:        clase 6
tema:         fortalecimiento
Descripción:  Números líderes 
Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros = list(map(int, input("Ingresa los números: ").split())) #estas funcionalidades las habiamos usado antes con Ish
lideres = []

mayor = -1
for num in reversed(numeros):
    if num > mayor:
        lideres.append(num)
        mayor = num

print("el numero lider es: " *reversed(lideres))