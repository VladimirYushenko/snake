import pygame, constants, board, snake
import gameText
class PauseScreen:
    def __init__(self, gameBoard: board.Board, mainSnake: snake.Snake):
        self.text = gameText.GameText()
        self.gameBoard = gameBoard
        self.mainSnake = mainSnake


    def render(self, screen: pygame.Surface):
        self.gameBoard.render(screen)
        self.mainSnake.render(screen)
        self.text.drawText(screen, 'press any key', 100, 400)
        self.text.drawText(screen, 'to continue game', 40, 480)
        pygame.display.flip()
    
    def process(self) -> int:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            return constants.GAME_STATE_PLAY
        
        return constants.GAME_STATE_PAUSE