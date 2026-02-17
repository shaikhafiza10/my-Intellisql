import sqlite3

# create/connect database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# create table
table = '''
CREATE TABLE IF NOT EXISTS STUDENTS(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    MARKS INT,
    COMPANY VARCHAR(25)
);
'''
cursor.execute(table)

# insert sample records
cursor.execute("INSERT INTO STUDENTS VALUES('Sijo','BTech',75,'JSW')")
cursor.execute("INSERT INTO STUDENTS VALUES('Anu','MCom',82,'INFOSYS')")
cursor.execute("INSERT INTO STUDENTS VALUES('Rahul','BSc',65,'TCS')")
cursor.execute("INSERT INTO STUDENTS VALUES('Meena','MCom',90,'WIPRO')")

connection.commit()
connection.close()





