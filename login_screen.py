from tkinter import *

root = Tk()
root.title('Login Screen')
root.geometry('400x400')

frame = Frame(master = root, height = 200, width = 360, bg = 'Cyan')
frame.place(x=20, y=0)

label1 = Label(frame, text = 'Full Name: ', bg = 'White', fg = 'Blue', width = 12)
label1.place(x=20, y=20)
entry1 = Entry(frame)
entry1.place(x=150, y=20)

label2 = Label(frame, text = 'eMail: ', bg = 'White', fg = 'Blue', width = 12)
label2.place(x=20, y=80)
entry2 = Entry(frame)
entry2.place(x=150, y=80)

label3 = Label(frame, text = 'Password: ', bg = 'White', fg = 'Blue', width = 12)
label3.place(x=20, y=140)
entry3 = Entry(frame)
entry3.place(x=150, y=140)

def display():
    name = entry1.get()
    greeting = 'Hello' + name
    msg = '\nCongratulations! Your account has been created'
    textbox.insert(END, greeting)
    textbox.insert(END, msg)
    
button = Button(text = 'Create Your New Account!', bg = 'red', command = display)
button.place(x=130, y=200)
textbox = Text(bg = 'gray', fg = 'black')
textbox.place(y=250)

root.mainloop()