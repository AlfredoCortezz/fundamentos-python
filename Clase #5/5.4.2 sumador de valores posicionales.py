'''
Clase:        Clase 5
Tema:         Fortalecimeinto 
Descripción:  Sumador de valores posicionales
Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numero = input("Ingresa un número: ")

while len(numero) > 1:
    suma = 0
    for digito in numero:
        suma += int(digito)
    print(f"{numero} = {suma}")
    numero = str(suma)

print(f"El resultado final es: {numero}")
