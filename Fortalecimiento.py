'''
Clase:        Clase 3
Tema:         Fortalecimeinto y guia de Github
Ejercicio:    Contraseña, calculadora y numero magico
Descripción:  crear por medio de if condicional ejercicios de fortalecimiento

Autor:        Alfredo Enmanuel Cortez Martínez
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''



#op = 7 // 2
#print(op)




#a= b =c = 1
#a = 5
#print(a,b,c)

#total = int(input("Total de tu cuenta: "))




#x = 10 

#if x > 10 and x % 2 == 0:
#    print("a")
#elif x > 10 and x % 2 ==0:
 #   print("b")
#else: 
 #   print("c")            



#-------------------------------------------------------------------------------------------------------------------------------------------

#contraseña

contraseña = input("Digite su contraseña: ")
num = False
letra_mayuscula = False

if len(contraseña) >= 8:
    for i in contraseña:
        if i.isdigit():
            num = True
        elif i.isupper():
            letra_mayuscula = True

    if num and letra_mayuscula:
        print("Contraseña segura")
    else:
        print("Contraseña no segura")
else:
    print("Contraseña no segura (debe tener al menos 8 caracteres)")

#-------------------------------------------------------------------------------------------------------------------

#calculadora de impuestos 

unidades = int(input("Ingrese sus unidades consumidas: "))

valor = 0  

if unidades >= 0 and unidades <= 100:
    valor = 0
elif unidades >= 101 and unidades <= 200:
    valor = (unidades - 100) * 0.5
else:
    valor = (100 * 0.5) + (unidades - 200) * 1

print(f"Total a pagar: ${valor:.2f}")




#-------------------------------------------------------------------------------------------------------------------------------------


#numero magico
num = int(input("Ingrese un numero: "))

if num % 7 == 0 and num % 5 != 0:
    print("Magico")

else:
    print("No magico")

#----------------------------------------------------------------------------------------------------------------------------------------
#propina

total = float(input("Total de la cuenta: "))
porcentaje = float(input("Porcentaje de propina: "))
propina = total * porcentaje / 100
total_final = total + propina
print(f"Total de la cuenta: ${total}")
print(f"Propina: {propina}")
print(f"Total con propina ({int(porcentaje)}%): ${total_final}")

#-----------------------------------------------------------------------------------------------------------------

#Correo

nombre1 = input("Primer nombre: ")
nombre2 = input("Segundo nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

print(f"El correo es: {nombre1}.{nombre2}.{apellido1}.{apellido2}@keyinstitute.edu.sv")


#_----------------------------------------------------------------------------------------------------------------------------------

#año biciesto

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")


#_------------------------------------------------------------------------------------------------------------------

# Posiciones iniciales de los elevadores 
A = int(input("Piso elevador A: "))
B = int(input("Piso elevador B: "))
p = int(input("Piso del usuario: "))

dist_A = abs(p - A)
dist_B = abs(p - B)

if dist_A <= dist_B:
    print("vas en el elevador A")
else:
    print("vas en el elevador B")
