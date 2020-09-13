import pygame
import math
from engine import gamestate, utils

unique = 0

class Gameobject:
  def __init__(self):
    global unique
    unique += 1
    self.id = unique
    self.local_position = pygame.Vector2((0, 0))
    self.rotation = 0
    self.surf = pygame.Surface((25, 25), pygame.SRCALPHA)
    self.surf.fill((255, 255, 255))
    self.draw_origin = pygame.Vector2(0.5, 0.5)
    self.parent = None
    self.children = []

  def __eq__(self, value):
    return value is not None and value.id == self.id

  def __ne__(self, value):
    return not self.__eq__(value)

  def start(self):
    pass

  def _draw(self, screen):
    surf = pygame.transform.rotate(self.surf, -self.rotation)
    rect = surf.get_rect()
    screen.blit(surf, self.local_position - (rect.width * self.draw_origin.x, rect.height * self.draw_origin.y))

  def get_pos(self):
    if self.parent == None:
      return self.local_position
    else:
      return utils.rot_point(self.local_position, self.parent.rotation) + self.parent.get_pos()

  def get_rot(self):
    if self.parent == None:
      return self.rotation
    else:
      return self.rotation + self.parent.get_rot()

  def draw(self, screen):
    rotation = self.get_rot()
    position = self.get_pos()
    surf = self.surf
    if surf.get_rect().width > 0:
      surf = pygame.transform.rotate(surf, -rotation)
    rect = surf.get_rect()

    o = self.draw_origin

    cos = math.cos(math.radians(rotation))
    sin = math.sin(math.radians(rotation))

    offset = pygame.Vector2((-rect.width * o.x, -rect.height * o.y))
    if cos < 0:
      offset.x -= rect.width
      offset.x += rect.width * o.x * 2
    if sin < 0:
      offset.y -= rect.height
      offset.y += rect.height * o.y * 2

    screen.blit(surf, position + offset)

  def add_child(self, obj):
    obj.parent = self
    self.children.append(obj)
    gamestate.create(obj)

  def update(self):
    pass

  def end(self):
    pass