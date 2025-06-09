'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    Diagonal principal y Secundaria
Descripción:  Completar ejercicio

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-06-9
Estado:       [ Terminado ]
'''

n = int(input("Ingrese el tamaño de la matriz : "))

vacio = []


print("Ingrese las filas de la matriz, separando los números con comas :")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
    vacio.append(fila)


diagonal_principal = [vacio[i][i] for i in range(n)]
diagonal_secundaria = [vacio[i][n - 1 - i] for i in range(n)]


print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)
