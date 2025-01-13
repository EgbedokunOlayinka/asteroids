import pygame

class Score(pygame.sprite.Sprite):
  def __init__(self, count):
    if hasattr(self, "containers"):
        super().__init__(self.containers)
    else:
        super().__init__()
    self.count = count

  def increment(self):
    self.count += 1
  
  def write(self, screen, font):
    score_text = font.render(f"SCORE: {self.count}", True, "black", "white")
    score_text_rect = score_text.get_rect()
    screen.blit(score_text, score_text_rect)
