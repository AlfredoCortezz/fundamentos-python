'''
Clase:        Clase 7
Tema:         Introducción a NumPy 
Ejercicio:    Cuestionario
Descripción:  completar cuestionario en base el array

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros(5)
print(zeros)

ones = np.ones(5)
print(ones)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2

resultado = arr1 * arr2

arr = np.array([1, 2, 3])
result = arr + 5

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# Recupera los elementos donde la condición es verdadera: [3, 4, 5]

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 
# Recupera los elementos en los índices especificados: [1, 3, 5]


#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales