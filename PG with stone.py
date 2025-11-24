import pygame
import numpy as np

# --- Config ---
WIDTH, HEIGHT = 400, 300
CELL_SIZE = 2
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Particle types
EMPTY = 0
SAND = 1
STONE = 2

# Grid
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

# Stones list (each stone is a rectangle block)
stones = []

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Stone dragging
dragging = False
start_pos = (0, 0)

# --- NEW: material selected ---
current_material = SAND   # Default is sand

running = True
while running:
    mx, my = pygame.mouse.get_pos()
    gx, gy = mx // CELL_SIZE, my // CELL_SIZE
    gx = min(max(gx, 0), GRID_WIDTH-1)
    gy = min(max(gy, 0), GRID_HEIGHT-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- NEW: Key presses select material ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_material = SAND
            elif event.key == pygame.K_2:
                current_material = STONE

        # Start stone drag (right mouse)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            dragging = True
            start_pos = (gx, gy)

        # Release stone drag
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and dragging:
            dragging = False
            x0, y0 = start_pos
            x1, y1 = gx, gy
            x0, x1 = sorted((x0, x1))
            y0, y1 = sorted((y0, y1))
            w, h = x1-x0+1, y1-y0+1

            # Place stone in grid
            grid[y0:y1+1, x0:x1+1] = STONE

            # Add to stone list
            stones.append({'x': x0, 'y': y0, 'w': w, 'h': h})

    # --- Left click places current material ---
    if pygame.mouse.get_pressed()[0]:
        grid[gy, gx] = current_material

    # --- Update grid ---
    # Falling sand
    for y in reversed(range(GRID_HEIGHT-1)):
        for x in range(GRID_WIDTH):
            if grid[y, x] == SAND:
                if grid[y+1, x] == EMPTY:
                    grid[y, x], grid[y+1, x] = EMPTY, SAND

    # Falling stones (optimized)
    for stone in stones:
        x, y, w, h = stone['x'], stone['y'], stone['w'], stone['h']
        if y + h < GRID_HEIGHT:
            # Check bottom row for free space
            can_fall = True
            for i in range(w):
                if grid[y+h, x+i] != EMPTY:
                    can_fall = False
                    break
            if can_fall:
                grid[y:y+h, x:x+w] = EMPTY
                stone['y'] += 1
                y = stone['y']
                grid[y:y+h, x:x+w] = STONE

    # --- Draw ---
    screen.fill((0, 0, 0))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y, x] == SAND:
                pygame.draw.rect(screen, (194, 178, 128), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[y, x] == STONE:
                pygame.draw.rect(screen, (120, 120, 120), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw drag rectangle preview
    if dragging:
        x0, y0 = start_pos
        rect_x = min(x0, gx) * CELL_SIZE
        rect_y = min(y0, gy) * CELL_SIZE
        rect_w = (abs(x0-gx)+1) * CELL_SIZE
        rect_h = (abs(y0-gy)+1) * CELL_SIZE
        pygame.draw.rect(screen, (200,200,200), (rect_x, rect_y, rect_w, rect_h), 1)

    pygame.display.flip()
    clock.tick(60)