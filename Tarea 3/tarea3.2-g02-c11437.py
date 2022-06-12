# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Tarea 3. Control de flujo.
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio 2. Factores de un número.

print("""
  ____      _            _               __            _                      
 / ___|__ _| | ___ _   _| | __ _ _ __   / _| __ _  ___| |_ ___  _ __ ___  ___ 
| |   / _` | |/ __| | | | |/ _` | '__| | |_ / _` |/ __| __/ _ \| '__/ _ \/ __|
| |__| (_| | | (__| |_| | | (_| | |    |  _| (_| | (__| || (_) | | |  __/\__ |
 \____\__,_|_|\___|\__,_|_|\__,_|_|    |_|  \__,_|\___|\__\___/|_|  \___||___/

""")

# Para evitar problemas más adelante, se prueba el valor ingresado de una vez con int().
try:
    valor_entrada=int(input("Ingrese un número: "))
    print("\n")
# Inicio de la función, condicionado por su propio rango.
    if valor_entrada >= 0:
    	def lista_factores(valor_entrada):
            print("Factores del número ingresado:")

# Inicio del loop 'for' definido desde 1 hasta el valor_entrada, con incrementos enteros del factor + 1.
            for factor in range(1, valor_entrada+1, 1):
                if valor_entrada % factor == 0:
                    print(factor)
# Llama a la función.
    	lista_factores(valor_entrada)
# El valor ingresado no pertenece al rango.
    else:
    	print("El número ingresado no está en el rango soportado.")

# Bloque de error en caso de ingresar un número que no es entero, u otro valor no válido.
except:
    print("No se digitó un valor válido.")