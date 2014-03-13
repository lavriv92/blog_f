from application import db
from datetime import datetime


class Category(db.Model):
    """
    Blog category model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created = db.Column(db.DateTime)

    def __init__(self, title, created=None):
        self.title = title
        if created is None:
            created = datetime.now()
        self.created = created

    def __repr__(self):
        return '<Category %s>' % self.title


class Post(db.Model):
    """
    Blog post model.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
                               backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, content, created=None):
        self.title = title
        self.content = content
        if created is None:
            created = datetime.now()
        self.created = created

    def __repr__(self):
        return '<Post %s>' % self.title
