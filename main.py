
from Hero import*
from magic import*
from interface import*
from unit import*
import time


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
    for i in range (1, 7):
        un = meleeunit()
        a =  canv.create_oval(100+1*50, i*50, 150+1*50, 50+i*50,fill="blue")
        halberdist(un, hero_1, 10, 1, i, a)
        un.hero = 1
        units_1.append(un)
    for i in range(1, 7):
        un = unitarcher()
        a =  canv.create_oval(100 + 6 * 50, i * 50, 150 + 6 * 50, 50 + i * 50, fill="green")
        shooter(un, hero_2, 7, 12, i, a)
        un.hero = 2
        units_2.append(un)
    all_units = units_1 + units_2

    conket(units_1, units_2)
    round_update()



inter = Interface( cell_update, start, cell_update, cell_update)


root.mainloop()



