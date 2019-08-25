from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a99c515275ef1355c18ff3efc46221ce'

posts = [
	{
		'author': 'Tommy',
		'title': 'Blog Post 1',
		'content': 'First post',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Aatrox',
		'title': 'Blog Post 2',
		'content': '2 post',
		'date_posted': 'April 20, 2018'
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/register')
def register():
	form = RegistrationForm()
	render_template('register.html', title='Register', form=form)


@app.route('/login')
def register():
	form = LoginForm()
	render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
	app.run(debug=True)