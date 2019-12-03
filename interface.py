import tkinter as tk
from PIL import Image, ImageTk
import BattleField as BF
from Hero import*
from unit import*

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1200x700')
root.title("Final fantasy XVI")
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

class Interface:
    def __init__(self, command1, command2, command3):

        self.restart = tk.Button(text="reset battlefield", background="#555", foreground="#ccc", width="20", height="3",
                                 command=command1)
        self.restart.place(x=0, y=100)
        self.start = tk.Button(text="start battle", background="#555", foreground="#ccc", width="20", height="3",
                               command=command2)
        self.start.place(x=0, y=160)
        self.spell_book = tk.Button(text="spell book", background="#555", foreground="#ccc", width="20", height="3",
                                    command=command3)
        self.spell_book.place(x=0, y=220)


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
    canv.create_oval(100+x*50, y*50, 150+x*50, 50+y*50,fill="blue")

def cell_update():
    field.biom_reset()

    for i in range(12):
        for j in range(12):
            field.cell_list[i][j].biom = field.biom_generation(i, j)
            field.cell_list[i][j].id = canv.create_rectangle((200 + 50 * (field.cell_list[i][j].coordx - 1)),
                                                             (100 + 50 * (field.cell_list[i][j].coordy - 1)),
                                                             (200 + 50 * field.cell_list[i][j].coordx),
                                                             (100 + 50 * field.cell_list[i][j].coordy),
                                                             fill=field.cell_list[i][j].biom)
    for un in all_units:
        print_unit(un)

def start_battle():
    pass



inter = Interface(cell_update, cell_update, cell_update)
root.mainloop()

