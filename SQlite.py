from fastapi import FastAPI
import sqlite3 

# SQLite is a lightweight, disk-based database that doesn’t require a separate server process.
#  It allows access to the database using a nonstandard variant of the SQL query language.

app = FastAPI()

conn = sqlite3.connect('example.db')

conn = sqlite3.connect('example.db', check_same_thread=False)  # Allow usage in multiple threads

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE
)
""")

conn.commit()



@app.get("/")
def user():
    return {"message": "Welcome to the FastAPI application!"}