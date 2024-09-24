#!/usr/bin/python3
"""
Let's compute the perimeter of an island.
"""


def island_perimeter(grid):
    """
     This function computes the perimeter of an island.
    """
    result = 0
    if type(grid) is not list:
        return 0
    g = len(grid)
    for k, row in enumerate(grid):
        r = len(row)
        for q, cell in enumerate(row):
            if cell == 0:
                continue
            island_edges = (
                k == 0 or (len(grid[k - 1]) > q and grid[k - 1][q] == 0),
                q == r - 1 or (r > q + 1 and row[q + 1] == 0),
                k == g - 1 or (len(grid[k + 1]) > q and grid[k + 1][q] == 0),
                q == 0 or row[q - 1] == 0,
            )
            result += sum(island_edges)
    return result
