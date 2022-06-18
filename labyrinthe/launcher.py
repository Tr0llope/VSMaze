from tkinter import *

def launch():
    root.destroy()
    import game


root = Tk()
root.title('Menu')
title = Label(root, text = 'VS Maze', font = (20))
title.pack()
frame = Canvas(root, bg = 'white', width = 250, height = 250)
frame.pack()
var_image = PhotoImage(file = 'logo.png')
logo = frame.create_image(0, 0, image = var_image, anchor = 'nw')
launch_button = Button(root, text ='Play', command = launch, width = 5)
launch_button.pack()

root.mainloop()
