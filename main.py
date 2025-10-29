# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameclock = pygame.time.Clock()

    start_x = SCREEN_WIDTH / 2
    start_y = SCREEN_HEIGHT / 2

    
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    game_player = Player(start_x, start_y)
    the_asteroidfield = AsteroidField()
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        for ast in asteroids:
            if game_player.collision(ast):
                print("Game over!")
                return


        
        #game_player.update(dt)
        #game_player.draw(screen)    



        pygame.display.flip()

        dt = (gameclock.tick(60) / 1000)




if __name__ == "__main__":
    main()
