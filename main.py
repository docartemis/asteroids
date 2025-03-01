#add pigmentize and rich to make debugging easier
from rich.traceback import install
install(show_locals=True)

#make print statements "fancier"
from rich import print as rprint

import pygame

from constants import *


def main():
   #for L2: initialize pygame
   pygame.init()
   
   #next 3lines from last exercise are commented out
   #rprint("[bold green]Starting Asteroids![/bold green]")
   #rprint(f"Screen width: [cyan]{SCREEN_WIDTH}[/cyan]")
   #rprint(f"Screen height: [cyan]{SCREEN_HEIGHT}[/cyan]")
   
   #use pygame.display.set_mode to get new GUI window
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   #5 game loop

   while True:
      # check for events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
   
      screen.fill(000)
   
      #refresh screen with pygame.display.flip()
      pygame.display.flip()

   
# main is called at end to run code of def main() above
if __name__ == "__main__":
    main()

