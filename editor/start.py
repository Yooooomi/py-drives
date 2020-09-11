from engine import gameobject
import pygame

class Start(gameobject.Gameobject):
  def __init__(self, pos):
    super().__init__()
    self.position = pos
    self.surf = pygame.Surface((5, 5), pygame.SRCALPHA)
