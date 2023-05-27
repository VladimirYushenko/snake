import pygame, constants
import gameText
class PauseScreen:
    def __init__(self):
        self.text = gameText.GameText()
        self.black = 0, 0, 0

    def render(self, screen: pygame.Surface):
        screen.fill(self.black)
        self.text.drawText(screen, 'press any key', 100, 400)
        self.text.drawText(screen, 'to continue game', 40, 480)
        pygame.display.flip()
    
    def process(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            return constants.GAME_STATE_PLAY
        
        return constants.GAME_STATE_PAUSE