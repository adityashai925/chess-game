from Piece import Piece


class Bishop(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the bishop can move to.
        """