from Board import Board
from Config import Config


settings = Config()
GameBoard = Board(settings, "Player 1", "Player 2")

GameBoard.main()