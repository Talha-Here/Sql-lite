import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create UserTokens table
conn.execute('''
    CREATE TABLE IF NOT EXISTS UserTokens (
        token_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        token_file TEXT NOT NULL,
        expires_at DATETIME
    )
''')
print("UserTokens table created successfully")

# Function to manage user's token files
def manage_user_tokens(user_id, token_file, expires_at):
    # Insert token data into the UserTokens table
    conn.execute('INSERT INTO UserTokens (user_id, token_file, expires_at) VALUES (?, ?, ?)', (user_id, token_file, expires_at))
    conn.commit()
    print("Token file added successfully")

# Function to retrieve user's token files by user_id
def get_user_tokens(user_id):
    cursor = conn.execute('SELECT * FROM UserTokens WHERE user_id = ?', (user_id,))
    tokens = cursor.fetchall()
    return tokens

# Example usage: Manage user's token files and retrieve tokens by user_id
manage_user_tokens(1, 'user_token123', '2023-12-31 23:59:59')
user_tokens = get_user_tokens(1)
print("User's token files:")
print(user_tokens)

# Close the connection
conn.close()
