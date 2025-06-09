'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    Matriz Simetrica
Descripción:  Completar ejercicio de matriz de simetrica

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-06-9
Estado:       [ Terminado ]
'''


n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

print("Ingrese las filas de la matriz, separando los números con comas:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
    if len(fila) != n:
        print("Error: la fila debe tener exactamente", n, "números.")
        exit()
    matriz.append(fila)

simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
