import tkinter as tk
from tkinter import ttk


class CinemaSeatSelection:
    def __init__(self, master):
        self.master = master
        self.master.title("Cinema Seat Selection")
        self.master.geometry("500x400")

        # Creating a frame to hold the widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Adding a title to the window
        self.title_label = tk.Label(self.frame, text="Cinema Seat Selection", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=(0, 20))

        # Adding an image to the window
        self.seat_image = tk.PhotoImage(file="Image.png")
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
