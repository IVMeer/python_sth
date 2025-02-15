from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def inde():
    return "Index Page"

@app.route('/hello')
def hello_world():
    return "Hello world"

@app.route("/<name>")
def helle(name):
    return f"Hello, {escape(name)}"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User{escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'