import enum
import pygame

keys = {}
keys_clicks = {}
mouse_buttons = {}
mouse_clicks = {}

class KeyState(enum.Enum):
  DOWN = 1,
  UP = 2,

def init():
  global mouse_clicks
  global keys_clicks
  mouse_clicks = {}
  keys_clicks = {}

def set_down(key):
  keys[key] = KeyState.DOWN


def set_up(key):
  if key in keys and keys[key] == KeyState.DOWN:
    keys_clicks[key] = True
  keys[key] = KeyState.UP


def is_down(key):
  return key in keys and keys[key] == KeyState.DOWN


def is_up(key):
  return key not in keys or keys[key] == KeyState.UP


def is_key_clicked(key):
  return key in keys_clicks and keys_clicks[key]

def get_mouse():
  return pygame.Vector2(pygame.mouse.get_pos())

def is_mouse_clicked(button):
  return button in mouse_clicks and mouse_clicks[button]

def set_mouse_button_down(button):
  mouse_buttons[button] = KeyState.DOWN

def set_mouse_button_up(button):
  if button in mouse_buttons and mouse_buttons[button] == KeyState.DOWN:
    mouse_clicks[button] = True
  mouse_buttons[button] = KeyState.UP