from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Leah'}
	posts = [
		{ 
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!' 
		},
		{ 
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for {}'.format(form.openid.data))
		return redirect('/index')
	else:
		return render_template('login.html', title='Sign In', form=form)
