import pygame
from pygame.locals import *

width = 960
height = 540

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

rend = Renderer(screen)

# Establecer color de fondo
rend.glClearColor(0.5, 0.5, 0.5)  # Color de fondo gris

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    rend.Clear()
    
    # Establecer color del polígono
    rend.glColor(1, 0, 0)  # Rojo
    
    # Dibuja un triángulo
    triangle = [(100, 100), (150, 200), (50, 200)]
    rend.drawPolygon(triangle)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()