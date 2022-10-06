from flask import Flask, abort
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

@app.route('/404')
def force404():
	abort(404)

@app.errorhandler(404)
def page_not_found(error):
	return "Whatever it is you're looking for, I don't have it.", 404

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
