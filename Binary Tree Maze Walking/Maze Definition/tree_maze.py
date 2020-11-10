import turtle
from random import choice

class Tree_Maze:
  """ Tree Maze class for representing a checkers-board-like maze made up of "erasable" lines. """

  def __init__(self, columns, rows):
    """ Create a new maze with 'columns' columns and 'rows' rows """
    #print "width:", maze_drawer.window_width()
    #print "height:", maze_drawer.window_height()

    self.columns = columns                # the width of the maze (number of squares)
    self.rows = rows                      # the height of the maze (number of squares)
    
    self.maze_connections = dict()        # the connections between the squares/nodes. key = a square; value = a square it's connected to. Filled out as lines are erased and squares are connected.
    
    self.maze_square_coordinates = dict() # the dict translating from square numbers to (column, row) maze coordinates
    
    self._maze_drawer = turtle.Turtle()   # the turtle which draws the maze lines
    maze_drawer = self._maze_drawer       # a short-hand for the maze-drawing turtle
    screen = turtle.Screen()

    window_width = 400
    window_height = 400
    screen.setup(width=window_width, height=window_height)

    self.square_size = 0.7 * min(window_width, window_height) / max(columns, rows)

    maze_drawer.setheading(0)
    maze_drawer.speed(10)
    #maze_drawer.tracer(3)
    maze_drawer.clear()
    maze_drawer.penup()
    
    self.init_x = -window_width * 0.35
    self.init_y = window_height * 0.35
    
    x = self.init_x
    y = self.init_y
    maze_drawer.goto(x, y)
    
    
    for r in range(rows + 1):
      maze_drawer.pendown()
      maze_drawer.goto(maze_drawer.xcor() + columns * self.square_size, maze_drawer.ycor())
      maze_drawer.penup()
      y = y - self.square_size
      maze_drawer.goto(x, y)
      
    x = -window_width * 0.35
    y = window_height * 0.35
    maze_drawer.goto(x, y)
    
    for c in range(columns + 1):
      maze_drawer.pendown()
      maze_drawer.goto(maze_drawer.xcor(), maze_drawer.ycor() - rows * self.square_size)
      maze_drawer.penup()
      x = x + self.square_size
      maze_drawer.goto(x, y)

    maze_drawer.hideturtle()
    
    
  def erase_line(self, square_number, side_direction): # top-left square = 0, bottom side = 'South'
    if side_direction == "None":
      neighbor_square = None                          # the bottom-right corner square
      self.maze_connections[square_number] = neighbor_square  # record the connection
      erase_command = "maze.erase_line(" + str(square_number) + ", '" + side_direction + "')"
      print (erase_command)
      return
    
    delta = 2
    maze_eraser = self._maze_drawer
    maze_eraser.penup()
    maze_eraser.pencolor("#F8F8FF")   # GhostWhite
    maze_eraser.pensize(3)
    small_square_size = self.square_size - 2 * delta

    # position eraser at the bottom-right corner of a square
    x = self.init_x + ( 1 + square_number % self.columns) * self.square_size
    y = self.init_y - ( 1 + square_number // self.rows) * self.square_size
    
    if side_direction == "South":
      maze_eraser.setheading(180)                     # erase by moving left (backwards)
      x = x - delta
      maze_eraser.goto(x, y)
      neighbor_square = square_number + self.columns  # the square this one will connect to
    elif side_direction == "East":
      maze_eraser.setheading(90)                      # erase by moving up
      y = y + delta
      maze_eraser.goto(x, y)
      neighbor_square = square_number + 1             # the square this one will connect to
    else:
      raise ValueError("erase_line(): direction to erase maze side is not defined")
      return

    erase_command = "maze.erase_line(" + str(square_number) + ", '" + side_direction + "')"
    print (erase_command)
    maze_eraser.pendown()
    maze_eraser.forward(small_square_size)
    maze_eraser.penup()
    self.maze_connections[square_number] = neighbor_square  # record the connection


  def assign_square_numbers(self, color):
    square_n = 0
    if color == "none" or color == "None":
      for row in range(1, self.rows + 1):
        for column in range(1, self.columns + 1):
          self.maze_square_coordinates[square_n] = [column, row]     # put (col, row) coordinates of the square in the map/dict
          square_n = square_n + 1
    else:
      maze_writer = self._maze_drawer
      maze_writer.setheading(0)
      maze_writer.penup()
      maze_writer.color(color)
      maze_writer.pensize(3)
      #maze_writer.tracer(1)
      text_align = -8
      for row in range(1, self.rows + 1):
        for column in range(1, self.columns + 1):
          c = self.init_x + (column - 0.5) * self.square_size # square column center
          r = self.init_y - (row - 0.5) * self.square_size    # square row center
          maze_writer.goto(c + text_align, r)                 # shift a bit to align text with square center
          maze_writer.write(square_n)
          self.maze_square_coordinates[square_n] = [column, row]     # put (col, row) coordinates of the square in the map/dict
          square_n = square_n + 1



  def get_square_coordinates(self, square):
    return self.maze_square_coordinates[square]

  def get_square_size(self):
    return self.square_size
  
  
  def get_columns(self):
    return self.columns
    
  def get_rows(self):
    return self.rows
    
  def get_blockers(self):
    return self.blockers

  def get_init_x(self):
    return self.init_x
    
  def get_init_y(self):
    return self.init_y
    

