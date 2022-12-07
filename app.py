import random, configparser, sqlite3
from sqlite3 import Error
from flask import Flask, abort, url_for, request, flash, redirect, render_template, session, g

app = Flask(__name__)
app.secret_key = 'lol,lmao_even'
db_location = "db/core.db"

def init(app):
    config = configparser.ConfigParser()
    conn = connect_db()
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

def create_table(connection, statement):
    try:
        cursor = connection.cursor()
        cursor.execute(statement)
    except Error as e:
        print(e)

@app.route('/')
def home():
    db = connect_db()
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute("SELECT * FROM lists")
    rows = cur.fetchall()
    user_made_parts_lists = []
#    print(type(user_made_parts_lists))
    for row in rows:
#        print("list ID should be: ", row[0])
#        print("list username should be: ", row[1])
        part_list = {
            "id" : int(row[0]),
            "username" : row[1],
            "cpu" : int(row[2]),
            "mobo" : int(row[3]),
            "ram_kit" : int(row[4]),
            "gpu" : int(row[5]),
            "drive" : int(row[6]),
            "psu" : int(row[7]),
            "cooler" : int(row[8]),
            "pc_case" : int(row[9])
        }
        #print(type(list))
        #print(list.values())
        user_made_parts_lists.append(part_list)
#    print(user_made_parts_lists)
#    print(type(user_made_parts_lists))
    for part_list in user_made_parts_lists:
#        print(type(part_list))
#        print(list.values())
#        print(list.keys())
        part_list_keys = list(part_list)
#        print(part_list_keys)
        for i in range(2, 10):
            print(part_list_keys[i])
            query = "SELECT FROM " + part_list_keys[i] + "s WHERE id = " + part_list[i] + ";"
            part_list[i] = cur.execute(query)
#        print(part_list)
    return render_template('index.html', lists=user_made_parts_lists)

@app.route('/404')
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Whatever it is you seek, I do not have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
    init(app)
    app.run(host="0.0.0.0", port=5000)