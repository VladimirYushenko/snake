import pygame
class Board:
    def __init__(self):
        self.emptyImage = pygame.image.load("assets/empty.png")
    
    def render(self, screen: pygame.Surface):
        for y in range(22):
            for x in range(29):
                screen.blit(self.emptyImage, (x * 44, y * 44))
