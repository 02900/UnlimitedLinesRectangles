import random
import pygame

def InicializarJuego():
    """ Se declaran las estructuras de datos a utilizar para almacenar los
     datos que maneja el programa """

    """Se crea la matriz 9x9 que representa el tablero, 
        un arreglo llamado jugada cuyos primeros dos elementos 
        corresponden los valores de la fila y columna de la ficha a mover
        y el tercer y cuarto elemento la fila y columna a donde se dirige
        por ultimo se declara un arreglo que contendrá los proximos objetos
        a aparecer en cada turno"""

    M = [[0 for i in range(9)] for j in range(9)]
    tipObjeto = list(range(1,8))
    posicion = [0, 0, 0, 0]
    proximosObj = [0, 0, 0]
    return M, tipObjeto, posicion, proximosObj

def ObtenerProximosObjetos ():
    # Almaceno en una lista los proximos tres objetos
    objetosAleatorios = []
    # Genero tres tipos de objetos aleatorios
    for i in range (3):
        # Genero un tipo de objeto aleatorio
        objetosAleatorios.append(random.choice(tipoDeObjeto))
    # Devuelvo la lista que contiene los proximos tres objetos
    return objetosAleatorios

def ColocarProximasFichas (proxFichas : [int]):
    # Genero tres posiciones aleatorias
    for i in range (3):
        # Genero una fila y columna aleatoria
        posicionAleatoria = [random.randint(0, 8), random.randint(0, 8)]
        # La posicion generada no debe estar ocupada. Si lo esta, genera otra posicion nueva
        while N[posicionAleatoria[0]][posicionAleatoria[1]] != 0:
            posicionAleatoria = [random.randint(0, 8), random.randint(0, 8)]
        # Recibo un numero aleatorio
        objetoAleatorio = proxFichas[i]
        #Establezco el (valor correspondiente al) tipo de objeto en la matriz N
        N[posicionAleatoria[0]][posicionAleatoria[1]] = objetoAleatorio


def MostrarEstadoJuego(largo, alto, margen):
    ActualizarTablero(largo, alto, margen)

