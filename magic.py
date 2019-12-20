

#эффект(баф или дебаф юнита)
class effect():
	def __init__(self, char, amount, duration):
		self.char = char
		self.amount = amount
		self.duration=duration

	def applyEffect(self, obj):
		print(self.char)
		if (self.char == "atk"):
			obj.atk += self.amount
		if (self.char == "defe"):
			obj.defe += self.amount
		if (self.char == "damage"):
			obj.damage += self.amount
		if (self.char == "rand"):
			obj.rand += self.amount
		if (self.char == "speed"):
			obj.speed += self.amount
		if (self.char == "x"):
			obj.x += self.amount
		if (self.char == "y"):
			obj.y += self.amount
		if (self.char == "luck"):
			obj.luck += self.amount
		if (self.char == "moral"):
			obj.moral += self.amount
		self.duration-=1


class magic():
	def __init__(self, name):
		self.name = name


#применение заклинания
	def cast(self, hero, unit):
		exec(self.name + "(unit, hero)")

