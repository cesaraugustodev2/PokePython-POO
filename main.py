# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:03:15 2021

@author: Cesar
"""
from Pokemon_class import Pokemon
#cria uma instancia de um pokemon
p = Pokemon('Pikachu', 'Eletric', 1, 25, 30, 15, 50, 25, 50, [['Tackle', 25, "Normal"], [
                  'Body Slam', 25, "Normal"], ['Thundershock', 50, "Eletric"], ['Water', 60, "Water"]])
#cria uma instancia de um pokemon
c = Pokemon('Charmander', 'Fire', 1, 35, 20, 10, 20, 15, 45, [['Tackle', 25, "Normal"], [
                  'Body Slam', 25, "Normal"], ['Ember', 50, "Fire"], ['Smokescreen ', 60, "Normal"]])

print(c.getname())
print(c.getlv())

c.damage(5)
c.attack(0)
c.attack(2)
c.level_up()
print("\n")
c.damage(5)
p.damage(5)
p.attack(0)
p.attack(2)
print("\n")
p.level_up()
c.damage(5)
c.attack(0)
c.attack(1)
c.damage(5)
print("\n")
c.attack(3)
c.attack(3)
c.level_up()
c.attack(3)
c.damage(5)
print("\n")
c.damage(5)
c.damage(5)
c.damage(20)
print(c.gethp())