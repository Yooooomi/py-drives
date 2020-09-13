import pygame
from engine import gameobject, inputs
import math

class TmpRoad(gameobject.Gameobject):
  def __init__(self, color):
    super().__init__()
    self.color = color
    self.start_pos = inputs.get_mouse()
    self.draw_origin = pygame.Vector2((0, 0))
    self.local_position = self.start_pos
    self.end_pos = None

  def update(self):
    super().update()
    mouse_pos = inputs.get_mouse()
    size = (mouse_pos - self.start_pos).magnitude()
    dir = mouse_pos - self.start_pos
    angle = math.atan2(dir.y, dir.x)
    self.rotation = math.degrees(angle)
    self.surf = pygame.Surface((size, 3), pygame.SRCALPHA)
    self.surf.fill(self.color)
