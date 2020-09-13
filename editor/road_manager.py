from engine import gameobject, inputs, gamestate, gametime
from editor.tmp_road import TmpRoad
from common.road import Road
from editor.start import Start
from common.road_io import RoadIO
import json
import sys
import pygame
from pygame.locals import (
  K_KP0,
  K_KP1,
  K_KP2,
  K_KP3,
  K_KP4,
  K_KP5,
  K_KP6,
  K_KP7,
  K_KP8,
  K_KP9,
  K_z,
)

class RoadManager(gameobject.Gameobject):
  def __init__(self):
    super().__init__()
    self.manager = RoadIO()
    self.tracing = None
    self.current_road = None
    self.roads_obj = []
    self.checks_obj = []
    self.start_obj = None
    self.history = []
    self.saves = [
      (K_KP0, "map0"),
      (K_KP1, "map1"),
      (K_KP2, "map2"),
      (K_KP3, "map3"),
      (K_KP4, "map4"),
      (K_KP5, "map5"),
      (K_KP6, "map6"),
      (K_KP7, "map7"),
      (K_KP8, "map8"),
      (K_KP9, "map9"),
    ]
    if len(sys.argv) == 2:
      filename = sys.argv[1]
      self.manager.load(filename)
    for r in self.manager.roads:
      self.create_road(r[0], r[1], True)
    for r in self.manager.checks:
      self.create_check(r[0], r[1], True)
    self.set_start(self.manager.start_pos[0], self.manager.start_pos[1], True)

  def undo(self):
    if len(self.history) <= 0:
      return
    self.manager.undo()
    typ = self.history.pop()
    obj = self.roads_obj.pop()
    gamestate.delete(obj)

  def create_road(self, a, b, loading = False):
    self.history.append("road")
    if loading == False:
      self.manager.create_road(a, b)
    new_road = Road(a, b, (255, 255, 255))
    self.roads_obj.append(new_road)
    gamestate.create(new_road)

  def create_check(self, a, b, loading = False):
    self.history.append("check")
    if loading == False:
      self.manager.create_check(a, b)
    new_road = Road(a, b, (0, 255, 0))
    self.checks_obj.append(new_road)
    gamestate.create(new_road)

  def set_start(self, a, b, loading = False):
    if self.start_obj != None:
      gamestate.delete(self.start_obj)
      self.start_obj = None
    new_road = Road(a, b, (0, 0, 255))
    if loading == False:
      self.manager.set_start(a, b)
    self.start_obj = new_road
    gamestate.create(new_road)

  def save(self, filename):
    self.manager.save(filename)

  def update(self):
    super().update()
    for s in self.saves:
      if inputs.is_key_clicked(s[0]):
        self.save(s[1])
    if inputs.is_key_clicked(K_z):
      self.undo()
    if inputs.is_mouse_clicked(1):
      if self.tracing == None:
        self.tracing = "road"
        tmp_road = TmpRoad((255, 255, 255))
        self.current_road = tmp_road
        gamestate.create(tmp_road)
      elif self.tracing == "road":
        self.tracing = None
        mouse_pos = inputs.get_mouse()
        self.create_road(self.current_road.start_pos, mouse_pos)
        gamestate.delete(self.current_road)
    if inputs.is_mouse_clicked(2):
      if self.tracing == None:
        self.tracing = "start"
        tmp_road = TmpRoad((0, 0, 255))
        self.current_road = tmp_road
        gamestate.create(tmp_road)
      elif self.tracing == "start":
        self.tracing = None
        mouse_pos = inputs.get_mouse()
        self.set_start(self.current_road.start_pos, mouse_pos)
        gamestate.delete(self.current_road)
    if inputs.is_mouse_clicked(3):
      if self.tracing == None:
        self.tracing = "check"
        tmp_road = TmpRoad((0, 255, 0))
        self.current_road = tmp_road
        gamestate.create(tmp_road)
      elif self.tracing == "check":
        self.tracing = None
        mouse_pos = inputs.get_mouse()
        self.create_check(self.current_road.start_pos, mouse_pos)
        gamestate.delete(self.current_road)