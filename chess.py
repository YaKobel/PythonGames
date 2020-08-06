#! -*- coding: utf-8 -*-

class ChessMan(object):
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return ('♙','♟')[self.color]


class Pawn(ChessMan):
    IMG = ('♙', '♟')
    def __repr__(self):
        return ('♙','♟')[self.color]


class King(ChessMan):
    IMG = ('♔', '♚')

    def get_moves(self, board, x, y):
        moves = []
        return moves



class Board(object):
    def __init__(self):
        self.board = [['.'] * 8 for y in range(8)]
        self.board[1][2] = Pawn(1)

    def __repr__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res

print(Board())