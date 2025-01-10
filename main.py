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
  player = Player(x, y)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    black = (0,0,0)
    pygame.Surface.fill(screen, black)
    player.draw(screen)
    pygame.display.flip()
    delta_time = clock.tick(60)
    dt = delta_time / 1000 #convert milliseconds to seconds
    player.update(dt)

if __name__ == "__main__":
  main()