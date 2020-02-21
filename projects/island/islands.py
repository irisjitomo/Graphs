Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. For example:


'''
1. Translate into graph terminology
2. Build the graph
3. Transverse the graph

Understand
Plan
E
R
'''

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def island_counter(matrix):
    # Create a visited matric of the same dimensions as the given matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)): # finding height
        visited.append([False] * len(matrix[0])) # finding width # Were making all the 0s and 1s into False
        # Once it is visited, it will be set to True
    # walk thru each cel of matrix
    for col in range(len(matrix[0])): #width of matrix
        for row in range(len(matrix)): #height of matrix
        # Count up the connected components
        # if it as not been visited...
        if not visited[row][col]:
            # When I reach a 1...
            if matrix[row][col] == 1:
                # Do a DFT and mark each 1 as visited
                visited = dft(col, row, matrix, visited)
                # increment counter by 1
                island_count += 1
            else:
                visited[row][col] = True
    return island_count


def dft(col, row, matrix, visited):
    '''
    This will mark each connected component as visited
    Return visited matrix
    '''
    s = Stack()
    # push starting node onto stack
    s.push( (col, row) )
    # while stack is not empty
    while s.size() > 0:
        # pop vertex from top of stack
        v = s.pop()
        col = v[o]
        row = v[1]
        # Check if visited, if not...
        if not visited[row][col]:
            # MArk it as visited
            visited[row][col] = True
            # Push each neighbot on top of stack
            for neighbor in get_neighbors((col,row), matrix):
                s.push(neighbor)
    return visited

def get_neighbors(vertex, graph_matrix):
    col = vertex[0]
    row = vertex[1]
    neighbors = []
    # Check North
    if row > 0 and graph_matrix[row - 1][col] == 1:
        neighbors.append((col, row-1))
    # Check South
    if row < len(graph_matrix) - 1 and graph_matrix[row + 1][col] == 1:
        neighbors.append((col, row + 1))
    # Check East
    if col < len(graph_matrix[0]) - 1 and graph_matrix[row][col+1] == 1:
        neighbors.append((col+1, row))
    # Check West
    if col > 0 and graph_matrix[row][col-1] == 1:
        neighbors.append((col - 1, row))
    # Return all directions that contain a 1
    return neighbors

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
)

island_counter(islands) # returns 4
