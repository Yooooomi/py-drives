from engine import gameobject
import math
import pygame

class Road(gameobject.Gameobject):
  def __init__(self, start_pos, end_pos, color):
    super().__init__()
    print(start_pos, end_pos)
    self.start_pos = start_pos
    self.end_pos = end_pos
    size = (self.end_pos - self.start_pos).magnitude()
    dir = self.end_pos - self.start_pos
    angle = math.atan2(dir.y, dir.x)
    self.position = start_pos
    self.rotation = math.degrees(angle)
    self.draw_origin = pygame.Vector2((0, 0))
    self.surf = pygame.Surface((size, 15), pygame.SRCALPHA)
    self.surf.fill(color)