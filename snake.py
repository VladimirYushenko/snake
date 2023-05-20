class Snake:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    # Direction:
    #   1 - up
    #   2 - right
    #   3 - down
    #   4 - left
    def __init__(self, snake, direction, maxX, maxY):
        self.snake = snake
        self.direction = direction
        self.maxX = maxX
        self.maxY = maxY
        self.growNextMove = False

    def setGrowNextMove(self):
        self.growNextMove = True

    def isAtTheEdge(self):
        if self.snake[0][0] == 0 and self.direction == Snake.LEFT:
            return True
        if self.snake[0][1] == 0 and self.direction == Snake.UP:
            return True
        if self.snake[0][0] == self.maxX and self.direction == Snake.RIGHT:
            return True
        if self.snake[0][1] == self.maxY and self.direction == Snake.DOWN:
            return True
        
        return False

    def moveSnake(self):
        if not self.isAtTheEdge():
            if self.direction == Snake.UP:
                self.__moveSnakeUp()
            elif self.direction == Snake.RIGHT:
                self.__moveSnakeRight()
            elif self.direction == Snake.DOWN:
                self.__moveSnakeDown()
            elif self.direction == Snake.LEFT:
                self.__moveSnakeLeft()
        
        return self.snake
    
    def changeDirection(self, newDirection):
        if self.direction == Snake.UP and newDirection != Snake.DOWN:
            self.direction = newDirection 
        elif self.direction == Snake.RIGHT and newDirection != Snake.LEFT:
            self.direction = newDirection
        elif self.direction == Snake.DOWN and newDirection != Snake.UP:
            self.direction = newDirection
        elif self.direction == Snake.LEFT and newDirection != Snake.RIGHT:
            self.direction = newDirection
        
        return self.direction

    def printSnake(self):
        print('snake')
        for i in self.snake:
            print(i)
    
    def __moveSnakeUp(self):
        newSnake = []
        newSnake.append([self.snake[0][0], self.snake[0][1] - 1])
        
        # decide weather to grow or move
        cellsToRemove = 1
        if self.growNextMove:
            cellsToRemove = 0
            self.growNextMove = False

        # move rest of snake
        i = 0
        while i < len(self.snake) - cellsToRemove:
            newSnake.append(self.snake[i])
            i = i + 1
        
        self.snake = newSnake

        return self.snake

    def __moveSnakeRight(self):
        newSnake = []
        # advance the head
        newSnake.append([self.snake[0][0] + 1, self.snake[0][1]])

        # decide weather to grow or move
        cellsToRemove = 1
        if self.growNextMove:
            cellsToRemove = 0
            self.growNextMove = False

        # move rest of snake
        i = 0
        while i < len(self.snake) - cellsToRemove:
            newSnake.append(self.snake[i])
            i = i + 1
        
        self.snake = newSnake

        return self.snake

    def __moveSnakeLeft(self):
        newSnake = []
        newSnake.append([self.snake[0][0] - 1, self.snake[0][1]])
        
        # decide weather to grow or move
        cellsToRemove = 1
        if self.growNextMove:
            cellsToRemove = 0
            self.growNextMove = False

        # move rest of snake
        i = 0
        while i < len(self.snake) - cellsToRemove:
            newSnake.append(self.snake[i])
            i = i + 1
        
        self.snake = newSnake

        return self.snake

    def __moveSnakeDown(self):
        newSnake = []
        newSnake.append([self.snake[0][0], self.snake[0][1] + 1])
        
        # decide weather to grow or move
        cellsToRemove = 1
        if self.growNextMove:
            cellsToRemove = 0
            self.growNextMove = False

        # move rest of snake
        i = 0
        while i < len(self.snake) - cellsToRemove:
            newSnake.append(self.snake[i])
            i = i + 1
        
        self.snake = newSnake

        return self.snake
    

