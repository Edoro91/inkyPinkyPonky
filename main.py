import pygame
import time
import random
import sys


pygame_icon = pygame.image.load('kkkk.jpeg')
pygame.display.set_icon(pygame_icon)

def ball_animation():
    global ball_speed_x, ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball.center = screen_width / 2, screen_height / 2
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.colliderect(player) or ball.colliderect(opponent_rect):
        ball_speed_x *= -1


def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    if opponent_rect.top <= ball.top:
        opponent_rect.top += opponent_speed
    if opponent_rect.bottom >= ball.bottom:
        opponent_rect.bottom -= opponent_speed



pygame.init()
screen_width = 1000
screen_height = 800
FPS = 60

window = pygame.display.set_mode((screen_width, screen_height))  # WIDTH , HEIGHT
pygame.display.set_caption("Inky pinky ponky daddy bought a donkey donkey die daddy cry")
clock = pygame.time.Clock()
bg_color = pygame.Color("black")

# figures colors
siptak = (255, 255, 255)

# pygame rects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
opponent_rect = pygame.Rect(10, screen_height / 2 - 70, 15, 140)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 15, 140)

ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

player_speed = 0
opponent_speed = 5



start_time = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 10
            if event.key == pygame.K_w:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 10
            if event.key == pygame.K_w:
                player_speed += 10
    window.fill(bg_color)
    pygame.draw.ellipse(window, siptak, ball)
    pygame.draw.rect(window, siptak, opponent_rect)
    pygame.draw.rect(window, siptak, player)
    pygame.draw.aaline(window, siptak, (screen_width / 2, 0), (screen_width / 2, screen_height))
    player.y += player_speed
    ball_animation()
    player_animation()
    opponent_animation()
    if time.time() - start_time >= 1:
        ball_speed_x += 10
        ball_speed_y += 10
        start_time += 1
        print("Speed change!", start_time)

    pygame.display.flip()
    clock.tick(FPS)
