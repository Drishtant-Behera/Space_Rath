import pygame
import pygame.freetype
import sys
import math
from Initialisation import display
class Crossbow:
   def __init__(self, x, y):
       self.xOffset = None
       self.x = x
       self.y = y
       self.animation_images = [pygame.image.load("CrossbowPull_1.png"), pygame.image.load("CrossbowPull_2.png"),
                                pygame.image.load("CrossbowPull_1.png"), pygame.image.load("CrossbowPull_2.png")]


   def DrawingCrossbow(self):
       display.blit(self.animation_images[0], (self.x, self.y))




crossbow = Crossbow(850, 400)
crossbow.DrawingCrossbow()
