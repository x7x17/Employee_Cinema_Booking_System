from tkinter import*
root=Tk()
root.minsize(height=500, width=1000)
def tab1():
    def tab2():
        label1.destroy()
        btn1.destroy()
        label2=Label(root,text='2nd Screen', font=('Arial', 25))
        label2.pack()
        #btn2=Button(root, text='Back', font=('Arial', 25), conmmand=back)
        #btn2.pack(side=BOTTOM)
        def back():
            label2.destroy()
            btn2.destroy()
            tab1()
        btn2=Button(root, text='Back', font=('Arial', 25), command=back)
        btn2.pack(side=BOTTOM)

    
    
    label1=Label(root,text='1st Screen', font=('Arial', 25))
    label1.pack()
    btn1=Button(root, text='NEXT', font=('Arial', 25), command=tab2, activebackground='blue')
    btn1.pack(side=BOTTOM)

tab1()
root.mainloop()