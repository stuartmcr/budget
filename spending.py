# pull in csv data with transactions

import csv

# 0: Date
# 1: Description
# 2: Category
# 3: Amount
# 4: Note
# 5: Account
# 6: Account #
# 7: Institution
# 8: Full Description
# 9: Check Number
# 10: Month
# 11: Week
# 12: Transaction ID
# 13: Date Added

print("---spending analysis---")

with open('2018_data.csv', 'r') as csv_2018_Data:
    csv_reader = csv.reader(csv_2018_Data)

    next(csv_reader) # removes header row

    for line in csv_reader:
        print(line[3])