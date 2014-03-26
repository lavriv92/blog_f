from application import db
from datetime import datetime


class Category(db.Model):
    """
    Blog category model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())

    def __unicode__(self):
        return self.title


class Post(db.Model):
    """
    Blog post model.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
                               backref=db.backref('posts', lazy='dynamic'))

    def __unicode__(self):
        return self.title
