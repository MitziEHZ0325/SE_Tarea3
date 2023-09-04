# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:04:43 2023

@author: Mitzi
"""

class Regla:
    def __init__(self, condiciones, consecuente):
        self.condiciones = condiciones
        self.consecuente = consecuente

    def evaluar(self, preferencias_usuario):
        condiciones_cumplidas = all(preferencias_usuario[condicion] == valor for condicion, valor in self.condiciones.items())
        if condiciones_cumplidas:
            return self.consecuente
        return None

class MotorDeReglas:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def evaluar_preferencias(self, preferencias_usuario):
        for regla in self.reglas:
            resultado = regla.evaluar(preferencias_usuario)
            if resultado:
                return resultado
        return "No podemos hacer una recomendación en base a tus preferencias."

# Definir preferencias del usuario
preferencias_usuario = {
    "vegetariano": True,
    "vegano": False
}

# Crear reglas
regla1 = Regla({"vegetariano": True}, "Te recomendamos una ensalada.")
regla2 = Regla({"vegano": True}, "Te recomendamos una opción vegana.")
regla3 = Regla({"vegetariano": False, "vegano": False}, "Puedes elegir cualquier opción del menú.")

# Crear un motor de reglas
motor_de_reglas = MotorDeReglas()

# Agregar reglas al motor
motor_de_reglas.agregar_regla(regla1)
motor_de_reglas.agregar_regla(regla2)
motor_de_reglas.agregar_regla(regla3)

# Evaluar preferencias del usuario y obtener una recomendación
recomendacion = motor_de_reglas.evaluar_preferencias(preferencias_usuario)

# Imprimir la recomendación
print(recomendacion)
