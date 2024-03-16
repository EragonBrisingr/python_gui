from tkinter import *

window = Tk()

window.geometry("400x200")

window.title("GUI")


greeting = Label(
    text="Welcome to python gui!",
    foreground="green",
    background="black",
    height=5,
    width=20
)
greeting.pack()

button = Button(
    text="Click me for coins!",
    width=20,
    height=5,
    bg="red",
    fg="white"
)
button.pack()



# Button function
def printButton():
    input = entry.get()
    lbl.config(text="Provided Input: " + input)

# Label
label = Label(window, text="Enter your name here (optional)")
label.pack()

# Text box
entry = Entry(
    window,
    width=50,
    borderwidth=1
)
entry.pack()

# Button creation
txtBtn = Button(
    window,
    text="Print",
    command = printButton
)
txtBtn.pack()

# Output label
lbl = Label(
    window,
    text=""
)
lbl.pack()














window.mainloop()




