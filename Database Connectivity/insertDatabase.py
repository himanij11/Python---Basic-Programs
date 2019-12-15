import sqlite3

conn = sqlite3.connect('test.db')
print("Database created successfully!")

conn.execute("INSERT INTO STUDENT1 (ID,NAME, AGE) VALUES (1,'HIMANI', 20)");
conn.execute("INSERT INTO STUDENT1 (ID,NAME, AGE) VALUES (2,'DEVVRAT', 20)");

#conn.execute("DELETE FROM STUDENT1")
conn.commit()
print("Records entered successfully!")
conn.close()
