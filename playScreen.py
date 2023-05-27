import pygame, board, snake, constants
import gameText
class PlayScreen:
    def __init__(self, gameBoard: board.Board, mainSnake: snake.Snake):
        self.text = gameText.GameText()
        self.black = 0, 0, 0
        self.gameBoard = gameBoard
        self.mainSnake = mainSnake
        self.loopCounter = 0

    def render(self, screen: pygame.Surface):
        screen.fill(self.black)

        self.gameBoard.render(screen)

        self.mainSnake.render(screen)

        pygame.display.flip()
    
    def process(self):
        self.loopCounter = self.loopCounter + 1
        if self.loopCounter == 10:
            self.loopCounter = 0
            self.mainSnake.moveSnake()

        if pygame.key.get_pressed()[pygame.K_w]:
            self.mainSnake.changeDirection(snake.Snake.UP)
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.mainSnake.changeDirection(snake.Snake.DOWN)
        elif pygame.key.get_pressed()[pygame.K_a]:
            self.mainSnake.changeDirection(snake.Snake.LEFT)
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.mainSnake.changeDirection(snake.Snake.RIGHT)
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            self.mainSnake.setGrowNextMove()

        return constants.GAME_STATE_PLAY