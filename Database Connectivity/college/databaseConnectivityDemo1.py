######Database Connectivity#######


import sqlite3

conn = sqlite3.connect('test.db')
print("Databse Opened Successfully!")

conn.execute('''CREATE TABLE STUDENT1
        (ID   INT    PRIMARY KEY    NOT NULL,
        NAME        TEXT     NOT NULL,
        AGE    INT     NOT NULL );''')

print("Table created successfully!")

conn.close()



####db browser for sqlite
