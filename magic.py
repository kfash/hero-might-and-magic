from spell import*

#эффект(баф или дебаф юнита)
class effect():
	def __init__(self, char, amount, duration):
		self.char = char
		self.amount = amount
		self.duration=duration

	def applyEffect(self, unit):
		exec("unit." + self.char + "+=" + self.amount)


class magic():
	def __init__(self, name, image, cost):
		self.name = name
		self.image = image
		self.cost = cost

#применение заклинания
	def cast(self, hero, unit):
		exec(self.name + "(unit, hero)")

