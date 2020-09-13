from engine import gameobject
import pygame

class Start(gameobject.Gameobject):
  def __init__(self, pos):
    super().__init__()
    self.local_position = pos
    self.surf = pygame.Surface((5, 5), pygame.SRCALPHA)
