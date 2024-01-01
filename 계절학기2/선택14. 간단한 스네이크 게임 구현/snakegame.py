import sys
import pygame
from pygame.locals import *
import random

pygame.init()

## 초당 프레임 단위 설정 ##
FPS = 20
FramePerSec = pygame.time.Clock()

## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

## 게임 창 설정 ##
GRID = 20
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
GRID_WIDTH = int(WINDOW_WIDTH/GRID)
GRID_HEIGHT = int(WINDOW_HEIGHT/GRID)
pygame.display.set_caption("Snake") # 창 이름 설정

NORTH = ( 0, -1)
SOUTH = ( 0,  1)
WEST  = (-1,  0)
EAST  = ( 1,  0)


class snake:
  def __init__(self):
    self.length = 1
    self.create_snake()
    self.color1 = GREEN
    self.head_color = GREEN

  def create_snake(self):
    self.length = 1
    self.positions = [(int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))]
    self.direction = random.choice([NORTH, SOUTH, WEST, EAST])
    global game_score
    game_score = 0

  def move_snake(self, surface):
    head = self.get_head_position()
    x, y = self.direction
    next = (head[0] + x * GRID, head[1] + y * GRID)  # 방향에 따라 이동할 위치 설정
    
    if next[0] < 0 or next[0] >= WINDOW_WIDTH or next[1] < 0 or next[1] >= WINDOW_HEIGHT:
        gameover(surface)  # 화면 밖으로 나갔을 때 게임 오버 처리
    
    if next in self.positions[1:]:
        gameover(surface)  # 자기 자신과 충돌했을 때 게임 오버 처리
    else:
        self.positions.insert(0, next)
        if len(self.positions) > self.length:
            del self.positions[-1]

  def draw_snake(self, surface):
    for index, pos in enumerate(self.positions):
      if index == 0:
          draw_object(surface, self.head_color, pos)
      elif index % 2 == 0:
          draw_object(surface, self.color1, pos)
      else:
          draw_object(surface, self.color1, pos)


  def game_control(self, arrowkey):
    if (arrowkey[0]*-1, arrowkey[1]*-1) == self.direction:
        return
    else:
        self.direction = arrowkey

  def get_head_position(self):
    return self.positions[0]
  
class Food:
  def __init__(self):
    self.position =(0, 0)
    self.color = RED
    self.randomize_food()

  def randomize_food(self):
    self.position = (random.randint(0, GRID_WIDTH-1) * GRID,
                       random.randint(0, GRID_HEIGHT-1) * GRID)
  def draw_food(self, surface):
    draw_object(surface, self.color, self.position)

def draw_food_group(food_group, surface):
    for food in food_group:
        food.draw_food(surface)

food_instance = Food()
food_group = []

for i in range(1):
    new_food = Food() 
    food_group.append(new_food)

for food in food_group:
    print(food.position)



def draw_background(surface):
  background = pygame.Rect((0,0),(WINDOW_WIDTH, WINDOW_HEIGHT))
  pygame.draw.rect(surface, WHITE, background)
  draw_grid(surface)

def draw_grid(surface):
  for row in range(0,int(GRID_HEIGHT)):
    for col in range(0, int(GRID_WIDTH)):
      rect = pygame.Rect((col * GRID, row * GRID), (GRID, GRID))
      pygame.draw.rect(surface, WHITE, rect)  # 사각형을 먼저 그립니다.
      pygame.draw.rect(surface, BLACK, rect, 1)  # 그리드 라인을 그립니다.

def draw_object(surface, color, pos):
    rect = pygame.Rect((pos[0], pos[1]), (GRID,GRID))
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, WHITE, rect, 1)


def position_check(snake, food_group):
    for food in food_group:
        if snake.get_head_position() == food.position:
            global game_score
            game_score += 1
            snake.length += 1
            food.randomize_food()

def restart_game():
    global player, game_score, food_group
    player = snake()
    game_score = 0
    food_group = [Food() for _ in range(1)]

def gameover(surface):
    font = pygame.font.SysFont('malgungothic', 50)
    image = font.render('GAME OVER', True, BLACK)
    text_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    surface.blit(image, text_rect)
    pygame.display.update()

    pygame.time.wait(2000)  # 게임 오버 메시지를 표시한 후 잠시 대기
    # pygame.quit()
    # sys.exit()
    restart_game()
player = snake()
run = True
game_score = 0

# ----- [ game loop ] -----

pygame.init()
pygame.display.set_caption('SNAKE GAME')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_UP:
                player.game_control(NORTH)
            if event.key == pygame.K_DOWN:
                player.game_control(SOUTH)
            if event.key == pygame.K_RIGHT:
                player.game_control(EAST)
            if event.key == pygame.K_LEFT:
                player.game_control(WEST)

    draw_background(screen)
    player.move_snake(screen)
    position_check(player, food_group)
    player.draw_snake(screen)
    draw_food_group(food_group, screen)
    speed = player.length/2
    pygame.display.flip()
    pygame.display.update()
    clock.tick(5+speed)

# ----- [ 파이게임 종료 ] -----

print('게임 오버입니다.')
pygame.quit()
sys.exit()