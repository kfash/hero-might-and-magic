from tkinter import *
from PIL import Image, ImageTk
import BattleField as BF

# FIXME: написать функцию, которая отображает передвижение юнита

all_units = list()
magici = 0

root = Tk()
root.wm_title("Final Fantasy XVI")
root.geometry("1300x700")
root.resizable(width=False, height=False)

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
imagine = Menu.create_image(2, 2, anchor=NW, image=Menu_background_img)

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

# Подгрузка текстур
# FIXME: добавить иконки персонажей и юнитов
archer_right = ImageTk.PhotoImage(Image.open("images/archer.png"))
crusader_left = ImageTk.PhotoImage(Image.open("images/crusader.png"))


# FIXME: class Menu:
class Menu_layout:
    def __init__(self, command1, command2, command3, command4, command5, command7, command8, command9,
                 command10, command11, command12, command13, command14, command15):

        self.reset = Button(root, text="reset battlefield", background="#555", foreground="#ccc", width="20",
                            height="3", command=command1)
        self.set = Button(root, text="set battlefield", background="#555", foreground="#ccc", width="20",
                          height="3", command=command1)
        self.start = Button(root, text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                            command=command2)
        self.spell_book = Button(root, text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                 command=self.spell_book_screen)
        self.start_game = Button(root, text="start game", background="#555", foreground="#ccc", width="20", height="3",
                                 command=self.pass_screen)
        self.back_to_game = Button(root, text="back", background="#555", foreground="#ccc", width="20",
                                   height="3", command=command5)
        self.back_to_battle = Button(root, text="back", background="#555", foreground="#ccc", width="20",
                                     height="3", command=self.start_screen)
        self.back_to_spells = Button(root, text="back", background="#555", foreground="#ccc", width="20",
                                     height="3", command=self.battle_screen)
        self.pass_turn = Button(root, text="pass", background="#555", foreground="#ccc", width="20",
                                height="3", command=self.pass_screen)
        self.give_up = Button(root, text="give up", background="#555", foreground="#ccc", width="20",
                              height="3", command=self.winner_screen)
        self.winner = Button(root, text="♀congrats♀", background="#555", foreground="#ccc", width="20",
                             height="3", command=self.start_screen)
        self.magic_arrow = Button(root, text="magic arrow", background="#555", foreground="#ccc", width="20",
                                  height="3", command=command11)
        self.lightning_bolt = Button(root, text="lightning bolt", background="#555", foreground="#ccc", width="20",
                                     height="3", command=command12)
        self.blessing = Button(root, text="blessing", background="#555", foreground="#ccc", width="20",
                               height="3", command=command13)
        self.stone_skin = Button(root, text="stone skin", background="#555", foreground="#ccc", width="20",
                                 height="3", command=command14)
        self.curse = Button(root, text="curse", background="#555", foreground="#ccc", width="20",
                            height="3", command=command15)
        self.ready = Button(root, text="player ready", background="#555", foreground="#ccc", width="20",
                            height="3", command=self.battle_screen)

        self.reset_window = self.set_window = self.start_window = self.spell_book_window = self.start_game_window = \
            self.back_to_game_window = self.back_to_battle_window = self.back_to_spells_window = \
            self.pass_turn_window = self.give_up_window = self.winner_window = self.magic_arrow_window = \
            self.lightning_bolt_window = self.blessing_window = self.stone_skin_window = self.curse_window = \
            self.ready_window = None

        self.button_list = (self.reset_window, self.set_window, self.start_window, self.spell_book_window,
                            self.start_game_window, self.back_to_game_window, self.back_to_battle_window,
                            self.back_to_spells_window, self.pass_turn_window, self.give_up_window, self.winner_window,
                            self.magic_arrow_window, self.lightning_bolt_window, self.blessing_window,
                            self.stone_skin_window, self.curse_window, self.ready_window)

        for i in self.button_list:
            i = None
        self.start_screen()

    def start_screen(self):
        self.delete(self.set_window)
        self.delete(self.reset_window)
        self.delete(self.start_window)
        self.delete(self.winner_window)
        self.delete(self.back_to_battle_window)
        self.delete(self.start_game_window)
        if Table_window is not None:
            self.set_window = Menu.create_window(75, 100, anchor=NW, window=self.set)
        else:
            self.reset_window = Menu.create_window(75, 100, anchor=NW, window=self.reset)
        self.start_window = Menu.create_window(75, 175, anchor=NW, window=self.start)

    def preparation_screen(self):
        self.delete(self.set_window)
        self.delete(self.reset_window)
        self.delete(self.start_window)
        self.start_game_window = Menu.create_window(75, 100, anchor=NW, window=self.start_game)
        self.back_to_battle_window = Menu.create_window(75, 175, anchor=NW, window=self.back_to_battle)

    def pass_screen(self):
        self.delete(self.back_to_battle_window)
        self.delete(self.magic_arrow_window)
        self.delete(self.blessing_window)
        self.delete(self.stone_skin_window)
        self.delete(self.curse_window)
        self.delete(self.lightning_bolt_window)
        self.delete(self.start_game_window)
        self.delete(self.pass_turn_window)
        self.delete(self.spell_book_window)
        self.delete(self.give_up_window)
        self.delete(self.back_to_spells_window)
        self.delete(self.back_to_game_window)
        self.ready_window = Menu.create_window(75, 100, anchor=NW, window=self.ready)

    def battle_screen(self):
        # fixme: удаление ненужных кнопок
        self.delete(self.magic_arrow_window)
        self.delete(self.blessing_window)
        self.delete(self.stone_skin_window)
        self.delete(self.curse_window)
        self.delete(self.lightning_bolt_window)
        self.delete(self.back_to_spells_window)
        self.delete(self.ready_window)

        self.spell_book_window = Menu.create_window(75, 100, anchor=NW, window=self.spell_book)
        self.pass_turn_window = Menu.create_window(75, 175, anchor=NW, window=self.pass_turn)
        self.give_up_window = Menu.create_window(75, 250, anchor=NW, window=self.give_up)

    def spell_book_screen(self):
        self.delete(self.spell_book_window)
        self.delete(self.pass_turn_window)
        self.delete(self.give_up_window)

        self.magic_arrow_window = Menu.create_window(75, 100, anchor=NW, window=self.magic_arrow)
        self.lightning_bolt_window = Menu.create_window(75, 175, anchor=NW, window=self.lightning_bolt)
        self.stone_skin_window = Menu.create_window(75, 250, anchor=NW, window=self.stone_skin)
        self.curse_window = Menu.create_window(75, 325, anchor=NW, window=self.curse)
        self.blessing_window = Menu.create_window(75, 400, anchor=NW, window=self.blessing)
        self.back_to_spells_window = Menu.create_window(75, 475, anchor=NW, window=self.back_to_spells)

    def winner_screen(self):
        self.delete(self.set_window)
        self.delete(self.reset_window)
        self.delete(self.start_window)
        self.delete(self.give_up_window)
        self.delete(self.pass_turn_window)
        self.delete(self.spell_book_window)
        self.delete(self.magic_arrow_window)
        self.delete(self.blessing_window)
        self.delete(self.stone_skin_window)
        self.delete(self.curse_window)
        self.delete(self.lightning_bolt_window)
        self.delete(self.back_to_spells_window)

        self.winner_window = Menu.create_window(75, 100, anchor=NW, window=self.winner)

    def delete(self, window):
        if window is not None:
            Menu.delete(window)
            window = None


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


