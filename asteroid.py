from constants import *
from circleshape import CircleShape
import random

import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            # Create two smaller asteroids
            new_radius = self.radius * 0.5
            angle = random.uniform(0, 360)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(angle + 180) * 1.2
            position1 = self.position + pygame.Vector2(0, 1).rotate(angle) * self.radius
            position2 = self.position + pygame.Vector2(0, 1).rotate(angle + 180) * self.radius
            asteroid1 = Asteroid(position1.x, position1.y, new_radius)
            asteroid1.velocity = velocity1
            asteroid2 = Asteroid(position2.x, position2.y, new_radius)
            asteroid2.velocity = velocity2
            return [asteroid1, asteroid2]
        return []
