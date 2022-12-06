import sqlite3

conn = sqlite3.connect('db/core.db')
conn.cursor().executescript('db/schema.sql'.read())
#feed sample data into db, will do this later
#    with app.open_resource('prepare.sql', mode='r') as load:
#        db.cursor().executescript(load.read()) 