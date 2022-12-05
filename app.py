import random, configparser, sqlite3
from sqlite3 import Error
from flask import Flask, abort, url_for, request, flash, redirect, render_template, session, g
from datastore import init_db

app = Flask(__name__)
app.secret_key = 'lol,lmao_even'
db_location = "db/core.db"

#bless sqlitetutorial,net if this works
def connect_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db=db
    return db

@app.teardown_appcontext
def disconnect_db(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

#def init_db():
#    with app.app_context():
#        db = get_db()
#        with app.open_resource('schema.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit

def create_table(connection, statement):
    try:
        cursor = connection.cursor()
        cursor.execute(statement)
    except Error as e:
        print(e)

def init(app):
    config = configparser.ConfigParser()
    conn = connect_db("db/core.db")
    lists_table_statement="""CREATE TABLE lists ( id integer PRIMARY KEY, username text NOT NULL, json TEXT NOT NULL )"""
    create_table(conn, lists_table_statement)

    try:
        config_location = 'etc/defaults.cfg'
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print("Couldn't read configs from etc/defaults.default_settings")

init(app)

@app.route('/')
def home():
    db = get_db()
#feed sample data into db, will do this later
#    with app.open_resource('prepare.sql', mode='r') as load:
#        db.cursor().executescript(load.read())
    return render_template('index.html')

@app.route('/404')
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Whatever it is you seek, I do not have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
    init(app)
    init_db()
    app.run(host="0.0.0.0", port=5000)