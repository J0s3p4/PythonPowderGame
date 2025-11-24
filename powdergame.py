import pygame
import numpy as np

# Screen and grid setup
WIDTH, HEIGHT = 400, 300
CELL_SIZE = 2
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)  # 0=empty, 1=sand, etc.

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Example: drop sand from mouse
    
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        gx = mx // CELL_SIZE
        gy =  my // CELL_SIZE
        if 0 <= gx < GRID_WIDTH and 0 <= gy < GRID_HEIGHT:
            grid[gy, gx] = 1

    
    # Update grid (simple falling sand rule)
    for y in reversed(range(GRID_HEIGHT)):
        for x in range(GRID_WIDTH):
            if grid[y, x] == 1:
                if y+1 < GRID_HEIGHT and grid[y+1, x] == 0:
                    grid[y, x], grid[y+1, x] = 0, 1

    # Draw
    screen.fill((0,0,0))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y, x] == 1:
                pygame.draw.rect(screen, (194, 178, 128), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()e
    clock.tick(60)