import pygame, foodItem, random
class FoodItems:

    def __init__(self, blockWidth, blockHeight, columns, rows):
        self.head = None
        self.blockWidth = blockWidth
        self.blockHeight = blockHeight
        self.columns = columns
        self.rows = rows

    def addFoodItem(self):
        foodCol = round(random.random() * self.columns)
        foodRow = round(random.random() * self.rows)
        newFoodItem = foodItem.FoodItem(foodCol, foodRow, self.blockWidth, self.blockHeight)
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
    
    # Detects and returns if snake touches any food item, and removes it 
    def eat(self, headCol, headRow):
        currentItem = self.head
        while currentItem != None:
            if headCol == currentItem.column and headRow == currentItem.row:
                self.removeItem(currentItem)
                return True
            currentItem = currentItem.next
        
        return False
    
    def removeItem(self, nodeToRemove: foodItem.FoodItem):
        if nodeToRemove == self.head:
            self.head = self.head.next
        else:
            currentItem = self.head
            while currentItem != None:
                if currentItem.next == nodeToRemove:
                    currentItem.next = nodeToRemove.next
                currentItem = currentItem.next

    
    def render(self, screen: pygame.Surface):
        currentItem = self.head
        while currentItem != None:
            currentItem.render(screen)
            currentItem = currentItem.next


