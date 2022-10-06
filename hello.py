from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello():
	x =  random.randint(1,100)
	if x % 2 == 0:
		return 'even'
	else:
		return 'odd'
	return 'done'

@app.errorhandler(404)
def page_not_found(error):
	return "Whatever it is you're looking for, I don't have it.", 404
