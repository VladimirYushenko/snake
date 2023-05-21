import pygame
import string
class GameText:
    def __init__(self):
        self.lettersDict = {}

        DEFAULT_IMAGE_SIZE = (51, 51)
        for letter in string.ascii_uppercase:
            letterImage = pygame.image.load("assets/letters/" + letter + ".png")
            letterImage = pygame.transform.scale(letterImage, DEFAULT_IMAGE_SIZE)
            self.lettersDict[letter] = letterImage
    
    def drawText(self, screen: pygame.Surface, text: str, x, y):
        textList = []
        textList[:0] = text.upper()
        currentX = x
        for character in textList:
            if character == ' ':
                currentX = currentX + 51
            else:
                letterImage = self.lettersDict[character]
                screen.blit(letterImage, (currentX, y))
                letterRect = letterImage.get_rect()
                currentX = currentX + letterRect.width