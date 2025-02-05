from random import random

import pygame


class Funny_Student():
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Веселый школьник")
        self.clock = pygame.time.Clock()

        self.student_pos = [self.screen_width // 2, self.screen_height - 30]
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)

        self.five_image = pygame.image.load("five.png")
        self.two_image = pygame.image.load("two.png")
        self.student_image = pygame.image.load("student.png")

        self.student_size = self.student_image.get_size()
        self.two_size = self.two_image.get_size()

        self.two_pos = []
        self.five_pos = []

        self.run()
        self.times = 0

    def run(self):
        while True:
            self.times += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.student_pos[0] >= 20:
                            self.student_pos[0] -= 20
                    elif event.key == pygame.K_RIGHT:
                        if self.student_pos[0] + 20 + self.student_size[0] <= self.screen_width:
                            self.student_pos[0] += 20
                    elif event.key == pygame.K_UP:
                        if self.student_pos[1] >= 20:
                            self.student_pos[1] -= 20
                    elif event.key == pygame.K_DOWN:
                        if self.student_pos[1] + 20 + self.student_size[1] <= self.screen_height:
                            self.student_pos[1] += 20

            for i in range(len(self.two_pos)):
                self.two_pos[i][1] += 3

            for i in range(len(self.five_pos_pos)):
                self.five_pos[i][1] += 3

            if self.times % 10 == 0:
                x = random.randint(0, self.screen_width - self.two_size[0])
                num = random.randint(0, 1)
                if num == 0:
                    self.two_pos.append([x, 0])
                else:
                    self.five_pos.append([x, 0])



if __name__ == "__main__":
    Funny_Student()
