from turtle import *
from math import sqrt
from random import randint

#######################################################################
# The prey team copies and pastes their superturtle code
# below, and renames their class Superturtle_prey.
#
# Below are empty functions necessary for running the main.py program.
# You will replace the pass command with your code.
#######################################################################


class Superturtle_prey():
  ''' A class of turtle with enhanced capabilities (methods) '''

  def __init__(self, init_x, init_y, init_heading, step, color):
    self.__turtle = Turtle()
    self.__turtle.color(color)
    self.__turtle.penup()

    self.__x = init_x
    self.__y = init_y
    self.__turtle.goto(init_x, init_y)

    self.__turtle.setheading(init_heading)

    self.__step = step        # the amount of movement each time

  def start_trace(self):
    self.__turtle.pendown()

  def get_turtle(self):
    return self.__turtle

  def get_x(self):
    return self.__turtle.xcor()

  def get_y(self):
    return self.__turtle.ycor()

  def distance_to(self, predator):
    dist = sqrt((self.get_x() - predator.get_x())**2 + (self.get_y() - predator.get_y())**2)
    return dist

  def go(self, predator, time):
    if self.distance_to(predator) > randint(30,70):
      self.__turtle.circle(-50, 50, self.__step)
    else:
      self.__turtle.circle(60, 40,  self.__step)
  
