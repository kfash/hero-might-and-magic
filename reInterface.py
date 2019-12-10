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


# FIXME: class Menu:
class Menu_layout:
    def __init__(self, command1, command2, command3, command4):
        self.reset = Button(root, text="reset battlefield", background="#555", foreground="#ccc", width="20",
                            height="3", command=command1)
        self.set = Button(root, text="set battlefield", background="#555", foreground="#ccc", width="20",
                          height="3", command=command1)
        self.start = Button(text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                            command=command2)
        self.spell_book = Button(text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command3)
        self.start_game = Button(text="start game", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command4)

        self.reset_window = self.set_window = self.start_window = self.spell_book_window = self.start_game_window = None
        self.start_screen()

    def start_screen(self):
        self.delete()
        if Table_window is not None:
            self.set_window = Menu.create_window(75, 100, anchor=NW, window=self.set)
        else:
            self.reset_window = Menu.create_window(75, 100, anchor=NW, window=self.reset)
        self.start_window = Menu.create_window(75, 175, anchor=NW, window=self.start)

    def preparation_screen(self):
        self.delete()
        self.start_game_window = Menu.create_window(75, 175, anchor=NW, window=self.start_game)

    def battle_screen(self):
        self.delete()
        self.spell_book_window = Menu.create_window(75, 250, anchor=NW, window=self.spell_book)

    def delete(self):
        if self.set_window is not None:
            Menu.delete(self.set_window)
            self.set_window = None
        if self.reset_window is not None:
            Menu.delete(self.reset_window)
            self.reset_window = None
        if self.start_game_window is not None:
            Menu.delete(self.start_game_window)
            self.start_game_window = None
        if self.start_window is not None:
            Menu.delete(self.start_window)
            self.start_window = None
        if self.spell_book_window is not None:
            Menu.delete(self.spell_book_window)
            self.spell_book = None


class Menu2_layout:
    def __init__(self):
        # картинка для стартового окна
        self.menu2_start_screen_img = ImageTk.PhotoImage(Image.open("images/menu2_start.jpg"))
        self.menu2_start_screen = Label(root, image=self.menu2_start_screen_img)
        self.menu2_start_screen_window = None
        self.label_attack = Label(root, text='Attack: ')
        self.label_attack_window = None
        self.label_defence = Label(root, text='Defence: ')
        self.label_defence_window = None
        self.label_unit_num = Label(root, text='Persons in unit: ')
        self.label_unit_num_window = None
        self.start_screen()
        # labels для окна с заклинаниями
        # FIXME: написать все характеристики

    def start_screen(self):
        self.delete()
        self.menu2_start_screen_window = Menu2.create_window(50, 50, anchor=NW, window=self.menu2_start_screen)

    def preparation_screen(self):
        self.delete()
        self.label_attack_window = Menu2.create_window(50, 50, anchor=NW, window=self.label_attack)

    def screen_info_unit(self):
        self.label_attack_window = Menu2.create_window(50, 50, anchor=NW, window=self.label_attack)

    def screen_info_spell(self):
        pass

    def delete(self):
        if self.menu2_start_screen_window is not None:
            Menu2.delete(self.menu2_start_screen_window)
            self.menu2_start_screen_window = None
        if self.label_attack_window is not None:
            Menu2.delete(self.label_attack_window)
            self.label_attack_window = None
        if self.label_unit_num_window is not None:
            Menu2.delete(self.label_unit_num_window)
            Menu2.delete(self.label_defence_num_window)
            Menu2.delete(self.label_attack_window)
            self.label_attack = Label(root, text='Attack: ')
            self.label_defence = Label(root, text='Defence: ')
            self.label_unit_num = Label(root, text='Persons in unit: ')


def cell_update():
    global Table_window
    if Table_window is not None:
        Table.delete(Table_window)
        Table_window = None
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
    menu_layout.start_screen()
    menu2_layout.start_screen()


def preparation():
    menu_layout.preparation_screen()
    menu2_layout.preparation_screen()

def army_placement(fraction_list1, fraction_list2, side):
    height = root.winfo_height()

    if side == 'left':
        for units in fraction_list1:
            units['readiness'] = False
            root.winfo_height()
            root.after()
        army_placement(fraction_list2, fraction_list2, 'right')
    else:
        pass


field = BF.Field()
menu_layout = Menu_layout(cell_update, preparation, cell_update, cell_update)
menu2_layout = Menu2_layout()

root.mainloop()
