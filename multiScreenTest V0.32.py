




from tkinter import *
from tkinter.ttk import Combobox

def s1ToS2():

    home_frame.destroy()

    showTime_frame = showingTimes()

    showTime_frame.pack(fill="both", expand=True)



def s2ToS3():

    showTime_frame.destroy()

    seatSelect_frame = seatSelect()
    seatSelect_frame.pack(fill=NONE, expand=0)
    #seatSelect_frame.pack(fill="both", expand=True)
    

    

 

def movieSelect():


    frame = Frame(root)

    frame = Frame(root, width=1000, height=500, bg='red')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

     # Create the heading label
    heading_label = Label(frame, text="List of Movies",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    # Create the movie buttons
    for i in range(10):
        movie_button = Button(frame, text=f"Movie {i+1}",font=("Ariel", 10), height=1, width=30)
        movie_button.pack(pady=5)

    # Create the contact details button
    contact_button = Button(frame, text="Phone Number: 0998393883939 \n Email: Vuecinema@xyz.com",height=3, width=60, font=("Ariel", 9))
    contact_button.pack(pady=10)


    Submitbtn = Button(frame, text = 'Submit', command = s1ToS2)
    Submitbtn.pack(pady=30)





    return frame

 

def showingTimes():
    
    frame = Frame(root)

    frame = Frame(root, width=1000, height=500, bg='blue')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)
    #frame.pack(fill=NONE, expand=0)


     # Create the heading label
    heading_label = Label(frame, text="Showing Times",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)


    # Create the movie buttons
    for i in range(3):
        movie_button = Button(frame, text=f"Time Slot {i+1}",font=("Ariel", 10), height=1, width=30)
        movie_button.pack(pady=5)

    
    Submitbtn = Button(frame, text = 'Submit', command = s2ToS3)
    Submitbtn.pack(pady=30)

    return frame


def seatSelect():

    
    frame = Frame(root)


    frame = Frame(root, width=1000, height=500, bg='green')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

    # Create the heading label
    heading_label = Label(frame, text="Seat Selection",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    # Adding a title to the window
    #title_label = Label(frame, text="Seat Selection", font=("Helvetica", 18, "bold"))
    #title_label.pack(pady=(0, 20))
    

    # Adding an image to the window
    seat_image = PhotoImage(file="cinemaSeats.png")
    image_label = Label(frame, image=seat_image)
    image_label.pack()

    # Adding a label for seat selection
    select_label = Label(frame, text="Select a seat:", font=("Helvetica", 12))
    select_label.pack(pady=(20, 10))

    # Adding a dropdown menu for seat selection
    seat_options = [str(i) for i in range(1, 21)]
    selected_seat = StringVar()
    selected_seat.set(seat_options[0])
    seat_dropdown = Combobox(frame, textvariable=selected_seat, values=seat_options,
                                          state="readonly")
    seat_dropdown.pack()

    '''

    # Adding a button to submit the seat selection
    submit_button = Button(frame, text="Submit", command=submit_seat_selection)
    submit_button.pack(pady=20)

    # Adding a label for displaying seat selection message
    message_label = Label(frame, text="", font=("Helvetica", 12))
    message_label.pack(pady=10)

    def submit_seat_selection(self):
    # Retrieving the selected seat
        selected_seat = selected_seat.get()

    # Updating the message label with the selected seat number
    message = f"You have selected seat {selected_seat}"
    message_label.config(text=message)
    '''
    return frame



    
   # Submitbtn = Button(frame, text = 'Submit', command = s2ToS3)
    #Submitbtn.pack(pady=30)

 

 

root = Tk()

root.minsize(height=500, width=1000)




#root.wm_title('Matricula UTEC')

 

home_frame = movieSelect()

home_frame.pack(fill=NONE, expand=0)


showTime_frame = showingTimes()


seatSelect_frame = seatSelect()


#showTime_frame.pack(fill=NONE, expand=0)


root.mainloop()







#seatSelect_frame.pack(fill="both", expand=True)



'''


if __name__ == "__main__":
    root =Tk()
    root.geometry('1000x500')
    root.title('KEELE PICTURE HOUSE')
    root.iconbitmap('C:/Software Engineering/Employee_Cinema_Booking_System/Employee_Cinema_Booking_System/ico.ico')

def main():
    frame = Frame(root, width=1000, height=500, bg='black')
    frame.place(x=0, y=0)

    btn1 = Button(frame, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame, text='Time Selection', command=screen1)
    btn2.place(x=10, y=40)

    btn3 = Button(frame, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)

     # Create the heading label
    heading_label = Label(frame, text="List of Movies",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    # Create the movie buttons
    for i in range(10):
        movie_button = Button(frame, text=f"Movie {i+1}",font=("Ariel", 10), height=1, width=30)
        movie_button.pack(pady=5)

    # Create the contact details button
    contact_button = Button(frame, text="Phone Number: 0998393883939 \n Email: Vuecinema@xyz.com",height=3, width=60, font=("Ariel", 9))
    contact_button.pack(pady=10)



def screen1():
  
    frame1 = Frame(root, width=1000, height=500, bg='red')
    frame1.place(x=0, y=0)

    btn1 = Button(frame1, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame1, text='Time Selection', command=screen1 )
    btn2.place(x=10, y=40)

    btn3 = Button(frame1, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)


def screen2():
    frame2.destory()

    frame2 = Frame(root, width=1000, height=500, bg='blue')
    frame2.place(x=0, y=0)
    
    btn1 = Button(frame2, text='Home', command=main)
    btn1.place(x=10, y=10)

    btn2 = Button(frame2, text='Time Selection', command=screen1 )
    btn2.place(x=10, y=40)

    btn3 = Button(frame2, text='Seat Selection', command=screen2)
    btn3.place(x=10, y=70)

    
    # Creating a frame to hold the widgets
    

    # Adding a title to the window
    title_label = Label(frame2, text="Seat Selection", font=("Helvetica", 18, "bold"))
    title_label.pack(pady=(0, 20))
    

    # Adding an image to the window
    seat_image = PhotoImage(file="cinemaSeats.png")
    image_label = Label(frame2, image=seat_image)
    image_label.pack()

    # Adding a label for seat selection
    select_label = Label(frame2, text="Select a seat:", font=("Helvetica", 12))
    select_label.pack(pady=(20, 10))

    # Adding a dropdown menu for seat selection
    seat_options = [str(i) for i in range(1, 21)]
    selected_seat = StringVar()
    selected_seat.set(seat_options[0])
    seat_dropdown = Combobox(frame2, textvariable=selected_seat, values=seat_options,
                                          state="readonly")
    seat_dropdown.pack()

    # Adding a button to submit the seat selection
    submit_button = Button(frame2, text="Submit", command=submit_seat_selection)
    submit_button.pack(pady=20)

    # Adding a label for displaying seat selection message
    message_label = Label(frame2, text="", font=("Helvetica", 12))
    message_label.pack(pady=10)

def submit_seat_selection(self):
    # Retrieving the selected seat
    selected_seat = selected_seat.get()

    # Updating the message label with the selected seat number
    message = f"You have selected seat {selected_seat}"
    message_label.config(text=message)
    



   



main()



root.mainloop()

'''