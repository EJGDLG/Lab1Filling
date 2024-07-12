import pygame
from pygame.locals import *

# Supongamos que el archivo `gl.py` contiene la clase Renderer
# from gl import Renderer

width = 960
height = 540

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.glClearColor(1, 0.5, 1)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    rend.Clear()
    
    # Dibuja un triángulo
    triangle = [(100, 100), (150, 200), (50, 200)]
    rend.drawPolygon(triangle)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
