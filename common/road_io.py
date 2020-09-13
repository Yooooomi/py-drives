import json
import sys
import pygame

class RoadIO():
  def __init__(self):
    super().__init__()
    self.roads = []
    self.checks = []
    self.history = []
    self.start_pos = [pygame.Vector2(0, 0), pygame.Vector2(0, 0)]

  def load(self, filename):
    try:
      with open(filename, "r") as f:
        js = json.loads(f.read(10000000))
        for r in js["roads"]:
          a = pygame.Vector2(r[0], r[1])
          b = pygame.Vector2(r[2], r[3])
          self.create_road(a, b)
        for r in js["checks"]:
          a = pygame.Vector2(r[0], r[1])
          b = pygame.Vector2(r[2], r[3])
          self.create_check(a, b)
        a = pygame.Vector2(js["start"][0], js["start"][1])
        b = pygame.Vector2(js["start"][2], js["start"][3])
        self.set_start(a, b)
      print("Loaded", filename)
    except Exception as e:
      print("Could not load file", e)
      pass

  def save(self, filename):
    with open(filename, "w") as f:
      js = {
        "roads": [[v[0].x, v[0].y, v[1].x, v[1].y] for v in self.roads],
        "checks": [[v[0].x, v[0].y, v[1].x, v[1].y] for v in self.checks],
        "start": [self.start_pos[0].x, self.start_pos[0].y, self.start_pos[1].x, self.start_pos[1].y],
      }
      f.write(json.dumps(js))
      print("Saved", filename)

  def undo(self):
    if len(self.history) <= 0:
      return
    typ = self.history.pop()
    self.roads.pop()

  def create_road(self, a, b):
    self.history.append("road")
    self.roads.append([a, b])

  def create_check(self, a, b):
    self.history.append("check")
    self.checks.append([a, b])

  def set_start(self, a, b):
    self.start_pos = [a, b]
