from Hero import *
from random import randrange as rnd
def magic_arrow(unit, hero):
	unit.hpat -= 20 + hero.magicforce*10
	unit.recount_num
	
	hero.mana -= 5

def thirst_for_blood(unit, hero):
	unit.effect.append(['atk', 6, hero.mageforce/2])
	unit.atk += 6
	
	hero.mana -= 5
	
def curse(unit, hero):
	unit.effect.append(['rand', -rand, hero.mageforce/2])
	unit.rand = 0
	
	hero.mana -= 6

def rabies(unit, hero):
	unit.effect.append(['atk', 1,5*unit.defe, 1])
	unit.effect.append(['defe', -unit.defe, 1])
	
	unit.atk += 1,5*unit.defe
	unit.defe = 0
	
	hero.mana -= 16
	
def failure(unit, hero):
	unit.effect.append(['luck', -2, hero.mageforce/2])
	
	unit.luck -= 2
	
	hero.mana -= 12
	
def blessing(unit, hero):
	unit.effect.append(['rand', -unit.rand, hero.mageforce/2])
	unit.effect.append(['damage', unit.rand, hero.mageforce/2])
	
	unit.damage += unit.rand
	unit.rand = 0
	
	hero.mana -= 5
	
def treatment(unit, hero):
	unit.hpat += 20 + hero.magicforce*5	
	
	while unit.effect:
		unit.effect.pop(-1)
		
	hero.mana -= 6
	
def snaping(unit, hero):
	while unit.effect:
		unit.effect.pop(-1)
	
	hero.mana -= 5
	
def ice_arrow(unit, hero):
	unit.hpat -= 20 + hero.magicforce*20
	unit.recount_num
	
	hero.mana -= 8
	
def weakness(unit, hero):
	unit.effect.append(['atk', -6, hero.mageforce/2])
	
	unit.atk -=6
	
	hero.mana -= 8
	
def joy(unit, hero):
	unit.effect.append(['moral', 2, hero.mageforce/2])
	
	unit.moral += 2
	
	hero.mana -= 12
	
def teleport(unit, hero):
	unit.x = rnd(1, 12)
	unit.y = rnd(1, 12)
	
	hero.mana -= 10
	
def prayer(unit, hero):
	unit.effect.append(['atk', 4, hero.mageforce/2])
	unit.effect.append(['defe', 4, hero.mageforce/2])
	unit.effect.append(['speed', 4, hero.mageforce/2])
	
	unit.atk += 4
	unit.defe += 4
	unit.speed += 4
	
	hero.mana -= 16
	
def slowness(unit, hero):
	unit.effect.append(['speed', unit.speed/2, hero.mageforce/2])
	
	unit.speed -= unit.speed/2
	
	hero.mana -= 6
	
def stone_skin(unit, hero):
	unit.effect.append(['defe', 6, hero.mageforce/2])
	
	unit.defe += 6
	
	hero.mana -= 5
	
def sadness(unit, hero):
	unit.effect.append(['moral', -2, hero.mageforce/2])
	
	unit.moral -= 2
	
	hero.mana -= 4
	
def explosion(unit, hero):
	unit.hpat -= 200 + hero.magicforce*75
	unit.recount_num
	
	hero.mana -= 30
	
def acceleration(unit, hero):
	unit.effect.append(['speed', 5, hero.mageforce/2])
	
	unit.speed += 5
	
	hero.mana -= 6
	
def destructive_beam(unit, hero):
	unit.effect.append(['defe', -5, 9999])
	
	unit.defe -= 5
	
	hero.mana -= 10
	
def luck(unit, hero):
	unit.effect.append(['luck', 2, hero.mageforce/2])
	
	unit.luck = 2
	
	hero.mana += 2
	
def lightning (unit, hero):
	unit.hpat -= 20 + hero.magicforce*25
	unit.recount_num
	
	hero.mana -= 10
	
