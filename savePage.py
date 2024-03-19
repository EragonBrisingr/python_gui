import os
from tkinter import *
from pathlib import Path

class SaveMe():

    def __init__(self, cookies):
        self.score = cookies

    def run(self):
        self.win = Tk()
        self.win.geometry("200x300")
        self.win.title("Save score")
        self.cBtn()
        self.showS()
        self.entryN()

    def showS(self):
        scr = Label(
            self.win,
            text = "Your score is: " + str(self.score)
        )
        scr.pack()

    def cBtn(self):
        self.memo = Button(
            self.win,
            height=10,
            width=20,
            text = "save",
            command = self.svFile
        )
        self.memo.pack()

    def entryN(self):
        self.ent = Entry(
            self.win,
            text = "Your name"
        )
        self.ent.pack()

    def errName(self):
        err = Label(
            self.win,
            height = 3,
            width = 5,
            text = "Name taken, please enter another one"
        )
        err.pack()

    def svFile(self):
        name = self.ent.get().lower()
        fileName = "scores.txt"

        if(name not in fileName):
            score = {
                name: self.score
            }
            with open(fileName, 'a') as f:
                f.write(str(score) + '\n', )
        else: self.errName()


