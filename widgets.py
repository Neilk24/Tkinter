from tkinter import *

root = Tk()

root.title('Getting started with Tkinter widgets!')
root.geometry('500x400')
label = Label(text='Hello', fg='white', bg='black', width=400, height=1)
label.pack()

name_label = Label(text='Enter your name!', fg='yellow', bg='green')
name_label.pack()

entry = Entry()
entry.pack()

def greeting():
    name = entry.get()
    message = 'Welcome to my window '+name+'!'
    textbox.insert(END, message)

button = Button(text='Click me!', fg='white', bg='red', command=greeting)
button.pack()

textbox = Text()
textbox.pack()

root.mainloop()