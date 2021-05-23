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
       return "Name: %s\nType: %s \nHP: %s \nlv: %s \nMoves:\n%s" % (self.name, self.nature, self.hp, self.lv, self.moves)

    def show_moves(self):
       print(self.name + " Knows: \n")
       for m in pikachu.moves:
          print(m[0] + "\nDamage: "+str(m[1])+"\n" +"Type: " + str(m[2])+"\n" )


pikachu = Pokemon('Pikachu', 'Eletric', '1', 25, 30, 15, 50, 25, 50, [['Tackle',25, "Normal"], ['Body Slam',25, "Normal"], ['Thundershock',50, "Eletric"],['Water',60, "Water"]])
pikachu.show_moves()
