import pygame
class GameText:
    def __init__(self):
        self.letter = pygame.image.load("assets/letters/A.png")
        DEFAULT_IMAGE_SIZE = (51, 51)
 
        # Scale the image to your needed size
        self.letter = pygame.transform.scale(self.letter, DEFAULT_IMAGE_SIZE)
        #letterArect = self.letter.get_rect()
    
    def drawText(self, screen, text, x, y):
        textList = []
        textList[:0] = text
        currentX = x
        for character in textList:
            if character == ' ':
                currentX = currentX + 51
            else:
                screen.blit(self.letter, (currentX, y))
                letterRect = self.letter.get_rect()
                currentX = currentX + letterRect.width