import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create VectorDB table
conn.execute('''
    CREATE TABLE IF NOT EXISTS VectorDB (
        metadata_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vector_id INTEGER,
        metadata_json TEXT NOT NULL
    )
''')
print("VectorDB table created successfully")

# Function to store vector database metadata
def store_vector_metadata(vector_id, metadata_json):
    # Insert metadata into the VectorDB table
    conn.execute('INSERT INTO VectorDB (vector_id, metadata_json) VALUES (?, ?)', (vector_id, metadata_json))
    conn.commit()
    print("Vector database metadata stored successfully")

# Function to retrieve metadata by vector_id
def get_vector_metadata(vector_id):
    cursor = conn.execute('SELECT * FROM VectorDB WHERE vector_id = ?', (vector_id,))
    metadata = cursor.fetchone()
    return metadata

# Example usage: Store vector database metadata and retrieve metadata by vector_id
store_vector_metadata(1, '{"key": "value", "description": "Metadata for vector 1"}')
vector_metadata = get_vector_metadata(1)
print("Vector database metadata:")
print(vector_metadata)

# Close the connection
conn.close()
