# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 4. Funciones (Subrutinas)
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 1. Aproximación de la función seno.

print("""
    _                        _                              
   / \   _ __  _ __ _____  _(_)_ __ ___   __ _ _ __    __ _ 
  / _ \ | '_ \| '__/ _ \ \/ / | '_ ` _ \ / _` | '__|  / _` |
 / ___ \| |_) | | | (_) >  <| | | | | | | (_| | |    | (_| |
/_/   \_\ .__/|_|  \___/_/\_\_|_| |_| |_|\__,_|_|     \__,_|
        |_|                                                 
                                          _____           _            
 ___  ___ _ __   ___     ___ ___  _ __   |_   _|_ _ _   _| | ___  _ __ 
/ __|/ _ \ '_ \ / _ \   / __/ _ \| '_ \    | |/ _` | | | | |/ _ \| '__|
\__ \  __/ | | | (_) | | (_| (_) | | | |   | | (_| | |_| | | (_) | |   
|___/\___|_| |_|\___/   \___\___/|_| |_|   |_|\__,_|\__, |_|\___/|_|   
                                                    |___/ 
""")
from math import sin, pi, factorial

try:

    # Input de variable en grados.
    print("Ingresar el valor del ángulo en grados")
    grados=float(input(": "))
    print("\n")

    # Input de cantidad de factores
    print("Ingresar cantidad de factores deseados")
    cantidad_factores=int(input(": "))
    print("\n")

    # Conversión a radianes.
    rad=float(grados*(pi/180))

    def obtener_serie_taylor_seno(rad, cantidad_factores)
        for n in range(1, cantidad_factores, 1):
            if n==cantidad_factores:
                return 1
            else:
                return float((((((-1)**n)/(factorial(2n+1)))*(((rad)**(2n+1)))) + obtener_serie_taylor_seno))

    obtener_serie_taylor_seno

    if grados < -180 or grados > 180:
        print("\n")
        print("** El error mostrado es muy grande dado el valor del ángulo ingresado. **")

    print("\n")

except:
    print("El valor del ángulo ingresado no es numérico.")
