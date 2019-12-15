import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database succesfully!")

cursor=conn.execute("SELECT name,password from STUDENT1")
#cursor=conn.execute("SELECT * from STUDENT1")

for row in cursor:
    print("NAME=",row[0])
    print("PASSWORD=",row[1],"\n")

print("Operation done successfully!")
conn.close()



#cursor=conn.execute("SELECT * from STUDENT1 where id=1")
#cursor=conn.execute("SELECT name,password from STUDENT1 where id=1")
#cursor=conn.execute("SELECT disctint name from STUDENT1") #displays one distinct name
#cursor=conn.execute("UPDATE STUDENT1 set NAME='Devvrat'")
