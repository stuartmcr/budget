import csv

""" spending categories:

---NECESSARY---
1.) Groceries
2.) Rent
3.) Utilities
4.) Transportation
5.) Medical
6.) Education
7.) Phone
8.) Piper (dog)

---DISCRETIONARY---
1.) Restaurants
2.) Drinks
3.) Holidays
4.) Fitness
5.) Hobbies
6.) Clothes
7.) Home Improvements
8.) Subscriptions
9.) Gifts
10.) Extra

"""


with open('2018.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter = ',')

    grocery_spending = 0.0
    for row in reader:
        if row[2] == 'Groceries':
            grocery_spending = grocery_spending + float(row[3])

print(grocery_spending)