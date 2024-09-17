import pygame 
import sys

class Enemigo: 
    def __init__(self, x , y):
        self.x = x 
        self.y = y
        self.ancho = 60
        self.alto = 60
        self.velocidad = 0.33
        self.color ="purple"
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana ):
        pygame.draw.rect(ventana, self.color, self.rectangulo)
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)
     