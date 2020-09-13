from engine.gameobject import Gameobject
from common.road_io import RoadIO
from common.road import Road
from engine import gamestate
from game.car import Car
import pygame
import sys
import math

class RoadManager(Gameobject):
  def start(self):
    super().start()
    self.manager = RoadIO()
    self.start_obj = None
    self.roads_obj = []
    self.checks_obj = []
    if len(sys.argv) == 2:
      self.manager.load(sys.argv[1])
    for r in self.manager.roads:
      self.create_road(r[0], r[1])
    for r in self.manager.checks:
      self.create_check(r[0], r[1])
    self.set_start(self.manager.start_pos[0], self.manager.start_pos[1])
    car = Car(self.manager)
    pos = ((self.manager.start_pos[0].x + self.manager.start_pos[1].x) / 2, (self.manager.start_pos[0].y + self.manager.start_pos[1].y) / 2)
    angle = 90 + math.degrees(math.atan2(self.manager.start_pos[1].y - self.manager.start_pos[0].y, self.manager.start_pos[1].x - self.manager.start_pos[0].x))
    car.local_position = pygame.Vector2(pos)
    car.rotation = angle
    gamestate.create(car)

  def create_road(self, a, b):
    new_road = Road(a, b, (255, 255, 255))
    self.roads_obj.append(new_road)
    gamestate.create(new_road)

  def create_check(self, a, b):
    new_road = Road(a, b, (0, 255, 0))
    self.checks_obj.append(new_road)
    gamestate.create(new_road)

  def set_start(self, a, b):
    if self.start_obj != None:
      gamestate.delete(self.start_obj)
      self.start_obj = None
    new_road = Road(a, b, (0, 0, 255))
    self.start_obj = new_road
    gamestate.create(new_road)