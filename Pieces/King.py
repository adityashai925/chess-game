from Piece import Piece


class King(Piece):
    def get_available_moves(self):
        """
        Returns a list of places the king can move to.
        """