import pygame
import math

unique = 0

class Gameobject:
  def __init__(self):
    global unique
    unique += 1
    self.id = unique
    self.position = pygame.Vector2((0, 0))
    self.rotation = 0
    self.surf = pygame.Surface((50, 15), pygame.SRCALPHA)
    self.surf.fill((255, 255, 255))
    self.draw_origin = pygame.Vector2(0.5, 0.5)

  def __eq__(self, value):
    return value.id == self.id

  def __ne__(self, value):
    return not self.__eq__(value)

  def start(self):
    pass

  def _draw(self, screen):
    surf = pygame.transform.rotate(self.surf, -self.rotation)
    rect = surf.get_rect()
    screen.blit(surf, self.position - (rect.width * self.draw_origin.x, rect.height * self.draw_origin.y))

  def draw(self, screen):
    surf = self.surf
    surf = pygame.transform.rotate(surf, -self.rotation)
    rect = surf.get_rect()

    o = self.draw_origin

    cos = math.cos(math.radians(self.rotation))
    sin = math.sin(math.radians(self.rotation))

    offset = pygame.Vector2((-rect.width * o.x, -rect.height * o.y))
    if cos < 0:
      offset.x -= rect.width
      offset.x += rect.width * o.x * 2
    if sin < 0:
      offset.y -= rect.height
      offset.y += rect.height * o.y * 2

    screen.blit(surf, self.position + offset)

  def update(self):
    pass

  def end(self):
    pass