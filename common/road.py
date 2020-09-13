from engine import gameobject, gametime
import math
import pygame

class Road(gameobject.Gameobject):
  def __init__(self, start_pos, end_pos, color):
    super().__init__()
    self.color = color
    self.start_pos = start_pos
    self.end_pos = end_pos
    self.size = (self.end_pos - self.start_pos).magnitude()
    dir = self.end_pos - self.start_pos
    angle = math.atan2(dir.y, dir.x)
    self.local_position = start_pos
    self.rotation = math.degrees(angle)
    self.draw_origin = pygame.Vector2((0, 0))
    self.surf = pygame.Surface((self.size, 3), pygame.SRCALPHA)
    self.surf.fill(color)
    self.current_to = 0

  def change_color(self, color, timeout = -1):
    self.surf = pygame.Surface((self.size, 3), pygame.SRCALPHA)
    self.surf.fill(color)
    self.current_to = timeout

  def update(self):
    super().update()
    tmp = self.current_to
    self.current_to -= gametime.delta_time
    if tmp > 0 and self.current_to <= 0:
      self.surf.fill(self.color)
