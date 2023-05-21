import snake, gameText, board, playScreen
import sys, pygame

pygame.init()
 
size = width, height = 1276, 968
speed = [2, 2]

screen = pygame.display.set_mode(size)

mainSnake = snake.Snake([[3, 4], [3, 3], [3, 2]], snake.Snake.DOWN, 28, 21)
gameBoard = board.Board()

play = playScreen.PlayScrean(gameBoard, mainSnake)

loopCounter = 0

while True:
    loopCounter = loopCounter + 1
    if loopCounter == 10:
        loopCounter = 0
        mainSnake.moveSnake()

    if pygame.key.get_pressed()[pygame.K_w]:
        mainSnake.changeDirection(snake.Snake.UP)
    elif pygame.key.get_pressed()[pygame.K_s]:
        mainSnake.changeDirection(snake.Snake.DOWN)
    elif pygame.key.get_pressed()[pygame.K_a]:
        mainSnake.changeDirection(snake.Snake.LEFT)
    elif pygame.key.get_pressed()[pygame.K_d]:
        mainSnake.changeDirection(snake.Snake.RIGHT)
    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        mainSnake.setGrowNextMove()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    play.render(screen)