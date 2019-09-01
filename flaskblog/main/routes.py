from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask import Blueprint
from flaskblog.main.forms import SurveyForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	# posts = Post.query.all()
	page = request.args.get('page', 1, type=int)  # passing from URL
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)

@main.route('/about')
def about():
	return render_template('about.html', title='About')



@main.route('/survey', methods=['GET', 'POST'])
def survey():
	form = SurveyForm()
	return render_template('survey.html', title='Survey', form=form, isSurvey=True)


