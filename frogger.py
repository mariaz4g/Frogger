from OpenGL.GL import *
import glfw
import math
import time

window = None

posicion_x = 0.0
posicion_y = -0.9
velocidad = 0.8
tiempo_anterior = 0.0
angulo_rotacion = 0.0

#Posición de cuadrado azul agua
posicion_cuadrado_agua_x = 0.0
posicion_cuadrado_agua_y = 0.5  

#Posición de cuadrados naranja
posicion_cuadrado_naranja_x = 0.2
posicion_cuadrado_naranja_y = -0.7  
velocidad_naranja = 0.1  # Velocidad del cuadrado naranja

posicion_segundo_cuadrado_naranja_x = 0.7
posicion_segundo_cuadrado_naranja_y = -0.7  

posicion_tercer_cuadrado_naranja_x = -0.3
posicion_tercer_cuadrado_naranja_y = -0.7  

#Posición de cuadrados rojos
posicion_cuadrado_rojo_x = 0.2
posicion_cuadrado_rojo_y = -0.5  
velocidad_rojo = 0.15

posicion_segundo_cuadrado_rojo_x = 0.7
posicion_segundo_cuadrado_rojo_y = -0.5  

posicion_tercer_cuadrado_rojo_x = -0.3
posicion_tercer_cuadrado_rojo_y = -0.5  

#Posición de cuadrados rosas
posicion_cuadrado_rosa_x = 0.2
posicion_cuadrado_rosa_y = -0.35  
velocidad_rosa = 0.3

# Nueva variable para la posición x del segundo cuadrado rosa
posicion_segundo_cuadrado_rosa_x = 0.7
posicion_segundo_cuadrado_rosa_y = -0.35  

# Nueva variable para la posición x del tercer cuadrado rosa
posicion_tercer_cuadrado_rosa_x = -0.3
posicion_tercer_cuadrado_rosa_y = -0.35 

#Posición de cuadrados amarillos
posicion_primer_cuadrado_amarillo_x= 0.3
posicion_primer_cuadrado_amarillo_y= -0.2
velocidad_amarillo = 0.4

#Posición de cuadrados lila
posicion_cuadrado_lila_x = 0.2
posicion_cuadrado_lila_y = -0.1
velocidad_lila = 0.2

posicion_segundo_cuadrado_lila_x = 0.7
posicion_segundo_cuadrado_lila_y = -0.1 

#Posición tortugas
#Primera línea 
#Tortugas 1
posicion_cuadrado_tortuga1_x = -1
posicion_cuadrado_tortuga1_y = 0.1  
velocidad_tortuga = 0.25

posicion_segundo_cuadrado_tortuga1_x = 0.9
posicion_segundo_cuadrado_tortuga1_y = 0.1  

posicion_tercer_cuadrado_tortuga1_x = 0.75
posicion_tercer_cuadrado_tortuga1_y = 0.1

#Tortugas 2
posicion_cuadrado_tortuga2_x = 0.5
posicion_cuadrado_tortuga2_y = 0.1  

posicion_segundo_cuadrado_tortuga2_x = 0.35
posicion_segundo_cuadrado_tortuga2_y = 0.1  

posicion_tercer_cuadrado_tortuga2_x = 0.2
posicion_tercer_cuadrado_tortuga2_y = 0.1

#Tortugas 3
posicion_cuadrado_tortuga3_x = -0.05
posicion_cuadrado_tortuga3_y = 0.1  

posicion_segundo_cuadrado_tortuga3_x = -0.2
posicion_segundo_cuadrado_tortuga3_y = 0.1  

posicion_tercer_cuadrado_tortuga3_x = -0.35
posicion_tercer_cuadrado_tortuga3_y = 0.1

#Tortugas 4
posicion_cuadrado_tortuga4_x = -0.5
posicion_cuadrado_tortuga4_y = 0.1  

posicion_segundo_cuadrado_tortuga4_x = -0.65
posicion_segundo_cuadrado_tortuga4_y = 0.1  

posicion_tercer_cuadrado_tortuga4_x = -0.8
posicion_tercer_cuadrado_tortuga4_y = 0.1

#Segunda línea
#Tortugas 1
posicion_cuadrado_tortuga1_1_x = -1
posicion_cuadrado_tortuga1_1_y = 0.55 
velocidad_tortuga = 0.25

posicion_segundo_cuadrado_tortuga1_2_x = 0.9
posicion_segundo_cuadrado_tortuga1_2_y = 0.55


#Tortugas 2
posicion_cuadrado_tortuga2_1_x = 0.5
posicion_cuadrado_tortuga2_1_y = 0.55  

posicion_segundo_cuadrado_tortuga2_2_x = 0.35
posicion_segundo_cuadrado_tortuga2_2_y = 0.55  


#Tortugas 3
posicion_cuadrado_tortuga3_1_x = -0.05
posicion_cuadrado_tortuga3_1_y = 0.55  

posicion_segundo_cuadrado_tortuga3_2_x = -0.2
posicion_segundo_cuadrado_tortuga3_2_y = 0.55  

#Tortugas 4
posicion_cuadrado_tortuga4_1_x = -0.5
posicion_cuadrado_tortuga4_1_y = 0.55

posicion_segundo_cuadrado_tortuga4_2_x = -0.65
posicion_segundo_cuadrado_tortuga4_2_y = 0.55 


#Troncos
#Troncos 1
posicion_cuadrado_tronco1_x = -0.95
posicion_cuadrado_tronco1_y = 0.25  
velocidad_tronco1 = 0.1

posicion_segundo_cuadrado_tronco1_x = 0.35
posicion_segundo_cuadrado_tronco1_y = 0.25

posicion_tercer_cuadrado_tronco1_x = -0.55
posicion_tercer_cuadrado_tronco1_y = 0.25
#Troncos 2
posicion_cuadrado_tronco2_x = -0.95
posicion_cuadrado_tronco2_y = 0.4 
velocidad_tronco2 = 0.3

posicion_segundo_cuadrado_tronco2_x = 0.35
posicion_segundo_cuadrado_tronco2_y = 0.4

