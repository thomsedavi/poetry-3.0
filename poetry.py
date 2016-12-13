from tkinter import *
import pickle
import random

root = Tk()

textFrame = Frame(root)
textFrame.pack()

buttonFrame = Frame(root)
buttonFrame.pack()

infoFrame = Frame(root)
infoFrame.pack()

lines = []
index = 0

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

def packButtons():
  newSeed.pack(side=LEFT)
  nextLineTrue = False
  for line in lines:
    if not line.complete:
      nextLineTrue = True
  if nextLineTrue:
    nextLine.pack(side=LEFT)
  saveFile.pack(side=LEFT)
  loadFile.pack(side=LEFT)

def newSeedDef():
  clearFrames()
  entry.delete(0, END)
  setInfo()

  entry.pack()
  packButtons()
  saveSeed.pack(side=LEFT)
  info.pack()

def nextLineDef():
  global index

  clearFrames()
  setInfo()

  if len(lines) == 1:
    index = 0
  else:
    index = (index + random.randint(1,len(lines)-1)) % len(lines)

  while lines[index].complete:
    index += 1
    index %= len(lines)

  display.configure(state="normal")
  display.delete(1.0, END)
  display.insert(INSERT, lines[index].seed)
  display.configure(state="disabled")

  entry.delete(0, END)
  entry.insert(INSERT, lines[index].line)

  display.pack()
  entry.pack()

  packButtons()
  saveDraft.pack(side=LEFT)
  saveLine.pack(side=LEFT)

  info.pack()

def saveDraftDef():
  global index

  text = entry.get()
  lines[index].line = text

  clearFrames()
  setInfo()

  message.pack()
  packButtons()
  info.pack()

def saveLineDef():
  global index

  text = entry.get()
  lines[index].line = text
  lines[index].complete = True

  clearFrames()
  setInfo()

  message.pack()
  packButtons()
  info.pack()

def saveSeedDef():
  text = entry.get()
  lines.append(Line(text))

  clearFrames()
  setInfo()

  message.pack()
  packButtons()
  info.pack()

def saveFileDef():
  pickle.dump(lines, open("test.ptry", "wb"))

def loadFileDef():
  global lines
  lines = pickle.load(open("test.ptry", "rb"))
  clearFrames()
  setInfo()
  packButtons()
  info.pack()

message = Label(textFrame, text="Saved!", width=80)
display = Text(textFrame, width=80, height=3, state="disabled")
entry = Entry(textFrame, width=80)
newSeed = Button(buttonFrame, text="New Seed", command=newSeedDef)
saveSeed = Button(buttonFrame, text="Save Seed", command=saveSeedDef)
nextLine = Button(buttonFrame, text="Next Line", command=nextLineDef)
saveDraft = Button(buttonFrame, text="Save Draft", command=saveDraftDef)
saveLine = Button(buttonFrame, text="Save Line", command=saveLineDef)
saveFile = Button(buttonFrame, text="Save File", command=saveFileDef)
loadFile = Button(buttonFrame, text="Load File", command=loadFileDef)
info = Text(infoFrame, width=80, height=3, state="disabled")

message.pack()
newSeed.pack()

info.pack()

root.mainloop()

