# filename: Recursion - Maze Definition - Project - WIP
# inspired by Buck 

import maze, walker, goal
from random import randint, choice
from math import floor

#############################
#
# Provided Utility Functions
#
#############################

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


#############################
#
# Your code goes below
#
#############################

def block_line_with_hole(maze, start_column, start_row, length, orientation, hole_column, hole_row, block_type):
  # Your code goes here (replacing the "pass" below)
  #
  # The code for creating walls with holes/passages/doorways.
  #
  # The parameters:
  # maze - the maze object, which needs to be divided with this line-with-a-hole.
  # start_column - the column number where the line starts (the maze starts at (1, 1) which is top left.
  # start_row - the row number where the line starts (the maze starts at (1, 1) which is top left.
  # length - the length of the line (how many rows or columns in length is it)
  # orientation - the direction of the line, which can be: "down" (going top-to-bottom) or "right" (going left-to-right)
  # hole_column - the column number where the hole ("passage" in the line) needs to be
  # hole_row - the row number where the hole ("passage" in the line) needs to be
  # block_type - "wall" or "bridge" (used in different mazes; not used here). Make it always a "wall"
  #
  # NOTE: when you call this function recursively, make sure you call it with the 
  # correct parameters, corresponding to the sub-maze you are dealing with.
  # For example, start_column and start_row will will be the ones for the big (initial) maze,
  # but when you call this function to deal with a sub-maze, you need to call it with the 
  # start_column and start_row of that sub-maze!
  
  for i in range(length):
    if orientation == "down":
      if start_row + i != hole_row:
        maze.block_square(start_column, start_row + i, block_type)
    elif orientation == "right": 
      if start_column + i != hole_column:
        maze.block_square(start_column + i, start_row, block_type)



def pick_orientation(columns, rows):
  # Your code goes here (replacing the "pass" below)
  #
  # Determine the direction for building a wall, depending on the shape of the maze (which maze side is longer?)
  # if the maze has more columns then rows, then the orientation will be vertical so, return "down"
  # if less, then the orientation should be horizontal, so return "right".
  # if it's a square, pick a random orientation (randomly return "down" or "right")
  #
  # The parameters:
  # columns - the number of columns of the maze.
  # rows - the number of rows of the maze.
  #
  # return "down" or "right"
  
  if columns > rows:
    return 'down'
  elif rows > columns:
    return 'right'
  elif columns == rows:
    return choice(['down', 'right'])


def process_maze(maze, maze_start_column, maze_start_row, maze_columns, maze_rows):
  # Your code goes here (replacing all the "Your code goes here" below)
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



#####################
#
# Main Program
#
#####################


# create an empty maze (with just perimeter walls):
# ------------------------------------
columns = 11   # should be an odd number!
rows = 9      # should be an odd number!
maze = maze.Maze(columns, rows)     # size of maze (columns, rows)
block_maze_perimeter(maze)         # draw the surrounding walls around the maze

# Create the goal:
# ----------------
# The default position in the lower right corner of the maze, inside the maze (hence -1):
goal = goal.Goal(maze, columns - 1, rows - 1, "gold")    # (maze, column, row, color)

# Create a maze walker:
# ---------------------
# The position should be top-right, inside the maze (hence 2,2) 
walker = walker.Walker(maze, 2, 2, 0, "blue")     # (maze, column, row, heading, color)
maze.update_display()     # don't change this line. for display acceleration.



# Create the maze walls:
#-----------------------
# the maze starts at (1, 1): top-left corner
maze_start_column = 1
maze_start_row = 1

process_maze(maze, maze_start_column, maze_start_row, columns, rows)  # add all maze walls recursively

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()