from flask import Flask, render_template
from post import Post
from datetime import datetime as dt

app = Flask(__name__)
posts = Post()

get_posts = posts.get_posts()
util_data = {
    "title": "My Blog",
    "year": dt.now().year
}

@app.route('/')
def home():  # put application's code here

    return render_template('index.html', posts=get_posts, util_data=util_data)

@app.route('/about')
def about():
    return render_template('about.html', util_data=util_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', util_data=util_data)

@app.route('/post/<id>')
def post(id):
    post = posts.get_post_by_id(id)
    return render_template('post.html', post=post, util_data=util_data)

@app.route('/post/<id>/all')
def all_user_posts(id):
    all_user_posts_data = posts.get_all_user_posts(id)
    return render_template('user_posts.html', posts=all_user_posts_data, util_data=util_data)


if __name__ == '__main__':
    app.run()
