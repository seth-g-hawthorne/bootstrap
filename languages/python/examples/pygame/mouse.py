import pygame 

# Initialize pygame 
pygame.init() 

# Create a window 
window = pygame.display.set_mode((800, 600)) 

# Main loop 
while True: 
    # Get the mouse position 
    mouse_position = pygame.mouse.get_pos() 

    # Get the mouse button state 
    mouse_pressed = pygame.mouse.get_pressed() 

    # Quitting the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

    # Drawing a circle when mouse is pressed 
    if mouse_pressed[0] == 1: 
        pygame.draw.circle(window, (255, 0, 0), mouse_position, 20) 

    # Update the display 
    pygame.display.update() 