import pygame
from random import *

#레벨에 맞게 설정
def setup(level):
    #몇개의 숫자를 보여줄 지 level에 따라서 결정
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) #최대 숫자는 20으로 세팅

    #실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

#숫자 섞기 @중요
#   [[0,0,0,0,0,0,0,0,0,]
#    [0,0,0,0,0,0,0,0,0,]
#    [0,0,0,0,0,0,0,0,0,]
#    [0,0,0,0,0,0,0,0,0,]
#    [0,0,0,0,0,0,0,0,0,]]
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 #각 grid cell의 가로 세로 크기
    button_size = 110 # 각 grid cell에 그려질 실제 버튼 크기(margin을 둠)
    screen_left_margin = 55 #스크린 왼쪽 여백
    screen_top_margin = 20 #스크린 위쪽 여백

    grid = [[0 for col in range(columns)] for row in range(rows)] #5 X 9 의 격자가 만들어짐
    #random으로 x,y 값을 설정한 후 0이면 숫자를 넣음

    number = 1 #시작 숫자를 1부터 number count까지 random하게 배치
    while number <= number_count:
        #x후보 0~8, y후보 0~4
        row_idx = randrange(0, rows) # 0~4 
        col_idx = randrange(0, columns) #0~8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            #현재 grid cell 위치 기준으로 x,y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            #숫자 버튼 그리기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            #버튼들을 새로운 리스트에 넣기
            number_buttons.append(button)


    print(grid)


#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #위치는 start button center, 반지름 60, 선두께 5

#게임 화면 보여주기
def display_game_screen():
    print("Game Start")
#pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True


# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0,0,0) #rgb값
WHITE = (255,255,255)

#플레이어가 눌러야 하는 버튼들(전역 변수로 사용하기 위해 선언)
number_buttons = []

#게임 시작 여부
start = False 

#게임 시작 전에 게임 설정 함수 수행
setup(1)

#게임 루프
running = True #게임 실행 중인지 판단
while running:
    click_pos = None

    #이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False

        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 마우스를 클릭
            click_pos = pygame.mouse.get_pos()
            
    #화면 background color 을 black
    screen.fill(BLACK)

    if start: 
        display_game_screen() #게임화면 표시

    else: 
        display_start_screen() #시작화면 표시


    #사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)
    #화면 업데이트
    pygame.display.update()

        
#게임 종료
pygame.quit()