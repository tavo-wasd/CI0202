# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 4. Funciones (Subrutinas)
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 1. Aproximación de la función exponencial.

print("""
    _                        _                         __                    
   / \   _ __  _ __ _____  _(_)_ __ ___   __ _ _ __   / _|_   _ _ __   ___   
  / _ \ | '_ \| '__/ _ \ \/ / | '_ ` _ \ / _` | '__| | |_| | | | '_ \ / __|  
 / ___ \| |_) | | | (_) >  <| | | | | | | (_| | |    |  _| |_| | | | | (__ _ 
/_/   \_\ .__/|_|  \___/_/\_\_|_| |_| |_|\__,_|_|    |_|  \__,_|_| |_|\___(_)
        |_|                                                                  
                                             _       _ 
  _____  ___ __   ___  _ __   ___ _ __   ___(_) __ _| |
 / _ \ \/ / '_ \ / _ \| '_ \ / _ \ '_ \ / __| |/ _` | |
|  __/>  <| |_) | (_) | | | |  __/ | | | (__| | (_| | |
 \___/_/\_\ .__/ \___/|_| |_|\___|_| |_|\___|_|\__,_|_|
          |_| 
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

    def obtener_serie_taylor_exp(rad, cantidad_factores):
        for K in range(1, cantidad_factores, 1):
            if K==cantidad_factores:
                return 1
            else:
                return float(((((x)**K)/(factorial(K)))) + obtener_serie_taylor_exp)

    obtener_serie_taylor_exp

    if grados < -180 or grados > 180:
        print("\n")
        print("** El error mostrado es muy grande dado el valor del ángulo ingresado. **")

    print("\n")

except:
    print("El valor del ángulo ingresado no es numérico.")
