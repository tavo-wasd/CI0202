# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Examen Parcial I. Corrección
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Ejercicio Temperatura del invernadero.

print("""       
 _____                                   _                   
|_   _|__ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ __ _ 
  | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _` |
  | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | | (_| |
  |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \__,_|
                   |_|                                       
 ___                                     _                
|_ _|_ ____   _____ _ __ _ __   __ _  __| | ___ _ __ ___  
 | || '_ \ \ / / _ \ '__| '_ \ / _` |/ _` |/ _ \ '__/ _ \ 
 | || | | \ V /  __/ |  | | | | (_| | (_| |  __/ | | (_) |
|___|_| |_|\_/ \___|_|  |_| |_|\__,_|\__,_|\___|_|  \___/ 
                                                          
""")

# Definición de función histograma individual.
def histograma_indiv(temp_error_zona_x, temp_corr_zona_x):
    asteriscos = int(temp_error_zona_x)
    guiones = int(temp_corr_zona_x)
    return str((asteriscos * "*") + (guiones * "-"))

#Definición de función histograma completo.
def histograma(temp_error_zona_1, temp_corr_zona_1, temp_error_zona_2, temp_corr_zona_2):
    if temp_error_zona_1 == 0 and temp_corr_zona_1 == 0:
        print("No se han realizado lecturas aún")
    else:
        print("Zona 1: %s" % histograma_indiv(temp_error_zona_1, temp_corr_zona_1))
        print("Zona 2: %s" % histograma_indiv(temp_error_zona_2, temp_corr_zona_2))

# Definición de función promedio.
def promedio(t1, t2):
    return (t1+t2)/2

# Definición de función menú.
def menu():
    try:
        opcion=int(input("[1=Registro 2=Histograma 3=Salir]: "))
        if opcion == 1:
            return 1
        elif opcion == 2:
            return 2
        elif opcion == 3:
            return 3
        else:
            print("Ingrese una opción válida")
    except:
        print("Ingrese una opción válida")

# Definición de función principal.
def func_principal():
    temp_error_zona_1 = 0   # Definición inicial de variables generales.
    temp_corr_zona_1 = 0
    temp_error_zona_2 = 0
    temp_corr_zona_2 = 0
    opcion = 0
    while opcion != 3:  # Ciclo para invocar función menú, y salida.
        print("\n")
        opcion = menu()
        if opcion == 1:
            try:    # Manejo de errores coordenadas, volver a preguntar en caso de valor incorrecto.
                term_1 = "X"
                while term_1 != "O" and term_1 != "C" and term_1 != "E":
                    term_1 = str(input("Termómetro  1: "))
                    # Manejo de errores temperaturas, volver a preguntar en caso de valor incorrecto.
                temp_1 = "X"
                while True:
                    try:
                        temp_1 = float(input("Temperatura 1: "))
                    except:
                        continue
                    else:
                        break

                term_2 = "X"
                while term_2 != "O" and term_2 != "C" and term_2 != "E" or term_2 == term_1:
                    term_2 = str(input("Termómetro  2: "))

                temp_2 = "X"
                while True:
                    try:
                        temp_2 = float(input("Temperatura 2: "))
                    except:
                        continue
                    else:
                        break

                term_3 = "X"
                while term_3 != "O" and term_3 != "C" and term_3 != "E" or term_3 == term_2 or term_3 == term_1:
                    term_3 = str(input("Termómetro  3: "))

                temp_3 = "X"
                while True:
                    try:
                        temp_3 = float(input("Temperatura 3: "))
                    except:
                        continue
                    else:
                        break
 
                if term_1 == "C":   # Definir correctamente según letra ingresada.
                    term_c = temp_1
                elif term_1 == "E":
                    term_e = temp_1
                else:
                    term_o = temp_1
                if term_2 == "O":
                    term_o = temp_2
                elif term_2 == "E":
                    term_e = temp_2
                else:
                    term_c = temp_2
                if term_3 == "O":
                    term_o = temp_3
                elif term_3 == "C":
                    term_c = temp_3
                else:
                    term_e = temp_3

                term_c = term_c - (term_c * 0.15)   # Correción de desviaciones conocidas.
                term_e = term_e + (term_e * 0.025)
                promedio_zona_1 = promedio(term_o, term_c)  # Asignación de variables promedios tras ajuste.
                promedio_zona_2 = promedio(term_c, term_e)
                print("\n")
                print("Promedio de temperaturas tras ajuste:")  # Print datos calculados.
                print("Zona 1: %.2f" % (promedio_zona_1))
                print("Zona 2: %.2f" % (promedio_zona_2))

                if promedio_zona_1 < 16 or promedio_zona_1 > 25:
                    temp_error_zona_1 += 1
                    print("Lectura errónea en Zona 1.")
                else:
                    temp_corr_zona_1 += 1
    
                if promedio_zona_2 < 16 or promedio_zona_2 > 25:    # Conteo de datos no viables
                    temp_error_zona_2 += 1
                    print("Lectura errónea en Zona 2.")
                else:
                    temp_corr_zona_2 += 1

            except:
                print("Ingrese una opción válida")
            
        if opcion == 2:
            histograma(temp_error_zona_1, temp_corr_zona_1, temp_error_zona_2, temp_corr_zona_2)

    else:
        print("Gracias por usar el sistema!")   # Salida con mensaje.

# Invocar función principal
func_principal()
