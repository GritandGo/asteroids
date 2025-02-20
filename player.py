import circleshape
import constants
import pygame
import shot
from constants import *


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation = constants.PLAYER_TURN_SPEED * dt + self.rotation


    def update(self, dt):
        self.timer -= dt
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
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
                    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt



    def shoot(self):
        new_shot = shot.Shot(self.position, self.velocity, SHOT_RADIUS)
        shooting = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity += shooting * constants.PLAYER_SHOOT_SPEED
