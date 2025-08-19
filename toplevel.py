from tkinter import *

root = Tk()
root.title('Top level window')
root.geometry('500x500')

def topwin():
    top = Toplevel()
    top.title('Inner window')
    top.geometry('200x200')

    label1 = Label(top, text='This is a top level window')
    label1.pack()

    top.mainloop()

label = Label(root, text='This is the main window')
label.pack()
button = Button(root, text='Click me!', command=topwin)
button.pack()

root.mainloop()