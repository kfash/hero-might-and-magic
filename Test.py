from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("parrot.jpg")
        load = load.resize([1200, 600])

        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
root = Tk()
Menu = Canvas(root, width=300, height=600, bg='green').pack(side=LEFT)
Menu2 = Canvas(root, width=300, height=600, bg='green').pack(side=RIGHT)
Field = Canvas(root, width=600, height=600, bg='white').pack(side=TOP)
support = Canvas(root, width=200, height=200, bg='black').pack(side=BOTTOM)
root.wm_title("Tkinter window")
root.geometry("1200x700")
root.mainloop()