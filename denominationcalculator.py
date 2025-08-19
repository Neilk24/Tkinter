from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='Blue')
root.geometry('650x400')

upload = Image.open('download.jpg')
upload = upload.resize((300, 300))

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg = 'Blue')
label.place(x=180, y=20)

label1 = Label(root, text = 'Hey user! Welcome to denomination calculator.', bg = 'Blue')
label1.place(relx = 0.5, y = 340, anchor = CENTER)

def topwin():
    top = Toplevel()
    top.title('Denomination Claculator')
    top.configure('light grey')
    top.geometry('600x450')

    label2 = Label(top, text = 'Enter your amount: ', bg = 'light grey')
    label2.place(x=230, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    def calculate():
        global amount
        amount = int(entry.get())
        note2000 = amount//2000
        amount%=2000
        note500 = amount//500
        amount%=500
        note200 = amount//200

        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)

        entry1.insert(END, note2000)
        entry2.insert(END, note500)
        entry3.insert(END, note200)


    button = Button(top, text='Calculator', command=calculate, bg = 'Brown', fg = 'White')
    button.place(x=240, y=120)

    label3 = Label(top, text='Here is the number of notes', bg = 'light grey')
    label4 = Label(top, text = '2000', bg = 'light grey')
    label5 = Label(top, text = '2000', bg = 'light grey')
    label6 = Label(top, text = '2000', bg = 'light grey')

    label3.place(x=140, y=170)
    label4.place(x=180, y=200)
    label5.place(x=180, y=230)
    label6.place(x=180, y=260)

    entry1 = Entry(top)
    entry2 = Entry(top)
    entry3 = Entry(top)

    entry1.place(x=270, y=200)
    entry2.place(x=270, y=230)
    entry3.place(x=270, y=260)


def message():
    msgbox = messagebox.showinfo('Alert', 'Do you want to calculate?')
    if msgbox=='ok':
        topwin()

button1 = Button(root, text = "Let's get started", command = message, bg = 'Brown', fg = 'White')
button1.place(x = 260, y = 360)

root.mainloop()