from Units_and_hero import *
from spell import *
from reInterface import *
from unit import *
import time

magici = 0
turni = 0
fght = 0
unit_dictionary = {'name': '', 'attack': 0, 'defence': 0, 'damage': 0, 'rand': 0, 'hp': 0, 'shoot': 0, 'speed': 0,
                   'image': 'ex.txt', 'x': 0, 'y': 0, 'num': 0, 'luck': 0, 'moral': 0, 'fraction': 'meme'}
unita = unit(unit_dictionary)
all_units = list()


def start():
    global hero_1
    global hero_2
    global units_1
    global units_2
    global all_units
    hero_1 = hero()
    hero_2 = hero()
    units_1 = []
    units_2 = []
    for i in range(1, 7):
        un = meleeunit(unit_dictionary)
        Texture = Table.create_image(2, 2 + i * 50, anchor=NW, image=crusader_left)
        # a = Table.create_oval(2 + 0 * 50, 2 + i * 50, 52 + 1 * 50, 52 + i * 50, fill="blue")
        halberdist(un, hero_1, 10, 1, i - 1, Texture)
        un.hero = 1
        units_1.append(un)
    for i in range(1, 7):
        un = unitarcher(unit_dictionary)
        a = Table.create_oval(2 + 11 * 50, 2 + i * 50, 52 + 11 * 50, 52 + i * 50, fill="green")
        shooter(un, hero_2, 10, 5, i - 1, a)
        un.hero = 2
        units_2.append(un)
    all_units = units_1 + units_2

    conket(units_1, units_2)
    round_update()


# FIXME: I must change the way battle initialize
def end_battle():
    pass


