from tkinter import *
from googletrans import Translator


def fileReader(fic):
    file = []
    for line in fic:
        line = line.split("=")
        line[1] = line[1].replace("\n", "")
        file.append(line)
    fic.close()
    return file


def replaceCharacters(fileProperties, fileInput):
    for character in fileProperties:
        fileInput = fileInput.replace(character[0], character[1])

    return fileInput


def transform():
    fileProperties = []
    translator = Translator()
    fileInput = inputText.get("1.0", "end")

    fic = open("format.propierties", "r", encoding="utf8")
    fileProperties = fileReader(fic)

    fileOutput = replaceCharacters(fileProperties, fileInput)

    outputText.configure(state="normal")
    outputText.delete(1.0, END)
    outputText.insert(1.0, fileOutput)
    outputText.configure(state="disabled")

    fileInputTranslated = translator.translate(fileInput, src="es", dest="ca").text

    fileOutputAnotherLenguaje = replaceCharacters(fileProperties, fileInputTranslated)

    outputTextAnotherLenguaje.configure(state="normal")
    outputTextAnotherLenguaje.delete(1.0, END)
    outputTextAnotherLenguaje.insert(1.0, fileOutputAnotherLenguaje)
    outputTextAnotherLenguaje.configure(state="disabled")


root = Tk()

root.resizable(False, False)

mainFrame = Frame(root)
leftFrame = Frame(mainFrame, width=300, height=150)
rightFrame = Frame(mainFrame, width=300, height=150)

labelInputText = Label(leftFrame, text="Texto en español a convertir")
inputText = Text(leftFrame, width=50, height=51.5)
scrollYInputText = Scrollbar(leftFrame, command=inputText.yview)
inputText.config(yscrollcommand=scrollYInputText.set)

labelOutputText = Label(rightFrame, text="Texto en español convertido")
outputText = Text(rightFrame, width=50, height=25, background="#eeebe9")
outputText.configure(state="disabled")
scrollYOutputText = Scrollbar(rightFrame, command=outputText.yview)
outputText.config(yscrollcommand=scrollYOutputText.set)

labelOutputTextAnotherLenguaje = Label(rightFrame, text="Texto en catalan convertido")
outputTextAnotherLenguaje = Text(rightFrame, width=50, height=25, background="#eeebe9")
outputTextAnotherLenguaje.configure(state="disabled")
scrollYOutputTextAnotherLenguaje = Scrollbar(rightFrame, command=outputTextAnotherLenguaje.yview)
outputTextAnotherLenguaje.config(yscrollcommand=scrollYOutputTextAnotherLenguaje.set)

tranformButton = Button(root, text="transform", command=transform)

mainFrame.grid(column=0, row=0)

leftFrame.grid(column=0, row =0, rowspan=2)
labelInputText.grid(column=0, row=0)
inputText.grid(row=1, column=0)
scrollYInputText.grid(row=1, column=1, sticky="nsew")

rightFrame.grid(column=1, row =0)
labelOutputText.grid(column=0, row=0)
outputText.grid(row=1, column=0)
scrollYOutputText.grid(row=1, column=1, sticky="nsew")

labelOutputTextAnotherLenguaje.grid(column=0, row=2)
outputTextAnotherLenguaje.grid(row=3, column=0)
scrollYOutputTextAnotherLenguaje.grid(row=3, column=1, sticky="nsew")

mainFrame.pack()
tranformButton.pack()

root.mainloop()
