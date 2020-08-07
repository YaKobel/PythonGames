#! -*- coding: utf-8 -*-

class Color(object):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

class Empty(object):
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception('Error !')

    def __repr__(self):
        return '.'

class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]


class Pawn(ChessMan):
    IMG = ('♙', '♟')

    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y+1) == Color.EMPTY:
            moves.append([x,y])
        return moves

class King(ChessMan):
    IMG = ('♔', '♚')

    def get_moves(self, board, x, y):
        moves = []
        return moves



class Board(object):
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        self.board[1][2] = Pawn(Color.BLACK)
        self.board[0][3] = King(Color.BLACK)
        self.board[7][3] = King(Color.WHITE)

    def get_moves(self, board, x, y):
        self.board[y][x].get_moves(self, x, y)

    def __repr__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res

print(Board())