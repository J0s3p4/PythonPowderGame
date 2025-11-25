# materials.py

#
# Holds logic for how different materials behave
#

from config import EMPTY, SAND, WATER
import random

def update_sand(grid, x, y):

    below = grid[y+1, x]

    # Fall into empty (If empty below, fall down)
    if below == EMPTY:
        grid[y, x], grid[y+1, x] = EMPTY, SAND
        return

    # Fall into / displace water
    if below == WATER:
        grid[y, x], grid[y+1, x] = WATER, SAND
        return

def update_water(grid, x, y):
    h, w = grid.shape

    # Try to fall straight down
    if y + 1 < h and grid[y+1, x] == EMPTY:
        grid[y, x], grid[y+1, x] = EMPTY, WATER
        return

    # Try random diagonal directions
    dirs = [-1, 1]
    random.shuffle(dirs)

    # Down-left or down-right
    for dx in dirs:
        nx = x + dx
        if 0 <= nx < w and y+1 < h and grid[y+1, nx] == EMPTY:
            grid[y, x], grid[y+1, nx] = EMPTY, WATER
            return

    # Left or right
    for dx in dirs:
        nx = x + dx
        if 0 <= nx < w and grid[y, nx] == EMPTY:
            grid[y, x], grid[y, nx] = EMPTY, WATER
            return