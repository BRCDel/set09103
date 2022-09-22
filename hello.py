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

