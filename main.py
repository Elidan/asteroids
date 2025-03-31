import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update player
        player.update(dt)

        # Paint background black
        pygame.Surface.fill(screen, color="black")

        # Paint the player
        player.draw(screen)

        #Get delta time - 60 FPS
        dt = clock.tick(60) / 1000

        # should always be at the end
        pygame.display.flip()

if __name__ == "__main__":
    main()