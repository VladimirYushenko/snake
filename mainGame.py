import snake, gameText, board, playScreen, splashScreen, pauseScreen, constants
import sys, pygame

pygame.init()

gameState = constants.GAME_STATE_SPLASH

gameBoard = board.Board(20, 20)
size = gameBoard.screenWidth, gameBoard.screenHeight
speed = [2, 2]

screen = pygame.display.set_mode(size)

mainSnake = snake.Snake(
    [[3, 4], [3, 3], [3, 2]], 
    snake.Snake.DOWN, 
    gameBoard.columns, 
    gameBoard.rows,
    board.Board.SQUARE_WIDTH,
    board.Board.SQUARE_HEIGHT)

play = playScreen.PlayScreen(gameBoard, mainSnake)
splash = splashScreen.SplashScreen(gameBoard)
pause = pauseScreen.PauseScreen(gameBoard, mainSnake)

loopCounter = 0

currentScreen = splash
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if gameState == constants.GAME_STATE_SPLASH:
        currentScreen = splash
    elif gameState == constants.GAME_STATE_PLAY:
        currentScreen = play
    elif gameState == constants.GAME_STATE_PAUSE:
        currentScreen = pause
    
    gameState = currentScreen.process()
    currentScreen.render(screen)