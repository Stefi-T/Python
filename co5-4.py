
import csv

with open("dict.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])
