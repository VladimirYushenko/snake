import pygame, board, snake
import gameText
class PlayScrean:
    def __init__(self, gameBoard: board.Board, mainSnake: snake.Snake):
        self.text = gameText.GameText()
        self.black = 0, 0, 0
        self.gameBoard = gameBoard
        self.mainSnake = mainSnake

    def render(self, screen: pygame.Surface):
        screen.fill(self.black)

        self.gameBoard.render(screen)

        self.mainSnake.render(screen)

        pygame.display.flip()