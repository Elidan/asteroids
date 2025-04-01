import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Paint background black
        pygame.Surface.fill(screen, color="black")

        # Draw all objects
        for objects in drawable:
         objects.draw(screen)

        # Update all objects
        updatable.update(dt)      

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                return

        #Get delta time - 60 FPS
        dt = clock.tick(60) / 1000

        # should always be at the end
        pygame.display.flip()

if __name__ == "__main__":
    main()