import pygame
from model import Category, Word
from screens import ScreenShower

width = 1200
height = 800
window_caption = "Word Guesser"
FPS = 120
background = (154, 213, 252)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(window_caption)
clock = pygame.time.Clock()
screen.fill(background)
pygame.display.update()

my_screen = ScreenShower(pygame, screen, background)

my_screen.show_main_screen()

done = True

while done :
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      done = False
    elif i.type == pygame.KEYDOWN:
      if i.key == pygame.K_ESCAPE:
        done = False
  # screen.fill(background)
  pygame.display.update()
  clock.tick(FPS)
pygame.quit()

