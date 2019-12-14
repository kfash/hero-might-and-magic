from tkinter import *
from PIL import Image, ImageTk
from unit import *
from math import *

root = Tk()
Menu = Canvas(root, width=300, height=600, bg='green')
Menu.pack(side=LEFT)
Menu1 = Canvas(root, width=300, height=600, bg='green')
Menu1.pack(side=LEFT)
Menu2 = Canvas(root, width=300, height=600, bg='green').pack(side=RIGHT)
Field = Canvas(root, width=600, height=600, bg='white').pack(side=TOP)
support = Canvas(root, width=200, height=200, bg='black').pack(side=BOTTOM)
root.wm_title("Tkinter window")

Menu_background_img = ImageTk.PhotoImage(Image.open("images/menu_background.jpg"))
Menu_background = Label(root, image=Menu_background_img)
menu_window = Menu.create_window(0, 0, anchor=NW, window=Menu_background)
attack_text = Menu.create_text(10, 0, anchor=NW, text='left for dead')
Menu.create_window(10,10, anchor=NW, window=attack_text)
# def coords_click(event):
    # if (root.winfo_pointery() - root.winfo_rooty() < 605) and (root.winfo_pointerx() - root.winfo_rootx() > 347) \
    #         and (root.winfo_pointerx() - root.winfo_rootx() < 952):
    #     print(trunc(event.x / 50) + 1, ' ', trunc(event.y / 50) + 1)


# root.bind('<Button-1>', coords_click)
root.mainloop()


