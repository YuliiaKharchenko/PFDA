
# The program that reads in the csv file as Dictionary, calculates the average age

import csv

FILENAME = "data.csv"
DATADIR =  "../Lab1/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        # print (line)
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time? (DictReader automatically skips 
                                          # the header and reads the remaining lines as dictionaries, 
                                          # so the header isn't counted.)
