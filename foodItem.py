import pygame
class FoodItem:
    def __init__(self, column, row, blockWidth, blockHeight):
        self.foodImage = pygame.image.load("assets/MushroomB.png")
        self.foodImage = pygame.transform.scale(self.foodImage, (blockWidth, blockHeight))
        self.column = column
        self.row = row
        self.bWidth = blockWidth
        self.bHeight = blockHeight
        self.next = None
        

    def render(self, screen: pygame.Surface):
        screen.blit(self.foodImage, (self.column * self.bWidth, self.row * self.bHeight))