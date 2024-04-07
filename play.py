from tkinter import *
from savePage import SaveMe
from loadPage import LoadMe

#creating the window
window = Tk()

window.geometry("400x400")

window.title("GUI")

cookies :int = 0
add = 1
cost = 50



#cookie function
def cookie():
    global cookies
    cookies += add
    cookieNum.config(text="Number of cookies: " + str(round(cookies))) #important line to update the label

# cookie clicker
heroBtn = Button(
    window,
    text = "Click me for cookies",
    height=10,
    width=20,
    borderwidth=4,
    bg = "lightblue",
    command = cookie
)
heroBtn.pack()

#more cookies per click
def moreCookies():
    global add
    global cost
    global cookies
    if(cookies>=cost):
        cookies-=cost
        
        add += 1
        cost*=1.3
        cookieNum.config(text="Number of cookies: " + str(round(cookies)))

incCookies = Button(
    window,
    text="double cc",
    bg = "cyan",
    command = moreCookies
)
incCookies.pack()

#display cookie number
cookieNum = Label(
    window,
    text = "Number of cookies: " + str(round(cookies))
)
cookieNum.pack()

#initiating the save gui
def save():
    global cookies
    global add
    sv = SaveMe(cookies, add)
    sv.run()
    cookies = 0
    cookieNum.config(text="Number of cookies: " + str(round(cookies)))

#save button
saveMe = Button(
    window,
    height = 5,
    width = 5,
    borderwidth=2,
    text="Save",
    command = save
)
saveMe.pack(padx = 5, pady = 5)

#function sent to LoadMe class
def load():
    global cookies
    global add
    cookieNum.config(text="Number of cookies: " + str(ld.score))
    cookies = ld.score
    add = ld.cookiesClick

ld = LoadMe(load)

def loadFile():
    ld.run()

loadMe = Button(
    window,
    height = 5,
    width = 5,
    borderwidth=2,
    text="Load",
    command = loadFile
)
loadMe.pack()





















window.mainloop()



