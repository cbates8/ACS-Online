import turtle, math, walker

from random import randint

class Maze:
  """ Maze class for representing a checkers-board-like maze made up of squares. """

  def __init__(self, columns, rows):
    """ Create a new maze with 'columns' columns and 'rows' rows """
    #print "width:", maze_drawer.window_width()
    #print "height:", maze_drawer.window_height()

    self.columns = columns        # the width of the maze (number of squares)
    self.rows = rows              # the height of the maze (number of squares)

    self.blockers = dict()        # containing all the non-empty squares ("blockers") in the maze
    self.wall_color = "red"
    self.bridge_color = "skyblue"

    self.blockers[self.wall_color] = []
    self.blockers[self.bridge_color] = []
    
    maze_drawer = turtle.Turtle()
    screen = turtle.Screen()

    window_width = 400
    window_height = 400
    screen.setup(width=window_width, height=window_height)

    self.square_size = 0.7 * min(window_width, window_height) / max(columns, rows)

    maze_drawer.setheading(0)
    maze_drawer.speed(50)
    #maze_drawer.tracer(2)
    maze_drawer.clear()
    maze_drawer.penup()
    
    self.init_x = -window_width * 0.3
    self.init_y = window_height * 0.3
    
    x = self.init_x
    y = self.init_y
    maze_drawer.goto(x, y)
    
    for r in range(rows + 1):
      maze_drawer.pendown()
      maze_drawer.goto(maze_drawer.xcor() + columns * self.square_size, maze_drawer.ycor())
      maze_drawer.penup()
      y = y - self.square_size
      maze_drawer.goto(x, y)
      
    x = -window_width * 0.3
    y = window_height * 0.3
    maze_drawer.goto(x, y)
    
    for c in range(columns + 1):
      maze_drawer.pendown()
      maze_drawer.goto(maze_drawer.xcor(), maze_drawer.ycor() - rows * self.square_size)
      maze_drawer.penup()
      x = x + self.square_size
      maze_drawer.goto(x, y)

    maze_drawer.hideturtle()
    
  
  # fill in (block off) a square/tile of the maze at (column, row) - or (x, y)
  # (1, 1) is the top-left square/block/tile

  def block_square(self, column, row, block_type):

    if column > self.columns or row > self.rows:
      raise ValueError("block_square(): The number of columns/rows doesn't match the size of the maze.")

    if block_type == "bridge":
      color = self.bridge_color
    else:
      color = self.wall_color
    
    if [column, row] in self.blockers[color]:
      raise ValueError("block_square(): The square at (" + str(column) + "," + str(row) + ") is already blocked/colored " + color)

    block_coord = self.square_size / 2
    screen = turtle.Screen()
    screen.register_shape("tile", ((-block_coord, -block_coord ), (block_coord,-block_coord), (block_coord,block_coord), (-block_coord,block_coord)))
    maze_blocker = turtle.Turtle()

    maze_blocker.shape("tile")
    maze_blocker.penup()
    maze_blocker.color(color)
    maze_blocker.goto(self.init_x + (column - 0.5) * self.square_size, self.init_y - (row - 0.5) * self.square_size)
    maze_blocker.stamp()
    
    if color not in self.blockers:
      self.blockers[color] = [ [column, row] ]
    else:
      self.blockers[color].append( [column, row] )
    #print self.blockers



  def block_squares(self, n_walls, excluded_blocks):
    if n_walls > (self.columns * self.rows - 2):
      raise ValueError("block_squares(): The number of blocked squares is too large for the size of the maze.")
    ###########################################
    # your code here, replacing the pass below
    ###########################################
    list_of_blockers = []
    for i in range(n_walls):
      column = randint(1, self.columns)
      row = randint(1, self.rows)
      
      while [column, row] in list_of_blockers or [column, row] in excluded_blocks:
        column = randint(1, self.columns)
        row = randint(1, self.rows)
      
      list_of_blockers.append([column, row])
      self.block_square(column, row, "wall")
      
  

  
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
