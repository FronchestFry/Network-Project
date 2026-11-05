#Working out the UI for battleship

import pygame

Ship_grid = pygame.display.set_mode((500,500))


columns = 10
rows = 9

pygame.display.set_caption('Ship grid')

Ship_grid.fill((0,0,0))

#Draw a grid
for column in range(columns):
    pygame.draw.line(Ship_grid, (78, 240, 78), (((column * (Ship_grid.get_width()/columns))+(Ship_grid.get_width()/columns)/2),(Ship_grid.get_width()/columns)/2), (((column * (Ship_grid.get_width()/columns))+(Ship_grid.get_width()/columns)/2), 500-(Ship_grid.get_width()/columns)/2))

for row in range(rows):
    pygame.draw.line(Ship_grid, (78, 240, 78), ((Ship_grid.get_height()/rows)/2, ((row * (Ship_grid.get_height()/rows))+(Ship_grid.get_height()/rows)/2)), (500-(Ship_grid.get_height()/rows)/2, ((row * (Ship_grid.get_height()/rows))+(Ship_grid.get_height()/rows)/2)))


pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False