#add pigmentize and rich to make debugging easier
from rich.traceback import install
install(show_locals=True)

#make print statements "fancier"
from rich import print as rprint


# import contents of other modules and files
import pygame
import random
import sys
from constants import *
from player import Player
from asteroid import Asteroid  
from asteroidfield import AsteroidField  
from shot import Shot



def main():
   # initialize pygame (note syntax)
   pygame.init()
   #use pygame.display.set_mode to get new GUI window
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   #create groups updatable, drawable, and asteroids
   updatable  = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()    
   shots = pygame.sprite.Group()  

   #set containers: belongs in main since containers come from other class files
   Asteroid.containers = (asteroids, updatable, drawable) 
   Shot.containers = (shots, updatable, drawable)
   AsteroidField.containers = (updatable)
   asteroid_field = AsteroidField()
   Player.containers = (updatable, drawable)

   #create player instance within main
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   #create new pygame.time.Clock object with dt variable set to 0
   clock = pygame.time.Clock()
   dt = 0
   

   #5 game loop

   while True:
      # check for events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
   
      screen.fill(000)
      #update player position using updatable group
      updatable.update(dt)

      #check for collision
      for asteroid in asteroids:
         if asteroid.collides_with(player):
            print("Game over!")
            sys.exit()

      #code call .kill() method from pygame
         for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()  

      #draw player using method created for Player class
      # replace player.draw(screen) with iteration through drawable group
      for thing in drawable:
         thing.draw(screen)
      #refresh screen with pygame.display.flip()
      pygame.display.flip()
      #clock.tick() limits framerate to 60FPS
      # dividing by 1000 then returns time since last call in ms
      dt = clock.tick(60) / 1000

   
# main is called at end to run code of def main() above
if __name__ == "__main__":
    main()
