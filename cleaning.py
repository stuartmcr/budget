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

outfile = open('2020_cleaned.csv', 'w')
with open('raw_data/2020_data.csv', 'r') as csv_2020:
    reader_2020 = csv.reader(csv_2020, delimiter=',')
    header = next(reader_2020)

    for row in reader_2020:
        date = row[0]
        description = row[1]
        category = row[2]
        amount = row[3]

        line = '{},{},{},{}\n'.format(date, description, category, amount)
        outfile.write(line)
outfile.close()