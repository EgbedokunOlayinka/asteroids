import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)

  asteroid_field = AsteroidField()

  #start game loop
  while True:
    #handle game quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    #run update for classes in updatable group
    for drawable_item in updatable:
      drawable_item.update(dt)

    for asteroid in asteroids:
      #exit game when asteroid collides with player
      if asteroid.collide(player):
        print("Game over!")
        sys.exit()
      for shot in shots:
        #destroy asteroid and shot when they collide
        if asteroid.collide(shot):
          asteroid.split()
          shot.kill()
      

    black = (0,0,0)
    pygame.Surface.fill(screen, black)

    #run draw for all classes in drawable group
    for item in drawable:
      item.draw(screen)

    pygame.display.flip()

    #peg game to 60FPS
    delta_time = clock.tick(60)
    dt = delta_time / 1000 #convert milliseconds to seconds

if __name__ == "__main__":
  main()