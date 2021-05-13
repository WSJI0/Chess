import pygame

rook_mv=[[0, 1], [0, -1], [1, 0], [-1, 0]]
knight_mv=[[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

class Piece:
    def __init__(self, game, ptype, color, y, x):
        self.game=game
        self.ptype=ptype
        self.x=x
        self.y=y
        self.color=color

    def canMove(self):
        ret=[]
        if self.ptype==1:
            if self.y-1>=0:
                if self.game.board[self.y-1][self.x]==0:
                    ret.append([self.y-1, self.x, 0])
                if self.x-1>=0 and self.game.board[self.y-1][self.x-1]!=0:
                    ret.append([self.y-1, self.x-1, 1])
                if self.x+1<8 and self.game.board[self.y-1][self.x+1]!=0:
                    ret.append([self.y-1, self.x+1, 1])
        elif self.ptype==2:
            for i in range(4):
                rook_mv[i]

        return ret