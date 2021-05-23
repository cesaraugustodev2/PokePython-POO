# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:04:10 2021

@author: Cesar
"""


class Pokemon():
    def __init__(self, name: str, nature: str, lv: int, hp: int, atk: int, df: int, sp_atk: int, sp_df: int, spd: int, moves: []):
        self.name = name
        self.nature = nature
        self.lv = lv
        self.hp = hp
        self.atk = atk
        self.df = df
        self.sp_atk = sp_atk
        self.sp_df = sp_df
        self.spd = spd
        self.moves = moves
    def __repr__(self):
       return "Name: %s\nType: %s \nHP: %s \nlv: %s \nMoves:\n%s\n%s\n%s\n%s"%(self.name,self.nature,self.hp,self.lv,self.moves[0], self.moves[1], self.moves[2],  self.moves[3])

pikachu = Pokemon('Pikachu', 'Eletric', '1',25, 30, 15, 50, 25,50, ['Tackle', 'ThunderShock', 'Body Slam', 'Surf'])
print(pikachu)
