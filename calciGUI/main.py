from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


window = Tk()
window.config()
window.title("Calculator")
window.geometry("300x400")

scvalue = StringVar()
screen = Entry(window, textvariable=scvalue, font=("arial", 35, "bold"))
screen.pack(fill=X, ipadx=7, pady=10, padx=7)

frame = Frame(window, bg="gray")
button = Button(frame, text="C", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text=".", font=("arial", 25))
button.pack(side=LEFT, padx=8, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="%", font=("arial", 25))
button.pack(side=LEFT, padx=8, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="/", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(window, bg="gray")
button = Button(frame, text="7", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="8", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="9", font=("arial", 25))
button.pack(side=LEFT, padx=8, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="*", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(window, bg="gray")
button = Button(frame, text="4", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="5", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="6", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="-", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(window, bg="gray")
button = Button(frame, text="1", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="2", font=("arial", 25))
button.pack(side=LEFT, padx=7, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="3", font=("arial", 25))
button.pack(side=LEFT, padx=9, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="+", font=("arial", 25))
button.pack(side=LEFT, padx=8, pady=10)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(window, bg="gray")
button = Button(frame, text="0", font=("arial", 25),width=11)
button.pack(side=LEFT, padx=6, pady=10)
button.bind("<Button-1>", click)

button = Button(frame, text="=", font=("arial", 25))
button.pack(side=LEFT, padx=7, pady=10)
button.bind("<Button-1>", click)
frame.pack()

window.mainloop()
