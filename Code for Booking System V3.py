
# Dictionary to store movies
#Rather than hard coding we should import by CSV 
import csv

available_seats = []
customer_order = []
booked_seats = {}
order_history = {}
order_history[0] = ['Pretty Woman', '14/03/2023 17:30', '4', 'aa', 'aa', 'aa', 'aa', 'aa']

orderSummary = []

for i in range (21):
    available_seats.append(i)



def read_csv(name):
    movieDict = {}
    with open(name, 'r', newline='') as file:
        csvreader = csv.reader(file)
        counter = 0
        for row in csvreader:
            if counter != 0:
                k = row[0]
                v=[row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
                movieDict[k]=v
            counter += 1     
        return movieDict
      


def check_showtime(movieDict):
    response1 = input('please key in the ID of the movie: ')
    print('time ID  |Time')
    for k,v in movieDict.items():
        if v[0] == response1:
            print(k,'       |',v[6])
            
    response2 = input('please key in the time ID:')
    print('you have selected to watch a ',movieDict[response2][1], ' at the following time: ',movieDict[response2][6])
    customer_order.append(response2)

def select_seat(booked_seats):
    
    print('please select a seat from the following ID')
    for i in available_seats:
        print(i)
    response3 = int(input('key in the seat number here: '))
    
    if customer_order[0] not in booked_seats:
        booked_seats_list = [response3]
        booked_seats[customer_order[0]] = booked_seats_list
        print('seat ',response3, ' booked successfully')  
    else:
        if response3 in booked_seats[customer_order[0]]:
            print('seat occupied')
        else:
            booked_seats[customer_order[0]].append(response3) 
            print('seat ',response3, ' booked successfully')         
            

#a = read_csv("Software Engineering - Movie List.csv")
movieDict = read_csv("Software Engineering - Movie List.csv")


from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox

def movieSelect():


    frame = Frame(root)

    frame = Frame(root, width=1000, height=500, bg='CadetBlue')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

     # Create the heading label
    heading_label = Label(frame, text="List of Movies",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    #create movie select buttons
    #movieDict = read_csv("Software Engineering - Movie List.csv")
    temp = []
    movie_options = []
    for k,v in movieDict.items():
        if v[0] not in temp:
           # print(v[0],v[1])   
            movie_list = Label(frame, text=f"{v[1]}",font=("Ariel", 10), height=1, width=70)
            movie_list.pack(pady=5)
            movie_options.append(v[1])
            temp.append(v[0])
    temp.clear()

    # Adding a dropdown menu for Movie selection
    selected_movie = StringVar()
    selected_movie.set(movie_options[0])
    movie_dropdown = Combobox(frame, textvariable=selected_movie, values=movie_options, state="readonly")
    movie_dropdown.pack()

    def s1ToS2():

        a =movie_dropdown.get()
        orderSummary.append(a)
        #print(orderSummary)
        home_frame.destroy()

        showTime_frame = showingTimes()

        showTime_frame.pack(fill="both", expand=True)

    


    '''
    # Create the movie buttons
    for i in range(10):
        movie_button = Button(frame, text=f"Movie {i+1}",font=("Ariel", 10), height=1, width=30)
        movie_button.pack(pady=5)
    '''
    # Create the contact details button
    contact_num = Label(frame, text="Phone Number: 0998393883939 \n Email: Vuecinema@xyz.com",height=3, width=60, font=("Ariel", 9))
    contact_num.pack(pady=10)


    Submitbtn = Button(frame, text = 'Submit', command = s1ToS2)
    Submitbtn.pack(pady=30)

    return frame

print(orderSummary)

def showingTimes():
    
    showTime_frame = Frame(root)

    showTime_frame = Frame(root, width=1000, height=500, bg='CadetBlue')

     # Create the heading label
    heading_label = Label(showTime_frame, text="Showing Times",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)


    # Create the movie buttons
    timeSlotOptions = []
    for k,v in movieDict.items():
        if v[1] == orderSummary[0]:
            movie_button = Button(showTime_frame, text=f"Time Slot {v[6]}",font=("Ariel", 10), height=1, width=30)
            movie_button.pack(pady=5)
            timeSlotOptions.append(v[6])

         
    # Adding a dropdown menu for Time Slot selection
    selected_TimeSlot = StringVar()
    selected_TimeSlot.set(timeSlotOptions[0])
    timeSlot_dropdown = Combobox(showTime_frame, textvariable=selected_TimeSlot, values=timeSlotOptions, state="readonly")
    timeSlot_dropdown.pack()


    #create back button to go back to the previous screen needs to be called within each screen function
    '''def back():
            showTime_frame.destroy()
            home_frame = movieSelect()
            home_frame.pack(fill=NONE, expand=0)
    backBtn =Button(showTime_frame, text='Back', font=('Arial', 25), command=back)
    backBtn.pack(pady=10)
    '''
    
    #Back button currently has errors relating to not unpacking the previous screen and also packing the 
    #backBtn each time the backBtn is pressed
    


    def s2ToS3():
        a = timeSlot_dropdown.get()
        orderSummary.append(a)

        showTime_frame.destroy()

        seatSelect_frame = seatSelect()
        seatSelect_frame.pack(fill=NONE, expand=0)

        #for loop to check if we are able to verfy the info selected by the user to the dictionary
        '''
        for k,v in movieDict.items():
            if v[1] == orderSummary[0] and v[6] == orderSummary[1]:
                print ('success')
        '''
    
    Submitbtn = Button(showTime_frame, text = 'Submit', command = s2ToS3)
    Submitbtn.pack(pady=30)


    def s2ToS1():
            
            
            showTime_frame.pack_forget()
            home_frame = movieSelect()

            home_frame.pack(fill=NONE, expand=0)
    
            
    Backbtn = Button(showTime_frame, text="Back", command= s2ToS1)
    Backbtn.pack()


    return showTime_frame


def seatSelect():

    
    seatSelect_frame = Frame(root)


    seatSelect_frame = Frame(root, width=1000, height=500, bg='CadetBlue')
    #frame.place(x=0, y=0)
    #frame.pack(fill="both", expand=True)

    # Create the heading label
    heading_label = Label(seatSelect_frame, text="Seat Selection",height=1, width=80, font=("Ariel", 12))
    heading_label.pack(pady=10)

    # Adding a title to the window
    

    # Adding an image to the window
    seat_image = PhotoImage(file="Image.png")
    image_label = Label(seatSelect_frame, image=seat_image)
    image_label.pack()

    # Adding a label for seat selection
    select_label = Label(seatSelect_frame, text="Select a seat:", font=("Helvetica", 12))
    select_label.pack(pady=(20, 10))

    # Adding a dropdown menu for seat selection
    occuppied_seat = []
    for k,v in order_history.items():
        if orderSummary[0] == v[0] and orderSummary[1] == v[1]:
            occuppied_seat.append (int(v[2]))
    print(occuppied_seat)
    seat_options = [str(i) for i in range(1, 21) if i not in occuppied_seat]
    occuppied_seat.clear()
    selected_seat = StringVar()
    selected_seat.set(seat_options[0])
    seat_dropdown = Combobox(seatSelect_frame, textvariable=selected_seat, values=seat_options, state="readonly")
    seat_dropdown.pack()
    
    
    #This code block doesn't work it just displays you have selected seat 1 constantly 

    '''
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

        a = seat_dropdown.get()
        orderSummary.append(a)
        
        seatSelect_frame.destroy()

        confirmPage_frame = confirmPage()
        confirmPage_frame.pack(fill=NONE, expand=0)

    
    #Submitbtn = Button(seatSelect_frame, text = 'Submit', command=lambda: [s3ToS4(), submit_seat_selection()])
    Submitbtn = Button(seatSelect_frame, text = 'Submit', command= s3ToS4) 
    Submitbtn.pack(pady=30)


    def s3ToS2():
            
            showingTimes_frame = showingTimes()
            seatSelect_frame.pack_forget()
            showingTimes_frame.pack(fill='both', expand=True)
    Backbtn = Button(seatSelect_frame, text="Back" , command= s3ToS2)
    Backbtn.pack()

   

   
    
    return seatSelect_frame


def confirmPage():

    confirmPage_frame = Frame(root)


    confirmPage_frame = Frame(root, width=1000, height=500, bg='CadetBlue')

    # Create the heading label
    heading_label = Label(confirmPage_frame, text="Confirmation Page",height=1, width=80, font=("Ariel", 12))
    heading_label.grid(row=0, column=1, sticky="news", padx=0, pady=0)


    listBox = Listbox(confirmPage_frame, width=80, height=12)
    index = tk.END
    listBox.insert(index,'Movie:'+orderSummary[0])
    listBox.insert(index,'Time: '+orderSummary[1])
    listBox.insert(index, 'Seat number: '+orderSummary[2])
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

        a = title_combobox.get()
        b= first_name_entry.get()
        c = last_name_entry.get()
        d= age_spinbox.get()
        e = email_entry.get()
        orderSummary.append(a)
        orderSummary.append(b)
        orderSummary.append(c)
        orderSummary.append(d)
        orderSummary.append(e)
        #print(orderSummary)

        order_history[len(order_history)] = orderSummary
        print(order_history)        
        orderSummary.clear()

    button =Button(confirmPage_frame, text="Submit" , command= enter_data)
    button.grid(row=3, column=1, sticky="news", padx=20, pady=10)


    def s4ToS3():
            
            seatSelect_frame = seatSelect()
            confirmPage_frame.pack_forget()
            seatSelect_frame.pack(fill='both', expand=True)
    Backbtn = Button(confirmPage_frame, text="Back" , command= s4ToS3)
    Backbtn.grid(row=3, column=2, sticky="news", padx=20, pady=10)

    return confirmPage_frame


# Create a new frame that displays the finally details alongside the price to pay and display payment details i..e paypal account or cash amount
#A button should be avaible to return the user to the home_frame
#def successScreen():

    
   


 

root = Tk()

root.minsize(height=500, width=1000)

home_frame = movieSelect()

home_frame.pack(fill=NONE, expand=0)

root.mainloop()