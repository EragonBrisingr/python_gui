import os
from tkinter import *
import json

class SaveMe():

    def __init__(self, cookies, upgrade1):
        self.score = cookies
        self.ensure_file_exists()
        self.err = None
        self.upgradeCookies = upgrade1

    def ensure_file_exists(self):
        """Ensure the scores.txt file exists."""
        if not os.path.exists('scores.txt'):
            with open('scores.txt', 'w') as file:
                file.write('{}')

    #creating the window
    def run(self):
        self.win = Tk()
        self.win.geometry("300x200")
        self.win.title("Save score")
        self.showS()
        self.entryN()
        self.cBtn()

    #label showing the score
    def showS(self):
        scr = Label(
            self.win,
            width = 15,
            text = "Your score is: " + str(self.score)
        )
        scr.pack()

    #button to save
    def cBtn(self):
        self.memo = Button(
            self.win,
            height=3,
            width=20,
            text = "save",
            command = self.svFile,
            bg = "lightblue"
        )
        self.memo.pack()

    #entry for name
    def entryN(self):
        self.ent = Entry(
            self.win,
            text = "Your name"
        )
        self.ent.pack()


    def errName(self):

        confirm = Tk()
        confirm.geometry("200x200")
        confirm.title("Confirm")

        ask = Label(
            confirm,
            text = "Name taken, override data?"
        )
        ask.pack()

        def delFn():
            self.scores[self.name] = self.score
            with open('scores.txt', 'w') as file:
                # Write the updated dictionary back to the file as JSON
                json.dump(self.scores, file, indent=4)
            confirm.destroy()
            self.win.destroy()

        yesBtn = Button(
            confirm,
            text = "yes",
            bg = "lightblue",
            command=delFn
        )
        yesBtn.pack()

        noBtn = Button(
            confirm,
            text = "no",
            bg = "lightblue",
            command=self.svFile
        )
        noBtn.pack()



    def clearError(self):
        if self.err is not None:
            self.err.destroy()
            self.err = None
            self.errName()

    def svFile(self):
        self.name = self.ent.get().lower()

        try:
            with open('scores.txt', 'r') as file:
                # Load the existing scores into a dictionary
                self.scores = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty dictionary
            self.scores = {}
        except json.JSONDecodeError:
            # If the file is empty or contains invalid JSON, start fresh
            self.scores = {}
        self.upgrade1 = 1   
        if self.name not in self.scores:
            self.scores[self.name] = {'score': self.score, 'upgradeCookies': self.upgrade1}
            with open('scores.txt', 'w') as file:
                # Write the updated dictionary back to the file as JSON
                json.dump(self.scores, file, indent=4)
            self.win.destroy()

        else:
            self.errName()




