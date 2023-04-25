#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:47:14 2023

@author: jeffrey
"""
from datetime import datetime
import random
from fpdf import FPDF
import csv
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox




class Ticket(FPDF):

    def header(self):
        self.image('KeeleCinemaLogo.png', 5, 4, 30)
        
        #font
        self.set_font('times', 'BU', size=20)
        #Padding
        self.cell(60)
        #title
        self.cell(90, 10, 'Movie Ticket', border=1, ln=1, align='C')
        #line break
        self.ln(20)
        
    # page footer
    def footer(self):
            #set postion of the footer 
            self.set_y(-15)
            #set font
            self.set_font('times', 'I', size=12)
            #Page number
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C' )
   
    def printpdf (orderSummary):
        pdf = Ticket('P', 'mm', 'A4')
    
        #get total page numbers
        pdf.alias_nb_pages()
            
            #set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)
            
         ## add a blank page to the PDF doc
        pdf.add_page()
            
            ## set font of text
            # fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
            # 'B' - bold, 'U' - underlined, 'I' - italics, '' (regular), combination e.g. ('BU')
        pdf.set_font('times', 'B', 12)  
    
        #add Page Contents
        pdf.set_xy(20,40)
        pdf.cell(180, 10, 'Movie Title:', 1, 0, 'C')
        
        
        pdf.set_xy(20, 70)
        pdf.cell(50, 10, 'Showing Time:', 1, 0, 'C')
        pdf.cell(50, 10, 'Seat No:', 1, 0, 'C')
    
    
        pdf.set_xy(20, 100)
        pdf.cell(20, 10, 'Title:', 1, 0, 'C')
        pdf.cell(50, 10, 'FirstName:', 1, 0, 'C')
        pdf.cell(70, 10, 'LastName:', 1, 0, 'C')
    
    
        pdf.set_xy(20, 130)
        pdf.cell(20, 10, 'Age:', 1, 0, 'C')
        pdf.cell(20,10, 'Sex:', 1, 0, 'C')
        pdf.cell(100, 10, 'Email Address:', 1,0, 'C')

        #values for first table in PDF
        pdf.set_xy(20, 50)
    
        pdf.cell(180, 10, '%s' %orderSummary[0],2, 0, 'C')
        
        #values for second table in PDF       
        pdf.set_xy(20, 80)
        
        pdf.cell(50, 10, '%s' %orderSummary[1], 1, 0, 'C')
        pdf.cell(50, 10, '%s' %orderSummary[3], 1, 0, 'C')
        pdf.cell(-50)
        
        #values for second table in PDF       
        pdf.set_xy(20, 110) 
    
        pdf.cell(20, 10, '%s' %orderSummary[4], 1, 0, 'C')
        pdf.cell(50, 10, '%s' %orderSummary[5], 1, 0, 'C')
        pdf.cell(70, 10, '%s' %orderSummary[6], 1, 0, 'C')
        pdf.cell(-50)     
    
        #values for third table in PDF       
        pdf.set_xy(20, 140) 
        pdf.cell(20, 10, '%s' %orderSummary[7], 1, 0, 'C')
        pdf.cell(20, 10, '%s' %orderSummary[8], 1, 0, 'C')
        pdf.cell(100, 10, '%s' %orderSummary[9], 1, 0, 'C')
        pdf.cell(-50)       
    
        pdf.output('MovieTicket.pdf')
    
class movie_info ():
    def __init__(self):
        self.movieDict = self.read_csv("Software Engineering - Movie List.csv")
    
    def read_csv(self,name):
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
    
    def retrieve_movie (movieDict):
        temp = []
        movie_options = []
        for k,v in movieDict.items():
            if v[0] not in temp:
               # print(v[0],v[1])   
                movie_options.append(v[1])
                temp.append(v[0])
        temp.clear()
        return movie_options
    
    def retrieve_price (movieDict,orderSummary):
        movie_price = 0
        for k,v in movieDict.items():
            if v[1] == orderSummary[0]:
                movie_price = v[5]
                break
        return movie_price

class showtime():
    def retrieve_showtime (movieDict,orderSummary):
        movie_price = 0
        timeSlotOptions = []
        for k,v in movieDict.items():
            if v[1] == orderSummary[0]:
                timeSlotOptions.append(v[6])
                movie_price = v[5]
        return timeSlotOptions
    
class seat_availability ():
    def check_occuppied(order_history,orderSummary):
        occuppied_seat = []
        for k,v in order_history.items():
           if orderSummary[0] == v[0] and orderSummary[1] == v[1]:
              
                occuppied_seat.append (int(v[3]))
        return occuppied_seat
    
class booking ():
    def create_order_csv(order_history,orderSummary):
        order_history[len(order_history)] = orderSummary
        with open('order history.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([[key] + value for key, value in order_history.items()])
            
    def read_past_orders ():
    
        order_history = {}
        with open("order history.csv", 'r', newline='') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
    
                k = row[0]
                v=[row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]
                order_history[k]=v
              
            return order_history
        
    
class movie_system(movie_info, Ticket):
    
    def __init__ (self):
        super().__init__()
        self.customer_order = []
  
        self.order_history = booking.read_past_orders()
        
        #self.order_history[0] = ['Pretty Woman', '14/03/2023 17:30', '£7.50','4', 'Mrs', 'Alexis', 'Richardson', '37', 'Female', 'A.Richardson@gmail.com']
        #self.order_history[1] = ['Pretty Woman', '14/03/2023 17:30', '£7.50','1', 'Mrs', 'Alexis', 'Richardson', '37', 'Female', 'A.Richardson@gmail.com']
        self.orderSummary = []
        self.root = Tk()
        self.root.minsize(height=500, width=1000)
        self.home_frame = self.movieSelect()
        self.home_frame.pack(fill=NONE, expand=0)
        self.root.mainloop()
    
    def movieSelect(self):
        self.frame = Frame(self.root)
        self.frame = Frame(self.root, width=1000, height=500, bg='CadetBlue')
    
         # Create the heading label
        heading_label = Label(self.frame, text="List of Movies",height=1, width=80, font=("Ariel", 12))
        heading_label.pack(pady=10)
        #create movie select buttons
        movie_options = movie_info.retrieve_movie(self.movieDict)
        for i in movie_options:
            movie_list = Label(self.frame, text=f"{i}",font=("Ariel", 10), height=1, width=70)
            movie_list.pack(pady=5)
            
        # Adding a dropdown menu for Movie selection
        selected_movie = StringVar()
        selected_movie.set(movie_options[0])
        movie_dropdown = Combobox(self.frame, textvariable=selected_movie, values=movie_options, state="readonly")
        movie_dropdown.pack()
        def s1ToS2():
            #global orderSummary
            a = movie_dropdown.get()
            self.orderSummary.append(a)
            #print(orderSummary)
            showTime_frame = self.showingTimes()
            self.frame.destroy()
            showTime_frame.pack(fill="both", expand=True)        
        # Create the contact details button
        contact_num = Label(self.frame, text="Phone Number: 0998393883939 \n Email: info@Keelemoviehouse.co.uk",height=3, width=60, font=("Ariel", 9))
        contact_num.pack(pady=10)
    
    
        Submitbtn = Button(self.frame, text = 'Submit', command = s1ToS2)
        Submitbtn.pack(pady=30)
    
        return self.frame
            
    def showingTimes(self):
        showTime_frame = Frame(self.root)
        showTime_frame = Frame(self.root, width=1000, height=500, bg='CadetBlue')

         # Create the heading label
        heading_label = Label(showTime_frame, text="Showing Times",height=1, width=80, font=("Ariel", 12))
        heading_label.pack(pady=10)

        # Create the movie buttons
        timeSlotOptions = showtime.retrieve_showtime(self.movieDict,self.orderSummary)
        
        for i in range(len(timeSlotOptions)):
            movie_button = Button(showTime_frame, text=f"Time Slot {timeSlotOptions[i]}",font=("Ariel", 10), height=1, width=30)
            movie_button.pack(pady=5)
        
        # Adding a dropdown menu for Time Slot selection
        selected_TimeSlot = StringVar()
        selected_TimeSlot.set(timeSlotOptions[0])
        timeSlot_dropdown = Combobox(showTime_frame, textvariable=selected_TimeSlot, values=timeSlotOptions, state="readonly")
        timeSlot_dropdown.pack()

        def s2ToS3():
            a = timeSlot_dropdown.get()
            self.orderSummary.append(a)
            self.movie_price = movie_info.retrieve_price(self.movieDict, self.orderSummary)
            self.orderSummary.append(self.movie_price)
            showTime_frame.destroy()
            seatSelect_frame = self.seatSelect()
            seatSelect_frame.pack(fill=NONE, expand=0)
        
        Submitbtn = Button(showTime_frame, text = 'Submit', command = s2ToS3)
        Submitbtn.pack(pady=30)
        Backbtn = Button(showTime_frame, text="Back", command= self.restart_gui)
        Backbtn.pack()

        return showTime_frame
    
    def seatSelect(self):
  
        seatSelect_frame = Frame(self.root)
        seatSelect_frame = Frame(self.root, width=1000, height=500, bg='CadetBlue')

        # Create the heading label
        heading_label = Label(seatSelect_frame, text="Seat Selection",height=1, width=80, font=("Ariel", 12))
        heading_label.pack(pady=10)

        # Adding an image to the window
        seat_image = PhotoImage(file="image1.png")
        image_label = Label(seatSelect_frame, image=seat_image)
        image_label.image = seat_image
        image_label.pack()
     
        image_label.config(border=1, relief="solid")

        # Adding a label for seat selection
        select_label = Label(seatSelect_frame, text="Select a seat:", font=("Helvetica", 12))
        select_label.pack(pady=(20, 10))
        
        # Adding a dropdown menu for seat selection
        occuppied_seat = seat_availability.check_occuppied(self.order_history, self.orderSummary)
        seat_options = [str(i) for i in range(1, 21) if i not in occuppied_seat]
        occuppied_seat.clear()
        selected_seat = StringVar()
        selected_seat.set(seat_options[0])
        seat_dropdown = Combobox(seatSelect_frame, textvariable=selected_seat, values=seat_options, state="readonly")
        seat_dropdown.pack()
        

        def s3ToS4():
            a = seat_dropdown.get()
            self.orderSummary.append(a)
            seatSelect_frame.destroy()
            confirmPage_frame = self.confirmPage()
            confirmPage_frame.pack(fill=NONE, expand=0)

        
        #Submitbtn = Button(seatSelect_frame, text = 'Submit', command=lambda: [s3ToS4(), submit_seat_selection()])
        Submitbtn = Button(seatSelect_frame, text = 'Submit', command= s3ToS4) 
        Submitbtn.pack(pady=30)


        def s3ToS2():
        
                del self.orderSummary[1]
                showingTimes_frame = self.showingTimes()
                seatSelect_frame.pack_forget()
                showingTimes_frame.pack(fill='both', expand=True)
        Backbtn = Button(seatSelect_frame, text="Back" , command= s3ToS2)
        Backbtn.pack()
        return seatSelect_frame
    

    def confirmPage(self):
    
        confirmPage_frame = Frame(self.root)
        confirmPage_frame = Frame(self.root, width=1000, height=500, bg='CadetBlue')
    
        # Create the heading label
        heading_label = Label(confirmPage_frame, text="Confirmation Page",height=1, width=80, font=("Ariel", 12))
        heading_label.grid(row=0, column=1, sticky="news", padx=0, pady=0)
    
    
        listBox = Listbox(confirmPage_frame, width=80, height=12)
        index = tk.END
        listBox.insert(index,'Movie:'+self.orderSummary[0])
        listBox.insert(index,'Time: '+self.orderSummary[1])
        listBox.insert(index, 'Seat number: '+self.orderSummary[3])
        listBox.insert(index, 'Price: '+self.orderSummary[2])
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
                e = sex_combobox.get()
                f = email_entry.get()
                self.orderSummary.append(a)
                self.orderSummary.append(b)
                self.orderSummary.append(c)
                self.orderSummary.append(d)
                self.orderSummary.append(e)
                self.orderSummary.append(f)
                Ticket.printpdf(self.orderSummary)
            
                
               
                booking.create_order_csv(self.order_history,self.orderSummary)
                self.orderSummary.clear()
                
                confirmPage_frame.destroy()
    
                Summary_frame = self.Summary()
                Summary_frame.pack(fill=NONE, expand=0)
            
    
        button =Button(confirmPage_frame, text="Submit" , command= enter_data)
        button.grid(row=3, column=1, sticky="news", padx=20, pady=10)
    
    
    
        def s4ToS3():
                
                del self.orderSummary[2]
                
                seatSelect_frame = self.seatSelect()
                confirmPage_frame.pack_forget()
                seatSelect_frame.pack(fill='both', expand=True)
        Backbtn = Button(confirmPage_frame, text="Back" , command= s4ToS3)
        Backbtn.grid(row=3, column=2, sticky="news", padx=20, pady=10)
        
        
    
        return confirmPage_frame
    
    def Summary(self):

        Summary_frame = Frame(self.root)
        
        
        Summary_frame = Frame(self.root, width=1000, height=500, bg='CadetBlue')
        
        # Create the heading label
        heading_label = Label(Summary_frame, text="Order Confirmed",height=1, width=80, font=("Ariel", 12))
        heading_label.grid(row=0, column=1, sticky="news", padx=0, pady=0)
        
        
        listBox = Listbox(Summary_frame, width=80, height=12)
        index = tk.END


        current_date = datetime.now().strftime('%d/%m/%Y')

        date_label = Label(Summary_frame, text=f"Current date: {current_date}")
        date_label.grid(row=1, column=1, sticky="news", padx=20, pady=2)   
        
        font = ("Ariel", 12, "underline")
        
        pay_label = Label(Summary_frame, text="Please consult the pricing sheet for ticket pricing. Customers can pay cash or via PayPal/Bank Transfer. Payment Details below:", font=font)
        pay_label.grid(row=2, column=1, sticky="news", padx=20, pady=2)  
        
        blank_label = Label(Summary_frame, bg='CadetBlue')
        
        blank_label2 = Label(Summary_frame, bg='CadetBlue')
        
        
            # Generate fake bank details
        bank_name = "Keele Bank"
        account_number = ''.join(random.choices('0123456789', k=10))
        sort_code = '12-34-56'
        balance = round(random.uniform(500, 10000), 2)
        
        # Create labels for bank details
        bank_name_label = Label(Summary_frame, text="Bank Name:", font = ("Ariel", 12))
        bank_name_value = Label(Summary_frame, text=bank_name)
        
        account_number_label = Label(Summary_frame, text="Account Number:", font = ("Ariel", 12))
        account_number_value = Label(Summary_frame, text=account_number)
        
        sort_code_label = Label(Summary_frame, text="Sort Code:", font = ("Ariel", 12))
        sort_code_value = Label(Summary_frame, text=sort_code)
        
        # Add labels to the tkinter application using grid()
        bank_name_label.grid(row=3, column=1, sticky="news", padx=20)
        bank_name_value.grid(row=4, column=1, sticky="news", padx=20)
        
        blank_label.grid(row=5, column=1, sticky="news", pady=1)
        
        account_number_label.grid(row=6, column=1, sticky="news", padx=20)
        account_number_value.grid(row=7, column=1, sticky="news", padx=20)
        
        
        blank_label2.grid(row=8, column=1, sticky="news", pady=1)
        
        sort_code_label.grid(row=9, column=1, sticky="news", padx=20)
        sort_code_value.grid(row=10, column=1, sticky="news", padx=20)
        
    

        return Summary_frame
        
    def restart_gui(self):
        
        self.orderSummary.clear()
        
        # Destroy the existing root window
        self.root.destroy()
        # Create a new root window
        self.root = Tk()
        self.root.minsize(height=500, width=1000)
        # Reinitialize the home_frame
        self.home_frame = self.movieSelect()
        self.home_frame.pack(fill=NONE, expand=0)
        # Start the main event loop again
       
        self.root.mainloop()

movie = movie_system()