import pygame, sys, random


def ball_animation():
  global ballSpeedX, ballSpeedY, opponentScore, playerScore, scoreTime

  ball.x += ballSpeedX
  ball.y += ballSpeedY

  if ball.top <= 0 or ball.bottom >= screenHeight:
    ballSpeedY *= -1

  # opponent score
  if ball.left<= 0:
    opponentScore += 1
    scoreTime = pygame.time.get_ticks()

  # player score
  if ball.right >= screenWidth:
    playerScore += 1
    scoreTime = pygame.time.get_ticks()

  if ball.colliderect(player) and ballSpeedX > 0:
    if abs(ball.right - player.left) < 10:
      ballSpeedX *= -1
    elif abs(ball.bottom - player.top) < 10 or abs(ball.top - player.bottom) < 10:
      ballSpeedY *= -1


  if ball.colliderect(opponent):
    if abs(ball.right - player.left) < 10:
      ballSpeedX *= -1
    else:
      ballSpeedY *= -1

def player_animation():
  player.y += playerSpeed

  if player.top <= 0:
    player.top = 0
  if player.bottom >= screenHeight:
    player.bottom = screenHeight


def opponent_ai():
  if opponent.top < ball.y:
    opponent.top += opponentSpeed
  if opponent.bottom > ball.y:
    opponent.bottom -= opponentSpeed

  if opponent.top <= 0:
    opponent.top = 0
  if opponent.bottom >= screenHeight:
    opponent.bottom = screenHeight


def ball_reset():
  global ballSpeedX, ballSpeedY, ballMoving, scoreTime
  ball.center = (screenWidth/2, screenHeight/2)
  currentTime = pygame.time.get_ticks()

  if currentTime - scoreTime < 700:
    numberThree = gameFont.render('3', False, lightGrey)
    screen.blit(numberThree, (screenWidth/2 - 10, screenHeight/2 + 20))
  if 700 < currentTime - scoreTime < 1400:
    numberTwo = gameFont.render('2', False, lightGrey)
    screen.blit(numberTwo, (screenWidth/2 - 10, screenHeight/2 + 20))
  if 1400 < currentTime - scoreTime < 2100:
    numberOne = gameFont.render('1', False, lightGrey)
    screen.blit(numberOne, (screenWidth/2 - 10, screenHeight/2 + 20))



# general setup
pygame.init()
clock = pygame.time.Clock()


# setting up the main window
screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')


# game rectangles
ball = pygame.Rect(screenWidth/2 - 15, screenHeight/2 - 15 ,30, 30)
player = pygame.Rect(10, screenHeight/2 - 70, 10, 140)
opponent = pygame.Rect(screenWidth - 20, screenHeight/2 - 70, 10, 140)

bgColour = pygame.Color('grey12')
lightGrey = (200, 200, 200)

ballSpeedX = 7 * random.choice((1,-1))
ballSpeedY = 7 * random.choice((1,-1))
playerSpeed = 0
opponentSpeed = 7
ballMoving = False
scoreTime = None


# score text
playerScore = 0
opponentScore = 0
gameFont = pygame.font.Font("freesansbold.ttf", 32)


while True:
  # handling input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        playerSpeed += 7
      if event.key == pygame.K_UP:
        playerSpeed -= 7
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        playerSpeed -= 7
      if event.key == pygame.K_UP:
        playerSpeed += 7


  ball_animation()
  player_animation()
  opponent_ai()


  # visuals
  screen.fill(bgColour)
  pygame.draw.rect(screen, lightGrey, player)
  pygame.draw.rect(screen, lightGrey, opponent)
  pygame.draw.ellipse(screen, lightGrey, ball)
  pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0), (screenWidth/2, screenHeight))

  if scoreTime:
    ball_reset()

  playerText = gameFont.render(f'{playerScore}', False, lightGrey)
  screen.blit(playerText, (604, 470))

  opponentText = gameFont.render(f'{opponentScore}', False, lightGrey)
  screen.blit(opponentText, (660, 470))


  # updating the window
  pygame.display.flip()
  clock.tick(60)