from engine.gameobject import Gameobject
import pygame
from engine import gametime, inputs
from pygame import Vector2
from game.ray import Ray
import math
from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
)


class Car(Gameobject):
  def __init__(self, manager):
    super().__init__()
    self.manager = manager

  def start(self):
    self.velocity = pygame.Vector2((0, 0))
    self.acceleration = 2000
    self.rotate_speed = 270
    self.max_speed = 375
    self.surf = pygame.Surface((35, 15), pygame.SRCALPHA)
    self.surf.fill((255, 255, 255))

    parts = 5
    dead_angle = math.radians(90)
    step = (math.pi - dead_angle) / (parts - 1)
    
    for i in range(parts):
      angle = dead_angle / 2 + step * i - math.radians(90)
      ray = Ray(math.degrees(angle), self.manager, i)
      ray.local_position = pygame.Vector2(35 / 2, 0)
      self.add_child(ray)

  def update(self):
    super().update()
    speed = self.acceleration * gametime.delta_time
    x = math.cos(math.radians(self.rotation))
    y = math.sin(math.radians(self.rotation))

    self.velocity -= self.velocity * 5 * gametime.delta_time

    if inputs.is_down(K_UP):
      self.velocity += Vector2(x, y) * speed
    if inputs.is_down(K_DOWN):
      self.velocity -= Vector2(x, y) * speed

    if self.velocity.magnitude() > self.max_speed:
      print("MAX")
      self.velocity = self.velocity.normalize() * self.max_speed

    self.local_position += self.velocity * gametime.delta_time

    if inputs.is_down(K_LEFT):
      self.rotation -= self.rotate_speed * gametime.delta_time
    if inputs.is_down(K_RIGHT):
      self.rotation += self.rotate_speed * gametime.delta_time
