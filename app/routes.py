from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Evan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Mexico'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Curious to see what the next Gladiator movie is like.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)