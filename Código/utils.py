import numpy
import random

def creartablero(tamano=10):
    return numpy.full((tamano, tamano), "_")
'''
Creamos el tablero con numpy.
'''

def crearbarco(eslora):
    while True:
        casilla0 = (random.randint(1, 9), random.randint(1, 9))
        orientacion = random.choice(["horizontal", "vertical", "diagonal"])
        barco = [casilla0]
        casilla = casilla0
        while len(barco) < eslora:
            if orientacion == "horizontal" and casilla[1] + 1 <= 9:
                casilla = (casilla[0], casilla[1] + 1)
            elif orientacion == "vertical" and casilla[0] + 1 <= 9:
                casilla = (casilla[0] + 1, casilla[1])
            elif orientacion == "diagonal" and casilla[0] + 1 <= 9 and casilla[1] + 1 <= 9:
                casilla = (casilla[0] + 1, casilla[1] + 1)
            else:
                break
            barco.append(casilla)
        if len(barco) == eslora:
            return barco
       
def barcos(lista_barcos=[]):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        lista_barcos.append(crearbarco(eslora))
    return lista_barcos
'''
Una funcion para que, por cada unidad en la lista de esloras reproduzca pares de coordenadas, y los liste.
'''

def colocarbarcos(tablero, lista_barcos):
    for barco in lista_barcos:
        while not all(tablero[casilla[0], casilla[1]] == "_" for casilla in barco):
            barco = crearbarco(len(barco))
        for casilla in barco:
            tablero[casilla[0], casilla[1]] = "O"
    return tablero
'''
Intento de conseguir que convierta las coordenadas de los barcos en casillas 
y al mismo tiempo, compruebe que, si hay dos barcos en una misma casilla, se elabore otra nueva lista.
'''

def verificar_hundido(barco, tablero):
    return all(tablero[casilla[0], casilla[1]] == "X" for casilla in barco)
'''
Una funcion para poder terminar la partida. 
'''

def creatableros(barcosj1, barcoscpu):
    tableroj = creartablero(310)
    tablerocpu = creartablero(10)
    
    tableroj = colocarbarcos(tableroj, barcosj1)
    tablerocpu = colocarbarcos(tablerocpu, barcoscpu)
    
    return tableroj, tablerocpu
'''
Antes de empezar el juego, que coloque los barcos ya comprobados
'''

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        return "Tocado"
    else:
        tablero[casilla] = "A"
        return "AGUA"


def disparo_jugador(tablero_cpu, barcos_cpu):
    errores = 0
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < 10 and 0 <= columna < 10:
                casilla = (fila, columna)
                resultado = disparar(casilla, tablero_cpu)
                print(resultado)
                for barco in barcos_cpu:
                    if verificar_hundido(barco, tablero_cpu):
                        print("¡Tocado y hundido!")
                if resultado == "Tocado":
                    continue  # Permitir otro disparo si acierta el jugador.
                break
            else:
                print("Coordenadas fuera del mapa. Inténtalo de nuevo.")
        except ValueError:
            errores += 1
            print("Introduzca únicamente números por favor.")
            if errores >= 3:
                print("Demasiados errores. Saliendo del juego.")
                exit()
            '''
            Una forma simple para salir del juego.
            '''    

def disparo_cpu(tablero_jugador, barcos_jugador):
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        casilla = (fila, columna)
        resultado = disparar(casilla, tablero_jugador)
        print(f"HAL dispara a ({fila}, {columna}): {resultado}")
        for barco in barcos_jugador:
            if verificar_hundido(barco, tablero_jugador):
                print("¡Tocado y hundido! BUAHAHA")
        if resultado == "Tocado":
            continue  
        break

def vista_oculta(tablero):
    tablero_mostrar = numpy.where(tablero == "-", "A", tablero)
    return numpy.where(numpy.isin(tablero_mostrar, ["X", "A"]), tablero_mostrar, "_")
#Una funcion para que antes de los disparos muestre el mapa del contrario con los barcos ocultos y solo muestre los dispareoa

def hundirflota():
    barcosj1 = barcos()
    barcoscpu = barcos([])
    tableroj, tablerocpu = creatableros(barcosj1, barcoscpu)
    
    turno_jugador = True
    
    while True:
        if turno_jugador:
            print("Tablero de la Maquina:")
            print(vista_oculta(tablerocpu))
            disparo_jugador(tablerocpu, barcoscpu)
            turno_jugador = False
        else:
            disparo_cpu(tableroj, barcosj1)
            print("Tu tablero:")
            print(tableroj)
            turno_jugador = True
        '''
        Para los turnos, con la funcion True false y que vaya cambiando y jugando automaticamente
        '''
        if numpy.all(tablerocpu != "O"):
            print("¡Felicidades! Has hundido todos los barcos del ordenador. \n ""My mind is going, I can feel it...""")
            break
        elif numpy.all(tableroj != "O"):
            print("HAL ha hundido todos tus barcos. ¡Has perdido!")
            break