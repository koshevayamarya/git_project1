import os
import random
import pygame


class Student:
    def __init__(self):
        self.times = 0
        self.speed = 1
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Веселый школьник")
        self.clock = pygame.time.Clock()

        self.student_pos = [self.screen_width // 2, self.screen_height - 30]
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.directory = 'data'
        self.five_image = pygame.image.load(os.path.join(self.directory, 'five.png'))
        self.two_image = pygame.image.load(os.path.join(self.directory, 'two.png'))
        self.student_image = pygame.image.load(os.path.join(self.directory, 'hero.png'))

        self.student_size = self.student_image.get_size()
        self.two_size = self.two_image.get_size()

        self.two_pos = []
        self.five_pos = []

        self.run()

    def run(self):
        while True:
            self.times += 1
            if self.times % 200 == 0:
                self.speed += 1
                self.screen.fill((0 + self.times / 10, 0, 0))
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
                self.two_pos[i][1] += self.speed

            for i in range(len(self.five_pos)):
                self.five_pos[i][1] += self.speed

            if self.times % (100 // self.speed) == 0:
                x = random.randrange(0, (self.screen_width - self.two_size[0]), 1)
                num = random.randrange(0, 2)
                if num == 0:
                    self.two_pos.append([x, 0])
                else:
                    self.five_pos.append([x, 0])

            for position5 in self.five_pos:
                if (abs(position5[0] - self.student_pos[0]) <= self.student_size[0]) and (
                        abs(position5[1] - self.student_pos[1]) <= self.student_size[1]):
                    self.score += 1
                    self.five_pos.remove(position5)
                else:
                    if position5[1] >= self.screen_height:
                        self.five_pos.remove(position5)

            for position2 in self.two_pos:
                if (abs(position2[0] - self.student_pos[0]) <= self.student_size[0] / 2) and (
                        abs(position2[1] - self.student_pos[1]) <= self.student_size[1] / 2):
                    message_scr = self.font.render(f"конец игры! Вы получили {self.score} пятерок",
                                                   True,
                                                   (255, 0, 0))
                    self.screen.blit(message_scr,
                                     (self.screen_width // 2 - message_scr.get_width() // 2,
                                      self.screen_height // 2 - message_scr.get_height() // 2))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    pygame.quit()
                    exit()
                else:
                    if position2[1] >= self.screen_height:
                        self.two_pos.remove(position2)
            if self.times < 2550:
                self.screen.fill((0 + self.times / 10, 0, 0))
            else:
                self.screen.fill((0 + self.times / 10, 0, 0))

            for position5 in self.five_pos:
                self.screen.blit(self.five_image, (position5[0], position5[1]))
            for position2 in self.two_pos:
                self.screen.blit(self.two_image, (position2[0], position2[1]))

            self.screen.blit(self.student_image, (self.student_pos[0], self.student_pos[1]))

            score_scr = self.font.render(f"Ваш счёт: {self.score} пятерок",
                                         True,
                                         (255, 255, 255))
            self.screen.blit(score_scr, (10, 10))

            pygame.display.update()

            self.clock.tick(60)


if __name__ == "__main__":
    Student()
