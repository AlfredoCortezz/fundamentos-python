import numpy as np
import matplotlib.pyplot as plt

fs = 100
tiempo = np.linspace(0, 5, 5 * fs)

#funcion para generar empuje
def generarEmpuje(tiempo, top, ancho, desplazamiento):
    curvaBase = top * np.exp(-((tiempo - desplazamiento) * 2) / (2 * ancho * 2))
    ondulacion = 0.01 * top * np.sin(25 * tiempo)
    decae = 1 - 0.151 * np.exp(-(tiempo - desplazamiento) * 2)
    return curvaBase * decae + ondulacion

#datos del combustible
datosDelCombustibles = {
    "APCP": {"color": "orange", "top": 500, "ancho": 0.5, "desplazamiento": 2.0},
    "Polvo negro": {"color": "green", "top": 150, "ancho": 0.4, "desplazamiento": 1.5},
    "HDC": {"color": "gray", "top": 400, "ancho": 0.6, "desplazamiento": 2.2},
    "Zinc-Azufre": {"color": "red", "top": 350, "ancho": 0.7, "desplazamiento": 2.5},
    "ANCP": {"color": "blue", "top": 300, "ancho": 0.8, "desplazamiento": 2.8},
}

for nombre, parametros in datosDelCombustibles.items():
    empuje = generarEmpuje(tiempo, parametros["top"], parametros["ancho"], parametros["desplazamiento"])
    empuje = np.clip(empuje, 0, None)
    plt.bar(tiempo, empuje / 100, width=0.04, label=nombre, color=parametros["color"])

plt.title("Empuje de combustibles sólidos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Empuje (kN)")
plt.legend()
plt.show()
