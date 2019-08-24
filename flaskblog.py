from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home</h1>"

@app.route('/about')
def about():
	return "<h2>About</h2>"


if __name__ == "__main__":
	app.run(debug=True)