# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI0202 Principios de Informática
# Prof. Jose Pablo Ramírez Méndez

# Práctica para Examen 1
# Est. Gustavo A. Calvo Gutiérrez
# Carné C11437
# Grupo 02

# Distancia, tiempo y desplazamiento de bicicletas para 'n' datos.

print("""
 ____        _              ____  _      _      _      _            
|  _ \  __ _| |_ ___  ___  | __ )(_) ___(_) ___| | ___| |_ __ _ ___ 
| | | |/ _` | __/ _ \/ __| |  _ \| |/ __| |/ __| |/ _ \ __/ _` / __|
| |_| | (_| | || (_) \__ \ | |_) | | (__| | (__| |  __/ || (_| \__ |
|____/ \__,_|\__\___/|___/ |____/|_|\___|_|\___|_|\___|\__\__,_|___/
""")

from math import sqrt

#distanciaTotalAnterior=0
#distanciaXAnterior=0
#distanciaYAnterior=0
#distanciaTotal=0
#duracionTotal=0
#lectura=0
#datosInvalidos=0
#CantidadRegistros=0

def EvaluarRutaBicicleta(CantidadRegistros):
    distanciaTotalAnterior=0
    distanciaXAnterior=0
    distanciaYAnterior=0
    distanciaTotal=0
    duracionTotal=0
    lectura=0
    datosInvalidos=0
    CantidadRegistros=0

    try:
        #CantidadRegistros=int(input("Cantidad de Regsitros deseada: "))

        for repetir in range(1, CantidadRegistros, 1):
            print("Registro %d:" % (repetir))
            distancia=float(input("Distancia: "))
            if distancia<0:
                distancia=-distancia
            distanciaTotalActual=distancia
            distanciaTotal=distanciaTotalAnterior+distantciaTotalActual
            distanciaTotalAnterior=distanciaTotal
            direccion=str(input("Dirección: "))
            if direccion==N:
                distanciaXActual=distancia
                distanciaX=distanciaXAnterior+distanciaXActual
                distanciaXAnterior=distanciaX
            elif direccion==S:
                distanciaXActual=-distancia
                distanciaX=distanciaXAnterior+distanciaXActual
                distanciaXAnterior=distanciaX
            elif direccion==E:
                distanciaYActual=distancia
                distanciaY=distanciaYAnterior+distanciaYActual
                distanciaYAnterior=distanciaY
            elif direccion==O:
                distanciaYActual=-distancia
                distanciaY=distanciaYAnterior+distanciaYActual
                distanciaYAnterior=distanciaY
            segundos=float(input("Tiempo: "))
            duracionTotal=duracionAnterior+segundos
            duracionAnterior=duracionTotal
            
            desplazamiento=sqrt(((distanciaY)**2)+((distanciaX)**2))

            def FormatoHMS(duracionTotal):
                segundos = duracionTotal % 86400
                horas = segundos // 3600
                segundos = segundos % 3600
                minutos = segundos // 60
                segundos = segundos % 60
                return "%d:%d:%d" % (horas, minutos, segundos)

        print("Distancia Total: %.1f" % (distanciaTotal))
        print("Desplazamiento: %.2f" % (desplazamiento))
        print("Duración: %s" % (FormatoHMS(duracionTotal)))

    except:
        print("Ha ingresado un valor inválido, regrsando al menú principal...")
        Menu()
        datosInvalidos=datosInvalidos+1

def Menu():
    print("Ingrese la opción deseada.")
    print("1. Ingresar y evaluar ruta bicicleta")
    print("2. Listar estadísticas actuales")
    print("3. Salir")
    opcion=int(input(": "))
    if opcion==1:
        CantidadRegistros=int(input("Cantidad de Regsitros deseada: "))
        EvaluarRutaBicicleta(CantidadRegistros)
        print("\n")
        Menu()
    elif opcion==2:
        print("Cantidad de lecturas realizadas: %d" % (lectura))
        print("Cantidad de datos inválidos %d" % (datosInvalidos))
        print("\n")
        Menu()
    elif opcion==3:
        print("Saliendo")
    else:
        print("Ingrese una opción válida.")
        Menu()

Menu()
