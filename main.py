from tkinter import *


def add_numbers():
    a = int(entry1.get()) + int(entry2.get())
    myText.set(a)


master = Tk()
myText = StringVar()
Label(master, text="Please enter first number:").grid(row=0, sticky=W)
Label(master, text="Please enter second number:").grid(row=1, sticky=W)
Label(master, text="Answer:").grid(row=3, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

entry1 = Entry(master)
entry2 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button = Button(master, text="Add", command=add_numbers)
button.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W + E + N + S, padx=5, pady=5)


def delete():
    entry1.delete(0, END)
    entry2.delete(0, END)


clear = Button(master, text="Clear", command=delete)
clear.grid(row=4, column=2, columnspan=1, rowspan=1, sticky=W + E + N + S, padx=5, pady=5)


def _exit():
    return master.destroy


x = Button(master, text="Exit", command=master.destroy)
x.grid(row=4, column=6, columnspan=1, rowspan=1, sticky=W + E + N + S, padx=5, pady=5)


def multiply():
    a = int(entry1.get()) * int(entry2.get())
    myText.set(a)


times = Button(master, text="Multiply", command=multiply)
times.grid(row=4, column=3, columnspan=1, rowspan=1, sticky=W + E + S, padx=5, pady=5)


def divide():
    a = int(entry1.get()) // int(entry2.get())
    myText.set(a)


divide = Button(master, text="divide", command=divide)
divide.grid(row=4, column=4, columnspan=1, rowspan=1, sticky=W + E + S, padx=5, pady=5)


def power():
    a = int(entry1.get()) ** int(entry2.get())
    myText.set(a)


divide = Button(master, text="Power", command=power)
divide.grid(row=4, column=5, columnspan=1, rowspan=1, sticky=W + E + S, padx=5, pady=5)

mainloop()
