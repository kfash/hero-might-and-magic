import tkinter as tk
from PIL import Image, ImageTk
import math
import BattleField as BF
from Hero import*
from unit import*

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1200x700')
root.title("Final fantasy XVI")
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
all_units = []

turni = 0
fght = 0
unita = meleeunit()

class Interface:
    def __init__(self, command1, command2, command3, command4):

        self.restart = tk.Button(text="reset battlefield", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command1)
        self.restart.place(x=0, y=100)
        self.start = tk.Button(text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                               command=command2)
        self.start.place(x=0, y=160)
        self.spell_book = tk.Button(text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                    command=command3)
        self.spell_book.place(x=0, y=220)

        self.create_hero = tk.Button(text="Create Hero", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command4)
        self.create_hero.place(x=0, y=280)


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
    x=un.x
    y=un.y
    canv.delete(un.id)
    if (un.hero == 1):
        un.id = canv.create_oval(100 + x * 50, y * 50, 150 + x * 50, 50 + y * 50, fill="blue")
    else:
        un.id = canv.create_oval(100 + x * 50, y * 50, 150 + x * 50, 50 + y * 50, fill="green")

def cell_update():
    field.biom_reset()
    for i in range(12):
        for j in range(12):
            field.cell_list[i][j].biom = field.biom_generation(i, j)
            if (field.cell_list[i][j].id != None):
                canv.delete(field.cell_list[i][j].id)


            field.cell_list[i][j].id = canv.create_rectangle((200 + 50 * (field.cell_list[i][j].coordx - 1)),
                                                             (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                                                             (200 + 50 * field.cell_list[i][j].coordx),
                                                             (100 + 50 * field.cell_list[i][j].coordy),
                                                             fill=field.cell_list[i][j].biom)
        for un in all_units:
            print_unit(un)

def round_update():
    for un in all_units:
        print_unit(un)



def conket(units_1, units_2):
    global all_units
    all_units=units_1 + units_2
    all_units.sort(key=sortbyinit)

def available_move (unit):
    for i in range(12):
        for j in range(12):
            if (abs(unit.x - i - 1) + abs(unit.y - j - 1) >= unit.speed):
                field.cell_list[i][j].id = canv.create_rectangle((200 + 50 * (field.cell_list[i][j].coordx - 1)),
                                                                 (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                                                                 (200 + 50 * field.cell_list[i][j].coordx),
                                                                 (100 + 50 * field.cell_list[i][j].coordy),
                                                                 fill=field.cell_list[i][j].biom, outline="black")

            else:
                canv.delete(field.cell_list[i][j].id)
                field.cell_list[i][j].id = canv.create_rectangle((200 + 50 * (field.cell_list[i][j].coordx - 1)),
                                                                 (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                                                                 (200 + 50 * field.cell_list[i][j].coordx),
                                                                 (100 + 50 * field.cell_list[i][j].coordy),
                                                                 fill=field.cell_list[i][j].biom, outline="lightblue")


def clickl(event):
    global all_units
    global turni
    global fght
    global unita
    n = 0

    for un in all_units:
        if (math.trunc((event.x - 100) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
            n += 1
    if (fght == 0):
        for un in all_units:
            if (math.trunc((event.x - 100) / 50) == un.x and math.trunc((event.y) / 50) == un.y and all_units[turni].hero != un.hero):
                for i in range(12):
                     for j in range(12):
                        canv.delete(field.cell_list[i][j].id)
                        field.cell_list[i][j].id = canv.create_rectangle(
                            (200 + 50 * (field.cell_list[i][j].coordx - 1)),
                            (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                            (200 + 50 * field.cell_list[i][j].coordx),
                            (100 + 50 * field.cell_list[i][j].coordy),
                            fill=field.cell_list[i][j].biom, outline="black")
                        round_update()

                        if (abs (all_units[turni].x - i - 1) + abs( all_units[turni].y - j - 1) < un.speed and abs(i - un.x) + abs(j - un.y) == 1):
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
        print(abs (unita.x - math.trunc((event.x - 100) / 50) ), abs(unita.y - math.trunc((event.y) / 50) ))
        if (abs (unita.x - math.trunc((event.x - 100) / 50) ) + abs(unita.y - math.trunc((event.y) / 50) ) <= 1):

            a = all_units[turni].move(math.trunc((event.x - 100) / 50), math.trunc((event.y) / 50))
            round_update()
            if (a == True):
                all_units[turni].fight(unita)
                unita.fight( all_units[turni])
                turni += 1
                fght = 0
                if (turni == len(all_units)):
                    turni = 0
                available_move(all_units[turni])
                round_update()

    for un in all_units:
        if (math.trunc((event.x - 100) / 50) == un.x and math.trunc((event.y) / 50) == un.y):
            n += 1


    if (n == 0 and fght == 0):
        a = all_units[turni].move(math.trunc((event.x-100)/50), math.trunc((event.y)/50))
        round_update()
        if (a == True):
            turni+=1
            if (turni == len(all_units)):
                turni = 0
            available_move(all_units[turni])
            round_update()

def clickr(event):
    global all_units
    for un in all_units:
        if (math.trunc((event.x-100)/50) == un.x and math.trunc((event.y)/50) == un.y):
            print("atk = ", un.atk)
            print("defe = ", un.defe)
            print("hp = ", un.hpta - un.hpun*(un.num-1))
            print("num = ", un.num)
            print("speed = ", un.speed)
            print("moral = ", un.moral)
            print("luck = ", un.luck)
            print("x = ", un.x)
            print("y = ", un.y)

def sortbyinit (str):
    return str.init

canv.bind('<Button-3>', clickr)
canv.bind('<Button-1>', clickl)






