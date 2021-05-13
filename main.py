import pygame
from src.game import startGame
import os

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS']='%i, %i'%(0, 0)
os.environ['SDL_VIDEO_CENTERED']='0'
screen=pygame.display.set_mode([1600, 900])

def main():
    startGame(screen)

if __name__=="__main__":
    main()