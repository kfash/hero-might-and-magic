
from Hero import*
from magic import*
from interface import*


def start():
    hero_1 = hero()
    hero_2 = hero()
    units_1 = []
    units_2 = []
    for i in range (1,7):
        un = unit()
        units_1.append(un)
        units_2.append(un)
    Kak(units_1, units_2)


inter = Interface(cell_update, cell_update, cell_update,cell_update)
start()
root.mainloop()

def round ():
    pass

