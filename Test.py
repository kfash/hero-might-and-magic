from reInterface import *
from math import *

# Menu_background_img = ImageTk.PhotoImage(Image.open("images/menu_background.jpg"))
# imagine = Menu.create_image(2, 2, anchor=NW, image=Menu_background_img)
mem = ImageTk.PhotoImage(Image.open("images/archangel.png"))
a = Menu.create_image(2, 2, anchor=NW, image=mem)
mem2 = ImageTk.PhotoImage(Image.open("images/crusader.png"))
a = Menu.create_image(52, 52, anchor=NW, image=crusader_left)

# # attack_text = Menu.create_text(10, 0, anchor=NW, text='left for dead')
# # Menu.create_window(10,10, anchor=NW, window=attack_text)
# # # def coords_click(event):
# #     # if (root.winfo_pointery() - root.winfo_rooty() < 605) and (root.winfo_pointerx() - root.winfo_rootx() > 347) \
# #     #         and (root.winfo_pointerx() - root.winfo_rootx() < 952):
# #     #     print(trunc(event.x / 50) + 1, ' ', trunc(event.y / 50) + 1)
# #
# #
# # # root.bind('<Button-1>', coords_click)
root.mainloop()
