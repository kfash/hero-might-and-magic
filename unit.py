from Hero import *
from magic import *

all_units=[]
unit_1=unit(1, 4, 10, 3, 1, 10, 1, 100, 3, 1, 1, [],0)
all_units.append(unit_1)

def halberdist(unit, hero, num, x, y, image):
	unit.atk = 6 + hero.atk
	unit,defe = 5 + hero.defe
	unit.damage = 2
	unit.rand = 1
	unit.hpta = 10*num
	unit.hpun = 10
	unit.speed = 5
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def shooter(unit, hero, num, x, y, image):
	unit.atk = 6 + hero.atk
	unit,defe = 3 + hero.defe
	unit.damage = 4
	unit.rand = 24
	unit.hpta = 10*num
	unit.hpun = 10
	unit.speed = 6
	unit.shoot
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def royal_griffin(unit, hero, num, x, y, image):
	unit.atk = 9 + hero.atk
	unit,defe = 9 + hero.defe
	unit.damage = 3
	unit.rand = 3
	unit.hpta = 25*num
	unit.hpun = 25
	unit.speed = 9
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def crusader(unit, hero, num, x, y, image):
	unit.atk = 12 + hero.atk
	unit,defe = 12 + hero.defe
	unit.damage = 7
	unit.rand = 3
	unit.hpta = 35*num
	unit.hpun = 35
	unit.speed = 6
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def fanatic(unit, hero, num, x, y, image):
	unit.atk = 12 + hero.atk
	unit,defe = 10 + hero.defe
	unit.damage = 10
	unit.rand = 2
	unit.hpta = 30*num
	unit.hpun = 30
	unit.speed = 7
	unit.shoot = 24
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def champion(unit, hero, num, x, y, image):
	unit.atk = 16 + hero.atk
	unit,defe = 16 + hero.defe
	unit.damage = 20
	unit.rand = 5
	unit.hpta = 100*num
	unit.hpun = 100
	unit.speed = 9
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def champion(unit, hero, num, x, y, image):
	unit.atk = 16 + hero.atk
	unit,defe = 16 + hero.defe
	unit.damage = 20
	unit.rand = 5
	unit.hpta = 100*num
	unit.hpun = 100
	unit.speed = 9
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
	
def archangel(unit, hero, num, x, y, image):
	unit.atk = 30 + hero.atk
	unit,defe = 30 + hero.defe
	unit.damage = 50
	unit.rand = 0
	unit.hpta = 250*num
	unit.hpun = 250
	unit.speed = 18
	unit.id = image
	unit.x = x
	unit.y = y
	unit.init = unit.speed
	unit.num = num
	unit.luck = hero.luck
	unit.moral = hero.moral
