
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