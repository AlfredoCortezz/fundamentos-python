'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    Juego del Entorno
Descripción:  Completar ejercicio de matriz binaria

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-06-9
Estado:       [ Terminado ]
'''

n = int(input("¿Cuántas filas y columnas tiene la matriz?: "))

m = []

print("Escribe cada fila separando los números con comas: ")
for f in range(n):
    fila = list(map(int, input(f"Fila {f + 1}: ").split(',')))
    m.append(fila)

x = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            x = False
            break

if x:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
