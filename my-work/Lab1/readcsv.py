
# The program that reads in the csv file and outputs each line as a list, calculates the average age

import csv

FILENAME = "data.csv"
DATADIR =  "../Lab1/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",",  quoting=csv.QUOTE_NONNUMERIC)
    
    linecount = 0
    total = 0

    for line in reader:
       if not linecount: 
          # print (f"{line}\n-------------------")
          pass
       else: # all subsequent rows
          # print (line)
          total += int(line[1]) # why 1 (accesses the second column (age) from each row)
       linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1 ? (subtracts 1 from the total count to exclude the header row when calculating the average)