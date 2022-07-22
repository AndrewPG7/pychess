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
        self.board = [[p.Rook('b'), p.Knight('b'), p.Bishop('b'), p.Queen('b'), p.King('b'), p.Bishop('b'), p.Knight('b'), p.Rook('b')],
            [p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b'), p.Pawn('b')],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank(), p.Blank()],
            [p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w'), p.Pawn('w')],
            [p.Rook('w'), p.Knight('w'), p.Bishop('w'), p.Queen('w'), p.King('w'), p.Bishop('w'), p.Knight('w'), p.Rook('w')]]
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

    def move(self, orig, new):
        m.Movement(orig, new, self.board)
        print()
        self.draw_board()

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

clear()
print()
print('                -- Chess Prototype --')
print()
game = GameBoard()
ent = input('Input movement: ')
while ent != 'exit':
    mov = t.Translator()
    if mov.translate(ent):
        game.move(mov.orig, mov.new)
    ent = input('Input movement: ')
clear()
print('See you next time')
