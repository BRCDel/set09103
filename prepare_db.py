import sqlite3

conn = sqlite3.connect('db/core.db')
with app.open_resource('db/schema.sql', mode='r') as f:
    conn.cursor().executescript(f.read())
#feed sample data into db, will do this later
#    with app.open_resource('prepare.sql', mode='r') as load:
#        db.cursor().executescript(load.read()) 