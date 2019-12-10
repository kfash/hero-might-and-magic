from tkinter import *
from PIL import Image, ImageTk
import math
import BattleField as BF
from Units_and_hero import *
from unit import *
from magic import *


# FIXME: написать функцию, которая отображает передвижение юнита


root = Tk()
root.wm_title("Final Fantasy XVI")
root.attributes("-fullscreen", True)

"""
Инициализация различных областей программы:
1) Menu - область с кнопками управления
2) Menu2 - область с игровой информацией о юните или участке поля, книга заклинаний
3) Table - поле сражения
4) support - линия инициативы(может не появиться)
"""
Menu = Canvas(root, width=300, height=600, bg='green')
Menu.pack(side=LEFT)
Menu2 = Canvas(root, width=300, height=600, bg='green')
Menu2.pack(side=RIGHT)
Table = Canvas(root, width=601, height=601, bg='white')
Table.pack(side=TOP)
support = Canvas(root, width=601, height=100, bg='blue')
support.pack(side=BOTTOM)

"""
Графические улучшение интерфейса(background)
Может возникнуть проблема с тем, что background выше, чем объекты, тогда стоит написать
cancas.delet(background)
"""
Menu_background_img = ImageTk.PhotoImage(Image.open("images/menu_background.jpg"))
Menu_background = Label(root, image=Menu_background_img)
Menu_background.pack()
Menu.create_window(0, 0, anchor=NW, window=Menu_background)

Menu2_background_img = ImageTk.PhotoImage(Image.open("images/menu_background.jpg"))
Menu2_background = Label(root, image=Menu2_background_img)
Menu2_background.pack()
Menu2.create_window(0, 0, anchor=NW, window=Menu2_background)

Table_background_img = ImageTk.PhotoImage(Image.open("images/Table_background.jpg"))
Table_background = Label(root, image=Table_background_img)
Table_background.pack()
Table_window = Table.create_window(0, 0, anchor=NW, window=Table_background)

support_background_img = ImageTk.PhotoImage(Image.open("images/support_background.jpg"))
support_background = Label(root, image=support_background_img)
support_background.pack()
support_window = support.create_window(0, 0, anchor=NW, window=support_background)



spellhero_1 = magic("")
spellhero_2 = magic("")
all_units = []
magicnow = 0
turni = 0
fght = 0
unita = unit()
end_of_game = 0


# FIXME: class Menu:
class Interface:
    def __init__(self, command1, command2, command3, command4):
        self.restart = Button(root, text="reset battlefield", background="#555", foreground="#ccc", width="20",
                              height="3", command=command1)
        self.restart_window = Menu.create_window(75, 100, anchor=NW, window=self.restart)

        self.start = Button(text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                            command=command2)
        self.start_window = Menu.create_window(75, 175, anchor=NW, window=self.start)

        self.spell_book = Button(text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command3)
        self.spell_book_window = Menu.create_window(75, 250, anchor=NW, window=self.spell_book)

        self.create_hero = Button(text="Create Hero", background="#555", foreground="#ccc", width="20", height="3",
                                  command=command4)  # что это


class Menu2_layout:
    def __init__(self):
        # картинка для стартового окна
        self.menu2_start_screen_img = ImageTk.PhotoImage(Image.open("images/menu2_start.jpg"))
        self.menu2_start_screen = Label(root, image=self.menu2_start_screen_img)
        self.menu2_start_screen.pack()

        self.screen_start()
        # labels для окна с юнитами
        self.label_attack = Label(root, text='Attack: ')
        self.label_attack.pack()
        self.label_defence = Label(root, text='Defence: ')
        self.label_defence.pack()
        self.label_unit_num = Label(root, text='Persons in unit: ')
        self.label_unit_num.pack
        # labels для окна с заклинаниями
        # FIXME: написать все характеристики

    def screen_start(self):
        #pass
        self.menu2_start_screen_window = Menu2.create_window(50, 50, anchor=NW, window=self.menu2_start_screen)

    def screen_info_unit(self):
        pass

    def screen_info_spell(self):
        pass

    def delete(self):
        if self.menu2_start_screen_window is not None:
            Menu2.delete(self.menu2_start_screen_window)
        if self.label_unit_num_window is not None:
            Menu2.delete(self.label_unit_num_window)
            Menu2.delete(self.label_defence_num_window)
            Menu2.delete(self.label_attack_window)
            self.label_attack = Label(root, text='Attack: ')
            self.label_defence = Label(root, text='Defence: ')
            self.label_unit_num = Label(root, text='Persons in unit: ')

field = BF.Field()


# FIXME: Change interface into new one
# def Interface():
#     pass

def print_unit(un):
    x = un.x - 1
    y = un.y - 1
    Table.delete(un.id)
    if un.hero == 1:
        un.id = Table.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="blue")
    else:
        un.id = Table.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="green")


