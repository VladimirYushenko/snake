direction = 1
snake = [[3, 2], [3, 3], [3, 4]]

def moveSnake(snake, direction):
    if direction == 1:
        moveSnakeUp(snake)
    elif direction == 2:
        moveSnakeRight(snake)
    elif direction == 3:
        moveSnakeDown(snake)
    elif direction == 4:
        moveSnakeLeft(snake)
    
    return snake
    
def printSnake(snake):
    print('snake')
    for i in snake:
        print(i)

def moveSnakeUp(snake):
    newSnake = []
    newSnake.append([snake[0][0], snake[0][1] - 1])
    i = 0
    while i < len(snake) - 1:
        newSnake.append(snake[i])
        i = i + 1
    return newSnake

def moveSnakeRight(snake):
    newSnake = []
    newSnake.append([snake[0][0] + 1, snake[0][1]])
    i = 0
    while i < len(snake) - 1:
        newSnake.append(snake[i])
        i = i + 1
    return newSnake

def moveSnakeLeft(snake):
    newSnake = []
    newSnake.append([snake[0][0] - 1, snake[0][1]])
    i = 0
    while i < len(snake) - 1:
        newSnake.append(snake[i])
        i = i + 1
    return newSnake

def moveSnakeDown(snake):
    newSnake = []
    newSnake.append([snake[0][0], snake[0][1] + 1])
    i = 0
    while i < len(snake) - 1:
        newSnake.append(snake[i])
        i = i + 1
    return newSnake



printSnake(snake)

snakeUp = moveSnakeUp(snake)
snakeRight = moveSnakeRight(snake)
snakeLeft = moveSnakeLeft(snake)
snakeDown = moveSnakeDown(snakeLeft)


printSnake(snakeUp)
printSnake(snakeRight)
printSnake(snakeLeft)
printSnake(snakeDown)