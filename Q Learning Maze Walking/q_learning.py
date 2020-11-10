from math import ceil, sqrt
from random import choice, randint


def start_q_learning(maze, goal):
  tiles_path = []
  learning_rate = 0.8  # alpha (from Wikipedia)
  maze_size = maze.get_columns() * maze.get_rows()
  goal_state = (goal.get_row() - 1) * maze.get_columns() + goal.get_column() - 1
  R_matrix = []
  Q_matrix = []
  
  ''' Initialize R Matrix '''
  #fill matrix with -1
  for i in range(maze_size):
    R_matrix.append([])
    for l in range(maze_size):
      R_matrix[i].append(-1)

  #add 0 when there is a link between nodes
  for state in range(maze_size):
    
    #Right Node
    for blocker in maze.get_blockers()["red"]:
      if state + 1 < maze_size and ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1) != state + 1:
        R_matrix[state][state + 1] = 0
        #print ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1), state + 1
      else:
        if state + 1 < 36:  
          R_matrix[state][state + 1] = -1  
        break
    
    #Left Node
    for blocker in maze.get_blockers()["red"]:
      if state - 1 < maze_size and state - 1 >= 0 and ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1) != state - 1:
        R_matrix[state][state - 1] = 0
        #print ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1), state - 1
      else:
        if state - 1 < 36 and state - 1 >= 0:
          R_matrix[state][state - 1] = -1  
        break
    
    #Below Node
    for blocker in maze.get_blockers()["red"]:
      if state + maze.get_columns() < maze_size and ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1) != state + maze.get_columns():
        #print ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1), state + maze.get_columns()
        R_matrix[state][state + maze.get_columns()] = 0
      else:
        if state + maze.get_columns() < 36:
          R_matrix[state][state + maze.get_columns()] = -1
        break
    
    #Above Node
    for blocker in maze.get_blockers()["red"]:  
      if state - maze.get_columns() < maze_size and state - maze.get_columns() >= 0 and ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1) != state - maze.get_columns():
        R_matrix[state][state - maze.get_columns()] = 0
        #print ((blocker[1] - 1)*maze.get_columns() + blocker[0] - 1), state - maze.get_columns()
      else:
        if state - maze.get_columns() < 36 and state - maze.get_columns() >= 0:
          R_matrix[state][state - maze.get_columns()] = -1  
        break
    #print 
    
    #add 100 when move leads to goal state
    if state + 1 == goal_state: #if goal is to the right
      R_matrix[state][state + 1] = 100
    if state - 1 == goal_state: #if goal is to the left
      R_matrix[state][state - 1] = 100
    if state + maze.get_columns() == goal_state: #if the goal is below
      R_matrix[state][state + maze.get_columns()] = 100
    if state - maze.get_columns() == goal_state:#if the goal is above
      R_matrix[state][state - maze.get_columns()] = 100
    
    left_edge = [0]
    for node in range(maze.get_rows() -1):
      left_edge.append(left_edge[-1] + maze.get_columns())
    
    right_edge = [maze.get_columns() - 1]
    for node in range(maze.get_rows() -1):
      right_edge.append(right_edge[-1] + maze.get_columns())
    
    if state in left_edge:
      R_matrix[state][state - 1] = -1
    if state in right_edge and state < maze_size - 1:
      R_matrix[state][state + 1] = -1
      
  #print R_matrix
  
  ''' Initialize Q Matrix '''
  #fill matrix with 0
  for i in range(maze_size):
    Q_matrix.append([])
    for l in range(maze_size):
      Q_matrix[i].append(0)
  #print Q_matrix
  
  ''' Q-Learning Episodes '''
  #run 100 episodes
  for episode in range(100):
    state = randint(0, maze_size - 1) #select a random starting state
    is_goal_reached = False
    island_counter = 0
    while is_goal_reached == False: #repeats until the goal state is reached
      island_counter += 1
      #calculate possible actions
      possible_actions = []
      counter = 0
      for node in R_matrix[state]:
        if node != -1:
          possible_actions.append([node, counter])
        counter += 1
      
      #randomly chose a possible action
      if possible_actions == []:
        raise ValueError("Inacessable Island. Please restart program")
      random_action = choice(possible_actions)
      next_state = random_action[1]
      
      #Get maximum Q value of next state
      next_state_actions = dict()
      counter = 0
      for i in range(len(R_matrix[next_state])):
        if R_matrix[next_state][i] != -1:
          next_state_actions[Q_matrix[next_state][i]] = counter
        counter += 1
      
      best_actions = []
      for action in next_state_actions:
        if action == max(next_state_actions):
          best_actions.append([action, next_state_actions[action]])
      
      if best_actions == []:
        raise ValueError("Inacessable Island. Please restart program")
      chosen_action = choice(best_actions)[1]
      Q_matrix[state][next_state] = R_matrix[state][next_state] + learning_rate*Q_matrix[next_state][chosen_action]
      
      #set the next state as the current state
      state = next_state
      #print episode, state
      if island_counter == 10000:
        raise ValueError("Inacessable Island. Please restart program")
      if state == goal_state:
        is_goal_reached = True
      
  ''' Using the Q Matrix to create a path '''
  #initializing tiles_path
  state = 0
  is_goal_reached = False
  while is_goal_reached == False:
    tiles_path.append(state)
    if state == goal_state:
      is_goal_reached = True
    
    state = Q_matrix[state].index(max(Q_matrix[state])) #find action with highest Q value
    
  for i in range(len(tiles_path)):
    node_column = (tiles_path[i] + 1) % maze.get_rows()
    if node_column == 0:
      node_column = 6
    node_row = int(tiles_path[i]/maze.get_rows()) + 1
    tiles_path[i] = [node_column, node_row]
  #print tiles_path
  return tiles_path