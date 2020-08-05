#! -*- coding: utf-8 -*-

class Pawn(object):
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return ('♙','♟')[self.color]

print(Pawn(1))