import csv
with open("D:\\Python\\python1\\record.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(type(row))
        for val in row:
            print(val)
