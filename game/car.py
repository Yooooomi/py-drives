from engine.gameobject import Gameobject
import pygame
from engine import gametime, inputs
from pygame import Vector2
import math
from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
)


class Car(Gameobject):
  def __init__(self):
    super().__init__()
    self.velocity = pygame.Vector2((0, 0))
    self.acceleration = 7000
    self.rotate_speed = 550
    self.max_speed = 800

  def update(self):
    super().update()
    speed = self.acceleration * gametime.delta_time
    x = math.cos(math.radians(self.rotation))
    y = math.sin(math.radians(self.rotation))

    self.velocity -= self.velocity * 8 * gametime.delta_time

    if inputs.is_down(K_UP):
      self.velocity += Vector2(x, y) * speed
    if inputs.is_down(K_DOWN):
      self.velocity -= Vector2(x, y) * speed

    if self.velocity.magnitude() > self.max_speed:
      self.velocity = self.velocity.normalize() * self.max_speed

    self.position += self.velocity * gametime.delta_time

    if inputs.is_down(K_LEFT):
      self.rotation -= self.rotate_speed * gametime.delta_time
    if inputs.is_down(K_RIGHT):
      self.rotation += self.rotate_speed * gametime.delta_time
