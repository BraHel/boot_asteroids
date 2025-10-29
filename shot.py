import pygame
from circleshape import * 
from constants import * 

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        #self.pos = [x,y]
    
    def rotate(self,dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        