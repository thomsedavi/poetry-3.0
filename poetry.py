from tkinter import *

root = Tk()

textFrame = Frame(root)
textFrame.pack()

buttonFrame = Frame(root)
buttonFrame.pack()

def clearFrames():
  for child in textFrame.winfo_children():
    child.pack_forget()
  for child in buttonFrame.winfo_children():
    child.pack_forget()

def newSeedDef():
  clearFrames()
  seed.delete(0, END)

  seed.pack()
  newSeed.pack(side=LEFT)
  saveSeed.pack(side=LEFT)

def saveSeedDef():
  text = seed.get()
  print(text)

  clearFrames()

  message.pack()
  newSeed.pack()

message = Label(textFrame, text="Message!", width=80)
seed = Entry(textFrame, width = 80)
newSeed = Button(buttonFrame, text="New Seed", command=newSeedDef)
saveSeed = Button(buttonFrame, text="Save Seed", command=saveSeedDef)

message.pack()
newSeed.pack()

root.mainloop()

