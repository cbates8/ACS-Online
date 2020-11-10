
def insert_node(node, tree):
  if node not in tree:
    tree[node] = [None, None]
  return tree[node]

def insert_children(node, tree, maze):
  maze_connections = maze.maze_connections
  node_connections = get_all_node_connections(node, maze_connections)
  if node in maze_connections:
    for connection in node_connections:
      if connection != None and connection not in tree:
        if tree[node][0] == None:
          tree[node][0] = connection
        elif tree[node][1] == None:
          tree[node][1] = connection
        insert_node(connection, tree)
        insert_children(connection, tree, maze)


def get_all_node_connections(node, maze_connections):
  if node in maze_connections:
    node_connections = [ maze_connections[node] ]       # put in the node this node connects to
    for key in maze_connections.keys():
      if node == maze_connections[key]:                 # put in any node connected to it
        node_connections.append(key)
    return node_connections
  return [None]

intersection_nodes = []
def search_node(node, goal, path, tree):
  global intersection_nodes
  #print "visiting:", node, "intersections:", intersection_nodes
  if node == goal:
    path.append(node)
    return path
  if has_two_children(node, tree):
    intersection_nodes.append(node)  # mark node in case we need to roll back
  if has_no_children(node, tree):
    backout_node = path.pop()
    while backout_node != intersection_nodes[-1]:
      backout_node = path.pop()
    intersection_nodes.pop()        # done with one interesction on the list
    return path
  if has_left_child(node, tree):
    path.append(node)
    search_node(get_left_child(node, tree), goal, path, tree)
  if has_right_child(node, tree):
    path.append(node)
    search_node(get_right_child(node, tree), goal, path, tree)
  

def has_no_children(node, tree):
  return tree[node][0] == None and tree[node][1] == None
 

def has_two_children(node, tree):
  return tree[node][0] != None and tree[node][1] != None
 

def has_left_child(node, tree):
  return tree[node][0] != None
 

def has_right_child(node, tree):
  return tree[node][1] != None
 

def get_left_child(node, tree):
  return tree[node][0]
 

def get_right_child(node, tree):
  return tree[node][1]
 

