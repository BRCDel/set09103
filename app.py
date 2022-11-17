from flask import Flask, abort, url_for, request, flash, redirect, render_template, session
import random, configparser
app = Flask(__name__)
app.secret_key = 'lol,lmao_even'

def init(app):
	config = configparser.ConfigParser()
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
def home()
	return "Home page here"

@app.route('/404')
def force404():
	abort(404)

@app.errorhandler(404)
def page_not_found(error):
	return "Whatever it is you're looking for, I don't have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
	init(app)
	app.run(host="0.0.0.0",port=5000)
