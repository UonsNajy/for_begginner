from tkinter import *
root = Tk()

def my_ckick():
    my_label = Label(root,text="Helle Tkinter!").pack
my_labe2 = Label(root, text="My name is Younes Najy!")

my_labe2 = Label(root, text="")
my_label.grid(row=0, column=0)
my_labe2.grid(row=2, column=1)
root.mainloop()