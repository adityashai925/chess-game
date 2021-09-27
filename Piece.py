import pygame
import os


class Piece:
    def __init__(self, color, config):
        """
        Has methods and attrs for all pieces.
        """
        self.settings = config

        self.COLOR = color

        path = os.path.join("images", "pieces", self.COLOR, f"{type(self).__name__.lower()}.png")
        IMAGE = pygame.image.load(path)
        self.IMAGE = pygame.transform.scale(IMAGE, (self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE))