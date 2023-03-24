from tkinter import*
root=Tk()
root.minsize(height=500, width=1000)
def tab1():
    def tab2():
        label1.destroy()
        btn1.destroy()
        label2=Label(root,text='2nd Screen', font=('Arial', 25))
        label2.pack()
        
        def back():
            label2.destroy()
            btn2.destroy()
            tab1()
        btn2=Button(root, text='Back', font=('Arial', 25), command=back)
        btn2.pack(side=BOTTOM)
        
        '''

        def tab3():
            label2.destroy()
            btn2.destroy()
            label3=Label(root,text='3rd Screen', font=('Arial', 25))
            label3.pack()

            def backToTab2():
                label3.destroy()
                btn3.destroy()
                tab2()
            btn4=Button(root, text='Back', font=('Arial', 25), command=backToTab2)
            btn4.pack(side=BOTTOM)
            

        btn3=Button(root, text='NEXT', font=('Arial', 25), command=tab3)
        btn3.pack(side=BOTTOM)


        def tab4():
            #label3.destroy()
            btn3.destroy()
            label4=Label(root,text='3rd Screen', font=('Arial', 25))
            label4.pack()

            def backToTab3():
                label4.destroy()
                btn5.destroy()
                tab3()
            btn6=Button(root, text='Back', font=('Arial', 25), command=backToTab3)
            btn6.pack(side=BOTTOM)
                    

        btn5=Button(root, text='NEXT', font=('Arial', 25), command=tab4)
        btn5.pack(side=BOTTOM)

        '''    

    
    label1=Label(root,text='1st Screen', font=('Arial', 25))
    label1.pack()
    btn1=Button(root, text='NEXT', font=('Arial', 25), command=tab2, activebackground='blue')
    btn1.pack(side=BOTTOM)

tab1()
root.mainloop()