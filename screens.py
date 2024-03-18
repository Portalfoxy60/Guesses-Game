import pygame
from pygame_widgets.button import Button
from model import Player
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

class ScreenShower:
    button_massive = []

    engine = create_engine("sqlite:///wordsBase.sqlite", echo=True)
    session = Session(engine)
    def __init__(self, pygame, screen, fill):
        self.screen = screen
        self.pygame = pygame
        self.fill = fill

    def show_main_screen(self):
        self.screen.fill(self.fill)
        title_font = pygame.font.SysFont("sans-serif", 120)
        title_text = title_font.render("Word Guesser", True,(0,0,0))
        self.screen.blit(title_text, (320, 100))
        
        start_button = Button(self.screen, 350, 400, 100, 40, text="Start!", textColour=(0,0,0), fontSize=40)
        start_button.draw()
        self.button_massive.append(start_button)

        score_button = Button(self.screen, 350, 500, 100, 40, text="Scores", textColour=(0,0,0), fontSize=40, onClick=lambda:self.all_scores_screen())
        score_button.draw()
        self.button_massive.append(score_button)

        volume_button = Button(self.screen, 100, 700, 100, 100, image=pygame.image.load('sound.png'), colour=(154, 213, 252))
        volume_button.draw()
        self.button_massive.append(volume_button)


        self.pygame.display.flip()


    def all_scores_screen(self):
        self.screen.fill(self.fill)
        title_font = pygame.font.SysFont("sans-serif", 120)
        title_text = title_font.render("SCORE TABLE", True,(0,0,0))
        self.screen.blit(title_text, (320, 100))

        stmt = select(Player).order_by(Player.scores).limit(10).offset(1)
        for a in self.session.scalars(stmt):
            text = pygame.font.SysFont("sans-serif", 80)
            score_table = text.render("Rank\tName\tScores", True, (0,0,0))
            self.screen.blit(score_table, (320, 250))
            rank = a.id
            name = a.name
            scores = a.scores
            table = pygame.font.SysFont("sans-serif", 60)
            column_rows=table.render(f"{rank}\t{name}\t{scores}", True, (0,0,0))
            self.screen.blit(column_rows, (320, 300+a.id*40))

        
        for button in self.button_massive:
            button.hide()


        volume_button = Button(self.screen, 100, 700, 100, 100, image=pygame.image.load('sound.png'), colour=(154, 213, 252))
        volume_button.draw()
        self.button_massive.append(volume_button)

        self.pygame.display.flip()
