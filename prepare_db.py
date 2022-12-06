import sqlite3

conn = sqlite3.connect('db/core.db')
with open('db/schema.sql', mode='r') as script:
    conn.cursor().executescript(script.read())
#feed sample data into db, will do this later
#    with app.open_resource('prepare.sql', mode='r') as load:
#        db.cursor().executescript(load.read()) 