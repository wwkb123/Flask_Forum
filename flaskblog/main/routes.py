from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask import Blueprint
from flaskblog.main.forms import SurveyForm
from scraper import scrape

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html', title='About', yt_video_ids=scrape("pokemon"))

@main.route('/about')
def about():
	return render_template('about.html', title='About')



@main.route('/survey', methods=['GET', 'POST'])
def survey():
	form = SurveyForm()
	return render_template('survey.html', title='Survey', form=form)


@main.route('/forum')
def forum():
	# posts = Post.query.all()
	page = request.args.get('page', 1, type=int)  # passing from URL
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('forum.html', posts=posts, enableSidebar=True)


@main.route('/admin')
def admin():
	return render_template('admin.html', title='ADMIN')