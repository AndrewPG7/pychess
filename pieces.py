class Piece:

    def __init__(self, piece_color, symbol, name):
        self.piece_color = piece_color
        self.symbol = self.set_symbol(symbol)
        self.name = name

    def set_symbol(self, symbol):
        if self.piece_color == 'w':
            return symbol.upper()
        elif self.piece_color == 'b':
            return symbol.lower()
        else:
            return symbol

    def valid_move(self, old, new):
        pass

    def move(self, old, new):
        print('Moving', self.name, 'from', old[0], ',', old[1], 'to', new[0], ',', new[1])
        return True

    def cant_move(self):
        print('Invalid move operation')
        return False

    def is_white(self):
        if self.piece_color == 'w':
            return True
        elif self.piece_color == 'b':
            return False


class Blank(Piece):

    def __init__(self):
        self.piece_color = ''
        super().__init__(self.piece_color, ' ', 'blank')

    def valid_move(self, old, new):
        return super().cant_move()


class Pawn(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'P', 'pawn')
        self.first_valid_move = True

    def valid_move(self, old, new):
        if self.piece_color == 'b':
            if self.black_valid_move(old, new):
                return super().move(old, new)
        elif self.piece_color == 'w':
            if self.white_valid_move(old, new):
                return super().move(old, new)
        return super().cant_move()

    def black_valid_move(self, old, new):
        if self.first_valid_move and new[0] - old[0] == 2 and new[1] == old[1]:
            self.first_valid_move = False
            return True
        elif new[0] - old[0] == 1 and new[1] == old[1]:
            self.first_valid_move = False
            return True
        else:
            return False

    def white_valid_move(self, old, new):
        if self.first_valid_move and old[0] - new[0] == 2 and new[1] == old[1]:
            self.first_valid_move = False
            return True
        elif old[0] - new[0] == 1 and new[1] == old[1]:
            self.first_valid_move = False
            return True
        else:
            return False

    def capture_valid(self, old, new):
        if self.piece_color == 'b':
            if self.black_capture_valid_move(old, new):
                return super().move(old, new)
        elif self.piece_color == 'w':
            if self.white_capture_valid_move(old, new):
                return super().move(old, new)

    def black_capture_valid_move(self, old, new):
        if new[0] - old[0] == 1 and new[1] - old[1] == -1:
            self.first_valid_move = False
            return True
        elif new[0] - old[0] == 1 and new[1] - old[1] == 1:
            self.first_valid_move = False
            return True
        return False

    def white_capture_valid_move(self, old, new):
        if new[0] - old[0] == -1 and new[1] - old[1] == -1:
            self.first_valid_move = False
            return True
        elif new[0] - old[0] == -1 and new[1] - old[1] == 1:
            self.first_valid_move = False
            return True
        return False


class Rook(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'R', 'rook')

    def valid_move(self, old, new):
        if old[0] != new[0] and old[1] == new[1]:
            return super().move(old, new)
        elif old[0] == new[0] and old[1] != new[1]:
            return super().move(old, new)
        else:
            return super().cant_move()


class Knight(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'N', 'knight')

    def valid_move(self, old, new):
        if (abs(old[0] - new[0]) + abs(old[1] - new[1])) == 3:
            return super().move(old, new)
        else:
            return super().cant_move()


class Bishop(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'B', 'bishop')

    def valid_move(self, old, new):
        if abs(old[0] - new[0]) == abs(old[1] - new[1]):
            return super().move(old, new)
        else:
            return super().cant_move()


class Queen(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'Q', 'queen')

    def valid_move(self, old, new):
        if abs(old[0] - new[0]) == abs(old[1] - new[1]):
            return super().move(old, new)
        elif old[0] != new[0] and old[1] == new[1]:
            return super().move(old, new)
        elif old[0] == new[0] and old[1] != new[1]:
            return super().move(old, new)
        else:
            return super().cant_move()


class King(Piece):

    def __init__(self, piece_color):
        super().__init__(piece_color, 'K', 'king')

    def valid_move(self, old, new):
        if old[0] - new[0] == 1 and old[1] == new[1]:
            return super().move(old, new)
        elif new[0] - old[0] == 1 and old[1] == new[1]:
            return super().move(old, new)
        elif new[0] == old[0] and old[1] - new[1] == 1:
            return super().move(old, new)
        elif new[0] == old[0] and new[1] - old[1] == 1:
            return super().move(old, new)
        else:
            return super().cant_move()
