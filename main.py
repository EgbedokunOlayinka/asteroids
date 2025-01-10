import pygame
from constants import *
from player import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  player = Player(x, y)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    for item in updatable:
      item.update(dt)
    black = (0,0,0)
    pygame.Surface.fill(screen, black)
    for item in drawable:
      item.draw(screen)
    pygame.display.flip()
    delta_time = clock.tick(60)
    dt = delta_time / 1000 #convert milliseconds to seconds

if __name__ == "__main__":
  main()