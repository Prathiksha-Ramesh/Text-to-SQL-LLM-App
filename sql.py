import sqlite3 
#connect to sqlite

connection=sqlite3.connect('student.db')
#create a cursor:

cursor=connection.cursor()
#create a table
table_info='''
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
'''
cursor.execute(table_info)
#Insert some more records:
cursor.execute('''Insert Into STUDENT values('Krish','Data science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Prathiksha','Data science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Sagarisha','Data science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Ramesh','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('sumathi','DEVOPS','A',35)''')

#display the all the records:

print('The inserted records are')
data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()