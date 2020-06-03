import matplotlib.pyplot as plt
import sys
from math import pi, cos, sin

def find_path(graph, start, end, path = []):
    """
    In given 'graph', find a path from node 'start' to 'end'.
    'graph' is a dictionary with nodes as keys and a list of
    connections (i.e.: other nodes) as value. 'start' and 'end'
    are nodes. A node is represented by a string (its name or
    label). 'path' is the way we have walked already (if any).

    The returned value is a list of nodes conforming the path.
    """
    # If we're there, just add the latest node and return
    if start == end:
        return path + [end]
    
    # If end is one of our connections, shortcut to it (don't look further)
    if end in graph[start]:
        return path + [start, end]

    # Loop on the connections of our starting point
    for node in graph[start]:

        # If the node is in the path already, forget it (loops)
        if node in path:  continue

        # Try out walks from each connected node
        # (including this node in the already walked path)
        newpath = find_path(graph, node, end, path + [start])

        # If the walk was OK, return it as a result, otherwise go on
        if newpath: return newpath

    # If no connection worked out fine, return impossible
    return None


def getXY(module, angle):
    """
    Return the vector 2-D coordinates for a given angle and module.
    """
    x = cos(angle) * module
    y = sin(angle) * module
    if abs(y) < 0.001: y = 0
    return x,y


def getNodes(graph):
    """
    Get the coordinates of the nodes of the graph in a circunference of
    radius 5 (same angle between two consecutive nodes).
    """
    nodes = {}
    # Loop on the graph nodes, move on our angle for each one
    for i, node in enumerate(sorted(graph)):
        angle = i * 2*pi/len(graph)
        nodes[node] = getXY(5, angle)
    return nodes


def add(v1, v2):
    """
    Returns the addition of a two 2-D vectors.
    """
    return (v1[0] + v2[0], v1[1] + v2[1])


def substract(v1, v2):
    """
    Returns the difference of a two 2-D vectors.
    """
    return (v2[0] - v1[0], v2[1] - v1[1])


def plotAll(graph, pathEnds = None, outfile = None):
    """
    Plot the specified graph and optionally path to the screen or
    to the specified file. 'graph' is a dictionary with nodes as keys
    and a list of connections (i.e.: other nodes) as value. 'pathEnds'
    is a list of two nodes (origin and destination). A node is
    represented by a string (its name or label).
    """

    # Calculate the nodes coordinate in the circunference
    nodes = getNodes(graph)

    # Plot the nodes (list of X coords, list of Y coords, red bullet)
    plt.axis('off')
    p = plt.plot([nodes[x][0] for x in nodes], [nodes[x][1] for x in nodes], 'ro')


    # Loop on the nodes
    half = len(nodes)/2
    for i, name in enumerate(sorted(nodes)):
        node = nodes[name]
#        print(node)
        # dlabel = distance of the node label to its location (below or above)
        if i > half:
            dlabel = -0.8
        else:
            dlabel = 0.6

        # Draw the node label
        plt.text(node[0], node[1]+dlabel, name, fontsize=12, fontweight='bold')

        # Now loop on the connections of the node at hand
        for con in graph[name]:

            # Coordinate diff between dest (connection) and org (current node)
            dx, dy = substract(node, nodes[con])

            # Plot connection
            plt.arrow(node[0], node[1], dx*0.88, dy*0.88, head_width=0.4, head_length=0.9)

    # If we were given a path, plot it as well
    if pathEnds:

        path = find_path(graph, pathEnds[0], pathEnds[1])

        if path:

            # Plot each one of the single-jump paths from the path list
            for i in range(len(path[:-1])):

                # Org, dest coordinates and diffs
                org = nodes[path[i]]
                dest = nodes[path[i+1]]
                dx, dy = substract(org, dest)

                # The Ox/y thing is to make the path arrow more easily visible
                if abs(dy)<0.2:  Ox, Oy = 0, 0.2
                else:            Ox, Oy = 0.2, 0

                # Plot
                plt.arrow(org[0] + Ox,  org[1] + Oy,  dx * 0.88,  dy * 0.88,
                      head_width=0.4, head_length=0.9,  edgecolor = 'r')
        else:
            plt.text(-3, 0,'NO POSSIBLE PATH BETWEEN %s and %s' %
                      (pathEnds[0], pathEnds[1]),  color='r')

