#!/usr/bin/python3
"""Island perimeter computing module.
"""
def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid of 0s and 1s.
    Args:
        grid (List[List[int]]): A 2D list representing the grid where 1s are land and 0s are water.
    Returns:
        int: The perimeter of the island.
    The function iterates through each cell in the grid. For each land cell (1), it checks its four neighbors
    (top, bottom, left, right). If a neighbor is water (0) or the cell is on the boundary of the grid, it 
    contributes to the perimeter.
    """
    if type(grid) != list:
        return 0;
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter