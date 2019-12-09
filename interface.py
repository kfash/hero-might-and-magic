from tkinter import *
from PIL import Image, ImageTk
import math
import BattleField as BF
from Hero import *
from unit import *

root = Tk()
Menu = Canvas(root, width=200, height=600, bg='green')
Menu.pack(side=LEFT)
Menu2 = Canvas(root, width=200, height=600, bg='green')
Menu2.pack(side=RIGHT)
Field = Canvas(root, width=601, height=601, bg='white')
Field.pack(side=TOP)
# support = Canvas(root, width=200, height=200, bg='black')
# support.pack(side=BOTTOM)
canv = Canvas()
root.wm_title("Tkinter window")
root.geometry("1200x700")

all_units = []

turni = 0
fght = 0
unita = unit()


class Interface:
    def __init__(self, command1, command2, command3, command4):
        self.restart = Button(text="reset battlefield", background="#555", foreground="#ccc", width="20", height="3",
                              command=command1)
        self.restart.place(x=0, y=100)
        self.start = Button(text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                            command=command2).place(x=0, y=160)
        self.spell_book = Button(text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command3).place(x=0, y=220)

        self.create_hero = Button(text="Create Hero", background="#555", foreground="#ccc", width="20", height="3",
                                  command=command4).place(x=0, y=280)


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)

        load = Image.open("parrot.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

field = BF.Field()

def print_unit(un):
    x = un.x - 1
    y = un.y - 1
    Field.delete(un.id)
    if un.hero == 1:
        un.id = Field.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="blue")
    else:
        un.id = Field.create_oval(2 + x * 50, 2 + y * 50, 52 + x * 50, 52 + y * 50, fill="green")


def cell_update():
    field.biom_reset()
    for i in range(12):
        for j in range(12):
            field.cell_list[i][j].biom = field.biom_generation(i, j)
            if field.cell_list[i][j].id is not None:
                Field.delete(field.cell_list[i][j].id)

            # FIXME:если есть идеи, то можете попытаться исправить эту функцию, а то она походит на костыль
            field.cell_list[i][j].id = Field.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
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
                field.cell_list[i][j].id = Field.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
                                                                  (2 + 50 * field.cell_list[i][j].coordy),
                                                                  (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                                                  (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                                                  fill=field.cell_list[i][j].biom, outline="black")

            else:
                Field.delete(field.cell_list[i][j].id)
                field.cell_list[i][j].id = Field.create_rectangle((2 + 50 * field.cell_list[i][j].coordx),
                                                                  (2 + 50 * field.cell_list[i][j].coordy),
                                                                  (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                                                                  (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                                                                  fill=field.cell_list[i][j].biom, outline="lightblue")


def clickl(event):
    global all_units
    global turni
    global fght
    global unita
    n = 0

    for un in all_units:
        if math.trunc((event.x - 100) / 50) == un.x and math.trunc((event.y) / 50) == un.y:
            n += 1
    if fght == 0:
        for un in all_units:
            if (math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y and
                    all_units[turni].hero != un.hero):
                for i in range(12):
                    for j in range(12):
                        Field.delete(field.cell_list[i][j].id)
                        field.cell_list[i][j].id = Field.create_rectangle(
                            (2 + 50 * field.cell_list[i][j].coordx),
                            (2 + 50 * field.cell_list[i][j].coordy),
                            (2 + 50 * (field.cell_list[i][j].coordx + 1)),
                            (2 + 50 * (field.cell_list[i][j].coordy + 1)),
                            fill=field.cell_list[i][j].biom, outline="black")
                        round_update()

                        if ((abs (all_units[turni].x - i - 1) + abs( all_units[turni].y - j - 1) < un.speed and abs(i - un.x) + abs(j - un.y) == 1) or type(all_units[turni])==unitarcher):
                            canv.delete(field.cell_list[i][j].id)
                            field.cell_list[i][j].id = canv.create_rectangle(
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

            if (type(all_units[turni])==meleeunit):
                a = all_units[turni].move(math.trunc((event.x - 100) / 50), math.trunc((event.y) / 50))
                round_update()
                if (a == True):
                    all_units[turni].fight(unita)
                    unita.fight( all_units[turni])
                    available_move(all_units[turni])
                    turni += 1
                    fght = 0
                    if (turni == len(all_units)):
                        turni = 0
                        available_move(all_units[turni])
                        end_round()
                    round_update()
            elif (type(all_units[turni])==unitarcher and all_units[turni].shoot>=0):
                all_units[turni].fight(unita)
                all_units[turni].shoot-=1
                turni += 1
                fght = 0
                if (turni == len(all_units)):
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
        if (a == True):
            turni+=1
            if (turni == len(all_units)):
                turni=0
                available_move(all_units[turni])
                end_round()
            round_update()


def clickr(event):
    global all_units
    for un in all_units:
        if math.trunc((event.x - 100) / 50) == un.x and math.trunc(event.y / 50) == un.y:
            print("atk = ", un.atk)
            print("defe = ", un.defe)
            print("hp = ", un.hpta - un.hpun * (un.num - 1))
            print("num = ", un.num)
            print("speed = ", un.speed)
            print("moral = ", un.moral)
            print("luck = ", un.luck)
            print("x = ", un.x)
            print("y = ", un.y)


def sortbyinit(str):
    return str.init


root.bind('<Button-3>', clickr)
root.bind('<Button-1>', clickl)


