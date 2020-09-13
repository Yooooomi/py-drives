import pygame
from engine import gametime, inputs, gamestate
import time
from pygame.locals import (
  QUIT,
  KEYDOWN,
  KEYUP,
  K_ESCAPE,
  MOUSEBUTTONDOWN,
  MOUSEBUTTONUP,
)

def launch():
  pygame.init()
  screen = pygame.display.set_mode((1600, 900))

  running = True
  last_time = time.time()

  while running:
    screen.fill((0, 0, 0))
    inputs.init()
    for event in pygame.event.get():
      if event == QUIT:
        running = False
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
        inputs.set_down(event.key)
      if event.type == KEYUP:
        inputs.set_up(event.key)
      if event.type == MOUSEBUTTONDOWN:
        inputs.set_mouse_button_down(event.button)
      if event.type == MOUSEBUTTONUP:
        inputs.set_mouse_button_up(event.button)
    for obj in gamestate.objects:
      obj.update()
    for obj in gamestate.objects:
      obj.draw(screen)
    pygame.display.flip()
    # print("Took", (time.time() - last_time) * 1000)
    gametime.delta_time = time.time() - last_time
    last_time = time.time()
