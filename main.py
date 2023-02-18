import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Hangman")


class Hangman():
    def __init__(self):
        self.running = True
        self.FPS = pygame.time.Clock()
        self.gallow_color = (0,0,0)
        self.body_color = (255,253,175)

    def gallow(self):
        stand = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(75, 280, 120, 10))
        body = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 10, 240))
        hanger = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 80, 10))
        rope = pygame.draw.rect(screen, self.gallow_color, pygame.Rect(205, 40,10, 30))

    def man_pieces(self):
        head = pygame.draw.circle(screen, self.body_color, [210, 85], 20, 0)
        body = pygame.draw.rect(screen, self.body_color, pygame.Rect(206, 105, 8, 45))
        r_arm = pygame.draw.line(screen, self.body_color, [183, 149], [200, 107], 6)
        l_arm = pygame.draw.line(screen, self.body_color, [231, 149], [218, 107], 6)
        r_leg = pygame.draw.line(screen, self.body_color, [189, 198], [208, 148], 6)
        l_leg = pygame.draw.line(screen, self.body_color, [224, 198], [210, 148], 6)


    def main(self):
        screen.fill((125, 0, 0))
        self.gallow()
        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                elif self.event.type == pygame.KEYDOWN:
                    self.man_pieces()

            pygame.display.update()
            self.FPS.tick(60)

        pygame.quit()

h = Hangman()
h.main()