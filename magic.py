import tkinter as tk
from random import*
import time
import math

class effect():
	def __init__(self, char, amount):
		self.char=char
		self.amount=amount


	def applyEffect(self,unit):
		exec("unit."+self.char+"+="+self.amount)


class magic():
	def __init__(self, school, image, cost):
		self.school = school
		self.image = image
		self.cost = cost
	
	def Cost(self, hero):
		hero.mana = hero.mana - cost

	def cast(self,unit):



class damagemagic(magic):
	def __init__ (self, damage, school, image, cost):
		magic.__init__ (self, school, image, cost)
		self.damage = damage

	def cast(self, unit):
		unit.hp = unit.hp - self.damage
		
		
class effectmagic(magic):
	def __init__ (self, effects, school, image, cost):
		magic.__init__ (self, school, image, cost)
		self.effects = effects

	def cast(self, unit):
		for eff in self.effects:
			unit.effect.append(eff)

