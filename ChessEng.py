# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:38:59 2021

@author: F0064WK
"""


class GameState(): 
    def __init__(self):
        self.board = [
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
            ["Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
            ]
        self.WhiteToMove = True
        self.movelog = []