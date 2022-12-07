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
    for row in rows:
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
        user_made_parts_lists.append(part_list)
    for part_list in user_made_parts_lists:
        part_list_keys = list(part_list)
        for x in part_list:
            if x == "id" or x == "username":
                continue
            query = "SELECT part_name FROM " + x + "s WHERE id = " + str(part_list[x]) + ";"
            result = cur.execute(query)
            part_list[x] = result.fetchone()[0]
    return render_template('index.html', lists=user_made_parts_lists)

@app.route("/builder")
def builder():
    return render_template("builder.html")

@app.route('/404')
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Whatever it is you seek, I do not have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
    init(app)
    app.run(host="0.0.0.0", port=5000)