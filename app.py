import random, configparser, sqlite3
from sqlite3 import Error
from flask import Flask, abort, url_for, request, flash, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'lol,lmao_even'

#bless sqlitetutorial,net if this works
def connect_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(connection, statement):
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
    except Error as e:
        print(e)

def init(app):
    config = configparser.ConfigParser()
    connect_db(r"db/core.db")
    lists_table_statement="""CREATE TABLE IF NOT EXISTS lists ( id integer PRIMARY KEY, username text NOT NULL, json TEXT NOT NULL )"""
    create_table(lists_table_statement)
    try:
        print("INIT FUNCTION")
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
    return "Home page here"

@app.route('/404')
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Whatever it is you seek, I do not have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
    init(app)
    app.run(host="0.0.0.0", port=5000)