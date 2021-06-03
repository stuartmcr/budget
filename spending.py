import sqlite3
from transaction import Transaction

# create and connect to database
# connect to ':memory:' instead of .db for a fresh memory instance database (good for testing)
conn = sqlite3.connect(':memory:')

# create cursor to execute commands
c = conn.cursor()

#create table to hold info
c.execute("""CREATE TABLE spending (
    month text,
    description text,
    category text,
    amount integer
    )""")

# added context manager 'with conn:', not needed for 'get' function
def insert_expense(exp):
    with conn:
        c.execute("INSERT INTO spending VALUES(:month, :description, :category, :amount)", {'month': exp.month, 'description': exp.description, 'category': exp.category, 'amount': exp.amount})

def get_expense_by_type(category_type):
    c.execute("SELECT * FROM spending WHERE category=:category", {'category': category_type})
    return c.fetchall()

def update_cost(exp, amount):
    with conn:
        c.execute("""Update spending SET amount = :amount WHERE month = :month AND category = :category""", {'month': exp.month, 'category': exp.category, 'amount': amount})

def remove_expense(exp):
    with conn:
        c.execute("""DELETE from spending WHERE month = :month AND category = :category""", {'month': exp.month, 'category':exp.category})

# Transaction: Month, Description, Category, Amount
exp_1 = Transaction('March', 'Pizza', 'Food', 12)
exp_2 = Transaction('March', 'Fifa Game', 'Hobbies', 60)

# Add expenses
insert_expense(exp_1)
insert_expense(exp_2)

# Display by category
expenses = get_expense_by_type('Food')
print(expenses)

# Edit expense amount and remove another
update_cost(exp_1, 9)
remove_expense(exp_2)

# Display updated value
expenses = get_expense_by_type('Food')
print(expenses)

# close connection
conn.close()