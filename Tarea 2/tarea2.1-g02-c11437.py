# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 2. Entrada y Salida de Datos con manejo de excepciones y Operadores.
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

    # Conversión a radianes.
    rad=float(grados*(pi/180))

    # Ecuación valor_aprox.
    valor_aprox=(rad)-((rad**3)/factorial(3))+((rad**5)/factorial(5))-((rad**7)/factorial(7))+((rad**9)/factorial(9))

    # Ecuación valor_real.
    valor_real=float(sin(rad))

    # Ecuación aprox_error.
    aprox_error=float(valor_real-valor_aprox)

    # Print del valor aproximado.
    print("Valor aproximado con polinomio de Taylor:")
    print("%.6f" % (valor_aprox))
    print("\n")

    # Print del valor real.
    print("Valor real del cálculo de la función seno:")
    print("%.6f" % (valor_real))
    print("\n")

    # Print del error.
    print("Cálculo de error en la aproximación")
    print("%.6f" % (aprox_error))
    print("\n")

    if grados < -180 or grados > 180:
        print("** El error mostrado es muy grande dado el valor del ángulo ingresado. **")

    print("\n")

except:
    print("El valor del ángulo ingresado no es numérico.")
