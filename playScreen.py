import pygame, board, snake, constants, foodItems
import gameText
class PlayScreen:
    def __init__(self, gameBoard: board.Board, mainSnake: snake.Snake):
        self.text = gameText.GameText()
        self.black = 0, 0, 0
        self.gameBoard = gameBoard
        self.mainSnake = mainSnake
        self.loopCounter = 0
        #self.foodItem1 = foodItem.FoodItem(2, 1, gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT)
        #self.foodItem2 = foodItem.FoodItem(3, 6, gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT)
        self.foodItems = foodItems.FoodItems(gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT)
        self.foodItems.addFoodItem(2, 1)
        self.foodItems.addFoodItem(3, 6)

    def render(self, screen: pygame.Surface):
        screen.fill(self.black)

        self.gameBoard.render(screen)

        self.foodItems.render(screen)

        self.mainSnake.render(screen)

        pygame.display.flip()
    
    def process(self):
        self.loopCounter = self.loopCounter + 1
        if self.loopCounter == 10:
            self.loopCounter = 0
            self.mainSnake.moveSnake()
            if self.mainSnake.hasDied():
                self.mainSnake.initialize()
                return constants.GAME_STATE_SPLASH

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
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return constants.GAME_STATE_PAUSE
    
        return constants.GAME_STATE_PLAY