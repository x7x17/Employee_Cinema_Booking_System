import tkinter as tk

# Create the main window
root = tk.Tk()
# Create the title and icon for window
root.title('KEELE PICTURE HOUSE')
root.iconbitmap('C:/Software Engineering/Employee_Cinema_Booking_System/Employee_Cinema_Booking_System/ico.ico')


# Create the heading label
heading_label = tk.Label(root, text="List of Movies",height=1, width=80, font=("Ariel", 12))
heading_label.pack(pady=10)

# Create the movie buttons
for i in range(10):
    movie_button = tk.Button(root, text=f"Movie {i+1}",font=("Ariel", 10), height=1, width=30)
    movie_button.pack(pady=5)

# Create the contact details button
contact_button = tk.Button(root, text="Phone Number: 0998393883939 \n Email: Vuecinema@xyz.com",height=3, width=60, font=("Ariel", 9))
contact_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
