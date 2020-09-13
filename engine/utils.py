import pygame
import math

def rot_point(v, angle):
  x = v.x * math.cos(math.radians(angle)) - v.y * math.sin(math.radians(angle))
  y = v.x * math.sin(math.radians(angle)) + v.y * math.cos(math.radians(angle))
  return pygame.Vector2(x, y)

def collide(linea, lineb):
  x1 = linea[0].x
  x2 = linea[1].x
  x3 = lineb[0].x
  x4 = lineb[1].x

  y1 = linea[0].y
  y2 = linea[1].y
  y3 = lineb[0].y
  y4 = lineb[1].y

  # calculate the distance to intersection point
  uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))

  # if uA and uB are between 0-1, lines are colliding
  if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
    return pygame.Vector2(x1 + (uA * (x2-x1)), y1 + (uA * (y2-y1)))
  return None