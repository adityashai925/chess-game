import pygame
import json

from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Queen import Queen


class Board:
    def __init__(self, config):
        """
        Has methods for running the game.
        """
        self.settings = config

        self.LAYOUT_FILE_NAME = "board-layout.json"
        self.generate_board()

        self.surface = pygame.Surface((self.settings.BLOCK_SIZE * 8, self.settings.BLOCK_SIZE * 8))

        self.running = True

    def generate_board(self):
        """
        Reads the layout from file and makes a 2d list with object of piece class and has rect for
        each box.
        """
        with open(self.LAYOUT_FILE_NAME, "r") as layout_file:
            self.board = json.load(layout_file)

        for row_num, row in enumerate(self.board):
            for col_num, col in enumerate(row):
                rect = pygame.Rect(
                    col_num * self.settings.BLOCK_SIZE,
                    row_num * self.settings.BLOCK_SIZE,
                    self.settings.BLOCK_SIZE,
                    self.settings.BLOCK_SIZE
                )
                self.board[row_num][col_num]["rect"] = rect

                if col["box-color"] == "primary":
                    self.board[row_num][col_num]["box-color"] = self.settings.COLOR1
                elif col["box-color"] == "secondary":
                    self.board[row_num][col_num]["box-color"] = self.settings.COLOR2

                if col["piece"]:
                    if col["piece"] == "pawn":
                        self.board[row_num][col_num]["piece"] = Pawn(col["piece-color"], self.settings)
                    elif col["piece"] == "rook":
                        self.board[row_num][col_num]["piece"] = Rook(col["piece-color"], self.settings)
                    elif col["piece"] == "knight":
                        self.board[row_num][col_num]["piece"] = Knight(col["piece-color"], self.settings)
                    elif col["piece"] == "bishop":
                        self.board[row_num][col_num]["piece"] = Bishop(col["piece-color"], self.settings)
                    elif col["piece"] == "king":
                        self.board[row_num][col_num]["piece"] = King(col["piece-color"], self.settings)
                    elif col["piece"] == "queen":
                        self.board[row_num][col_num]["piece"] = Queen(col["piece-color"], self.settings)

                    del self.board[row_num][col_num]["piece-color"]

    def draw_window(self):
        """
        Draws the window but does not update it.
        """
        self.settings.win.fill(self.settings.BG_COLOR)
        pygame.draw.rect(self.settings.win, self.settings.BOARD_BOUNDARY_COLOR, self.settings.BOUNDARY_RECT)

        for row in self.board:
            for box in row:
                pygame.draw.rect(self.surface, box["box-color"], box["rect"])

                if box["piece"]:
                    self.surface.blit(box["piece"].IMAGE, box["rect"])

        self.settings.win.blit(self.surface, (self.settings.BLOCK_SIZE // 2, self.settings.BLOCK_SIZE * 1.5))

    def event_loop(self):
        """
        Checks the events happening and calls the necessary methods.
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def main(self):
        """
        Main game loop.
        """
        while self.running:
            self.event_loop()

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)