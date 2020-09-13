import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from engine import gamestate, entry
from game.car import Car
from game.road_manager import RoadManager
from game.map_runner import MapRunner
from game.point import Point
import pygame

rm = RoadManager()
gamestate.create(rm)
runner = MapRunner()
gamestate.create(runner)
# gamestate.create(Car())
entry.launch()
