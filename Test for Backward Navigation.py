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

movieDict = {}

def read_csv(name):
    #movieDict = {}
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

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # create a container to hold all the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # create three frames
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start Page")
        label.pack(side="top", fill="x", pady=10)

        temp = []
        movie_options = []
        for k,v in movieDict.items():
            if v[0] not in temp:
                # print(v[0],v[1])   
                movie_list = tk.Label(self, text=f"{v[1]}",font=("Ariel", 10),height=1, width=70)
                movie_list.pack(pady=5)
                movie_options.append(v[1])
                temp.append(v[0])
        temp.clear()

        # Adding a dropdown menu for Movie selection
        selected_movie = StringVar()
        selected_movie.set(movie_options[0])
        movie_dropdown = Combobox(self, textvariable=selected_movie, values=movie_options, state="readonly")
        movie_dropdown.pack()

        # Dictionary to store movies
#Rather than hard coding we should import by CSV 
import csv

available_seats = []
customer_order = []
booked_seats = {}
order_history = {}
order_history[0] = ['Pretty Woman', '14/03/2023 17:30', '4', 'aa', 'aa', 'aa', 'aa', 'aa']

orderSummary = []

orderSummary.append("")

for i in range (21):
    available_seats.append(i)

movieDict = {}

def read_csv(name):
    #movieDict = {}
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

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # create a container to hold all the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # create three frames
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start Page")
        label.pack(side="top", fill="x", pady=10)

        temp = []
        movie_options = []
        for k,v in movieDict.items():
            if v[0] not in temp:
                # print(v[0],v[1])   
                movie_list = tk.Label(self, text=f"{v[1]}",font=("Ariel", 10),height=1, width=70)
                movie_list.pack(pady=5)
                movie_options.append(v[1])
                temp.append(v[0])
        temp.clear()

        # Adding a dropdown menu for Movie selection
        selected_movie = StringVar()
        selected_movie.set(movie_options[0])
        movie_dropdown = Combobox(self, textvariable=selected_movie, values=movie_options, state="readonly")
        movie_dropdown.pack()

        def s1ToS2(orderSummary):
            a = movie_dropdown.get()
            orderSummary.append(a)
            button1 = tk.Button(self, text="Go to Next Page ", 
                                command=lambda: controller.show_frame(PageOne))
            button1.pack()
        
            
            
            
        Submitbtn = Button(self, text = 'Submit', command = s1ToS2(orderSummary))
        Submitbtn.pack(pady=30)

       
        # Create the contact details button
        
        contact_num = Label(self, text="Phone Number: 0998393883939 \n Email: info.keelecinemahouse@keele.ac.uk",height=3, width=60, font=("Ariel", 9))
        contact_num.pack(pady=10) 

        
print(orderSummary)
   

        
      

       
            
            
       # button2 = tk.Button(self, text="Go to Page Two",
        #    command=lambda: controller.show_frame(PageTwo))
        #button2.pack()






class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page One")
        label.pack(side="top", fill="x", pady=10)

        
          # Create the heading label
        heading_label = Label(self, text="Showing Times",height=1, width=80, font=("Ariel", 12))
        heading_label.pack(pady=10)

        

        # Create the movie buttons
        timeSlotOptions = []
        for k,v in movieDict.items():
            if v[1] == orderSummary[0]:
                movie_button = Button(self, text=f"Time Slot {v[6]}",font=("Ariel", 10), height=1, width=30)
                movie_button.pack(pady=5)
                timeSlotOptions.append(v[6])


"""
         
        # Adding a dropdown menu for Time Slot selection
        selected_TimeSlot = StringVar()
        selected_TimeSlot.set(timeSlotOptions[0])
        timeSlot_dropdown = Combobox(self, textvariable=selected_TimeSlot, values=timeSlotOptions, state="readonly")
        timeSlot_dropdown.pack()


       #button1 = tk.Button(self, text="Go to Start Page",
        #                    command=lambda: controller.show_frame(StartPage))
        
        
        def s2ToS3():
            a = timeSlot_dropdown.get()
            orderSummary.append(a)

            button1 = tk.Button(self, text="Go to Next Page",
                            command=lambda: controller.show_frame(PageTwo))

            button1.pack()

   
        button2 = tk.Button(self, text="Go Back a Page",
                                command=lambda: controller.show_frame(StartPage))
        button2.pack()

        Submitbtn = Button(self, text = 'Submit', command = s2ToS3)
        Submitbtn.pack(pady=30)

"""  
        

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page Two")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Start Page",
                            command=lambda: controller.show_frame(StartPage))
        button2 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
        
            
  