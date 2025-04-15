
import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)










if __name__ == "__main__":
    main()
