import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create Files table
conn.execute('''
    CREATE TABLE IF NOT EXISTS Files (
        file_id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_id INTEGER,
        file_name TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
print("Files table created successfully")

# Function to upload a file
def upload_file(folder_id, file_name):
    # Insert file data into the Files table
    conn.execute('INSERT INTO Files (folder_id, file_name) VALUES (?, ?)', (folder_id, file_name))
    conn.commit()
    print("File uploaded successfully")

# Function to retrieve files by folder_id
def get_files_by_folder(folder_id):
    cursor = conn.execute('SELECT * FROM Files WHERE folder_id = ?', (folder_id,))
    files = cursor.fetchall()
    return files

# Example usage: Upload a file and retrieve files by folder_id
upload_file(1, 'example.txt')
files_in_folder = get_files_by_folder(1)
print("Files in folder:")
print(files_in_folder)

# Close the connection
conn.close()
