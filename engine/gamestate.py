from engine.gameobject import Gameobject

objects = []

def create(obj: Gameobject):
  objects.append(obj)
  obj.start()

def delete(obj: Gameobject):
  obj.end()
  objects.remove(obj)
