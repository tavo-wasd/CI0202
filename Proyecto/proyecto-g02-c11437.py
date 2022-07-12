# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Proyecto: Método de reducción Gauss-Jordan
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

#  _____ _    ____  _____   _   _ _   _  ___  
# |  ___/ \  / ___|| ____| | | | | \ | |/ _ \ 
# | |_ / _ \ \___ \|  _|   | | | |  \| | | | |
# |  _/ ___ \ ___) | |___  | |_| | |\  | |_| |
# |_|/_/   \_\____/|_____|  \___/|_| \_|\___/ 
# --------------- Operaciones ----------------

# Función intercambiar
def intercambiar_filas(M, i, j):
    fila_actual_1 = M[i]
    fila_actual_2 = M[j]
    M[i] = fila_actual_2
    M[j] = fila_actual_1

# Función multiplicar
def multiplicar_fila(M, i, k):
    for j in range(len(M[i])):
        M[i][j] *= k

# Función sumar
def suma_fila(M, j, i, k):
    for elemento in range(len(M[i])):
        M[j][elemento] += k*(M[i][elemento])

#  _____ _    ____  _____   ____   ___  ____  
# |  ___/ \  / ___|| ____| |  _ \ / _ \/ ___| 
# | |_ / _ \ \___ \|  _|   | | | | | | \___ \ 
# |  _/ ___ \ ___) | |___  | |_| | |_| |___) |
# |_|/_/   \_\____/|_____| |____/ \___/|____/ 
# -------------- Gauss-Jordan ----------------

# Función reducción Gauss-Jordan
def gauss_jordan(M):

    # Verificar que la matriz cumpla (n) * (n+1)
    for i in range(len(M)):
        if len(M[i]) == (len(M)+1):
            condicion_34 = True
        else:
            return 1 # Archivo no aceptado

    # Reducir fila
    for i in range(len(M)):

        # Revisar si el número es 0
        if M[i][i] == 0:
            # Buscar un sustituto
            for j in range(1, (len(M)+1)):
                if M[i][j] != 0:
                    intercambiar_filas(M, j, i)
                    break
            # Revisar si sigue siendo 0
            if M[i][i] == 0:
                return 2 # No tiene solución

        # Dividir fila por el número
        multiplicar_fila(M, i, ((1)/(M[i][i])))

        # Para el resto de filas se resta de tal
        # forma que la columna i se convierta en 0
        for j in range(len(M)):
            if M[j] != M[i]:
                suma_fila(M, j, i, (-(M[j][i])))
    return M

#  _____ _    ____  _____   _____ ____  _____ ____  
# |  ___/ \  / ___|| ____| |_   _|  _ \| ____/ ___| 
# | |_ / _ \ \___ \|  _|     | | | |_) |  _| \___ \ 
# |  _/ ___ \ ___) | |___    | | |  _ <| |___ ___) |
# |_|/_/   \_\____/|_____|   |_| |_| \_\_____|____/ 
# ------------------- Archivos- --------------------                                                  

def cargar_matriz(modo = "r"):

    # Verificar que el archivo existe
    try:
        print("\n")
        nombre = input("Ingrese el nombre de un archivo de matriz en formato csv: ")
        archivo = open(nombre, modo)
        M = []
        for linea in archivo:
            fila = []
            linea = linea.replace("\n", "")
            lista = linea.split(",")
            for elem_hilera in lista:
                num = float(elem_hilera)
                fila.append(num)
            M.append(fila)
        archivo.close()
    except:
        return 0 # El archivo ingresado no existe

    # Verificar que cada elemento sea un número real
    try:
        for i in range(len(M)):
            for j in range(len(M[i])):
                float(M[i][j])
    except:
        return 1 # Archivo de matriz no aceptado

    # Lectura correcta, cumple condiciones, retorna matriz
    return M

#  ____  ____  ___ _   _  ____ ___ ____   _    _
# |  _ \|  _ \|_ _| \ | |/ ___|_ _|  _ \ / \  | |
# | |_) | |_) || ||  \| | |    | || |_) / _ \ | |
# |  __/|  _ < | || |\  | |___ | ||  __/ ___ \| |___
# |_|   |_| \_\___|_| \_|\____|___|_| /_/   \_\_____|
# ---------------------------------------------------

def principal():

    # Definir la matriz a reducir
    matriz = cargar_matriz()

    # Verificar entrada correcta
    if matriz == 0:
        print("El archivo ingresado no existe.")
        return False
    elif matriz == 1:
        print("Archivo de matriz no aceptado.")
        return False
    else:

        # Realizar el médoto de reducción Gauss-Jordan
        matriz_reducida = gauss_jordan(matriz)

        # Verificar procedimiento correcto
        if matriz_reducida == 1:
            print("Archivo de matriz no aceptado.")
            return False
        elif matriz_reducida == 2:
            print("No existe solución para el sistema.")
            return False
        else:
            return matriz_reducida
matriz_reducida = principal()

if matriz_reducida != False:
    # Escribir Soluciones
    for i in range(len(matriz_reducida)):
        print("v%.d = %.5f" % ((i+1), matriz_reducida[i][-1]), end='\n')


###########################################3

 # NO TOMA EN CUENTA ARCHIVOS VACÍOS

 ##########################################
