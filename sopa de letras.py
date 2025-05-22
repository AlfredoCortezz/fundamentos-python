words = ["PAJARO", "GATO", "GATOS", "PERRO", "TIGRE", "RATON"] #Mayuscyulas esta la sopa de letras, sino vamos a usar lowe
lineas = []
with open("sopa_de_letras.txt", "r") as f:
    for filas in f:
        letters = filas.strip().split()
        lineas.append(letters)
print(lineas)
num_filas = 0
for filas in lineas:
    string = ''.join(filas)
    for word in words:
        x = string.find(word)
        if x != -1:
            print(f"[{word}], [{num_filas},{x}]")
    num_filas +=1