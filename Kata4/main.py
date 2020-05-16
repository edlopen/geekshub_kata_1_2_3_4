import pygame, random

screen_width = 1280
screen_height = 960

# Colors
back_color = pygame.Color('grey12')
white_color = pygame.Color('white')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

def move_rectangle():
    global speed
    if rectangle.top + rectangle.height < screen_height:
        rectangle.top += speed

speed_ball_x = 7
speed_ball_y = 7

def start_ball():
    global speed_ball_x, speed_ball_y
    ball.top = screen_height // 2
    ball.left = screen_width // 2

    speed_ball_x = random.choice((1, -1)) * 3
    speed_ball_y = random.choice((1, -1)) * 3

def move_ball():
    global speed_ball_x, speed_ball_y
    # rebote abajo
    if ball.top + ball.height > screen_height:
        speed_ball_x = - speed_ball_x
    # rebote top
    elif ball.top < 0:
        speed_ball_x = - speed_ball_x
    # se sale por la derecha, reinicio
    elif ball.left + ball.width > screen_width:
        start_ball()
    # se sale por la izquierda, reinicio
    #elif ball.left + ball.width < screen_width:
    #    start_ball()

    if ball.left < 10 and rectangle.top < ball.top and rectangle.top + 140:
        speed_ball_y = -speed_ball_y

    ball.top += speed_ball_x
    ball.left += speed_ball_y

rectangle = pygame.Rect(10, 10, 10, 140)
ball = pygame.Rect(50, 10, 50, 50)

speed = 0

while True:
    # color de fondo
    screen.fill(back_color)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -5
            elif event.key == pygame.K_DOWN:
                speed = 5
        elif event.type == pygame.KEYUP:
            speed = 0

    move_rectangle()
    move_ball()
    pygame.draw.rect(screen, white_color, rectangle)
    pygame.draw.rect(screen, white_color, ball)
    # calcula los gráficos
    pygame.display.flip()
    # calcula el tiempo entre ticks para que se calcula n veces
    clock.tick(60)
