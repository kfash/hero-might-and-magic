from Units_and_hero import *
from random import randrange as rnd


def magic_arrow(unit, hero):
	unit.hpat -= 20 + hero.magicforce * 10
	unit.recount_num
	
	hero.mana -= 5

def thirst_for_blood(unit, hero):
	ef=effect('atk', 6, hero.mageforce / 2)
	unit.effect.append(ef)

	hero.mana -= 5

# FIXME: ошибка в rand
def curse(unit, hero):
	ef = effect('rand', - rand, hero.mageforce/2)
	unit.effect.append(ef)
	
	hero.mana -= 6

def rabies(unit, hero):
	ef1 = effect('atk', 1, 5 * unit.defe, 1)
	ef2 = effect('defe', -unit.defe, 1)
	unit.effect.append(ef1)
	unit.effect.append(ef2)
	
	hero.mana -= 16
	
def failure(unit, hero):
	ef = effect('luck', -2, hero.mageforce / 2)
	unit.effect.append(ef)

	hero.mana -= 12
	
def blessing(unit, hero):
	ef1 = effect('rand', -unit.rand, hero.mageforce / 2)
	ef2 = effect('damage', unit.rand, hero.mageforce / 2)
	unit.effect.append(ef1)
	unit.effect.append(ef2)
	
	hero.mana -= 5
	
def treatment(unit, hero):
	unit.hpat += 20 + hero.magicforce * 5
	
	while unit.effect:
		unit.effect.pop(-1)
		
	hero.mana -= 6
	
def snaping(unit, hero):
	while unit.effect:
		unit.effect.pop(-1)
	
	hero.mana -= 5
	
def ice_arrow(unit, hero):
	unit.hpat -= 20 + hero.magicforce * 20
	unit.recount_num
	
	hero.mana -= 8
	
def weakness(unit, hero):
	ef = effect('atk', -6, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana -= 8
	
def joy(unit, hero):
	ef = effect('moral', 2, hero.mageforce / 2)
	unit.effect.append(ef)

	hero.mana -= 12
	
def teleport(unit, hero):
	unit.x = rnd(1, 12)
	unit.y = rnd(1, 12)

	hero.mana -= 10
	
def prayer(unit, hero):
	ef1 = effect('atk', 4, hero.mageforce / 2)
	ef2 = effect('defe', 4, hero.mageforce / 2)
	ef3 = effect('speed', 4, hero.mageforce / 2)
	unit.effect.append(ef1)
	unit.effect.append(ef2)
	unit.effect.append(ef3)

	hero.mana -= 16
	
def slowness(unit, hero):
	ef = effect('speed', -unit.speed/2, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana -= 6
	
def stone_skin(unit, hero):
	ef = effect('defe', 6, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana -= 5
	
def sadness(unit, hero):
	ef = effect('moral', -2, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana -= 4
	
def explosion(unit, hero):
	unit.hpat -= 200 + hero.magicforce * 75
	unit.recount_num
	
	hero.mana -= 30
	
def acceleration(unit, hero):
	ef = effect('speed', 5, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana -= 6
	
def destructive_beam(unit, hero):
	ef = effect('defe', -5, 9999)
	unit.effect.append(ef)
	
	hero.mana -= 10
	
def luck(unit, hero):
	ef = effect('luck', 2, hero.mageforce / 2)
	unit.effect.append(ef)
	
	hero.mana += 2
	
def lightning (unit, hero):
	unit.hpat -= 20 + hero.magicforce * 25
	unit.recount_num
	
	hero.mana -= 10
	
