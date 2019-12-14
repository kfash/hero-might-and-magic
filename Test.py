from tkinter import *
from PIL import Image, ImageTk
from unit import *
from math import *

root = Tk()
Menu = Canvas(root, width=300, height=600, bg='green')
Menu.pack(side=LEFT)
Menu2 = Canvas(root, width=300, height=600, bg='green').pack(side=RIGHT)
Field = Canvas(root, width=600, height=600, bg='white').pack(side=TOP)
support = Canvas(root, width=200, height=200, bg='black').pack(side=BOTTOM)
root.wm_title("Tkinter window")
root.geometry("1300x700")
root.resizable(width=False, height=False)
Menu_background_img = ImageTk.PhotoImage(Image.open("images/menu_background.jpg"))
Menu_background = Label(root, image=Menu_background_img)
Menu_background.pack()
Menu.create_window(0, 0, anchor=NW, window=Menu_background)
restart = Button(text="reset battlefield", background="#555", foreground="#ccc", width="20", height="3")
restart_window = Menu.create_window(75, 10, anchor=NW, window=restart)

def coords_click(event):
    if (root.winfo_pointery() - root.winfo_rooty() < 605) and (root.winfo_pointerx() - root.winfo_rootx() > 347) \
            and (root.winfo_pointerx() - root.winfo_rootx() < 952):
        print(trunc(event.x / 50) + 1, ' ', trunc(event.y / 50) + 1)


root.bind('<Button-1>', coords_click)
root.mainloop()


