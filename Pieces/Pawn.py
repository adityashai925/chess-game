from Piece import Piece


class Pawn(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the pawn can move to.
        """