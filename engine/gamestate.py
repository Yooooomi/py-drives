from engine.gameobject import Gameobject

objects = []

def create(obj: Gameobject):
  objects.append(obj)
  obj.start()

def delete(obj: Gameobject):
  for child in obj.children:
    delete(child)
  obj.end()
  objects.remove(obj)

def find(typ):
  for o in objects:
    if isinstance(o, typ):
      return o
