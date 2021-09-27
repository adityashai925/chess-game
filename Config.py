import pygame


class Config:
    def __init__(self):
        """
        Has attributes for window size etc. and methods which may be required by all other classes.
        """
        pygame.init()

        self.BLOCK_SIZE = 90

        self.WIDTH = self.BLOCK_SIZE * 8
        self.HEIGHT = self.BLOCK_SIZE * 8

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chess")

        self.COLOR1 = (255, 255, 255)
        self.COLOR2 = (152, 78, 222)

        self.clock = pygame.time.Clock()
        self.FPS = 60