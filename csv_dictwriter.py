#adding records to existing file
import csv
with open("D:\\Python\\python1\\record3.csv",'a+') as fp:
    colname = ["ID", "Name", "city", "age"]  # header name
    record = [{"ID":1, "Name":"smita", "city":"Mumbai", "age":25},
              {"ID":3, "Name":"john", "city":"pune", "age":23},
              {"ID":2, "Name":"ali", "city":"gaon", "age":24}]
    wr = csv.DictWriter(fp,fieldnames=colname)
    wr.writeheader()
    wr.writerow(record)
    print("records added to the  Csv file")