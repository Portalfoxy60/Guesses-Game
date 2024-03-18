import pygame
import pygame_widgets
class ScreenShower:
    def __init__(self, pygame, screen, fill):
        self.screen = screen
        self.pygame = pygame
        self.fill = fill

    def show_main_screen(self):
        self.screen.fill(self.fill)
        title_font = pygame.font.SysFont("sans-serif", 120)
        title_text = title_font.render("Word Guesser", True,(0,0,0))
        self.screen.blit(title_text, (320, 100))
        start_button = pygame_widgets.Button(self.screen, 350, 400, 30, 40, "Start!")
        
        
        self.pygame.display.flip()

