import pygame
from personaje import Cubo
from enemigo import Enemigo
import sys 

# Inicializar Pygame
pygame.init()

ANCHO=1000
ALTO=800
# Configurar la pantalla (ejemplo con una ventana de 800x600 píxeles)
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

# Establecer un título para la ventana
pygame.display.set_caption("Mi Juego")

# Bucle principal del juego
jugando = True

cubo = Cubo(100,100)

enemigos = []

enemigos.append(Enemigo(ANCHO/2, 100))  

def gestion_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
while jugando:

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestion_teclas(teclas)


    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill(("black")) # Color negro
    cubo.dibujar(VENTANA)
    

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
    pygame.display.update()# Actualizar la pantalla
    
# Salir del juego
quit()
sys.exit()