
from Hero import*
from magic import*
from interface import*


def start():
    global hero_1
    global hero_2
    global units_1
    global units_2
    hero_1 = hero()
    hero_2 = hero()
    units_1 = []
    units_2 = []
    for i in range (1,7):
        un = unit()
        un.x=i
        units_1.append(un)
        units_2.append(un)
    conket(units_1, units_2)

def new_round():
    units_1[0].move(3,4)


inter = Interface(round_update, cell_update, cell_update,cell_update)
start()
new_round()



root.mainloop()



