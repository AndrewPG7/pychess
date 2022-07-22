import pieces as p


class Movement:

    def __init__(self, orig, new, board):
        self.orig = orig
        self.new = new
        self.board = board
        self.old_pos = self.board[self.orig[0]][self.orig[1]]
        self.new_pos = self.board[self.new[0]][self.new[1]]
        self.move()

    def move(self):
        if self.block_move():
            if not isinstance(self.new_pos, p.Blank):
                self.capture()

            elif self.old_pos.valid_move(self.orig, self.new):
                self.board[self.new[0]][self.new[1]] = self.board[self.orig[0]][self.orig[1]]
                self.board[self.orig[0]][self.orig[1]] = p.Blank()
        else:
            print("Can't move")

    def block_move(self):
        if isinstance(self.old_pos, p.Pawn):
            return True
        elif isinstance(self.old_pos, p.Knight):
            return True
        elif isinstance(self.old_pos, p.Rook):
            return self.block_move_rook()
        elif isinstance(self.old_pos, p.Bishop):
            return self.block_move_bishop()
        elif isinstance(self.old_pos, p.Queen):
            if self.block_move_bishop():
                return True
            elif self.block_move_rook():
                return True
        elif isinstance(self.old_pos, p.King):
            return True
        else:
            return False

    def block_move_rook(self):
        if self.orig[1] < self.new[1]:
            for i in range(self.orig[1] + 1, self.new[1] - 1):
                if not isinstance(self.board[self.orig[0]][i], p.Blank):
                    return False
        elif self.orig[1] > self.new[1]:
            for i in range(self.new[1] + 1, self.orig[1] - 1):
                if not isinstance(self.board[self.orig[0]][i], p.Blank):
                    return False
        elif self.orig[0] < self.new[0]:
            for i in range(self.orig[0] + 1, self.new[0] - 1):
                if not isinstance(self.board[i][self.orig[1]], p.Blank):
                    return False
        elif self.orig[0] > self.new[0]:
            for i in range(self.new[0] + 1, self.orig[0] - 1):
                if not isinstance(self.board[i][self.orig[1]], p.Blank):
                    return False
        else:
            return False
        return True

    def block_move_bishop(self):
        if self.orig[0] < self.new[0] and self.orig[1] < self.new[1]:
            for i, j in [(self.orig[0] + 1, self.new[0] + 1), (self.orig[1] + 1, self.new[1] + 1)]:
                if not isinstance(self.board[i][j], p.Blank):
                    return False
        elif self.orig[0] < self.new[0] and self.orig[1] > self.new[1]:
            for i, j in [(self.orig[0] + 1, self.new[0] + 1), (self.orig[1] - 1, self.new[1] + 1, -1)]:
                if not isinstance(self.board[i][j], p.Blank):
                    return False
        elif self.orig[0] > self.new[0] and self.orig[1] < self.new[1]:
            for i, j in zip(range(self.orig[0] - 1, self.new[0] + 1, -1), range(self.orig[1] + 1, self.new[1] - 1)):
                if not isinstance(self.board[i][j], p.Blank):
                    return False
        elif self.orig[0] > self.new[0] and self.orig[1] > self.new[1]:
            for i, j in [(self.orig[0] - 1, self.new[0] + 1, -1), (self.orig[1] - 1, self.new[1] + 1, -1)]:
                if not isinstance(self.board[i][j], p.Blank):
                    return False
        else:
            return False
        return True

    def capture(self):
        if (self.old_pos.is_white() and not self.new_pos.is_white()) or (
                not self.old_pos.is_white() and self.new_pos.is_white()):
            if isinstance(self.old_pos, p.Pawn):
                self.pawn_capture()
            else:
                self.board[self.new[0]][self.new[1]] = self.board[self.orig[0]][self.orig[1]]
                self.board[self.orig[0]][self.orig[1]] = p.Blank()
        else:
            print("Can't capture your buddies!")

    def pawn_capture(self):
        if self.old_pos.capture_valid(self.orig, self.new):
            self.board[self.new[0]][self.new[1]] = self.board[self.orig[0]][self.orig[1]]
            self.board[self.orig[0]][self.orig[1]] = p.Blank()
        else:
            print("Pawn can't capture ahead!")
