import snake
import sys, pygame

pygame.init()
 
size = width, height = 1276, 968
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/intro_ball.gif")
ballrect = ball.get_rect()

empty = pygame.image.load("assets/empty.png")
body = pygame.image.load("assets/body.png")
bodyrect = body.get_rect()

letterA = pygame.image.load("assets/letters/A.png")
DEFAULT_IMAGE_SIZE = (51, 51)
 
# Scale the image to your needed size
letterA = pygame.transform.scale(letterA, DEFAULT_IMAGE_SIZE)
letterArect = letterA.get_rect()

mainSnake = snake.Snake([[3, 4], [3, 3], [3, 2]], snake.Snake.DOWN, 28, 21)

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
    


    emptyrect = empty.get_rect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
   
    for y in range(22):
        for x in range(29):
            screen.blit(empty, emptyrect)
            emptyrect = emptyrect.move([44, 0])
        emptyrect = emptyrect.move([0, 44])
        emptyrect.left = 0

    for part in mainSnake.snake:
        bodyrect.left = 44 * part[0]
        bodyrect.top = 44 * part[1]
        screen.blit(body, bodyrect)

    screen.blit(ball, ballrect)
    screen.blit(letterA, letterArect)
    pygame.display.flip()