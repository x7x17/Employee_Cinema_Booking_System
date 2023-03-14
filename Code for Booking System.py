
# Dictionary to store movies
#Rather than hard coding we should import by CSV 


import csv

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
    response = input('please key in the ID of the movie: ')
    print(movieDict[response])

a = read_csv("Software Engineering - Movie List.csv")
show_movie(a)
check_showtime(a)