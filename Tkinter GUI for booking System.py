
from tkinter import *
from tkinter.ttk import Combobox

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

    def s1ToS2():

        home_frame.destroy()

        showTime_frame = showingTimes()

        showTime_frame.pack(fill="both", expand=True)


    Submitbtn = Button(frame, text = 'Submit', command = s1ToS2)
    Submitbtn.pack(pady=30)





    return frame

 

def showingTimes():
    
    showTime_frame = Frame(root)

    showTime_frame = Frame(root, width=1000, height=500, bg='blue')

    
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)
    #frame.pack(fill=NONE, expand=0)


     # Create the heading label
    heading_label = Label(showTime_frame, text="Showing Times",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)


    # Create the movie buttons
    for i in range(3):
        movie_button = Button(showTime_frame, text=f"Time Slot {i+1}",font=("Ariel", 10), height=1, width=30)
        movie_button.pack(pady=5)

    '''
    #create back button to go back to the previous screen needs to be called within each screen function
    def back():
            showTime_frame.destroy()
            home_frame = movieSelect()
            home_frame.pack(fill=NONE, expand=0)
    backBtn =Button(showTime_frame, text='Back', font=('Arial', 25), command=back)
    backBtn.pack(pady=10)
    
    #Back button currently has errors relating to not unpacking the previous screen and also packing the 
    backBtn each time the backBtn is pressed
    '''


    def s2ToS3():

        showTime_frame.destroy()

        seatSelect_frame = seatSelect()
        seatSelect_frame.pack(fill=NONE, expand=0)

    
    Submitbtn = Button(showTime_frame, text = 'Submit', command = s2ToS3)
    Submitbtn.pack(pady=30)


    return showTime_frame


def seatSelect():

    
    seatSelect_frame = Frame(root)


    seatSelect_frame = Frame(root, width=1000, height=500, bg='green')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

    # Create the heading label
    heading_label = Label(seatSelect_frame, text="Seat Selection",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    # Adding a title to the window
    #title_label = Label(frame, text="Seat Selection", font=("Helvetica", 18, "bold"))
    #title_label.pack(pady=(0, 20))
    

    # Adding an image to the window
    seat_image = PhotoImage(file="cinemaSeats.png")
    image_label = Label(seatSelect_frame, image=seat_image)
    image_label.pack()

    # Adding a label for seat selection
    select_label = Label(seatSelect_frame, text="Select a seat:", font=("Helvetica", 12))
    select_label.pack(pady=(20, 10))

    # Adding a dropdown menu for seat selection
    seat_options = [str(i) for i in range(1, 21)]
    selected_seat = StringVar()
    selected_seat.set(seat_options[0])
    seat_dropdown = Combobox(seatSelect_frame, textvariable=selected_seat, values=seat_options,
                                          state="readonly")
    seat_dropdown.pack()
    
    '''
    #This code block doesn't work it just displays you have selected seat 1 constantly 


     #Adding a label for displaying seat selection message
    message_label = Label(seatSelect_frame, text="", font=("Helvetica", 12))
    message_label.pack(pady=10)
    def display_choosen_seat():
    # Retrieving the selected seat
        choosen_seat = selected_seat.get()
    # Updating the message label with the selected seat number
        message = f"You have selected seat {choosen_seat}"
        message_label.config(text=message)
    '''

    def s3ToS4():

        seatSelect_frame.destroy()

        confirmPage_frame = confirmPage()
        confirmPage_frame.pack(fill=NONE, expand=0)

    
    #Submitbtn = Button(seatSelect_frame, text = 'Submit', command=lambda: [s3ToS4(), submit_seat_selection()])
    Submitbtn = Button(seatSelect_frame, text = 'Submit', command= s3ToS4) 
    Submitbtn.pack(pady=30)

   

   
    
    return seatSelect_frame


def confirmPage():

    confirmPage_frame = Frame(root)


    confirmPage_frame = Frame(root, width=1000, height=500, bg='purple')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

    # Create the heading label
    heading_label = Label(confirmPage_frame, text="Confirmation Page",height=1, width=80, font=("Ariel", 12))
    heading_label.grid(row=0, column=1, sticky="news", padx=0, pady=0)


    listBox = Listbox(confirmPage_frame, width=80, height=12)
    listBox.grid(row=1, column=1, sticky="news", padx=20, pady=10)


    user_info_LabelFrame =LabelFrame(confirmPage_frame, text ="Customer Information")
    user_info_LabelFrame.grid(row=2, column=1, padx =20, pady = 10)

    title_label = Label(user_info_LabelFrame , text="Title")
    title_combobox = Combobox(user_info_LabelFrame , values=["", "Mr.","Miss", "Ms", "Mrs.","Dr.","Master"])

    title_label.grid(row=0, column=0)
    title_combobox.grid(row=1, column =0)


    first_name_label =Label(user_info_LabelFrame , text ="First Name")
    first_name_label.grid(row=0, column=1)
    last_name_label = Label(user_info_LabelFrame , text ="Last Name")
    last_name_label.grid(row=0, column=2)

    first_name_entry= Entry(user_info_LabelFrame )
    last_name_entry = Entry(user_info_LabelFrame )

    first_name_entry.grid(row=1, column=1,)
    last_name_entry.grid(row =1, column =2)



    age_label = Label(user_info_LabelFrame , text ="Age")
    age_spinbox =Spinbox(user_info_LabelFrame , from_=12, to =150)

    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column =0)

    sex_label= Label(user_info_LabelFrame , text = "Sex")
    sex_combobox =Combobox(user_info_LabelFrame , values=["Male","Female"])

    sex_label.grid(row=2, column= 1)
    sex_combobox.grid(row=3, column=1)


    email_label =Label(user_info_LabelFrame , text ="Email Address")
    email_label.grid(row=2, column=2,)

    email_entry= Entry(user_info_LabelFrame )
    email_entry.grid(row=3, column=2,)


    for widget in user_info_LabelFrame .winfo_children():
        widget.grid_configure(padx=10,pady=5)


    def enter_data():

        print(title_combobox.get(), first_name_entry.get(), last_name_entry.get(), age_spinbox.get(), email_entry.get())

    button =Button(confirmPage_frame, text="Submit" , command= enter_data)
    button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

    return confirmPage_frame
 

 

root = Tk()

root.minsize(height=500, width=1000)

home_frame = movieSelect()

home_frame.pack(fill=NONE, expand=0)

root.mainloop()
