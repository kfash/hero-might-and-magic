import tkinter as tk
from random import *
import time
import math

#эффект(баф или дебаф юнита)
class effect():
	def __init__(self, char, amount):
		self.char = char
		self.amount = amount

	def applyEffect(self, unit):
		exec("unit." + self.char + "+=" + self.amount)


class magic():
	def __init__(self, effects, school, image, cost):
		self.effects = effects
		self.school = school
		self.image = image
		self.cost = cost

#применение заклинания
	def cast(self, unit):
		for eff in self.effects:
			unit.effect.append(eff)

	def cost(self, hero):
		hero.mana = hero.mana - cost
