import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database succesfully!")

cursor=conn.execute("UPDATE STUDENT1 set NAME='Devvrat'")
conn.commit
print("Total number of rows updated:",conn.total_changes)

cursor=conn.execute("SELECT name,password from STUDENT1")
for row in cursor:
    print("NAME=",row[0])
    print("PASSWORD=",row[1],"\n")

print("Operation done successfully!")
conn.close()

