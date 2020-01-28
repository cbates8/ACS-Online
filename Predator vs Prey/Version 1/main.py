from random import randint
from superturtle import *

# make sure to implement a class that supports the following:

prey = Superturtle(10, 10, 90, 0, 'blue')       # (x, y, heading, step, color)

predator = Superturtle(60, 60, 90, 5, 'red')    # (x, y, heading, step, color)
predator.start_trace()                          # lower the pen to leave a trace as the superturtle moves

# The Pseudo Code:
'''
while the distance between the predator and the prey is bigger than the predator step size:
  the predator moves forward
  if the smell of the prey is "weaker" after this step, compared to the smell before:
    the predator turns left by a random amount in the range of 1-90 degrees
'''

# Your code here:
while predator.distance_to(prey) > predator.get_step():
  predator.move_forward()
  if predator.smell_to(prey) == 'weaker':
    predator.left_turn(randint(1, 90))

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()
