""" Lattice paths
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""

import math


def lattice_path_count_recursive(position):
    """Returns number of routes to bottom right corner (0, 0) from current position. """
    if position[0] == 0:
        path_count = 1
    elif position[1] == 0:
        path_count = 1
    else:
        path_count = lattice_path_count_recursive((position[0] - 1, position[1]))
        path_count += lattice_path_count_recursive((position[0], position[1] - 1))

    return path_count


def lattice_path_count_formula(grid_size):
    """Returns number of lattice paths in a grid_size grid. """
    path_node_count = 2*grid_size - 1   # the number of nodes in each path
    path_count = int(2*math.factorial(path_node_count)/(math.factorial(grid_size)*math.factorial(grid_size-1)))
    return path_count


if __name__ == '__main__':  # only if run as a script, skip when imported as module
    for n in range(1, 11):
        print("{0}x{0}:".format(n), lattice_path_count_recursive((n, n)), lattice_path_count_formula(n))
    print()
    print("20x20:", lattice_path_count_formula(20))
