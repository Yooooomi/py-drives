import pygame
from engine import gameobject, gamestate, utils
from game.car import Car
from common.road_io import RoadIO
from game.road_manager import RoadManager
from game.point import Point
import math

class MapRunner(gameobject.Gameobject):
  def start(self):
    self.c: Car = gamestate.find(Car)
    self.rm = gamestate.find(RoadManager)
    self.m = self.rm.manager
    self.current_check = 0

  def update(self):
    super().update()
    pos = self.c.local_position
    x = math.cos(math.radians(self.c.rotation))
    y = math.sin(math.radians(self.c.rotation))
    points = [
      pygame.Vector2(pos.x + (x * -35/2 - y * -15/2), pos.y + (y * -35/2 + x * -15/2)),
      pygame.Vector2(pos.x + (x * -35/2 - y * +15/2), pos.y + (y * -35/2 + x * +15/2)),
      pygame.Vector2(pos.x + (x * +35/2 - y * +15/2), pos.y + (y * +35/2 + x * +15/2)),
      pygame.Vector2(pos.x + (x * +35/2 - y * -15/2), pos.y + (y * +35/2 + x * -15/2)),
    ]
    lines = [
      [points[0], points[1]],
      [points[1], points[2]],
      [points[2], points[3]],
      [points[3], points[0]],
    ]
    rlines = self.m.roads

    # Check walls
    for idx in range(len(rlines)):
      r = rlines[idx]
      for l in lines:
        point = utils.collide(l, r)
        if point == None:
          continue
        self.rm.roads_obj[idx].change_color((255, 0, 0))
        break

    # Check checkpoint
    if self.current_check < len(self.m.checks):
      check = self.m.checks[self.current_check]
      for l in lines:
        point = utils.collide(l, check)
        if point == None:
          continue
        self.rm.checks_obj[self.current_check].change_color((255, 165, 0), 0.5)
        self.current_check += 1
        break

    # Check start
    if self.current_check == len(self.m.checks):
      for l in lines:
        point = utils.collide(l, self.m.start_pos)
        if point == None:
          continue
        self.rm.start_obj.change_color((255, 165, 0), 0.5)
        self.current_check = 0
        break
