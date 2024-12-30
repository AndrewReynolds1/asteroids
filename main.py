# this allows us to use code from the open-source pygame library
import pygame
# import constants that are used in game.
from constants import *
# import player class
from player import Player
#import asteroid class
from asteroid import Asteroid
#import asteroid field
from asteroidfield import AsteroidField

def main():
    # Initializing all used pygame modules
    pygame.init()

    # Create the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initiate the clock so we can restrict our game to 60 FPS and great the
    # dt variable so that we can track the time since the last frame was drawn
    clock = pygame.time.Clock()
    dt = 0


    # Create pygame groups to help keep everything tidy
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #Initiate the Player Triangle
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Initiate the Asteroid Field
    asteroidfield = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #This is the main game loop
    while True:
        #This will check if the user has closed the window and exit the game loop if they do. 
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all sprites
        for obj in updatable:
            obj.update(dt)

        #This fills the Screen Black
        screen.fill("black")
        
        # draw sprites
        for obj in drawable:
            obj.draw(screen)


        #method to refresh the screen.
        pygame.display.flip()

        #At the end of each iteration of the game loop, call the .tick() method, and pass it 60. 
        #It will pause the game loop until 1/60th of a second has passed.
        #method also returns the amount of time that has passed since the last time it was called: the delta time. 
        #Divide the return value by 1000
        dt = clock.tick(MAX_FRAME_RATE) / 1000

if __name__ == "__main__":
    main()