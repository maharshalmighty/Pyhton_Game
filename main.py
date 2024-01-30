import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("Block world!")

    BG_COLOR = (255, 245, 200) # To define the background color
    WIDTH, HEIGHT = 1000, 800 # To define the height and width
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # Define the Screen
    clock = pygame.time.Clock() # Setting the clock

    rectangle = Rect(30,30,60,60) # Defining out rectangle
    x= 0 # X coordiante
    y= 0 # Y coordinate
    while True:
        for event in pygame.event.get(): # To catch exit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN: # To catch keyboard press events
                if event.key==K_LEFT:
                    x=-5
                    y=0
                if event.key==K_RIGHT:
                    x=5
                    y=0
                if event.key==K_UP:
                    x=0
                    y=-5
                if event.key==K_DOWN:
                    x=0
                    y=+5
        SCREEN.fill(BG_COLOR) # Fill the screen
        pygame.draw.rect(SCREEN,(210, 245, 200),rectangle,100) # Draw the rectangle on the screen
        rectangle.move_ip(x,y) # Move the rectangle
        pygame.display.flip() # To update the entire display
        clock.tick(60)  # Set the frame rate (frames per second)

if __name__ == "__main__":
    main()
