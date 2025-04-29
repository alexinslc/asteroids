from constants import *
from circleshape import CircleShape
from shot import Shot

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        triangle = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), triangle, 2)

    def shoot(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      shot_position = self.position + forward * self.radius
      shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
      shot.velocity = forward * PLAYER_SHOOT_SPEED
      return shot


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            shot = self.shoot()
        # Normalize rotation to be within 0-360 degrees
        self.rotation %= 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]