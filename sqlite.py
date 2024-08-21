import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

#create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

##INSERT SOME MORE RECORDS
cursor.execute('''Insert Into STUDENT values('Anurag','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',75)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','C',65)''')
cursor.execute('''Insert Into STUDENT values('jab','Data Science','A',98)''')
cursor.execute('''Insert Into STUDENT values('rock','Data Science','A',94)''')

#Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

##commit your changes in the database
connection.commit()
connection.close()
