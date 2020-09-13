import pygame
from engine import gameobject

class Point(gameobject.Gameobject):
  def __init__(self, pos, size):
    super().__init__()
    self.local_position = pos
    self.surf = pygame.Surface(size, pygame.SRCALPHA)
    self.surf.fill((255, 255, 255))