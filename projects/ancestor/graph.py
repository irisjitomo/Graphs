"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph():

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
            raise IndexError("Can't create edge based on given vertices")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a Queue
        queue = Queue()
        # create a list of visited nodes
        visited = set()
        # put starting node in the queue
        queue.enqueue(starting_vertex)
        # while queue not empty
        while queue.size() > 0:
        # pop first node out of queue
            vertex = queue.dequeue()
        # if not visited
            if vertex not in visited:
        #     mark as visited
                visited.add(vertex)
                print(vertex)
        #     Get adjacent and add to list
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
        # go to top of loop

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node is viisited
        if visited is None:
            visited = set()
        # If not...
        if starting_vertex not in visited:
        #     Mark it as visited
            visited.add(starting_vetex)
        #     Print
            print(starting_vertex)
        #     Call DFT_Recursive on each child
            for neighbor in self.get_neighbor(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue( [starting_vertex] )
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # CHECK IF IT'S THE TARGET
            # Check if it's been visited
            if v == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push( [starting_vertex] )
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v == destination_vertex:
                return v
            if v not in visited:
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # initialize visited if its not yet initialized
        if visited is None:
            visited = set()
        # initialize path if its not yet initialized
        if path is None:
            path = []
        # Check if starting vertex has been visited
        # If not...
        if starting_vetex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # If starting_vertex is destination:
            if starting_vertex == destination_vertex:
                return path_copy
                # return path
            # Mark as visited
            # Call DFS recursive on each neighbor
            for neighbor in self.get_neighbor(starting_vertex):
                path_copy = path.copy()
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path