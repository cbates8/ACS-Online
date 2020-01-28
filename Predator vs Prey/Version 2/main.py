from random import randint
from superturtle import *
import time
# make sure to implement a class that supports the following:

prey = Superturtle(100, -100, 90, 5, 'blue')       # (x, y, heading, step, color)
prey.start_trace()

predator = Superturtle(60, 60, 90, 10, 'red')    # (x, y, heading, step, color)
predator.start_trace()                          # lower the pen to leave a trace as the superturtle moves

# The Pseudo Code:
'''
while the distance between the predator and the prey is bigger than the predator step size:
  the predator moves forward
  if the smell of the prey is "weaker" after this step, compared to the smell before:
    the predator turns left by a random amount in the range of 1-90 degrees
'''

# Your code here:
start_time = time.time()
while predator.distance_to(prey) > predator.get_step():
  predator.move_forward()
  if predator.smell_to(prey) == 'weaker':
    predator.left_turn(randint(1, 90))
  prey.make_circle(predator)
end_time = time.time()
total_time = end_time - start_time
print 'Chase time was %s seconds' % (round(total_time, 3))

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()
