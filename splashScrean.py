import pygame
import gameText
class SplashScrean:
    def __init__(self):
        self.text = gameText.GameText()

    def render(self, screen: pygame.Surface):
        self.text.drawText(screen, 'snake', 510, 88)
        self.text.drawText(screen, 'press any key', 300, 220)
        self.text.drawText(screen, 'to start game', 300, 280)