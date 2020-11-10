# filename: Recursion - Maze Walking - Project - WIP
import maze, walker, goal
from random import randint, choice
from math import floor

def block_line(maze, start_column, start_row, length, direction, block_type):
  # direction of the line can be: "down" (going top-to-bottom) or "right" (going left-to-right)
  if direction == "down":
    for i in range(length):
        maze.block_square(start_column, start_row + i, block_type)
  elif direction == "right":
    for i in range(length):
        maze.block_square(start_column + i, start_row, block_type)
  maze.update_display()   # Don't change this line. display acceleration "flush the pipe"


def block_maze_perimeter(maze):
  # put blocks/walls all around the maze perimeter:
  block_line(maze, 1, 1, maze.get_rows(), "down", "wall")
  block_line(maze, maze.get_columns(), 1, maze.get_rows(), "down", "wall")
  block_line(maze, 2, 1, maze.get_columns() - 2, "right", "wall")
  block_line(maze, 2, maze.get_rows(), maze.get_columns() - 2, "right", "wall")
  


def determine_wall_length(columns, rows, orientation):
  # columns and rows are the ones for the maze (or sub-maze) to be blocked with a wall
  wall_length = 0
  if orientation == "down":
    wall_length = rows  - 2
  elif orientation == "right":
    wall_length = columns  - 2
  return wall_length


def determine_wall_start_column(columns, maze_start_column, orientation):
  wall_start_column = 0     # initialize
  if orientation == "down":
    wall_start_column = randint(maze_start_column + 2, maze_start_column + columns - 3)
    if wall_start_column % 2 == 0:
      wall_start_column = wall_start_column + choice([-1, 1]) # add or subtract 1 to make it odd
  elif orientation == "right":
    wall_start_column = maze_start_column + 1
  return wall_start_column


def determine_wall_start_row(rows, maze_start_row, orientation):
  wall_start_row = 0    # initialize
  if orientation == "down":
    wall_start_row = maze_start_row + 1
  elif orientation == "right":
    wall_start_row = randint(maze_start_row + 2, maze_start_row + rows - 3)
    if wall_start_row % 2 == 0:
      wall_start_row = wall_start_row + choice([-1, 1]) # add or subtract 1 to make it odd
  return wall_start_row


def determine_hole_location(wall_start_column, wall_start_row, wall_length, orientation):
  hole_column = 0    # initialize
  hole_row = 0       # initialize
  if orientation == "down":
    hole_row = int(floor(randint(wall_start_row, wall_start_row + wall_length - 1) / 2) * 2)
    hole_column = wall_start_column
  elif orientation == "right":
    hole_column = int(floor(randint(wall_start_column, wall_start_column + wall_length - 1) / 2) * 2)
    hole_row = wall_start_row
  return (hole_column, hole_row)

def block_line_with_hole(maze, start_column, start_row, length, orientation, hole_column, hole_row, block_type):
  for i in range(length):
    if orientation == "down":
      if start_row + i != hole_row:
        maze.block_square(start_column, start_row + i, block_type)
    elif orientation == "right": 
      if start_column + i != hole_column:
        maze.block_square(start_column + i, start_row, block_type)



def pick_orientation(columns, rows):
  if columns > rows:
    return 'down'
  elif rows > columns:
    return 'right'
  elif columns == rows:
    return choice(['down', 'right'])


def process_maze(maze, maze_start_column, maze_start_row, maze_columns, maze_rows):
  '''
    Parameters:
    maze - the maze object which we need to process.
    maze_start_column and maze_start_row are the coordinates of the top-left corner of the maze 
    (not the line/wall we want to draw!)
  '''
  #print "starting maze:", maze_start_column, maze_start_row, maze_columns, maze_rows
  if maze_rows <= 3 or maze_columns <= 3: # recursion base case (stop condition): maze too small to draw walls in it
    return
  
  orientation = pick_orientation(maze_columns, maze_rows)
  wall_length = determine_wall_length(maze_columns, maze_rows, orientation)
  wall_start_column = determine_wall_start_column(maze_columns, maze_start_column, orientation)
  wall_start_row = determine_wall_start_row(maze_rows, maze_start_row, orientation)
  (hole_column, hole_row) = determine_hole_location(wall_start_column, wall_start_row, wall_length, orientation)

  # build a wall (going "down" (top-to-bottom) or "right" (left-to-right)):
  block_line_with_hole(maze, wall_start_column, wall_start_row, wall_length, orientation, hole_column, hole_row, "wall")

  if orientation == "down":
    # handle left sub maze (left of the wall line):
    left_sub_maze_columns = wall_start_column - maze_start_column + 1
    left_sub_maze_rows = wall_length + 2
    
    # a recursive call:
    process_maze(maze, maze_start_column, maze_start_row, left_sub_maze_columns, left_sub_maze_rows)

    # handle right sub maze (right of the wall line):
    right_sub_maze_columns = maze_columns - left_sub_maze_columns + 1
    right_sub_maze_rows = left_sub_maze_rows

    # a recursive call:
    process_maze(maze, wall_start_column, maze_start_row, right_sub_maze_columns, right_sub_maze_rows)

  else: # orientation is "right" (going across):
    # handle the top sub maze (above the wall line):
    top_sub_maze_rows = wall_start_row - maze_start_row + 1
    top_sub_maze_columns = wall_length + 2
    
    # a recursive call:
    process_maze(maze, maze_start_column, maze_start_row, top_sub_maze_columns, top_sub_maze_rows)

    # handle the bottom sub maze (below the wall line):
    bottom_sub_maze_rows = maze_rows - top_sub_maze_rows + 1
    bottom_sub_maze_columns = top_sub_maze_columns

    # a recursive call:
    process_maze(maze, maze_start_column, wall_start_row, bottom_sub_maze_columns, bottom_sub_maze_rows)

