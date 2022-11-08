from flask import Flask, abort, url_for, request, session, render_template
import random, configparser
app = Flask(__name__)

def init(app):
	config = configparser.ConfigParser()
	try:
		config_location = 'etc/defaults.cfg'
		config.read(config_location)

		app.config['DEBUG'] = config.get("config", "debug")
		app.config['ip_address'] = config.get("config", "ip_address")
		app.config['port'] = config.get("config", "port")
		app.config["url"] = config.get("config", "url")
	except:
		print("Couldn't read configs from: ", config_location)

@app.route('/')
def home():
	x = random.randint(1,100)
	return "Here's a random number: "+str(x)

@app.route('/config/')
def config():
	s = []
	s.append('Config info follows')
	s.append('debug: '+str(app.config['DEBUG']))
	s.append('port: '+str(app.config['port']))
	s.append('url: '+str(app.config["url"]))
	s.append('ip_address: '+str(app.config['ip_address']))
	return ', '.join(s)

@app.route('/inherits/')
def inherits():
	return render_template('base.html')

@app.route('/inherits/one')
def inherits_one():
	return render_template('extension.html')

@app.route('/inherits/two')
def inherits_two():
	return render_template('second_extension.html')

@app.route('/users')
def users():
	names = ['del', 'v', 'david', 'maine', 'rebb']
	return render_template('users.html', names=names)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/static/vmask')
def static_example_img():
	start = '<img src="'
	url = url_for("static", filename="vmask.jpg")
	end = '">'
	return start+url+end, 200

@app.route("/account", methods=['GET', 'POST'])
def account():
	if request.method == 'POST':
		print(request.form)
		name = request.form['name']
		return "Hello %s" % name
	else:
		page = '''
		<html><body>
			<form action="" method="post" name="form">
				<label form="name">Name:</label>
				<input type="text" name="name" id="name"/>
				<input type="submit" name="submit" id="submit"/>
			</form>
		</body></html>'''
		return page

@app.route("/account/<name>")
def accountName(name):
	return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first,second):
	return str(first+second)

@app.route('/404')
def force404():
	abort(404)

@app.errorhandler(404)
def page_not_found(error):
	return "Whatever it is you're looking for, I don't have it. (Error 404: Not Found)", 404

if __name__ == "__main__":
	session = {}
	init(app)
	app.run(
		host=app.config['ip_address'], 
		debug=app.config['DEBUG'],
		port = int(app.config['port'])
	)
