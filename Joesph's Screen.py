import tkinter 


from tkinter import ttk
window =tkinter.Tk()

window.title("Showing time 1")

frame= tkinter.Frame(window)
head_frame =tkinter.Frame(window)
heading_lb = tkinter.Label(head_frame, text= "Movie Title From Previous Selection")


frame.pack()
#showing time 1

Showing_time_1_frame =tkinter.LabelFrame(frame, text="Showing time 1")
Showing_time_1_frame.grid(row=0, column=0, padx=20, pady=20)

Day_label= tkinter.Label(Showing_time_1_frame, text="Day")
Day_spinbox=tkinter.Spinbox(Showing_time_1_frame, values=["mon","tue","wed","thur","fri","sat","sun"])
Day_label.grid(row=0, column=0)
Day_spinbox.grid(row=1, column=0)

Time_label= tkinter.Label(Showing_time_1_frame, text="Time")
Time_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1,to=12)
Time_label.grid(row=0, column=1)
Time_spinbox.grid(row=1, column=1)

Theatre_No_label= tkinter.Label(Showing_time_1_frame, text="Theatre No")
Theatre_No_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1, to=4)
Theatre_No_label.grid(row=0, column=2)
Theatre_No_spinbox.grid(row=1, column=2)




window.title("Showing time 2")

frame= tkinter.Frame(window)

frame.pack()
#showing time 2

Showing_time_1_frame =tkinter.LabelFrame(frame, text="Showing time 2")
Showing_time_1_frame.grid(row=0, column=0, padx=20, pady=20)

Day_label= tkinter.Label(Showing_time_1_frame, text="Day")
Day_spinbox=tkinter.Spinbox(Showing_time_1_frame, values=["mon","tue","wed","thur","fri","sat","sun"])
Day_label.grid(row=0, column=0)
Day_spinbox.grid(row=1, column=0)

Time_label= tkinter.Label(Showing_time_1_frame, text="Time")
Time_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1,to=12)
Time_label.grid(row=0, column=1)
Time_spinbox.grid(row=1, column=1)

Theatre_No_label= tkinter.Label(Showing_time_1_frame, text="Theatre No")
Theatre_No_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1, to=4)
Theatre_No_label.grid(row=0, column=2)
Theatre_No_spinbox.grid(row=1, column=2)


window.title("Showing time 3")

frame= tkinter.Frame(window)

frame.pack()
#showing time 3

Showing_time_1_frame =tkinter.LabelFrame(frame, text="Showing time 3")
Showing_time_1_frame.grid(row=0, column=0, padx=20, pady=20)

Day_label= tkinter.Label(Showing_time_1_frame, text="Day")
Day_spinbox=tkinter.Spinbox(Showing_time_1_frame, values=["mon","tue","wed","thur","fri","sat","sun"])
Day_label.grid(row=0, column=0)
Day_spinbox.grid(row=1, column=0)

Time_label= tkinter.Label(Showing_time_1_frame, text="Time")
Time_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1,to=12)
Time_label.grid(row=0, column=1)
Time_spinbox.grid(row=1, column=1)

Theatre_No_label= tkinter.Label(Showing_time_1_frame, text="Theatre No")
Theatre_No_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1, to=4)
Theatre_No_label.grid(row=0, column=2)
Theatre_No_spinbox.grid(row=1, column=2)


window.title("Movie Title From Previous Selection")

frame= tkinter.Frame(window)

frame.pack()
#showing time 4

Showing_time_1_frame =tkinter.LabelFrame(frame, text="Showing time 4")
Showing_time_1_frame.grid(row=0, column=0, padx=20, pady=20)

Day_label= tkinter.Label(Showing_time_1_frame, text="Day")
Day_spinbox=tkinter.Spinbox(Showing_time_1_frame, values=["mon","tue","wed","thur","fri","sat","sun"])
Day_label.grid(row=0, column=0)
Day_spinbox.grid(row=1, column=0)

Time_label= tkinter.Label(Showing_time_1_frame, text="Time")
Time_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1,to=12)
Time_label.grid(row=0, column=1)
Time_spinbox.grid(row=1, column=1)

Theatre_No_label= tkinter.Label(Showing_time_1_frame, text="Theatre No")
Theatre_No_spinbox=tkinter.Spinbox(Showing_time_1_frame, from_=1, to=4)
Theatre_No_label.grid(row=0, column=2)
Theatre_No_spinbox.grid(row=1, column=2)









window.mainloop()
