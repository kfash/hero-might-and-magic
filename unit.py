from Units_and_hero import *
from magic import *

"""
Меняю способ задания юнитов, так как не понимаю, как работать со старым
"""
halberdist_dictionary =  {'name': '', 'attack': 0, 'defence': 0, 'damage': 0, 'rand': 0, 'hp': 0, 'speed': 0,
                          'image': 'ex.txt', 'x': 0, 'y': 0, 'num': 0, 'luck': 0, 'moral': 0, 'fraction': 'meme'}
crusader_dictionary =  {'name': '', 'attack': 0, 'defence': 0, 'damage': 0, 'rand': 0, 'hp': 0, 'speed': 0,
                        'image': 'ex.txt', 'x': 0, 'y': 0, 'num': 0, 'luck': 0, 'moral': 0, 'fraction': 'meme'}
archangel_dictionary = {'name': '', 'attack': 0, 'defence': 0, 'damage': 0, 'rand': 0, 'hp': 0, 'speed': 0,
                        'image': 'ex.txt', 'x': 0, 'y': 0, 'num': 0, 'luck': 0, 'moral': 0, 'fraction': 'meme'}
unit_list = {'halberdist': halberdist_dictionary, 'crusader': crusader_dictionary, 'archangel': archangel_dictionary}

# Fixme: ниже данную функцию можно улучшить
def fraction1_initialisation(unit_dictionary):
    for dictionary in unit_dictionary:
        with open('characteristics/units.txt') as input_file:
            for line in input_file:
                line_split = line.split()
                if len(line_split) == 0 or line[0] == '#':
                    continue  # пустые строки и строки-комментарии пропускаем
                elif dictionary == line_split[0]:
                    unit_dictionary[dictionary]['name'] = line_split[0]
                    unit_dictionary[dictionary]  ['attack'] = line_split[1]
                    unit_dictionary[dictionary]['defence'] = line_split[2]
                    unit_dictionary[dictionary]['damage'] = line_split[3]
                    unit_dictionary[dictionary]['rand'] = line_split[4]
                    unit_dictionary[dictionary]['hp'] = line_split[5]
                    unit_dictionary[dictionary]['speed'] = line_split[6]
                    unit_dictionary[dictionary]['image'] = line_split[7]
                    unit_dictionary[dictionary]['x'] = line_split[8]
                    unit_dictionary[dictionary]['y'] = line_split[9]
                    unit_dictionary[dictionary]['num'] = line_split[10]
                    unit_dictionary[dictionary]['luck'] = line_split[11]
                    unit_dictionary[dictionary]['moral'] = line_split[5]
                    unit_dictionary[dictionary]['fraction'] = line_split[5]
    return unit_dictionary

def halberdist(unit, hero, num, x, y, image):
    unit.atk = 6 + hero.atk
    unit.defe = 5 + hero.defe
    unit.damage = 2
    unit.rand = 1
    unit.hpta = 10 * num
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
    unit.defe = 3 + hero.defe
    unit.damage = 4
    unit.rand = 24
    unit.hpta = 10 * num
    unit.hpun = 10
    unit.speed = 6
    unit.shoot = 12
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def royal_griffin(unit, hero, num, x, y, image):
    unit.atk = 9 + hero.atk
    unit.defe = 9 + hero.defe
    unit.damage = 3
    unit.rand = 3
    unit.hpta = 25 * num
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
    unit.defe = 12 + hero.defe
    unit.damage = 7
    unit.rand = 3
    unit.hpta = 35 * num
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
    unit.defe = 10 + hero.defe
    unit.damage = 10
    unit.rand = 2
    unit.hpta = 30 * num
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
    unit.defe = 16 + hero.defe
    unit.damage = 20
    unit.rand = 5
    unit.hpta = 100 * num
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
    unit.defe = 30 + hero.defe
    unit.damage = 50
    unit.rand = 0
    unit.hpta = 250 * num
    unit.hpun = 250
    unit.speed = 18
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def master_gremlin(unit, hero, num, x, y, image):
    unit.atk = 4 + hero.atk
    unit.defe = 4 + hero.defe
    unit.damage = 1
    unit.rand = 1
    unit.hpta = 4 * num
    unit.hpun = 4
    unit.speed = 5
    unit.shoot = 8
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def obsidian_gargoyle(unit, hero, num, x, y, image):
    unit.atk = 7 + hero.atk
    unit.defe = 7 + hero.defe
    unit.damage = 2
    unit.rand = 1
    unit.hpta = 16 * num
    unit.hpun = 16
    unit.speed = 9
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def iron_golele(unit, hero, num, x, y, image):
    unit.atk = 9 + hero.atk
    unit.defe = 10 + hero.defe
    unit.damage = 4
    unit.rand = 1
    unit.hpta = 35 * num
    unit.hpun = 35
    unit.speed = 5
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def archmage(unit, hero, num, x, y, image):
    unit.atk = 12 + hero.atk
    unit.defe = 9 + hero.defe
    unit.damage = 7
    unit.rand = 2
    unit.hpta = 30 * num
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


def master_gin(unit, hero, num, x, y, image):
    unit.atk = 12 + hero.atk
    unit.defe = 12 + hero.defe
    unit.damage = 13
    unit.rand = 3
    unit.hpta = 40 * num
    unit.hpun = 40
    unit.speed = 11
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def queen_of_naga(unit, hero, num, x, y, image):
    unit.atk = 16 + hero.atk
    unit.defe = 21 + hero.defe
    unit.damage = 30
    unit.rand = 0
    unit.hpta = 110 * num
    unit.hpun = 110
    unit.speed = 7
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral


def titan(unit, hero, num, x, y, image):
    unit.atk = 24 + hero.atk
    unit.defe = 24 + hero.defe
    unit.damage = 50
    unit.rand = 20
    unit.hpta = 300 * num
    unit.hpun = 300
    unit.speed = 11
    unit.shoot = 24
    unit.id = image
    unit.x = x
    unit.y = y
    unit.init = unit.speed
    unit.num = num
    unit.luck = hero.luck
    unit.moral = hero.moral

#FIXME: wtf!?
# all_units = []
# unit_1 = unit()
# hero_1 = hero()
# halberdist(unit_1, hero_1, 1, 1, 4, None)
# all_units.append(unit_1)
