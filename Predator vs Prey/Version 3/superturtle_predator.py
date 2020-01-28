from turtle import *
from math import sqrt
from random import randint

########################################################################
# The predator team copies and pastes their superturtle code
# below, and renames their class Superturtle_predator.
#
# Below are empty functions necessary for running the main.py program.
# You will replace the pass command with your code.
########################################################################


class Superturtle_predator():
  ''' A class of turtle with enhanced capabilities (methods) '''

  def __init__(self, init_x, init_y, init_heading, step, color):
    self.__turtle = Turtle()
    self.__turtle.color(color)
    self.__turtle.penup()
    self.__x = init_x
    self.__y = init_y
    self.__turtle.goto(init_x, init_y)
    self.__turtle.setheading(init_heading)
    self.__step = step

  def get_turtle(self):
    return self.__turtle

  def get_x(self):
    return self.__turtle.xcor()

  def get_y(self):
    return self.__turtle.ycor()

  def start_trace(self):
    self.__turtle.pendown()

  def go(self, prey, time):
    deflection = self.__turtle.towards(prey.get_turtle())
    self.__turtle.setheading(deflection)
    self.__turtle.forward(self.__step)

  def get_step(self):
    return self.__step

  def distance_to(self, prey):
    dist = sqrt((self.get_x() - prey.get_x())**2 + (self.get_y() - prey.get_y())**2)
    return dist

  
