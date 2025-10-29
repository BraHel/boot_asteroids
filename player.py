import pygame
from circleshape import * 
from constants import * 
from shot import *
import math

class Player(CircleShape):
    
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        mytriangle = self.triangle()
        pygame.draw.polygon(screen,"white",mytriangle,2)

    def rotate(self,dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.shot_cooldown -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        #print()
        if self.shot_cooldown > 0:
            return
        else:
            new_shot = Shot(self.position[0],self.position[1],SHOT_RADIUS)
            new_shot.rotation = self.rotation + 90
            new_shot.velocity = pygame.Vector2(math.cos(math.radians(new_shot.rotation)),math.sin(math.radians(new_shot.rotation)))
            new_shot.velocity = new_shot.velocity * PLAYER_SHOOT_SPEED
            self.shot_cooldown = .3


