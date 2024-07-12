import pygame
from pygame.locals import *

class Renderer(object):
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        
        self.glColor(1, 1, 1)
        self.glClearColor(0, 0, 0)
        
    def glColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))
        
        self.currColor = [r, g, b]
    
    def glClearColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))
        
        self.clearColor = [r, g, b]
        
    def Clear(self):
        color = [int(i * 255) for i in self.clearColor]
        self.screen.fill(color)
        
    def glPoint(self, x, y, color=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            color = [int(i * 255) for i in (color or self.currColor)]
            self.screen.set_at((x, self.height - 1 - y), color)

    def drawLine(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            self.glPoint(x0, y0)
            if x0 == x1 and y0 == y1:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
    
    def drawPolygon(self, points):
        num_points = len(points)
        for i in range(num_points):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % num_points]
            self.drawLine(x0, y0, x1, y1)
