# grid.py

#
# Contains the grid array and update step
#

import numpy as np
from config import GRID_WIDTH, GRID_HEIGHT, SAND
from materials import update_sand
from config import EMPTY

class Grid:
    def __init__(self):
        self.data = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

    def place(self, x, y, material):
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.data[y, x] = material

    def update(self):
        # falling sand logic
        for y in reversed(range(GRID_HEIGHT - 1)):
            for x in range(GRID_WIDTH):
                cell = self.data[y, x]

                if cell == SAND:
                    update_sand(self.data, x, y)