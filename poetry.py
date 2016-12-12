from tkinter import *

root = Tk()

textFrame = Frame(root)
textFrame.pack()

buttonFrame = Frame(root)
buttonFrame.pack()

infoFrame = Frame(root)
infoFrame.pack()

lines = []

class Line:
  def __init__(self, seed):
    self.seed = seed
    self.line = ""
    self.complete = False

def clearFrames():
  for child in textFrame.winfo_children():
    child.pack_forget()
  for child in buttonFrame.winfo_children():
    child.pack_forget()

def setInfo():
  info.configure(state="normal")
  info.delete(1.0, END)
  info.insert(INSERT, "Amount of seeds: " + str(len(lines)) + "\n")

  drafts = 0
  complete = 0

  for line in lines:
    if len(line.line) > 0:
      drafts += 1
    if line.complete:
      complete += 1

  info.insert(INSERT, "Amount of drafts: " + str(drafts - complete) + "\n")
  info.insert(INSERT, "Amount completed: " + str(complete))
  info.configure(state="disabled")

def newSeedDef():
  clearFrames()
  seed.delete(0, END)
  setInfo()

  seed.pack()
  newSeed.pack(side=LEFT)
  saveSeed.pack(side=LEFT)
  info.pack()

def saveSeedDef():
  text = seed.get()
  lines.append(Line(text))

  clearFrames()
  setInfo()

  message.pack()
  newSeed.pack(side=LEFT)
  info.pack()

message = Label(textFrame, text="Message!", width=80)
seed = Entry(textFrame, width = 80)
newSeed = Button(buttonFrame, text="New Seed", command=newSeedDef)
saveSeed = Button(buttonFrame, text="Save Seed", command=saveSeedDef)
info = Text(infoFrame, width=80, height=3, state='disabled')

message.pack()
newSeed.pack()

info.pack()

root.mainloop()

