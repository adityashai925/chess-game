from Piece import Piece


class Queen(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the queen can move to.
        """