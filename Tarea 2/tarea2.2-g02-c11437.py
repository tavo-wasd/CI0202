# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 2. Entrada y Salida de Datos con manejo de excepciones y Operadores.
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 2. Calculadora de nivel de pH en bosques y lagos.

print("""
  ____      _            _           _                         _   _ 
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _   _ __ | | | |
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | | '_ \| |_| |
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | | |_) |  _  |
 \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_| | .__/|_| |_|
                                                        |_|       
""")
from math import log10

try:
    # En esta parte se usa un try para evitar un error en caso de que se ingrese una conecntración que no sea numérica.

    # Input de concentracion_h.
    print("Ingresar la concentración de iones de hidrógeno en mol/L")
    concentracion_h=float(input(": "))
    print("\n")

    # Excepción para una concentración menor o igual a 0.
    if concentracion_h <= 0:
        print("Nivel de pH dada la concentración")
        print("14.0")
        print("\n")
        print("Es Alcalino: True")
        print("Es Neutral: False")
        print("Es Ácido: False")

    # Si no hay indefinición, entonces se continúa con el cálculo.
    else:
        # Ecuación para calcular pH.
        ph=float(-log10(concentracion_h))

        # Print de pH.
        print("Nivel de pH dada la concentración")
        print(ph)
        print("\n")

        # Clasificación según pH.
        print("Es Alcalino: %s" % (ph>7))
        print("Es Neutral: %s" % (ph==7))
        print("Es Ácido: %s" % (ph<7))
except:
    # En caso de que se use un valor no numérico para la concentración y se interrumpa el try.
    print("\n")
    print("Se ingresó un valor de concentración incorrecto.")
    print("\n")
