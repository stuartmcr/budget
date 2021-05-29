import sqlite3

#create and connect to database
conn = sqlite3.connect('test.db')

#create cursor to execute commands
c = conn.cursor()

#create table to hold info
'''
c.execute("""CREATE TABLE spending (
    month text,
    description text,
    category text,
    amount integer
    )""")
'''

#c.execute("INSERT INTO spending VALUES('January', 'Potbellys', 'Food', 7)")
#conn.commit()

c.execute("SELECT * FROM spending WHERE category='Food'")

print(c.fetchall())

#commits current transaction
conn.commit()

#close connection
conn.close()