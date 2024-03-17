import pygame
import model

width = 1200
height = 800
window_caption = "Word Guesser"
FPS = 120
background = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(window_caption)
clock = pygame.time.Clock()
screen.fill(background)
pygame.display.update()

done = True

while done :
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      done = False
    elif i.type == pygame.KEYDOWN:
      if i.key == pygame.K_ESCAPE:
        done = False
  screen.fill(background)
  
  pygame.display.update()
  clock.tick(FPS)
pygame.quit()

