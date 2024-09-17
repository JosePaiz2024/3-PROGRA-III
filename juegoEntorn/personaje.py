import pygame
import sys

class Cubo: 
    def __init__(self, x , y):s
        self.x = x 
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.velocidad = 1
        self.color ="red"
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana ):
        pygame.draw.rect(ventana, self.color, self.rectangulo)
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        