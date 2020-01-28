# filename: OO - Super Turtles - Project 2 (team) - WIP
# Inspired by "Turtle Geometry" by Abelson and diSessa

from random import randint
from superturtle_prey import *
from superturtle_predator import *

# Don't change the Superturtle conditions!
prey = Superturtle_prey(100, -100, 90, 5, 'blue')      # (x, y, heading, step, color)
prey.start_trace()      # leave a trace/path on the screen

# Don't change the Superturtle conditions!
predator = Superturtle_predator(60, 60, 90, 10, 'red')
predator.start_trace()  # leave a trace/path on the screen

t = 0
predator_step = predator.get_step()

while predator.distance_to(prey) > predator_step:
  prey.go(predator, t)
  predator.go(prey, t)
  t = t + 1

print t

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()
