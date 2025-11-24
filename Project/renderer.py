# renderer.py

#
# Only handles drawing—not logic.
#

import pygame
from config import CELL_SIZE, SAND, STONE, WATER

SAND_COLOR = (194, 178, 128)
STONE_COLOR = (120, 120, 120)
WATER_COLOR = (64, 164, 223)   # light blue


def draw_grid(screen, grid):
    screen.fill((0, 0, 0))

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            cell = grid[y, x]

            if cell == SAND:
                pygame.draw.rect(screen, SAND_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == STONE:
                pygame.draw.rect(screen, STONE_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == WATER:
                pygame.draw.rect(screen, WATER_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))