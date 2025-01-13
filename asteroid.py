import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    #destroy asteroid
    self.kill()

    #if asteroid cannot be split into two
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    # split asteroid into two
    random_angle = random.uniform(20, 50)
    first_child_angle = self.velocity.rotate(random_angle)
    second_child_angle = self.velocity.rotate(-random_angle)

    new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
    first_child = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
    first_child.velocity = first_child_angle * 1.2
    second_child = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
    second_child.velocity = second_child_angle * 1.2

