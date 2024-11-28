import sqlite3

# Connect to SQLite database (or create it if it doesn’t exist)
conn = sqlite3.connect("testdb.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,        -- Auto-increment ID
    username TEXT NOT NULL,        -- Username
    password TEXT NOT NULL         -- Password
)
""")

# Insert sample data into the users table
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup completed!")
