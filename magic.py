import tkinter as tk
from random import*
import time
import math

class effect():
	def __init__(self, char, amount):
		self.char=char
		self.amount=amount


	def applyEffect(self,unit):
		unit[self.char]+=self.amount
''''		if (self.char == 'atc'):
			unit.atc += self.amount
		if (self.char == 'defe'):
			unit.defe += self.amount
		if (self.char == 'damage'):
			unit.damage += self.amount
		if (self.char == 'rand'):
			unit.rand += self.amount
		if (self.char == 'hpta'):
			unit.hpta += self.amount
		if (self.char == 'hpun'):
			unit.hpun += self.amount
		if (self.char == 'speed'):
			unit.speed += self.amount
		if (self.char == 'x'):
			unit.x += self.amount
		if (self.char == 'y'):
			unit.y += self.amount
		if (self.char == 'init'):
			unit.init += self.amount
		if (self.char == 'num'):
			unit.num += self.amount
		if (self.char == 'sleep'):
			unit.sleep += self.amount'''


class magic():
	def __init__(self, school, image, cost):
		self.school = school
		self.image = image
		self.cost = cost
	
	def Cost(self, hero)
		hero.mana = hero.mana - cost

	def cast(self,unit):



class damagemagic(magic):
	def __init__ (self, damage, school, image, cost):
		magic.__init__ (self, school, image, cost)
		self.damage = damage

	def cast(self, unit):
		unit.hp = unit.hp - self.damage
		
		
class effectmagic(magic)
	def __init__ (self, effects, school, image, cost):
		magic.__init__ (self, school, image, cost)
		self.effects = effects


	def cast(self, unit):
		for eff in self.effects:
			unit.effect.append(eff)

