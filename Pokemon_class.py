# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:04:10 2021

@author: Cesar
"""
# classe pokemon


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

#serializar o Pokemon
    def __repr__(self):
       return "Name: %s\nType: %s \nHP: %s \nlv: %s \nMoves:\n%s" % (self.name, self.nature, self.hp, self.lv, self.moves)

    def getname(self):
        return self.name

    def getlv(self):
        return self.lv

    def getnature(self):
        return self.nature

    def setname(self, name):
        self.name = name

    def getlv(self):
        return self.lv
    def gethp(self):
        return self.hp

    def getnature(self):
        return self.nature
    #metodo para mostrar o movelist

    def show_moves(self):
       print(self.name + " Pode usar: \n")
       for m in self.moves:
          print(m[0] + "\nDamage: "+str(m[1])+"\n" + "Type: " + str(m[2])+"\n")
          #metodo para atacar n = movimento dentro do array
    def attack(self,n):
          print(self.name + " Atacou com "+str(self.moves[n][0])+" Causou "+str(self.moves[n][1])+" de dano")
     #metodo para atacar n = movimento dentro do array
    def damage(self,n):
        if self.hp>n:
           print(self.name + " sofreu  "+str(n)+" de dano")
           self.hp = self.hp-n
           print("HP restante: "+str(self.hp))
        else:
          print(self.name+" desmaiou")
          exit()
#metodo para subir de nivel
    def level_up(self):
        try:
            self.lv += 1
        except Exception as e:
            return print("Erro ao evoluir Pokemon: ", e)
        else:
            print("Parabéns! %s Subiu para o lv %d" % (self.name, self.lv))
#metodo para mostrar informações do pokemon
    def pokedex(self):
        print("Pokedex: ")
        print(self.name+" Tipo: "+self.nature + " Lv: "+str(self.lv)+"\n")
        print("Lista de Movimentos: ")
        for m in self.moves:
                print(m[0] + "\nDamage: "+str(m[1])+"\n" + "Type: " + str(m[2])+"\n")


