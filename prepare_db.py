import sqlite3

with open('db/schema.sql', mode='r') as schema:
    script = schema.read()
conn = sqlite3.connect('db/core.db')
conn.cursor().executescript(script)
conn.commit()
conn.close()