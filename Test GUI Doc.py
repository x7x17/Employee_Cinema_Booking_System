import tkinter as tk
from tkinter import *



customerOrder = []

customerOrder.append

window = tk.Tk()

window.title('Cinema Booking System')


Lb = Listbox(window)
Lb.insert(1, 'movieTitle1')
Lb.insert(2, 'movieTitle2')
Lb.insert(3, 'movieTitle3')
Lb.insert(4, 'movieTitle4')
Lb.insert(5, 'movieTitle5')
Lb.insert(6, 'movieTitle6')
Lb.insert(7, 'movieTitle7')
Lb.insert(8, 'movieTitle8')
Lb.insert(9, 'movieTitle9')
Lb.insert(10, 'movieTitle10')
Lb.pack()

'''
Label(window, text='First Name').grid(row=0)
Label(window, text='Last Name').grid(row=1)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

'''


window.mainloop()