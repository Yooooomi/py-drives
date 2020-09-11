import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from engine import gamestate, entry
from game.car import Car

car = Car()
gamestate.create(car)
print("Launch")
entry.launch()
