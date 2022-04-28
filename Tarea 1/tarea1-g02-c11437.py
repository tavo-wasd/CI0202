# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 1. Variables y tipos de dato
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 1. Ecuación de la recta lineal con dos puntos ordenados.

print("""
  ____      _            _           _                       _
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _    __| | ___
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |  / _` |/ _ |
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | | (_| |  __/
 \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|  \__,_|\___|

               _          _ _                  _
 _ __ ___  ___| |_ __ _  | (_)_ __   ___  __ _| |
| '__/ _ \/ __| __/ _` | | | | '_ \ / _ \/ _` | |
| | |  __/ (__| || (_| | | | | | | |  __/ (_| | |
|_|  \___|\___|\__\__,_| |_|_|_| |_|\___|\__,_|_|
""")

# Ingreso de coordenadas de puntos ordenados:
# Se definen como float para no definirlo por separado en cada operación
print("Escriba la coordenada x del punto 1: ")
x1 = float(input("= "))
print("Escriba la coordenada y del punto 1: ")
y1 = float(input("= "))
print("Escriba la coordenada x del punto 2: ")
x2 = float(input("= "))
print("Escriba la coordenada y del punto 2: ")
y2 = float(input("= "))

# Definición de variables como operaciones entre datos float:
ecm = float((y2 - y1) / (x2 - x1))
ecb = float(y1 - ecm * x1)

# Print de variables 'm' y 'b', según el input del usuario, se redondea:
print("\n")
print("Valor de 'm':")
print(round(ecm, 2))
print("\n")
print("Valor de 'b':")
print(round(ecb, 2))

# Print de la función de la recta, se redondea, se escriben las variables como str:
print("\n")
print("Ecuación de la recta:")
print("f(x) =", (str(round(ecm, 2))) + "x", "+", (str(round(ecb, 2))))

# Fin del código
print ("\n")

# Ejercicio 2. Longitud de los cables del puente colgante.

print("""
 ____                   _                   _                   _       
|  _ \ _   _  ___ _ __ | |_ ___    ___ ___ | | __ _  __ _ _ __ | |_ ___ 
| |_) | | | |/ _ \ '_ \| __/ _ \  / __/ _ \| |/ _` |/ _` | '_ \| __/ _ |
|  __/| |_| |  __/ | | | ||  __/ | (_| (_) | | (_| | (_| | | | | ||  __/
|_|    \__,_|\___|_| |_|\__\___|  \___\___/|_|\__, |\__,_|_| |_|\__\___|
                                              |___/
""")

# Ingreso de coordenadas de puntos ordenados:
print("Escriba la coordenada x de un punto en la función cuadrática:")
x = input("= ")
print("Escriba la coordenada y de un punto en la función cuadrática:")
y = input("= ")

# Ingreso de distancia del puente en metros:
print("Escriba la distancia del puente en metros:")
dist = float(input("= "))

# Definición de variables como operaciones entre datos float:
eca = float(float(y) / (float(x) ** 2))
ecy = float(eca * (dist ** 2))

# Print del criterio de la función cuadrática, se escriben las variables como str:
print("\n")
print("Función cuadrática que representa al puente:")
print("f(x) =", "(" + str(y), "/", str(x) + "^2" + ")" + "x^2")

# Print de la longitud de cable necesaria, con redondeo:
print("\n")
print("Longitud de cable necesaria en pies:")
print(round(ecy, 2))

# Fin del código
print("\n")
