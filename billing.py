import sqlite3

# Connect to the database 
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create Billing table
conn.execute('''
    CREATE TABLE IF NOT EXISTS Billing (
        bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subscription_type TEXT NOT NULL,
        start_date DATETIME NOT NULL,
        end_date DATETIME NOT NULL,
        amount REAL NOT NULL
    )
''')
print("Billing table created successfully")

# Function to manage billing and subscriptions
def manage_billing(user_id, subscription_type, start_date, end_date, amount):
    # Insert billing data into the Billing table
    conn.execute('INSERT INTO Billing (user_id, subscription_type, start_date, end_date, amount) VALUES (?, ?, ?, ?, ?)', (user_id, subscription_type, start_date, end_date, amount))
    conn.commit()
    print("Billing information added successfully")

# Function to retrieve billing information by user_id
def get_billing_info(user_id):
    cursor = conn.execute('SELECT * FROM Billing WHERE user_id = ?', (user_id,))
    billing_info = cursor.fetchall()
    return billing_info

# Example usage: Manage billing information and retrieve billing information by user_id
manage_billing(1, 'Premium', '2023-10-01', '2023-11-01', 19.99)
billing_info = get_billing_info(1)
print("Billing information:")
print(billing_info)

# Close the connection
conn.close()
