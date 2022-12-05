from datastore import init_db
import sqlite3

init_db()
#feed sample data into db, will do this later
#    with app.open_resource('prepare.sql', mode='r') as load:
#        db.cursor().executescript(load.read())