#Troncos 3
posicion_cuadrado_tronco3_x = -0.95
posicion_cuadrado_tronco3_y = 0.7 
velocidad_tronco3 = 0.2

posicion_segundo_cuadrado_tronco3_x = 0.35
posicion_segundo_cuadrado_tronco3_y = 0.7

posicion_tercer_cuadrado_tronco3_x = -0.55
posicion_tercer_cuadrado_tronco3_y = 0.7

# Definir tiempo_colision y tiempo_espera
tiempo_colision = 0.0
tiempo_espera = 0.5

# Posición inicial del triángulo
posicion_inicial_triangulo_x = 0.0
posicion_inicial_triangulo_y = -0.9

def actualizar():
    global posicion_x, posicion_y, angulo_rotacion, tiempo_anterior, window, tiempo_colision, \
        posicion_cuadrado_agua_x, posicion_cuadrado_agua_y, \
        posicion_cuadrado_naranja_x, posicion_cuadrado_naranja_y, posicion_segundo_cuadrado_naranja_x, posicion_segundo_cuadrado_naranja_y, posicion_tercer_cuadrado_naranja_x, posicion_tercer_cuadrado_naranja_y, \
        posicion_primer_cuadrado_amarillo_x, posicion_primer_cuadrado_amarillo_y, \
        posicion_cuadrado_rojo_x, posicion_cuadrado_rojo_y, posicion_segundo_cuadrado_rojo_x, posicion_segundo_cuadrado_rojo_x, posicion_tercer_cuadrado_rojo_x, posicion_tercer_cuadrado_rojo_y, \
        posicion_cuadrado_rosa_x, posicion_cuadrado_rosa_y, posicion_segundo_cuadrado_rosa_x, posicion_cuadrado_rosa_y, posicion_tercer_cuadrado_rosa_x, posicion_tercer_cuadrado_rosa_y, \
        posicion_cuadrado_lila_x, posicion_cuadrado_lila_y, posicion_segundo_cuadrado_lila_x, posicion_segundo_cuadrado_lila_y, \
        posicion_cuadrado_tortuga1_x, posicion_cuadrado_tortuga1_y, posicion_segundo_cuadrado_tortuga1_x, posicion_segundo_cuadrado_tortuga1_y, posicion_tercer_cuadrado_tortuga1_x, posicion_tercer_cuadrado_tortuga1_y, \
        posicion_cuadrado_tortuga2_x, posicion_cuadrado_tortuga2_y, posicion_segundo_cuadrado_tortuga2_x, posicion_segundo_cuadrado_tortuga2_y, posicion_tercer_cuadrado_tortuga2_x, posicion_tercer_cuadrado_tortuga2_y, \
        posicion_cuadrado_tortuga3_x, posicion_cuadrado_tortuga3_y, posicion_segundo_cuadrado_tortuga3_x, posicion_segundo_cuadrado_tortuga3_y, posicion_tercer_cuadrado_tortuga3_x, posicion_tercer_cuadrado_tortuga3_y, \
        posicion_cuadrado_tortuga4_x, posicion_cuadrado_tortuga4_y, posicion_segundo_cuadrado_tortuga4_x, posicion_segundo_cuadrado_tortuga4_y, posicion_tercer_cuadrado_tortuga4_x, posicion_tercer_cuadrado_tortuga4_y, \
        posicion_cuadrado_tortuga1_1_x, posicion_cuadrado_tortuga1_1_y, posicion_segundo_cuadrado_tortuga1_2_x, posicion_segundo_cuadrado_tortuga1_2_y, \
        posicion_cuadrado_tortuga2_1_x, posicion_cuadrado_tortuga2_1_y, posicion_segundo_cuadrado_tortuga2_2_x, posicion_segundo_cuadrado_tortuga2_2_y, \
        posicion_cuadrado_tortuga3_1_x, posicion_cuadrado_tortuga3_1_y, posicion_segundo_cuadrado_tortuga3_2_x, posicion_segundo_cuadrado_tortuga3_2_y, \
        posicion_cuadrado_tortuga4_1_x, posicion_cuadrado_tortuga4_1_y, posicion_segundo_cuadrado_tortuga4_2_x, posicion_segundo_cuadrado_tortuga4_2_y, \
        posicion_cuadrado_tronco1_x, posicion_cuadrado_tronco1_y, posicion_segundo_cuadrado_tronco1_x, posicion_segundo_cuadrado_tronco1_y, posicion_tercer_cuadrado_tronco1_x, posicion_tercer_cuadrado_tronco1_y, \
        posicion_cuadrado_tronco2_x, posicion_cuadrado_tronco2_y, posicion_segundo_cuadrado_tronco2_x, posicion_segundo_cuadrado_tronco2_y, \
        posicion_cuadrado_tronco3_x, posicion_cuadrado_tronco3_y, posicion_segundo_cuadrado_tronco3_x, posicion_segundo_cuadrado_tronco3_y, posicion_tercer_cuadrado_tronco3_x, posicion_tercer_cuadrado_tronco3_y

    
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    # Guardar la posición anterior
    posicion_x_anterior = posicion_x
    posicion_y_anterior = posicion_y

    # get_key regresa PRESS o RELEASE
    estado_flecha_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_flecha_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_flecha_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_flecha_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    if estado_flecha_arriba == glfw.PRESS:
        angulo_rotacion = 0 
        if posicion_y < 0.9:  # Evitar que salga por arriba
            posicion_y += velocidad * tiempo_delta
    elif estado_flecha_abajo == glfw.PRESS:
        angulo_rotacion = 180  
        if posicion_y > -1.0:  # Evitar que salga por abajo
            posicion_y -= velocidad * tiempo_delta
    elif estado_flecha_derecha == glfw.PRESS:
        angulo_rotacion = -90
        if posicion_x < 0.9:  # Evitar que salga por la derecha
            posicion_x += velocidad * tiempo_delta
    elif estado_flecha_izquierda == glfw.PRESS:
        angulo_rotacion = 90 
        if posicion_x > -0.9:  # Evitar que salga por la izquierda
            posicion_x -= velocidad * tiempo_delta

    # Mover los cuadrados a la derecha
    #Amarillo
    posicion_primer_cuadrado_amarillo_x += velocidad_amarillo * tiempo_delta
    if posicion_primer_cuadrado_amarillo_x > 1.0:
        posicion_primer_cuadrado_amarillo_x = -1.0

    #Rojo
    posicion_cuadrado_rojo_x += velocidad_rojo * tiempo_delta
    posicion_segundo_cuadrado_rojo_x += velocidad_rojo * tiempo_delta
    posicion_tercer_cuadrado_rojo_x += velocidad_rojo * tiempo_delta

    if posicion_cuadrado_rojo_x > 1.0:
        posicion_cuadrado_rojo_x = -1.0
    if posicion_segundo_cuadrado_rojo_x > 1.0:
        posicion_segundo_cuadrado_rojo_x = -1.0
    if posicion_tercer_cuadrado_rojo_x > 1.0:
        posicion_tercer_cuadrado_rojo_x = -1.0
    
    #Troncos1
    posicion_cuadrado_tronco1_x += velocidad_tronco1 * tiempo_delta
    posicion_segundo_cuadrado_tronco1_x += velocidad_tronco1 * tiempo_delta
    posicion_tercer_cuadrado_tronco1_x += velocidad_tronco1 * tiempo_delta

    if posicion_cuadrado_tronco1_x > 1.0:
        posicion_cuadrado_tronco1_x = -1.0
    if posicion_segundo_cuadrado_tronco1_x > 1.0:
        posicion_segundo_cuadrado_tronco1_x = -1.0
    if posicion_tercer_cuadrado_tronco1_x > 1.0:
        posicion_tercer_cuadrado_tronco1_x = -1.0

    #Troncos2
    posicion_cuadrado_tronco2_x += velocidad_tronco2 * tiempo_delta
    posicion_segundo_cuadrado_tronco2_x += velocidad_tronco2 * tiempo_delta 
    if posicion_cuadrado_tronco2_x > 1.0:
        posicion_cuadrado_tronco2_x = -1.0
    if posicion_segundo_cuadrado_tronco2_x > 1.0:
        posicion_segundo_cuadrado_tronco2_x = -1.0

    #Troncos3
    posicion_cuadrado_tronco3_x += velocidad_tronco3 * tiempo_delta
    posicion_segundo_cuadrado_tronco3_x += velocidad_tronco3 * tiempo_delta
    posicion_tercer_cuadrado_tronco3_x += velocidad_tronco3 * tiempo_delta

    if posicion_cuadrado_tronco3_x > 1.0:
        posicion_cuadrado_tronco3_x = -1.0
    if posicion_segundo_cuadrado_tronco3_x > 1.0:
        posicion_segundo_cuadrado_tronco3_x = -1.0
    if posicion_tercer_cuadrado_tronco3_x > 1.0:
        posicion_tercer_cuadrado_tronco3_x = -1.0

    # Mover los cuadrados a la izquierda
    #Naranja
    posicion_cuadrado_naranja_x -= velocidad_naranja * tiempo_delta
    posicion_segundo_cuadrado_naranja_x -= velocidad_naranja * tiempo_delta
    posicion_tercer_cuadrado_naranja_x -= velocidad_naranja * tiempo_delta
    if posicion_cuadrado_naranja_x < -1.0:
        posicion_cuadrado_naranja_x = 1.0
    if posicion_segundo_cuadrado_naranja_x < -1.0:
        posicion_segundo_cuadrado_naranja_x = 1.0
    if posicion_tercer_cuadrado_naranja_x < -1.0:
        posicion_tercer_cuadrado_naranja_x = 1.0
    #Rosa
    posicion_cuadrado_rosa_x -= velocidad_rosa * tiempo_delta
    posicion_segundo_cuadrado_rosa_x -= velocidad_rosa * tiempo_delta
    posicion_tercer_cuadrado_rosa_x -= velocidad_rosa * tiempo_delta
    if posicion_cuadrado_rosa_x < -1.0:
        posicion_cuadrado_rosa_x = 1.0
    if posicion_segundo_cuadrado_rosa_x < -1.0:
        posicion_segundo_cuadrado_rosa_x = 1.0
    if posicion_tercer_cuadrado_rosa_x < -1.0:
        posicion_tercer_cuadrado_rosa_x = 1.0
    #Lila
    posicion_cuadrado_lila_x -= velocidad_lila * tiempo_delta
    posicion_segundo_cuadrado_lila_x -= velocidad_lila * tiempo_delta
    if posicion_cuadrado_lila_x < -1.0:
        posicion_cuadrado_lila_x = 1.0
    if posicion_segundo_cuadrado_lila_x < -1.0:
        posicion_segundo_cuadrado_lila_x = 1.0
    #Tortuga linea 1
    posicion_cuadrado_tortuga1_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga1_x -= velocidad_tortuga * tiempo_delta
    posicion_tercer_cuadrado_tortuga1_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga2_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga2_x -= velocidad_tortuga * tiempo_delta
    posicion_tercer_cuadrado_tortuga2_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga3_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga3_x -= velocidad_tortuga * tiempo_delta
    posicion_tercer_cuadrado_tortuga3_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga4_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga4_x -= velocidad_tortuga * tiempo_delta
    posicion_tercer_cuadrado_tortuga4_x -= velocidad_tortuga* tiempo_delta

    if posicion_cuadrado_tortuga1_x < -1.0:
        posicion_cuadrado_tortuga1_x = 1.0
    if posicion_segundo_cuadrado_tortuga1_x < -1.0:
        posicion_segundo_cuadrado_tortuga1_x = 1.0
    if posicion_tercer_cuadrado_tortuga1_x < -1.0:
        posicion_tercer_cuadrado_tortuga1_x = 1.0
    if posicion_cuadrado_tortuga2_x < -1.0:
        posicion_cuadrado_tortuga2_x = 1.0
    if posicion_segundo_cuadrado_tortuga2_x < -1.0:
        posicion_segundo_cuadrado_tortuga2_x = 1.0
    if posicion_tercer_cuadrado_tortuga2_x < -1.0:
        posicion_tercer_cuadrado_tortuga2_x = 1.0
    if posicion_cuadrado_tortuga3_x < -1.0:
        posicion_cuadrado_tortuga3_x = 1.0
    if posicion_segundo_cuadrado_tortuga3_x < -1.0:
        posicion_segundo_cuadrado_tortuga3_x = 1.0
    if posicion_tercer_cuadrado_tortuga3_x < -1.0:
        posicion_tercer_cuadrado_tortuga3_x = 1.0
    if posicion_cuadrado_tortuga4_x < -1.0:
        posicion_cuadrado_tortuga4_x = 1.0
    if posicion_segundo_cuadrado_tortuga4_x < -1.0:
        posicion_segundo_cuadrado_tortuga4_x = 1.0
    if posicion_tercer_cuadrado_tortuga4_x < -1.0:
        posicion_tercer_cuadrado_tortuga4_x = 1.0

    #Tortuga linea 2
    posicion_cuadrado_tortuga1_1_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga1_2_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga2_1_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga2_2_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga3_1_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga3_2_x -= velocidad_tortuga * tiempo_delta
    posicion_cuadrado_tortuga4_1_x -= velocidad_tortuga * tiempo_delta
    posicion_segundo_cuadrado_tortuga4_2_x -= velocidad_tortuga * tiempo_delta

    if posicion_cuadrado_tortuga1_1_x < -1.0:
        posicion_cuadrado_tortuga1_1_x = 1.0
    if posicion_segundo_cuadrado_tortuga1_2_x < -1.0:
        posicion_segundo_cuadrado_tortuga1_2_x = 1.0
    if posicion_cuadrado_tortuga2_1_x < -1.0:
        posicion_cuadrado_tortuga2_1_x = 1.0
    if posicion_segundo_cuadrado_tortuga2_2_x < -1.0:
        posicion_segundo_cuadrado_tortuga2_2_x = 1.0
    if posicion_cuadrado_tortuga3_1_x < -1.0:
        posicion_cuadrado_tortuga3_1_x = 1.0
    if posicion_segundo_cuadrado_tortuga3_2_x < -1.0:
        posicion_segundo_cuadrado_tortuga3_2_x = 1.0
    if posicion_cuadrado_tortuga4_1_x < -1.0:
        posicion_cuadrado_tortuga4_1_x = 1.0
    if posicion_segundo_cuadrado_tortuga4_2_x < -1.0:
        posicion_segundo_cuadrado_tortuga4_2_x = 1.0

    tiempo_colision = tiempo_actual


    # Comprobar colisión entre el triángulo y cuadrados naranjas
    if (
    (posicion_x + 0.05 > posicion_cuadrado_naranja_x - 0.05 and
     posicion_x - 0.05 < posicion_cuadrado_naranja_x + 0.05 and
     posicion_y + 0.05 > posicion_cuadrado_naranja_y - 0.05 and
     posicion_y - 0.05 < posicion_cuadrado_naranja_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_segundo_cuadrado_naranja_x - 0.05 and
     posicion_x - 0.05 < posicion_segundo_cuadrado_naranja_x + 0.05 and
     posicion_y + 0.05 > posicion_segundo_cuadrado_naranja_y - 0.05 and
     posicion_y - 0.05 < posicion_segundo_cuadrado_naranja_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_tercer_cuadrado_naranja_x - 0.05 and
     posicion_x - 0.05 < posicion_tercer_cuadrado_naranja_x + 0.05 and
     posicion_y + 0.05 > posicion_tercer_cuadrado_naranja_y - 0.05 and
     posicion_y - 0.05 < posicion_tercer_cuadrado_naranja_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y
    
    # Comprobar colisión entre el triángulo y cuadrados amarillos
    if (
    (posicion_x + 0.05 > posicion_primer_cuadrado_amarillo_x - 0.05 and
     posicion_x - 0.05 < posicion_primer_cuadrado_amarillo_x + 0.05 and
     posicion_y + 0.05 > posicion_primer_cuadrado_amarillo_y - 0.05 and
     posicion_y - 0.05 < posicion_primer_cuadrado_amarillo_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y
    
    # Comprobar colisión entre el triángulo y cuadrados rojos
    if (
    (posicion_x + 0.05 > posicion_cuadrado_rojo_x - 0.05 and
     posicion_x - 0.05 < posicion_cuadrado_rojo_x + 0.05 and
     posicion_y + 0.05 > posicion_cuadrado_rojo_y - 0.05 and
     posicion_y - 0.05 < posicion_cuadrado_rojo_y + 0.05 )
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_segundo_cuadrado_rojo_x - 0.05 and
     posicion_x - 0.05 < posicion_segundo_cuadrado_rojo_x + 0.05 and
     posicion_y + 0.05 > posicion_segundo_cuadrado_rojo_y - 0.05 and
     posicion_y - 0.05 < posicion_segundo_cuadrado_rojo_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_tercer_cuadrado_rojo_x - 0.05 and
     posicion_x - 0.05 < posicion_tercer_cuadrado_rojo_x + 0.05 and
     posicion_y + 0.05 > posicion_tercer_cuadrado_rojo_y - 0.05 and
     posicion_y - 0.05 < posicion_tercer_cuadrado_rojo_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    # Comprobar colisión entre el triángulo y cuadrados rosas
    if (
    (posicion_x + 0.05 > posicion_cuadrado_rosa_x - 0.05 and
     posicion_x - 0.05 < posicion_cuadrado_rosa_x + 0.05 and
     posicion_y + 0.05 > posicion_cuadrado_rosa_y - 0.05 and
     posicion_y - 0.05 < posicion_cuadrado_rosa_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_segundo_cuadrado_rosa_x - 0.05 and
     posicion_x - 0.05 < posicion_segundo_cuadrado_rosa_x + 0.05 and
     posicion_y + 0.05 > posicion_segundo_cuadrado_rosa_y - 0.05 and
     posicion_y - 0.05 < posicion_segundo_cuadrado_rosa_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_tercer_cuadrado_rosa_x - 0.05 and
     posicion_x - 0.05 < posicion_tercer_cuadrado_rosa_x + 0.05 and
     posicion_y + 0.05 > posicion_tercer_cuadrado_rosa_y - 0.05 and
     posicion_y - 0.05 < posicion_tercer_cuadrado_rosa_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y
    
    # Comprobar colisión entre el triángulo y cuadrados lilas
    if (
    (posicion_x + 0.05 > posicion_cuadrado_lila_x - 0.05 and
     posicion_x - 0.05 < posicion_cuadrado_lila_x + 0.05 and
     posicion_y + 0.05 > posicion_cuadrado_lila_y - 0.05 and
     posicion_y - 0.05 < posicion_cuadrado_lila_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    if (
    (posicion_x + 0.05 > posicion_segundo_cuadrado_lila_x - 0.05 and
     posicion_x - 0.05 < posicion_segundo_cuadrado_lila_x + 0.05 and
     posicion_y + 0.05 > posicion_segundo_cuadrado_lila_y - 0.05 and
     posicion_y - 0.05 < posicion_segundo_cuadrado_lila_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y


    if (
    (posicion_x + 0.05 > posicion_segundo_cuadrado_lila_x - 0.05 and
     posicion_x - 0.05 < posicion_segundo_cuadrado_lila_x + 0.05 and
     posicion_y + 0.05 > posicion_segundo_cuadrado_lila_y - 0.05 and
     posicion_y - 0.05 < posicion_segundo_cuadrado_lila_y + 0.05)
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

 # Comprobar colisión entre el triángulo y cuadrado agua, tortuga 1
    if (
        (posicion_x + 0.05 > posicion_cuadrado_agua_x - 1 and
         posicion_x - 0.05 < posicion_cuadrado_agua_x + 1 and
         posicion_y + 0.05 > posicion_cuadrado_agua_y - 0.25 and
         posicion_y - 0.05 < posicion_cuadrado_agua_y + 0.25) and
        not (posicion_y > posicion_cuadrado_tortuga1_y - 0.05 and
             posicion_y < posicion_cuadrado_tortuga1_y + 0.05 and
             (posicion_x > posicion_cuadrado_tortuga1_x - 0.1 and
              posicion_x < posicion_cuadrado_tortuga1_x + 0.1) or
             (posicion_x > posicion_segundo_cuadrado_tortuga1_x - 0.1 and
              posicion_x < posicion_segundo_cuadrado_tortuga1_x + 0.1) or
             (posicion_x > posicion_tercer_cuadrado_tortuga1_x - 0.1 and
              posicion_x < posicion_tercer_cuadrado_tortuga1_x + 0.1) or
              posicion_y > posicion_cuadrado_tortuga2_y - 0.05 and
             posicion_y < posicion_cuadrado_tortuga2_y + 0.05 and
             (posicion_x > posicion_cuadrado_tortuga2_x - 0.1 and
              posicion_x < posicion_cuadrado_tortuga2_x + 0.1) or
             (posicion_x > posicion_segundo_cuadrado_tortuga2_x - 0.1 and
              posicion_x < posicion_segundo_cuadrado_tortuga2_x + 0.1) or
             (posicion_x > posicion_tercer_cuadrado_tortuga2_x - 0.1 and
              posicion_x < posicion_tercer_cuadrado_tortuga2_x + 0.1) or
              posicion_y > posicion_cuadrado_tortuga3_y - 0.05 and
             posicion_y < posicion_cuadrado_tortuga3_y + 0.05 and
             (posicion_x > posicion_cuadrado_tortuga3_x - 0.1 and
              posicion_x < posicion_cuadrado_tortuga3_x + 0.1) or
             (posicion_x > posicion_segundo_cuadrado_tortuga3_x - 0.1 and
              posicion_x < posicion_segundo_cuadrado_tortuga3_x + 0.1) or
             (posicion_x > posicion_tercer_cuadrado_tortuga3_x - 0.1 and
              posicion_x < posicion_tercer_cuadrado_tortuga3_x + 0.1) or
              posicion_y > posicion_cuadrado_tortuga4_y - 0.05 and
             posicion_y < posicion_cuadrado_tortuga4_y + 0.05 and
             (posicion_x > posicion_cuadrado_tortuga4_x - 0.1 and
              posicion_x < posicion_cuadrado_tortuga4_x + 0.1) or
             (posicion_x > posicion_segundo_cuadrado_tortuga4_x - 0.1 and
              posicion_x < posicion_segundo_cuadrado_tortuga4_x + 0.1) or
             (posicion_x > posicion_tercer_cuadrado_tortuga4_x - 0.1 and
              posicion_x < posicion_tercer_cuadrado_tortuga4_x + 0.1) or
              posicion_y > posicion_cuadrado_tronco1_y - 0.05 and
             posicion_y < posicion_cuadrado_tronco1_y + 0.05 and
             (posicion_x > posicion_cuadrado_tronco1_x - 0.3 and
              posicion_x < posicion_cuadrado_tronco1_x + 0.3) or
             (posicion_x > posicion_segundo_cuadrado_tronco1_x - 0.3 and
              posicion_x < posicion_segundo_cuadrado_tronco1_x + 0.3) or
             (posicion_x > posicion_tercer_cuadrado_tronco1_x - 0.3 and
              posicion_x < posicion_tercer_cuadrado_tronco1_x + 0.3) or
              posicion_y > posicion_cuadrado_tronco2_y - 0.05 and
             posicion_y < posicion_cuadrado_tronco2_y + 0.05 and
             (posicion_x > posicion_cuadrado_tronco2_x - 0.3 and
              posicion_x < posicion_cuadrado_tronco2_x + 0.3) or
             (posicion_x > posicion_segundo_cuadrado_tronco2_x - 0.3 and
              posicion_x < posicion_segundo_cuadrado_tronco2_x + 0.3) or
              posicion_y > posicion_cuadrado_tronco3_y - 0.05 and
             posicion_y < posicion_cuadrado_tronco3_y + 0.05 and
             (posicion_x > posicion_cuadrado_tronco3_x - 0.3 and
              posicion_x < posicion_cuadrado_tronco3_x + 0.3) or
             (posicion_x > posicion_segundo_cuadrado_tronco3_x - 0.3 and
              posicion_x < posicion_segundo_cuadrado_tronco3_x + 0.3))
              
    ):
        posicion_x = posicion_inicial_triangulo_x
        posicion_y = posicion_inicial_triangulo_y

    tiempo_anterior = tiempo_actual

def dibujar():
    #Fondo calle cuadro negro
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(1,0.0)   # Esquina superior derecha
    glVertex2f(-1, 0.0)  # Esquina superior izquierda
    glVertex2f(-1, -1)  # Esquina inferior izquierda
    glVertex2f(1, -1)   # Esquina inferior derecha
    glEnd()

    # Dibujar cuadrado azul agua
    glColor3f(0.0, 0.749, 1.0) # Color azul
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_agua_x - 1, posicion_cuadrado_agua_y - 0.45)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_agua_x + 1, posicion_cuadrado_agua_y - 0.45)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_agua_x + 1, posicion_cuadrado_agua_y + 0.25)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_agua_x - 1, posicion_cuadrado_agua_y + 0.25)  # Esquina superior izquierda
    glEnd()

    # Dibujar cuadrados naranjas
    glColor3f(1.0, 0.5, 0.0)  # Color naranja
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_naranja_x - 0.05, posicion_cuadrado_naranja_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_naranja_x + 0.05, posicion_cuadrado_naranja_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_naranja_x + 0.05, posicion_cuadrado_naranja_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_naranja_x - 0.05, posicion_cuadrado_naranja_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_naranja_x - 0.05, posicion_segundo_cuadrado_naranja_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_naranja_x + 0.05, posicion_segundo_cuadrado_naranja_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_naranja_x + 0.05, posicion_segundo_cuadrado_naranja_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_naranja_x - 0.05, posicion_segundo_cuadrado_naranja_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_naranja_x - 0.05, posicion_tercer_cuadrado_naranja_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_naranja_x + 0.05, posicion_tercer_cuadrado_naranja_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_naranja_x + 0.05, posicion_tercer_cuadrado_naranja_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_naranja_x - 0.05, posicion_tercer_cuadrado_naranja_y + 0.05)  # Esquina superior izquierda
    glEnd()

    #Dibujar cuadrados amarillos
    glColor3f(1.0, 1.0, 0.0) #Color amarillo
    glBegin(GL_QUADS)
    glVertex2f(posicion_primer_cuadrado_amarillo_x - 0.05, posicion_primer_cuadrado_amarillo_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_primer_cuadrado_amarillo_x + 0.05, posicion_primer_cuadrado_amarillo_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_primer_cuadrado_amarillo_x + 0.05, posicion_primer_cuadrado_amarillo_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_primer_cuadrado_amarillo_x - 0.05, posicion_primer_cuadrado_amarillo_y + 0.05)  # Esquina superior izquierda
    glEnd()

    #Dibujar cuadrados rojos
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_rojo_x - 0.05, posicion_cuadrado_rojo_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_rojo_x + 0.05, posicion_cuadrado_rojo_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_rojo_x + 0.05, posicion_cuadrado_rojo_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_rojo_x - 0.05, posicion_cuadrado_rojo_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_rojo_x - 0.05, posicion_segundo_cuadrado_rojo_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_rojo_x + 0.05, posicion_segundo_cuadrado_rojo_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_rojo_x + 0.05, posicion_segundo_cuadrado_rojo_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_rojo_x - 0.05, posicion_segundo_cuadrado_rojo_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_rojo_x - 0.05, posicion_tercer_cuadrado_rojo_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_rojo_x + 0.05, posicion_tercer_cuadrado_rojo_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_rojo_x + 0.05, posicion_tercer_cuadrado_rojo_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_rojo_x - 0.05, posicion_tercer_cuadrado_rojo_y + 0.05)  # Esquina superior izquierda
    glEnd()

    # Dibujar cuadrados rosas
    glColor3f(1.0, 0.5, 0.5)  # Color rosa
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_rosa_x - 0.05, posicion_cuadrado_rosa_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_rosa_x + 0.05, posicion_cuadrado_rosa_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_rosa_x + 0.05, posicion_cuadrado_rosa_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_rosa_x - 0.05, posicion_cuadrado_rosa_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_rosa_x - 0.05, posicion_segundo_cuadrado_rosa_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_rosa_x + 0.05, posicion_segundo_cuadrado_rosa_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_rosa_x + 0.05, posicion_segundo_cuadrado_rosa_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_rosa_x - 0.05, posicion_segundo_cuadrado_rosa_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_rosa_x - 0.05, posicion_tercer_cuadrado_rosa_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_rosa_x + 0.05, posicion_tercer_cuadrado_rosa_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_rosa_x + 0.05, posicion_tercer_cuadrado_rosa_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_rosa_x - 0.05, posicion_tercer_cuadrado_rosa_y + 0.05)  # Esquina superior izquierda
    glEnd()

    # Dibujar cuadrados lilas
    glColor3f(0.7, 0.3, 1.0)  # Color lila
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_lila_x - 0.05, posicion_cuadrado_lila_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_lila_x + 0.05, posicion_cuadrado_lila_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_lila_x + 0.05, posicion_cuadrado_lila_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_lila_x - 0.05, posicion_cuadrado_lila_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_lila_x - 0.05, posicion_segundo_cuadrado_lila_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_lila_x + 0.05, posicion_segundo_cuadrado_lila_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_lila_x + 0.05, posicion_segundo_cuadrado_lila_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_lila_x - 0.05, posicion_segundo_cuadrado_lila_y + 0.05)  # Esquina superior izquierda
    glEnd()

    # Dibujar cuadrados tortuga linea 1
    glColor3f(1.0, 0.0, 0.0) # color rojo
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga1_x - 0.05, posicion_cuadrado_tortuga1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga1_x + 0.05, posicion_cuadrado_tortuga1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga1_x + 0.05, posicion_cuadrado_tortuga1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga1_x - 0.05, posicion_cuadrado_tortuga1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga1_x - 0.05, posicion_segundo_cuadrado_tortuga1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga1_x + 0.05, posicion_segundo_cuadrado_tortuga1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga1_x + 0.05, posicion_segundo_cuadrado_tortuga1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga1_x- 0.05, posicion_segundo_cuadrado_tortuga1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tortuga1_x - 0.05, posicion_tercer_cuadrado_tortuga1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tortuga1_x+ 0.05, posicion_tercer_cuadrado_tortuga1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga1_x + 0.05, posicion_tercer_cuadrado_tortuga1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga1_x - 0.05, posicion_tercer_cuadrado_tortuga1_y + 0.05)  # Esquina superior izquierda
    glEnd()


    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga2_x - 0.05, posicion_cuadrado_tortuga2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga2_x + 0.05, posicion_cuadrado_tortuga2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga2_x + 0.05, posicion_cuadrado_tortuga2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga2_x - 0.05, posicion_cuadrado_tortuga2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga2_x - 0.05, posicion_segundo_cuadrado_tortuga2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga2_x + 0.05, posicion_segundo_cuadrado_tortuga2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga2_x + 0.05, posicion_segundo_cuadrado_tortuga2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga2_x- 0.05, posicion_segundo_cuadrado_tortuga2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tortuga2_x - 0.05, posicion_tercer_cuadrado_tortuga2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tortuga2_x+ 0.05, posicion_tercer_cuadrado_tortuga2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga2_x + 0.05, posicion_tercer_cuadrado_tortuga2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga2_x - 0.05, posicion_tercer_cuadrado_tortuga2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga3_x - 0.05, posicion_cuadrado_tortuga3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga3_x + 0.05, posicion_cuadrado_tortuga3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga3_x + 0.05, posicion_cuadrado_tortuga3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga3_x - 0.05, posicion_cuadrado_tortuga3_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga3_x - 0.05, posicion_segundo_cuadrado_tortuga3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga3_x + 0.05, posicion_segundo_cuadrado_tortuga3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga3_x + 0.05, posicion_segundo_cuadrado_tortuga3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga3_x- 0.05, posicion_segundo_cuadrado_tortuga3_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tortuga3_x - 0.05, posicion_tercer_cuadrado_tortuga3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tortuga3_x+ 0.05, posicion_tercer_cuadrado_tortuga3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga3_x + 0.05, posicion_tercer_cuadrado_tortuga3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga3_x - 0.05, posicion_tercer_cuadrado_tortuga3_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glColor3f(0.0, 1.0, 0.0)  # Color verde
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga4_x - 0.05, posicion_cuadrado_tortuga4_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga4_x + 0.05, posicion_cuadrado_tortuga4_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga4_x + 0.05, posicion_cuadrado_tortuga4_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga4_x - 0.05, posicion_cuadrado_tortuga4_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga4_x - 0.05, posicion_segundo_cuadrado_tortuga4_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga4_x + 0.05, posicion_segundo_cuadrado_tortuga4_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga4_x + 0.05, posicion_segundo_cuadrado_tortuga4_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga4_x- 0.05, posicion_segundo_cuadrado_tortuga4_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tortuga4_x - 0.05, posicion_tercer_cuadrado_tortuga4_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tortuga4_x+ 0.05, posicion_tercer_cuadrado_tortuga4_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga4_x + 0.05, posicion_tercer_cuadrado_tortuga4_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tortuga4_x - 0.05, posicion_tercer_cuadrado_tortuga4_y + 0.05)  # Esquina superior izquierda
    glEnd()

    #tortugas linea 2
    glColor3f(1.0, 0.0, 0.0) # color rojo
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga1_1_x - 0.05, posicion_cuadrado_tortuga1_1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga1_1_x + 0.05, posicion_cuadrado_tortuga1_1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga1_1_x + 0.05, posicion_cuadrado_tortuga1_1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga1_1_x - 0.05, posicion_cuadrado_tortuga1_1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga1_2_x - 0.05, posicion_segundo_cuadrado_tortuga1_2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga1_2_x + 0.05, posicion_segundo_cuadrado_tortuga1_2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga1_2_x + 0.05, posicion_segundo_cuadrado_tortuga1_2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga1_2_x- 0.05, posicion_segundo_cuadrado_tortuga1_2_y + 0.05)  # Esquina superior izquierda
    glEnd()


    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga2_1_x - 0.05, posicion_cuadrado_tortuga2_1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga2_1_x + 0.05, posicion_cuadrado_tortuga2_1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga2_1_x + 0.05, posicion_cuadrado_tortuga2_1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga2_1_x - 0.05, posicion_cuadrado_tortuga2_1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga2_2_x - 0.05, posicion_segundo_cuadrado_tortuga2_2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga2_2_x + 0.05, posicion_segundo_cuadrado_tortuga2_2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga2_2_x + 0.05, posicion_segundo_cuadrado_tortuga2_2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga2_2_x- 0.05, posicion_segundo_cuadrado_tortuga2_2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga3_1_x - 0.05, posicion_cuadrado_tortuga3_1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga3_1_x + 0.05, posicion_cuadrado_tortuga3_1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga3_1_x + 0.05, posicion_cuadrado_tortuga3_1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga3_1_x - 0.05, posicion_cuadrado_tortuga3_1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga3_2_x - 0.05, posicion_segundo_cuadrado_tortuga3_2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga3_2_x + 0.05, posicion_segundo_cuadrado_tortuga3_2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga3_2_x + 0.05, posicion_segundo_cuadrado_tortuga3_2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga3_2_x- 0.05, posicion_segundo_cuadrado_tortuga3_2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glColor3f(0.0, 1.0, 0.0)  # Color verde
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tortuga4_1_x - 0.05, posicion_cuadrado_tortuga4_1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tortuga4_1_x + 0.05, posicion_cuadrado_tortuga4_1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tortuga4_1_x + 0.05, posicion_cuadrado_tortuga4_1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tortuga4_1_x - 0.05, posicion_cuadrado_tortuga4_1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tortuga4_2_x - 0.05, posicion_segundo_cuadrado_tortuga4_2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tortuga4_2_x + 0.05, posicion_segundo_cuadrado_tortuga4_2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga4_2_x + 0.05, posicion_segundo_cuadrado_tortuga4_2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tortuga4_2_x- 0.05, posicion_segundo_cuadrado_tortuga4_2_y + 0.05)  # Esquina superior izquierda
    glEnd()


    #Troncos
    # Dibujar cuadrados café
    glColor3f(0.6, 0.3, 0.0); #Color café claro
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tronco1_x - 0.05, posicion_cuadrado_tronco1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tronco1_x + 0.3, posicion_cuadrado_tronco1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tronco1_x + 0.3, posicion_cuadrado_tronco1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tronco1_x - 0.05, posicion_cuadrado_tronco1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tronco1_x - 0.05, posicion_segundo_cuadrado_tronco1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tronco1_x + 0.3, posicion_segundo_cuadrado_tronco1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco1_x + 0.3, posicion_segundo_cuadrado_tronco1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco1_x - 0.05, posicion_segundo_cuadrado_tronco1_y + 0.05)  # Esquina superior izquierda
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tronco1_x - 0.05, posicion_tercer_cuadrado_tronco1_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tronco1_x + 0.3, posicion_tercer_cuadrado_tronco1_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tronco1_x + 0.3, posicion_tercer_cuadrado_tronco1_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tronco1_x - 0.05, posicion_tercer_cuadrado_tronco1_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tronco2_x - 0.05, posicion_cuadrado_tronco2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tronco2_x + 0.3, posicion_cuadrado_tronco2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tronco2_x + 0.3, posicion_cuadrado_tronco2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tronco2_x - 0.05, posicion_cuadrado_tronco2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tronco2_x - 0.05, posicion_segundo_cuadrado_tronco2_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tronco2_x + 0.3, posicion_segundo_cuadrado_tronco2_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco2_x + 0.3, posicion_segundo_cuadrado_tronco2_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco2_x - 0.05, posicion_segundo_cuadrado_tronco2_y + 0.05)  # Esquina superior izquierda
    glEnd()

    #Troncos 3
    glBegin(GL_QUADS)
    glVertex2f(posicion_cuadrado_tronco3_x - 0.05, posicion_cuadrado_tronco3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_cuadrado_tronco3_x + 0.3, posicion_cuadrado_tronco3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_cuadrado_tronco3_x + 0.3, posicion_cuadrado_tronco3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_cuadrado_tronco3_x - 0.05, posicion_cuadrado_tronco3_y + 0.05)  # Esquina superior izquierda
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(posicion_segundo_cuadrado_tronco3_x - 0.05, posicion_segundo_cuadrado_tronco3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_segundo_cuadrado_tronco3_x + 0.3, posicion_segundo_cuadrado_tronco3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco3_x + 0.3, posicion_segundo_cuadrado_tronco3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_segundo_cuadrado_tronco3_x - 0.05, posicion_segundo_cuadrado_tronco3_y + 0.05)  # Esquina superior izquierda
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex2f(posicion_tercer_cuadrado_tronco3_x - 0.05, posicion_tercer_cuadrado_tronco3_y - 0.05)  # Esquina inferior izquierda
    glVertex2f(posicion_tercer_cuadrado_tronco3_x + 0.3, posicion_tercer_cuadrado_tronco3_y - 0.05)   # Esquina inferior derecha
    glVertex2f(posicion_tercer_cuadrado_tronco3_x + 0.3, posicion_tercer_cuadrado_tronco3_y + 0.05)   # Esquina superior derecha
    glVertex2f(posicion_tercer_cuadrado_tronco3_x - 0.05, posicion_tercer_cuadrado_tronco3_y + 0.05)  # Esquina superior izquierda
    glEnd()

    #Rana
    glPushMatrix()
    glTranslatef(posicion_x, posicion_y, 0.0)
    glRotatef(angulo_rotacion, 0, 0, 1)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.025, -0.025, 0.0)
    glVertex3f(0.0, 0.025, 0.0)
    glVertex3f(0.025, -0.025, 0.0)
    glEnd()
    glPopMatrix()

def main():
    global window
    global posicion_inicial_triangulo_x, posicion_inicial_triangulo_y

    posicion_inicial_triangulo_x = posicion_x
    posicion_inicial_triangulo_y = posicion_y

    # Establece el tamaño de la ventana
    width = 1280
    height = 1024
    # Inicializar GLFW
    if not glfw.init():
        return
    
    # Declarar Ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)
    # Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # Verificar la creacion de la ventana
    if not window:
        glfw.terminate()
        return
    # Establecer el contexto
    glfw.make_context_current(window)
    # imprimir version
    version = glGetString(GL_VERSION)
    print(version)
    # Ciclo de dibujo (Draw Loop)
    while not glfw.window_should_close(window):
        # Establecer el viewport
        glViewport(0, 0, width, height)
        # Establecer el color de borrado
        glClearColor(0.5, 0.5, 0.5, 1.0)
        # Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Actualizar
        actualizar()
        # Dibujar
        dibujar()
        # Polling de inputs
        glfw.poll_events()
        # Cambiar los buffers
        glfw.swap_buffers(window)
    # Acabar con procesos y uso de memoria
    glfw.destroy_window(window)
    glfw.terminate()

# Ejecutar el main
if __name__ == "__main__":
    main()
