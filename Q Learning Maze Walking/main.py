# filename: Q-Learning with OO Maze -Final - WIP
import maze, walker, goal
from random import randint, choice
from q_learning import *



#####################
#
# Main Program
#
#####################


# create the maze:
# ----------------
columns = 6
rows = 6
maze = maze.Maze(columns, rows)      # size of maze (columns, rows)

# Create the goal (you can move it around the maze, if you'd like):
# -----------------------------------------------------------------
goal_column = randint(1, maze.get_columns())
goal_row = randint(1, maze.get_rows())
goal = goal.Goal(maze, goal_column, goal_row, "gold")    # (maze, column, row, color)

# Create a maze walker (you can assume that the walker starts at the top left corner (1, 1):
# ------------------------------------------------------------------------------------------
walker = walker.Walker(maze, 1, 1, 0, "blue")     # (maze, column, row, heading, color)

# Placing blocking walls/tiles in the maze:
# -----------------------------------------
# When putting walls and bridges in the maze, don't put them on the goal and the walker:
excluded_blocks = [ [goal.get_column(), goal.get_row()], [walker.get_column(), walker.get_row()] ]


# For testing/debugging purposes:
# Block specific tiles in a 6-by-6 maze:
'''
maze.block_square(1, 2, "wall")
maze.block_square(1, 3, "wall")
maze.block_square(2, 2, "wall")
maze.block_square(2, 5, "wall")
maze.block_square(3, 4, "wall")
maze.block_square(4, 1, "wall")
maze.block_square(4, 2, "wall")
maze.block_square(4, 5, "wall")
maze.block_square(5, 1, "wall")
maze.block_square(5, 5, "wall")

# for testing of your Q-Learning algorithm, you can uncomment the following:
maze.block_square(1, 6, "wall")
maze.block_square(5, 3, "wall")
'''

######################################################################################################
#
# Code the block_squares() function AFTER your Q-Learning works with the hard-coded maze blocks above
#
######################################################################################################
# After your program works with the "hard-coded" maze above, write the following function,
# and comment out the hard-coded block_square() functions above.
# Randomly put blocks (or walls) in the maze.

# Your function should make sure that there are no "inaccessible islands" due to placement of walls/blocks
# otherwise, you Q-Learning algorithm may end up in an endless loop!

# randomly position number_of_wall_tiles in the maze, while excluding the blocks in the exclusion list.

maze.block_squares(9, excluded_blocks)      

##############
# Q-Learning:
##############
tiles_path = start_q_learning(maze, goal)
#print "Q-Learning path:", tiles_path
#print maze.get_blockers()

###################################
# Maze walking based on Q-Learning:
# (using the tiles_path above)
###################################

walker.start_trace()  # pendown
for tile in tiles_path:
  walker.goto_tile(maze, tile)
walker.stop_trace()  # penup

# Following code prevents graphics window from closing automatically when the program completes
import turtle
turtle.done()