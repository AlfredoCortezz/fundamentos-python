'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    Juego del Entorno
Descripción:  Completar ejercicio de matriz binaria

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-06-9
Estado:       [ Terminado ]
'''

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
print(f"Ingrese {filas} filas, cada una con {columnas} números separados por comas (ej. 1,0,1,1,0):")
for f in range(filas):
    linea = input(f"Fila {f + 1}: ").split(',')
    if len(linea) != columnas:
        print("Error: se esperaban", columnas, "valores en esta fila.")
        exit()
    fila_numerica = [int(x) for x in linea]
    matriz.append(fila_numerica)

entorno = []
for i in range(filas):
    nueva_fila = []
    for j in range(columnas):
        suma = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                x = i + dx
                y = j + dy
                if 0 <= x < filas and 0 <= y < columnas:
                    suma += matriz[x][y]
        nueva_fila.append(suma)
    entorno.append(nueva_fila)


print("Matriz del entorno:")
for fila in entorno:
    print(fila)
