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

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    b = 'ыыы'

if __name__ == "__main__":
    Funny_Student()
