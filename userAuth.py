import sqlite3
import bcrypt

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

# #Create a cursor
# c = conn.cursor()

# Create Users table
conn.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )
''')
print("Table created successfully")

# Function to register a new user
def register_user(username, email, password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Insert user data into the Users table
    conn.execute('INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)', (username, email, hashed_password))
    conn.commit()

# Function to authenticate a user
def authenticate_user(username, password):
    cursor = conn.execute('SELECT password_hash FROM Users WHERE username = ?', (username,))
    row = cursor.fetchone()
    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        return True
    else:
        return False


# Example: Register a new user and authenticate
register_user('talha_khan', 'talha@example.com', 'secretpassword')
authenticated = authenticate_user('talha_khan', 'secretpassword')

if authenticated:
    print("Authentication successful")
else:
    print("Authentication failed")

#Commit 
conn.commit()

# Close the connection
conn.close()