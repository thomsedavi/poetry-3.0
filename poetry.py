import tkinter
from tkinter import *

root = tkinter.Tk()

text = Text(root, width=80, height=4)
text.insert(INSERT, "Hello world, I guess?")
text.configure(state="disabled")
text.pack()

entry = Text(root, width=80, height=4)
entry.pack()

root.mainloop()

