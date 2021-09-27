from Piece import Piece


class Rook(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the rook can move to.
        """