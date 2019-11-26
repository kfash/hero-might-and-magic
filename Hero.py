import tkinter as tk
from random import*
from magic import *
import time
import math

root = tk.Tk()
canv = tk.Canvas(root)


class unit():
	def __init__(self, x, y, atc, defe, shot, damage, rand, hp, speed, image, num, effect,sleep):
		self.atc = atc
		self.defe = defe
		self.damage = damage
		self.rand = rand
		self.hpta = hp * num
		self.hpun = hp
		self.speed = speed
		self.id = image
		self.x = x
		self.y = y
		self.v = 1
		self.init = speed
		self.num = num
		self.effect = effect
		self.sleep = sleep
		
		
	def move(self, obj):
		r = ((self.x - obj.x)**2 + (self.y - obj.y)**2)
		vx = v*(self.x - obj.x)/r
		vy = v*(self.y - obj.y)/r
	
		while (r > 1):
			canv.move(self.id, vx, vy)
			self.x += vx 
			self.y += vy
			
	def recount_num(self):
		a = (num - 1)*self.hpun - self.hpta
		
		if (a > 0):
			num =num - a//self.hpun - (a - (a//self.hpun)*self.hpun)
			
		if (a < - self.hpun):
			self.hpta = num *self.hpun	
		
		
	def ApplyAllEffects(self):
		for eff in self.effect:
			eff.applyEffect(eff, self)

	def Defence(self):
		self.defe *= 1.3
	
	def Initiative(self):
		self.init *= 1.3
		
	def fight(self, obj):
		#elementaldamage = elementalmod()
		
		basedamage = self.damage + (rnd(100, 100*self.rand)/100)
		
		if (self.atk > obj.defe):
			attackdefensemod = 1 + (self.atk - obj.defe)*0.05
			
		else:
			attackdefensemod = 1/(1 + (obj.defe - self.atk)*0.05)
			
		if ((self.x - obj.x)**2 + (self.y - obj.y)**2 < 2):
			physicalmod = self.physmodb()
			
		else:
			physicalmod = self.physmodd()
		
		phusicaldamage = self.num * basedamage * attackdefensemod * physicalmod
		
		totaldamage = phusicaldamage #+ elementaldamage
		
		return totaldamage
		
					
class unitarcher(unit):
	def __init__ (self, shoot, x, y, atk, defe, shot, damage, rand, hp, speed, image, num, effect):
		unit.__init__ (self, x, y, atk, defe, shot, damage, rand, hp, speed, image, num, effect)
		self.shoot = shoot
			
	def fight(self, obj):
		if ((self.x - obj.x)**2 + (self.y - obj.y)**2 < 2):
			damage = unit.fight(self, obj)/2
		else:
			damage = unit.fight(self, obj)
			
		obj.hpta -= damage
		obj.recount_num()
		
		
class meleeunit(unit):
	def __init__(self, x, y, atk, defe, shot, damage, rand, hp, speed, image, num, effect):
		unit.__unit__(self, x, y, atk, defe, shot, damage, rand, hp, speed, image, num, effect)
	
	def fight(self, obj):
		damage = unit.fight(self, obj)
			
		odj.hpta -= damage
		obj.recount_num()		
				
					
					
class hero():
	def __init__(self, atc, defe, mageforce, knowlege, luck, moral, image, skill, spell):
		self.atc = atc
		self.defe = defe
		self.mageforce = mageforce
		self.mana = knowlege*10
		self.luck = luck
		self.moral = moral
		self.id = image
		self.skill = skill
		self.spell = spell
			
			
		#def cast (self, ):
			
		
