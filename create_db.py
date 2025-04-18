import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        village TEXT,
        contact TEXT,
        reason TEXT,
        area TEXT,
        time TEXT,
        slot TEXT
    )
''')

conn.commit()
conn.close()
print("✅ Database with 'appointments' table created.")
