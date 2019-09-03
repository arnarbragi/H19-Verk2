from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Halló Heimur</h1></h1><a href="/skoli">Skóli </a><a href="/vinna">Vinna </a>'

@app.route('/skoli')
def sida1():
	return '<h1>Skóli </h1><a href="/">Heim </a><a href="/vinna">Vinna </a>'

@app.route('/vinna')
def sida2():
	return '<h1>Vinna </h1><a href="/">Heim </a><a href="/skoli">Skóli </a>'

if __name__ == "__main__":
	app.run(debug=True)