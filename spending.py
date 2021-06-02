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

insert_expense(exp_1)
insert_expense(exp_2)

expenses = get_expense_by_type('Food')
print(expenses)

update_cost(exp_1, 9)
remove_expense(exp_2)

expenses = get_expense_by_type('Food')
print(expenses)

conn.close()

# c.execute("INSERT INTO spending VALUES(?, ?, ?, ?)", (exp_1.month, exp_1.description, exp_1.category, exp_1.amount))
# conn.commit()

# c.execute("INSERT INTO spending VALUES(:month, :description, :category, :amount)", {'month': exp_2.month, 'description': exp_2.description, 'category': exp_2.category, 'amount': exp_2.amount})
# conn.commit()

# c.execute("SELECT * FROM spending WHERE category=?", ('Food',))
# print(c.fetchall())

# c.execute("SELECT * FROM spending WHERE category=:category", {'category': 'Hobbies'})
# print(c.fetchall())

# commits current transaction
# conn.commit()

# close connection
# conn.close()