def ObtenerJugadaValida():
    while True:
        try:
            filaActual = int(input("\n Introduzca la fila de la pieza a mover: "))
            columnaActual = int(input("\n Introduzca la columna de la pieza a mover: "))

            filaDsps = int(input("\n Introduzca la fila a donde mover la ficha: "))
            columnaDsps = int(input("\n Introduzca la columna a donde mover la ficha: "))
            # Verifica que la ficha seleccionada (a mover) este en el tablero 
            # y que la ficha se pueda mover a la casilla seleccionada
            assert(0<=filaActual<=8 and 0<=columnaActual<=8 and N[filaActual][columnaActual] != 0 \
                and 0<=filaDsps<=8 and 0<=columnaDsps<=8 and N[filaDsps][columnaDsps] == 0)
            
            casillaVaciaAlrrededor = False
            
            if 0<filaActual<8 and 0<columnaActual<8:
                for i in range(3):
                    for j in range(3):
                        print(-1 + filaActual + i, -1 + columnaActual + j)
                        if N[-1 + filaActual + i][-1 + columnaActual + j] == 0:
                                casillaVaciaAlrrededor = True
            
            else:
                if filaActual == 0 and 0<columnaActual<8:
                    for i in range (2):
                        for j in range (3):
                            print(filaActual + i, -1 + columnaActual + j)
                            if N[filaActual + i][-1 + columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif 0<filaActual<8 and columnaActual == 0:
                    for i in range (3):
                        for j in range (2):
                            print(-1 + filaActual + i, columnaActual + j)
                            if N[-1 + filaActual + i][columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif filaActual == 0 and columnaActual == 0:
                    for i in range (2):
                        for j in range (2):
                            print(filaActual + i, columnaActual + j)
                            if N[filaActual + i][columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif filaActual == 8 and columnaActual == 0:
                    for i in range (2):
                        for j in range (2):
                            print(-1 + filaActual + i, columnaActual + j)
                            if N[-1 + filaActual + i][columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True
                
                elif filaActual == 0 and columnaActual == 8:
                    for i in range (2):
                        for j in range (2):
                            print(filaActual + i, -1 + columnaActual + j)
                            if N[filaActual + i][-1 + columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif filaActual==8 and 0<columnaActual<8:
                    for i in range (2):
                        for j in range (3):
                            print(-1 + filaActual + i, -1 + columnaActual + j)
                            if N[-1 + filaActual + i][-1 + columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif 0<filaActual<8 and columnaActual == 8:
                    for i in range (3):
                        for j in range (2):
                            print(-1 + filaActual + i, -1 + columnaActual + j)
                            if N[-1 + filaActual + i][-1 + columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

                elif filaActual == 8 and columnaActual == 8:
                    for i in range (2):
                        for j in range (2):
                            print(-1 + filaActual + i, -1 + columnaActual + j)
                            if N[-1 + filaActual + i][-1 + columnaActual + j] == 0:
                                    casillaVaciaAlrrededor = True

            assert (casillaVaciaAlrrededor)
            break
        except:
            print("\n No ha seleccionado una posicion valida. Vuelva a intentarlo")
    jugadaValida = [filaActual, columnaActual, filaDsps, columnaDsps]

    return jugadaValida

def MoverObjetoSeleccionado(filaActual: int, columnaActual: int, filaDsps : int, columnaDsps : int):
    # Asigno el valor de objeto a mover a el lugar movido
    N[filaDsps][columnaDsps] = N[filaActual][columnaActual]

    # Elimino la ficha de su posicion inicial
    N[filaActual][columnaActual] = 0

def InicializarTablero (largo, alto, margen):
    # Limpia la pantalla con Blanco
    pantalla.fill(BLANCO)

    # Declaracion de variable correspondiente a la fuente del texto
    fuente = pygame.font.Font(None, 24)
    # Ciclo que recorre cada fila de la matriz N
    for fila in range(len(N)):
        # Reproduce el texto. "True" significa texto suavizado(anti-aliased).
        # texto es el numero de la fila actual
        texto = fuente.render(str(fila), True, NEGRO)
        # Escribo sobre la pantalla los numeros de filas y columnas
        # Imprimo el numero de la fila actual
        pantalla.blit(texto, [70, 105 + (margen+alto)*fila+margen])
        # Aprovecho que la Matriz es NxN y puedo entonces imprimir la columna 
        # actual usando el mismo texto que el valor de la fila actual
        pantalla.blit(texto, [95 + (margen+largo)*fila+margen, 80])

        # Recorro las columnas de la matriz N
        for columna in range(len(N)):
            # Establezco el color de cada casilla del tablero
            color = GOSTWHITE
            pygame.draw.rect(pantalla, color, [85 + (margen+largo)*columna+margen, 95 + (margen+alto)*fila+margen, largo, alto])

def ActualizarTablero (largo, alto, margen):
    # Esto creo que no es necesario
    InicializarTablero(largo, alto, margen)
    ActualizarFichas(largo, alto, margen)
    # Avanzamos y actualizamos la pantalla con las fichas actuales.
    pygame.display.flip()

def ActualizarFichas (largo, alto, margen):
    colores = ["GOSTWHITE, ROJO, VERDE, AZUL CLARO, ROSADO, NARANJA, AMARILLO, AZUL OSCURO"]
    colores_RGB = [(200, 200, 255), (255, 10, 10), (10, 255, 10), (0, 255, 255), (255, 51, 153), (255, 94, 0), (249, 255, 51), (0, 0, 255)]
    # Selecciona la fuente. Fuente Default, tamaño 25 pt.
    fuente = pygame.font.Font(None, 24)
    textProximos = fuente.render("Proximos: ", True, NEGRO)
    pantalla.blit(textProximos, [90, 25])

    for i in range (3):

        color = colores_RGB[proximosObjetos[i]]

        if proximosObjetos[i] == 7:
            pygame.draw.rect(pantalla, color, [180 + (largo + 5*margen)*i, 20, largo, alto])
        
        else:
            pygame.draw.ellipse(pantalla, color, [180 + (largo + 5*margen)*i, 20, largo, alto])

    # Recorro la matriz N para agregar fichas nuevas
    for fila in range (len(N)):
        for columna in range (len(N)):
            # Color de la ficha a colocar
            color = colores_RGB[N[fila][columna]]
            # Si es siete la figura a colocar es un cuadrado
            if N[fila][columna] == 7:
                pygame.draw.rect(pantalla, color, [85 + (margen+largo)*columna+margen, 95 + (margen+alto)*fila+margen, largo, alto])
            # Sino, se debe colocar un circulo del color que corresponda a su tipo de objeto
            else:
                pygame.draw.ellipse(pantalla, color, [85 + (margen+largo)*columna+margen, 95 + (margen+alto)*fila+margen, largo, alto])

#VARIABLES GLOBALES
NEGRO = (0,0,0)
BLANCO = (255,255,255)
GOSTWHITE = (200, 200, 255)

LARGO = 30
ALTO = 30
MARGEN = 1

# Inicializa el motor de juegos
pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [450,450]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Color Lines")

FinJuego = False

N, tipoDeObjeto, jugada, proximosObjetos = InicializarJuego()
proximosObjetos = ObtenerProximosObjetos()
ColocarProximasFichas(proximosObjetos)
proximosObjetos = ObtenerProximosObjetos()

InicializarTablero(LARGO, ALTO, MARGEN)

# Bucle principal del Programa
while FinJuego == False:
    # Bucle principal de eventos
    for evento in pygame.event.get(): # El usuario realizó alguna acción
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir
            FinJuego = True # Marcamos que hemos acabado y abandonamos este bucle

    MostrarEstadoJuego(LARGO, ALTO, MARGEN)
    jugada = ObtenerJugadaValida()
    MoverObjetoSeleccionado(jugada[0], jugada[1], jugada[2], jugada[3])
    ColocarProximasFichas(proximosObjetos)
    proximosObjetos = ObtenerProximosObjetos()
    MostrarEstadoJuego(LARGO, ALTO, MARGEN)
         
# Cerramos la ventana y salimos.
pygame.quit()