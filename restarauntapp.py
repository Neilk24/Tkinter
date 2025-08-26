from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Restaraunt App')
root.geometry('800x800')

frame = Frame(master = root, height = 400, width = 500, bg='gray')
frame.place(x=200, y=200)

label = Label(text='Welcome to the restaraunt app!', fg='black', bg='Gray')
label.place(x=250, y=170)

menu = {'Pizza': 15, 
        'Burger' : 5, 
        'Fries' : 2, 
        'Sandwich': 7, 
        'Pasta': 12, 
        'Family (all)': 25}

entries = {}

for item, price in menu.items():
    row = Frame(frame)
    row.pack(fill='x', pady=5)

    label1 = Label(row, text=f'{item} (${price})', width=33, anchor='w')
    label1.pack(side='left')

    entry = Entry(row, width = 5)
    entry.pack(side='right')

    entries[item] = entry

def calculate():
    total = 0
    for item, entry in entries.items():
        quantity = int(entry.get())
        total+=quantity*menu[item]
    total_label.config(text=f'Total : ${total}')

def reset():
    for entry in entries.values():
        entry.delete(0, END)
    total_label.config(text='Total = $0')

def exit_app():
    frame.destroy()


button = Button(text = 'Calculate', command=calculate)
button.place(x=200, y=400)

button1=Button(text='Reset', command = reset)
button1.place(x=300, y=400)

button2=Button(text='Exit', command=exit_app)
button2.place(x=400, y=400)

total_label = Label(text='Total: $0')
total_label.pack(pady=10)

root.mainloop()