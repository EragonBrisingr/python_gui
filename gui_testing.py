from tkinter import *
#creating the window
window = Tk()

window.geometry("400x400")

window.title("GUI")

cookies = 0
#cookie function
def cookie():
    global cookies
    cookies += 1
    cookieNum.config(text="Number of cookies: " + str(cookies)) #important line to update the label

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

#display cookie number
cookieNum = Label(
    window,
    text = "Number of cookies: " + str(cookies)
)
cookieNum.pack()



#save button
saveMe = Button(
    window,
    height = 5,
    width = 5,
    borderwidth=2,
    text="Save"#,
    #command = save
)


window.mainloop()