import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def get_points(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            return 10
        elif self.radius == ASTEROID_MAX_RADIUS:
            return 5
        else:
            return 7

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20.0, 50.0)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteriod1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteriod1.velocity = vector1 * 1.2
        new_asteriod2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteriod2.velocity = vector2 * 1.2
