import pygame
from pygame.locals import *
import sys

#Iniciación de Pygame
pygame.init()

#Pantalla - Ventana
W, H = 1000,600
Pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption("Soldado")
icono=pygame.image.load("imgs/png/soldado.png")
pygame.display.set_icon(icono)

#Fondo del Juego
fondo=pygame.image.load("imgs/png/selva.png")

#Música de Fondo del Juego
pygame.mixer.music.load('sound/musica_vjsoldado.mp3')
pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.5)


#Personaje
quieto = pygame.image.load("imgs/png/Idle (1).png")

caminaDerecha = [pygame.image.load("imgs/png/Run (1).png"),
                 pygame.image.load("imgs/png/Run (2).png"),
                 pygame.image.load("imgs/png/Run (3).png"),
                 pygame.image.load("imgs/png/Run (4).png"),
                 pygame.image.load("imgs/png/Run (5).png"),
                 pygame.image.load("imgs/png/Run (6).png"),
                 pygame.image.load("imgs/png/Run (7).png"),
                 pygame.image.load("imgs/png/Run (8).png"),
                 pygame.image.load("imgs/png/Run (9).png"),
                 pygame.image.load("imgs/png/Run (10).png")]


caminaIzquierda = [pygame.image.load("imgs/png/Runizq (1).png"),
                   pygame.image.load("imgs/png/Runizq (2).png"),
                   pygame.image.load("imgs/png/Runizq (3).png"),
                   pygame.image.load("imgs/png/Runizq (4).png"),
                   pygame.image.load("imgs/png/Runizq (5).png"),
                   pygame.image.load("imgs/png/Runizq (6).png"),
                   pygame.image.load("imgs/png/Runizq (7).png"),
                   pygame.image.load("imgs/png/Runizq (8).png"),
                   pygame.image.load("imgs/png/Runizq (9).png"),
                   pygame.image.load("imgs/png/Runizq (10).png")]

salta = [pygame.image.load("imgs/png/Jump (1).png"),
         pygame.image.load("imgs/png/Jump (2).png"),
         pygame.image.load("imgs/png/Jump (3).png"),
         pygame.image.load("imgs/png/Jump (4).png"),
         pygame.image.load("imgs/png/Jump (5).png"),
         pygame.image.load("imgs/png/Jump (6).png"),
         pygame.image.load("imgs/png/Jump (7).png"),
         pygame.image.load("imgs/png/Jump (8).png"),
         pygame.image.load("imgs/png/Jump (9).png"),
         pygame.image.load("imgs/png/Jump (10).png")]

#Variables
x = 0
px = 50
py = 320
ancho = 40
velocidad = 10


#Control de FPS
Reloj = pygame.time.Clock()

#Variables Salto
salto = False
#Altura de Salto
cuentaSalto = 10

#variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables Globales
    global cuentaPasos
    global x

    #Fondo en Movimiento
    x_relativa = x % fondo.get_rect().width
    Pantalla.blit(fondo, (x_relativa - fondo.get_rect().width , 0))

    if x_relativa < W:
        Pantalla.blit(fondo, (x_relativa,0))

    x -= 5

    #Fondo en Movimiento
    x_relativa = x % fondo.get_rect().width
    Pantalla.blit(fondo, (x_relativa + fondo.get_rect().width , 1000))

    if x_relativa > W:
        Pantalla.blit(fondo, (x_relativa,0))

    x -= 5

    #Contador de Pasos
    if cuentaPasos + 1 >= 10:
        cuentaPasos = 0

    #Movimiento a la izquierda
    if izquierda:
        Pantalla.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    #Movimiento a la izquierda
    elif derecha:
        Pantalla.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 10:
        cuentapasos = 0
        Pantalla.blit(salta[cuentapasos // 1], (int(px), int(py)))
        cuentapasos += 1

    else:
        Pantalla.blit(quieto, (int(px), int(py)))

    #Actualización de la ventana
    pygame.display.update()

ejecuta = True

#Bucle de Acciones y controles
while ejecuta:
    #FPS
    Reloj.tick(18)

    # Bucle de Juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción Tecla Pulsada
    keys = pygame.key.get_pressed()

    #Tecla <- - Movimiento a la izquierda
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla -> - Movimiento a la derecha
    elif keys[pygame.K_RIGHT] and px < 800 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

        #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla arriba - Movimiento hacia arriba
    if keys[pygame.K_UP] and py > 320:
        py -= velocidad

    #Tecla abajo - Movimiento hacia abajo
    if keys[pygame.K_DOWN] and py < 380:
        py += velocidad

    #Tecla espacio - Movimiento Saltar
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
            if cuentaSalto >= -10:
                py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
                cuentaSalto -= 1
            else:
                cuentaSalto = 10
                salto = False

    # Control del audio
    # Baja volumen
    sonido_arriba = pygame.image.load('sound/volume_up.png')
    sonido_abajo = pygame.image.load('sound/volume_down.png')
    sonido_mute = pygame.image.load('sound/volume_muted.png')
    sonido_max = pygame.image.load('sound/volume_max.png')

    if keys[pygame.K_PAGEUP] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        Pantalla.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_PAGEUP] and pygame.mixer.music.get_volume() == 0.0:
        Pantalla.blit(sonido_mute, (850, 25))

    # Sube volumen
    if keys[pygame.K_PAGEDOWN] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        Pantalla.blit(sonido_arriba, (850, 25))
    elif keys[pygame.K_PAGEDOWN] and pygame.mixer.music.get_volume() == 1.0:
        Pantalla.blit(sonido_max, (850, 25))

    # Desactivar sonido
    elif keys[pygame.K_PAUSE]:
        pygame.mixer.music.set_volume(0.0)
        Pantalla.blit(sonido_mute, (850, 25))

    # Reactivar sonido
    elif keys[pygame.K_INSERT]:
        pygame.mixer.music.set_volume(1.0)
        Pantalla.blit(sonido_max, (850, 25))

    #Llmada a la función de Actualización de la Ventana
    recargaPantalla()

#Salida del Juego
pygame.quit()
