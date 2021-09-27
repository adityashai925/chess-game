import pygame
import json


class Board:
    def __init__(self, config):
        """
        Has methods for running the game.
        """
        self.settings = config

        self.LAYOUT_FILE_NAME = "board-layout.json"
        self.generate_board()

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
                rect = pygame.Rect(col_num * self.settings.BLOCK_SIZE, row_num * self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE)
                self.board[row_num][col_num]["rect"] = rect
                if col["color"] == "primary":
                    self.board[row_num][col_num]["color"] = self.settings.COLOR1
                elif col["color"] == "secondary":
                    self.board[row_num][col_num]["color"] = self.settings.COLOR2

    def draw_window(self):
        """
        Draws the window but does not update it.
        """
        self.settings.win.fill((255, 255, 255))

        for row in self.board:
            for box in row:
                pygame.draw.rect(self.settings.win, box["color"], box["rect"])

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