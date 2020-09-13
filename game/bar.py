import pygame
from engine import gameobject

class Bar(gameobject.Gameobject):
  def __init__(self):
    self.surf = pygame.Surface((5, 5), pygame.SRCALPHA)
    self.surf.fill((255, 255, 255))