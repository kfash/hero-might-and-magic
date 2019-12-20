from random import randrange as rnd
import math
from reInterface import*

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
                    Table.move(self.id, 50, 0)

                else:
                    Table.move(self.id, -50, 0)
                a = True
            for i in range(0, abs(y - self.y)):
                if y > self.y:
                    Table.move(self.id, 0, 50)

                else:
                    Table.move(self.id, 0, -50)
                a = True
            self.x = x
            self.y = y
            return a

    def recount_num(self):
        a = (self.num) * self.hpun - self.hpta

        if (a > 0):
            print(self.num, self.hpta, a, a // self.hpun)
            self.num = self.num - a // self.hpun

        if (a < - self.hpun):
            self.hpta =self.num * self.hpun

        if (self.num <= 0):
            Table.delete(self.id)

    def ApplyAllEffects(self):
        i = 0
        while(i < len(self.effect)):
            self.effect[i].applyEffect(self)
            if ( self.effect[i].duration == 0):
                self.effect.pop(i)
            i += 1


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
    def __init__(self, unit_dictionary):
        unit.__init__(self, unit_dictionary)
        self.shoot = unit_dictionary['shoot']

    def fight(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < 2:
            damage = unit.fight(self, obj) / 2
        else:
            damage = unit.fight(self, obj)

        obj.hpta -= damage
        obj.recount_num()


class meleeunit(unit):
    def __init__(self, unit_dictionary):
        unit.__init__(self, unit_dictionary)

    def fight(self, obj):
        damage = unit.fight(self, obj)
        print("damage = ", damage)
        obj.hpta -= damage
        obj.recount_num()


class hero():
    def __init__(self, atk=0, defe=0, mageforce=10, knowlege=10, luck=0, moral=0, image=0, spell=0):
        self.atk = atk
        self.defe = defe
        self.mageforce = mageforce
        self.mana = knowlege * 10
        self.luck = luck
        self.moral = moral
        self.id = image
        self.spell = spell
