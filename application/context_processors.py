from application import app
from models import Category


@app.context_processor
def inject_categories():
    categories = Category.query.all()
    print categories
    return {
        'categories': categories
    }
