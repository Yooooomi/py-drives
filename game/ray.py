from engine import gameobject, utils
import pygame

class Ray(gameobject.Gameobject):
  def __init__(self, angle, manager, i):
    super().__init__()
    self.i = i
    self.draw_origin = pygame.Vector2(0, 0)
    self.surf = pygame.Surface((1000, 2), pygame.SRCALPHA)
    self.surf.fill((255, 165, 0))
    self.no_coll = self.surf
    self.rotation = angle
    self.manager = manager

  def collide(self, points):
    pos = self.get_pos()
    sort = sorted(points, key=lambda point: pos.distance_to(point))
    point = sort[0]
    dist = self.get_pos().distance_to(point)
    self.surf = pygame.Surface((dist, 2), pygame.SRCALPHA)

  def update(self):
    super().update()
    pos = self.get_pos()
    end = pos + pygame.Vector2(1, 0).normalize().rotate(self.get_rot()) * 1000
    colls = []
    for r in self.manager.roads:
      point = utils.collide([pos, end], r)
      if point == None:
        continue
      colls.append(point)
    if len(colls) > 0:
      self.collide(colls)
      self.surf.fill((0, 255, 0))
    else:
      self.surf = self.no_coll