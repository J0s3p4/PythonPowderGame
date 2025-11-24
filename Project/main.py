# main.py

import pygame
from config import WIDTH, HEIGHT, SAND, STONE
from grid import Grid
from renderer import draw_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    grid = Grid()
    current_material = SAND

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        gx, gy = mx // 2, my // 2   # uses CELL_SIZE = 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_material = SAND
                elif event.key == pygame.K_2:
                    current_material = STONE

        # left click to place
        if pygame.mouse.get_pressed()[0]:
            grid.place(gx, gy, current_material)

        # update simulation
        grid.update()

        # draw
        draw_grid(screen, grid.data)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()