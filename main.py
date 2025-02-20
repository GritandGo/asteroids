import pygame
from constants import *
import player as player_module
import asteroidfield
import asteroid
import sys
import shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    asteroids_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    asteroid.Asteroid.containers = (asteroids_group, updatable, drawable)
    player_module.Player.containers = (updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    shot.Shot.containers = (shots, updatable, drawable)


    my_ship = player_module.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field_object = asteroidfield.AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for a in asteroids_group:
            if a.collision_detection(my_ship) == True:
                sys.exit("Game over!")
            for bullet in shots:
                if bullet.collision_detection(a) == True:
                    a.split()
                    bullet.kill()

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
    
if __name__ == "__main__":
    main()