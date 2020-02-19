
from graph import Graph
from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node, visited=None):
    parents = []
    for ancestor in ancestors:
        if ancestor[1] == starting_node:
            print(ancestor[0])
            parents.append(ancestor[0])
            starting_node = ancestor[0]
    if len(parents) < 1:
        return -1
    elif len(parents) == 2:
        return parents[-1]
        #return parents
    elif len(parents) > 2:
        return min(parents)
    else:
        return parents[0]
        # return parents