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

def man_pieces(body_color=(255,253,175)):
    head = pygame.draw.circle(screen, body_color, [210, 85], 20, 0)
    body = pygame.draw.rect(screen, body_color, pygame.Rect(206, 105, 8, 45))
    r_arm = pygame.draw.line(screen, body_color, [183, 149], [200, 107], 6)
    l_arm = pygame.draw.line(screen, body_color, [231, 149], [218, 107], 6)
    r_leg = pygame.draw.line(screen, body_color, [189, 198], [208, 148], 6)
    l_leg = pygame.draw.line(screen, body_color, [224, 198], [210, 148], 6)

    pygame.display.update()

guessed_word = "Guessed word: b*st"
wrong_guesses = 'Wrong guesses: r, a, i'
enter_guess = "Enter guess: "

running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    gallow()
    man_pieces()

    font = pygame.font.SysFont("Arial", 25)

    text1 = font.render(guessed_word, True, (0,255,0))
    screen.blit(text1,(75,330))    
    text2 = font.render(wrong_guesses, True, (0,0,255))
    screen.blit(text2,(75,360))    
    text3 = font.render(enter_guess, True, (255,0,255))
    screen.blit(text3,(75,390))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
