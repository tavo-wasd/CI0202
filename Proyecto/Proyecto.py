# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Proyecto: Método de reducción Gauss-Jordan
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

import numpy as np

#  _____ _    ____  _____   _   _ _   _  ___  
# |  ___/ \  / ___|| ____| | | | | \ | |/ _ \ 
# | |_ / _ \ \___ \|  _|   | | | |  \| | | | |
# |  _/ ___ \ ___) | |___  | |_| | |\  | |_| |
# |_|/_/   \_\____/|_____|  \___/|_| \_|\___/ 
# --------------- Operaciones ----------------

# Función intercambiar
def intercambiar_filas(matriz, i, j):
    fila_actual_1 = matriz[i]
    fila_actual_2 = matriz[j]
    matriz[i] = fila_actual_2
    matriz[j] = fila_actual_1

# Función multiplicar
def multiplicar_fila(matriz, i, k):
    fila = matriz[i]
    for elemento in range(len(fila)):
        fila[elemento] *= k
    matriz[i] = fila

# Función sumar
def suma_fila(matriz, j, i, k):
    fila_j = matriz[j]
    fila_i = matriz[i]
    for elemento in range(len(fila_i)):
        fila_j[elemento] += k*(fila_i[elemento])

#  _____ _    ____  _____   ____   ___  ____  
# |  ___/ \  / ___|| ____| |  _ \ / _ \/ ___| 
# | |_ / _ \ \___ \|  _|   | | | | | | \___ \ 
# |  _/ ___ \ ___) | |___  | |_| | |_| |___) |
# |_|/_/   \_\____/|_____| |____/ \___/|____/ 
# -------------- Gauss-Jordan ----------------

# Función reducción
#def gauss_jordan(matriz)

#  _____ _    ____  _____   _____ ____  _____ ____  
# |  ___/ \  / ___|| ____| |_   _|  _ \| ____/ ___| 
# | |_ / _ \ \___ \|  _|     | | | |_) |  _| \___ \ 
# |  _/ ___ \ ___) | |___    | | |  _ <| |___ ___) |
# |_|/_/   \_\____/|_____|   |_| |_| \_\_____|____/ 
# ------------------- Archivos- --------------------                                                  

def cargar_matriz(modo):
    condicion_2 = False
    condicion_34 = False
    archivo_correcto = False
    while condicion_2 == False or condicion_34 == False or archivo_correcto == False:
        try:

            # Verificar que es un archivo correcto
            print("\n")
            nombre = input("Ingrese el nombre de un archivo de matriz en formato csv: ")
            archivo = open(nombre, modo)
            archivo_correcto = True
            matriz = []
            for linea in archivo:
                fila = []
                linea = linea.replace("\n", "")
                lista = linea.split(",")
                for elem_hilera in lista:
                    num = float(elem_hilera)
                    fila.append(num)
                matriz.append(fila)

            # Verificar que cada elemento sea un número real
            for fila_id in range(len(matriz)):
                fila = matriz[fila_id]
                for elemento_id in range(len(fila)):
                    try:
                        float(fila[elemento_id])
                        condicion_2 = True
                    except:
                        condicion_2 = False
                        break
                if condicion_2 == False:
                    break
            if condicion_2 == False:
                print("Todos los elementos de la matriz deben ser números reales")

            # Verificar que la matriz cumpla (n) * (n+1)
            for fila_id in range(len(matriz)):
                if len(matriz[fila_id]) != (len(matriz)+1):
                    print("La matriz debe cumplir para n filas, ser de tamaño (n)*(n+1)")
                    break
                else:
                    condicion_34 = True

        # Excepción, no se pudo leer el archivo
        except:
            print("No se logró identificar el archivo, intente de nuevo.")
    archivo.close()

    # Lectura correcta, cumple condiciones, retorna matriz
    return matriz

#  ____  ____  ___ _   _  ____ ___ ____   _    _
# |  _ \|  _ \|_ _| \ | |/ ___|_ _|  _ \ / \  | |
# | |_) | |_) || ||  \| | |    | || |_) / _ \ | |
# |  __/|  _ < | || |\  | |___ | ||  __/ ___ \| |___
# |_|   |_| \_\___|_| \_|\____|___|_| /_/   \_\_____|
# ---------------------------------------------------

matriz=cargar_matriz("r")

############################### Identificar errores ###################################

print("\n")
print(np.array(matriz))
print("sumando...")
suma_fila(matriz, 0, 1, 2)
print("\n")
print(np.array(matriz))
print("multiplicando...")
multiplicar_fila(matriz, 1, -1)
print("\n")
print(np.array(matriz))
print("intercambiando...")
intercambiar_filas(matriz, 2, 0)
print("\n")
print(np.array(matriz))


############################### PORTAPAPELES ###################################

#archivo.close()

#archivo_str=open(nombre_archivo, "r").read()
#print(archivo_str)
#archivo=open(nombre_archivo, "r")
#nombre_archivo=str(input("Ingrese el nombre de un archivo de matriz en formato csv: "))

#for linea in archivo:
#    print(linea, end='')

#def abrir_archivo(modo):
#    archivo_correcto = False
#    while not(archivo_correcto):
#        print("\n")
#        nombre = input("Ingrese el nombre de un archivo de matriz en formato csv: ")
#        try:
#            archivo = open(nombre, modo)
#            archivo_correcto = True
#        except:
#            print("No se logró identificar el archivo, intente de nuevo.")
#    return archivo
#archivo = abrir_archivo("r")
#
#def convertir_a_matriz(archivo):
#    matriz = []
#    for linea in archivo:
#        fila = []
#        linea = linea.replace("\n", "")
#        lista = linea.split(",")
#        for elem_hilera in lista:
#            num = float(elem_hilera)
#            fila.append(num)
#        matriz.append(fila)
#    return matriz
#matriz=convertir_a_matriz(archivo)

