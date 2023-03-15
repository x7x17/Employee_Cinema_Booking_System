
# Dictionary to store movies
#Rather than hard coding we should import by CSV 
import csv

available_seats = []
booked_seats = []
customer_order = []
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
                v=[row[1],row[2],row[3],row[4],row[5],[row[6],row[7],row[8]]]
                movieDict[k]=v
            counter += 1     
        return movieDict
      
def show_movie(movieDict):
    print('ID','Movie title')
    for k,v in movieDict.items():
        print(k,v[0])          


def check_showtime(movieDict):
    response1 = input('please key in the ID of the movie: ')
    print('time ID  |Time')
    for i in range(3):
        print(i+1,'       |',movieDict[response1][5][i])
        
      
    
 import tkinter as tk
from tkinter import ttk


class CinemaSeatSelection:
    def __init__(self, master):
        self.master = master
        self.master.title("Cinema Seat Selection")
        self.master.geometry("2500x1800")

        # Creating a frame to hold the widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Adding a title to the window
        self.title_label = tk.Label(self.frame, text="Cinema Seat Selection", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=(0, 20))

        # Adding an image to the window
        self.seat_image = tk.PhotoImage(file="cinemaSeats2.png")
        self.image_label = tk.Label(self.frame, image=self.seat_image)
        self.image_label.pack()

        # Adding a label for seat selection
        self.select_label = tk.Label(self.frame, text="Select a seat:", font=("Helvetica", 12))
        self.select_label.pack(pady=(20, 10))

        # Adding a dropdown menu for seat selection
        self.seat_options = [str(i) for i in range(1, 21)]
        self.selected_seat = tk.StringVar()
        self.selected_seat.set(self.seat_options[0])
        self.seat_dropdown = ttk.Combobox(self.frame, textvariable=self.selected_seat, values=self.seat_options,
                                          state="readonly")
        self.seat_dropdown.pack()

        # Adding a button to submit the seat selection
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_seat_selection)
        self.submit_button.pack(pady=20)

        # Adding a label for displaying seat selection message
        self.message_label = tk.Label(self.frame, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=10)

    def submit_seat_selection(self):
        # Retrieving the selected seat
        selected_seat = self.selected_seat.get()

        # Updating the message label with the selected seat number
        message = f"You have selected seat {selected_seat}"
        self.message_label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CinemaSeatSelection(root)
    root.mainloop()
    
        
    response2 = int(input('please key in the time ID:'))-1

    print('you have selected to watch a ',movieDict[response1][0], ' at the following time: ',movieDict[response1][5][response2])
    customer_order.append(response1)
    customer_order.append(movieDict[response1][0])
    
    customer_order.append(movieDict[response1][5][response2])
def select_seat(booked_seats):
    print('please select a seat from the following ID')
    for i in available_seats:
        print(i)
    response3 = int(input('key in the seat number here: '))
    if response3 not in booked_seats:
        print(response3, 'selected')
        booked_seats.append(response3)
        customer_order.append(response3)
    else:
        print('seat occuppied')
    return booked_seats


a = read_csv("Software Engineering - Movie List.csv")
show_movie(a)
check_showtime(a)
booked_seats = select_seat(booked_seats)
print(customer_order)
