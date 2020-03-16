"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('ERROR: VERTEX DOES NOT EXIST')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('ERROR: NO NEIGHBOR')
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        # while queue is not empty
        while queue.size() > 0:
            # dequeue first vertex
            temp = queue.dequeue()
            # check if visited
            # if not visited:
            if temp not in visited:
                print(temp)
                # mark it as visited
                visited.add(temp)
                # enqueue all of its neighbors
                for neighbor in self.get_neighbors(temp):
                    queue.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create a stack
        stack = Stack()
        #push vertex to stack
        stack.push(starting_vertex)
        # make visited set
        visited = set()
        # while stack is not empty:
        while stack.size() > 0:
            # pop first vertex
            temp = stack.pop()
            # if vertex is not in visited:
            if temp not in visited:
                print('----', temp)
                # mark as visited
                visited.add(temp)
                # push the neighbors
                for n in self.get_neighbors(temp):
                    stack.push(n)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print('dft_recursive', starting_vertex)
        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        queue = Queue()
        # Enqueue A PATH TO the starting vertex
        queue.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            node = path[-1] # grab the last vertex in the `path` list
            # Check if it's been visited
            # If it hasn't been visited...
            if node not in visited:
                # Mark it as visited
                visited.add(node)
                # CHECK IF IT'S THE TARGET
                if node == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                else:
                # Enqueue A PATH TO all it's neighbors
                    for neighbor in self.get_neighbors(node):
                        path_copy = path.copy()
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                        path_copy.append(neighbor)
                        queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create our stack
        stack = Stack()
        # make a visited set
        visited = set()
        # add our starting vertex (as a list/array) in our stack
        stack.push( [starting_vertex] )
        # while the stack is not empty
        while stack.size() > 0:
            # make a path, this is a list because were popping from the stack stack.pop()
            path = stack.pop()
            # get the very last vertex in that path list
            v = path[-1]
            # if v is the destination_vertex
            if v == destination_vertex:
                # return it
                return path
            # if v is not in visited
            if v not in visited:
                # add to visited set
                visited.add(v)
                # enqueue a path to all neighbors
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = path.copy()
                    # append that neighbor to the copy [starting_vertex, neighbor]
                    path_copy.append(neighbor)
                    # push that path_copy to the stack
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        path = path + [starting_vertex] # were concatinating 2 lists (adding 2 lists)
        if starting_vertex == destination_vertex:
            return path
        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                recursion = self.dfs_recursive(n, destination_vertex, visited, path)
                if recursion is not None:
                    return recursion

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
