
# Dictionary to store movies
#Rather than hard coding we should import by CSV 

import csv


#Function to read csv file and place values which are in more than one column into a list
def new_dict1(name):
    dict1 = {}
    
    with open(name, mode="r") as doc:
        for row in csv.reader(doc):
            nlist = []
            for x in row:
            
                if x != '':
                    nlist.append(x)
            
            for i in nlist:
                dict1[nlist[0].upper()] = nlist[1:]

    return dict1


movieTitles = new_dict1('Software Engineering - Movie List.csv')





'''
movieTitles = {'A Fist Full of Dollar': [15, '1h 39m', 6], 
              'Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan': [15, '1h 24m', 6]
              
             
              
               }

'''






print(movieTitles)

#TKinter GUI for Booking Confirmation Screen
