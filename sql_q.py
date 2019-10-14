#working with database
#import related liberaries

import sqlite3

import os


try:
    import pandas as pd

except:
    os.system('python -m pip install pandas')
import pandas as pd

#create variable to store an query
query = """
        CREATE TABLE test
        (a VARCHAR(20), b VARCHAR(20),
        c REAL, d INTEGER
        );"""

#create connection
con = sqlite3.connect('mydata.sqlite')
# execute query
con.execute(query)
#
con.commit()

print("New DB with Test table created.")
#
data = [('Atlanta', 'Georgia', 1.25, 6),('Tallahassee', 'Florida', 2.6, 3),('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
print("Values inserted into test table.")
#
cursor = con.execute('select * from test')
rows = cursor.fetchall()
# print(rows)
# print(cursor.description)
# # #
print(pd.DataFrame(rows, columns=[x[0] for x in cursor.description]))
