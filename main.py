import pygame

from constants import *
from highscore import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    game_running = True
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
    shots = pygame.sprite.Group()

    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player_score = 0
    asteroid_field = AsteroidField()

    # Game Loop Start
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game was closed")
                print(f"Score: {player_score}")
                return
    
        # Update all objects
        updatable.update(dt) 

        # Check for collisions with asteroids
        for asteroid in asteroids:
            # Player collision
            if asteroid.collision_detection(player):
                print("Game over!\n")
                print(f"Your score: {player_score}")
                game_running = False

            # Shot collision
            for shot in shots:
                if asteroid.collision_detection(shot):
                    asteroid.split()
                    player_score += asteroid.get_points()
                    shot.kill()
        

        # Paint background black
        pygame.Surface.fill(screen, color="black") 

        # Draw all objects
        for objects in drawable:
         objects.draw(screen)     

        # should always be at the end
        pygame.display.flip()

         #Get delta time - 60 FPS
        dt = clock.tick(60) / 1000
    # Game Loop End

    print_highscores_to_console()
    if(is_top10(player_score)):
        user_input = input("Write your name to add it as a high score! Just type 'n' to skip\n")
        if(user_input == "n"):
            return
        else:
            add_new_score(user_input, player_score)
            print_highscores_to_console()
        

if __name__ == "__main__":
    main()