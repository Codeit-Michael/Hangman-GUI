import pygame
from pygame.locals import *
import os
import random
from string import ascii_letters

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Hangman")


class Hangman():
    def __init__(self):
        with open("./words.txt", "r") as file:
            words = file.read().split("\n")
            self.secret_word = random.choice(words)
            self.guessed_word = "*" * len(self.secret_word)
        self.wrong_guesses = []
        self.wrong_guess_count = 0
        self.taking_guess = True
        self.running = True

        self.FPS = pygame.time.Clock()
        self.gallow_color = (0,0,0)
        self.body_color = (255,253,175)
        self.font = pygame.font.SysFont("Arial", 20)

    def _gallow(self):
        stand = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(75, 280, 120, 10))
        body = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 10, 240))
        hanger = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 80, 10))
        rope = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(205, 40,10, 30))

    def _man_pieces(self):
        if self.wrong_guess_count == 1:
            pygame.draw.circle(screen, self.body_color, [210, 85], 20, 0)
        elif self.wrong_guess_count == 2:
            pygame.draw.rect(screen, self.body_color, pygame.Rect(206, 105, 8, 45))
        elif self.wrong_guess_count == 3:
            pygame.draw.line(screen, self.body_color, [183, 149], [200, 107], 6)
        elif self.wrong_guess_count == 4:
            pygame.draw.line(screen, self.body_color, [231, 149], [218, 107], 6),
        elif self.wrong_guess_count == 5:
            pygame.draw.line(screen, self.body_color, [189, 198], [208, 148], 6),
        elif self.wrong_guess_count == 6:
            pygame.draw.line(screen, self.body_color, [224, 198], [210, 148], 6)

    def _right_guess(self, guess_letter):
        index_positions = [index for index, item in enumerate(self.secret_word) if item == guess_letter]
        for i in index_positions:
            self.guessed_word = self.guessed_word[0:i] + guess_letter + self.guessed_word[i+1:]

    def _wrong_guess(self, guess_letter):
        self.wrong_guesses.append(guess_letter)
        self.wrong_guess_count += 1
        self._man_pieces()
        if self.wrong_guess_count == 6:
            self.taking_guess = False
            print('you lose')

    def _guess_taker(self, guess_letter):
        if guess_letter in ascii_letters:
            if guess_letter in self.secret_word and guess_letter not in self.guessed_word:
                self._right_guess(guess_letter)
            elif guess_letter not in self.secret_word and guess_letter not in self.wrong_guesses:
                self._wrong_guess(guess_letter)
        else:
            print("Invalid input")

    def main(self):
        screen.fill((155, 120, 70))
        self._gallow()
        instructions = self.font.render('Press any key to take Guess', True, (9,255,78))
        screen.blit(instructions,(70,460))
        print(self.secret_word)

        while self.running:
            guessed_word = self.font.render(f"guessed word: {self.guessed_word}", True, (0,0,138))
            screen.blit(guessed_word,(80,350))
            wrong_guess = self.font.render(f"wrong_guesses: {self.wrong_guesses}", True, (178,0,0))
            screen.blit(wrong_guess,(80,400))
        
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                elif self.event.type == pygame.KEYDOWN:
                    if self.taking_guess:
                        self._guess_taker(self.event.unicode)
            pygame.display.flip()
            self.FPS.tick(60)

        pygame.quit()

h = Hangman()
h.main()
