# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:30:03 2021

@author: F0064WK
"""

import pygame as pyg
from Chess import ChessEng

width = height = 512
dim = 8
sqsize = height // dim
Image = dict()
max_fps = 15

'''
Load piece images using this method
'''
def loadImages():
    pieces = ['Wp', 'WR', 'WN', 'WB', 'WQ', 'WK', 'Bp', 'BR', 'BN', 'BB', 'BQ', 'BK']
    for piece in pieces:
        Image[piece] = pyg.transform.scale(pyg.image.load("Chess/Images/" + piece +".png"), (sqsize, sqsize))
    return Image
   
'''
Main driver for the game      
'''
def main():
    pyg.init()
    playing = True #Play until done == True
    screen = pyg.display.set_mode((width, height))
    clock = pyg.time.Clock()
    screen.fill(pyg.Color("white"))
    gamestate = ChessEng.GameState()
    Image = loadImages()
    
    while playing:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                playing = False
        DrawGameState(screen, gamestate, Image)
        clock.tick(max_fps)
        pyg.display.flip()

def DrawGameState(screen, gamestate, Image):
    drawboard(screen)
    drawpieces(screen, gamestate.board, Image)

'''
Draw the 8x8 board
'''
def drawboard(screen):
    colors = [pyg.Color("white"), pyg.Color("grey")]
    for r in range(dim):
        for c in range(dim):
            color = colors[(r + c)%2]
            pyg.draw.rect(screen, color, pyg.Rect(c*sqsize, r*sqsize, sqsize, sqsize))
                
    
    
'''
Draw and place pieces on board given gamestate
'''
def drawpieces(screen, board, Image):
    for r in range(dim):
        for c in range(dim):
            piece = board[r][c]
            if piece != "--":
                screen.blit(Image[piece], pyg.Rect(c*sqsize, r*sqsize, sqsize, sqsize))



if __name__ == "__main__":
    main() 