def cell_update():
    Table.delete(Table_window)
    field.biom_reset()
    for i in range(12):
        for j in range(12):
            field.cell_list[i][j].biom = field.biom_generation(i, j)
            if field.cell_list[i][j].id is not None:
                Table.delete(field.cell_list[i][j].id)

            # FIXME:если есть идеи, то можете попытаться исправить эту функцию, а то она походит на костыль
            field.cell_list[i][j].id = Table.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
                                                              (2 + 50 * field.cell_list[i][j].coordy),
                                                              (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                                              (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                                              fill=field.cell_list[i][j].biom)
        for un in all_units:
            print_unit(un)


def round_update():
    for un in all_units:
        print_unit(un)


def conket(units_1, units_2):
    global all_units
    all_units = units_1 + units_2
    all_units.sort(key=sortbyinit)


def available_move(unit):
    for i in range(12):
        for j in range(12):
            if abs(unit.x - i - 1) + abs(unit.y - j - 1) >= unit.speed:
                field.cell_list[i][j].id = Table.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
                                                                  (2 + 50 * field.cell_list[i][j].coordy),
                                                                  (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                                                  (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                                                  fill=field.cell_list[i][j].biom, outline="black")
            else:
                Table.delete(field.cell_list[i][j].id)
                field.cell_list[i][j].id = Table.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
                                                                  (2 + 50 * field.cell_list[i][j].coordy),
                                                                  (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                                                  (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                                                  fill=field.cell_list[i][j].biom, outline="lightblue")


def end_round():
    for un in all_units:
        un.ApplyAllEffects()
    magicnow = 1
    print("Введите заклинание первого игрока")
    input_1 = str(input())
    global spellhero_1
    spellhero_1 = magic(input_1)
    print("Введите заклинание второго игрока")
    input_2 = str(input())
    global spellhero_2
    spellhero_2 = magic(input_2)

    global end_of_game
    end_of_game = 1
    for un in all_units:
        if un.hero != all_units[0]:
            end_of_game = 0


def clickl(event):
    global all_units
    global turni
    global fght
    global magicnow
    global unita
    n = 0
    if magicnow == 1:
        for un in all_units:
            if math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y:
                spellhero_1.cast(un, hero_1)
                magicnow = 2
    elif magicnow == 2:
        for un in all_units:
            if math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y:
                spellhero_1.cast(un, hero_2)
                magicnow = 0
    if (magicnow == 0):
        for un in all_units:
            if math.trunc((event.x - 100) / 50) == un.x and math.trunc((event.y) / 50) == un.y:
                n += 1
        if (fght == 0):
            for un in all_units:
                if math.trunc((event.x - 100) / 50) == un.x and \
                        math.trunc(event.y / 50) == un.y and all_units[turni].hero != un.hero:
                    for i in range(12):
                        for j in range(12):
                            Table.delete(field.cell_list[i][j].id)
                            field.cell_list[i][j].id = Table.create_rectangle(
                                (2 + 50 * field.cell_list[i][j].coordx),
                                (2 + 50 * field.cell_list[i][j].coordy),
                                (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                fill=field.cell_list[i][j].biom, outline="black")
                            round_update()
                            if (abs(all_units[turni].x - i - 1) + abs(all_units[turni].y - j - 1) < un.speed and
                                abs(i - un.x) + abs(j - un.y) == 1) or type(all_units[turni]) == unitarcher:
                                Table.delete(field.cell_list[i][j].id)
                                field.cell_list[i][j].id = Table.create_rectangle(
                                    (200 + 50 * (field.cell_list[i][j].coordx - 1)),
                                    (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                                    (200 + 50 * field.cell_list[i][j].coordx),
                                    (100 + 50 * field.cell_list[i][j].coordy),
                                    fill=field.cell_list[i][j].biom, outline="gold")
                                round_update()
                                fght = 1
                                unita = un
        else:
            print(abs(unita.x - math.trunc((event.x - 100) / 50)), abs(unita.y - math.trunc(event.y / 50)))
            if abs(unita.x - math.trunc((event.x - 100) / 50)) + abs(unita.y - math.trunc(event.y / 50)) <= 1:
                if type(all_units[turni]) == meleeunit:
                    a = all_units[turni].move(math.trunc((event.x - 100) / 50), math.trunc((event.y) / 50))
                    round_update()
                    if a == True:
                        all_units[turni].fight(unita)
                        unita.fight(all_units[turni])
                        available_move(all_units[turni])
                        turni += 1
                        fght = 0
                        if turni == len(all_units):
                            turni = 0
                            available_move(all_units[turni])
                            end_round()
                        round_update()
                elif type(all_units[turni]) == unitarcher and all_units[turni].shoot >= 0:
                    all_units[turni].fight(unita)
                    all_units[turni].shoot -= 1
                    turni += 1
                    fght = 0
                    if turni == len(all_units):
                        turni = 0
                        available_move(all_units[turni])
                        end_round()
                    round_update()
        for un in all_units:
            if math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y:
                n += 1
        if n == 0 and fght == 0:
            a = all_units[turni].move(math.trunc((event.x - 100) / 50), math.trunc(event.y / 50))
            round_update()
            if a == True:
                turni += 1
                if turni == len(all_units):
                    turni = 0
                    available_move(all_units[turni])
                    end_round()
                round_update()


def clickr(event):
    global all_units
    for un in all_units:
        if math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y:
            print("")
            print("atk = ", un.atk)
            print("defe = ", un.defe)
            print("hp = ", un.hpta - un.hpun * (un.num - 1))
            print("num = ", un.num)
            print("speed = ", un.speed)
            print("moral = ", un.moral)
            print("luck = ", un.luck)
            print("x = ", un.x)
            print("y = ", un.y)
            print("effects:", un.effect)


def sortbyinit(str):
    return str.init


root.bind('<Button-3>', clickr)
root.bind('<Button-1>', clickl)
