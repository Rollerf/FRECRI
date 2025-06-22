from tkinter import *
import sys
import os

def fileReader(fic):
    file = []
    for line in fic:
        line = line.split("=")
        line[1] = line[1].replace("\n","")
        file.append(line)
    fic.close()
    return file

def replaceCharacters(fileProperties, fileInput):
  for character in fileProperties:
    fileInput = fileInput.replace(character[0],character[1]);
  
  return fileInput

def get_properties_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, 'format.properties')

def transform():
  fileProperties = []
  fileInput = inputText.get("1.0", "end")

  properties_path = get_properties_path()
  with open(properties_path, "r", encoding="utf8") as fic:
    fileProperties = fileReader(fic)

  fileOutput = replaceCharacters(fileProperties, fileInput)

  outputText.delete(1.0, END)

  outputText.configure(state='normal')

  outputText.insert(1.0, fileOutput)

  outputText.configure(state='disabled')



root = Tk()

root.resizable(False, False)

myFrame = Frame(root, width=500, height=500)

myFrame.pack()

inputText = Text(myFrame, width=50, height=50)
inputText.grid(row=0, column=0, padx=10, pady=10)

scrollYInputText = Scrollbar(myFrame, command=inputText.yview)
scrollYInputText.grid(row=0, column=1, sticky="nsew")

inputText.config(yscrollcommand=scrollYInputText.set)

outputText = Text(myFrame, width=50, height=50)
outputText.grid(row=0, column=2, padx=10, pady=10)

scrollYOutputText = Scrollbar(myFrame, command=outputText.yview)
scrollYOutputText.grid(row=0, column=3, sticky="nsew")

outputText.config(yscrollcommand=scrollYOutputText.set)

tranformButton = Button(root, text="transform",command=transform)
tranformButton.pack()

root.mainloop()