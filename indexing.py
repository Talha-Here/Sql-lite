import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create Indexing table
conn.execute('''
    CREATE TABLE IF NOT EXISTS Indexing (
        index_id INTEGER PRIMARY KEY AUTOINCREMENT,
        index_name TEXT NOT NULL,
        details TEXT
    )
''')
print("Indexing table created successfully")

# Function to store index_name Todo
def store_index_name(index_name, details):
    # Insert index data into the Indexing table
    conn.execute('INSERT INTO Indexing (index_name, details) VALUES (?, ?)', (index_name, details))
    conn.commit()
    print("Index name stored successfully")

# Function to retrieve index details by index_name
def get_index_details(index_name):
    cursor = conn.execute('SELECT * FROM Indexing WHERE index_name = ?', (index_name,))
    index_details = cursor.fetchone()
    return index_details

# Example usage: Store index_name Todo and retrieve details by index_name
store_index_name('Todo', 'Details about the Todo index')
index_details = get_index_details('Todo')
print("Index details:")
print(index_details)

# Close the connection
conn.close()
