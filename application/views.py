import statuses
from flask import render_template, abort, request
from application import app
from .forms import ContactForm
from .models import Category, Post


@app.route('/')
def index():
    posts = Post.query.limit(5)
    context = {
        'posts': posts
    }
    return render_template('core/index.html', **context)


@app.route('/contacts/', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print form
    context = {
        'form': form
    }
    return render_template('core/contacts.html', **context)


@app.route('/categories/')
def categories():
    categories = Category.query.all()
    context = {
        'categories': categories
    }
    return render_template('posts/categories.html', **context)


@app.route('/archive/')
def archive():
    return render_template('core/index.html')


@app.route('/categories/<id>/')
def category_detail(id):
    category = Category.query.filter_by(id=int(id)).first()
    if category is not None:
        posts = category.posts.all()
        context = {
            'posts': posts
        }
        return render_template('posts/category_detail.html', **context)
    abort(statuses.NOT_FOUND)


@app.route('/post/<id>/')
def post_detail(id):
    post = Post.query.filter_by(id=int(id)).first()
    context = {
        'post': post
    }
    return render_template('posts/posts.html', **context)
