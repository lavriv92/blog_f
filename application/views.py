from flask import render_template
from application import app
from models import Category, Post


@app.route('/')
def index():
    categories = Category.query.all()
    context = {
        'categories': categories
    }
    return render_template('core/index.html', **context)


@app.route('/categories')
def categories():
    categories = Category.query.all()
    context = {
        'categories': categories
    }
    return render_template('categories.html', **context)


@app.route('/posts')
def posts():
    posts = Post.query.all().limit(5)
    context = {
        'posts': posts
    }
    return render_template('posts/posts.html', **context)
