import pygame

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600))

# Create a circle
circle_rect = pygame.draw.circle(window, (255, 255, 255), (400, 300), 100)

# Create a surface for the rectangle
rectangle_surface = pygame.Surface((50, 50))
rectangle_surface.set_colorkey((0, 0, 0))

# Draw the rectangle on the surface
pygame.draw.rect(rectangle_surface, (255, 0, 0), (0, 0, 50, 50))

# Blit the surface onto the circle
window.blit(rectangle_surface, (375, 275))

# Main loop
while True:
    # Quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update the display
    pygame.display.update()