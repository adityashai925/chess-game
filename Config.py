import pygame
import os


class Config:
    def __init__(self):
        """
        Has attributes for window size etc. and methods which may be required by all other classes.
        """
        pygame.init()

        self.BLOCK_SIZE = 60

        self.WIDTH = self.BLOCK_SIZE * 8  + self.BLOCK_SIZE
        self.HEIGHT = self.BLOCK_SIZE * 8 + self.BLOCK_SIZE * 4

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chess")

        player_font_path = os.path.join("fonts", "MiliTech.otf")
        self.PLAYER_NAME_FONT_SIZE = 45
        self.player_name_font = pygame.font.Font(player_font_path, self.PLAYER_NAME_FONT_SIZE)

        self.PLAYER1_TEXT_POS = (self.BLOCK_SIZE // 2, self.BLOCK_SIZE // 5)
        self.PLAYER2_TEXT_POS = (self.BLOCK_SIZE // 2, self.HEIGHT - (self.BLOCK_SIZE // 5 + self.PLAYER_NAME_FONT_SIZE))

        self.COLOR1 = (241, 242, 233)
        self.COLOR2 = (47, 168, 146)

        self.BOARD_BOUNDARY_COLOR = (16, 48, 7)

        self.BG_COLOR = (191, 191, 191)

        self.BOUNDARY_THICKNESS = 7
        self.BOUNDARY_RECT = pygame.Rect(
            self.BLOCK_SIZE // 2 - self.BOUNDARY_THICKNESS,
            self.BLOCK_SIZE * 2 - self.BOUNDARY_THICKNESS,
            self.BLOCK_SIZE * 8 + 2 * self.BOUNDARY_THICKNESS,
            self.BLOCK_SIZE * 8 + 2 * self.BOUNDARY_THICKNESS
        )

        self.clock = pygame.time.Clock()
        self.FPS = 60