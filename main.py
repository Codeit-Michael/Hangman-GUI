import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
screen.fill((125,0,0))
pygame.display.update()

def gallow(gallow_color=(0,0,0)):
    # gallow pieces
    stand = pygame.draw.rect(screen, gallow_color, pygame.Rect(75, 280, 120, 10))
    body = pygame.draw.rect(screen, gallow_color, pygame.Rect(128, 40, 10, 240))
    hanger = pygame.draw.rect(screen, gallow_color, pygame.Rect(128, 40, 80, 10))
    rope = pygame.draw.rect(screen, gallow_color, pygame.Rect(205, 40,10, 30))
    pygame.display.update()

# 190, 70

def man_piece(body_color=(255,253,175)):
    head = pygame.draw.circle(screen, body_color, [210, 85], 20, 0)

    body = pygame.draw.rect(screen, body_color, pygame.Rect(206, 105, 8, 50))

    shoulder = pygame.draw.rect(screen, body_color, pygame.Rect(195, 105, 30, 6))
    r_arm = pygame.draw.rect(screen, body_color, pygame.Rect(192, 109, 6, 35))
    l_arm = pygame.draw.rect(screen, body_color, pygame.Rect(222, 109, 6, 35))

    hips = pygame.draw.rect(screen, body_color, pygame.Rect(196, 155, 28, 6))
    r_leg = pygame.draw.rect(screen, body_color, pygame.Rect(196, 158, 6, 50))
    l_leg = pygame.draw.rect(screen, body_color, pygame.Rect(218, 158, 6, 50))
    pygame.display.update()

running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    gallow()
    man_piece()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
