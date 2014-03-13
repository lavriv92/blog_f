from flask import render_template
from application import app, db
from models import Category, Post


@app.route('/')
def index():
    categories = Category.query.all()
    print categories
    return render_template('core/index.html')
