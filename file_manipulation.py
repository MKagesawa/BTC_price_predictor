import csv
import datetime
import numpy as np

# I added a column to the csv file measuring the change in price
f = open('coinbaseUSD.csv')
csv_f = list(csv.reader(f))
first_line = True

for row in csv_f:
    # skip first line
    if first_line:
        first_line = False
        continue
    
    row.pop()
    
    # adding 8 hours to Universal Time to match China Time
    row[0] = int(row[0]) + 28800
    # converting unix time to date time format
    row[0] = datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')
    
    # add a direction column to the end of the row
    # -1 means price went down, 0 means price didn't change, 1 means price went up
    if float(row[-1]) > 0:
        row.append(1)
    elif float(row[-1]) < 0:
        row.append(-1)
    else:
        row.append(0)

f.close()

print(csv_f[:5])