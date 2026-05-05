#James Moore
#SDEV220-50P
#Module 4 Programming Assignment - Modules and Databases

# 11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'. 
# Then, use the interactive interpreter to import the zoo module and call its hours() function.

import zoo
zoo.hours()

#11.2 In the interactive interpreter, 
# import the zoo module as menagerie and call its hours() function.

import zoo as menagerie
menagerie.hours()

#16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. 
# As in 16.6, select and print the title column from the book table in alphabetical order.

import sqlalchemy

# Connect to the database
engine = sqlalchemy.create_engine('sqlite:///books.db')
conn = engine.connect()

# Select the title column and order by title
query = sqlalchemy.text("SELECT title FROM book ORDER BY title ASC")
rows = conn.execute(query)

# Print the results
for row in rows:
    print(row.title)

conn.close()