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

""" Cuesionario """


consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_viernes = consumo[4, 4]  # índice 4 porque es la fila 5 y la columna 5 (empezando desde 0)
print(f"Consumo del hogar 5 el viernes: {consumo_hogar5_viernes}")

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
consumo_ultimos3_domingo = consumo[-3:, 6]  # Últimas 3 filas, columna 6 (domingo)
print(f"Consumo de los últimos 3 hogares el domingo: {consumo_ultimos3_domingo}")

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_finde = np.mean(consumo[:, 5:7], axis=1)
print(f"Promedio de consumo en fines de semana por hogar: {promedio_finde}")

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares?
desviacion_dias = np.std(consumo, axis=0)
dia_mayor_desv = np.argmax(desviacion_dias)
print(f"Día con mayor desviación estándar entre hogares: Día {dia_mayor_desv} (0=Lunes)")
print("Esto indica que ese día los hogares tienen las mayores diferencias entre sí en su consumo energético.")

# 5. Identifica los 3 hogares con menor consumo total durante la semana.
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print(f"Índices de los 3 hogares con menor consumo: {indices_menor_consumo}")
print(f"Valores de consumo total de esos hogares: {valores_menor_consumo}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
nuevo_hogar3 = consumo[2] * 1.10
nuevo_total_hogar3 = np.sum(nuevo_hogar3)
print(f"Nuevo consumo total semanal del hogar 3 tras aumento del 10% diario: {nuevo_total_hogar3}")
