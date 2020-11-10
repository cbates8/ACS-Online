#inspired by Jamis Buck at http://weblog.jamisbuck.org/2011/2/1/maze-generation-binary-tree-algorithm

import turtle
from maze_structure import *
from random import choice

class Tree_Maze:
  """ Tree Maze class for representing a checkers-board-like maze made up of "erasable" lines. """

  def __init__(self, columns, rows):
    """ Create a new maze with 'columns' columns and 'rows' rows """
    #print "width:", maze_drawer.window_width()
    #print "height:", maze_drawer.window_height()

    self.columns = columns                # the width of the maze (number of squares)
    self.rows = rows                      # the height of the maze (number of squares)
    self.maze_size = columns * rows       # total number of squares in the maze
    
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
    #maze_drawer.tracer(2)
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


  def get_connection_of(self, square_number):
    return self.maze_connections.get(square_number, None)
    
  
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


  def get_tree_structure(self, root_node):
    tree_structure = dict()
    
    ###############################################################
    # your code needs to replace this hard-coded tree structure,
    # based on your randomly generated maze.
    ###############################################################
    self.create_tree(tree_structure, root_node)
    return tree_structure

  def create_tree(self, dictionary, node): 
    child_node=[None, None]
    dictionary[node]=child_node
    node_counter = 0
    connecting_node = self.get_connection_of(node)
    
    if connecting_node != None and dictionary.get(connecting_node, None) == None: 
      child_node[node_counter] = connecting_node
      node_counter += 1
      self.create_tree(dictionary, connecting_node)
      
    for square in range(self.maze_size): 
      if dictionary.get(square, None) == None: 
        if self.get_connection_of(square) == node and square != connecting_node: 
          child_node[node_counter] = square
          self.create_tree(dictionary, square)

  def create_random_maze(self):
    # Creating a random binary tree maze:
    ###############################################################
    # your code needs to replace this hard-coded maze definition.
    # You can reuse your code from the previous project here.
    ###############################################################
  
    #Creates a list of cells in the bottom row
    bottom_row = []
    for i in range(self.maze_size - self.columns, self.maze_size):
      bottom_row.append(i)
    
    #Creates a list of cells in the far-right column
    right_column = []
    for l in range(self.rows):
      right_column.append((l * self.columns)-1)
    
    for cell in range(0, self.maze_size-1):
      if cell in right_column:
        self.erase_line(cell, 'South')
      elif cell in bottom_row:
        self.erase_line(cell, 'East')
      else:
        self.erase_line(cell, choice(['East', 'South']))
    self.erase_line(self.maze_size-1, "None")


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
    

