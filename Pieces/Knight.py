from Piece import Piece


class Knight(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the knight can move to.
        """