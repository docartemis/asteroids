#stuff from player,py
import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
   def __init__(self, x, y, radius):   
      super().__init__(x, y, radius)  


   # Override the draw() method to draw the asteroid as a pygame.draw.circle.
   # Use its position, radius, and a width of 2  circle(surface, color, center, radius)
   def draw(self, screen):
      #note: this doesn't work>pygame.draw.circle(screen, (255,255,255),(x,y), radius, 2)
      pygame.draw.circle(screen, "white", self.position, self.radius, 2)

   # Override the update() method so that it moves in a straight line at constant speed. On each frame
   # add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
   
   def update(self, dt):
       self.position += self.velocity * dt


   #method to split astorids
   def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