#######################################
#
# Your code goes in the function below
#
#######################################

def find_goal_starting_at(column, row):
  '''
    Recursively walk a maze: 
    Start at the beginning (top-left), and check if you can move in any direction,
    marking cells (blocked, visited, or free) as you go.
    
    The almost-pseudo-code:
    
    First, put the cell you are considering visiting into the path list.
    
    Now check for the base cases (the simple case):
      If this cell happens to be the goal cell, you are done, return True.
      Check if you can move to that cell (the cell is within the bounds of the maze).
      if it's out of bounds, pop the cell from the list (it will not be part of the path) and return False (i.e., you don't have a cell that's part of the path)
      Then check if this cell is not blocked or marked.
      If the cell is blocked/wall, or had been visited/marked), pop the cell from the list (it will not be part of the path) and return False (i.e., you don't have a cell that's part of the path)

    Do the recursive cases:
      if calling the function with the cell on the right of this one returns True, then return True (i.e., you found another cell which is on the path)
      if calling the function with the cell on the left of this one returns True, then return True (i.e., you found another cell which is on the path)
      if calling the function with the cell above this one returns True, then return True (i.e., you found another cell which is on the path)
      if calling the function with the cell below this one returns True, then return True (i.e., you found another cell which is on the path)
      
    At the end, the path list contains only the cells which are available/valid to walk through from
    start to goal.
    
    Implement the algorithm, and mark visited cells by calling: 
    maze.block_square(column, row, "bridge")
    which will place a light-blue block in the cell/position [column, row]
  '''
  
  # your code goes here (replacing the pass statement:
  
  global path                   # a list to keep all valid [column, row] locations
  path.append([column, row])    # first thing is to save the current cell, if it is valid. pop it later, if it's not valid.
  
  if column == goal_column and row == goal_row:
    return True
  if walker.is_tile_blocked(maze, column, row) == True or walker.is_tile_visited(maze, column, row) == True:
    path.pop()
    return False
  else:
    maze.block_square(column, row, 'bridge')
    walker.jump_to(column, row)
  
  if find_goal_starting_at(column + 1, row) == True: #Checks the space to the left
    return True
  if find_goal_starting_at(column - 1, row) == True: #Checks the space to the right
    return True
  if find_goal_starting_at(column, row - 1) == True: #Checks the space above
    return True
  if find_goal_starting_at(column, row + 1) == True: #Checks the space below
    return True
  else:
    path.pop()
    return False





#####################
#
# Main Program
#
#####################


# create a random maze:
# ---------------------
columns = 23   # should be an odd number!
rows = 19      # should be an odd number!
maze = maze.Maze(columns, rows)      # size of maze (columns, rows)
block_maze_perimeter(maze)
process_maze(maze, 1, 1, columns, rows)

# Create the goal:
# ----------------
# The default position in the lower right corner of the maze, inside the maze (hence -1):
goal = goal.Goal(maze, columns - 1, rows - 1, "gold")    # (maze, column, row, color)

# Create a maze walker:
# ---------------------
# The position should be top-right, inside the maze (hence 2,2) 
walker = walker.Walker(maze, 2, 2, 0, "blue")     # (maze, column, row, heading, color)


# Recursively walk the maze:
#---------------------------
# find the locations of the walker (at the starting position) and the goal:
walker_column = walker.get_column()
walker_row = walker.get_row()
goal_column = goal.get_column()
goal_row = goal.get_row()
# init the list which will contain the chain of cells leading from start to goal:
path = []                         
# recursively find the path from start to goal:
find_goal_starting_at(walker_column, walker_row)
# after finding the path, go back to the starting point:
walker.jump_to(walker_column, walker_row)
# pendown for tracing/coloring the path:
walker.start_trace()
# go through all locations from start to goal:
for block in path:
  walker.jump_to(block[0], block[1])
maze.update_display()

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()