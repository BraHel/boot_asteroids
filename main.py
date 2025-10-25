# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 

def main():
    pygame.init
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameclock = pygame.time.Clock()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")



        pygame.display.flip()

        dt = (gameclock.tick(60) / 1000)




if __name__ == "__main__":
    main()
