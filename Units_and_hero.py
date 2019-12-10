import random as rnd
import math

class unit:
    def __init__(self, unit_dictionary):
        self.name = unit_dictionary['name']
        self.atk = unit_dictionary['attack']  # атака
        self.defe = unit_dictionary['defence']  # защита
        self.damage = unit_dictionary['damage']  # минимальны урон
        self.rand = unit_dictionary['rand'] * 0  # разброс урона
        self.hpta = unit_dictionary['hp'] * unit_dictionary['num']  # хп стека
        self.hpun = unit_dictionary['hp']  # хп юнита
        self.speed = unit_dictionary['speed']  # скорость
        self.id = unit_dictionary['image']  # изображение
        self.x = unit_dictionary['x']  # положение по х в клетках
        self.y = unit_dictionary['y']  # положение по у в клетках
        self.v = 1  # скорость анимации движения
        self.init = self.speed  # инициатива
        self.num = unit_dictionary['num']  # количество юнитов в стеке
        self.effect = list()  # массив эффектов
        self.luck = unit_dictionary['luck']  # удача юнита
        self.moral = unit_dictionary['moral']  # мораль юнита
        self.sopr = 0
        self.hero = unit_dictionary['fraction']

# FIXME: эта функиция не должна рисовать ничего!!!!!!!!!
    def move(self, x, y):
        a = False
        if abs(self.x - x) + abs(self.y - y) < self.speed:
            for i in range(0, abs(x - self.x)):
                if x > self.x:
                    canv.move(self.id, 50, 0)

                else:
                    canv.move(self.id, -50, 0)
                a = True
            for i in range(0, abs(y - self.y)):
                if y > self.y:
                    canv.move(self.id, 0, 50)

                else:
                    canv.move(self.id, 0, -50)
                a = True
            self.x = x
            self.y = y
            return a

    def recount_num(self):
        a = (self.num) * self.hpun - self.hpta

        if a > 0:
            print(self.num, self.hpta, a, a // self.hpun)
            self.num = self.num - a // self.hpun

        if (a < - self.hpun):
            self.hpta = num * self.hpun

    def ApplyAllEffects(self):

        for eff in self.effect:
            eff.applyEffect(eff, self)

    def Defence(self):
        self.defence *= 1.3

    def Initiative(self):
        self.init *= 1.3

    def fight(self, obj):
        # elementaldamage = elementalmod()

        basedamage = self.damage + (rnd(0, 100 * self.rand, 1) / 100)

        if (self.atk > obj.defe):
            attackdefensemod = 1 + (self.atk - obj.defe) * 0.05

        else:
            attackdefensemod = 1 / (1 + (obj.defe - self.atk) * 0.05)

        phusicaldamage = math.trunc(self.num * basedamage * attackdefensemod)

        totaldamage = phusicaldamage  # + elementaldamage

        return totaldamage


class unitarcher(unit):
    def __init__(self, shoot=0, x=1, y=1, atk=0, defe=0, damage=0, rand=0, hp=0, speed=6, image=None, num=0, luck=0,
                 moral=0, hero=0):
        unit.__init__(self, x, y, atk, defe, damage, rand, hp, speed, image, num, luck, moral, hero)
        self.shoot = shoot

    def fight(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < 2:
            damage = unit.fight(self, obj) / 2
        else:
            damage = unit.fight(self, obj)

        obj.hpta -= damage
        obj.recount_num()


class meleeunit(unit):
    def __init__(self, x=1, y=1, atk=0, defe=0, damage=0, rand=0, hp=0, speed=6, image=None, num=0, luck=0, moral=0,
                 hero=0):
        unit.__init__(self, x, y, atk, defe, damage, rand, hp, speed, image, num, luck, moral, hero)

    def fight(self, obj):
        damage = unit.fight(self, obj)
        print("damage = ", damage)
        obj.hpta -= damage
        obj.recount_num()


class hero():
    def __init__(self, atk=0, defe=0, mageforce=0, knowlege=0, luck=0, moral=0, image=0, spell=0):
        self.atk = atk
        self.defe = defe
        self.mageforce = mageforce
        self.mana = knowlege * 10
        self.luck = luck
        self.moral = moral
        self.id = image
        self.spell = spell
