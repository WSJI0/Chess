import pygame
from src.piece import Piece

color=["black", "white"]
piece=["", "pawn", "rook", "knight", "bishop", "queen", "king"]

class Game:
    def __init__(self, screen):
        self.screen=screen
        self.board=[[None for _ in range(8)] for _ in range(8)]
        self.turn=0
        self.black=0 # 0:Computer / 1:Human
        self.white=0 # 0:Computer / 1:Human
        self.delay=500 # Computer decision delay
        self.drawBoard()
    
    def newGame(self):
        board=self.board
        board[0][0]=Piece(self, 2, 0, 0, 0); board[0][1]=Piece(self, 3, 0, 0, 1); board[0][2]=Piece(self, 4, 0, 0, 2); board[0][3]=Piece(self, 5, 0, 0, 3)
        board[0][4]=Piece(self, 6, 0, 0, 4); board[0][5]=Piece(self, 4, 0, 0, 5); board[0][6]=Piece(self, 3, 0, 0, 6); board[0][7]=Piece(self, 2, 0, 0, 7)
        board[1][0]=Piece(self, 1, 0, 1, 0); board[1][1]=Piece(self, 1, 0, 1, 1); board[1][2]=Piece(self, 1, 0, 1, 2); board[1][3]=Piece(self, 1, 0, 1, 3)
        board[1][4]=Piece(self, 1, 0, 1, 4); board[1][5]=Piece(self, 1, 0, 1, 5); board[1][6]=Piece(self, 1, 0, 1, 6); board[1][7]=Piece(self, 1, 0, 1, 7)
        self.drawPiece()

    def drawBoard(self):
        self.screen.blit(pygame.image.load("img/background.png"), [0, 0])
        self.screen.blit(pygame.image.load("img/board.png"), [350, 0])
        pygame.display.flip()
    
    def drawPiece(self):
        for y in range(8):
            for x in range(8):
                if self.board[y][x]!=None:
                    self.screen.blit(pygame.image.load("img/"+piece[self.board[y][x].ptype]+"_"+color[self.board[y][x].color]+".png"), [400+x*100, 52+y*100])
        pygame.display.flip()

    def drawAll(self):
        self.drawBoard()
        self.drawPiece()

    def select(self, y, x):
        self.drawBoard()
        pygame.draw.rect(self.screen, (255, 255, 0), (400+x*100, 52+y*100, 100, 100))
        self.drawPiece()
    
    def play(self):
        crash=False
        clock=pygame.time.Clock()
        cur=0; sel=[0, 0]
        while not crash:
            clock.tick(120)
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    crash=True
                elif e.type==pygame.MOUSEBUTTONDOWN:
                    mx, my=e.pos
                    if mx>=400 and mx<=1200 and my>=50 and my<=850:
                        if cur==0:
                            self.select((my-55)//100, (mx-400)//100)
                            sel=[(my-55)//100, (mx-400)//100]
                        else:
                            self.move(sel[0], sel[1], (my-55)//100, (mx-400)//100)
                        cur^=1
                    
    def move(self, sy, sx, ey, ex):
        self.board[ey][ex]=self.board[sy][sx]
        self.board[sy][sx]=None
        self.drawAll()
        pygame.display.flip()

def startGame(screen):
    game=Game(screen)
    game.newGame()
    game.play()