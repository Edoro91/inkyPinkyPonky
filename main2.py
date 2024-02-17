import random
import pygame
import time
import sys


def ball_animation():
    global ball_speed_x, ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball.center = screen_width / 2, screen_height / 2
        time.sleep(1)
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

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inky pinky ponki daddy bought a donkey daddy dye donkey cry")
clock = pygame.time.Clock()
bg_color = pygame.Color("black")

# Text settings
score_font = pygame.font.Font(None, 100)
score_color = (255, 255, 255)

# figures colors
siptak = (255, 255, 255)

# pygame rects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
opponent_rect = pygame.Rect(10, screen_height / 2 - 70, 15, 140)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 15, 140)

ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

player_speed = 0
opponent_speed = 1
start_time = time.time()
player_score = 0
opponent_score = 0

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

    # Check if the ball goes out of bounds
    if ball.left <= 0:
        player_score += 1
        print("Opponent scores!", opponent_score)
    elif ball.right >= screen_width:
        opponent_score += 1
        print("Player scores!", player_score)

    # Render scores
    player_text = score_font.render(str(player_score), True, score_color)
    opponent_text = score_font.render(str(opponent_score), True, score_color)
    window.blit(player_text, (screen_width - 100, 50))
    window.blit(opponent_text, (50, 50))

    pygame.display.flip()
    clock.tick(FPS)
