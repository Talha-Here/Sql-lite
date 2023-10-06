import sqlite3
import bcrypt

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

#Create a cursor
c = conn.cursor()

# Query Database
c.execute("SELECT * FROM Billing")
print(c.fetchall())

# Commit command
conn.commit()
# Close connection
conn.close()