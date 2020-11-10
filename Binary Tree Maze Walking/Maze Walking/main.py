# filename: Binary Tree - Maze Walking - WIP

import tree_maze, walker
from random import choice
from maze_structure import search_node

#####################
#
# Main Program
#
#####################


# Create the maze:
# ----------------
columns = 9
rows = 9
maze = tree_maze.Tree_Maze(columns, rows)      # size of maze (columns, rows)

# ------------------------------------------------------------
# Create a maze by randomly deleting either the "Eastern" (left) or "Southern" (bottom) wall of every cell:
# ------------------------------------------------------------
print ("\n Maze erase commands:\n")
######################################################################################
# your code for random maze generation goes into the function maze.create_random_maze()
# in the tree_maze.py tab.
######################################################################################

maze.create_random_maze()


# Don't change the code below:
# Prints square numbers for each cell of the maze: color = "red", "blue", etc., or,
#maze.assign_square_numbers(color = "none")    # no numbers are displayed
maze.assign_square_numbers("Blue")

# Get the binary tree structure of the maze (in a dictionary):
root_node = 0

######################################################################################
# your code for getting the maze tree structure goes into the function maze.get_tree_structure()
# in the tree_maze.py tab.
######################################################################################
maze_structure = maze.get_tree_structure(root_node)
print ("\n\n The maze binary tree structure:\n", maze_structure)


# Don't change the code below:
# ------------------------------------------------------------
# Find a path in the maze, from the top-left corner (start) to the bottom-right (goal).
# This takes advantage of the "bias" of this maze for a path across the diagonal top-left to bottom-right.
# ------------------------------------------------------------
node = root_node
goal_node = maze.columns * maze.rows - 1
path_squares = []

##########################################################################################
# your code for putting the walking path information into the path_squares list goes here:
# (your code should replace the line assigning a hard-coded list to path_squares)
##########################################################################################

#path_squares = [0, 1, 6, 11, 12, 17, 18, 19, 24]

def create_path():
  global node, goal_node
  while node != goal_node:
    path_squares.append(node)
    child1 = maze_structure[node][0]
    child2 = maze_structure[node][1]
    
    if child1 != None and child2 != None:
      if child1 > child2:
        node = child1
      else:
        node = child2
    elif child1 == None:
      node = child2
    elif child2 == None:
      node = child1
  path_squares.append(goal_node)

create_path()

# Don't change the code below:
print ("\n\n A path through the maze, from %d to %d:\n %s" % (root_node, goal_node, path_squares))


# ------------------------------------------------------------
# Create a maze walker and walk the maze: from the top-left corner (start) to the bottom-right (goal).
# ------------------------------------------------------------

walker = walker.Walker(maze, 1, 1, 0, "blue")     # (maze, column, row, heading, color)

walker.start_trace()  # pendown

####################################################################################################
# your code for moving the walker through the maze, following the squares in path_squares goes here:
# (your code below should use walker.goto_tile() to move from square to square)
####################################################################################################

for square in path_squares:
  coords = maze.get_square_coordinates(square)
  walker.goto_tile(maze, coords)



# Don't change the code below
walker.stop_trace()  # penup

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()