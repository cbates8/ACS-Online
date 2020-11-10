# filename: Binary Tree - Maze Definition - WIP

import tree_maze
from random import choice
# ---------------------------------------------------
# Create the maze - just a grid of rows and columns:
# ---------------------------------------------------
columns = 5
rows = 5
maze = tree_maze.Tree_Maze(columns, rows)      # size of maze (columns, rows)


# ------------------------------------------------------------
# Create a maze by randomly deleting either 
# the "Eastern" (left) or "Southern" (bottom) wall of every cell.
#
# Your code, ENCAPSULATED IN A FUNCTION, will replace the erase_line() 
# calls below, which you need to comment out before running your function.
#
# ------------------------------------------------------------
print ("\n Maze erase commands:\n")
'''maze.erase_line(0, 'South')
maze.erase_line(1, 'East')
maze.erase_line(2, 'South')
maze.erase_line(3, 'East')
maze.erase_line(4, 'South')
maze.erase_line(5, 'South')
maze.erase_line(6, 'East')
maze.erase_line(7, 'East')
maze.erase_line(8, 'None')'''

def create_maze():
  ''' Erases lines to create a maze '''
  
  maze_size = columns * rows
  
  #Creates a list of cells in the bottom row
  bottom_row = []
  for i in range(maze_size - columns, maze_size):
    bottom_row.append(i)
  
  #Creates a list of cells in the far-right column
  right_column = []
  for l in range(rows):
    right_column.append((l * columns)-1)
  
  for cell in range(0, maze_size-1):
    if cell in right_column:
      maze.erase_line(cell, 'South')
    elif cell in bottom_row:
      maze.erase_line(cell, 'East')
    else:
      maze.erase_line(cell, choice(['East', 'South']))
  maze.erase_line(maze_size-1, "None")
  
create_maze()
# Don't modify the code below:
# Print square numbers for each cell of the maze: color = "red", "blue", etc., or,
#maze.assign_square_numbers(color = "none")    # no numbers are displayed
maze.assign_square_numbers("blue")

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()