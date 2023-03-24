import tkinter
from tkinter import ttk

def enter_data():
    first_name_label = first_name_entry.get()
    last_name_label = last_name_entry.get()
    age_label = age_spinbox.get()
    title_label = title_combobox.get()
    email_label = email_entry.get()
  
    
    
    print(title_label, first_name_label , last_name_label, age_label, email_label)

window = tkinter.Tk()
window.title("Booking Confirmation")
frame =tkinter.Frame(window)
frame.pack()


#saving user info



#saving user info
# Listbox to display outputs from users searches 

# Listbox to display outputs from users searches 


listBox = tkinter.Listbox(frame, width=80, height=12)
listBox.grid(row=0, column=1, sticky="news", padx=20, pady=10)


user_info_LabelFrame =tkinter.LabelFrame(frame, text ="Customer Information")
user_info_LabelFrame .grid(row=1, column=1, padx =20, pady = 10)

title_label = tkinter.Label(user_info_LabelFrame , text="Title")
title_combobox = ttk.Combobox(user_info_LabelFrame , values=["", "Mr.","Miss", "Ms", "Mrs.","Dr.","Master"])

title_label.grid(row=0, column=0)
title_combobox.grid(row=1, column =0)


first_name_label =tkinter.Label(user_info_LabelFrame , text ="First Name")
first_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(user_info_LabelFrame , text ="Last Name")
last_name_label.grid(row=0, column=2)

first_name_entry= tkinter.Entry(user_info_LabelFrame )
last_name_entry = tkinter.Entry(user_info_LabelFrame )

first_name_entry.grid(row=1, column=1,)
last_name_entry.grid(row =1, column =2)



age_label = tkinter.Label(user_info_LabelFrame , text ="Age")
age_spinbox =tkinter.Spinbox(user_info_LabelFrame , from_=12, to =150)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column =0)

sex_label= tkinter.Label(user_info_LabelFrame , text = "Sex")
sex_combobox =ttk.Combobox(user_info_LabelFrame , values=["Male","Female"])

sex_label.grid(row=2, column= 1)
sex_combobox.grid(row=3, column=1)


email_label =tkinter.Label(user_info_LabelFrame , text ="Email Address")
email_label.grid(row=2, column=2,)

email_entry= tkinter.Entry(user_info_LabelFrame )
email_entry.grid(row=3, column=2,)


for widget in user_info_LabelFrame .winfo_children():
    widget.grid_configure(padx=10,pady=5)



button =tkinter.Button(frame, text="Submit" , command= enter_data)
button.grid(row=3, column=1, sticky="news", padx=20, pady=10)



window.mainloop()