def print_unit(un):
    x = un.x
    y = un.y
    Table.delete(un.id)
    if un.hero == 1:
        un.id = Table.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="blue")
    else:
        un.id = Table.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="green")

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
    round_update()

def round_update():
    for un in all_units:
        print_unit(un)


def conket(units_1, units_2):
    global all_units
    all_units = units_1 + units_2
    all_units.sort(key=sortbyinit)

def sortbyinit(str):
    return str.init


def available_move(unit):
    for i in range(12):
        for j in range(12):
            if abs(unit.x - i) + abs(unit.y - j) >= unit.speed:
                Table.delete(field.cell_list[i][j].id)
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
                                                                  fill=field.cell_list[i][j].biom, outline="red")


def magic1():
    global magici
    magici = 1
    print(1)

def magic2():
    global magici
    magici = 2
    print(2)

def magic3():
    global magici
    magici = 3

def magic4():
    global magici
    magici = 4

def magic5():
    global magici
    magici = 5

def magicreturn():
    global  magici
    a = magici
    magici = 0
    return a


# def army_placement(fraction_list1, fraction_list2, side):
#     height = root.winfo_height()
#
#     if side == 'left':
#         for units in fraction_list1:
#             units['readiness'] = False
#             root.winfo_height()
#             root.after()
#         army_placement(fraction_list2, fraction_list2, 'right')
#     else:
#         pass


field = BF.Field()
menu_layout = Menu_layout(cell_update, preparation, cell_update, cell_update, cell_update, cell_update, cell_update,
                          cell_update, cell_update, magic1, magic2, magic3, magic4, magic5)
menu2_layout = Menu2_layout()

