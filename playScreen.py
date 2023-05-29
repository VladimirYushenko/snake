import pygame, board, snake, constants, foodItems, random
import gameText
class PlayScreen:
    def __init__(self, gameBoard: board.Board, mainSnake: snake.Snake):
        self.text = gameText.GameText()
        self.black = 0, 0, 0
        self.gameBoard = gameBoard
        self.mainSnake = mainSnake
        self.frameCounter = 0
        #self.foodItem1 = foodItem.FoodItem(2, 1, gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT)
        #self.foodItem2 = foodItem.FoodItem(3, 6, gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT)
        self.foodItems = foodItems.FoodItems(gameBoard.SQUARE_WIDTH, gameBoard.SQUARE_HEIGHT, gameBoard.columns, gameBoard.rows)
        self.foodItems.addFoodItem()
        self.foodItems.addFoodItem()

    def render(self, screen: pygame.Surface):
        screen.fill(self.black)

        self.gameBoard.render(screen)

        self.foodItems.render(screen)

        self.mainSnake.render(screen)

        pygame.display.flip()
    
    def process(self):
        self.frameCounter = self.frameCounter + 1
        if self.frameCounter == 10:
            self.frameCounter = 0
            # Try to add more food
            if random.random() < 0.015:
                self.foodItems.addFoodItem()

            # Move the snake
            self.mainSnake.moveSnake()

            # Check if snake died
            if self.mainSnake.hasDied():
                self.mainSnake.initialize()
                return constants.GAME_STATE_SPLASH
            
            # Check if food item was eaten
            if self.foodItems.eat(self.mainSnake.snake[0][0], self.mainSnake.snake[0][1]):
                self.mainSnake.setGrowNextMove()

        if pygame.key.get_pressed()[pygame.K_w]:
            self.mainSnake.changeDirection(snake.Snake.UP)
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.mainSnake.changeDirection(snake.Snake.DOWN)
        elif pygame.key.get_pressed()[pygame.K_a]:
            self.mainSnake.changeDirection(snake.Snake.LEFT)
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.mainSnake.changeDirection(snake.Snake.RIGHT)
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return constants.GAME_STATE_PAUSE
    
        return constants.GAME_STATE_PLAY