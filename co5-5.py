
import csv 
dict_value = [
{"Name":"binoy","Age":19,"Course":"bsc cs"},
{"Name":"joel","Age":19,"Course":"bsc cs"},
{"Name":"gokul","Age":19,"Course":"bsc cs"},
]

fields = ["Name","Age","Course"]

with open('dictconverted.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dictconverted.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
        print(rows)


