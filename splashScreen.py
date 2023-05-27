import pygame, constants, board
import gameText
class SplashScreen:
    def __init__(self, gameBoard: board.Board):
        self.text = gameText.GameText()
        self.gameBoard = gameBoard

    def render(self, screen: pygame.Surface):
        self.gameBoard.render(screen)
        self.text.drawText(screen, 'snake', 320, 300)
        self.text.drawText(screen, 'press any key', 100, 400)
        self.text.drawText(screen, 'to start game', 100, 480)
        pygame.display.flip()
    
    def process(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            return constants.GAME_STATE_PLAY
        
        return constants.GAME_STATE_SPLASH