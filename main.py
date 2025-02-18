import pygame
from constants import *
import player as player_module


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    my_ship = player_module.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        my_ship.update(dt)
        my_ship.draw(screen)
        pygame.display.flip()
        
    
if __name__ == "__main__":
    main()