
import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
   def __init__(self, x, y):
      super().__init__(x, y, PLAYER_RADIUS)
      self.rotation = 0
      self.shoot_timer = 0
      #player containers- moved to main.py


   # in the player class
   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

   
   def draw(self, screen):
      # sub-classes must override
      # take the screen object as a parameter, and call pygame.draw.polygon. 
      # polygon(surface, color, points, width=0) note rgb for white is 255X3
      pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

   #create method called rotate that takes one argument: dt. 
   #When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current 
   def rotate(self, dt):
      self.rotation = self.rotation + PLAYER_TURN_SPEED * dt
      #use rotation instead of rotate to avoid overwriting rotate

   #create method update
   def update(self, dt):
      self.shoot_timer -= dt
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
          self.rotate(-dt)
      if keys[pygame.K_d]:
          self.rotate(dt)
   #call move() when W or S are pressed
      if keys[pygame.K_w]:
          self.move(dt) 
      if keys[pygame.K_s]:
          self.move(-dt)
      if keys[pygame.K_SPACE]:
            self.shoot() 

   # create method called .move(). It takes one argument: dt
   # start with a unit vector pointing straight up from (0, 0) to (0, 1).
   # rotate that vector by the player's rotation to point in the direction the player is facing.
   # multiply by PLAYER_SPEED * dt. Add the vector to our position to move the player.
   
   def move(self, dt):   
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

   # create method .shoot(). It should:
   #Create a new shot at the position of the player
   #Set the shot's velocity: Start with a pygame.Vector2 of (0, 1) 
   #.rotate() it in the direction the player is facing
   #Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster
   
   def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED   
