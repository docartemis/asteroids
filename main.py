#add pigmentize and rich to make debugging easier
from rich.traceback import install
install(show_locals=True)

#make print statements "fancier"
from rich import print as rprint

import pygame

from constants import *

#below is fancier version of original code
def main():
   rprint("[bold green]Starting Asteroids![/bold green]")
   rprint(f"Screen width: [cyan]{SCREEN_WIDTH}[/cyan]")
   rprint(f"Screen height: [cyan]{SCREEN_HEIGHT}[/cyan]")

if __name__ == "__main__":
    main()

