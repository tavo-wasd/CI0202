# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 3. Control de flujo.
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 1. Función cuadrática.

print("""
 ____        _            _                             _      
/ ___|  ___ | |_   _  ___(_) ___  _ __   ___  ___    __| | ___ 
\___ \ / _ \| | | | |/ __| |/ _ \| '_ \ / _ \/ __|  / _` |/ _ | 
 ___) | (_) | | |_| | (__| | (_) | | | |  __/\__ \ | (_| |  __/
|____/ \___/|_|\__,_|\___|_|\___/|_| |_|\___||___/  \__,_|\___|
                  ___  
 _   _   _____   / _ \ 
| | | | |_____| | | | |
| |_| | |_____| | |_| |
 \__, |          \___/ 
 |___/ 
""")

from math import sqrt

# Al estar encerrada en el try, si falla la entrada de tipo float, se interrumpe y ejecuta el except.
try:
    valor_a=float(input("a = "))
    valor_b=float(input("b = "))
    valor_c=float(input("c = "))
# De nuevo, hace un intento de cálculo que al ser fallido asume que la raíz se indefine y por lo tanto no tiene solución en x.
    try:
# Definición de funciones para cálculo de las soluciones.
        def x_1(valor_a, valor_b, valor_c):
            return (-valor_b + sqrt((valor_b**2)-4*(valor_a*valor_c)))/2*valor_a
        def x_2(valor_a, valor_b, valor_c):
            return (-valor_b - sqrt((valor_b**2)-4*(valor_a*valor_c)))/2*valor_a
# Output en caso de hacer un cálculo correcto.
        print("Las soluciones de la ecuación f(x) = %.2fx^2 + %.2fx + %.2f = 0 son:" % (valor_a, valor_b, valor_c))
        print("x_1 = %.2f y x_2 = %.2f" % (x_1(valor_a, valor_b, valor_c), x_2(valor_a, valor_b, valor_c)))
# Except si la función se indefine en la raíz del discriminante.
    except:
        print("La ecuación no tiene solución real.")
# Except del bloque general, los valores no son numéricos.
except:
    print("No se digitó un valor numérico.")  
