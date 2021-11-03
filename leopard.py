
import csv

class Leopard(object):
    def __init__(self, csvfile):
        c1 = []
        c2 = []
        with open('C:\py\diabetes_data.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                c1.append(row[0])
                c2.append(row[1])

    def get_header(self, csvfile):
        file = open("C:\py\diabetes_data.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()

    def get_dimension(self, csvfile):
        print('rows')


    def count_instances(column_heading, value):
        print('rows')

    def total_missing(self, csvfile):
        print('rows')




    # Remove these lines before you commit the project to Git
    # This line prints everything under the get_header function
    # get_header('self', 'csvfile')
    # This line prints everything under the __init__ function
    # __init__('self', 'csvfile')