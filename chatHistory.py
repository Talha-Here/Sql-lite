import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create ChatHistory table
conn.execute('''
    CREATE TABLE IF NOT EXISTS ChatHistory (
        chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        query TEXT NOT NULL,
        token_count INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
print("ChatHistory table created successfully")

# Function to log chat history and token count
def log_chat_history(user_id, query, token_count):
    # Insert chat history data into the ChatHistory table
    conn.execute('INSERT INTO ChatHistory (user_id, query, token_count) VALUES (?, ?, ?)', (user_id, query, token_count))
    conn.commit()
    print("Chat history logged successfully")

# Function to retrieve chat history by user_id
def get_chat_history(user_id):
    cursor = conn.execute('SELECT * FROM ChatHistory WHERE user_id = ?', (user_id,))
    chat_history = cursor.fetchall()
    return chat_history

# Example usage: Log chat history and retrieve chat history by user_id
log_chat_history(1, 'Hello, how can I help you?', 10)
chat_history = get_chat_history(1)
print("Chat history:")
print(chat_history)

# Close the connection
conn.close()
