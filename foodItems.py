import pygame, foodItem
class FoodItems:

    def __init__(self, blockWidth, blockHeight):
        self.head = None
        self.blockWidth = blockWidth
        self.blockHeight = blockHeight

    def addFoodItem(self, column, row):
        newFoodItem = foodItem.FoodItem(column, row, self.blockWidth, self.blockHeight)
        if self.head == None:
            self.head = newFoodItem
        else:
            lastItem = self.findLastItem()
            lastItem.next = newFoodItem
    
    def findLastItem(self):
        if self.head == None:
            return None
        
        currentItem = self.head
        while currentItem.next != None:
            currentItem = currentItem.next
        
        return currentItem
    
    def render(self, screen: pygame.Surface):
        currentItem = self.head
        while currentItem != None:
            currentItem.render(screen)
            currentItem = currentItem.next


