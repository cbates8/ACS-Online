from turtle import *

class Superturtle():
  ''' A class of turtle with enhanced capabilities (methods) '''

  def __init__(self, initx, inity, heading, step, color):
    self.__turtle = Turtle()
    self.__turtle.penup()
    self.__turtle.color(color)

    self.__x = initx
    self.__y = inity

    self.__turtle.goto(initx, inity)
    self.__turtle.setheading(heading)

    self.__step = step

    self.__distances = []
  def get_step(self):
    return self.__step

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y

  def start_trace(self):
    self.__turtle.pendown()

  def distance_to(self, other_st):
    self.__distances.append((((other_st.__turtle.xcor() - self.__turtle.xcor())**2) + ((other_st.__turtle.ycor() - self.__turtle.ycor())**2)) ** 0.5)
    print self.__distances[-1]
    return self.__distances[-1]

  def move_forward(self):
    self.__turtle.forward(self.__step)

  def left_turn(self, angle):
    self.__turtle.left(angle)

  def smell_to(self, other_st):
    if len(self.__distances) > 1:
      if self.__distances[-1] > self.__distances[-2]:
        return 'weaker'
    return 'stronger'

  def get_distances(self):
    return self.__distances

  def make_circle(self, other_st):
   self.__turtle.circle(90, self.__step)
  
