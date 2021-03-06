import turtle, math, goal, walker

from random import randint

class Maze:
  """ Maze class for representing a checkers-board-like maze made up of squares. """

  def __init__(self, columns, rows):
    """ Create a new maze with 'columns' columns and 'rows' rows """
    #print "width:", maze_drawer.window_width()
    #print "height:", maze_drawer.window_height()

    if columns % 2 == 0 or rows % 2 == 0: # even numbers given as parameters - not good!
      raise ValueError("maze init: Both numbers of columns/rows of the maze need to be ODD not even.")

    self.columns = columns        # the width of the maze (number of squares)
    self.rows = rows              # the height of the maze (number of squares)

    self.blockers = dict()        # containing all the non-empty squares ("blockers") in the maze
    self.wall_color = "red"
    self.bridge_color = "skyblue"

    self.blockers[self.wall_color] = []
    self.blockers[self.bridge_color] = []
    
    maze_drawer = turtle.Turtle()
    maze_drawer.hideturtle()
    screen = turtle.Screen()

    window_width = 400
    window_height = 400
    screen.setup(width=window_width, height=window_height)

    self.square_size = 0.7 * min(window_width, window_height) / max(columns, rows)

    maze_drawer.setheading(0)
    maze_drawer.speed(10)
    maze_drawer.clear()
    maze_drawer.penup()
    
    self.init_x = -window_width * 0.35
    self.init_y = window_height * 0.35
    
    x = self.init_x
    y = self.init_y
    maze_drawer.goto(x, y)
    
    #maze_drawer.tracer(10)    # accelerate drawing
    
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

    # create a turtle for marking blocked tiles:
    block_coord = self.square_size / 2
    self.screen = turtle.Screen()
    self.screen.register_shape("tile", ((-block_coord, -block_coord ), (block_coord,-block_coord), (block_coord,block_coord), (-block_coord,block_coord)))
    self.maze_blocker = turtle.Turtle()
    self.maze_blocker.hideturtle()

    self.maze_blocker.shape("tile")
    self.maze_blocker.penup()


  
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

    self.maze_blocker.penup()
    self.maze_blocker.color(color)
    self.maze_blocker.goto(self.init_x + (column - 0.5) * self.square_size, self.init_y - (row - 0.5) * self.square_size)
    self.maze_blocker.stamp()
    
    if color not in self.blockers:
      self.blockers[color] = [ [column, row] ]
    else:
      self.blockers[color].append( [column, row] )
    #print self.blockers


  def block_squares(self, n_walls, n_bridges, excluded_blocks):
    if n_walls + n_bridges > (self.columns * self.rows - 2):
      raise ValueError("block_squares(): The number of blocked squares is too large for the size of the maze.")

    for wall in range(n_walls):
      column = randint(1, self.columns)
      row = randint(1, self.rows)
      #while ([column, row] in self.blockers[self.wall_color]) or (column == goal_column and row == goal_row) or (column == walker_column and row == walker_row):
      while ([column, row] in self.blockers[self.wall_color]) or ( [column, row] in excluded_blocks ):
        column = randint(1, self.columns)
        row = randint(1, self.rows)
      #print "block at:", column, row
      self.block_square(column, row, "wall")
      
    for bridge in range(n_bridges):
      column = randint(1, self.columns)
      row = randint(1, self.rows)
      while ([column, row] in self.blockers[self.wall_color]) or ([column, row] in self.blockers[self.bridge_color]) or ( [column, row] in excluded_blocks ):
        column = randint(1, self.columns)
        row = randint(1, self.rows)
      self.block_square(column, row, "bridge")
      
  
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
    
  def update_display(self):
    self.screen.update()      # update the display which may be missing shapes due to tracer() acceleration.

    
    
