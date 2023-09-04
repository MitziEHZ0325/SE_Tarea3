# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:04:12 2023

@author: Mitzi
"""

# Definición de las reglas
reglas = [
    {"condiciones": {"vegetariano": True}, "consecuente": "Te recomendamos una ensalada."},
    {"condiciones": {"vegano": True}, "consecuente": "Te recomendamos una opción vegana."},
    {"condiciones": {"vegetariano": False, "vegano": False}, "consecuente": "Puedes elegir cualquier opción del menú."}
]

# Preferencias del usuario
preferencias_usuario = {
    "vegetariano": True,  # El usuario es vegetariano
    "vegano": False       # El usuario no es vegano
}

# Función de encadenamiento de reglas
def encadenamiento_reglas(reglas, preferencias_usuario):
    for regla in reglas:
        condiciones_cumplidas = all(preferencias_usuario[condicion] == valor for condicion, valor in regla["condiciones"].items())
        if condiciones_cumplidas:
            return regla["consecuente"]
    return "No podemos hacer una recomendación en base a tus preferencias."

# Realizar la inferencia
recomendacion = encadenamiento_reglas(reglas, preferencias_usuario)

# Imprimir la recomendación
print(recomendacion)
