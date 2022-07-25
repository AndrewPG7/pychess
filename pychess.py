from os import system, name
import pieces as p
import movement as m
import translator as t


class GameBoard:

    def __init__(self):

        self.rows = 8
        self.row_nums = (8, 7, 6, 5, 4, 3, 2, 1)
        self.columns = 8
        self.columns_let = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        self.board = [
            [p.Rook('b'), p.Knight('b'), p.Bishop('b'), p.Queen('b'), p.King('b'), p.Bishop('b'), p.Knight('b'),
             p.Rook('b')],
            [p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b')],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w')],
            [p.Rook('w'), p.Knight('w'), p.Bishop('w'), p.Queen('w'), p.King('w'), p.Bishop('w'), p.Knight('w'),
             p.Rook('w')]]
        self.draw_board()

    def set_board(self):
        # function to set board and not use that ugly thing up there
        pass

    def draw_board(self):
        clear()
        print()
        for i in range(self.rows):
            print('          ---------------------------------')
            for j in range(self.columns):
                if j == 0:
                    print('         ', '|', end=' ')
                print(self.board[i][j].symbol, end=' | ')
                if j == 7:
                    print('', self.row_nums[i])

        print('          ---------------------------------')
        # print()
        print('            ', end='')
        for i in self.columns_let:
            print(i, end='   ')
        print()
        print()

    def move(self, w_turn, orig, new):
        if (w_turn and self.board[orig[0]][orig[1]].is_white()) or \
                (not w_turn and not self.board[orig[0]][orig[1]].is_white()):
            m.Movement(orig, new, self.board)
            print()
            self.draw_board()
            return True
        else:
            return False

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
print()
print('                -- Chess Prototype --')
print()
player_w = input('Whites player name: ')
player_b = input('Blacks player name: ')
player_w_turn = True
game = GameBoard()
ent = ''
while ent != 'exit':
    ent = input('Input movement: ')
    mov = t.Translator()
    if mov.translate(ent):
        if game.move(player_w_turn, mov.orig, mov.new):
            player_w_turn = not player_w_turn
        else:
            print('Move your pieces')
clear()
print('See you next time')
