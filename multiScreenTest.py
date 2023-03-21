from tkinter import *

root =Tk()
root.geometry('500x250')

def main():
    frame = Frame(root, width=500, height=250, bg='black')
    frame.place(x=0, y=0)

    btn1 = Button(frame, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame, text='Time Selection', command=screen1)
    btn2.place(x=10, y=40)

    btn3 = Button(frame, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)


def screen1():
    frame1 = Frame(root, width=500, height=250, bg='red')
    frame1.place(x=0, y=0)

    btn1 = Button(frame1, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame1, text='Time Selection', command=screen1 )
    btn2.place(x=10, y=40)

    btn3 = Button(frame1, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)

def screen2():
    frame2 = Frame(root, width=500, height=250, bg='blue')
    frame2.place(x=0, y=0)

    btn1 = Button(frame2, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame2, text='Time Selection', command=screen1 )
    btn2.place(x=10, y=40)

    btn3 = Button(frame2, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)




main()
screen1()
screen2()



root.mainloop()