def clickl(event):
    global all_units
    global turni
    global fght
    global unita
    if (menu_layout.spell_book_window is not None) and (root.winfo_pointery() - root.winfo_rooty() < 605)\
            and (root.winfo_pointerx() - root.winfo_rootx() > 347) \
            and (root.winfo_pointerx() - root.winfo_rootx() < 952):
        n = 0
        magici = magicreturn()
        if (hero_1.mana == 0 and all_units[turni].hero == 1):
            magici = 0

        if (hero_2.mana == 0 and all_units[turni].hero == 2):
            magici = 0

        if (magici != 0):
            if (magici == 1):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                        if (un.hero == 1):
                            magic_arrow(un, hero_2)
                        if (un.hero == 2):
                            magic_arrow(un, hero_1)
                        magici = 0

            if (magici == 2):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                        if (un.hero == 1):
                            lightning(un, hero_2)
                        if (un.hero == 2):
                            lightning(un, hero_1)
                        magici = 0

            if (magici == 4):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                        if (un.hero == 1):
                            stone_skin(un, hero_1)
                        if (un.hero == 2):
                            stone_skin(un, hero_2)
                        magici = 0

            if (magici == 5):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                        if (un.hero == 1):
                            curse(un, hero_2)
                        if (un.hero == 2):
                            curse(un, hero_1)
                        magici = 0

            if (magici == 3):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                        if (un.hero == 1):
                            blessing(un, hero_1)
                        if (un.hero == 2):
                            blessing(un, hero_2)
                        magici = 0

        else:
            for un in all_units:
                if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                    n += 1
            if (fght == 0):
                for un in all_units:
                    if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y and all_units[turni].hero != un.hero):
                        for i in range(12):
                            for j in range(12):
                                Table.delete(field.cell_list[i][j].id)
                                field.cell_list[i][j].id = Table.create_rectangle(
                                    (2 + 50 * (field.cell_list[i][j].coordx)),
                                    (1 + 50 * (field.cell_list[i][j].coordy)),
                                    (2 + 50 * field.cell_list[i][j].coordx),
                                    (1 + 50 * field.cell_list[i][j].coordy),
                                    fill=field.cell_list[i][j].biom, outline="black")
                                round_update()

                                if (abs(all_units[turni].x - i) + abs(all_units[turni].y - j) < un.speed and abs(
                                        i - un.x) + abs(j - un.y) == 1):
                                    Table.delete(field.cell_list[i][j].id)
                                    field.cell_list[i][j].id = Table.create_rectangle(
                                        (2 + 50 * (field.cell_list[i][j].coordx)),
                                        (1 + 50 * (field.cell_list[i][j].coordy)),
                                        (2 + 50 * field.cell_list[i][j].coordx),
                                        (1 + 50 * field.cell_list[i][j].coordy),
                                        fill=field.cell_list[i][j].biom, outline="gold")
                                    round_update()
                                    fght = 1
                                    unita = un
                        if (type(all_units[turni]) == unitarcher and all_units[turni].shoot >= 0):
                            all_units[turni].fight(un)
                            all_units[turni].shoot -= 1
                            print("shoot = ",  all_units[turni].shoot)
                            turni += 1
                            fght = 0
                            if (turni == len(all_units)):
                                turni = 0
                                end_round()
                                available_move(all_units[turni])

                            round_update()


            else:
                print(abs(unita.x - math.trunc((event.x) / 50)), abs(unita.y - math.trunc((event.y) / 50)))

                if (abs(unita.x - math.trunc((event.x) / 50)) + abs(unita.y - math.trunc((event.y) / 50)) <= 1):

                    if (type(all_units[turni]) == meleeunit or (type(all_units[turni]) == unitarcher and all_units[turni].shoot < 0)):

                        a = all_units[turni].move(math.trunc((event.x - 100) / 50), math.trunc((event.y) / 50))
                        round_update()
                        if (a == True):
                            all_units[turni].fight(unita)
                            unita.fight(all_units[turni])
                            available_move(all_units[turni])
                            turni += 1
                            fght = 0
                            if (turni == len(all_units)):
                                turni = 0
                                end_round()
                                available_move(all_units[turni])
                            round_update()

            available_move(all_units[turni])
            round_update()

            for un in all_units:
                if (math.trunc((event.x) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
                    n += 1

            if (n == 0 and fght == 0):
                a = all_units[turni].move(math.trunc((event.x) / 50), math.trunc((event.y) / 50))
                round_update()
                if (a == True):
                    turni += 1
                    if (turni == len(all_units)):
                        turni = 0
                        end_round()
                    available_move(all_units[turni])
                    round_update()

        i = 0
        while (i < len(all_units)):
            if (all_units[i].num <= 0):
                Table.delete(all_units[i].id)
                all_units.pop(i)
                if (i <= turni and turni > 0):
                    turni -= 1
            i += 1


def clickr(event):
    global all_units
    for un in all_units:
        if (math.trunc(event.x / 50) == un.x and math.trunc(event.y / 50) == un.y)\
                and (root.winfo_pointery() - root.winfo_rooty() < 605) \
                and (root.winfo_pointerx() - root.winfo_rootx() > 347)\
                and (root.winfo_pointerx() - root.winfo_rootx() < 952)\
                and (menu_layout.spell_book_window is not None):
            print("atk = ", un.atk)
            print("defe = ", un.defe)
            print("damage = ", un.damage, " - ", un.damage + un.rand)
            print("hp = ", un.hpta - un.hpun * (un.num - 1))
            print("num = ", un.num)
            print("speed = ", un.speed)
            print("moral = ", un.moral)
            print("luck = ", un.luck)
            print("x = ", un.x)
            print("y = ", un.y)
            print("eff = ", un.effect)


def round_update():
    for un in all_units:
        print_unit(un)

def end_round():
    a = all_units[0].hero
    i = 0
    for un in all_units:
        un.ApplyAllEffects()
        if (a == un.hero):
            i += 1
    if (i == len(all_units)):
        end_battle()

start()
nen2 = Menu2_layout()
root.bind('<Button-3>', clickr)
root.bind('<Button-1>', clickl)

root.mainloop()
