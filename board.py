import pygame
class Board:
    SQUARE_WIDTH = 44
    SQUARE_HEIGHT = 44
    DEFAULT_IMAGE_SIZE = (SQUARE_WIDTH, SQUARE_HEIGHT)

    def __init__(self, rows, columns):
        self.emptyImage = pygame.image.load("assets/empty.png")
        self.emptyImage = pygame.transform.scale(self.emptyImage, Board.DEFAULT_IMAGE_SIZE)
        self.rows = rows
        self.columns = columns
        self.screenWidth = Board.SQUARE_WIDTH * columns
        self.screenHeight = Board.SQUARE_HEIGHT * rows
    
    def render(self, screen: pygame.Surface):
        for y in range(self.rows):
            for x in range(self.columns):
                screen.blit(self.emptyImage, (x * Board.SQUARE_WIDTH, y * Board.SQUARE_HEIGHT))
