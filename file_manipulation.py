import csv
import datetime

f = open('coinbaseUSD.csv')
csv_f = csv.reader(f)
first_line = True


for row in csv_f:
    # skip first line
    if first_line:
        first_line = False
        continue
    # adding 8 hours to Universal Time to match China Time
    row[0] = int(row[0]) + 28800
    # converting unix time to date time format
    row[0] = datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')
    print(row)
