import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Rock, Paper, Scissors!")

    BG_COLOR = (255, 245, 200)
    WIDTH, HEIGHT = 1000, 800
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(BG_COLOR)

        # Your game logic goes here

        pygame.display.flip()
        clock.tick(60)  # Set the frame rate (frames per second)

if __name__ == "__main__":
    main()
