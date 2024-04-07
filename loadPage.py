import json
from tkinter import *



class LoadMe():

    def __init__(self, loadFn):
        self.loadFn = loadFn

    def run(self):
        self.win = Tk()
        self.win.geometry("300x200")
        self.win.title("Load Player")
        self.showS()
        self.loadName()
        self.loadBtn()

    def loadName(self):
        self.ent = Entry(
            self.win
        )
        self.ent.pack()
    
    def showS(self):
        scr = Label(
            self.win,
            width = 30,
            text = "Your name"
        )
        scr.pack()

    def loadBtn(self):
         ldBtn = Button(
            self.win,
            height=3,
            width=20,
            text = "load",
            bg = "lightblue",
            command = self.searchName
         )
         ldBtn.pack()

    def searchName(self):
        name = self.ent.get()
        scores = {}
        with open('scores.txt', 'r') as file:
                # Load the existing scores into a dictionary
                scores = json.load(file)
                
        if name in scores:
            self.cookiesClick = round(scores[name]['upgradeCookies'])
            self.score = round(scores[name]['score'])
            self.loadFn()
            self.win.destroy()
        else: pass #add an error message

