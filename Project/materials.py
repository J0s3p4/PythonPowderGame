# materials.py

#
# Holds logic for how different materials behave
#

from config import EMPTY, SAND

def update_sand(grid, x, y):
    if grid[y+1, x] == EMPTY:
        grid[y, x], grid[y+1, x] = EMPTY, SAND