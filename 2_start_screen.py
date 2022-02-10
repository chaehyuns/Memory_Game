import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #위치는 start button center, 반지름 60, 선두께 5
    

# 초기화
pygame.init()
screen_width = 1280 # 가로크기
screen_height = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색
BLACK = (0,0,0) #rgb값
WHITE = (255,255,255)


#게임 루프
running = True #게임 실행 중인지 판단
while running:
    #이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False
    
    #화면 background color 을 black
    screen.fill(BLACK)

    #시작화면 표시
    display_start_screen()

    #화면 업데이트
    pygame.display.update()

        
#게임 종료
pygame.quit()